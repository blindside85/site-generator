import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_basic_parent_node(self):
        node = ParentNode(
            "div",
            [LeafNode("p", "Hello, world!")]
        )
        self.assertEqual(node.to_html(), "<div><p>Hello, world!</p></div>")
    
    def test_nested_parent_nodes(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "section",
                    [LeafNode("p", "Nested content")]
                )
            ]
        )
        self.assertEqual(
            node.to_html(), 
            "<div><section><p>Nested content</p></section></div>"
        )
    
    def test_multiple_children(self):
        node = ParentNode(
            "nav",
            [
                LeafNode("a", "Home"),
                LeafNode("a", "About"),
                LeafNode("a", "Contact")
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<nav><a>Home</a><a>About</a><a>Contact</a></nav>"
        )
    
    def test_with_props(self):
        node = ParentNode(
            "div",
            [LeafNode("p", "Content")],
            {"class": "container"}
        )
        self.assertEqual(
            node.to_html(),
            '<div class="container"><p>Content</p></div>'
        )
    
    def test_invalid_construction(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [])  # No tag
        with self.assertRaises(ValueError):
            ParentNode("div", None)  # No children
        with self.assertRaises(ValueError):
            ParentNode("div", "not a list")  # Invalid children type

if __name__ == "__main__":
    unittest.main()
