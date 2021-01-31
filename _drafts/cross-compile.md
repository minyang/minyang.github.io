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



ld, ar, ranlib, strip

https://stackoverflow.com/questions/47910759/what-is-the-difference-between-ranlib-ar-and-ld-for-making-libraries

stripping: 

https://www.technovelty.org/linux/stripping-shared-libraries.html
