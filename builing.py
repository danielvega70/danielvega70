import bpy
import mathutils

# Set up the parameters for the building
num_floors = 40
floor_height = 3.0
building_width = 10.0
building_depth = 10.0

# Create the base of the building
bpy.ops.mesh.primitive_cube_add(size=building_width, location=(0, 0, floor_height/2))

# Extrude the base to create the floors of the building
for i in range(1, num_floors):
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, floor_height)})
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.context.object.name = f"Floor{i}"
    
# Add a roof to the building
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, floor_height)})
bpy.ops.mesh.select_all(action='INVERT')
bpy.ops.mesh.delete(type='VERT')
bpy.context.object.name = "Roof"
    
# Center the building
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
bpy.ops.transform.translate(value=(-building_width/2, -building_depth/2, 0))
