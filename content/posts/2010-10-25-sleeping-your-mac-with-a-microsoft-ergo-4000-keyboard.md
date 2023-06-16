---
id: 890
title: "Sleeping your Mac with a Microsoft Ergo 4000 Keyboard"
date: "2010-10-25T21:27:04-04:00"
author: zacharyzacharyccom
layout: post
guid: "https://zacharyc.com/?p=890"
permalink: /2010/10/25/sleeping-your-mac-with-a-microsoft-ergo-4000-keyboard/
restapi_import_id:
  - 5b3546f08dfe0
categories:
  - Programming
  - Stuff
  - Technology
tags:
  - Apple
---

One of my friends, who will remain nameless for the purpose of this discussion, convinced me start playing around with a [Microsoft Natural Ergo Keyboard 4000](http://www.amazon.com/gp/product/B000A6PPOK?ie=UTF8&tag=zacharycohen-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=B000A6PPOK)![](http://www.assoc-amazon.com/e/ir?t=zacharycohen-20&l=as2&o=1&a=B000A6PPOK). I got one at work, then I bought one for the home and I’ve been pretty happy with it. There are just a couple of things missing from my standard mac keyboard.

Firstly, on my old computer, I used to be able to hit the a keyboard combination to get my machine to sleep. I believe it was something like Cmd – Shft – Eject. Well, the Microsoft keyboard doesn’t have Eject. So I’m out of luck there. It does, however, have a set of buttons reserved for favorites. So I decided to code up a little AppleScript and bind it to one of these keys. Here’s the script, and I just saved it as an editable application. Then you can go into the preference pane for the keyboard and assign the whichever key you want to this script. Good luck.

```osascript
tell application "finder" sleep
end tell
```
