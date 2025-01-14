from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> str:
    """
    Determine the type of a markdown block.
    
    Args:
        block (str): A block of markdown text, with leading/trailing whitespace stripped
        
    Returns:
        str: The type of block as a string (paragraph, heading, code, quote, unordered_list, or ordered_list)
    """
    # Handle empty blocks
    if not block:
        return BlockType.PARAGRAPH.value
        
    # Split into lines for multi-line analysis
    lines = block.split('\n')
    
    # Code blocks
    if block.startswith('```') and block.endswith('```'):
        return BlockType.CODE.value
        
    # Heading - check for 1-6 # characters followed by space
    if re.match(r'^#{1,6}\s', block):
        return BlockType.HEADING.value
        
    # Quote - every line must start with >
    if all(line.startswith('>') for line in lines):
        return BlockType.QUOTE.value
        
    # Unordered list - every line must start with * or - followed by space
    if all(line.strip().startswith(('* ', '- ')) for line in lines):
        return BlockType.UNORDERED_LIST.value
        
    # Ordered list - check if lines start with incrementing numbers
    if all(line.strip() and bool(re.match(r'^\d+\.\s', line.strip())) for line in lines):
        # Additional check for proper number sequence
        numbers = [int(re.match(r'^(\d+)\.', line.strip()).group(1)) 
                  for line in lines if line.strip()]
        if numbers == list(range(1, len(numbers) + 1)):
            return BlockType.ORDERED_LIST.value
            
    # Default case - paragraph
    return BlockType.PARAGRAPH.value
