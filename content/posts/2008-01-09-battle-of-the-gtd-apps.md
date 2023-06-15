---
id: 40
title: 'Battle of The GTD Apps'
date: '2008-01-09T14:26:28-05:00'
author: zacharyzacharyccom
layout: post
guid: 'https://zacharyc.com/?p=40'
permalink: /2008/01/09/battle-of-the-gtd-apps/
restapi_import_id:
    - 5b3546f08dfe0
categories:
    - Programming
    - Technology
tags:
    - Apple
    - Apps
---

[Getting Things Done (GTD)](http://en.wikipedia.org/wiki/Getting_Things_Done) has become increasingly popular in past few years. There have been many attempts to build an application that integrates with the whole framework. As a mac user I have been aware of a few, but the big one of the past was [Kinkless GTD](http://kinkless.com/kgtd). This application consists of a bunch of applescripts meant to work with [OmniOutliner](http://www.omnigroup.com/omnioutliner). There was a lot of hype surrounding the application, and for good reason, it was one of the best options out there. The problem was, it wasn’t good enough for me to get really committed. You had to hit this “sync” button ever couple of seconds to make sure everything was up to date, contexts were confusing, and sometimes the kinkless page would go down for days at a time. Others shared my concerns and now there are several different applications that aim to fill the same gap that KGTD left open. In this article I will be comparing [OmniFocus](http://www.omnigroup.com/omnifocus) and [Things](http://culturedcode.com/things/).

People at Omni recognized a good nitch for a better product and so began to create a new product [OmniFocus](http://www.omnigroup.com/omnifocus). This product would be directly geared towards the kinkless users and perhaps pick up more users in the wake of the new GTD craze. As of this post, I’m aware that omni has sold over 11,000 licenses for its application, which just hit version 1.0 yesterday (no, they didn’t make 11,000 in a day, they have been selling the product in beta for a couple of months).

Now, I’m a big fan of Omni products. I swear by [Omnigraffle](http://www.omnigroup.com/omnigraffle), and there are some interesting uses for [OmniOutliner](http://www.omnigroup.com/omnioutliner) that sometimes make it more useful than excel or numbers (it is much FASTER than numbers). However, I have been using OmniFocus for a little while and am a little disappointed that they have released version 1.0 in the condition it is in. This app feels like it is so far from done, that I can’t understand how it can be at revision 1.0. Also, they up until announcing version 1.0, they were calling the builds alpha builds, which leads me to believe that this might be a premature release.

Here is a list of some of things that are frustrating me with the app:

- There is a “Clean Up” button on menu bar that you have to hit in order for your tasks to disappear. I agree that making them disappear as soon as you enter them is bad UI design, but the fact that I have to click on this button to move everything is also bad. I wonder if there couldn’t be a clean up every time you switch contexts or projects or if you stop using the application for several minutes if the clean up could happen automatically.
- The views are still a little confusing. This could be because I have never been a big subscriber to the GTD methodologies, I just want an application that organizes all my tasks, I don’t care about the FORMAL practice elements.
- The autoupdate feature continues to crash every time I install an update. Well, it claims to have crashed, if I look at the version of OmniFocus, it will say that is running the newest version.
- The App doesn’t **feel** like a finished Leopard App. There is zebra striping in some of the windows. I’m not a big fan of high contrast zebra striping, I feel like it takes away from the users focus.

Despite my misgivings, the app has a strong community and a good development core. There are a couple of really great things about the app that make me wonder how it will progress in the future. Here are a couple of the features that I like about OmniFocus

- Integration with iCal To Dos. This means that it will appear on your iPhone (or other syncable phone) currently. Also the way in which they do this is very smart. They allow you to select certain contexts to be synced with your iCal, which means if you are only interested in your Errands while you are mobile, you can set it to only sync those tasks and leave the rest off.
- Potential integration with [OmniPlan](http://www.omnigroup.com/omniplan). This is a great app for project management. It is the most Mac-like project management app I’ve seen and if you could hook OmniFocus to a specific project it would be easy for people to see what they have to complete, without having to look at OmniPlan and then copy it tasks to OmniFocus (this is not very [DRY](http://en.wikipedia.org/wiki/Don't_repeat_yourself)).
- Better integration that KGTD. This applications is specifically designed to do many of the things that KGTD did, but it does it natively, whereas KGTD was a bunch of add on Applescripts. KGTD also made all of your toolbars in OmniOutliner look like a KGTD app (they might have fixed this in later versions of OmniOutliner, but I can’t remember and don’t feel like installing this all over again).

This leads me to my next app, [Things](http://culturedcode.com/things/). This app is made by a much smaller company in Germany, so it might not have the same market penetration as the OmniGroup, but in my opinion this is what I really expect in terms of a GTD application. Keep in mind that I have only been using Things for about a day and I have been following OmniFocus for quite some time now, so my feedback on this app might not be as complete. Before I jump into feature analysis, here is a screenshot of things:

[<span class="Apple-style-span" style="color:#000000;text-decoration:none;">![Screenshot of Things](https://i0.wp.com/zacharyc.com/wp-content/uploads/2008/01/things_window.png?w=1100&ssl=1)</span><span class="Apple-tab-span" style="white-space:pre;"></span>](https://zacharyc.com/2008/01/09/battle-of-the-gtd-apps/screenshot-of-things/ "Screenshot of Things")

Now, Things is still in a beta stage, and the author claims that they will be releasing the code later in the spring. The price of this app will be $49 when released, compared to the OmniFocus $79. The overall look and feel of the app, though is still significantly more “finished” than OmniFocus, but some of the main features of OmniFocus are missing.

Here’s a rundown of what I like about Things:

```
<ul>    
    <li>Very professional looking application. Okay, yes I'll admit it, looks are only skin deep, but when it comes to working with an app, if it is pretty look at, you will look at it more, therefore I feel that aesthetics can count for something here.</li>  
    <li>The cost is lower than OmniFocus. Saving money is always a good thing.</li>
    <li>The layout is more structured than OmniFocus. By this, I mean that the menu on the let has specific sections: Collect, Focus, Organize; and then brakes down the tasks within this section. If I don't know the full GTD rules or I don't want to reread David Allen before I start using the application, this makes it more clear where I should put all my tasks.</li>   
    <li>It allows you tag your items. This is both a positive and a negative for me. It allows me to put tags with an item that I think belong in different projects and then find them together, but the downside is, Tags replace the notion of context in OmniFocus. I think these are two different items, tags relate to the type of app, but I feel like context relates to where/how the task should be completed. By handling both of these with items with tags its not always clear how to differentiate which tags belong to which.</li> 
    <li>The Focus section allows you to clearly see what you have to do and what you can do. The whole goal of GTD is to make it easy to see what you should be doing next. This focus section does exactly that.</li>
</ul>

```

Despite all these good features (and the one issue with tags that I have already mentioned), there are several other issues that I have with the application:

- No direct support for integration with iCal or mobile devices. This feature is on the roadmap, but it is unclear when it will be implemented, and I think it is very important to have it.
- No ties to any specific project management suite. This could cause issues with having to enter your information twice.
- Currently no way to recur items. If you want to repeat an item every day, right now, that just isn’t possible. This whole notion of recurring calendar events is probably pretty tricky to get right, but it is still an important feature that is missing. Again, this is in the future features, but no indication is provided on when it will be available.

There are a bunch of additional features intended for Things, which you can see [here](http://culturedcode.com/things/wiki/index.php?title=Future_Features).

As for me, I have made up my decision, I’m going to try to stick with things for a little while and see how that works out. If OmniFocus has some major changes perhaps I will give it another look, but right now, I’m just enthused by the application. Also, if anyone else has any other task management applications they are using, please add a comment or contact me.