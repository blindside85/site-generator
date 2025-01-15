def extract_title(markdown):
    """
    Extract the h1 header from a markdown document.
    
    Args:
        markdown (str): Markdown content containing an h1 header
        
    Returns:
        str: The text content of the h1 header
        
    Raises:
        ValueError: If no h1 header is found
    """
    # Split into lines and look for h1
    lines = markdown.split('\n')
    
    for line in lines:
        # Look for line starting with single #
        if line.strip().startswith('# '):
            # Return everything after the # and any whitespace
            return line.strip()[2:].strip()
            
    raise ValueError("No h1 header found in markdown")
