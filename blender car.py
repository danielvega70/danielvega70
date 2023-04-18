#Blender Menu Sample 1
import bpy

class MySimpleMenu(bpy.types.Operator):
    
    bl_idname = "my.simple_menu"
    bl_label = "My Simple Menu"
    
def add_to_menu(self, context) :
    self.layout.operator("mesh.primitive_cube_add", icon = "LIGHTPROBE_CUBEMAP")
    self.layout.operator("mesh.primitive_uv_sphere_add", icon = "SPHERE")
    self.layout.operator("mesh.primitive_torus_add", icon = "SURFACE_NTORUS")
    
def register():
    bpy.utils.register_class(MySimpleMenu)
    bpy.types.VIEW3D_MT_mesh_add.append(add_to_menu)
    
def unregister():
    bpy.utils,unregister_class(MySimpleMenu)
def unregiste() :
    bpy.utils.unregister_class(MySimpleMenu)
    bpt.types.VIEW3D_MT_mesh_add.remove(add_to_menu)

if __name__ == "__main__"
register()

"""
bpy.types.TOPBAR_MT_file.append(menu_draw)
bpy.types.TOPBAR_MT_edit.append(menu_draw)
bpy.types.TOPBAR_MT_render.append(menu_draw)
bpy.types.TOPBAR_MT_window.append(menu_draw)
bpy.types.TOPBAR_MT_help.append(menu_draw)


bpy.types.VIEW3D_MT_curve_add.append(menu_draw)
bpy.types.VIEW3D_MT_mesh_add.append(menu_draw)
bpy.types.VIEW3D_MT_surface_add.append(menu_draw)
bpy.types.VIEW3D_MT_metaball_add.append(menu_draw)
bpy.types.VIEW3D_MT_volume_add.append(menu_draw)
"""  

###############################################

# Blender Menu Sample 2

import bpy

class MyMenu(bpy.types.Operator):
   
    bl_idname = "my.simple_menu"
    bl_label = "My Menu"
    
def add_to_menu(self, context) :
    layout = self.layout
    
    layout.operator("mesh.primitive_plane_add")
    layout.operator("mesh.primitive_uv_sphere_add")
    
    layout.separator()
    
    layout.operator("curve.primitive_bezier_circle_add")
    layout.operator("curve.primitive_nurbs_curve_add")
    
    layout.separator()
    
    layout.operator("object.camera_add")
    
    
def register() :
    bpy.utils.register_class(MyMenu)
    bpy.types.TOPBAR_MT_file.append(add_to_menu)


def unregister() :
    bpy.utils.unregister_class(MyMenu)
    bpy.types.TOPBAR_MT_file.remove(add_to_menu)

if __name__ == "__main__" :
    register()
    
###############################################

# Blender Custom Menu 1

import bpy

class MySimpleMenu(bpy.types.Menu):
    bl_label = "My Simple Menu"
    bl_idname = "OBJECT_MT_my_simple_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("mesh.primitive_plane_add")
        layout.operator("object.armature_add")
        layout.operator("mesh.primitive_torus_add")
        
        layout.separator()
        
        layout.operator("object.camera_add")
        layout.operator("curve.primitive_bezier_circle_add")
        
        layout.separator()
        
        layout.operator_menu_enum("object.select_by_type",
                                  property="type",
                                  text="Select All by Type",
                                  )
        layout.operator_menu_enum("object.light_add",
                                  property="type",
                                  text="Add Light",
                                  )

def register():
    bpy.utils.register_class(MySimpleMenu)
    
   
def unregister():
    bpy.utils.unregister_class(MySimpleMenu)

if __name__ == "__main__":
    register()
    
bpy.ops.wm.call_menu(name="OBJECT_MT_my_simple_menu")

###############################################

# Blender Custom Menu 2

bl_info = {
    "name": "My Menu",
    "author": "Murat",
    "version": (1, 0),
    "blender": (2, 93, 4),
    "location": "View3D",
    "description": "Add objects menu",
    "warning": "",
    "doc_url": "",
    "category": "Add Object",
}

import bpy

class MySimpleMenuSC(bpy.types.Menu):
    bl_label = "My Simple Menu"
    bl_idname = "OBJECT_MT_my_simple_menusc"

    def draw(self, context):
        layout = self.layout
        layout.operator("mesh.primitive_plane_add")
        layout.operator("object.armature_add")
        layout.operator("mesh.primitive_torus_add")
        
        layout.separator()
        
        layout.operator("object.camera_add")
        layout.operator("curve.primitive_bezier_circle_add")
        
        layout.separator()
        
        layout.operator_menu_enum("object.select_by_type",
                                  property="type",
                                  text="Select All by Type",
                                  )
        layout.operator_menu_enum("object.light_add",
                                  property="type",
                                  text="Add Light",
                                  )
                            
addon_keymaps = []

def register():
    bpy.utils.register_class(MySimpleMenuSC)
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new('wm.call_menu', 'W', 'PRESS', ctrl=True, shift=False, alt=False)
        kmi.properties.name =  MySimpleMenuSC.bl_idname
        addon_keymaps.append((km, kmi))

def unregister():
    bpy.utils.unregister_class(MySimpleMenuSC)
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()
    
#bpy.ops.wm.call_menu(name="OBJECT_MT_my_simple_menusc")

###############################################

# Blender Top Menu 1

import bpy

class TOPBAR_MT_custom_sub_menu(bpy.types.Menu):
    bl_label = "Menu"

    def draw(self, context):
        layout = self.layout

class TOPBAR_MT_custom_menu(bpy.types.Menu):
    bl_label = "My Menu"

    def draw(self, context):
        layout = self.layout
        
        layout.operator("mesh.primitive_plane_add", icon = "LIGHTPROBE_CUBEMAP")
        layout.operator("mesh.primitive_uv_sphere_add")
        
        layout.separator()
        
        layout.operator("curve.primitive_bezier_circle_add")
        layout.operator("curve.primitive_nurbs_curve_add")
        
        layout.separator()
        
        layout.operator("object.camera_add")
        

    def menu_draw(self, context):
        self.layout.menu("TOPBAR_MT_custom_menu")

classes = (TOPBAR_MT_custom_sub_menu, TOPBAR_MT_custom_menu)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.TOPBAR_MT_editor_menus.append(TOPBAR_MT_custom_menu.menu_draw)

def unregister():
    bpy.types.TOPBAR_MT_editor_menus.remove(TOPBAR_MT_custom_menu.menu_draw)
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
    
###############################################

# Blender Top Menu 2

import bpy

class TOPBAR_MT_custom_menu(bpy.types.Menu):
    bl_label = "My Menu"

    def draw(self, context):
        layout = self.layout
        layout.menu("TOPBAR_MT_custom_sub_menu")

    def menu_draw(self, context):
        self.layout.menu("TOPBAR_MT_custom_menu")

class TOPBAR_MT_custom_sub_menu(bpy.types.Menu):
    bl_label = "Sub Menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("mesh.primitive_cube_add")

classes = (TOPBAR_MT_custom_sub_menu, TOPBAR_MT_custom_menu)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.TOPBAR_MT_editor_menus.append(TOPBAR_MT_custom_menu.menu_draw)


def unregister():
    bpy.types.TOPBAR_MT_editor_menus.remove(TOPBAR_MT_custom_menu.menu_draw)
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()

###############################################

# Blender Sub Menu

import bpy

class MY_MT_NewMenu(bpy.types.Menu):
    bl_label = "My Menu"
    bl_idname = "OBJECT_MT_custom_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("mesh.primitive_plane_add")
        layout.operator("mesh.primitive_uv_sphere_add")
        
        layout.separator()
        
        layout.operator("curve.primitive_bezier_circle_add")
        layout.operator("curve.primitive_nurbs_curve_add")
        
        layout.separator()
         
        layout.menu("OBJECT_MT_sub_menu")


class MY_MT_NewSubMenu(bpy.types.Menu):
    bl_label = "Sub Menu"
    bl_idname = "OBJECT_MT_sub_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.camera_add")
        layout.operator("object.armature_add")
        

def draw_menu(self, context):
    self.layout.menu(MY_MT_NewMenu.bl_idname)


def register():
    bpy.utils.register_class(MY_MT_NewMenu)
    bpy.utils.register_class(MY_MT_NewSubMenu)
    bpy.types.VIEW3D_MT_curve_add.append(draw_menu)

def unregister():
    
    bpy.utils.unregister_class( MY_MT_NewMenu) 
    bpy.utils.unregister_class(MY_MT_NewSubMenu) 
    bpy.types.VIEW3D_MT_curve_add.remove(draw_menu)
    
      
if __name__ == "__main__":
    register()
    
###############################################

# Blender Append Samples

import bpy

def menu_draw(self, context):
    layout = self.layout
    
    layout.operator("mesh.primitive_circle_add")
    layout.operator("mesh.primitive_cylinder_add")
    layout.operator("mesh.primitive_torus_add")
    layout.operator("object.armature_add")
    
bpy.types.TOPBAR_MT_file.append(menu_draw)
bpy.types.TOPBAR_MT_edit.append(menu_draw)
bpy.types.TOPBAR_MT_render.append(menu_draw)
bpy.types.TOPBAR_MT_window.append(menu_draw)
bpy.types.TOPBAR_MT_help.append(menu_draw)

bpy.types.VIEW3D_MT_curve_add.append(menu_draw)
bpy.types.VIEW3D_MT_mesh_add.append(menu_draw)
bpy.types.VIEW3D_MT_surface_add.append(menu_draw)
bpy.types.VIEW3D_MT_metaball_add.append(menu_draw)
bpy.types.VIEW3D_MT_volume_add.append(menu_draw)

###############################################

# Blender Pie Menu 1

import bpy
from bpy.types import Menu

class PIE_MT_AddMeshObjects(Menu):
    bl_idname = "PIE_MT_add_mesh_objects"
    bl_label = "Add Mesh Objects"

    def draw(self, context):
        layout = self.layout
        #layout.scale_y = 1
        #layout.scale_y = 1

        pie = layout.menu_pie()
        # 4 - LEFT
        pie.operator("mesh.primitive_plane_add", text = "Add Plane", icon = "MESH_PLANE")
        # 6 - RIGHT
        pie.operator("mesh.primitive_cube_add", text = "Add Cube", icon = "MESH_CUBE")
        # 2 - BOTTOM
        pie.operator("mesh.primitive_circle_add", text = "Add Circle", icon = "MESH_CIRCLE")
        # 8 - TOP
        pie.operator("mesh.primitive_uv_sphere_add", text = "Add UV Sphere", icon = "MESH_UVSPHERE")
        # 7 - TOP - LEFT
        pie.operator("mesh.primitive_ico_sphere_add", text = "Add Ico Sphere", icon = "MESH_ICOSPHERE")
        # 9 - TOP - RIGHT
        pie.operator("mesh.primitive_cylinder_add", text = "Add Cylinder", icon = "MESH_CYLINDER")
        # 1 - BOTTOM - LEFT
        pie.operator("mesh.primitive_cone_add", text = "Add Cone", icon = "MESH_CONE")
        # 3 - BOTTOM - RIGHT
        pie.operator("mesh.primitive_torus_add", text = "Add Torus", icon = "MESH_TORUS")
        
        
        """
        pie.operator("object.select_by_type", text="Select By Type")
        pie.operator("object.light_add", text="Add Light")
        pie.operator("object.empty_add", text="Add Empty")
        pie.operator("mesh.select_similar", text="Similar")
        """
        
def register():
    bpy.utils.register_class(PIE_MT_AddMeshObjects)
    
    
def unregister():
    bpy.utils.unregister_class(PIE_MT_AddMeshObjects)


if __name__ == "__main__":
    register()
    
    bpy.ops.wm.call_menu_pie(name="PIE_MT_add_mesh_objects")

###############################################

# Blender Pie Menu 2

import bpy
from bpy.types import Menu

class PIE_MT_AddMeshObjects(Menu):
    bl_idname = "PIE_MT_add_mesh_objects"
    bl_label = "Add Mesh Objects"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        # 4 - LEFT
        pie.operator("mesh.primitive_plane_add", text = "Add Plane", icon = "MESH_PLANE")
        # 6 - RIGHT
        pie.operator("mesh.primitive_cube_add", text = "Add Cube", icon = "MESH_CUBE")
        # 2 - BOTTOM
        pie.operator("mesh.primitive_circle_add", text = "Add Circle", icon = "MESH_CIRCLE")
        # 8 - TOP
        pie.operator("mesh.primitive_uv_sphere_add", text = "Add UV Sphere", icon = "MESH_UVSPHERE")
        # 7 - TOP - LEFT
        pie.operator("mesh.primitive_ico_sphere_add", text = "Add Ico Sphere", icon = "MESH_ICOSPHERE")
        # 9 - TOP - RIGHT
        pie.operator("mesh.primitive_cylinder_add", text = "Add Cylinder", icon = "MESH_CYLINDER")
        # 1 - BOTTOM - LEFT
        pie.operator("mesh.primitive_cone_add", text = "Add Cone", icon = "MESH_CONE")
        # 3 - BOTTOM - RIGHT
        pie.operator("mesh.primitive_torus_add", text = "Add Torus", icon = "MESH_TORUS")
        
        
        """
        pie.operator("object.select_by_type", text="Select By Type")
        pie.operator("object.light_add", text="Add Light")
        pie.operator("object.empty_add", text="Add Empty")
        pie.operator("mesh.select_similar", text="Similar")
        """
        
classes = (
    PIE_MT_AddMeshObjects,
    )

addon_keymaps = []


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    wm = bpy.context.window_manager
    if wm.keyconfigs.addon:
        # Shading
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new('wm.call_menu_pie', 'W', 'PRESS', ctrl=True, shift=False, alt=False)
        kmi.properties.name = "PIE_MT_add_mesh_objects"
        addon_keymaps.append((km, kmi))

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        for km, kmi in addon_keymaps:
            km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()
    
    #bpy.ops.wm.call_menu_pie(name="PIE_MT_AddMeshObjects")


###############################################

# Blender Operator Example
    
import bpy

class MakeGoldOperator(bpy.types.Operator):
    """Turn Objects into Gold"""
    bl_idname = "object.makegold_operator"
    bl_label = "Make Gold"

    def execute(self, context):
        ob = bpy.context.active_object
        mod_subsurf = ob.modifiers.new("My Modifier", 'SUBSURF')
        mod_subsurf.levels = 3
        #bpy.ops.object.modifier_apply(modifier="My Modifier")
        bpy.ops.object.shade_smooth()
        new_mat = bpy.data.materials.new("New Material")
        new_mat.use_nodes = True
        principled = new_mat.node_tree.nodes['Principled BSDF']
        principled.inputs['Metallic'].default_value = 1
        principled.inputs['Roughness'].default_value = 0
        principled.inputs['Base Color'].default_value = (1,0.6,0,1)
        ob.data.materials.append(new_mat)
        return {'FINISHED'}
    
def register():
    bpy.utils.register_class(MakeGoldOperator)


def unregister():
    bpy.utils.unregister_class(MakeGoldOperator)
    
    
class MyPanel(bpy.types.Panel):
    
    bl_label = "Panel"
    bl_idname = "MY_PT_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Turn into Gold"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.operator("object.makegold_operator", text = "Make Gold")

classes = (MakeGoldOperator, MyPanel)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
classes =(MakeGoldOperato, MyPanel)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
def unregister():
    for cls in  classes:
        bpy.utils.unregister_class(cls)
if__name__=="__main__"
register()
