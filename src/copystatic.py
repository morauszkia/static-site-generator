import os
import shutil


def empty_directory(path):
    if os.path.exists(path):
        print(f"Deleting {os.path.abspath(path)}")
        shutil.rmtree(path)
        print(f"Deleted directory: {path}")
    try:
        os.makedirs(path)
    except FileExistsError:
        print("Directory already exists.")


def copy_static_files(src_dir, dest_dir):

    if not os.path.exists(src_dir):
        print(f"Source directory {os.path.abspath(src_dir)} does not exist!")
        return

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dst_path = os.path.join(dest_dir, item)

        if os.path.isdir(src_path):
            copy_static_files(src_path, dst_path)
        else:
            print(f"Copying file {src_path} to {dst_path}")
            shutil.copy(src_path, dst_path)
    



