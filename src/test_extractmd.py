import unittest
from extractmd import extract_markdown_link, extract_markdown_images

class TestExtractLinks(unittest.TestCase):

    def test_extract_markdown_link(self):
        links = extract_markdown_link("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertEqual(len(links), 2)
        self.assertEqual(links[0][0], "to boot dev")
        self.assertEqual(links[0][1], "https://www.boot.dev")
        self.assertEqual(links[1][0], "to youtube")
        self.assertEqual(links[1][1], "https://www.youtube.com/@bootdotdev")


    def test_extract_markdown_image(self):
        images = extract_markdown_images("This is text with an image ![boot dev image](https://www.boot.dev) and ![youtube img](https://www.youtube.com/@bootdotdev)")
        self.assertEqual(len(images), 2)
        self.assertEqual(images[0][0], "boot dev image")
        self.assertEqual(images[0][1], "https://www.boot.dev")
        self.assertEqual(images[1][0], "youtube img")
        self.assertEqual(images[1][1], "https://www.youtube.com/@bootdotdev")

    def test_extract_markdown_image_not_link(self):
        images = extract_markdown_images("This is text with an image ![boot dev image](https://www.boot.dev) and [youtube img](https://www.youtube.com/@bootdotdev)")
        self.assertEqual(len(images), 1)
        self.assertEqual(images[0][0], "boot dev image")
        self.assertEqual(images[0][1], "https://www.boot.dev")


    def test_extract_markdown_link_not_image(self):
        images = extract_markdown_link("This is text with an image ![boot dev image](https://www.boot.dev) and [youtube link](https://www.youtube.com/@bootdotdev)")
        self.assertEqual(len(images), 1)
        self.assertEqual(images[0][0], "youtube link")
        self.assertEqual(images[0][1], "https://www.youtube.com/@bootdotdev")

