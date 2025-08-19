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


