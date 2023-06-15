---
id: 502
title: 'C++ Coding Standard: The If Block'
date: '2009-03-10T15:15:44-04:00'
author: zacharyzacharyccom
layout: post
guid: 'https://zacharyc.com/?p=502'
permalink: /2009/03/10/c-coding-standard-the-if-block/
restapi_import_id:
    - 5b3546f08dfe0
categories:
    - C/C++
---

Almost two months ago I went to a [CocoaHeads](http://cocoaheads.org/us/SiliconValleyCalifornia/index.html) meeting during Macworld. They had [Mike Lee](http://www.atomicwang.org/motherfucker/Index/Index.html) talk. His presentation was about “Pimping Your App”. There were a bunch of interesting points, but one thing really stuck in my head. Mike was talking about how is a messy person in his life. His car is messy. His room is messy. His desk is messy. Everything is messy, except his code. HIs code is crystal clean, squeaky even. As a programmer you need to make sure your code is consistent and clean. Ever since I have been thinking about standardizing the way I write code. This is the first post in hopefully a stream of posts about quality code.

Yesterday, there was a discussion in the office about code quality. There were many points discussed, topics like line length, white space, and my personal favorite “if” statements. I have a track record of being incredibly inconsistent with my “if” block. The basic if block is the following:

```

if(foo) {
  //...
}
```

The “if” statement by itself is really not that big of a deal. It’s when you start adding “else if” and “else” clauses that it becomes complicated. The problem for me is twofold. Firstly, I’m inconsistent. The type of blocks I use on larger sections of code is different from the blocks I use on smaller sections of code. Secondly, my desire for consistency is at odds with my crazy, cooky desire to have code look aesthetically pleasing.

#### The Condensed If Block

I sometimes use the following style of the if statement:

```

if( foo ) {
   //...
} else if( bar ) {
   //...
} else {
   //...
}
```

This block is very condensed. You throw the braces for each clause on it’s own line. I feel that it this type of statement makes it clear and easy to really make the if statements a smaller part of the code. On trivial if blocks, I really like this approach. Where it suffers is in more complex if statements. If the ifs and else ifs fit really just blend into the code, sometimes making it easy to miss them. Okay, so if I’m looking at the code in detail, not a big ideal, but if I’m just giving it a quick glance over I might miss something. Also, if the “if” statement line is long enough, it could easily blend into the line below it.

#### The Almost Condensed If Block

This one is a take on the Condensed If block. It is actually just really poorly formatted “if” statements, but I often find myself using this one:

```

if( foo ) 
{
   //...
} else if( bar ) {
   //...
} else {
   //...
}
```

All we are doing here is moving the opening brace from the end of the if statement to the next line. The rest of the code follows the condensed. So, I really like this approach because the first “if” block is clearly separated from the rest of the code. It’s clear that we are are entering an “if” statement line. The remainder of the statements don’t take up too much space. The closing brace, the else if/else, and the following opening brace are all on the same line.

The downside of this approach is that it looks inconsistent. Why does the initial “if” statement get one extra return, and all the subsequent lines statements get jammed into one line? It’s not functionally different, and it might in general be more appealing to me, but consistency is also important. I have started to shift away from using this style.

#### The Intermediate If Block

This one has more white space:

```

if( foo ) {
   //...
}
else if ( bar ) {
   //...
}
else {
   //...
}
```

This approach has gives you a little bit more separation of the control statements from the code. For some reason, though, I just feel it looks weird to write the close brace on its own line but then incorporate the opening brace on the same line as the control statement. Still feels inconsistent.

#### White Space Heaven If Block

The following block is the last if style I’m going to talk about:

```

if( foo ) 
{
   //...
}
else if( bar )
{
   //...
}
else 
{
   //...
}
```

This block takes up a very large amount of space, everything gets its own line. It is probably the clearest of all the examples above, but the trade off is that your code is now three lines longer for each else statement. This extra space means that you can theoretically fit less code in the same amount of screen space.

#### Additional Concerns

There are a couple of additional concerns when working with if blocks. For example, if you are chaining “if” blocks, how much space should you provide.

```

// What I don't like
if(foo)
{
   //...
}
if(bar)
{
   //...
}

// What I prefer
if(foo)
{
   //...
}

if(bar)
{
   //...
}
```

I have run into some people who prefer the first option above with no space between each block. The reason I dislike this so much is that depending on the method of “if” syntax you use, you second if block could look identical to your else blocks. As your code gets large and complex, it is important to make it as easy to discern different control paths that might be executed, and in this case, white space is really your friend.

Another concern is the ternary operator. This operator is basically a simple “if/else” block which fits on one line.

```

double number;
if(foo)
    number = 3.1415;
else
    number = 2.71828183;

// As opposed to
double number = foo ? 3.1415 : 2.71828183;
```

Ternary operators are great for doing assignments as in the one line above, but be careful with trying to do too much in one line. My general rule is the line is getting really long, or I’m doing multiple clauses in my condition I tend to shift away from ternary operator.

#### Conclusion

The problem with all of this is that my mind changes depending on where I am in, what I’m working on and what I plan to be doing with my code. I’m learning towards using the condensed form of the “if” block in the future for the simple reason that I can fit more lines of code in less space (not to mention that some pointed out it was the K&amp;R way, too). Bottom line, whatever method you choose, you should really stick to it as best you can for each project. If you open up a file in a project that was edited by someone else, you should probably follow their precedence.