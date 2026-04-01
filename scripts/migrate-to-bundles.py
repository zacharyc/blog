#!/usr/bin/env python3
"""
Phase 2: Migrate posts to year-based page bundles

Creates structure:
  content/posts/
    2006/
      getting-better/
        index.md
    2007/
      post-slug/
        index.md
    ...

Each post is moved to content/posts/YYYY/slug/index.md
"""

import os
import re
import sys
import shutil
from pathlib import Path


def parse_front_matter(content):
    """Parse YAML front matter from markdown content."""
    if not content.startswith('---'):
        return None, content

    end_match = re.search(r'\n---\n', content[3:])
    if not end_match:
        return None, content

    front_matter_end = end_match.end() + 3
    front_matter_str = content[4:front_matter_end - 5]
    body = content[front_matter_end:]

    return front_matter_str, body


def extract_date_from_front_matter(front_matter_str):
    """Extract date value from front matter string."""
    match = re.search(r'^date:\s*[\'"]?(\d{4})-(\d{2})-(\d{2})', front_matter_str, re.MULTILINE)
    if match:
        return match.groups()
    return None


def extract_slug_from_url(front_matter_str):
    """Extract slug from url: field."""
    match = re.search(r'^url:\s*/\d{4}/\d{2}/\d{2}/([^/\s]+)/?', front_matter_str, re.MULTILINE)
    if match:
        return match.group(1)
    return None


def get_year_and_slug(filename, front_matter_str):
    """
    Get year and slug from filename or front matter.
    Returns (year, slug) tuple.
    """
    # Try filename pattern: YYYY-MM-DD-slug.md
    match = re.match(r'^(\d{4})-\d{2}-\d{2}-(.+)\.md$', filename)
    if match:
        year = match.group(1)
        slug = match.group(2).lower()
        return year, slug

    # Fallback: extract from front matter
    if front_matter_str:
        date_parts = extract_date_from_front_matter(front_matter_str)
        slug = extract_slug_from_url(front_matter_str)
        if date_parts and slug:
            return date_parts[0], slug

        # Last fallback: use date from front matter and filename as slug
        if date_parts:
            slug = filename.rsplit('.', 1)[0].lower()
            return date_parts[0], slug

    return None, None


def find_image_references(content):
    """
    Find all image references in the markdown content.
    Returns list of image paths referenced in the post.
    """
    images = []

    # Markdown images: ![alt](path)
    md_images = re.findall(r'!\[[^\]]*\]\(([^)\s]+)', content)
    images.extend(md_images)

    # HTML img tags: <img src="path"
    html_images = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    images.extend(html_images)

    # Cover image in front matter
    cover_match = re.search(r'image:\s*["\']?(/[^"\'\n]+)["\']?', content)
    if cover_match:
        images.append(cover_match.group(1))

    return images


def migrate_post(filepath, posts_dir, dry_run=False):
    """
    Migrate a single post to page bundle structure.
    Returns (success, message, image_references).
    """
    filename = os.path.basename(filepath)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    front_matter_str, body = parse_front_matter(content)

    if front_matter_str is None:
        return False, f"SKIP: {filename} - No front matter found", []

    year, slug = get_year_and_slug(filename, front_matter_str)

    if not year or not slug:
        return False, f"SKIP: {filename} - Could not determine year/slug", []

    # Create destination path
    dest_dir = posts_dir / year / slug
    dest_file = dest_dir / 'index.md'

    if dest_file.exists():
        return False, f"SKIP: {filename} - Destination already exists: {dest_file}", []

    # Find image references for reporting
    images = find_image_references(content)

    if not dry_run:
        # Create directory
        dest_dir.mkdir(parents=True, exist_ok=True)

        # Move the file
        shutil.move(filepath, dest_file)

    action = f"MIGRATE: {filename} -> {year}/{slug}/index.md"
    if images:
        action += f" (references {len(images)} images)"

    return True, action, images


def main():
    dry_run = '--dry-run' in sys.argv
    year_filter = None

    # Check for year filter argument
    for arg in sys.argv[1:]:
        if arg.isdigit() and len(arg) == 4:
            year_filter = arg
            break

    posts_dir = Path(__file__).parent.parent / 'content' / 'posts'

    if not posts_dir.exists():
        print(f"Error: Posts directory not found: {posts_dir}")
        sys.exit(1)

    print(f"Processing posts in: {posts_dir}")
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
    if year_filter:
        print(f"Year filter: {year_filter}")
    print("-" * 60)

    # Get all markdown files in the root posts directory
    md_files = sorted([f for f in posts_dir.glob('*.md') if f.is_file()])

    stats = {
        'migrated': 0,
        'skipped': 0,
        'errors': 0
    }

    all_images = []
    year_counts = {}

    for filepath in md_files:
        filename = filepath.name

        # If year filter is set, only process matching files
        if year_filter:
            if not filename.startswith(year_filter):
                # Also check front matter date
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                front_matter_str, _ = parse_front_matter(content)
                date_parts = extract_date_from_front_matter(front_matter_str) if front_matter_str else None
                if not date_parts or date_parts[0] != year_filter:
                    continue

        try:
            success, message, images = migrate_post(filepath, posts_dir, dry_run)
            print(message)

            if success:
                stats['migrated'] += 1
                all_images.extend(images)
                # Extract year from message for counting
                year_match = re.search(r'-> (\d{4})/', message)
                if year_match:
                    year = year_match.group(1)
                    year_counts[year] = year_counts.get(year, 0) + 1
            else:
                stats['skipped'] += 1

        except Exception as e:
            print(f"ERROR: {filepath.name} - {e}")
            stats['errors'] += 1

    print("-" * 60)
    print(f"Summary:")
    print(f"  Migrated: {stats['migrated']}")
    print(f"  Skipped: {stats['skipped']}")
    print(f"  Errors: {stats['errors']}")
    print(f"  Total image references found: {len(all_images)}")

    if year_counts:
        print(f"\nPosts per year:")
        for year in sorted(year_counts.keys()):
            print(f"  {year}: {year_counts[year]}")

    if dry_run:
        print("\nThis was a DRY RUN. No files were modified.")
        print("Run without --dry-run to apply changes.")
        print("\nUsage:")
        print("  python migrate-to-bundles.py --dry-run      # Preview all")
        print("  python migrate-to-bundles.py --dry-run 2006 # Preview single year")
        print("  python migrate-to-bundles.py                # Migrate all")
        print("  python migrate-to-bundles.py 2006           # Migrate single year")


if __name__ == '__main__':
    main()
