---
layout: post
title: Are you sure your software will not kill anyone?
date: '2020-01-29 00:00:00'
tags:
- medical robotics
- safety
- paper
---

Yes, it may sound a bit bold, especially for those who work in medical robotics industry.
It is actually the title of an article recently published in the Communications of the ACM
(Vol 63, Issue 2, Feb 2020):

* Nancy Leveson, "Are you sure your software will not kill anyone?", Commun. ACM 63, 2
(February 2020), 25–28. DOI: [10.1145/3376127](https://doi.org/10.1145/3376127)

If you are interested in the topics around safety such as software system safety, safety
engineering, and dependable computing, you have probably heard of
[Dr. Nancy Leveson](http://sunnyday.mit.edu).  She is a
Professor at Aeronautics and Astronautics/MIT and her research takes a systems approach to
safety, safety engineering, and software system safety.  Her work has been formulated as a
new model for safety, called the system-theoretic model of accidents (STAMP).
She is leading the [Partnership for Systems Approaches to Safety and Security (PSASS)](http://psas.scripts.mit.edu).

I first came across her name and her body of work when I started working on literature
review for my PhD thesis.  While digging through her research and publication, it was
relieving to me to realize safety is a "real" problem, not something that people talk
about at an abstract level and/or without substantial thinking around it.  The existing
body of work around safety in various domains confirmed that safety is still a challenging
topic both for academia and for industry, thereby validating the problem of my thesis in
medical robotics.

In this short recent article, she briefly talks about some of the key concepts in safety,
discuss some of the most common misconceptions around software and safety, and wraps up
the article with a quick intro to her book -- 
[Engineering a Safer World](https://www.amazon.com/Engineering-Safer-World-Systems-Thinking/dp/0262533693/ref=sr_1_1?crid=1A3QQ8DJ71NXC) -- and PSASS.

Here are the misconceptions listed in the article:

> 1. Misconception 1: Software itself can be unsafe.
> 1. Misconception 2: Reliable systems are safe; that is, reliability and safety are
   essentially the same thing.  Reliability assessment can therefore act as a proxy for
   safety.
> 1. Misconception 3: The safety of components in a complex system is a useful concept; that
   is, we can model or analyze the safety of software in isolation from the entire system
   design.
> 1. Misconception 4: Software can be shown to be safe by testing, simulation, or standard
   formal verification.

From the article, I got a sense of the need for her to straighten something up about
software system safety.  This article also reminded me of all the years back in Baltimore
reading and writing a bunch of articles on software system safety.

For those who'd like to explore more on safety engineering and software system safety,
the following two books would be a good starting point:

- [Safeware: System Safety and Computers](https://www.amazon.com/Safeware-Computers-Nancy-G-Leveson/dp/0201119722/ref=sr_1_2?keywords=nancy+leveson&qid=1580308654&s=books&sr=1-2): 
  The first book from Nancy Leveson that I went through cover to cover.  A bit outdated
  (published in 1995), but still contain a lot of great and fundamental materials.
- [Engineering a Safer World](https://www.amazon.com/Engineering-Safer-World-Systems-Thinking/dp/0262533693/ref=sr_1_1?crid=1A3QQ8DJ71NXC):
  The second book in my bookshelf.  More recently updated materials with modern concepts.
