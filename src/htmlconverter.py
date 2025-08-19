import re
from splitnodes import split_doc_to_blocks, text_to_nodes
from blockconverter import block_to_block_type
from textconverter import text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from blocktype import BlockType


# converts an md text document into an html text document wrapped in <div></div> tags.
def markdown_to_html_node(doc):
    #todo, put this in its own file
    html_nodes = []
    blocks = split_doc_to_blocks(doc)
    for block in blocks:
        #determine type
        block_type = block_to_block_type(block);
        html_node = None;
        match (block_type):
            case BlockType.PARAGRAPH:
                #remove newlines from this block type
                block = " ".join(block.split("\n"))
                text_nodes = text_to_nodes(block)
                block_html_children = text_to_children(text_nodes)
                html_node = ParentNode("p", block_html_children)
            case BlockType.HEADING:
                hnum = 0;
                while hnum < 7:
                    hnum += 1
                    if block[hnum] != "#":
                        break
                text_nodes = text_to_nodes(block[hnum:len(block)].strip())
                block_html_children = text_to_children(text_nodes)
                html_node = ParentNode(f"h{hnum}", block_html_children)
            case BlockType.CODE:
                # wrap with <pre></pre> and treat block as one long text node without the wrapping ```...``` ie. do not add inner html
                stripped_block = block[3:len(block)].strip()
                # should remove leading and trailing \n 
                stripped_block = re.sub("^(\n)+$", "", stripped_block)
                stripped_block = re.sub("(\n)*```", "", stripped_block)
                html_node = ParentNode("pre", [LeafNode("code", stripped_block)])
            case BlockType.QUOTE:
                #remove all > characters that follow a newline
                split_block = block[1:len(block)].split("\n>")
                #Replace the newline characters without the '>'
                split_block = strip_splits(split_block)
                formatted_block = "\n".join(split_block)
                #Now that the wrapping markdown is removed, we can conver the text into nodes
                text_nodes = text_to_nodes(formatted_block)
                block_html_children = text_to_children(text_nodes)
                html_node = ParentNode("blockquote", block_html_children)
            case BlockType.ORDERED_LIST:
                #remove all - characters
                split_block = re.split("\n[1-9][0-9]*[.]", block[2:len(block)])
                #create parent nodes out of each of these splits
                ol_children = []
                for split in split_block:
                    ol_children.append(ParentNode('li', text_to_children(text_to_nodes(split))))
                html_node = ParentNode("ol", ol_children)
            case BlockType.UNORDERED_LIST:
                #remove all - characters
                split_block = re.split("\n-", block[1:len(block)])
                #create parent nodes out of each of these splits
                ol_children = []
                for split in split_block:
                    ol_children.append(ParentNode('li', text_to_children(text_to_nodes(split))))
                html_node = ParentNode("ul", ol_children)
            case _:
                printf(f"unsupported case {block_type}")
        html_nodes.append(html_node)
    return ParentNode("div", html_nodes)


def strip_splits(splits):
    for split in range(len(splits)):
        splits[split] = splits[split].strip()#Takes a list of text nodes and converts them into html leaf nodes
    return splits


def text_to_children(text_nodes):
    leaf_html_nodes = []
    for text_node in text_nodes:
        leaf_html_nodes.append(text_node_to_html_node(text_node))
    return leaf_html_nodes
        
