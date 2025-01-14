def markdown_to_blocks(markdown):
    """
    Split markdown text into blocks based on blank lines.
    A block is a piece of text separated by blank lines.
    
    Args:
        markdown (str): Complete markdown document
        
    Returns:
        list: List of strings, each representing a markdown block
        
    Example:
        >>> text = "# Header\\n\\nParagraph\\n\\n* List item"
        >>> markdown_to_blocks(text)
        ['# Header', 'Paragraph', '* List item']
    """
    # First, split the text into lines and combine them into blocks
    lines = markdown.split('\n')
    blocks = []
    current_block = []
    
    for line in lines:
        # If we hit an empty line, start a new block
        if line.strip() == '' and current_block:
            # Join the lines in the current block and add to blocks
            blocks.append('\n'.join(current_block))
            current_block = []
        # If it's not an empty line, add to current block
        elif line.strip() != '':
            current_block.append(line)
    
    # Add the last block if there is one
    if current_block:
        blocks.append('\n'.join(current_block))
    
    # Strip any whitespace from the blocks
    blocks = [block.strip() for block in blocks]
    
    # Filter out any empty blocks
    blocks = [block for block in blocks if block]
    
    return blocks
