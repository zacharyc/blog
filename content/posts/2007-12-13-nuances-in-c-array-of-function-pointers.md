---
id: 32
title: 'Nuances in C: Array of Function pointers'
date: '2007-12-13T17:31:06-05:00'
author: zacharyzacharyccom
layout: post
guid: 'https://zacharyc.com/?p=32'
permalink: /2007/12/13/nuances-in-c-array-of-function-pointers/
restapi_import_id:
    - 5b3546f08dfe0
categories:
    - C/C++
    - Programming
---

I was in a job interview the other day and someone asked me the following question, which I got wrong. Its not hard to remember, but I figure if I pass it on, and anyone out there who reads this blog for technical content might get a little refresher.The question was something like: write the declaration for an array of function pointers that take an integer and return a double in C.

This problem isn’t overly complicated, but C can be a tricky language. I used the language for a year of solid development, and never had to use anything this complicated.

My attempt at this problem without any resource ended up looking like:  
 `double function_array(int foo)[];`

Okay, before you laugh, remember I haven’t had to ever actually defined a complicated structure like this. What this translates to in C is: a function named “function\_array” is takes an int “foo” and returns an array of doubles. This is not possible in C as you can’t return arrays. You can return pointers, which can be indexed as an array, but you cannot return an array.

The solution is actually:`double (*function_array[])(int foo);`which solves the problem as stated.

The resource that I used to find the answer is a book called [Expert C Programming: Deep C Secrets](http://www.amazon.com/Expert-Programming-Peter-van-Linden/dp/0131774298/ref=pd_bbs_sr_1?ie=UTF8&amp;s=books&amp;qid=1197566443&amp;sr=8-1). This book is *AMAZING* and you should definitely invest in it if you do any serious work with C. It does have a bit of a Sun systems bias, as the author was a compiler writer for Sun Microsystems, but the book has useful information for anyone using the language. There is a whole chapter on unscrambling declarations in C.

So there it is, another friendly reminder about declarations in C.

### Update:

After rereading the post I realized that I was not content with my understanding of how to use arrays of functions. I came up with a mock project to work on. Lets say you have an input string, and would like to process it to remove some special characters (in my case I used “:”, ” “, and “t”). I wrote a function for each special character and iterated through all the functions on each string. This might not be the most expedient way of solving this problem, but it allowed to me to test the use of arrays of functions.

You can see the source: [here](https://zacharyc.com/wp-content/uploads/2007/12/function_arrays.c). It has some brief inline documentation, but I’m not doing anything else too crazy. One additional note, I rediscovered that if you initialize a string like `char *foo = "some string";` it stores it read only memory. Note that is different than `char foo[] = "some string"` which is stored in read/write memory.