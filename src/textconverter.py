from textnode import TextType, TextNode
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    if text_node is None:
        raise ValueError("Expected TextType but was None")
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", text_node.text, {"src":text_node.url, "alt":text_node.text})
        case _:
            raise ValueError("unsupported text node value")

# Not sure I need this, but I wrote it so I'm keeping it here for a while
def remove_text_markdown(md_node, wrapper):
    if wrapper == "**":
        return md_node[2:len(md_node)-2]
    if wrapper == "_":
        return md_node[1:len(md_node)-1]
    if wrapper == "```":
        return md_node[3:len(md_node)-3]
    return md_node

