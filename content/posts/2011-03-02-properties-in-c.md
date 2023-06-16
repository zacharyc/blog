---
id: 918
title: "Properties in C#"
date: "2011-03-02T20:00:29-05:00"
author: zacharyzacharyccom
layout: post
guid: "https://zacharyc.com/?p=918"
permalink: /2011/03/02/properties-in-c/
restapi_import_id:
  - 5b3546f08dfe0
categories:
  - Programming
  - Web
---

I’m a new C# programmer. I’m using it for a project at work. Doing an ASP.NET MVC project. So far I’ve been very happy with the language. It has some nice stuff built in. ASP.NET MVC is pretty nice too. It’s almost as easy to use as rails. So, all in all, I’m pretty happy, but today I ran into something stupid.

I have a method that is trying to do a `TryUpdateModel(model, new[] {"prop1", "prop2"});` call and my model wasn’t getting updated. I checked out the associated FormCollection and sure enough my values were in it. The problem was in how I was defining my model.

```c-sharp
public class MyModel
{
   public int prop1;
   public DateTime prop2;
}
```

Can you see the problem?

It took some digging, but it turns out that prop1 and prop2 as defined above are not properties. They are public members of the class MyModel. In order to be properties you need to assign them getters and setters like so:

```c-sharp
public class MyModel
{
   public int prop1 { get; set; }
   public DateTime prop2 { get; set; }
}
```

My frustration is that prop1 and prop2 from my perspective as a consumer don’t really change with the new definition. It seems weird I should have to do that. I’m a new C# programmer and I totally believe that in 3 months more of working with this language I might become a purist and understand the reason to have these things behave differently, but for someone new to the language this isn’t the most intuitive approach.
