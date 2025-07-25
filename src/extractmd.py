import re
# \[([^\(]+)\]\(([^\)]+)\)

# takes a string of text with supposed url in it and extracts the url in a tuple
# structure of the tuple is [0] = alt text; [1] = url
def extract_markdown_link(url_md):
    match_links = re.findall("(?<!!)\[([^\(]+)\]\(([^\)]+)\)",url_md)
    return match_links


# takes a string of text with img url in it and extracts the url in a tuple
# structure of the tuple is [0] = alt text; [1] = url
def extract_markdown_images(url_md):
    match_images = re.findall("!\[([^\(]+)\]\(([^\)]+)\)",url_md)
    return match_images


