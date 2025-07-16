import unittest

from htmlnode import HTMLNode 


class TestHTMLNode(unittest.TestCase):


    def test_props_to_html(self):
        node = HTMLNode(tag="a", value="Google", props={"href":"http://www.google.com", "target":"_blank"})
        result = node.props_to_html()
        expected = ' href="http://www.google.com" target="_blank"'
        self.assertEqual(result, expected)


    def test_props_to_html_no_props(self):
        node = HTMLNode()
        self.assertEqual("", node.props_to_html())

    def test_htmlnode_repr(self):
        node = HTMLNode(tag="a", value="Google", props={"href":"http://www.google.com", "target":"_blank"})
        self.assertEqual(node.__repr__(), f"HTMLNode({node.tag}, {node.value}, {node.children}, {node.props})")


if __name__ == "__main__":
    unittest.main()
