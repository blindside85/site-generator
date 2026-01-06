import os
import shutil
import logging
from pathlib import Path

def should_copy_file(file_path: Path) -> bool:
    """
    Determine if a file should be copied based on filtering rules.
    """
    return not file_path.name.startswith('.')

def copy_static_recursive(src: Path, dest: Path, root: Path):
    """
    Recursively copy files with detailed logging of nested structures.
    
    Args:
        src (Path): Source directory path
        dest (Path): Destination directory path
        root (Path): Project root path for relative path logging
        
    Example structure:
        static/
        └── images/
            └── hero/
                └── banner.png
    Will log:
        Copying static/images/hero/banner.png -> public/images/hero/banner.png
    """
    # Create destination if it doesn't exist
    dest.mkdir(exist_ok=True)
    
    for item in src.iterdir():
        if not should_copy_file(item):
            logging.debug(f"Skipping {item.relative_to(root)}")
            continue
            
        dest_path = dest / item.name
        
        if item.is_file():
            # Log relative paths for clearer output
            rel_src = item.relative_to(root)
            rel_dest = dest_path.relative_to(root)
            logging.info(f"Copying {rel_src} -> {rel_dest}")
            shutil.copy2(item, dest_path)
        else:
            # Recursively copy subdirectories
            copy_static_recursive(item, dest_path, root)

def copy_static():
    """
    Initialize the static file copy process from project root.
    """
    # Get project root and define paths
    current_dir = Path(__file__).parent
    project_root = current_dir.parent
    static_dir = project_root / "static"
    public_dir = project_root / "docs"

    if not static_dir.exists():
        raise FileNotFoundError(f"Static directory not found at {static_dir}")

    # Clean existing public directory
    if public_dir.exists():
        logging.info(f"Cleaning {public_dir.relative_to(project_root)}")
        shutil.rmtree(public_dir)

    # Create fresh public directory
    public_dir.mkdir(exist_ok=True)

    # Start recursive copy
    copy_static_recursive(static_dir, public_dir, project_root)
