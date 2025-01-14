import unittest
from block_parser import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_single_block(self):
        """Test parsing a single block without blank lines"""
        text = "This is a single block"
        blocks = markdown_to_blocks(text)
        self.assertEqual(len(blocks), 1)
        self.assertEqual(blocks[0], "This is a single block")
    
    def test_multiple_blocks(self):
        """Test parsing multiple blocks separated by blank lines"""
        text = "Block 1\n\nBlock 2\n\nBlock 3"
        blocks = markdown_to_blocks(text)
        self.assertEqual(len(blocks), 3)
        self.assertEqual(blocks[0], "Block 1")
        self.assertEqual(blocks[1], "Block 2")
        self.assertEqual(blocks[2], "Block 3")
    
    def test_lists(self):
        """Test parsing lists where line breaks are meaningful"""
        text = "* Item 1\n* Item 2\n\nNew block"
        blocks = markdown_to_blocks(text)
        self.assertEqual(len(blocks), 2)
        self.assertEqual(blocks[0], "* Item 1\n* Item 2")
        self.assertEqual(blocks[1], "New block")
    
    def test_whitespace_handling(self):
        """Test handling of various whitespace scenarios"""
        text = "  Block with spaces  \n\n\n  Another block  "
        blocks = markdown_to_blocks(text)
        self.assertEqual(len(blocks), 2)
        self.assertEqual(blocks[0], "Block with spaces")
        self.assertEqual(blocks[1], "Another block")
    
    def test_empty_document(self):
        """Test handling of empty or whitespace-only documents"""
        self.assertEqual(markdown_to_blocks(""), [])
        self.assertEqual(markdown_to_blocks("\n\n  \n"), [])

if __name__ == "__main__":
    unittest.main()
