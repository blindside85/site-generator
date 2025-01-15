import logging
from compiler import copy_static

def main():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(message)s'
    )
    
    # Copy static files
    copy_static()
    
    # Future: Add markdown processing here
    
if __name__ == "__main__":
    main()
