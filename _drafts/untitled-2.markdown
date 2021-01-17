---
layout: post
title: Cross-compile
---

Print out default paths used by gcc/c++:

[https://stackoverflow.com/questions/4980819/what-are-the-gcc-default-include-directories](https://stackoverflow.com/questions/4980819/what-are-the-gcc-default-include-directories)

In order to figure out the default paths used by `gcc`/`g++`, as well as their priorities, you need to examine the output of the following commands:

1. For **C** :

        gcc -xc -E -v -

1. For **C++** :

        gcc -xc++ -E -v -

echo | ./x86\_64-poky-linux-g++ -Wp,-v -x c++ - -fsyntax-only

