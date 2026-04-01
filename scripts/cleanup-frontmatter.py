#!/usr/bin/env python3
"""
Phase 4: Cleanup legacy WordPress front matter.

Removes unused WordPress fields:
- id
- guid
- restapi_import_id
- original_post_id
- layout: post
- author: zacharyzacharyccom
- permalink (now replaced by url)

Keeps: title, date, url, categories, tags, draft, cover, showToc, etc.
"""

import os
import re
import sys
from pathlib import Path


# Fields to remove (exact matches)
FIELDS_TO_REMOVE = {
    'id',
    'guid',
    'restapi_import_id',
    'original_post_id',
    'layout',
    'author',
    'permalink',
}


def parse_front_matter(content):
    """Parse YAML front matter from markdown content."""
    if not content.startswith('---'):
        return None, content, None

    end_match = re.search(r'\n---\n', content[3:])
    if not end_match:
        return None, content, None

    front_matter_end = end_match.end() + 3
    front_matter_str = content[4:front_matter_end - 5]
    body = content[front_matter_end:]

    return front_matter_str, body, content[:front_matter_end]


def cleanup_front_matter(front_matter_str):
    """
    Remove legacy WordPress fields from front matter.
    Returns (cleaned_front_matter, list_of_removed_fields).
    """
    lines = front_matter_str.split('\n')
    new_lines = []
    removed_fields = []
    skip_until_next_field = False

    for line in lines:
        # Check if this line starts a new field (not indented or empty)
        is_field_line = line and not line[0].isspace() and ':' in line

        if skip_until_next_field:
            if is_field_line:
                skip_until_next_field = False
            else:
                # Still part of the multi-line value, skip it
                continue

        if is_field_line:
            # Extract field name
            field = line.split(':')[0].strip()
            if field in FIELDS_TO_REMOVE:
                removed_fields.append(field)
                # Check if this could be a multi-line value
                value_part = line.split(':', 1)[1].strip() if ':' in line else ''
                if not value_part or value_part == '|' or value_part == '>':
                    skip_until_next_field = True
                continue

        new_lines.append(line)

    # Remove any trailing empty lines
    while new_lines and not new_lines[-1].strip():
        new_lines.pop()

    return '\n'.join(new_lines), removed_fields


def process_file(filepath, dry_run=False):
    """Process a single file. Returns (modified, removed_fields)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    front_matter_str, body, original_header = parse_front_matter(content)

    if front_matter_str is None:
        return False, []

    cleaned_front_matter, removed_fields = cleanup_front_matter(front_matter_str)

    if not removed_fields:
        return False, []

    # Reconstruct the file
    new_content = f'---\n{cleaned_front_matter}\n---\n{body}'

    if not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return True, removed_fields


def main():
    dry_run = '--dry-run' in sys.argv
    verbose = '--verbose' in sys.argv or '-v' in sys.argv

    posts_dir = Path(__file__).parent.parent / 'content' / 'posts'

    if not posts_dir.exists():
        print(f"Error: Posts directory not found: {posts_dir}")
        sys.exit(1)

    print(f"Processing posts in: {posts_dir}")
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
    print(f"Fields to remove: {', '.join(sorted(FIELDS_TO_REMOVE))}")
    print("-" * 60)

    # Find all index.md files
    md_files = list(posts_dir.rglob('index.md'))

    total_files_modified = 0
    field_counts = {field: 0 for field in FIELDS_TO_REMOVE}

    for filepath in sorted(md_files):
        modified, removed_fields = process_file(filepath, dry_run)

        if removed_fields:
            total_files_modified += 1
            for field in removed_fields:
                field_counts[field] += 1

            if verbose:
                rel_path = filepath.relative_to(posts_dir)
                print(f"{rel_path}: removed {', '.join(removed_fields)}")

    print("-" * 60)
    print(f"Summary:")
    print(f"  Files cleaned: {total_files_modified}")
    print(f"\nFields removed:")
    for field in sorted(FIELDS_TO_REMOVE):
        if field_counts[field] > 0:
            print(f"  {field}: {field_counts[field]}")

    if dry_run:
        print("\nThis was a DRY RUN. No files were modified.")
        print("Run without --dry-run to apply changes.")


if __name__ == '__main__':
    main()
