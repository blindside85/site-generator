# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A static site generator that converts Markdown content to HTML using a custom-built parser. The project is deployed to GitHub Pages at the `/site-generator/` path.

## Build and Deployment Commands

### Local Development
```bash
./main.sh               # Build site with "/" basepath and serve locally on :8888
```

### GitHub Pages Deployment
```bash
./build.sh              # Build site with "/site-generator/" basepath for GitHub Pages
```

### Testing
```bash
./test.sh                                                 # Run all tests
cd src && python3 -m unittest test_htmlnode               # Run single test file
```

## Architecture

### Three-Phase Pipeline

1. **Markdown Parsing** → 2. **HTML Generation** → 3. **Site Building**

#### Phase 1: Markdown to Intermediate Representation
- **TextNode**: Intermediate representation for inline elements (bold, italic, code, links, images)
- **HTMLNode hierarchy**: Base class for all HTML output
  - `LeafNode`: Terminal nodes (text, images, links)
  - `ParentNode`: Container nodes with children (divs, paragraphs, lists)

The parsing flow:
```
Raw markdown → markdown_to_blocks() → block_to_block_type()
            → text_to_textnodes() → TextNode objects
            → text_node_to_html_node() → HTMLNode tree
```

#### Phase 2: HTML Node Tree Construction
- `markdown_to_html_node()` in `src/markdown_to_html.py` is the main entry point
- Processes blocks sequentially: paragraphs, headings, lists, quotes, code blocks
- Each block type has a dedicated converter function (e.g., `paragraph_to_html_node()`)

#### Phase 3: Site Generation
- `generate_page()`: Takes markdown, template, and basepath → produces final HTML
- `generate_pages_recursive()`: Walks content/ directory preserving structure
- `copy_static()`: Copies static assets (CSS, images) to output directory

### Critical Path Handling

**IMPORTANT**: The basepath parameter is injected into generated HTML via string replacement:
```python
final_html = final_html.replace("href=\"/", f'href="{basepath}')
final_html = final_html.replace("src=\"/", f'src="{basepath}')
```

This allows the same content to work both locally (basepath="/") and on GitHub Pages (basepath="/site-generator/").

### Directory Structure

- `content/` - Source markdown files (preserves directory structure in output)
- `static/` - CSS and images to be copied verbatim
- `docs/` - **Output directory** (used by GitHub Pages, served locally)
- `public/` - **OBSOLETE** (legacy directory, can be deleted)
- `src/` - Python source and tests
- `template.html` - HTML template with `{{ Title }}` and `{{ Content }}` placeholders

**Key Point**: Both `copy_static()` and `generate_pages_recursive()` output to `docs/`. The `public/` directory is legacy and should be ignored.

## Common Patterns

### Adding New Inline Markdown Syntax
1. Add new `TextType` enum value in `src/textnode.py`
2. Add parsing logic in `src/split_nodes.py` or related parser
3. Add HTML conversion in `text_node_to_html_node()`
4. Add tests in corresponding `test_*.py` file

### Adding New Block-Level Markdown Syntax
1. Add new `BlockType` enum value in `src/block_to_block.py`
2. Add detection logic in `block_to_block_type()`
3. Add converter function in `src/markdown_to_html.py`
4. Update `markdown_to_html_node()` to handle new block type
