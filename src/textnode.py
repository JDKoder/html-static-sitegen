from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        isTextEq = self.text == other.text
        isTextTypeEq = self.text_type == other.text_type
        isURLEq = self.url == other.url
        return isTextEq and isTextTypeEq and isURLEq

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

"""
#Testing node creation
test_node = TextNode("hello Jacob", TextType.TEXT, "http://word.com")
print(test_node)

#Testing TextNode eq comparison
clone_node = TextNode("**I'm some bod text**", TextType.BOLD, "http://foo.com")
print(test_node == clone_node)
"""
