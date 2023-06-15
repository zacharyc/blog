---
id: 1398
title: 'Writing a Safari Extension'
date: '2015-10-30T04:21:34-04:00'
author: zacharyzacharyccom
layout: post
guid: 'https://zacharyc.com/?p=1398'
permalink: /2015/10/30/writing-a-safari-extension/
restapi_import_id:
    - 5b3546f08dfe0
categories:
    - Web
---

I’ve switched to using Safari as my primary browser. It works pretty well because I use it on all my devices so passwords and bookmarks are available on all devices.

The one downside, the developer community isn’t as big. We use [Github](http://www.github.com) at work for all of our repositories. Github code diffs are constrained by the width of their center column. On larger diffs this can make it hard to see all of the code without tons of scrolling. There is a [chrome extension](https://github.com/xthexder/wide-github) for this task, but there hasn’t been a safari extension for this same task, so I decided to write one.

I have worked on several chrome extensions in the past, so I thought this would be pretty easy, but there are a couple of challenges that I didn’t expect in completing the code. I’d like to share my experience with anyone else starting to write an extension, so hopefully you don’t run through the same issues that I did.

Firstly, you can see the code I used to make the extension [here.](https://github.com/zacharyc/safari-widen-github)

This essentially takes something like this:  
[![Narrow Github](https://i0.wp.com/zacharyc.com/wp-content/uploads/2015/10/Screen-Shot-2015-10-29-at-9.13.10-PM.png?resize=1024%2C711&ssl=1)](https://i0.wp.com/zacharyc.com/wp-content/uploads/2015/10/Screen-Shot-2015-10-29-at-9.13.10-PM.png?ssl=1)

and turns it into something like this:

[![Wide Github](https://i0.wp.com/zacharyc.com/wp-content/uploads/2015/10/Screen-Shot-2015-10-29-at-9.13.16-PM.png?resize=1024%2C711&ssl=1)](https://i0.wp.com/zacharyc.com/wp-content/uploads/2015/10/screen-shot-2015-10-29-at-9-13-16-pm.png?ssl=1)

Here are some of my tips for writing a Safari Extensions:

- If things aren’t working the way you expect, don’t trust the reload. Restart the browser!
- Even if you just want to do something simple, you need to have a base html page. This page can hit your javascript, but you need to follow the developer instructs.
- Your HTML page can listen for events and then send actions to your javascript, but you have to listen to all commands and filter out the ones you don’t want.

While I’ve shared my extension with a coworker, I’m pretty sure I”m the only one who uses it. You an download the extension from [here](https://zacharyc.com/safariextensions/Wide%20Github.safariextz).

Comments and suggestions are welcome.