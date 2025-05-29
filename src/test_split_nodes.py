import unittest

from split_nodes import *
from textnode import *

class TestSplitNodes(unittest.TestCase):
    def test_single_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(result, expected)
    
    def test_single_bold(self):
        node = TextNode("Here is **bold text** in the sentence", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("Here is ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" in the sentence", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_single_italic(self):
        node = TextNode("Some _italic_ words", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = [
            TextNode("Some ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" words", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_single_invalid(self):
        node = TextNode("Unclosed `code block", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_bold_at_start(self):
        node = TextNode("**bold start** and more text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("bold start", TextType.BOLD),
            TextNode(" and more text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_code_at_end(self):
        node = TextNode("Text before a `code snippet`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("Text before a ", TextType.TEXT),
            TextNode("code snippet", TextType.CODE)
        ]
        self.assertEqual(result, expected)
    
    def test_already_formatted_bold(self):
        node = TextNode("Already bold", TextType.BOLD)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [TextNode("Already bold", TextType.BOLD)]
        self.assertEqual(result, expected)

    def test_already_formatted_italic(self):
        node = TextNode("Already italic", TextType.ITALIC)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = [TextNode("Already italic", TextType.ITALIC)]
        self.assertEqual(result, expected)

    def test_already_formatted_code(self):
        node = TextNode("Already code", TextType.CODE)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [TextNode("Already code", TextType.CODE)]
        self.assertEqual(result, expected)

    def test_text_with_no_delimiter(self):
        node = TextNode("Just plain text here", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [TextNode("Just plain text here", TextType.TEXT)]
        self.assertEqual(result, expected)

    def test_multiple(self):
        nodes = [
            TextNode("Start with ", TextType.TEXT),
            TextNode("some `code` snippet", TextType.TEXT),
            TextNode(" and end", TextType.TEXT),
            TextNode("Already formatted", TextType.BOLD)
        ]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        expected = [
            TextNode("Start with ", TextType.TEXT),
            TextNode("some ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" snippet", TextType.TEXT),
            TextNode(" and end", TextType.TEXT),
            TextNode("Already formatted", TextType.BOLD),
        ]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()