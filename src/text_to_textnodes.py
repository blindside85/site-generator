from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter
from split_nodes_link_image import split_nodes_link, split_nodes_image

def text_to_textnodes(text):
    """
    Convert a markdown-flavored text string into a list of TextNode objects.
    
    The function processes the text in stages:
    1. Creates initial text node
    2. Splits on image markdown
    3. Splits on link markdown
    4. Splits on delimiter pairs (**, *, `)
    
    Args:
        text (str): Markdown-flavored text to parse
        
    Returns:
        list: List of TextNode objects representing the parsed text
    
    Example:
        >>> text = "Hello **world** with [link](url.com)"
        >>> nodes = text_to_textnodes(text)
        >>> [node.text_type for node in nodes]
        [TextType.TEXT, TextType.BOLD, TextType.TEXT, TextType.LINK]
    """
    # Start with a single text node
    nodes = [TextNode(text, TextType.NORMAL)]
    
    # Split on image markdown first (images can't contain other markdown)
    nodes = split_nodes_image(nodes)
    
    # Split on link markdown next (links can't contain other markdown)
    nodes = split_nodes_link(nodes)
    
    # Split on markdown delimiters
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    return nodes
