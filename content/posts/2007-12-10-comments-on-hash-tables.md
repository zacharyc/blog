---
id: 31
title: 'Comments on Hash Tables'
date: '2007-12-10T20:06:02-05:00'
author: zacharyzacharyccom
layout: post
guid: 'https://zacharyc.com/?p=31'
permalink: /2007/12/10/comments-on-hash-tables/
restapi_import_id:
    - 5b3546f08dfe0
categories:
    - Programming
---

In a recent article at [Coding Horror](http://www.codinghorror.com/blog/), the author discusses [Hash Tables](http://www.codinghorror.com/blog/archives/001014.html). This is a very strong post on hash tables and their hashing function. It is definitely worth the read, but there is one thing I want to comment on.

In the post Jeff Atwood discusses hash tables and states the following:

> Key-value pairs are quite common in real world data, and hashtables are both reasonably efficient in storage and quite fast at lookups, offering O(1) performance in most cases. That’s why hashtables are the go-to data structure for many programmers. It may not be the optimal choice, but unlike so many things in computer science, it’s rarely a bad choice.

and while I don’t disagree with this comment, I’m afraid that some programmers might misunderstand what is being said here. This post mostly covers the concept of hashing functions. This page is **NOT** saying that hash tables ARE the solution to **EVERY** problem.

One of the biggest problems I see in code that I look at is that people are not fully thinking out their data structures before writing code. Linked lists are great if you are going to be adding elements constantly and searching through your items rarely, but if search is of high demand, that maybe you would want to consider something that has less of a search time. I’m not going to go into [Big O Notation](http://en.wikipedia.org/wiki/Big_O_notation) here, but that is another worthwhile concept for any computer programmer to understand.

Hash tables are great for searching one-to-one mapped pairs. If you are keeping track of person to phone number, than a hash table would be an accurate representation, and a good tool to solve the problem. If the problem were to get more complicated, lets say we start holding the phone number in an object designed to store more than just phone information. If we are writing an App that only looks up by person, then hash table might still be the best choice. If we change our search parameters, perhaps we start looking for people in a certain town, or we have a phone number and want to see if it is associated with anyone in our records, this becomes a costly search.

We end up having to look through all records, because the hash is keyed off of data that is irrelevant to our search. This problem can be solved in many different ways, and the solutions are beyond the scope of this article. My one point is that while hashing is very unique and powerful, it is the the universal tool that solves any and all problems. A very important precursor to Jeff’s article is to decide whether a hash table is indeed the solution you seek, otherwise, space and hashing functions may be the least of your problems.