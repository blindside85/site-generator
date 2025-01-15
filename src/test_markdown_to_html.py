import unittest
from markdown_to_html import (
    markdown_to_html_node,
    text_to_children,
    paragraph_to_html_node,
    heading_to_html_node,
    code_to_html_node,
    quote_to_html_node,
    unordered_list_to_html_node,
    ordered_list_to_html_node
)
from htmlnode import HTMLNode
from parentnode import ParentNode

class TestMarkdownToHTML(unittest.TestCase):
    def test_text_to_children(self):
        # Test basic text
        nodes = text_to_children("Hello world")
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].value, "Hello world")
        
        # Test text with inline markdown
        nodes = text_to_children("Hello **bold** and *italic*")
        self.assertEqual(len(nodes), 4)
        self.assertEqual(nodes[1].tag, "b")
        self.assertEqual(nodes[3].tag, "i")
        
    def test_paragraph_to_html_node(self):
        # Test basic paragraph
        node = paragraph_to_html_node("Hello world")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.to_html(), "<p>Hello world</p>")
        
        # Test paragraph with inline markdown
        node = paragraph_to_html_node("Hello **world**")
        self.assertEqual(node.to_html(), "<p>Hello <b>world</b></p>")
        
    def test_heading_to_html_node(self):
        # Test different heading levels
        node = heading_to_html_node("# Heading 1")
        self.assertEqual(node.to_html(), "<h1>Heading 1</h1>")
        
        node = heading_to_html_node("### Heading 3")
        self.assertEqual(node.to_html(), "<h3>Heading 3</h3>")
        
    def test_code_to_html_node(self):
        # Test code block
        text = "```\ndef hello():\n    print('Hello')\n```"
        node = code_to_html_node(texblock_typest)
        self.assertEqual(
            node.to_html(),
            "<pre><code>def hello():\n    print('Hello')</code></pre>"
        )
        
    def test_quote_to_html_node(self):
        # Test quote block
        node = quote_to_html_node("> This is a quote")
        self.assertEqual(node.to_html(), "<blockquote>This is a quote</blockquote>")
        
        # Test multi-line quote
        node = quote_to_html_node("> Line 1\n> Line 2")
        self.assertEqual(node.to_html(), "<blockquote>Line 1 Line 2</blockquote>")
        
    def test_unordered_list_to_html_node(self):
        # Test unordered list
        text = "* Item 1\n* Item 2"
        node = unordered_list_to_html_node(text)
        self.assertEqual(
            node.to_html(),
            "<ul><li>Item 1</li><li>Item 2</li></ul>"
        )
        
    def test_ordered_list_to_html_node(self):
        # Test ordered list
        text = "1. First\n2. Second"
        node = ordered_list_to_html_node(text)
        self.assertEqual(
            node.to_html(),
            "<ol><li>First</li><li>Second</li></ol>"
        )
        
    def test_markdown_to_html_node(self):
        # Test complete markdown document
        markdown = """# Title
        
This is a paragraph with **bold** text.

* List item 1
* List item 2

> A quote block

```
Code block
```"""
        
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        
        # Verify essential components
        self.assertIn("<h1>Title</h1>", html)
        self.assertIn("<p>This is a paragraph with <b>bold</b> text.</p>", html)
        self.assertIn("<ul><li>List item 1</li><li>List item 2</li></ul>", html)
        self.assertIn("<blockquote>A quote block</blockquote>", html)
        self.assertIn("<pre><code>Code block</code></pre>", html)

if __name__ == "__main__":
    unittest.main()
