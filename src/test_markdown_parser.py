import unittest
from markdown_parser import extract_markdown_images, extract_markdown_links

class TestMarkdownParser(unittest.TestCase):
    def test_extract_markdown_images(self):
        # Test basic image extraction
        text = "![alt text](image.jpg)"
        self.assertEqual(
            extract_markdown_images(text),
            [("alt text", "image.jpg")]
        )
        
        # Test multiple images
        text = "![img1](url1.jpg) ![img2](url2.jpg)"
        self.assertEqual(
            extract_markdown_images(text),
            [("img1", "url1.jpg"), ("img2", "url2.jpg")]
        )
        
        # Test with surrounding text
        text = "Here's an ![image](pic.jpg) in text"
        self.assertEqual(
            extract_markdown_images(text),
            [("image", "pic.jpg")]
        )
        
        # Test with no images
        text = "Just plain text"
        self.assertEqual(extract_markdown_images(text), [])

        text = "[not an image](image.jpg)"
        self.assertEqual(extract_markdown_images(text), [])
        
    def test_extract_markdown_links(self):
        # Test basic link extraction
        text = "[Boot.dev](https://boot.dev)"
        self.assertEqual(
            extract_markdown_links(text),
            [("Boot.dev", "https://boot.dev")]
        )
        
        # Test multiple links
        text = "[link1](url1.com) [link2](url2.com)"
        self.assertEqual(
            extract_markdown_links(text),
            [("link1", "url1.com"), ("link2", "url2.com")]
        )
        
        # Test with surrounding text
        text = "Click [here](link.com) for more"
        self.assertEqual(
            extract_markdown_links(text),
            [("here", "link.com")]
        )
        
        # Test with no links
        text = "Just plain text"
        self.assertEqual(extract_markdown_links(text), [])
        
        # Test with image (should not extract)
        text = "![alt](img.jpg)"
        self.assertEqual(extract_markdown_links(text), [])

if __name__ == "__main__":
    unittest.main()
