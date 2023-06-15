---
id: 2702
title: 'Documentation Formats'
date: '2023-01-30T15:27:02-05:00'
author: zacharyc
layout: post
guid: 'https://zacharyc.com/?p=2702'
permalink: /2023/01/30/documentation-formats/
categories:
    - Programming
    - Technology
---

Life is full of things to catalog, especially for someone like me. Someone who loves organization in data and looking for patterns. Someone who is convinced that the random things in my life will probably come together someday like the unification theory. But how? How does one sort, contain, and search data?

The first step is recording the data. There are many ways to do this. Databases have traditionally been a great way. NoSQL databases with their loose document format are interesting. The second brain methodology uses documents or notes to contain the same thing. And while these documents can be formatted in things like Markdown and have front matter for categorization, much of the data is contained in the raw text which means a human has to parse and read it.

Before you expect this post to come to some epic realization, tl;dr; I still don’t have one. This post is about the methods out there I’m considering for sorting my life.

#### Option 1: SQL

I’m not a fan of no SQL databases. From my point of view, if you are going to create data to exist in a place that is typed, loose document formats make comparing and reading things hard. So structured data is better, hence SQL.

**Pros:**

- The data is structured from the start
- There are many different options for which SQL platform to use and many of them are interchangeable so there are options.
- Things like normalization define best practices for working with something like this, so you don’t have to develop them yourself.

**Cons:**

- You need to run a server somewhere.
- It is not easily human decodable.
- You need to learn to use SQL to really be successful and joins are fun (and hard).
- Because structure is required you have to define it up front.

#### Option 2: Markdown

This is honestly what I’m currently using in my second brain with Obsidian. This may be the best of all worlds. It has the notion of storing structured data in front matter, and throughout the document with special tags. Much of the document remains readable in sentences, but it is in loose format and you have to create and maintain your own formatting standards.

**Pros:**

- Format is loose so you don’t need to stress about it.
- Much of the notes are human-readable.
- There are many tools to convert markdown to the web for sharing.
- Cost of starting is very low.

**Cons:**

- Because the format is loose, the responsibility lies on the creator to maintain the structure desired.
- The organization of individual documents is also important.
- Search is only as good as you are at searching and remembering.
- It’s easy to end up with a mess of documents.

**Option 3: Stricter document format**

This category contains things similar to markdown but with more structure. This category fits things like JSON, YAML, and TOML. This is following the Pragramtic Programmer guideline of storing things in the text but putting some structure behind it. Some of these formats are more readable than others.

**Pros:**

- Easily computer parsable.
- More human-readable than a SQL database

**Cons:**

- No official typing.
- Need to use a validator to confirm you have a valid document.
- Nothing requires the structure like a SQL Table so searching could be difficult.

## Summation

I don’t have a conclusion. I’m still thinking, but these are interesting options of how to start really putting the data together. Our lives are full of data, it’s a shame when it gets lost or mislabeled or put in a place where we can’t find it. Hopefully, I’ll start putting together something more useful.