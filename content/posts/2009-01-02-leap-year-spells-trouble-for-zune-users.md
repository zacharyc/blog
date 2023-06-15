---
id: 447
title: 'Leap Year Spells Trouble for Zune Users'
date: '2009-01-02T16:30:58-05:00'
author: zacharyzacharyccom
layout: post
guid: 'https://zacharyc.com/?p=447'
permalink: /2009/01/02/leap-year-spells-trouble-for-zune-users/
restapi_import_id:
    - 5b3546f08dfe0
categories:
    - C/C++
---

On December 31st, all 30GB Zune users woke up to their music players not working. In a rarity for Microsoft problems, the source for for the problem was found. There is a good explanation of the problem [here](http://www.zuneboards.com/forums/zune-news/38143-cause-zune-30-leapyear-problem-isolated.html).

There are two lessons to be learned from this: 1) be careful of your looping conditions. 2) Try and write your code in small snippets that are testable, and write tests! A simple iteration through the total amount of days including a leap year would have caught this bug.

Just FYI, I’m not saying I would have been good enough to catch this, but it is worth writing down so I try to remember for myself.