import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_basic_text(self):
        """Test conversion of plain text"""
        text = "Hello, world!"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "Hello, world!")
        self.assertEqual(nodes[0].text_type, TextType.NORMAL)
    
    def test_bold_text(self):
        """Test conversion of bold text"""
        text = "Hello **world**!"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "Hello ")
        self.assertEqual(nodes[1].text, "world")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text, "!")
    
    def test_italic_text(self):
        """Test conversion of italic text"""
        text = "Hello *world*!"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[1].text_type, TextType.ITALIC)

    def test_italic_text_underscore(self):
        """Test conversion of italic text with underscore syntax"""
        text = "Hello _world_!"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "Hello ")
        self.assertEqual(nodes[1].text, "world")
        self.assertEqual(nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(nodes[2].text, "!")

    def test_bold_text_underscore(self):
        """Test conversion of bold text with underscore syntax"""
        text = "Hello __world__!"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "Hello ")
        self.assertEqual(nodes[1].text, "world")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text, "!")
    
    def test_code_text(self):
        """Test conversion of code text"""
        text = "Hello `world`!"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[1].text_type, TextType.CODE)
    
    def test_link(self):
        """Test conversion of markdown link"""
        text = "Click [here](https://example.com)!"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[1].text, "here")
        self.assertEqual(nodes[1].text_type, TextType.LINK)
        self.assertEqual(nodes[1].url, "https://example.com")
    
    def test_image(self):
        """Test conversion of markdown image"""
        text = "See ![image](pic.jpg) here"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[1].text, "image")
        self.assertEqual(nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(nodes[1].url, "pic.jpg")
    
    def test_complex_markdown(self):
        """Test conversion of complex markdown with multiple elements"""
        text = "This is **bold** with *italic* and `code` plus ![img](pic.jpg) and [link](url.com)"
        nodes = text_to_textnodes(text)

        # Verify sequence of node types
        expected_types = [
            TextType.NORMAL,  # "This is "
            TextType.BOLD,    # "bold"
            TextType.NORMAL,  # " with "
            TextType.ITALIC,  # "italic"
            TextType.NORMAL,  # " and "
            TextType.CODE,    # "code"
            TextType.NORMAL,  # " plus "
            TextType.IMAGE,   # "img"
            TextType.NORMAL,  # " and "
            TextType.LINK,    # "link"
        ]

        actual_types = [node.text_type for node in nodes]
        self.assertEqual(actual_types, expected_types)

    def test_mixed_emphasis_syntax(self):
        """Test conversion of markdown with mixed asterisk and underscore syntax"""
        text = "This is **bold** and __also bold__ with *italic* and _also italic_"
        nodes = text_to_textnodes(text)

        # Verify sequence of node types
        expected_types = [
            TextType.NORMAL,  # "This is "
            TextType.BOLD,    # "bold"
            TextType.NORMAL,  # " and "
            TextType.BOLD,    # "also bold"
            TextType.NORMAL,  # " with "
            TextType.ITALIC,  # "italic"
            TextType.NORMAL,  # " and "
            TextType.ITALIC,  # "also italic"
        ]

        actual_types = [node.text_type for node in nodes]
        self.assertEqual(actual_types, expected_types)

    def test_unmatched_delimiters(self):
        """Test handling of unmatched delimiters"""
        with self.assertRaises(ValueError):
            text_to_textnodes("This **is unmatched")
        with self.assertRaises(ValueError):
            text_to_textnodes("This *is unmatched")
        with self.assertRaises(ValueError):
            text_to_textnodes("This `is unmatched")

if __name__ == "__main__":
    unittest.main()
