from textnode import TextNode, TextType
from extractmd import extract_markdown_link, extract_markdown_images


def split_doc_to_blocks(doc):
    blocks = doc.split("\n\n")
    final_blocks = []
    for block in blocks:
        #If the block is empty, skip it to the next one
        if block.strip() == "":
            continue
        #format each block line of the block so none have trailing whitespace
        splits = block.split("\n")
        f_splits = []
        for split in splits:
            f_splits.append( split.strip())
        block = "\n".join(f_splits).strip()
        final_blocks.append(block)
    return final_blocks


def text_to_nodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_images(nodes)
    return nodes


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        splits = old_node.text.split(delimiter)
        if len(splits) == 1:
           #nothing happened, add the node as is and continue
            new_nodes.append(old_node)
            continue
        for i in range(len(splits)):
            # The delimiter is at the start or end of the text.
            if splits[i] == "":
                # don't include empty text nodes in the final list
                continue
            # odd indices are added with the passed text type
            if i % 2 > 0:
                new_nodes.append(TextNode(splits[i], text_type))
            else:
                new_nodes.append(TextNode(splits[i], old_node.text_type))
    return new_nodes


def split_nodes_link(nodes):
    new_nodes = []
    for old_node in nodes:
        links = extract_markdown_link(old_node.text)
        if len(links) > 0:
            #split the old text by the links found above
            for link_itr in range(len(links)):
                splits = old_node.text.split(f"[{links[link_itr][0]}]({links[link_itr][1]})",1)
                # splits should only be 2 long since we split a max of 1 time
                if len(splits) == 2:
                    if splits[0] != "":
                        #only add a leading TextNode if the link is not the first thing that was split
                        new_nodes.append(TextNode(splits[0], old_node.text_type, old_node.url))
                    #always add the link after the first split
                    new_nodes.append(TextNode(links[link_itr][0], TextType.LINK, links[link_itr][1]))
                    if splits[1] != "" and link_itr < len(links) -1:
                        # we have more links to process so let's set the remaining text we'll be splitting for the next link.
                        old_node.text = splits[1]
                    elif splits[1] != "" and link_itr == len(links) -1:
                        # we're at the end of the links so we can add the remaining text node as long as it's not blank
                        new_nodes.append(TextNode(splits[1], old_node.text_type, old_node.url))
        else:
            new_nodes.append(old_node)
    return new_nodes


def split_nodes_images(nodes):
    new_nodes = []
    for old_node in nodes:
        images = extract_markdown_images(old_node.text)
        if len(images) > 0:
            #split the old text by the images found above
            for image_itr in range(len(images)):
                splits = old_node.text.split(f"![{images[image_itr][0]}]({images[image_itr][1]})",1)
                # splits should only be 2 long since we split a max of 1 time
                if len(splits) == 2:
                    if splits[0] != "":
                        #only add a leading TextNode if the link is not the first thing that was split
                        new_nodes.append(TextNode(splits[0], old_node.text_type, old_node.url))
                    #always add the link after the first split
                    new_nodes.append(TextNode(images[image_itr][0], TextType.IMAGE, images[image_itr][1]))
                    if splits[1] != "" and image_itr < len(images) -1:
                        # we have more images to process so let's set the remaining text we'll be splitting for the next link.
                        old_node.text = splits[1]
                    elif splits[1] != "" and image_itr == len(images) -1:
                        # we're at the end of the images so we can add the remaining text node as long as it's not blank
                        new_nodes.append(TextNode(splits[1], old_node.text_type, old_node.url))
        else:
            new_nodes.append(old_node)
    return new_nodes







