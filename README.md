# Maya Target Height Resizer

A small Maya Python tool to scale a model or group to a specific height ($Y$-axis) without distorting its $X$ and $Z$ proportions. Useful for fixing scale drift when prepping models for game engines.

Works on frozen or unfrozen transforms because it reads world bounding box values instead of scale channels.

## How to use

1. Open Maya's Script Editor (`Windows > General Editors > Script Editor`).
2. Paste `target_height_resizer.py` into a Python tab.
3. Highlight the code and drag it to your Shelf using the Middle Mouse Button.
4. (Optional) Set the button icon to `icons/icon_resize.png`.

Clicking the shelf button opens a small popup window. Enter your desired height in scene units (metres) and hit Apply.

## Compatibility

Tested on Maya 2022+ (Python 3) on macOS and Windows.
