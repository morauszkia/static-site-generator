import unittest

from block_conversions import *

class TestBlockConversions(unittest.TestCase):
    def test_md_to_blocks(self):
        md = """
# This is a heading

This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_md_to_blocks_empty(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_heading(self):
        self.assertEqual(block_to_blocktype("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_blocktype("### Heading 3"), BlockType.HEADING)
        self.assertEqual(block_to_blocktype("###### Heading 6"), BlockType.HEADING)

    def test_block_to_code(self):
        code = "```\nprint('Hello')\n```"
        self.assertEqual(block_to_blocktype(code), BlockType.CODE)
        self.assertEqual(block_to_blocktype("```code snippet```"), BlockType.CODE)

    def test_block_to_quote(self):
        quote = "> This is a quote\n> Continued quote"
        self.assertEqual(block_to_blocktype(quote), BlockType.QUOTE)

    def test_block_to_unordered_list(self):
        ul = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_blocktype(ul), BlockType.UNORDERED_LIST)

    def test_block_to_ordered_list(self):
        ol = "1. First\n2. Second\n3. Third"
        self.assertEqual(block_to_blocktype(ol), BlockType.ORDERED_LIST)

    def test_block_to_paragraph(self):
        para = "This is just a regular paragraph.\nIt spans multiple lines but has no special formatting."
        self.assertEqual(block_to_blocktype(para), BlockType.PARAGRAPH)

    def test_block_to_paragraph_from_mixed_list(self):
        mixed = "- Item\n1. Ordered"
        self.assertEqual(block_to_blocktype(mixed), BlockType.PARAGRAPH)

    def test_block_to_quote_with_empty_lines(self):
        quote = "> Quote line\n>\n> Another quote line"
        self.assertEqual(block_to_blocktype(quote), BlockType.QUOTE)

    def test_block_to_paragraph_from_incomplete_code(self):
        incomplete_code = "```\ndef hello():\n  pass"
        self.assertEqual(block_to_blocktype(incomplete_code), BlockType.PARAGRAPH)

    def test_block_to_paragraph_from_malformed_heading(self):
        not_heading = "####This is not a heading"
        self.assertEqual(block_to_blocktype(not_heading), BlockType.PARAGRAPH)

    def test_block_to_paragraph_another_malformed_heading(self):
        not_heading = "####### This is also not a heading"
        self.assertEqual(block_to_blocktype(not_heading), BlockType.PARAGRAPH)
   
    def test_block_to_paragraph_malformed_list(self):
        not_list = "-This is\n-Not a\n-valid list"
        self.assertEqual(block_to_blocktype(not_list), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()