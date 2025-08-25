from textnode import TextNode, TextType
from static_copy import copy_to_dest_dir
from generate_page import generate_page


def main():
    print(f"Transferring content from ./static to ./public")
    print(f"Removing directory ./public")
    copy_to_dest_dir("./static", "./public", overwrite=True)
    generate_page("./content/index.md", "./template.html", "./public/index.html")


main()
