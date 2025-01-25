# import the blender library to get access to blender objects and code
import bpy

# put the currently selected object in a variable
object_to_clone = bpy.context.selected_objects[0]
y_offset = 0

for row in range(8):
    y_offset = y_offset + 3
    for i in range(1, 9):
        new_object = object_to_clone.copy()
        bpy.context.collection.objects.link(new_object)
        new_object.location.x = new_object.location.x + (3 * i)
        new_object.location.y = new_object.location.y + y_offset
