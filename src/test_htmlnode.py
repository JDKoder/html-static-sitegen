import unittest

from htmlnode import HTMLNode, LeafNode


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


    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


if __name__ == "__main__":
    unittest.main()
