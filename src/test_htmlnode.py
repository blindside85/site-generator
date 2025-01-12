import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        # Test with no properties
        node = HTMLNode(tag="p")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single_prop(self):
        # Test with a single property
        node = HTMLNode(tag="a", props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_multiple_props(self):
        # Test with multiple properties
        node = HTMLNode(
            tag="a",
            props={
                "href": "https://www.google.com",
                "target": "_blank"
            }
        )
        # Check both possible orderings since dictionary order isn't guaranteed
        result = node.props_to_html()
        valid_outputs = [
            ' href="https://www.google.com" target="_blank"',
            ' target="_blank" href="https://www.google.com"'
        ]
        self.assertIn(result, valid_outputs)

    def test_init_default_values(self):
        # Test initialization with default values
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_repr_output(self):
        # Test string representation
        node = HTMLNode(
            tag="p",
            value="Hello",
            props={"class": "greeting"}
        )
        expected = 'HTMLNode(tag=p, value=Hello, children=[], props={\'class\': \'greeting\'})'
        self.assertEqual(repr(node), expected)

if __name__ == "__main__":
    unittest.main()
