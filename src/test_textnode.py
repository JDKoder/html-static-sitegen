import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_textnode_type_eq(self):
        for value in TextType:
            # print(f"testing {value}")
            node = TextNode("This is a text node", value)
            node2 = TextNode("This is a text node", value)
            self.assertEqual(node, node2)

    def test_textnode_text_eq(self):
        node = TextNode("foo", TextType.TEXT)
        node2 = TextNode("bar", TextType.TEXT)
        self.assertNotEqual(node,node2)

    def test_textnode_type_not_eq(self):
        control_text = "This is a text node"
        node = TextNode(control_text, TextType.TEXT)
        # Loop over TextType values to compare against base case
        for value in TextType:
            # print(f"Testing {value}")
            if value == TextType.TEXT:
                continue
            self.assertNotEqual(node, TextNode(control_text, value))

    def test_textnode_url_not_eq(self):
        node = TextNode("foo", TextType.TEXT, "foo")
        node2 = TextNode("foo", TextType.TEXT, "bar")
        self.assertNotEqual(node,node2)

    def test_textnode_url_eq(self):
        node = TextNode("foo", TextType.TEXT, "foo")
        node2 = TextNode("foo", TextType.TEXT, "foo")
        self.assertEqual(node,node2)





if __name__ == "__main__":
    unittest.main()
