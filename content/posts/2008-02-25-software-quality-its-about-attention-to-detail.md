---
id: 56
title: 'Software Quality, its about attention to detail'
date: '2008-02-25T07:56:49-05:00'
author: zacharyzacharyccom
layout: post
guid: 'https://zacharyc.com/2008/02/25/software-quality-its-about-attention-to-detail/'
permalink: /2008/02/25/software-quality-its-about-attention-to-detail/
restapi_import_id:
    - 5b3546f08dfe0
categories:
    - Programming
---

[![Competion Staff Shirts](https://i0.wp.com/zacharyc.com/wp-content/uploads/2008/02/competion.jpg?w=1100&ssl=1)](https://zacharyc.com/2008/02/25/software-quality-its-about-attention-to-detail/competion-staff-shirts/ "Competion Staff Shirts")Software quality can be measured in many ways. Complexity, efficiency, executable size, these are just a few of the potential metrics. The bad news is that these aren’t normally mutually exclusive. Normally if you maximize one, you might reduce the others. The hardest part of being a developer is deciding where to sacrifice and potentially how to marry the important metrics for each component we write.

Sometimes, however, we make a bad decision and write what we would call ***bad*** code. Finding the right balance of good is hard, but seeing bad code is easier.

I was talking to a friend the other day about an assignment at work. The story told was enough to terrify me into writing this blog post. Basically, the developer was working on some code in python. They were making a method call and getting back an exception which printed out

 rc = someMethodCall()  
…  
\# returned:  
“error: no error”

Code like this really frustrates me. The programmer who wrote the call is returning an exception with “error: no error”, basically the error was that it executed successfully. I don’t like this approach for several reasons:

1. If you want an exit status, use a return code.
2. “No Error” is not a type of error, so there shouldn’t be a thrown exception for it.

Okay, so I only have two reasons why you shouldn’t do this, but I feel these reasons are compelling.

Now, I’m not saying anything about the developer, perhaps the “No Error” call might be due to some legacy code, but still, if you have this, write a wrapper. Just as if you were the person printing the shirt above. If you are a printer, you should check the quality of what you are printing. Say they did send you the text incorrectly, with the words “Competion”, shouldn’t you look at the message before you blindly attach it to a t-shirt?