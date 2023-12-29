---
title: "Trust in Code"
date: 2023-12-29T09:14:05-05:00
draft: false
---

As a software engineer, you tend not to trust code you don't write yourself. Or even if you have written it yourself, there is a tendency to think we could write it better this time.

Eventually, you run up against a project that is too complex to write from scratch. You will look for libraries and tools to help you solve the problem. Once a library has been located, the questions only grow. Is the library safe? What dependencies does this particular library have? How do I know I can trust it?

One solution is to thoroughly vet the code, line by line, to ensure it is safe. There are many challenges associated with this. First, reading all of someone else's code is challenging. It could be as complex as writing your own. Also, as you are reading and learning the code, the code may change, and keeping up with the changes might be a full-time job. Especially if you are looking at a community project with multiple contributors, you are just one person. Reading the code may be too big an undertaking. Also, even if the project is small, it might have complex external dependencies. If you are researching the safety of a project, you must also explore the dependencies. A code commit in a dependency might open up a vulnerability in your code.

I mention this issue as I embark on a couple of coding projects. One of them I found was [Authorizer](https://authorizer.dev). This project is the most important regarding security as it solves the user Authentication and Identification process. Many of my side projects in the past have fallen apart because I want to invest in something other than building this myself. There are other solutions, like [Auth0](https://auth0.com) by Okta, but those are more expensive. Part of what you get in that price is added security and responsibility, but the cost might be prohibitive for a smaller project. The other truth is that we must discover what is happening on the Auth0 side. Without looking through their codebase, there could be security weaknesses. As more people use Auth0, there is a stronger motivation for malicious actors to find an exploit.

I'm not bringing this up because I have some proposed resolution to this complex challenge. I'm bringing it up because it is top of mind. If you have a better solution, please send it to me!
