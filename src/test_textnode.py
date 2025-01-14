import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("A text node", TextType.ITALIC)
        node2 = TextNode("Other text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_invalid(self):
        with self.assertRaises(AttributeError):
            TextNode("A text node", TextType.DIV)
            TextNode("A text node", True)
            TextNode("A text node", 15) 

    def test_printing(self):
        node = repr(TextNode("A text node", TextType.BOLD, "my.url"))
        printed = "TextNode(A text node, bold, my.url)"
        self.assertEqual(node, printed)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_conversion(self):
        # Test normal text
        node = TextNode("Hello, world!", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "Hello, world!")
        
        # Test bold text
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<b>Bold text</b>")
        
        # Test italic text
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<i>Italic text</i>")
        
        # Test code text
        node = TextNode("Code text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<code>Code text</code>")
        
        # Test link with URL
        node = TextNode("Click me", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(
            html_node.to_html(), 
            '<a href="https://example.com">Click me</a>'
        )
        
        # Test image with URL
        node = TextNode("Alt text", TextType.IMAGE, "image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "image.jpg", "alt": "Alt text"},
        )
    
    def test_invalid_text_type(self):
        # Test missing URL for link
        node = TextNode("Click me", TextType.LINK)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)
        
        # Test missing URL for image
        node = TextNode("Alt text", TextType.IMAGE)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()
