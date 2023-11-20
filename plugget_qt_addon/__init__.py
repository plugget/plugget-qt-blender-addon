bl_info = {
    "name": "Plugget Qt Package Manager",
    "description": "Manage Plugget packages",
    "author": "Hannes Delbeke",
    "version": (0, 1, 0),
    "blender": (2, 91, 0),
    "category": "Development",
}

import bpy
import subprocess
import sys
from pathlib import Path


user_scripts_path = Path(bpy.utils.script_path_user())
pth_path = user_scripts_path / "modules"
sys.path.append(str(pth_path))  # in case the folder doesnt exist and Blender is already running
print(f"adding '{pth_path}' to sys.path")

def plugget_qt_installed():
    try:
        import plugget_qt
        return True
    except ImportError:
        return False
    

class OpenPluggetQt(bpy.types.Operator):
    """Open the Plugget Qt Manager window"""
    bl_idname = "plugget.show_qt_manager"
    bl_label = "Plugget Qt Manager"
    widget = None

    def execute(self, context):
        try:
            import plugget_qt
            self.widget = plugget_qt.show()  # store ref to prevent garbage collect
            return {'RUNNING_MODAL'}  # MODAL keeps operator alive to prevent instant garbage collection
        except ImportError:
            self.report({'ERROR'}, "plugget-qt module is not installed. Please install it.")
            return {'CANCELLED'}


class InstallPlugget(bpy.types.Operator):
    """Install Plugget Qt Manager"""
    bl_idname = "plugget.install_plugget"
    bl_label = "Install Plugget Qt"
    
    def execute(self, context):
        # get blender user folder
        user_folder = bpy.utils.resource_path('USER')
        command = [sys.executable, "-m", "pip", "install", "plugget-qt", "--target", str(pth_path), "--no-user"]
        print(" ".join(command))
        subprocess.run(command)
        # clear cache so we can import the module
        import importlib
        importlib.invalidate_caches()        
        self.report({'INFO'}, "plugget-qt module installed successfully. Please restart Blender.")
        return {'FINISHED'}


class PluggetPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    def draw(self, context):
        layout = self.layout

        if not plugget_qt_installed():
            # Display warning and install button
            box = layout.box()
            box.label(text="plugget-qt module is not installed", icon='ERROR')
            box.label(text="Please install it to use the Plugget Qt Manager.")
            box.operator(InstallPlugget.bl_idname, icon='PLUGIN')
        else:
            # Display success message and open button
            box = layout.box()
            box.label(text="plugget-qt module is installed", icon='INFO')
            box.operator(OpenPluggetQt.bl_idname, icon='PLUGIN')

def menu_func(self, context):
    self.layout.operator(OpenPluggetQt.bl_idname, icon="MESH_CUBE")

def register():
    bpy.utils.register_class(OpenPluggetQt)
    bpy.utils.register_class(InstallPlugget)
    bpy.utils.register_class(PluggetPreferences)
    bpy.types.TOPBAR_MT_window.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OpenPluggetQt)
    bpy.utils.unregister_class(InstallPlugget)
    bpy.utils.unregister_class(PluggetPreferences)
    bpy.types.TOPBAR_MT_window.remove(menu_func)

if __name__ == "__main__":
    register()
