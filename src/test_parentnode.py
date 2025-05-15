import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_no_tag(self):
        child = LeafNode("p", "This is a paragraph")
        node = ParentNode(None, [child])
        self.assertRaises(ValueError)

    def test_no_child(self):
        node = ParentNode("p", None)
        self.assertRaises(ValueError)

    def test_one_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_multiple_children(self):
        child_one = LeafNode("span", "child")
        child_two = LeafNode("strong", "bold child")
        child_three = LeafNode("a", "anchor", {
            "href": "https://www.google.com"
        })
        parent_node = ParentNode("div", [
            child_one,
            child_two,
            child_three
        ])

        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span><strong>bold child</strong><a href=\"https://www.google.com\">anchor</a></div>"
        )

    def test_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
            )

    def test_multiple_nested(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        another_child_node = LeafNode("strong", "child")
        parent_node = ParentNode("div", [child_node, another_child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span><strong>child</strong></div>",
            )

    def test_parent_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {
            "class": "container"
        })
        self.assertEqual(parent_node.to_html(), "<div class=\"container\"><span>child</span></div>")

    def child_with_props(self):
        child_node = LeafNode("span", "child", {
            "class": "red"
        })
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span class=\"red\">child</span></div>")
