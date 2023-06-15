---
id: 159
title: 'Wanting To Find A Bug'
date: '2008-09-02T15:15:30-04:00'
author: zacharyzacharyccom
layout: post
guid: 'https://zacharyc.com/?p=159'
permalink: /2008/09/02/wanting-to-find-a-bug/
restapi_import_id:
    - 5b3546f08dfe0
categories:
    - Programming
---

This happened to me last week. Yet another lesson learned. I was working on debugging some code at work. Someone was complaining about some functionality in an element we draw on screen. In order to better diagnose the problem, I wanted to create an example and see if I couldn’t get the problem to reproduce. Not a bad first step.

The problem was that as I wrote out the code I made a typo on the code I was writing. I wrote something like the following snippet:

```

     // ... 
     int x = pixels2OtherUnitsX(20);
     int y = pixels2OtherUnitsX(23);

     // ...

```

If you look closely you will see that I’m using `pixels2OtherUnitsX()` in both cases, where I should probably be using `pixesl2OtherUnitsY()` in the second case. Oops.

What do you know, my image didn’t render correctly on screen. I had recreated the bug that someone said was out there. Now all I had to do was figure out where in our production code the bug was. I spent way too long looking around for the problem.

**Lesson** don’t be so blinded by your desire to find a bug you miss one that is right in front of your face.