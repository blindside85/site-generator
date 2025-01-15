import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_basic_title(self):
        """Test extracting a simple h1 header"""
        markdown = "# My Title"
        self.assertEqual(extract_title(markdown), "My Title")
    
    def test_title_with_extra_whitespace(self):
        """Test handling of extra whitespace"""
        markdown = "#    Spacey   Title    "
        self.assertEqual(extract_title(markdown), "Spacey   Title")
    
    def test_title_with_other_content(self):
        """Test extracting title from full document"""
        markdown = """# Main Title
        
        ## Section 1
        Some content here
        
        ## Section 2
        More content
        """
        self.assertEqual(extract_title(markdown), "Main Title")
    
    def test_missing_title(self):
        """Test handling of missing h1 header"""
        markdown = """## Not a main title
        Just some content
        """
        with self.assertRaises(ValueError):
            extract_title(markdown)
    
    def test_title_with_hash_in_content(self):
        """Test handling of # characters in content"""
        markdown = """# Title with # symbol
        ## Subtitle
        """
        self.assertEqual(extract_title(markdown), "Title with # symbol")
    
    def test_empty_document(self):
        """Test handling of empty document"""
        with self.assertRaises(ValueError):
            extract_title("")

if __name__ == "__main__":
    unittest.main()
