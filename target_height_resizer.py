import maya.cmds as cmds


def resize_to_target_height(target_height):
    selection = cmds.ls(selection=True)

    if not selection:
        cmds.warning("Please select an object or group first.")
        return

    if target_height <= 0:
        cmds.warning("Target height must be greater than zero.")
        return

    for obj in selection:
        # Get exact world-space bounding box [xmin, ymin, zmin, xmax, ymax, zmax]
        bbox = cmds.xform(obj, query=True, boundingBox=True, worldSpace=True)

        current_height = bbox[4] - bbox[1]  # ymax - ymin

        if current_height <= 0.0001:
            cmds.warning(
                f"Skipping '{obj}': Object height is too close to zero."
            )
            continue

        # Calculate exact uniform multiplier required
        scale_factor = target_height / current_height

        # Get current local scale values
        current_scale = cmds.xform(obj, query=True, scale=True, relative=True)

        # Multiply existing scale by scale factor to maintain scale state
        new_scale = [s * scale_factor for s in current_scale]

        # Apply uniform scaling across X, Y, Z
        cmds.xform(obj, scale=new_scale, relative=False)

    cmds.inViewMessage(
        amg=f"<col=00FF00>Resized selection to {target_height}m tall</col>",
        pos="topCenter",
        fade=True,
    )


def build_size_tool_ui():
    window_name = "TargetSizeToolWin"

    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name)

    window = cmds.window(
        window_name,
        title="Target Height Resizer",
        widthHeight=(300, 100),
        sizeable=False,
    )

    cmds.columnLayout(
        adjustableColumn=True, rowSpacing=10, columnOffset=["both", 15]
    )
    cmds.separator(height=10, style="none")

    height_field = cmds.floatFieldGrp(
        numberOfFields=1,
        label="Target Height (Y): ",
        value1=1.0,
        columnWidth2=[110, 150],
    )

    def on_click_apply(*args):
        val = cmds.floatFieldGrp(height_field, query=True, value1=True)
        resize_to_target_height(val)

    cmds.button(
        label="Apply Target Height",
        command=on_click_apply,
        height=35,
        backgroundColor=[0.2, 0.5, 0.3],
    )
    cmds.separator(height=5, style="none")

    cmds.showWindow(window)


# Launch UI
build_size_tool_ui()