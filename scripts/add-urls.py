#!/usr/bin/env python3
"""
Phase 1: Add URL field to all posts

For legacy posts: Convert existing `permalink:` to `url:`
For modern posts: Generate `url:` from filename (YYYY-MM-DD-slug.md -> /YYYY/MM/DD/slug/)

This ensures all posts have explicit URLs before reorganizing into page bundles.
"""

import os
import re
import sys
from pathlib import Path


def parse_front_matter(content):
    """Parse YAML front matter from markdown content."""
    if not content.startswith('---'):
        return None, content

    # Find the closing ---
    end_match = re.search(r'\n---\n', content[3:])
    if not end_match:
        return None, content

    front_matter_end = end_match.end() + 3
    front_matter_str = content[4:front_matter_end - 5]  # Strip the --- markers
    body = content[front_matter_end:]

    return front_matter_str, body


def extract_url_from_permalink(front_matter_str):
    """Extract permalink value from front matter string."""
    match = re.search(r'^permalink:\s*(.+)$', front_matter_str, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None


def has_url_field(front_matter_str):
    """Check if front matter already has a url: field."""
    return bool(re.search(r'^url:\s*', front_matter_str, re.MULTILINE))


def extract_date_from_front_matter(front_matter_str):
    """Extract date value from front matter string."""
    match = re.search(r'^date:\s*[\'"]?(\d{4})-(\d{2})-(\d{2})', front_matter_str, re.MULTILINE)
    if match:
        return match.groups()
    return None


def generate_url_from_filename(filename, front_matter_str=None):
    """
    Generate URL from filename pattern YYYY-MM-DD-slug.md
    Returns /YYYY/MM/DD/slug/
    Falls back to using date from front matter if filename doesn't match pattern.
    """
    # Match pattern: YYYY-MM-DD-slug.md
    match = re.match(r'^(\d{4})-(\d{2})-(\d{2})-(.+)\.md$', filename)
    if match:
        year, month, day, slug = match.groups()
        # Convert slug to lowercase and preserve hyphens
        slug = slug.lower()
        return f'/{year}/{month}/{day}/{slug}/'

    # Fallback: try to get date from front matter
    if front_matter_str:
        date_parts = extract_date_from_front_matter(front_matter_str)
        if date_parts:
            year, month, day = date_parts
            # Use filename (without .md) as slug
            slug = filename.rsplit('.', 1)[0].lower()
            return f'/{year}/{month}/{day}/{slug}/'

    return None


def add_url_to_front_matter(front_matter_str, url):
    """Add url: field to front matter, placing it after date: if present."""
    lines = front_matter_str.split('\n')
    result_lines = []
    url_added = False

    for i, line in enumerate(lines):
        result_lines.append(line)
        # Add url after date line
        if line.strip().startswith('date:') and not url_added:
            result_lines.append(f'url: {url}')
            url_added = True

    # If date wasn't found, add url after title
    if not url_added:
        result_lines = []
        for i, line in enumerate(lines):
            result_lines.append(line)
            if line.strip().startswith('title:') and not url_added:
                result_lines.append(f'url: {url}')
                url_added = True

    # Last resort: add at the end
    if not url_added:
        result_lines.append(f'url: {url}')

    return '\n'.join(result_lines)


def convert_permalink_to_url(front_matter_str):
    """Convert permalink: to url: in front matter."""
    return re.sub(r'^permalink:', 'url:', front_matter_str, flags=re.MULTILINE)


def process_post(filepath, dry_run=False):
    """Process a single post file. Returns (modified, message)."""
    filename = os.path.basename(filepath)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    front_matter_str, body = parse_front_matter(content)

    if front_matter_str is None:
        return False, f"SKIP: {filename} - No front matter found"

    # Check if already has url:
    if has_url_field(front_matter_str):
        return False, f"SKIP: {filename} - Already has url: field"

    # Check if has permalink: (legacy post)
    permalink = extract_url_from_permalink(front_matter_str)
    if permalink:
        # Convert permalink: to url:
        new_front_matter = convert_permalink_to_url(front_matter_str)
        action = f"CONVERT: {filename} - permalink: -> url: {permalink}"
    else:
        # Modern post - generate url from filename (or front matter date)
        url = generate_url_from_filename(filename, front_matter_str)
        if url is None:
            return False, f"SKIP: {filename} - Could not generate URL from filename or front matter"
        new_front_matter = add_url_to_front_matter(front_matter_str, url)
        action = f"ADD: {filename} - Generated url: {url}"

    # Reconstruct the file
    new_content = f'---\n{new_front_matter}\n---\n{body}'

    if not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return True, action


def main():
    # Parse arguments
    dry_run = '--dry-run' in sys.argv

    posts_dir = Path(__file__).parent.parent / 'content' / 'posts'

    if not posts_dir.exists():
        print(f"Error: Posts directory not found: {posts_dir}")
        sys.exit(1)

    print(f"Processing posts in: {posts_dir}")
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
    print("-" * 60)

    # Get all markdown files
    md_files = sorted(posts_dir.glob('*.md'))

    stats = {
        'converted': 0,
        'added': 0,
        'skipped': 0,
        'errors': 0
    }

    for filepath in md_files:
        try:
            modified, message = process_post(filepath, dry_run)
            print(message)

            if 'CONVERT' in message:
                stats['converted'] += 1
            elif 'ADD' in message:
                stats['added'] += 1
            else:
                stats['skipped'] += 1

        except Exception as e:
            print(f"ERROR: {filepath.name} - {e}")
            stats['errors'] += 1

    print("-" * 60)
    print(f"Summary:")
    print(f"  Converted permalink -> url: {stats['converted']}")
    print(f"  Added new url: {stats['added']}")
    print(f"  Skipped: {stats['skipped']}")
    print(f"  Errors: {stats['errors']}")
    print(f"  Total files: {len(md_files)}")

    if dry_run:
        print("\nThis was a DRY RUN. No files were modified.")
        print("Run without --dry-run to apply changes.")


if __name__ == '__main__':
    main()
