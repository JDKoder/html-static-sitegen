from textnode import TextNode, TextType
from static_copy import copy_to_dest_dir


def main():
    print(f"Transferring content from ./static to ./public")
    print(f"Removing directory ./public")
    copy_to_dest_dir("./static", "./public", overwrite=True)

main()
