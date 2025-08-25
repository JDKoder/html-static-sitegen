import os
import shutil
from htmlconverter import markdown_to_html_node
from extractmd import extract_title

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dir_path_content):
        raise ValueError(f"{dir_path_content} does not exist.")
    if not os.path.exists(template_path):
        raise ValueError(f"{template_path} does not exist.")

    for file in os.listdir(dir_path_content):
        working_file = f"{dir_path_content}/{file}"
        print(f"Working on {working_file}")
        if os.path.isdir(working_file):
            print(f"{file} is a directory")
            generate_pages_recursive(working_file, template_path, dest_dir_path + "/" + file)
        else:
            file_tuple = os.path.splitext(file)
            print(f"file tuple is {file_tuple}")
            # destination file should be named .html
            new_filename = f"{file_tuple[0]}.html"
            #print(f"file name is {file_tuple[0]} and will be saved as {new_filename}")
            generate_page(working_file, template_path, f"{dest_dir_path}/{new_filename}")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    #Read Markdown file @ from_path
    markdown_file = None
    with open(from_path) as from_read:
        markdown_file = from_read.read()
    #print(f"content of markdown_file {markdown_file}")

    #Read Template file @ template_path
    html_template_file = None
    with open(template_path) as template_read:
        html_template_file = template_read.read()
    #print(f"content of html_template_file {html_template_file}")
    #Use markdown_to_html_node and .to_html() method to convert the markdown file to an HTML string
    result_html_nodes = markdown_to_html_node(markdown_file)
    result_html = None
    if result_html_nodes:
        result_html = result_html_nodes.to_html()
    #print(f"content of html after markdown_to_html_node: \n\n{result_html.to_html()}")
    #Use the extract_title function to grab the title of the page.
    title = extract_title(markdown_file)
    print(f"title is {title}")
    #Replace the {{ Title }} and {{ Content }} placeholder
    template_title_replaced = replace_tag("Title", html_template_file, title)
    final_result_html = replace_tag("Content", template_title_replaced, result_html)
    #Ensure directory exists prior to writing our file to it
    #Even though this is a fun solution, we should not reinvent the wheel eh?
    #dest_dir = dest_path[0:len(dest_path)-(dest_path[::-1].index("/"))]
    dest_dir = os.path.dirname(dest_path)

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    #write new full HTML page to a file at dest_path
    with open(dest_path, 'w', encoding="utf-8") as dest_write:
        dest_write.write(final_result_html)

def replace_tag(tagname, content, replacement):
    return content.replace("{{ " + tagname + " }}", replacement)

#generate_page("/home/jboy/git/JDKoder/html-static-sitegen/content/index.md", "/home/jboy/git/JDKoder/html-static-sitegen/template.html","/home/jboy/git/JDKoder/html-static-sitegen/public/index.html")
