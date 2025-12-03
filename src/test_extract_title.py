import unittest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_single_start(self):
        md="# My Title\n\nThis is a paragraph.\n\nThis is another one."
        title = extract_title(md)
        self.assertEqual(title, "My Title")

    def test_single_middle(self):
        md="This is not the title\n\n# My Title\n\nThis is a paragraph.\n\nThis is another one."
        title = extract_title(md)
        self.assertEqual(title, "My Title")

    def test_single_with_spaces(self):
        md="#   My Title   \n\nThis is a paragraph.\n\nThis is another one."
        title = extract_title(md)
        self.assertEqual(title, "My Title")

    def test_title_with_tabs(self):
        md="#\tMy Title\t\n\nThis is a paragraph.\n\nThis is another one."
        title = extract_title(md)
        self.assertEqual(title, "My Title")

    def test_multiple_titles(self):
        md="# My Title\n\nThis is a paragraph.\n\n# This should not be a title"
        title = extract_title(md)
        self.assertEqual(title, "My Title")

    def test_no_title(self):
        md="This is a paragraph.\n\nThis is another one."
        with self.assertRaises(Exception) as context:
            extract_title(md)
        self.assertEqual(str(context.exception), "No valid title found in markdown")

    def test_invalid_format(self):
        md="    # This should start at the beginning of the line\n\nThis is a paragraph."
        with self.assertRaises(Exception) as context:
            extract_title(md)
        self.assertEqual(str(context.exception), "No valid title found in markdown")

    def test_empty_title(self):
        md="# \n\nThis is a paragraph.\n\nThis is another one."
        with self.assertRaises(Exception) as context:
            extract_title(md)
        self.assertEqual(str(context.exception), "Invalid title: Title cannot be empty")

    def test_first_title_empty(self):
        md="#     \n\n# Valid Title\n\nThis is a paragraph."
        with self.assertRaises(Exception) as context:
            extract_title(md)
        self.assertEqual(str(context.exception), "Invalid title: Title cannot be empty")

    def test_level_two_heading(self):
        md="## Subtitle\n\nThis is a paragraph."
        with self.assertRaises(Exception) as context:
            extract_title(md)
        self.assertEqual(str(context.exception), "No valid title found in markdown")

    def test_first_heading_not_title(self):
        md="## Not a Title\n\n# Valid Title\n\nThis is a paragraph."
        title = extract_title(md)
        self.assertEqual(title, "Valid Title")

    def test_title_with_special_characters(self):
        md="# My Title! @2024 #StaticSiteGenerator\n\nThis is a paragraph."
        title = extract_title(md)
        self.assertEqual(title, "My Title! @2024 #StaticSiteGenerator")

    def test_title_with_markdown(self):
        md="# **Bold Title** with _Italics_ and `Code`\n\nThis is a paragraph."
        title = extract_title(md)
        self.assertEqual(title, "**Bold Title** with _Italics_ and `Code`")

    def test_title_with_emoji(self):
        md="# My Title 😊🚀\n\nThis is a paragraph."
        title = extract_title(md)
        self.assertEqual(title, "My Title 😊🚀")

    def test_utf8_title(self):
        md="# Egy gyűrű mind fölött\n\nThis is a paragraph."
        title = extract_title(md)
        self.assertEqual(title, "Egy gyűrű mind fölött")

    # TODO: Invalid markdown in title
    # TODO: Valid markdown in title: code, bold, italics, link
    # TODO: 