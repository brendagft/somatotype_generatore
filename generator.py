import random
import bpy
import os

def delete_object():
  if bpy.context.object.mode == 'EDIT':
    bpy.ops.object.mode_set(mode='OBJECT')

  bpy.ops.object.select_all(action='DESELECT')
  if 'SMPLX-male' in bpy.data.objects:
    bpy.data.objects['SMPLX-male'].select_set(True)
    bpy.ops.object.delete()

  bpy.ops.object.select_all(action='DESELECT')
  if 'SMPLX-mesh-male' in bpy.data.objects:        
    bpy.data.objects['SMPLX-mesh-male'].select_set(True)
    bpy.ops.object.delete()

  bpy.ops.object.select_all(action='DESELECT')
  if 'SMPLX-female' in bpy.data.objects:        
    bpy.data.objects['SMPLX-female'].select_set(True)
    bpy.ops.object.delete()

  bpy.ops.object.select_all(action='DESELECT')
  if 'SMPLX-mesh-female' in bpy.data.objects:        
    bpy.data.objects['SMPLX-mesh-female'].select_set(True)
    bpy.ops.object.delete()

bpy.props.FloatProperty(name="Target Height [m]", default=1.70, min=1.4, max=2.2)
bpy.props.FloatProperty(name="Target Weight [kg]", default=110, min=110, max=110) #110

for i in range(300, 600):
  delete_object()
  gender = random.choice(["female", "male"])
  bpy.context.window_manager.smplx_tool.smplx_gender = gender

  handpose = 'relaxed'#random.choice(["flat", "relaxed"])
  bpy.context.window_manager.smplx_tool.smplx_handpose = handpose

  bpy.ops.scene.smplx_add_gender()

  textures = []
  if gender == "female":
    textures.append("smplx_texture_f_alb.png")
  else:
    textures.append("smplx_texture_m_alb.png")

  texture = random.choice(textures)
  bpy.context.window_manager.smplx_tool.smplx_texture = texture
  bpy.ops.object.smplx_set_texture()

  bpy.ops.object.smplx_random_shape()

  bpy.ops.object.smplx_snap_ground_plane()

  blend_path = bpy.data.filepath
  blend_path = os.path.dirname(bpy.path.abspath(blend_path))

  dirpath = os.path.join(blend_path, "endomorphe")

  filepath = os.path.join(dirpath, "endomorphe{}.png")
  scene = bpy.context.scene
  scene.render.image_settings.file_format = 'PNG'

  bpy.ops.render.render()
  RR = "Render Result"
  bpy.data.images[RR].save_render(filepath.format(i))
