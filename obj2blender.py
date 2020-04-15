import os
import bpy

#path_to_obj_dir = os.path.join("絶対PATH") #Win
#ex.path_to_obj_dir = os.path.join("C:\Users\Your Name\Desktop\obj2blender.py") #Windows
path_to_obj_dir = bpy.path.abspath('絶対PATH') #Mac

# ディレクトリ内のすべてのファイルのリストを取得します
file_list = sorted(os.listdir(path_to_obj_dir))

#「obj」で終わるファイルのリストを取得します
obj_list = [item for item in file_list if item[-3:] == 'obj'] # obj, fbx, vrm, etc..

# obj_listの文字列をループし、ファイルをシーンに追加します
for item in obj_list:
    path_to_file = os.path.join(path_to_obj_dir, item)
    bpy.ops.import_scene.obj(filepath = path_to_file)
