import sys
from textnode import TextNode, TextType
from static_copy import copy_to_dest_dir
from generate_page import generate_page, generate_pages_recursive


def main():
    base_path = "/"
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    print(f"base path = {base_path}")
    copy_to_dest_dir("./static", "./docs", overwrite=True)
    generate_pages_recursive(base_path, "./content", "./template.html", "./docs")
    #generate_page("./content/index.md", "./template.html", "./public/index.html")



main()
