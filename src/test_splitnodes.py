import unittest
from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter, split_nodes_link, split_nodes_images, text_to_nodes, split_doc_to_blocks

class TestSplitNodes(unittest.TestCase):


    def test_split_nodes_delimiter_no_split(self):
        node = TextNode("Test text", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 1)


    def test_split_nodes_delimiter_split_code_in_middle(self):
        node = TextNode("Test `text` is cool", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[2].text_type, TextType.TEXT)


    def test_split_nodes_delimiter_split_at_end(self):
        node = TextNode("Test `text`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text_type, TextType.CODE)


    def test_split_nodes_delimiter_split_at_start(self):
        node = TextNode("`Test` text", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text_type, TextType.CODE)
        self.assertEqual(result[1].text_type, TextType.TEXT)


    def test_split_nodes_delimiter_split_bold_in_middle(self):
        node = TextNode("Test *text* is cool", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text_type, TextType.TEXT)


    def test_split_nodes_delimiter_split_italic_in_middle(self):
        node = TextNode("Test _text_ is cool", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text_type, TextType.ITALIC)
        self.assertEqual(result[2].text_type, TextType.TEXT)


    def test_split_nodes_delimiter_split_multi_node(self):
        nodes = []
        nodes.append(TextNode("Test _text_ is cool", TextType.TEXT))
        nodes.append(TextNode("Test `text`", TextType.TEXT))
        nodes.append(TextNode("Test *text* is cool", TextType.TEXT))
        result = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        self.assertEqual(len(result), 5)
        result = split_nodes_delimiter(result, "`", TextType.CODE)
        self.assertEqual(len(result), 6)
        result = split_nodes_delimiter(result, "*", TextType.BOLD)
        self.assertEqual(len(result), 8)
        # print(result)
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text_type, TextType.ITALIC)
        self.assertEqual(result[2].text_type, TextType.TEXT)
        self.assertEqual(result[3].text_type, TextType.TEXT)
        self.assertEqual(result[4].text_type, TextType.CODE)
        self.assertEqual(result[5].text_type, TextType.TEXT)
        self.assertEqual(result[6].text_type, TextType.BOLD)
        self.assertEqual(result[7].text_type, TextType.TEXT)


    def test_split_nodes_delimiter_split_single_node(self):
        nodes = [TextNode("Test _italic_ text. Test `code` text. Test *bold* text.", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        self.assertEqual(len(result), 3)
        result = split_nodes_delimiter(result, "`", TextType.CODE)
        self.assertEqual(len(result), 5)
        result = split_nodes_delimiter(result, "*", TextType.BOLD)
        self.assertEqual(len(result), 7)
        # print(result)
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text_type, TextType.ITALIC)
        self.assertEqual(result[2].text_type, TextType.TEXT)
        self.assertEqual(result[3].text_type, TextType.CODE)
        self.assertEqual(result[4].text_type, TextType.TEXT)
        self.assertEqual(result[5].text_type, TextType.BOLD)
        self.assertEqual(result[6].text_type, TextType.TEXT)


    def test_split_nodes_link_two_links_in_text(self):
        old_node = TextNode("Some basic text [a link](http://www.google.com) and [another link](http://www.boot.dev) and then some more text", TextType.TEXT)
        new_nodes = split_nodes_link([old_node])
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, "Some basic text ")
        self.assertEqual(new_nodes[1].text_type, TextType.LINK)
        self.assertEqual(new_nodes[1].text, "a link")
        self.assertEqual(new_nodes[1].url, "http://www.google.com")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].text_type, TextType.LINK)
        self.assertEqual(new_nodes[3].text, "another link")
        self.assertEqual(new_nodes[3].url, "http://www.boot.dev")
        self.assertEqual(new_nodes[4].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[4].text, " and then some more text")


    def test_split_nodes_image_solo(self):
        old_node = TextNode("![a image](http://www.google.com)", TextType.TEXT)
        new_nodes = split_nodes_images([old_node])
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text_type, TextType.IMAGE)
        self.assertEqual(new_nodes[0].text, "a image")
        self.assertEqual(new_nodes[0].url, "http://www.google.com")


    def test_split_nodes_image_one_image_in_text(self):
        old_node = TextNode("Some basic text ![a image](http://www.google.com) and then some more text", TextType.TEXT)
        new_nodes = split_nodes_images([old_node])
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(new_nodes[1].text, "a image")
        self.assertEqual(new_nodes[1].url, "http://www.google.com")

    def test_split_nodes_image_two_images_in_text(self):
        old_node = TextNode("Some basic text ![a image](http://www.google.com) and ![another image](http://www.boot.dev) and then some more text", TextType.TEXT)
        new_nodes = split_nodes_images([old_node])
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, "Some basic text ")
        self.assertEqual(new_nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(new_nodes[1].text, "a image")
        self.assertEqual(new_nodes[1].url, "http://www.google.com")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].text_type, TextType.IMAGE)
        self.assertEqual(new_nodes[3].text, "another image")
        self.assertEqual(new_nodes[3].url, "http://www.boot.dev")
        self.assertEqual(new_nodes[4].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[4].text, " and then some more text")


    def test_split_nodes_image_solo(self):
        old_node = TextNode("![a image](http://www.google.com)", TextType.TEXT)
        new_nodes = split_nodes_images([old_node])
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text_type, TextType.IMAGE)
        self.assertEqual(new_nodes[0].text, "a image")
        self.assertEqual(new_nodes[0].url, "http://www.google.com")


    def test_split_nodes_image_one_image_in_text(self):
        old_node = TextNode("Some basic text ![a image](http://www.google.com) and then some more text", TextType.TEXT)
        new_nodes = split_nodes_images([old_node])
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(new_nodes[1].text, "a image")
        self.assertEqual(new_nodes[1].url, "http://www.google.com")

    
    def test_text_to_nodes(self):
        test_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        #print(text_to_nodes(test_text))
        nodes = text_to_nodes(test_text)
        self.assertEqual(len(nodes), 10)
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[3].text_type, TextType.ITALIC)
        self.assertEqual(nodes[4].text_type, TextType.TEXT)
        self.assertEqual(nodes[5].text_type, TextType.CODE)
        self.assertEqual(nodes[6].text_type, TextType.TEXT)
        self.assertEqual(nodes[7].text_type, TextType.IMAGE)
        self.assertEqual(nodes[8].text_type, TextType.TEXT)
        self.assertEqual(nodes[9].text_type, TextType.LINK)


    def test_split_doc_to_blocks(self):
        test_doc = """This is a test doc.

            every double newline character is going to be a new block

            so this should have 3"""
        nodes = split_doc_to_blocks(test_doc)
        self.assertEqual(len(nodes), 3)


    def test_split_doc_to_blocks_empty_block(self):
        test_doc = """This is a test doc.



            every double newline character is going to be a new block

            so this should have 3"""
        nodes = split_doc_to_blocks(test_doc)
        self.assertEqual(len(nodes), 3)


def test_split_doc_to_blocks_empty_block(self):
    test_doc = """This is a test doc.

                    every double newline character is going to be a new block

        so this should have 3               """
    blocks = split_doc_to_blocks(test_doc)
    self.assertEqual(len(blocks), 3)
    self.assertEqual(blocks[0], "this is a test doc.")
    self.assertEqual(blocks[1], "every double newline character is going to be a new block")
    self.assertEqaul(blocks[2], "so this should have 3")


def test_split_doc_to_blocks_multiline_block(self):
    test_doc = """-line one
        -line two
        -line three"""
    self.assertEqual(len(split_doc_to_blocks(test_doc)), 1)
