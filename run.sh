#!/usr/bin/env bash
./script/gen_tag.py
[ $? -ne 0 ] && { echo "Failed to generate tags"; exit 1; }

# Pre-production, locally serve pages
jekyll serve

# Pre-production, testing production
#JEKYLL_ENV=production jekyll serve

# Production
#jekyll build
