---
title: "Tailwind Part 2"
date: 2024-04-12T08:28:42-04:00
tags: ["frontend", "css", "programming"]
draft: false
---

I've been working in a tailwind environment for a couple of weeks on this Clojure project. I have some more opinions about it, and I figured I'd share.

Firstly, Tailwind is pretty powerful. One of the reasons we are using it is because of its plugins like DaisyUI, which should allow us to theme our app more easily. Looking at the documentation, there are classes for everything you need to style your front end. The challenge is that it is not always clear how to go from a known CSS property to a Tailwind style. I find myself constantly referring to the documentation.

What this means is that there is an additional translation layer. There is something to fix in the layout. I know how I want to do it in CSS, but then I have to figure out a suitable tailwind class to add to that element and apply it. There is an additional layer in our project because we are using Clojure. So sometimes my dot notation for my class doesn't apply, and I have to include a class on the element:

```clojure
[:div.my-class {:class "p-4"}]
;; vs:
[:div.my-class.p-4]
```

We are still determining why this is the case, but it is frustrating to keep trying to get my CSS to work the way I hoped.

It's still early, and I'm still grumbling and getting used to Tailwindcss, so I reserve the right to reverse my current opinion. However, I still miss using [Sass](https://sass-lang.com) or even standard CSS. It is one less layer of translation, and I'm just more familiar with it.
