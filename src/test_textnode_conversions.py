import unittest

from textnode import *
from textnode_conversions import *


class TestTextNodeConversions(unittest.TestCase):
    def test_text_to_node_simple(self):
        text = "Just plain text with no formatting."
        result = text_to_textnodes(text)
        expected = [TextNode("Just plain text with no formatting.", TextType.TEXT)]
        self.assertEqual(result, expected)

    def test_text_to_node_bold(self):
        text = "This is **bold text** only."
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" only.", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_text_to_node_italic(self):
        text = "This is _italic text_ only."
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
            TextNode(" only.", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_text_to_node_code(self):
        text = "Here is `code_snippet` alone."
        result = text_to_textnodes(text)
        expected = [
            TextNode("Here is ", TextType.TEXT),
            TextNode("code_snippet", TextType.CODE),
            TextNode(" alone.", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_text_to_node_image(self):
        text = "Look at this image: ![alt](http://example.com/img.png)"
        result = text_to_textnodes(text)
        expected = [
            TextNode("Look at this image: ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, "http://example.com/img.png"),
        ]
        self.assertEqual(result, expected)

    def test_text_to_node_link(self):
        text = "Visit [Google](https://www.google.com) now."
        result = text_to_textnodes(text)
        expected = [
            TextNode("Visit ", TextType.TEXT),
            TextNode("Google", TextType.LINK, "https://www.google.com"),
            TextNode(" now.", TextType.TEXT),
        ]
        self.assertEqual(result, expected)
    
    def test_text_to_node_bold_invalid(self):
        text = "This is **unclosed bold"
        with self.assertRaises(Exception):
            text_to_textnodes(text)

    def test_text_to_node(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(result, expected)

    def test_text_to_html_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_to_html_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_text_to_html_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_text_to_html_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")
    
    def test_text_to_html_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props["href"], "https://www.google.com")

    def test_text_to_html_image(self):
        node = TextNode("This is alt text", TextType.IMAGE, "./image.jpeg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "./image.jpeg")
        self.assertEqual(html_node.props["alt"], "This is alt text")

    def test_text_to_html_link_missing_href(self):
        node = TextNode("This is a link", TextType.LINK)
        with self.assertRaises(ValueError):
            html_node = text_node_to_html_node(node)

    def test_text_to_html_image_missing_src(self):
        node = TextNode("This is an image", TextType.IMAGE)
        with self.assertRaises(ValueError):
            html_node = text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()