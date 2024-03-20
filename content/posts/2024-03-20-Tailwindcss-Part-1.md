---
title: "Tailwindcss Part 1"
date: 2024-03-20T19:06:37-04:00
draft: false
---

I'm working on a new project and am motivated. We have carved out some aggressive goals, so I'm spending time writing software and learning more about Clojure. I even got to file a bug on [Calva](https://github.com/BetterThanTomorrow/calva/issues/2443) and work with Pez on it.

So, on to the subject of this post, [tailwindcss](https://tailwindcss.com). This is a framework for generating CSS in your HTML by using utility classes. These classes you put directly on your HTML elements affect how they appear. The benefit is that you don't need to jump between content and styling. The styling happens based on the classes you put on elements.

On top of tailwind, we are also using the [daisyui](https://daisyui.com) plugin. This plugin allows you to style colors and themes, and builds some visual components on top of tailwindcss.

Here's what I like:

- You don't need to jump between CSS and HTML.
- Using hiccup-type styling, including multiple classes, is VERY easy.
- There are tons of classes.
- The bundle tool with Tailwind keeps the CSS smaller than if it included everything (it only consists of the classes you use).
- This is a commonly used framework, so there are easily findable examples of how to do many things.

Here's what I DON'T like:

- It is hard to know which class to use where. Remembering the utility classes is a whole new level of memorization on top of standard CSS values.
- The documentation on the tailwindcss and daisyUI has yet to make sense to me. There is still more to grok before mastery.
- Because things are made of utility classes, I wonder how things will work when we want to have named classes and provide styles for them. This feels like a prototyping language that will be replaced when we get to production.

There is still a lot to read and learn, so don't consider this a final opinion in any way, shape, or form. More to come as I learn.
