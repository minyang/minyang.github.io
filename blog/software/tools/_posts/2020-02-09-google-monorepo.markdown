---
layout: post
title: Google's Monolithic Repo
date: '2020-02-09 00:00:00'
tags:
- software
- development
---

How do you maintain source code of your project?  Of course, you probably use one of
version control software like git, svn, and Perforce.  Those off-the-shelf tools should
work for the most of personal and small/medium-sized projects.  As the scale and
complexity of the projects grow, however, you  may encounter practical issues on a daily
basis in different areas.  For example, git clone may take too much time, back-end CI
infrastructure may be a bottleneck when verifying new change sets (e.g., too slow, too
many false build failures), and developers may start noticing room for improvement in
their development workflow.  These  issues are essentially related to the scalability of
development environments, which can be asked with one simple question: 
*does your development environment scale?*

Not until recently did I ask the question to myself.  For the last project that I worked
on at work, we structured our repos using git submodules to accommodate certain build
scenario requirements.  This submodule-based modular repo structure enabled us to quickly
and independently develop each sub-project while the main project moves forward (I will
write about this experience later on a separate article).  For the current project,
though, it became part of our company's monolithic source repository, which is shared
among all the engineers within the company.  As someone who was familiar with the
submodule-based multi-repo model, I was curious about the rationale of choosing the
monolithic repo model.  More importantly, I wanted to better understand the benefits and
implications of such a decision on not only in a short term (e.g., on engineers'
day-to-day development workflow) but also in a long(er) term (e.g., what it means to the
company after 10/20+ years).  Essentially, I was asking the question – *does it scale?*

Coincidentally, I came across two interesting articles from Google Research around this topic:

- Why Google Stores Billions of Lines of Code in a Single Repository (ACM 2016) [1]
- Advantages and disadvantages of a monolithic repository: a case study at Google (ICSE-SEIP 2018) [2]

With an introduction to the Google scale (9 billion source files, 35 million commits, 86TB
of content, ~40k commits/workday as of 2015), the first article describes why Google chose
the monolithic-source-management strategy in 1999, how it has been working for Google,
what in-house tooling and custom infrastructural efforts they have made over the years to
enable streamlined trunk-based development workflows, and advantages and alternatives of
the strategy.  From the first article:

> ... Google has embraced the monolithic model due to its compelling advantages.  Most important, it supports:
> 
> - Unified versioning, one source of truth
> - Extensive code sharing and reuse
> - Simplified dependency management
> - Atomic changes
> - Large-scale refactoring
> - Collaboration across teams
> - Flexible team boundaries and code ownership
> - Code visibility and clear tree structure providing implicit team namespacing

The second article is a survey-based case study where hundreds Google engineers were asked
about their experience with the mono-repo vs. multi-repo models and discusses pros and
cons of the mono-repo model.  The five key findings from the article are as follows (from
Sec. 5. Discussion):

- The visibility of a monolithic repo is highly impactful.
- Developer tools may be as important as the type of repo.
- There is a tension between consistent style and tool use with freedom and flexibility of the toolchain.
- There is a tension between having all dependencies at the latest version and having versioned dependencies.
- Reducing cognitive load is important, but there are many ways to achieve this.

Related to 3rd and 4th points, the paper points out that the multi-repo model brings more
flexibility for engineers to choose their own toolchains, provides more access control,
and enables stability.

Although these two articles articulate the rationale and benefits of the mono-repo based
on Google's experience, one key take-away for me is that the mono-repo model requires
substantial amount of engineering efforts on creating in-house tooling and custom
infrastructures to streamline the development workflow and activities such as code review,
sample code search, API auto-update, pre-commit CI verify jobs with impact analysis and
assessment, and so forth.  Without such heavy investment on infrastructure and tooling
support, the mono-repo model simply would not work.  Looking at Facebook's Mercurial
extension [3] and Microsoft's GVFS [4-7], this seems to be true for other companies that
adopted the mono-repo model but with different approaches/solutions

### References

- Rachel Potvin and Josh Levenberg, "Why Google Stores Billions of Lines of Code in a
    Single Repository," Communications of the ACM, July 2016, Vol. 59 No. 7, Pages 78-87
    (DOI: [10.1145/2854146](http://dx.doi.org/10.1145/2854146)).
- Jaspan, Ciera, Matthew Jorde, Andrea Knight, Caitlin Sadowski, Edward K. Smith, Collin
    Winter, and Emerson Murphy-Hill, "Advantages and disadvantages of a monolithic
    repository: a case study at Google," In Proceedings of the 40th International
    Conference on Software Engineering: Software Engineering in Practice, pp. 225-234.
    2018 (DOI: [10.1145/3183519.3183550](https://dl.acm.org/doi/abs/10.1145/3183519.3183550)).
- Facebook: Mercurial extension https://engineering.fb.com/core-data/scaling-mercurial-at-facebook (Accessed: February 9, 2020)
- Brian Harry, [Scaling Git (February 3,
    2017)](https://devblogs.microsoft.com/bharry/scaling-git-and-some-back-story):
    [GVFS](https://vfsforgit.org) (Accessed: February 9, 2020)
- Brian Harry, [The larget Git repo on the
    planet](https://devblogs.microsoft.com/bharry/the-largest-git-repo-on-the-planet) (May 24, 2017) (Accessed: February 9, 2020)
- Brian Harry, [Perf results on scaling Git on VSTS with
    GVFS](https://devblogs.microsoft.com/bharry/perf-results-on-scaling-git-on-vsts-with-gvfs) (July 6, 2017) (Accessed: February 9, 2020)
- Saeed Noursalehi,
    [https://docs.microsoft.com/en-us/azure/devops/learn/git/git-at-scale](https://docs.microsoft.com/en-us/azure/devops/learn/git/git-at-scale) (Accessed: February 9, 2020)
