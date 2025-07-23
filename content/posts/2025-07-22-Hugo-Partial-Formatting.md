---
title: "Hugo Partial Formatting"
date: 2025-07-22T09:36:00-04:00
draft: true
---

I'm late to the game. Writing most of my web projects in WordPress has been a staple of my younger self. I started writing PHP in college and naturally transitioned to using WordPress for almost all of my projects. Throughout the years, these sites have been made in WordPress:

- [zacharyc.com](https://zacharyc.com) - Now built with Hugo.
- [zacroyoga](https://www.zacroyoga.com)
- [patagoniafanboy](https://www.patagoniafanboy.com)

Here's the rub. WordPress is great for interactive features, such as accepting comments and starting forums. Even if you are looking to create an e-commerce site, WordPress is a solid choice. The challenge is that WordPress is built on PHP, and it has evolved over many years, forming its own ecosystem. There are tools on top of WordPress, such as Elementor, that make it easier to create reusable elements in your WordPress site. However, the site still sits on a Database, which primarily houses text. If your site doesn't do a ton of interactivity, then it might not be necessary to use a system like WordPress. If you want to move your blog posts, you need to run a SQL query against your database to get the posts out. You need to install an extension to enable post caching, which reduces the number of times your website needs to recreate pages. Then, when you are developing, you need to turn that off to see changes more expediently.

It helped that the providers I used had 1-click WordPress installs. This made creating a new site straightforward. Before I knew what was happening, I had several websites running on WordPress, each with its own database and PHP code. Whenever a vulnerability was found in the WordPress code, I would have to update the sites manually. Every time you didn't update the site, you left your website and the server it was hosted on vulnerable to attacks from malicious actors.

All this has led me to Hugo. Maybe this post should have been titled **"Why Hugo?"** Skipping ahead a bit, I settled on Hugo to try and master. It creates a static site, has a decent amount of online support, has a strong community, and has been around for a while.

## Understanding Partials and Shortcodes

In my day job, before transitioning into iOS Development, I worked on a variety of web development projects with [Ruby on Rails](https://rubyonrails.org/). Much of my internal terminology is built on the vocabulary popularized by Rails. In Rails, a partial is a small piece of code that is reused multiple times. It allows you to adhere to one of the primary tenets of Rails: DRY (Don't Repeat Yourself). If you can write it once and reuse it, you can save yourself a lot of trouble when you need to refactor or make changes. This reusable code is typically saved in a file called a _partial_.

Hugo also has partials. But Hugo partials are not the same as Rails Partials. To understand how they differ, it's essential to recognize that there are two primary types of content in Hugo.

- **Layouts** - These are usually theme templates, but they are used for rendering the shell of the page. This rendering process happens first.
- **Content** - This is the content of a page or post. It is often written in Markdown. It occurs after the layout code is compiled. Generally, content code resides in the `content/` directory.

Hugo has two ways to make reusable code. Partials and Shortcodes. Both live in the `layouts/` directory.

### Partials

Partials are reusable code used for _layouts_ only. This code is used when creating the page design, but you cannot access it in the content. The whole reason this post exists is that I've made this mistake _several_ times. I write a component or piece that I want to reuse in a partial, only to find out that I can't access partials from a Markdown file. You need to create shortcodes for that.

Examples of partials that come in standard themes are:

- Header - your site's headers file
- Head - The content that goes in between your `<head>` tags
- Footer - Your site footer file

Your theme can include multiple files, and you can override them by placing them in your local layouts directory.

Partials CAN call other partials.

### Shortcodes

Shortcodes are reusable code pieces that can be used in content. The one I use most often is `rawhtml`, which allows me to embed some HTML into my content pages, for example, when I need a table. Shotcodes are tremendous and are mostly what I'm thinking about when I'm writing partials.

They can be embedded with [nested shortcodes](https://gohugo.io/content-management/shortcodes/#nesting).

## Should I be using Hugo?

Many sites these days are not just static sites, but many of the ones I'm developing today are. For a write once and then serve model, Hugo has been working great. When building a more complicated auction site, Hugo is not the right platform for that.

There are other competitors out there as well, like Jekyll and 11ty. I chose Hugo because I wanted to spend some time learning more Go. C was my first real programming language, and Go was written by part of the team behind C.
