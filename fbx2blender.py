import os
import bpy

#path_to_fbx_dir = os.path.join("絶対PATH") #Win
#ex.path_to_fbx_dir = os.path.join("C:\Users\Your Name\Desktop\fbx2blender.py") #Windows

path_to_fbx_dir = bpy.path.abspath('絶対PATH') #Mac

# ディレクトリ内のすべてのファイルのリストを取得します
file_list = sorted(os.listdir(path_to_fbx_dir))

#「fbx」で終わるファイルのリストを取得します
fbx_list = [item for item in file_list if item[-3:] == 'fbx'] # obj, fbx, vrm, etc..

# fbx_listの文字列をループし、ファイルをシーンに追加します
for item in fbx_list:
    path_to_file = os.path.join(path_to_fbx_dir, item)
    bpy.ops.import_scene.fbx(filepath = path_to_file)