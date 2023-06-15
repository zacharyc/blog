---
id: 2621
title: "Building Apps In Airkit"
date: "2022-08-04T23:47:44-04:00"
author: zacharyc
layout: post
guid: "https://zacharyc.com/?p=2621"
permalink: /2022/08/04/building-apps-in-airkit/
categories:
  - Programming
---

I work for [Airkit](https://www.airkit.com). I’m technically a Solutions Engineer but have done a bunch of building and education for the product as well. While the company has a bunch of documentation about how to use each tool, I figured I’d write quickly about how I build an Airkit App, what some of my practices are, and generally how I go about things.

## Start with the UI

My first big tip is to start by creating the UI. One of the greatest things about Airkit is its ability to rapidly prototype interaction with your end users. Create the app quickly and show it to users. Often there are use cases that are missed when initially thinking about a project and this rapid prototyping brings them out.

## Variables and Types

Create types for your complex object. If the data is going to be stored in AirData, then I create an AirData object, but Custom Types are good to explain what you expect the data to look like. Knowing the format of your data is helpful when using it to fill in form details data ops.

Naming is also important. Tables are capitalized where as instance variables are lower snake case. Profile constants can be capitalized snake case. Following this convention will make things clearer to read, but is not enforced by the platform. It is useful for understanding how variables are used across the app.

Scoping of variables is also important. In general, the goal is to minimize the scope of variables as low as possible to allow for more reuse of your components. That means if it is possible keep your variable on a web page then do, because it will come when you copy and paste the page. If you move it up to the flow level you will need to copy the entire flow together to have access to the variable. The downside of keeping everything at the page level is that you might end up passing it in to a bunch of pages, which is also not good. That is the trade off.

Also of note, because of some legacy notions, variable scopes are a little confusing:

| **Web Builder** **Concept** | **Variable Scope** | **Notes**                                                                      |
| --------------------------- | ------------------ | ------------------------------------------------------------------------------ |
| Journey                     | Session            | This is available anywhere in the runtime, but must be passed into data flows. |
| Web Flow                    | Activity Group     | An activity group is available for all the web pages and actions on the flow.  |
| Web Page                    | Activity           | Available only in the context of the web page.                                 |

## Variants and Themes

While each individual element has its style properties in the web builders inspector, the best practice is to store things on variants for each type. Even if the variant is only used once. This gives clear intention to the way you are styling each component and all styles can be managed directly through Theme Builder. It allows them to be reused as well.

## Getting Help

There are plenty of ways to get help with Airkit. Start with the [support site](https://support.airkit.com) and if you can’t find the answer there you can always post a question on the [community board](https://community.airkit.com). If that doesn’t work you can send an email to <support@airkit.com>.
