import unittest

from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()
