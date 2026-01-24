---
title: "Font Awards and AI Coding"
date: 2026-01-24T16:21:48-07:00
draft: false
tags: ["programming", "font", "ai"]
cover:
  image: "/assets/img/2026/01/amador-loureiro-BVyNlchWqzs-unsplash.jpg"
  alt: "Letter type graphic"
  caption: ""
  relative: false
---

Sometimes I get a crazy notion to put something together and decide to do it on a whim. That is the story of [font-awards](https://www.font-awards.com). It is my first fully AI project (sort of, as in sort of fully AI).

A former coworker and good friend was talking about how they created a quick prototype of a project using nothing but Windsurf and AI, and how they were able to build out the project's scaffolding very quickly, with very little manual input.

The next day I had an idea that it would be cool to honor all the fonts that were created in 2025 and have people vote on them in a bracket. After reaching out to Dan Cederholm of [Simple Bits](https://www.simplebits.com) for a sanity check, the idea carried some merit. The project began with a pretty simple ask of Claude Code: could you make an online app with Next.js that lets people vote on fonts and pick the best one through a bracketed system? Not going to lie, the first version of it took less than an hour.

The first version used standard web fonts, didn't have a font preview, and was far from good, but the time-to-quality ratio was rather impressive. Still, like all coding projects, the last 20% of the work has taken 80% of the time. The site is live, and we are actually past the initial round and onto the bracketed rounds.

So far, AI has issues with deploying code, making reusable components on its own (I have to prompt it write reusable components), and general style issues.

The scope of this project was relatively simple, so doing it with AI was a great way to see it really shine. The security was not a super big concern with this app, as I'm not storing any personally identifiable information, only tracking voted cookies. It has inspired me to use it on some other bigger projects, though not for the full thing. I'm excited to see how this tool can help me bring more of my ideas to reality in the software space.
