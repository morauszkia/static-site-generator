import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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