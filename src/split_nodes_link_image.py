from textnode import TextNode, TextType
from markdown_parser import extract_markdown_links, extract_markdown_images

def split_nodes_link(old_nodes):
    """
    Split TextNodes that contain markdown links into multiple TextNodes.
    
    Args:
        old_nodes (list): List of TextNode objects to process
        
    Returns:
        list: New list of TextNode objects with links split into separate nodes
    """
    new_nodes = []
    
    for old_node in old_nodes:
        # Skip non-text nodes
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
            
        # Extract all links from the text
        links = extract_markdown_links(old_node.text)
        
        # If no links found, preserve the original node
        if not links:
            new_nodes.append(old_node)
            continue
            
        # Process the text, splitting on each link
        remaining_text = old_node.text
        
        for link_text, link_url in links:
            # Split text before the link
            parts = remaining_text.split(f"[{link_text}]({link_url})", 1)
            
            # Add the text before the link if it exists
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.NORMAL))
                
            # Add the link node
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            
            # Update remaining text
            remaining_text = parts[1] if len(parts) > 1 else ""
            
        # Add any remaining text after the last link
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.NORMAL))
            
    return new_nodes

def split_nodes_image(old_nodes):
    """
    Split TextNodes that contain markdown images into multiple TextNodes.
    
    Args:
        old_nodes (list): List of TextNode objects to process
        
    Returns:
        list: New list of TextNode objects with images split into separate nodes
    """
    new_nodes = []
    
    for old_node in old_nodes:
        # Skip non-text nodes
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
            
        # Extract all images from the text
        images = extract_markdown_images(old_node.text)
        
        # If no images found, preserve the original node
        if not images:
            new_nodes.append(old_node)
            continue
            
        # Process the text, splitting on each image
        remaining_text = old_node.text
        
        for alt_text, image_url in images:
            # Split text before the image
            parts = remaining_text.split(f"![{alt_text}]({image_url})", 1)
            
            # Add the text before the image if it exists
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.NORMAL))
                
            # Add the image node
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, image_url))
            
            # Update remaining text
            remaining_text = parts[1] if len(parts) > 1 else ""
            
        # Add any remaining text after the last image
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.NORMAL))
            
    return new_nodes
