import unittest

from extract_markdown import *

class TestMarkdownExtraction(unittest.TestCase):
    def test_no_links(self):
        text = "This text has no links, just words."
        self.assertEqual(extract_markdown_links(text), [])

    def test_no_links_with_image(self):
        text = "This is just an image without links: ![alt text](https://image.url/img.png)"
        self.assertEqual(extract_markdown_links(text), [])

    def test_no_images(self):
        text = "This text has no images, just words."
        self.assertEqual(extract_markdown_images(text), [])

    def test_no_images_with_link(self):
        text = "This is just a [link](http://example.com) without images."
        self.assertEqual(extract_markdown_images(text), [])

    def test_only_link(self):
        text = "Check this [example](https://example.com)."
        expected_links = [("example", "https://example.com")]
        self.assertEqual(extract_markdown_links(text), expected_links)

    def test_only_image(self):
        text = "Here is an image: ![alt text](https://image.url/img.png)"
        expected_images = [("alt text", "https://image.url/img.png")]
        self.assertEqual(extract_markdown_images(text), expected_images)

    def test_multiple_links(self):
        text = "Links: [Google](https://google.com) and [GitHub](https://github.com)"
        expected_links = [
            ("Google", "https://google.com"),
            ("GitHub", "https://github.com")
        ]
        self.assertEqual(extract_markdown_links(text), expected_links)

    def test_multiple_images(self):
        text = (
            "Images: ![First](https://example.com/1.png) and "
            "![Second](https://example.com/2.png)"
        )
        expected_images = [
            ("First", "https://example.com/1.png"),
            ("Second", "https://example.com/2.png")
        ]
        self.assertEqual(extract_markdown_images(text), expected_images)

    def test_text_with_links_and_images(self):
        text = (
            "Text with [a link](http://link.com) and "
            "![an image](http://img.com/image.jpg). Also another "
            "[second link](http://another.com) and ![second image](http://img.com/2.jpg)."
        )
        expected_links = [
            ("a link", "http://link.com"),
            ("second link", "http://another.com"),
        ]
        expected_images = [
            ("an image", "http://img.com/image.jpg"),
            ("second image", "http://img.com/2.jpg"),
        ]
        self.assertEqual(extract_markdown_links(text), expected_links)
        self.assertEqual(extract_markdown_images(text), expected_images)

if __name__ == "__main__":
    unittest.main()
