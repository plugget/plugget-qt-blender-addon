"""
to create an installer blend file:
- create a new blend file
- copy this code in the text editor
- in text editor menu: toggle Text/Register
- save the blend file.
on opening the blend file, the addon will be installed and enabled.
"""

import os
import urllib.request
import shutil
import tempfile
import bpy
from pathlib import Path


# TODO, pip install plugget
# use plugget to install plugget-qt-addon

# Define the URL of the repo and the file to be downloaded
# Download the repo and save it as a zip file
url = "https://github.com/hannesdelbeke/plugget-qt-addon/archive/refs/heads/main.zip"
filename = "main.zip"
urllib.request.urlretrieve(url, filename)

# Define the path to the addon folder
local_script_dir = bpy.utils.script_path_user()
local_addons_dir = Path(local_script_dir) / "addons"
# TODO, this doesn't install any dependencies !

# Extract the contents of the zip file to a temporary folder
with tempfile.TemporaryDirectory() as tmpdir:
    shutil.unpack_archive(filename, tmpdir)

    # Move the plugget_addon.py file to the addon folder
    source_path = os.path.join(tmpdir, "plugget-qt-addon-main", "plugget_qt_addon")
    target_path = os.path.join(local_addons_dir, "plugget_qt_addon")
    shutil.move(source_path, target_path)

# Enable the addon in Blender
import bpy

bpy.ops.preferences.addon_enable(module="plugget_qt_addon")

# Refresh all addons
bpy.ops.preferences.addon_refresh()
