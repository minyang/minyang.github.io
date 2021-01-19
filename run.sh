#!/usr/bin/env bash
./script/gen_tag.py
[ $? -ne 0 ] && { echo "Failed to generate tags"; exit 1; }

jekyll serve
