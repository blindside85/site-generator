import re

def extract_markdown_images(text):
    """
    Extract all markdown images from text and return list of (alt_text, url) tuples.
    
    Args:
        text (str): Markdown text to parse
        
    Returns:
        list[tuple]: List of tuples containing (alt_text, url)
        
    Example:
        >>> text = "![alt](url.jpg) ![other](pic.png)"
        >>> extract_markdown_images(text)
        [('alt', 'url.jpg'), ('other', 'pic.png')]
    """
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    """
    Extract all markdown links from text and return list of (anchor_text, url) tuples.
    
    Args:
        text (str): Markdown text to parse
        
    Returns:
        list[tuple]: List of tuples containing (anchor_text, url)
        
    Example:
        >>> text = "[Link](url.com) [Other](site.com)"
        >>> extract_markdown_links(text)
        [('Link', 'url.com'), ('Other', 'site.com')]
    """
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

