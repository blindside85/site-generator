import os
import logging
from pathlib import Path
from extract_title import extract_title
from markdown_to_html import markdown_to_html_node
from compiler import copy_static

def generate_page(from_path, template_path, dest_path, basepath):
    """
    Generate an HTML page from a markdown file using a template.
    
    Args:
        from_path (str): Path to source markdown file
        template_path (str): Path to HTML template file
        dest_path (str): Destination path for generated HTML
    """
    logging.info(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read markdown content
    with open(from_path, 'r') as f:
        markdown_content = f.read()
    
    # Read template content
    with open(template_path, 'r') as f:
        template_content = f.read()
    
    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    
    # Extract title
    title = extract_title(markdown_content)
    
    # Replace placeholders in template
    final_html = template_content.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)
    final_html = final_html.replace("href=\"/", f'href="{basepath}')
    final_html = final_html.replace("src=\"/", f'src="{basepath}')
    
    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Write final HTML to destination
    with open(dest_path, 'w') as f:
        f.write(final_html)


def generate_pages_recursive(dir_path_content: Path, template_path: Path, dest_dir_path: Path, basepath: Path):
    """
    Recursively generate HTML pages from markdown files while preserving directory structure.
    
    Args:
        dir_path_content (Path): Source directory containing markdown files
        template_path (Path): Path to HTML template file
        dest_dir_path (Path): Destination directory for generated HTML files
        
    Example:
        If content/ has structure:
            content/
            ├── index.md
            └── majesty/
                └── index.md
                
        It will generate:
            public/
            ├── index.html
            └── majesty/
                └── index.html
    """
    # Ensure the destination directory exists
    dest_dir_path.mkdir(exist_ok=True)
    
    # Iterate through all files and directories
    for entry in dir_path_content.iterdir():
        if entry.is_file() and entry.suffix == '.md':
            # Calculate relative path to maintain directory structure
            rel_path = entry.relative_to(dir_path_content)
            # Convert .md extension to .html
            dest_file = dest_dir_path / rel_path.with_suffix('.html')
            # Ensure destination subdirectories exist
            dest_file.parent.mkdir(parents=True, exist_ok=True)
            # Generate the HTML page
            generate_page(str(entry), str(template_path), str(dest_file), basepath)
        elif entry.is_dir():
            # Recursively process subdirectories
            generate_pages_recursive(entry, template_path, dest_dir_path / entry.name, basepath)

