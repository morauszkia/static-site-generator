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

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_trailing_text(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png), and trailing text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(", and trailing text", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_split_images_with_link(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png), and a [link](https://www.google.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(
                    ", and a [link](https://www.google.com)", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_split_image_multiple_nodes(self):
        nodes = [
            TextNode("Image ![1](a.png)", TextType.TEXT),
            TextNode(" and ![2](b.png)", TextType.TEXT),
        ]
        result = split_nodes_image(nodes)
        self.assertListEqual(
            [
                TextNode("Image ", TextType.TEXT),
                TextNode("1", TextType.IMAGE, "a.png"),
                TextNode(" and ", TextType.TEXT),
                TextNode("2", TextType.IMAGE, "b.png"),
            ],
            result,
        )

    def test_split_links(self):
        node = TextNode("Here are links to [Google](https://www.google.com) and [Boot.dev](https://boot.dev)", TextType.TEXT)
        result = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Here are links to ", TextType.TEXT),
                TextNode("Google", TextType.LINK, "https://www.google.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("Boot.dev", TextType.LINK, "https://boot.dev"),
            ],
            result,
        )

    def test_split_links_trailing_text(self):
        node = TextNode("Here are links to [Google](https://www.google.com) and [Boot.dev](https://boot.dev), and some trailing text", TextType.TEXT)
        result = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Here are links to ", TextType.TEXT),
                TextNode("Google", TextType.LINK, "https://www.google.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("Boot.dev", TextType.LINK, "https://boot.dev"),
                TextNode(", and some trailing text", TextType.TEXT)
            ],
            result,
        )

    def test_split_links_with_image(self):
        node = TextNode("Here are links to [Google](https://www.google.com) and [Boot.dev](https://boot.dev), and an image: ![alt text](image.png)", TextType.TEXT)
        result = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Here are links to ", TextType.TEXT),
                TextNode("Google", TextType.LINK, "https://www.google.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("Boot.dev", TextType.LINK, "https://boot.dev"),
                TextNode(", and an image: ![alt text](image.png)", TextType.TEXT)
            ],
            result,
        )
        
    # Multiple nodes
    def test_split_link_multiple_nodes(self):
        nodes = [
            TextNode("Link to [Google](https://www.google.com)", TextType.TEXT),
            TextNode(" and [Boot.dev](https://boot.dev)", TextType.TEXT),
        ]
        result = split_nodes_link(nodes)
        self.assertListEqual(
            [
                TextNode("Link to ", TextType.TEXT),
                TextNode("Google", TextType.LINK, "https://www.google.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("Boot.dev", TextType.LINK, "https://boot.dev"),
            ],
            result,
        )
    # Extract images and then links
    def test_split_links_and_images_both(self):
        node = TextNode(
            "This is a link to [Google](https://www.google.com), an ![example image](https://example.com/image.png), and another link to [GitHub](https://github.com).",
            TextType.TEXT
        )

        link_split_nodes = split_nodes_link([node])
        final_nodes = split_nodes_image(link_split_nodes)

        self.assertListEqual(
            [
                TextNode("This is a link to ", TextType.TEXT),
                TextNode("Google", TextType.LINK, "https://www.google.com"),
                TextNode(", an ", TextType.TEXT),
                TextNode("example image", TextType.IMAGE, "https://example.com/image.png"),
                TextNode(", and another link to ", TextType.TEXT),
                TextNode("GitHub", TextType.LINK, "https://github.com"),
                TextNode(".", TextType.TEXT),
            ],
            final_nodes
        )

if __name__ == '__main__':
    unittest.main()