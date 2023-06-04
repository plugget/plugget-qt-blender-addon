bl_info = {
    "name": "Plugget Qt Package Manager",
    "description": "manage Plugget packages",
    "author": "Hannes D",
    "version": (1, 0),
    "blender": (2, 91, 0),
    "location": "Window/Plugget Qt Manager",
    "category": "Development",
}


import bpy


# Define a new menu class
# class MyMenu(bpy.types.Menu):
#     bl_idname = "OBJECT_MT_my_menu"
#     bl_label = "My Menu"

#     def draw(self, context):
#         layout = self.layout
#         layout.operator("object.my_operator")


# Define a new operator class
class MyOperator(bpy.types.Operator):
    bl_idname = "object.my_operator"
    bl_label = "My Operator"

    def execute(self, context):
        # Your code here
        import plugget_search_widget as psw
        psw.show()
        return {'FINISHED'}


# Add the new menu item to the "Window" menu
def menu_func(self, context):
#     self.layout.menu(MyMenu.bl_idname)
    self.layout.operator(MyOperator.bl_idname, icon="MESH_CUBE")


def register():
    # bpy.utils.register_class(MyMenu)
    bpy.utils.register_class(MyOperator)
#    bpy.types.VIEW3D_MT_object.append(menu_func)
    bpy.types.TOPBAR_MT_window.append(menu_func)


def unregister():
    # bpy.utils.unregister_class(MyMenu)
    bpy.utils.unregister_class(MyOperator)
#    bpy.types.VIEW3D_MT_object.remove(menu_func)
    bpy.types.TOPBAR_MT_window.remove(menu_func)


# if __name__ == "__main__":
#     register()