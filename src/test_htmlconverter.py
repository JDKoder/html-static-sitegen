from htmlconverter import markdown_to_html_node
import unittest

class TestHTMLConverter(unittest.TestCase):

    def test_paragraphs(self):
        md = """
                This is **bolded** paragraph
                text in a p
                tag here

                This is another paragraph with _italic_ text and `code` here

                """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """```
This is text that _should_ remain
the **same** even with inline stuff
```"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(f"mine: {html}")
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>",
        )

    def test_quote(self):
        md = """> This is a _quote_
        > There are many like it but this one is mine
        > Without me, my quote is nothing
        > Without my quote, **I** am nothing"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a <i>quote</i>\nThere are many like it but this one is mine\nWithout me, my quote is nothing\nWithout my quote, <b>I</b> am nothing</blockquote></div>"
        )


    def test_unordered_list(self):
        md = """- This is an _unordered list_
        - There are many like it but this one is mine
        - Without me, my unordered list is nothing
        - Without my unordered list, **I** am nothing"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is an <i>unordered list</i></li><li>There are many like it but this one is mine</li><li>Without me, my unordered list is nothing</li><li>Without my unordered list, <b>I</b> am nothing</li></ul></div>"
        )


    def test_ordered_list(self):
        md = """1. This is an _ordered list_
        2. There are many like it but this one is mine
        3. Without me, my ordered list is nothing
        4. Without my ordered list, **I** am nothing"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is an <i>ordered list</i></li><li>There are many like it but this one is mine</li><li>Without me, my ordered list is nothing</li><li>Without my ordered list, <b>I</b> am nothing</li></ol></div>"
        )


    def test_header_h1(self):
        md = """# Header"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h1>Header</h1></div>")



    def test_header_h2(self):
        md = """## Header"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h2>Header</h2></div>")


    def test_header_h3(self):
        md = """### Header"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h3>Header</h3></div>")


    def test_header_h4(self):
        md = """#### Header"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h4>Header</h4></div>")


    def test_header_h5(self):
        md = """##### Header"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h5>Header</h5></div>")


    def test_header_h6(self):
        md = """###### Header"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h6>Header</h6></div>")




































