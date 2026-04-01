#!/usr/bin/env python3
"""
Fix relref/ref shortcodes after migrating to page bundles.

Converts references from:
  {{< relref "2025-03-18-Web-Forms-Hugo-Sites-pt1" >}}
  {{< relref "/posts/2023-01-02-2022-into-2023.md" >}}
  {{< relref "2026-03-07-Your-Contacts-App-Is-Broken.md" >}}

To:
  {{< relref "/posts/2025/web-forms-hugo-sites-pt1" >}}
  {{< relref "/posts/2023/2022-into-2023" >}}
  {{< relref "/posts/2026/your-contacts-app-is-broken" >}}
"""

import os
import re
import sys
from pathlib import Path


def convert_old_ref_to_new(ref_path):
    """
    Convert old reference path to new page bundle path.
    """
    # Remove leading /posts/ if present
    ref_path = re.sub(r'^/posts/', '', ref_path)
    # Remove .md extension if present
    ref_path = re.sub(r'\.md$', '', ref_path)

    # Match pattern: YYYY-MM-DD-slug
    match = re.match(r'^(\d{4})-\d{2}-\d{2}-(.+)$', ref_path)
    if match:
        year = match.group(1)
        slug = match.group(2).lower()
        return f'/posts/{year}/{slug}'

    return None


def fix_relrefs_in_content(content):
    """
    Find and fix all relref/ref shortcodes in content.
    Returns (modified_content, list_of_changes).
    """
    changes = []

    def replace_relref(match):
        shortcode = match.group(1)  # relref or ref
        quote_char = match.group(2)  # " or '
        old_path = match.group(3)

        new_path = convert_old_ref_to_new(old_path)
        if new_path:
            changes.append((old_path, new_path))
            return f'{{{{< {shortcode} "{new_path}" >}}}}'

        # If conversion failed, return original
        return match.group(0)

    # Match both relref and ref shortcodes
    # Handles: {{< relref "path" >}} and {{<relref "path" >}} (with/without space)
    pattern = r'\{\{<\s*(relref|ref)\s*(["\'])([^"\']+)\2\s*>\}\}'

    modified_content = re.sub(pattern, replace_relref, content)

    return modified_content, changes


def process_file(filepath, dry_run=False):
    """Process a single file. Returns (modified, changes)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content, changes = fix_relrefs_in_content(content)

    if changes and not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return bool(changes), changes


def main():
    dry_run = '--dry-run' in sys.argv

    posts_dir = Path(__file__).parent.parent / 'content' / 'posts'

    if not posts_dir.exists():
        print(f"Error: Posts directory not found: {posts_dir}")
        sys.exit(1)

    print(f"Scanning posts in: {posts_dir}")
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
    print("-" * 60)

    # Find all index.md files in page bundles
    md_files = list(posts_dir.rglob('index.md'))

    total_files_modified = 0
    total_refs_fixed = 0

    for filepath in sorted(md_files):
        modified, changes = process_file(filepath, dry_run)

        if changes:
            total_files_modified += 1
            total_refs_fixed += len(changes)

            rel_path = filepath.relative_to(posts_dir)
            print(f"\n{rel_path}:")
            for old, new in changes:
                print(f"  {old} -> {new}")

    print("-" * 60)
    print(f"Summary:")
    print(f"  Files modified: {total_files_modified}")
    print(f"  References fixed: {total_refs_fixed}")

    if dry_run:
        print("\nThis was a DRY RUN. No files were modified.")
        print("Run without --dry-run to apply changes.")


if __name__ == '__main__':
    main()
