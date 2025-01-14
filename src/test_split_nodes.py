import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_bold(self):
        node = TextNode("This is **bold** text", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.NORMAL),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.NORMAL),
            ]
        )
    
    def test_split_code(self):
        node = TextNode("Hello `code` world", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("Hello ", TextType.NORMAL),
                TextNode("code", TextType.CODE),
                TextNode(" world", TextType.NORMAL),
            ]
        )
        
    def test_multiple_delimiters(self):
        node = TextNode("Hello `code` world `more code`", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("Hello ", TextType.NORMAL),
                TextNode("code", TextType.CODE),
                TextNode(" world ", TextType.NORMAL),
                TextNode("more code", TextType.CODE),
            ]
        )
        
    def test_unmatched_delimiter(self):
        node = TextNode("This is **bold text", TextType.NORMAL)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)
            
    def test_preserve_other_nodes(self):
        nodes = [
            TextNode("Hello ", TextType.NORMAL),
            TextNode("world", TextType.BOLD),
            TextNode(" with `code`", TextType.NORMAL),
        ]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("Hello ", TextType.NORMAL),
                TextNode("world", TextType.BOLD),
                TextNode(" with ", TextType.NORMAL),
                TextNode("code", TextType.CODE),
            ]
        )

if __name__ == "__main__":
    unittest.main()
