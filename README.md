# plugget qt addon
A simple add-on to add a [plugget qt](https://github.com/plugget/plugget-qt) launcher to the Blender menu `Window/Plugget Qt Manager` <br>
There's no actual code in the add-on. It just runs
```python
import plugget_qt
plugget_qt.show()
```

If you already have an add-on or script, to manage your menu and tools, you can skip this add-on and launch the widget with above code.
(I recommend the menu manager [unimenu](https://github.com/hannesdelbeke/unimenu_addon))

![image](https://github.com/plugget/plugget-qt-addon/assets/3758308/0752c140-5b26-452e-81ac-fc4e36ccdb23)<br>
_Dark ui is auto applied in Blender due to the qt stylesheet_

## Use
- type in the search box and press enter to search packages on the web
- click list to see all installed packages
- select a version in the dropdown, and click install, to install that version
- click uninstall to uninstall a package

## install

### Plugget install
TODO

### Manual install
- Download and extract this repo.
- Add the `plugget_qt_addon` folder (not `plugget-qt-addon` ⚠️) to your add-ons folder#
- Ensure you have the dependencies installed.
- Enable the addon, it should now show in your Blender menu `Window/Plugget Qt Manager`


### requirements
- [plugget qt](https://github.com/plugget/plugget-qt) ofcourse
  - [plugget](https://github.com/plugget/plugget)
  - [PySide2](https://pypi.org/project/PySide2/)
- (may i suggest [bqt](https://github.com/techartorg/bqt/))

### support
- PRs and bugreports are welcome
- If this tool is helpfull, you can ⭐ star it on the github page,
just click the ⭐ star button in the top-right of this page.
