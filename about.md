---
layout: page
title: About
---

![about](/assets/about.jpg)
Hello, thanks for visiting my personal website.

I am a Software Engineering Manager at Intuitive Surgical, Inc. (Sunnyvale, CA, USA) that develops and manufactures the da Vinci® Surgical System to enable surgeons to perform delicate and complex operations through a few small incisions (minimally invasive surgery).

I really enjoy designing and building robot software systems. I am always fascinated by carefully structured and implemented software systems that are capable of gracefully dealing with errors and unexpected events, because such resiliency and robustness cannot be achieved by substantial design effort and development experience. While working in the online game industry for a few years, I started to develop my fascination for quality systems. My PhD in computer science (medical robotics) was a great opportunity for me to further deepen my understanding of the system design and to have hands-on experience with designing and building real-time robot control software systems.

## My PhD Research

During my Ph.D. at Johns Hopkins University, I was very fortunate to work with those who pioneered medical robotics since the early days (late 80’s and early 90’s). My Ph.D. advisor is Dr. Peter Kazanzides, who co-founded the Integrated Surgical Systems in 1990 to commercialize the ROBODOC® System for orthopedic surgery. I also had valuable opportunities to work with Dr. Russell Taylor, one of the very early pinoneers of medical robotics.

My Ph.D. research was focused on software system safety for component-based medical and surgical robot systems. The goal was to develop structured and systematic methods to manage safety of component-based surgical robot systems at the middleware or framework level, so that medical and surgical robot systems can be systematically and consistently designed, implemented, tested, and validated. My dissertation takes an architectural approach to safety of robot systems. Its final result was formulated as a software architecture, called the Safety Architecture for Engineering Computer-Assisted Surgical Systems (SAFECASS). I built it as an open source C++ library, which I work on as my weekend project.

In parallel with my research on robot system safety, I also worked on a collaborative research project with THINK Surgical to develop the research ROBODOC System. We built the entire software stack of the system and used it to investigate and develop new methods for kinematic calibration of the robot system, which later became the core module of the TCAT System. Throughout this project, I closely worked with my advisor and Dr. Simon Leonard on the project and had valuable chances to learn from their experience with designing, building, and debugging real-time robot control systems.

I have actively participated in the development of the cisst libraries and Surgical Assistant Workstation (SAW), an open source cross-platform component-based software packages designed to ease the development of computer-assisted intervention systems. The cisst/SAW has been used for medical robotics research in various application areas, such as neurosurgery and retinal microsurgery. One substantial use case of the cisst/SAW is the da Vinci Research Kit (DVRK) project. My contribution was primarily on the cisstMultiTask library that provides the component-based framework for the cisst/SAW-based systems. I have also contributed to other cisst libraries, such as cisstOSAbstration (OS abstraction library), cisstStereoVision (stereo vision processing library), and cisstRobot (computational tools and algorithms for robotics).

## Outside of Work

Outside the work, I am an avid skier and enjoy tennis and biking. I have a KSIA Level 2 ski instructor’s license (comparable to CSIA Level 2~3) and my National Tennis Rating Program (NTRP) level (used by the USTA) is around 3.5~4.0.

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
