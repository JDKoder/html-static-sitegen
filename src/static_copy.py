import os
import shutil
"""Write a recursive function that copies all the contents from a source directory to a dest_dirination directory (in our case, static to public)

    It should first delete all the contents of the dest_dirination directory (public) to ensure that the copy is clean.
    It should copy all files and subdirectories, nested files, etc.
    I recommend logging the path of each file you copy, so you can see what's happening as you run and debug your code."""

def copy_to_dest_dir(src_dir, dest_dir, overwrite=False):
    if overwrite:
        print(f"Deleting tree at {dest_dir}")
        shutil.rmtree(dest_dir)

    if not os.path.exists(dest_dir):
        print(f"Creating directory: {dest_dir}")
        os.mkdir(dest_dir)
    #    raise ValueError("src_dir must be a directory")
    for file in os.listdir(src_dir):
        print(f"Copying {src_dir}/{file} to {dest_dir}/{file}")
        if os.path.isdir(src_dir + "/" + file):
            print(f"{file} is a directory")
            copy_to_dest_dir(src_dir + "/" + file, dest_dir + "/" + file, False)
        else:
            shutil.copy(src_dir + "/" + file, dest_dir)


