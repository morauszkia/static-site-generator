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


def copy_files(src, dst):
    if not os.path.exists(src):
        print(f"Source directory {os.path.abspath(src)} does not exist!")
        return

    if not os.path.exists(dst):
        os.makedirs(dst)
    
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isdir(src_path):
            copy_files(src_path, dst_path)
        else:
            print(f"Copying file {src_path} to {dst_path}")
            shutil.copy(src_path, dst_path)
    
        

def copy_static_files(src_dir="static", dest_dir="public"):
    empty_directory(dest_dir)

    print(f"Copying static files from {src_dir} to {dest_dir}")
    copy_files(src_dir, dest_dir)
    print("Finished copying files.")


