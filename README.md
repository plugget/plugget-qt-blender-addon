# plugget qt addon
A simple add-on to add a [plugget qt](https://github.com/plugget/plugget-qt) launcher to the Blender menu `Window/Plugget Qt Manager` <br>
There's no actual code in the add-on. It just runs
```python
import plugget_search_widget
plugget_search_widget.show()
```

If you already have an add-on or script, to manage your menu and tools, you can skip this add-on and launch the widget with above code.
(I recommend the menu manager [unimenu](https://github.com/hannesdelbeke/unimenu_addon))

![image](https://github.com/plugget/plugget-qt-addon/assets/3758308/f8322473-0071-46d7-86bc-165f42dfd24b)

## install

### Plugget install
TODO

### Manual install
- Download and extract this repo.
- Add the `plugget_qt_addon` folder (not `plugget-qt-addon` ⚠️) to your add-ons folder#
- Ensure you have the dependencies installed.
- Enable the addon, it should now show in your Blender menu `Window/Plugget Qt Manager`
