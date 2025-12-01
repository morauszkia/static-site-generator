import unittest

from md_to_html import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>",
        )

    def test_unordered_list(self):
        md = """
- Item one with **bold** text
- Item _two_ with `inline code`
- Item three with a [link](https://example.com) and an ![alt](img.png)
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item one with <b>bold</b> text</li><li>Item <i>two</i> with <code>inline code</code></li><li>Item three with a <a href=\"https://example.com\">link</a> and an <img src=\"img.png\" alt=\"alt\"></li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. First **bold** item
2. Second with _italic_ and [link](https://example.com)
3. Third containing `code` and an image ![pic](pic.jpg)
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First <b>bold</b> item</li><li>Second with <i>italic</i> and <a href=\"https://example.com\">link</a></li><li>Third containing <code>code</code> and an image <img src=\"pic.jpg\" alt=\"pic\"></li></ol></div>",
        )

    def test_blockquote(self):
        md = """
> This is a blockquote with **bold**, _italic_, `code`,
> a [link](https://example.com), and an image ![alt](img.png)
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote with <b>bold</b>, <i>italic</i>, <code>code</code>,\na <a href=\"https://example.com\">link</a>, and an image <img src=\"img.png\" alt=\"alt\"></blockquote></div>",
        )
    
    def test_h1(self):
        md = "# Heading One with **bold** and _italic_"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading One with <b>bold</b> and <i>italic</i></h1></div>",
        )

    def test_h3(self):
        md = "### Heading Three with [link](https://example.com)"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>Heading Three with <a href=\"https://example.com\">link</a></h3></div>",
        )
    
    def test_h6(self):
        md = "###### Heading Six with `inline code`"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h6>Heading Six with <code>inline code</code></h6></div>",
        )
    
    def test_complex_markdown(self):
        md = """
# Main Title with **bold**

Some paragraph text with _italic_, `code`, and a [link](https://example.com).

## Subheading With Image

Here is an image: ![logo](logo.png)

- First list item with **bold**
- Second item with _italic_ and `code`
- Third with [link](https://example.com) and image ![img](pic.jpg)

1. Ordered **one**
2. Ordered _two_
3. Ordered `three`

> Quoted text with **bold** and a link to [site](https://example.com)

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div>" +
            "<h1>Main Title with <b>bold</b></h1>" +
            "<p>Some paragraph text with <i>italic</i>, <code>code</code>, and a " +
            "<a href=\"https://example.com\">link</a>.</p>" +
            "<h2>Subheading With Image</h2>" +
            "<p>Here is an image: <img src=\"logo.png\" alt=\"logo\"></p>" +
            "<ul>" +
            "<li>First list item with <b>bold</b></li>" +
            "<li>Second item with <i>italic</i> and <code>code</code></li>" +
            "<li>Third with <a href=\"https://example.com\">link</a> and image " +
            "<img src=\"pic.jpg\" alt=\"img\"></li>" +
            "</ul>" +
            "<ol>" +
            "<li>Ordered <b>one</b></li>" +
            "<li>Ordered <i>two</i></li>" +
            "<li>Ordered <code>three</code></li>" +
            "</ol>" +
            "<blockquote>" +
            "Quoted text with <b>bold</b> and a link to <a href=\"https://example.com\">site</a>"
            "</blockquote>" +
            "</div>",
        )