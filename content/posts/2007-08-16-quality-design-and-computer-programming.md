---
id: 1686
title: 'Quality Design and Computer Programming'
date: '2007-08-16T07:44:00-04:00'
author: zacharyzacharyccom
layout: post
guid: 'https://zacharyc.com/?p=11'
permalink: /2007/08/16/quality-design-and-computer-programming/
restapi_import_id:
    - 5b3546f08dfe0
original_post_id:
    - '11'
categories:
    - Technology
---

Recently a friend and I had a conversation about the quality of programmers in the workplace. Without delving too deeply into the specifics (so as not to get anyone in trouble), we discussed various metrics for measuring programmers and how they perform. That conversation, along with a recent talk I heard about quality of code, leads to the conclusion that as systems get more and more complex in our society, quality of code, effected by the quality of programmers, will become a serious matter.

Firstly, lets talk about the breadth of programmers in this world. Programmers are just one shape and size. Their skills range from systems level programmers to high level web designers. Some programmers know assembly, others also know the intricate details of Photoshop. This wide range of skill determination make it very difficult to judge the “Quality” of a programmer. This gets further complicated by the fact that in order to judge a quality programmer, you need to judge the quality of the code/product produced. Much of this judging could be subjective. This is a conversation for another realm, and other people to handle. I just want to centralize this post on the conversation that happened between me and my friend.

The conversation arose around some code like the following:

``

if(state.to\_upper() == "AL")

 print "Alabama";

elsif(state.to\_upper() == "AK")

 print "Alaska";

.

.

.

elsif(state.to\_upper() == "WY")

 print "Wyoming";

else

 print "Unknown State";

What are your thoughts on this code? Is it efficient? Would we consider this good code?

Well that depends on many different factors. As a programmer, my first instinct when I see this code is: WHY??? Why do you have to go through 100 lines of code to find Wyoming? As a programmer I see a hash. I see a one to one mapping set. That train of though, however, is limited, it does not take into consideration several factors that might crop up. From what I can see there are a bunch of factors that can determine how you write code, but in this example I really see three main factors.

1. **Efficiency:** If you the environment that your code will be running on and you can test it, it may be significantly faster to use the above set of code than dealing with setting up a hash and using hash algorithms. Conversely, if you don’t know the exact environment, you may be taking a risk assuming this factor.
2. **Maintenance:** If you are looking to write code that can be easily updated and modified, say for example we decide to add Costa Rica, to your list, is it simple and easy, and straight forward. While this is a simple example, consider if we need to add a bunch of items to our statements, the above approach might be better represented as a Hash.
3. **Readability:** This is a tough one, because there is both a positive and negative of this code in terms of readability. One, it puts all your code inline, meaning that you don’t have to jump to another file to see where a bunch of values are defined. However this approach also eats up a ton of space in your file that you have to scroll thus making more difficult to understand.

**Conclusion** Coding is not always easy, and sometimes there is a tradeoff for what you decide to actually implement in your code. It best to try and consider why and for whom you are writing your code and that will help you make the best choices.