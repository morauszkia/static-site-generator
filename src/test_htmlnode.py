import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_no_prop(self):
        node = HTMLNode("p", "This is just text.")
        expected_props = ""
        actual_props = node.props_to_html()
        self.assertEqual(actual_props, expected_props)

    def test_single_prop(self):
        node1 = HTMLNode("a", "Google", None, { "href": "https://www.google.com"})
        expected_props1 = ' href="https://www.google.com"'
        actual_props1 = node1.props_to_html()

        node2 = HTMLNode("p", "This is a paragraph", None, { "class": "highlighted" })
        expected_props2 = ' class="highlighted"'
        actual_props2 = node2.props_to_html()

        self.assertEqual(actual_props1, expected_props1)
        self.assertEqual(actual_props2, expected_props2)

    def test_two_props(self):
        node1 = HTMLNode("a", "Boot.dev", None, {
            "href": "https://www.boot.dev",
            "target": "_blank"
        })
        expected_props1 = ' href="https://www.boot.dev" target="_blank"'
        actual_props1 = node1.props_to_html()

        self.assertEqual(actual_props1, expected_props1)