import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


    def test_parent_to_html_with_grandchildren_with_props(self):
        left_text = LeafNode(None, "some text on the left ")
        link_leaf = LeafNode("a", "link", lprops={"href":"www.google.com", "target":"_blank"})
        right_text = LeafNode(None, " some text on the right")
        parent = ParentNode("p", [left_text, link_leaf, right_text], {"class":"p1"})
        self.assertEqual(
            parent.to_html(),
                '<p class="p1">some text on the left <a href="www.google.com" target="_blank">link</a> some text on the right</p>'
        )

    def test_parent_to_html_all_leaf(self):
        pnode = ParentNode("p",
                           [
                           LeafNode("b", "Bold text"),
                           LeafNode(None, "Normal text"),
                           LeafNode("i", "italic text"),
                           LeafNode(None, "Normal text")
                           ])
        self.assertEqual(
            pnode.to_html(),
            '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        )

if __name__ == "__main__":
    unittest.main()
