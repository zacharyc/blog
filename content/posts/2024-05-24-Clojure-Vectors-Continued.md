---
title: "Clojure Vectors Continued"
date: 2024-05-24T09:12:31-04:00
draft: false
---

I made a few misconceptions in my previous discussion on Clojure Vectors and Lists. While the concept aligns well with Scheme, Clojure has distinct characteristics that set it apart.

Firstly, [here](https://clojure.org/reference/lisps) is a page on the differences between Clojure and other Lisps. The note at the bottom is about List/sequence library manipulations. It turns out Clojure does some very pretty interesting things with Vectors. Mostly, it just makes them easier, but understanding how they work under the hood might be important depending on the use case.

I'm still going through this post on [Understanding Clojure's Persistent Vectors](https://hypirion.com/musings/understanding-persistent-vector-pt-1). To put it a little cleaner, Clojure keeps persistent vectors by using a tree structure and abstracting the vector concept. Clojure can update vectors by creating small chunks of new memory when inserting but allows fast lookup on the order of O(Log32(n)). This means that, in most instances, Clojure vector access is high-speed. Its tree leaf size is 32, so if you are reading sequentially, you can access each item quickly.

However, it's crucial to understand that this memory allocation strategy does come with its tradeoffs. Frequent memory allocation necessitates a robust garbage collection engine to handle unused memory. In a later post, Hypirion delves into the specifics of Vector Performance, shedding light on where the Clojure implementation may experience degradation. This underscores the fact that there are indeed tradeoffs in the design of Clojure vectors.

As I mentioned in my previous post, I'm still going to try to think about how I use Vectors and Lists in my programs.
