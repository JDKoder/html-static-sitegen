import re
# \[([^\(]+)\]\(([^\)]+)\)

#Looks for a h1 in markdown represented by a line starting with a single '#'
#strips leading and trailing whitespace as well as the markdown and returns the text.
def extract_title(markdown):
    title = re.findall("^#.*", markdown)
    #print(f"title length {len(title)}")
    if not title:
        raise Exception("no title found")
    return title[0][1:len(title[0])].strip()

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


