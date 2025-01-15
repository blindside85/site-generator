from typing import List
from textnode import TextNode, text_node_to_html_node
from text_to_textnodes import text_to_textnodes
from block_parser import markdown_to_blocks
from block_to_block import block_to_block_type, BlockType
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode

def text_to_children(text: str) -> List[HTMLNode]:
    """
    Convert a text string with inline markdown to a list of HTMLNode objects.
    
    Args:
        text (str): The text to convert
        
    Returns:
        List[HTMLNode]: List of HTML nodes representing the text
    """
    nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in nodes]

def paragraph_to_html_node(text: str) -> HTMLNode:
    """
    Convert a paragraph block to an HTMLNode.
    
    Args:
        text (str): The paragraph text
        
    Returns:
        HTMLNode: A paragraph node with child nodes for inline markdown
    """
    children = text_to_children(text)
    return ParentNode("p", children)

def heading_to_html_node(text: str) -> HTMLNode:
    """
    Convert a heading block to an HTMLNode.
    
    Args:
        text (str): The heading text including '#' characters
        
    Returns:
        HTMLNode: A heading node with the appropriate heading level
    """
    # Count the number of # characters at the start
    level = 0
    for char in text:
        if char == "#":
            level += 1
        else:
            break
            
    # Remove the # characters and any following spaces
    content = text[level:].strip()
    
    # Create heading node with appropriate h1-h6 tag
    children = text_to_children(content)
    return ParentNode(f"h{level}", children)

def code_to_html_node(text: str) -> HTMLNode:
    """
    Convert a code block to nested pre and code HTMLNodes.
    
    Args:
        text (str): The code block text including ``` delimiters
        
    Returns:
        HTMLNode: A pre node containing a code node
    """
    # Remove the ``` delimiters and any language specification
    content = text.split("\n", 1)[1].rsplit("\n", 1)[0]
    
    # Create the nested structure: <pre><code>content</code></pre>
    code_node = ParentNode("code", [LeafNode(None, content)])
    return ParentNode("pre", [code_node])

def quote_to_html_node(text: str) -> HTMLNode:
    """
    Convert a quote block to an HTMLNode.
    
    Args:
        text (str): The quote text with > characters
        
    Returns:
        HTMLNode: A blockquote node
    """
    # Remove the > characters and any following spaces
    lines = [line.lstrip("> ").strip() for line in text.split("\n")]
    content = " ".join(lines)
    
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def list_item_to_html_node(text: str) -> HTMLNode:
    """
    Convert a single list item to an HTMLNode.
    Expects text without list markers.
    """
    # No need to strip markers - they're already removed
    children = text_to_children(text.strip())
    return ParentNode("li", children)

def unordered_list_to_html_node(text: str) -> HTMLNode:
    """
    Convert an unordered list block to an HTMLNode.
    Preprocesses list markers before passing to item processor.
    """
    items = []
    for line in text.split("\n"):
        line = line.strip()
        # Remove marker here, so list_item_to_html_node gets clean text
        if line.startswith(('* ', '- ')):
            items.append(line[2:])
        else:
            items.append(line)
            
    children = [list_item_to_html_node(item) for item in items]
    return ParentNode("ul", children)

def ordered_list_to_html_node(text: str) -> HTMLNode:
    """
    Convert an ordered list block to an HTMLNode.
    Properly preprocesses number markers for list items.
    
    Args:
        text (str): The full list text with number markers (e.g., "1. First\n2. Second")
        
    Returns:
        HTMLNode: An ol node containing li nodes
        
    Example:
        >>> text = "1. First item\\n2. Second item"
        >>> node = ordered_list_to_html_node(text)
        >>> node.to_html()
        '<ol><li>First item</li><li>Second item</li></ol>'
    """
    items = []
    for line in text.split("\n"):
        line = line.strip()
        # Match any number followed by period and space
        if line and line[0].isdigit():
            # Find the position after the period and space
            marker_end = line.find('. ')
            if marker_end != -1:
                items.append(line[marker_end + 2:])
            else:
                items.append(line)
        else:
            items.append(line)
            
    children = [list_item_to_html_node(item) for item in items]
    return ParentNode("ol", children)

def markdown_to_html_node(markdown: str) -> HTMLNode:
    """
    Convert a full markdown document to a single HTML node.
    
    Args:
        markdown (str): The complete markdown document
        
    Returns:
        HTMLNode: A div node containing all converted content
    """
    blocks = markdown_to_blocks(markdown)
    children = []
    
    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == BlockType.PARAGRAPH.value:
            children.append(paragraph_to_html_node(block))
        elif block_type == BlockType.HEADING.value:
            children.append(heading_to_html_node(block))
        elif block_type == BlockType.CODE.value:
            children.append(code_to_html_node(block))
        elif block_type == BlockType.QUOTE.value:
            children.append(quote_to_html_node(block))
        elif block_type == BlockType.UNORDERED_LIST.value:
            children.append(unordered_list_to_html_node(block))
        elif block_type == BlockType.ORDERED_LIST.value:
            children.append(ordered_list_to_html_node(block))
            
    return ParentNode("div", children)
