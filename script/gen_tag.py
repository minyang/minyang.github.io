#!/usr/bin/env python

'''
gen_tag.py

Adapted from original code by Long Qian:
    https://longqian.me/2017/02/09/github-jekyll-tag
'''

import glob
import os

post_dir = 'blog/**/'
tag_dir = 'tag/'

filenames = glob.glob(post_dir + '*.md', recursive=True)

total_tags = set()
for filename in filenames:
    print(filename)
    f = open(filename, 'r', encoding='utf8')
    crawl = False
    extract = False
    for line in f:
        if line.strip() == '---':
            if not crawl:
                crawl = True
            else:
                crawl = False
                print("TAG STOP")
                break
        if crawl:
            current_tags = line.strip().split()
            if current_tags[0] == 'tags:':
                if not extract:
                    extract = True
                    print("TAG BEGINS")
                    continue
            if extract:
                current_tags = line.strip().split()[1]
                if not current_tags:
                    continue
                print("current_tags = {}".format(current_tags))
                total_tags.add(current_tags)
                print("TAG found: {}".format(current_tags))
    f.close()
print("total_tags = {}".format(total_tags))
#total_tags = set(total_tags)

old_tags = glob.glob(tag_dir + '*.md')
for tag in old_tags:
    os.remove(tag)
    
if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

for tag in total_tags:
    tag_filename = tag_dir + tag + '.md'
    f = open(tag_filename, 'a')
    write_str = '---\nlayout: tag\ntitle: \"Tag: ' + tag + '\"\ntag: ' + tag + '\nrobots: noindex\n---\n'
    f.write(write_str)
    f.close()
print("Tags generated, count", total_tags.__len__())
