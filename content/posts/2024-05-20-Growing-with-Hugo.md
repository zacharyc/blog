---
title: "Growing With Hugo"
date: 2024-05-20T09:08:10-04:00
draft: false
tags: ["programming", "Go", "web design"]
---

I've committed to building websites with [Hugo](https://gohugo.io) about ten years after it was cool. I'll admit that I sat on the WordPress bus for too long. I'm currently redesigning [zacroyoga](https://www.zacroyoga.com).

The challenge is that I still need to be a theme designer. Designing a theme would be fun, but I like the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme, but there are certain areas I want to extend beyond it. For example, on zacroyoga, I don't want posts on the front page. The front page is a landing zone. It will have information about me and acroyoga and places to visit. I will put posts on a separate page.

After doing a bit of testing, I figured out that the index page is a `List` `Kind`. This page on [Template Lookup Order](https://gohugo.io/templates/lookup-order/) talks a bit about how this works. This page also explains how to override the behavior because of the way Hugo looks for templates to build files. On this page, you can see how the index page is found:

1. layouts/index.html.html
2. layouts/home.html.html
3. layouts/list.html.html
4. layouts/index.html
5. layouts/home.html
6. layouts/list.html
7. layouts/\_default/index.html.html
8. layouts/\_default/home.html.html
9. layouts/\_default/list.html.html
10. layouts/\_default/index.html
11. layouts/\_default/home.html
12. layouts/\_default/list.html

This is the order Hugo looks for on the index page, which is the site's root. This lineup implies that Hugo considers the root page a list page.

To solve the problem on my site, I added the layouts/index.html page and modified the content so that the articles section was removed from the list page. You can see the commit [here](https://github.com/zacharyc/zacroyoga/commit/79a3746aa7f97e09820151395621f3e4b114eed2).

I know this content is super technical, but I was looking around online and couldn't find it. Hopefully, it helps someone else.
