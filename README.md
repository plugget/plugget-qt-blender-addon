# Plugget Qt Blender addon
A Blender add-on that adds [plugget qt](https://github.com/plugget/plugget-qt) to the menu: `Window/Plugget Qt Manager`, and offers an easy installer for [plugget](https://github.com/plugget/plugget) in Blender    


![image](https://github.com/plugget/plugget-qt-addon/assets/3758308/0752c140-5b26-452e-81ac-fc4e36ccdb23)<br>
_Dark ui is auto applied in Blender due to the qt stylesheet_


## Use
- type in the search box and press enter to search packages on the web
- click list to see all installed packages
- select a version in the dropdown, and click install, to install that version
- click uninstall to uninstall a package


## Installation

#### Blender install script (recommended)
- open the script editor & run this code
```python
# ===================== install plugget =================================
from pip._vendor import requests
import zipfile
import os
import io
import shutil
import tempfile
import bpy
from pathlib import Path
import sys

def download_github_repo(repo_url, extract_to):
    # Construct the URL to the zip file
    if repo_url.endswith('/'):
        repo_url = repo_url[:-1]
    zip_url = f"{repo_url}/archive/refs/heads/main.zip"

    # Send a request to the URL
    response = requests.get(zip_url)
    if response.status_code == 200:
        print(f"Successfully downloaded {zip_url}")
    else:
        print(f"Failed to download {zip_url}")
        return

    with tempfile.TemporaryDirectory() as temp_dir:
        # Extract the content of the zip file to the temporary directory
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
            zip_file.extractall(path=temp_dir)
            print(f"Repository extracted to temporary directory {temp_dir}")

        extracted_folder_name = os.path.join(temp_dir, "plugget-main")
        plugget_folder_path = os.path.join(extracted_folder_name, "plugget")

        # Move 'plugget' directory to the final destination
        final_destination_path = os.path.join(extract_to, "plugget")
        if os.path.exists(final_destination_path):
            shutil.rmtree(final_destination_path)  # Remove if exists
        else:
            # create parent folder if it doesn't exist
            Path(final_destination_path).parent.mkdir(parents=True, exist_ok=True)
            
        shutil.move(plugget_folder_path, extract_to)
        print(f"Moved 'plugget' to {final_destination_path}")
        
        # add to path, since some apps dont do this by default
        sys.path.append(extract_to)

default_target_path = str(Path(str(bpy.utils.script_path_user())) / "modules")
repo_url = "https://github.com/plugget/plugget"
try:
    import plugget
except ImportError:
    download_github_repo(repo_url, default_target_path)

# ===================== install dependencies =================================
import plugget._utils  
plugget._utils.install_plugget_dependencies(app="blender")

# ===================== install plugget addon =================================
plugget.install("bqt")
plugget.install("plugget-qt-addon")
```

#### Blender install file (recommended)
- Download [installer-blender-2.93.blend](https://github.com/plugget/plugget-qt-addon/raw/main/installer/installer-blender-2.93.blend)
- Open this Blend file
- On startup, blender ask if you want to run the script in the blend file, click `allow`.
- This will install plugget qt addon and dependencies automatically
- If all goes well it will install and open plugget-qt when finished.

You can also run the script yourself instead:
- copy the code from the [installer.py](https://github.com/plugget/plugget-qt-addon/blob/main/installer/install_script.py)
- in Blender, go to the scripting tab, click new script, paste the copied code
- run the script. This installs & enables the addon, and opens the Qt Window at the end.

<details>
<summary><h3>Other installation methods</h3></summary>

#### Plugget install
If you already have plugget installed, you can plugget-install this addon by name `plugget-qt-addon`
```python
import plugget
plugget.install("plugget-qt-addon")
```

#### Manual install
- Download and extract this repo.
- Add the `plugget_qt_addon` folder (not `plugget-qt-addon` ⚠️) to your add-ons folder#
- Ensure you have the dependencies installed.  
There's a button in the add-on's preferences to install the `plugget-qt` dependency.
- Enable the addon, it should now show in your Blender menu `Window/Plugget Qt Manager`

#### local editable install
Great for development.  
1. Install the add-on without dependencies to addon folder
- `pip install --target "%appdata%\Blender Foundation\Blender\3.2\scripts\addons" --editable "path/to/repo" --no-dependencies --no-user`
2. Install the plugget-qt pip dependency to the modules folder
- `pip install plugget-qt -target "%appdata%\Blender Foundation\Blender\3.2\scripts\modules" --no-user`
3. start blender, and on every startup you need to add the modules path to site packages.
```python
import site, os
blender_scripts_path = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Blender Foundation", "Blender", "3.2", "scripts", "addons")  # Windows OS example
site.addsitedir(blender_scripts_path)
```

</details>



---

### requirements
- [plugget qt](https://github.com/plugget/plugget-qt) ofcourse
  - [plugget](https://github.com/plugget/plugget)
  - [PySide2](https://pypi.org/project/PySide2/)
- (may i suggest [bqt](https://github.com/techartorg/bqt/))

### custom menu
The add-on launches plugget_qt like this:
```python
import plugget_qt
plugget_qt.show()
```
If you already have an add-on or script, to manage your menu and tools, you can skip this add-on and launch the widget with above code.
(I recommend the menu manager [unimenu](https://github.com/hannesdelbeke/unimenu_addon))

### support
- PRs and bugreports are welcome
- If this tool is helpfull, you can ⭐ star it on the github page,
just click the ⭐ star button in the top-right of this page.
