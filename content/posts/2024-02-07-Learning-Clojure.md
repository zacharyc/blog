---
title: "Learning Clojure"
date: 2024-02-07T19:00:26-05:00
draft: false
tags: ["programming"]
---

I'm working with a friend on a top-secret project I hope to tell you more about soon. Still, because my friend likes functional programming, I'm dusting off some of the material I learned in college at Villanova and better understanding some concepts that escaped me back then.

## What is Clojure

What is [Clojure](https://clojure.org)? Clojure is a Lisp-like, functional programming language that compiles jar files to run on the JVM. This means it will run anywhere you can run Java. It also means you can use existing Java libraries in your Clojure code.

Being Lisp-like means you get a ton of parenthesis, and much of the language is written in itself. This implies you can overwrite existing functions to reach your desired behavior. This is both cool and pretty risky. But it also means you can understand how much of the code is written.

As someone who comes from Objective-C and other environments where there is compiled code, you can't see the source; it is refreshing to know that I can look up what is going on under the hood of a defined function.

## What I like so far

As mentioned above, because many of the internal functions are written in Clojure and available, it is possible to see how standard functions are created. Theoretically, it is easy to uncover how anything works. In reality, it is taking more time as there are some interesting patterns in Clojure that I need to get used to, and more on what I don't like later.

Clojure is primarily a functional programming language, meaning most functions are pure. This implies they returned the changed state instead of modifying the state in place. This makes things like concurrency easier to get right. It makes testing more manageable because you can treat functions like a black box from a testing perspective. If you put the same thing in, you expect the same thing out. Pure functions don't have side effects on the state.

ClojureScript is another excellent piece of code. It takes Clojure and compiles it to JavaScript instead of a Jar file. This means you can effectively write the same language for both front-end and back-end. Yes, you can do the same with Vanilla JavaScript and other languages. While most languages can be written functionally, it's not their only or primary way of writing.

Community. Clojure, as a Lisp-like language, has a strong community surrounding it. It takes a particular type of person to love writing the way Lisp inspires you to write. The community around Clojure is generally full of brilliant, capable developers.

## What I don't love

Unlike Lisp, Clojure has many special characters and codes to make writing certain things faster. [Weird Characters](https://clojure.org/guides/weird_characters) is a site with many odd characters that can be used in Clojure. I have referred to this page a fair bit when looking through some of the Clojure projects I'm going through.

I was brought up programming C. Something about me loves how C is so linear and straightforward. Learning to loop through items in Clojure differs from a standard for looping in other languages.

Getting code up and running is more complex than some other scripting languages. Despite its simple syntax, Clojure requires compilation to be run, and it can be more complicated. When I started writing this post, I was trying to write a simple Clojure hello world.

```clojure
(ns helloworld.core)

(defn -main
  "I can say 'Hello World'."
  []
  (println "Hello, World!"))
```

This is a simple function. Still running, it requires compilation, and the most simplistic way I could find was through [Leiningen](https://leiningen.org).

## Summation

I wanted to use a conclusion, but I'm not there. I'm still learning the language and working on this project with it. I'm still deciding whether to make a conclusion about Clojure. I will be writing some more about this as I learn more.

Right now, I'm excited about the project and the teammate I'm working with. I'm willing to put up with the headache of learning something new and get to work on this fun codebase.

More to come soon.
