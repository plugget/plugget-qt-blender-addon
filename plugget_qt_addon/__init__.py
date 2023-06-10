bl_info = {
    "name": "Plugget Qt Package Manager",
    "description": "manage Plugget packages",
    "author": "Hannes D",
    "version": (0, 0, 1),
    "blender": (2, 91, 0),
    "location": "Window/Plugget Qt Manager",
    "category": "Development",
}


import bpy


class OpenPluggetQt(bpy.types.Operator):
    """Open the Plugget Qt Manager window"""
    bl_idname = "plugget.show_qt_manager"
    bl_label = "Open Plugget Qt Manager"

    def execute(self, context):
        import plugget_qt
        global widget  # prevent widget from being garbage collected
        widget = plugget_qt.show()
        return {'FINISHED'}


def menu_func(self, context):
    # Add the new menu item to the "Window" menu
    self.layout.operator(OpenPluggetQt.bl_idname, icon="MESH_CUBE")


def register():
    bpy.utils.register_class(OpenPluggetQt)
    bpy.types.TOPBAR_MT_window.append(menu_func)


def unregister():
    bpy.utils.unregister_class(OpenPluggetQt)
    bpy.types.TOPBAR_MT_window.remove(menu_func)
