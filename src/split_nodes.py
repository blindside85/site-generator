from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Split text nodes based on a delimiter and assign the specified text type.
    
    Args:
        old_nodes (list): List of TextNode objects to process
        delimiter (str): The delimiter to split on (e.g. "**" for bold)
        text_type (TextType): The TextType to assign to text between delimiters
        
    Returns:
        list: New list of TextNode objects with text split on delimiters
        
    Raises:
        ValueError: If text contains an unmatched delimiter
    """
    new_nodes = []
    
    for old_node in old_nodes:
        # Only process TEXT nodes - pass through others unchanged
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
            
        # Split node text on delimiter
        pieces = old_node.text.split(delimiter)
        
        # No delimiters found - keep text as-is
        if len(pieces) == 1:
            new_nodes.append(old_node)
            continue
            
        # Must have even number of delimiters for matching pairs
        if len(pieces) % 2 == 0:
            raise ValueError(f"Found unmatched delimiter {delimiter}")
            
        # Process pieces alternating between text and delimited
        for i, piece in enumerate(pieces):
            if piece == "":
                continue
                
            # Even indices are normal text, odd indices are delimited
            text_node_type = text_type if i % 2 else TextType.NORMAL
            new_nodes.append(TextNode(piece, text_node_type))
            
    return new_nodes
