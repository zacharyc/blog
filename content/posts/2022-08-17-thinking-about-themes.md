---
id: 2636
title: "Thinking About Themes"
date: "2022-08-17T20:16:30-04:00"
author: zacharyc
layout: post
guid: "https://zacharyc.com/?p=2636"
permalink: /2022/08/17/thinking-about-themes/
categories:
  - Design
  - Technology
---

I’m not a visual designer, but I do like pretty things.

On the top of my mind recently has been the idea of my Purple Owl Theme. It comes from the “Night Owl” theme on [MonoLisa’s website](https://www.monolisa.dev).

Blue background with a big purple highlight. Light gray as a text color. I love the theme, and I’ve tried to make a version of it for [Obsidian](https://obsidian.md). In doing so, I realized that actually figuring out what colors goes where is confusing. Colors that make sense on the MonoLisa site don’t make sense in my Obsidian theme. There are also a bunch of additional color and syntax settings for something like my Obsidian notes that aren’t really matched to any of the theme values from the MonoLisa site.

I look at some other themes like [Monokia Pro](https://monokai.pro) and see that they are using mostly 6 colors and backgrounds.

There has to be a better solution to theming. Having to write themes for everything, customizing for each individual application. As we do themes at [Airkit](https://www.airkit.com), the same thing applies. We have things like “Brand-Primary” and “Brand-Tint1” and various other colors defined within our apps.

After talking to a VERY smart coworker he turned me on to Design Tokens. Design tokens are the elements of style that Salesforce uses in their Lightning Design System (LDS). They define a set of tokens that are then used throughout their various different products. They use tools to take these defined tokens and send them out to SASS out for web products and p-lists for iOS, etc.

After looking at [LDS Design Tokens](https://www.lightningdesignsystem.com/design-tokens/), there are a bunch of things on there that aren’t exactly what I’m looking for. I’m looking for a way to define a few select attributes and have a tool interpret it into a full theme that is usable in many different applications. Looking at [Solarized](https://github.com/altercation/solarized/tree/master/adobe-swatches-solarized) they only have 16 defined colors.

Anyway, I’m not done with anything yet. I’m just starting to think through this project.
