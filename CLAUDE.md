# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a personal blog built with Hugo using the PaperMod theme. The site is deployed to zacharyc.com.

## Common Commands

```bash
# Run local development server
hugo server

# Run with drafts visible
hugo server -D

# Build the site (outputs to public/)
hugo

# Create a new post
hugo new posts/YYYY-MM-DD-post-title.md

# Build and deploy to production
./deploy
```

## Project Structure

- `config.yml` - Main Hugo configuration (theme settings, menus, params)
- `content/` - All site content in Markdown
  - `posts/` - Blog posts (named YYYY-MM-DD-title.md)
  - `projects/`, `projects-page/`, `projects-dir/` - Project showcases
  - `city-guides/` - Location guides
  - `resumes/` - Resume content
- `layouts/` - Custom template overrides
  - `partials/extend_head.html` - Custom head includes (fonts, analytics)
  - `shortcodes/` - Custom Hugo shortcodes
- `themes/PaperMod/` - Theme (git submodule)
- `static/` - Static assets copied directly to output
- `assets/css/` - Custom CSS

## Custom Shortcodes

- `cheer_job` - Display job/position info with org, location, start/end dates
- `div_code` - Wrap content in a div with custom className
- `line_break` - Insert a `<br />`

## Content Front Matter

Posts use this front matter pattern:
```yaml
---
title: "Post Title"
date: YYYY-MM-DDTHH:MM:SS-TZ
draft: true/false
---
```

## Deployment

The `deploy` script builds with Hugo and rsyncs to DreamHost VPS. The `public/` directory is gitignored.
