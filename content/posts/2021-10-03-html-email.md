---
id: 2417
title: 'HTML Email'
date: '2021-10-03T13:33:24-04:00'
author: zacharyc
layout: post
guid: 'https://zacharyc.com/?p=2417'
permalink: /2021/10/03/html-email/
categories:
    - Programming
    - Web
---

What some of you may not know is that much of the time at Salesforce was spent in the world of electronic mail (or email for short). Email is interesting and relevant today because almost everyone has it and communicates with it. It is an official form of communication.

What you may not understand is that the world of email is rather confusing. Basically, the email that comes over the wire is presented to you by your email client and where email gets very confusing is that there are a million different email clients. You probably use more than one. If you look at your email on a mobile device and on a computer that is two different clients. Then when you think about 3rd party clients and even GMail which renders in a browser, you have a client which is actually a client within a browser.

Because of the various numbers of email clients and security concerns, while the web has advanced, email was still written and styled like the early 2000s web. This means table layouts, no real stylesheets, and things like the **center** tag from way back in the day.

When I left Salesforce, I was hoping that my email wondering days were behind me. Well, for the most part, they are, but one common thing our clients need is to send emails to their clients. Bringing me back to writing stylized email HTML like the 2000s in table layouts.

Despite being very forward-thinking when it was first created, Gmail is usually the hardest client to style for. It’s not really their fault. They are presenting your email in a web browser and they have to be secure on their side of things. I don’t begrudge them thinking about branding and security. Still, things are starting to change and Gmail is now supporting some new things:

- [CSS Support](https://developers.google.com/gmail/design/css#example)
- [Schema.org Proposals](https://developers.google.com/gmail/markup/reference/schema-org-proposals)

Gmail isn’t the only client, though. Because of this, much of the email stuff is still being done with tables. This is pretty challenging for those of us who have spent a bunch of time learning to do things right in CSS (though, to be fair, I’m not the best at CSS).

The association for me feels a bit like the Cobal programmers who were needed to fix all the old code used before the year 2000. Granted, we have better tools for conversion, but this does feel a little archaic.

A Good resource is:

<https://www.udemy.com/course/html-email/> – a good course on how to work through HTML email.

I’m learning more things as I go through this process. So far, I’ve learned that not all divs are respected and also that you have to use a capital M in margin for outlook. You also cannot use SVGs in email, you must use PNGs. More lessons to come as I dig through this project.