---
layout: post
title: Working with Binary Files
description: How to use vim to edit binary files
date: '2021-01-10 20:04:54'
tags:
- vim
- software
- development
---

I am a huge fan of vim.  I don't even know how to quit eclipse :) Whichever system I
happen to work on, the very first tool I always check and customize is vim.  After trying
out a variety of plug-ins and auxilary tools around vim, I settled down with my own vimrc
file and ended up using the exvim as my favorite editor.  Perhaps my own customization
around vim may deserve a separate write-up.

Anyway, I recently had to work with binary files and learned that vim already provides
a nice way to work with binary files.

When vim loads up a binry file, its content may look like this:

![vim-binary-1](/assets/vim-binary-1.png)

With `:%!xxd`, it shows up as follows:

![vim-binary-2](/assets/vim-binary-2.png)

Enabling syntax coloring makes it more readable: `:set ft=xxd`

![vim-binary-3](/assets/vim-binary-3.png)

At this point, it is possible to directly change hex values on the left side.  Once
changes are completed, we need to go back to the previous mode before updating the file: `:%!xxd -r`.
We can then now save the changes to file by `:w`.

You may notice an extra `0A` is added to the end of the file that you just updated.  To truncate
the last byte:
- `truncate --size=-1 bin_file`
- `sed '$ s/.$//' bin_file> > output_file` (if `truncate` is not available)

Lastly, a couple well known tips that may be useful when working with binary files:

- To dump a file in the hex format: `hexdump bin_file`
- To diff two binary files: `diff <(xxd binary_file1) <(xxd binary_file2)`
