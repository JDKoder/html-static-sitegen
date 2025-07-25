import unittest
from textconverter import text_node_to_html_node
from textnode import TextType, TextNode
from htmlnode import LeafNode

class TestTextConverter(unittest.TestCase):
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.html_assertions(html_node, value=node.text)


    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.html_assertions(html_node, tag="b", value="This is a bold text node")


    def test_italic(self):
        node = TextNode("This is a italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.html_assertions(html_node, tag="i", value="This is a italic text node")


    def test_code(self):
        node = TextNode("This is a code text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.html_assertions(html_node, tag="code", value="This is a code text node")


    def test_image(self):
        node = TextNode("image alt text", TextType.IMAGE, "http://google.com")
        html_node = text_node_to_html_node(node)
        self.html_assertions(html_node, tag="img", props={"src":"http://google.com", "alt":"image alt text"}, value="image alt text")

    def test_link(self):
        node = TextNode("link alt text", TextType.LINK, "http://google.com")
        html_node = text_node_to_html_node(node)
        self.html_assertions(html_node, tag="a", props={"href":"http://google.com"}, value="link alt text")


        

        
    def html_assertions(self, result, tag=None, value=None, props=None):
        self.assertEqual(result.tag, tag)
        self.assertEqual(result.value, value)
        self.assertEqual(result.props, props)
