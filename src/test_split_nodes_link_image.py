import unittest
from textnode import TextNode, TextType
from split_nodes_link_image import split_nodes_link, split_nodes_image

class TestSplitNodesLink(unittest.TestCase):
    def test_single_link(self):
        node = TextNode(
            "This is text with a [link](https://example.com) in it",
            TextType.NORMAL
        )
        nodes = split_nodes_link([node])
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "This is text with a ")
        self.assertEqual(nodes[1].text, "link")
        self.assertEqual(nodes[1].url, "https://example.com")
        self.assertEqual(nodes[2].text, " in it")

    def test_multiple_links(self):
        node = TextNode(
            "Here's [one](link1.com) and [two](link2.com) links",
            TextType.NORMAL
        )
        nodes = split_nodes_link([node])
        self.assertEqual(len(nodes), 5)
        self.assertEqual(nodes[1].text, "one")
        self.assertEqual(nodes[1].url, "link1.com")
        self.assertEqual(nodes[3].text, "two")
        self.assertEqual(nodes[3].url, "link2.com")

    def test_no_links(self):
        node = TextNode("Plain text without links", TextType.NORMAL)
        nodes = split_nodes_link([node])
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "Plain text without links")

    def test_non_text_node(self):
        node = TextNode("Already processed", TextType.LINK, "url.com")
        nodes = split_nodes_link([node])
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "Already processed")
        self.assertEqual(nodes[0].url, "url.com")

class TestSplitNodesImage(unittest.TestCase):
    def test_single_image(self):
        node = TextNode(
            "This is text with an ![image](pic.jpg) in it",
            TextType.NORMAL
        )
        nodes = split_nodes_image([node])
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "This is text with an ")
        self.assertEqual(nodes[1].text, "image")
        self.assertEqual(nodes[1].url, "pic.jpg")
        self.assertEqual(nodes[2].text, " in it")

    def test_multiple_images(self):
        node = TextNode(
            "Here's ![one](img1.jpg) and ![two](img2.jpg) images",
            TextType.NORMAL
        )
        nodes = split_nodes_image([node])
        self.assertEqual(len(nodes), 5)
        self.assertEqual(nodes[1].text, "one")
        self.assertEqual(nodes[1].url, "img1.jpg")
        self.assertEqual(nodes[3].text, "two")
        self.assertEqual(nodes[3].url, "img2.jpg")

    def test_no_images(self):
        node = TextNode("Plain text without images", TextType.NORMAL)
        nodes = split_nodes_image([node])
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "Plain text without images")

    def test_non_text_node(self):
        node = TextNode("Already an image", TextType.IMAGE, "img.jpg")
        nodes = split_nodes_image([node])
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "Already an image")
        self.assertEqual(nodes[0].url, "img.jpg")

if __name__ == "__main__":
    unittest.main()
