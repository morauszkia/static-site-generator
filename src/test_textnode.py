import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_type_neq(self):
        node1 = TextNode("This is some code", TextType.CODE)
        node2 = TextNode("This is some code", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_text_neq(self):
        link1 = TextNode("This is a link", TextType.LINK, "http://google.com")
        link2 = TextNode("This is another link", TextType.LINK, "http://google.com")
        self.assertNotEqual(link1, link2)
    
    def test_url_neq(self):
        link1 = TextNode("Example link", TextType.LINK, "https://google.com")
        link2 = TextNode("Example link", TextType.LINK, "https://boot.dev")
        self.assertNotEqual(link1, link2)


if __name__ == "__main__":
    unittest.main()