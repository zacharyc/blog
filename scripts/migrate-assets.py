#!/usr/bin/env python3
"""
Phase 3: Migrate assets into page bundles.

Finds images referenced in posts and:
1. Copies them from static/assets/img/ to the post bundle
2. Updates image paths from absolute to relative

Example:
  /assets/img/2024/03/cover.jpg -> ./cover.jpg (and file copied to bundle)
"""

import os
import re
import sys
import shutil
from pathlib import Path


def find_image_references(content):
    """
    Find all image references in markdown content.
    Returns list of (full_match, image_path) tuples.
    """
    refs = []

    # Markdown images: ![alt](path)
    for match in re.finditer(r'(!\[[^\]]*\]\()([^)\s]+)(\))', content):
        refs.append((match.group(0), match.group(2), 'markdown', match.groups()))

    # Cover image in front matter: image: "/path/to/image"
    for match in re.finditer(r'(image:\s*["\'])(/[^"\'\n]+)(["\'])', content):
        refs.append((match.group(0), match.group(2), 'cover', match.groups()))

    return refs


def get_source_file(img_path, static_dir):
    """
    Convert an image path to its source file location.
    /assets/img/2024/03/file.jpg -> static/assets/img/2024/03/file.jpg
    """
    if img_path.startswith('/'):
        img_path = img_path[1:]  # Remove leading /

    # Handle query strings (like ?w=1100&ssl=1)
    img_path = img_path.split('?')[0]

    source_file = static_dir / img_path
    return source_file


def process_post(post_dir, static_dir, dry_run=False):
    """
    Process a single post bundle.
    Returns (images_migrated, images_not_found, changes).
    """
    index_file = post_dir / 'index.md'

    if not index_file.exists():
        return 0, 0, []

    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()

    refs = find_image_references(content)
    if not refs:
        return 0, 0, []

    images_migrated = 0
    images_not_found = 0
    changes = []

    new_content = content

    for full_match, img_path, ref_type, groups in refs:
        # Skip external URLs
        if img_path.startswith('http://') or img_path.startswith('https://'):
            continue

        # Skip already relative paths
        if not img_path.startswith('/'):
            continue

        # Get source file
        source_file = get_source_file(img_path, static_dir)

        # Extract just the filename for the new relative path
        filename = source_file.name

        if source_file.exists():
            dest_file = post_dir / filename

            if not dry_run:
                # Copy the image to the bundle
                if not dest_file.exists():
                    shutil.copy2(source_file, dest_file)

            # Create the replacement
            if ref_type == 'markdown':
                # ![alt](old_path) -> ![alt](./filename)
                old = full_match
                new = f'{groups[0]}./{filename}{groups[2]}'
            else:
                # image: "/old_path" -> image: "./filename"
                old = full_match
                new = f'{groups[0]}./{filename}{groups[2]}'

            new_content = new_content.replace(old, new, 1)
            changes.append((img_path, f'./{filename}'))
            images_migrated += 1
        else:
            images_not_found += 1
            changes.append((img_path, 'NOT FOUND'))

    # Write updated content
    if changes and not dry_run:
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return images_migrated, images_not_found, changes


def main():
    dry_run = '--dry-run' in sys.argv
    verbose = '--verbose' in sys.argv or '-v' in sys.argv

    base_dir = Path(__file__).parent.parent
    posts_dir = base_dir / 'content' / 'posts'
    static_dir = base_dir / 'static'

    if not posts_dir.exists():
        print(f"Error: Posts directory not found: {posts_dir}")
        sys.exit(1)

    print(f"Processing posts in: {posts_dir}")
    print(f"Looking for assets in: {static_dir}")
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
    print("-" * 60)

    total_migrated = 0
    total_not_found = 0
    posts_with_images = 0

    # Find all post bundles (directories with index.md)
    for year_dir in sorted(posts_dir.iterdir()):
        if not year_dir.is_dir():
            continue

        for post_dir in sorted(year_dir.iterdir()):
            if not post_dir.is_dir():
                continue

            migrated, not_found, changes = process_post(post_dir, static_dir, dry_run)

            if changes:
                posts_with_images += 1
                total_migrated += migrated
                total_not_found += not_found

                if verbose or not_found > 0:
                    rel_path = post_dir.relative_to(posts_dir)
                    print(f"\n{rel_path}:")
                    for old, new in changes:
                        status = "" if new != 'NOT FOUND' else " [MISSING]"
                        print(f"  {old} -> {new}{status}")

    print("-" * 60)
    print(f"Summary:")
    print(f"  Posts with images: {posts_with_images}")
    print(f"  Images migrated: {total_migrated}")
    print(f"  Images not found: {total_not_found}")

    if dry_run:
        print("\nThis was a DRY RUN. No files were modified.")
        print("Run without --dry-run to apply changes.")
        print("\nUsage:")
        print("  python migrate-assets.py --dry-run         # Preview all")
        print("  python migrate-assets.py --dry-run -v      # Verbose preview")
        print("  python migrate-assets.py                   # Migrate all")


if __name__ == '__main__':
    main()
