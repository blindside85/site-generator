import logging
from pathlib import Path
from compiler import copy_static
from generate_page import generate_pages_recursive

def main():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(message)s'
    )
    
    # Get project root and define paths
    project_root = Path(__file__).parent.parent
    content_dir = project_root / "content"
    template_path = project_root / "template.html"
    public_dir = project_root / "public"
    
    # Copy static files (this also cleans public directory)
    copy_static()
    
    # Generate all pages recursively
    generate_pages_recursive(content_dir, template_path, public_dir)

if __name__ == "__main__":
    main()
