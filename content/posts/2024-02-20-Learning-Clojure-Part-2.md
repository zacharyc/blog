---
title: "Learning Clojure Part 2"
date: 2024-02-20T20:53:50-05:00
draft: false
---

I am still working on learning [Clojure](https://clojure.org) for a fun project. As I'm going through the learning process, I want to talk about a couple of resources.

## Calva

If you like [Visual Studio Code](https://code.visualstudio.com), which I do, you should know about [Calva](https://calva.io), an extension for VS Code. This extension is fantastic. It has a straightforward way to get a REPL up and running and a starter project, making playing around with the language pretty simple.

Another benefit of the extension is that it comes with a starter project with lessons on learning Calva and Clojure.
![Calva Starter Project](/assets/img/2024/02/calva-starter-project.png)

I like to learn from books, so I bought [Programming Clojure and Third Edition](https://pragprog.com/titles/shcloj3/programming-clojure-third-edition/) from Pragmatic Bookshelf. I've been a fan of their books before, but this book could be more beginner-friendly. The Calva "Getting Started REPL" has an excellent tutorial for the language. It feels better tailored to a Clojure language beginner than the book. I'd suggest starting here.

## Leiningen

The slogan for [Leiningen](https://leiningen.org) is:

> for automating Clojure projects without setting your hair on fire

And it's not wrong. As I mentioned in my [previous post](https://www.zacharyc.com/posts/2024-02-07-learning-clojure/), because Clojure is run on the JVM, writing simple scripts is challenging because the code must be compiled into a `jar`. Leiningen solves some of these problems by creating a structure for you.

You can send your project to another person and have them run it with Leiningen or distribute it as a compiled jar (called an uberjar) to run with just a Java runtime.

The project I'm currently working on was not created with Leiningen, but my sample learning projects have been. It's pretty simple to set up and use.

## Path Continues

While I'm progressing with Clojure, I still have much left to learn. Programming without a ton of side effects is exciting. This is particularly hard while I'm also working on learning more about Swift and SwiftUI. The languages are about as different as can be. Still, more to come.
