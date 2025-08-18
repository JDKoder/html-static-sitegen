from splitnodes import split_doc_to_blocks, text_to_nodes
from blockconverter import block_to_block_type
from textconverter import text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextType


# converts an md text document into an html text document wrapped in <div></div> tags.
def markdown_to_html_node(doc):
    #todo, put this in its own file
    blocks = split_doc_to_blocks(doc)
    for block in blocks:
        #determine type
        block_type = block_to_block_type(block);
        block_node = None;
        match (block_type):
            case TextType.TEXT:
                text_nodes = text_to_nodes(block)
                block_html_children = text_to_children(text_nodes)
                block_node = ParentNode("p", block_html_children)
                break
            case TextType.HEADING:
                # TODO: special handling:  count the number of "#" marks up to 6
                hnum = 0;
                while hnum < 7:
                    hnum += 1
                    if block[hnum] != "#":
                        break
                }
                text_nodes = text_to_nodes(block[hnum:len(block)].strip())
                block_html_children = text_to_children(text_nodes)
                block_node = ParentNode(f"h{hnum}", block_html_children)
                break
            case TextType.CODE:
                # TODO special handling:  wrap with <pre></pre> tags and treet block as one long text node without the wrapping ```...``` ie. do not add inner html
                block_node = ParentNode("pre", [LeafNode("code", block[3:len(block)-3])])
                break
            case TextType.QUOTE:
                #remove all > characters that follow a newline
                split_block = block[1:len(block)]).split("\n>")
                formatted_block = "\n".join(split_block)
                text_nodes = text_to_nodes(formatted_block)
                block_html_children = text_to_children(text_nodes)
                
                block_node = ParentNode("blockquote", block_html_children)
                break



#Takes a list of text nodes and converts them into html leaf nodes
def text_to_children(text_nodes)
    leaf_html_nodes = []
    for text_node in text_nodes:
        leaf_html_nodes.append(text_node_to_html_node(text_node))
    return leaf_html_nodes
        
