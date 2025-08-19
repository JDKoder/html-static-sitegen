import os
"""Write a recursive function that copies all the contents from a source directory to a dest_dirination directory (in our case, static to public)

    It should first delete all the contents of the dest_dirination directory (public) to ensure that the copy is clean.
    It should copy all files and subdirectories, nested files, etc.
    I recommend logging the path of each file you copy, so you can see what's happening as you run and debug your code."""

def copy_to_dest_dir(src_dir, dest_dir, overwrite=True):
    if src_dir is null or not os.path.exists or not os.path.isdir(src_dir):
        raise ValueError("src_dir must be a directory")
    if dest_dir is null or not os.path.exists or not os.path.isdir(src_dir):
        raise ValueError("src_dir must be a directory")


