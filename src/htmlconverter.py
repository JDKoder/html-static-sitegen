from splitnodes import split_doc_to_blocks 
from blockconverter import block_to_block_type
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
                block_node = HTMLNode("p", block, None, None )#todo implement adding children
 
