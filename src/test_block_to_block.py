import unittest
from block_to_block import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        text = "This is a regular paragraph."
        self.assertEqual(block_to_block_type(text), "paragraph")
        
        # Test multi-line paragraph
        text = "This is a\nmulti-line\nparagraph."
        self.assertEqual(block_to_block_type(text), "paragraph")
        
        # Test empty block
        self.assertEqual(block_to_block_type(""), "paragraph")
        
    def test_heading(self):
        # Test different heading levels
        self.assertEqual(block_to_block_type("# Heading 1"), "heading")
        self.assertEqual(block_to_block_type("## Heading 2"), "heading")
        self.assertEqual(block_to_block_type("###### Heading 6"), "heading")
        
        # Test invalid headings
        self.assertEqual(block_to_block_type("#Missing space"), "paragraph")
        self.assertEqual(block_to_block_type("####### Too many"), "paragraph")
        
    def test_code(self):
        # Test basic code block
        text = "```\ndef hello():\n    print('Hello')\n```"
        self.assertEqual(block_to_block_type(text), "code")
        
        # Test with language specification
        text = "```python\ndef hello():\n    print('Hello')\n```"
        self.assertEqual(block_to_block_type(text), "code")
        
        # Test invalid code blocks
        self.assertEqual(block_to_block_type("```\nUnclosed code block"), "paragraph")
        self.assertEqual(block_to_block_type("`Not a code block`"), "paragraph")
        
    def test_quote(self):
        # Test single line quote
        self.assertEqual(block_to_block_type("> This is a quote"), "quote")
        
        # Test multi-line quote
        text = "> Line 1\n> Line 2\n> Line 3"
        self.assertEqual(block_to_block_type(text), "quote")
        
        # Test invalid quotes
        self.assertEqual(block_to_block_type(">Missing space"), "quote")
        self.assertEqual(block_to_block_type("> Mixed\nNon-quote line"), "paragraph")
        
    def test_unordered_list(self):
        # Test single item
        self.assertEqual(block_to_block_type("* List item"), "unordered_list")
        self.assertEqual(block_to_block_type("- List item"), "unordered_list")
        
        # Test multiple items
        text = "* Item 1\n* Item 2\n* Item 3"
        self.assertEqual(block_to_block_type(text), "unordered_list")
        text = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(text), "unordered_list")
        
        # Test invalid lists
        self.assertEqual(block_to_block_type("*Missing space"), "paragraph")
        self.assertEqual(block_to_block_type("* Mixed\nNon-list line"), "paragraph")
        
    def test_ordered_list(self):
        # Test single item
        self.assertEqual(block_to_block_type("1. First item"), "ordered_list")
        
        # Test multiple items
        text = "1. First\n2. Second\n3. Third"
        self.assertEqual(block_to_block_type(text), "ordered_list")
        
        # Test invalid ordered lists
        self.assertEqual(block_to_block_type("1.Missing space"), "paragraph")
        self.assertEqual(block_to_block_type("1. First\n3. Third"), "paragraph")
        self.assertEqual(block_to_block_type("2. Wrong start"), "paragraph")

if __name__ == "__main__":
    unittest.main()
