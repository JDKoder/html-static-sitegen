import unittest
from blocktype import BlockType
from blockconverter import block_to_block_type


class TestBlockConverter(unittest.TestCase):


    def verify(self, test_str, expected_block_type):
        self.assertEqual(block_to_block_type(test_str), expected_block_type)


    def test_block_to_block_type_heading1(self):
        self.verify("# This is a simple heading", BlockType.HEADING)


    def test_block_to_block_type_heading2(self):
        self.verify("## This is a simple heading", BlockType.HEADING)


    def test_block_to_block_type_heading3(self):
        self.verify("### This is a simple heading", BlockType.HEADING)


    def test_block_to_block_type_heading4(self):
        self.verify("#### This is a simple heading", BlockType.HEADING)
        

    def test_block_to_block_type_heading5(self):
        self.verify("##### This is a simple heading", BlockType.HEADING)


    def test_block_to_block_type_heading6(self):
        self.verify("###### This is a simple heading", BlockType.HEADING)


    def test_block_to_block_type_heading(self):
        self.verify("# This is a simple heading", BlockType.HEADING)


    def test_code_block_happy(self):
        self.verify("```Happy Test```", BlockType.CODE)


    def test_quote_block_unhappy(self):
        self.verify(">I'm a happy little quote block\n<whoops", BlockType.PARAGRAPH)


    def test_quote_block_single_line(self):
        self.verify(">I'm a happy little quote block", BlockType.QUOTE)


    def test_unordered_list_block_unhappy(self):
        ul_str = "- I\'m a happy little unordered list\n I have 2 items"
        self.verify(ul_str, expected_block_type=BlockType.PARAGRAPH)

    def test_unordered_list_block_happy(self):
        ul_str = "- I\'m a happy little unordered list\n- I have 2 items"
        self.verify(ul_str, expected_block_type=BlockType.UNORDERED_LIST)


    def test_ordered_list_block_happy(self):
        ul_str = "1. I\'m a happy little ordered list\n2. I have 2 items"
        self.verify(ul_str, expected_block_type=BlockType.ORDERED_LIST)


    def test_ordered_list_block_unhappy(self):
        ul_str = "1. I\'m an unhappy little ordered list\n2 . I have 2 items"
        self.verify(ul_str, expected_block_type=BlockType.PARAGRAPH)


    def test_paragraph_block(self):
        self.verify("""> This is not a quote\n- or a list\n# or a heading""", BlockType.PARAGRAPH)

