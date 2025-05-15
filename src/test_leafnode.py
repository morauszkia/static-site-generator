import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p_prop(self):
        node = LeafNode("p", "Hello, world!", { "class": "highlighted" })
        self.assertEqual(node.to_html(), '<p class="highlighted">Hello, world!</p>')

    def test_leaf_to_html_a_prop(self):
        node = LeafNode("a", "Hello, world!", { "href": "https://boot.dev" })
        self.assertEqual(node.to_html(), '<a href="https://boot.dev">Hello, world!</a>')

    def test_leaf_to_html_a_multiple_props(self):
        node = LeafNode("a", "Hello, world!", { 
            "href": "https://boot.dev",
            "target": "_blank"
            })
        self.assertEqual(node.to_html(), '<a href="https://boot.dev" target="_blank">Hello, world!</a>')

    def test_leaf_no_value(self):
        _ = LeafNode("a", None)
        self.assertRaises(ValueError)

    def test_leaf_no_tag(self):
        node = LeafNode(None, "This is raw text")
        self.assertEqual(node.to_html(), "This is raw text")