import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_node_initialization(self):
        # Test valid initialization
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello, world!")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_leaf_node_with_props(self):
        # Test initialization with properties
        node = LeafNode(
            "a",
            "Click me!",
            {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "Click me!")
        self.assertEqual(node.props["href"], "https://www.google.com")

    def test_leaf_node_no_value(self):
        # Test that initialization without a value raises ValueError
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_to_html_basic(self):
        # Test basic HTML rendering
        node = LeafNode("p", "This is a paragraph")
        self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")

    def test_to_html_with_props(self):
        # Test HTML rendering with properties
        node = LeafNode(
            "a",
            "Click me!",
            {"href": "https://www.google.com"}
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
        )

    def test_to_html_no_tag(self):
        # Test rendering with no tag (raw text)
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")

if __name__ == "__main__":
    unittest.main()
