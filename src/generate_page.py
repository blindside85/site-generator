import os
import logging
from pathlib import Path
from extract_title import extract_title
from markdown_to_html import markdown_to_html_node
from compiler import copy_static

def generate_page(from_path, template_path, dest_path):
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
    
    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Write final HTML to destination
    with open(dest_path, 'w') as f:
        f.write(final_html)
