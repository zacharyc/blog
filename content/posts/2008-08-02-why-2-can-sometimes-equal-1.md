---
id: 96
title: 'Why 2 can sometimes equal 1'
date: '2008-08-02T15:53:44-04:00'
author: zacharyzacharyccom
layout: post
guid: 'https://zacharyc.com/?p=96'
permalink: /2008/08/02/why-2-can-sometimes-equal-1/
restapi_import_id:
    - 5b3546f08dfe0
categories:
    - C/C++
    - Programming
---

Ran into a fun situation today where I was writing some code, and I came across an interesting situation in C++. Now, before I get to the end of this post, I’ll give you the punch-line, Developer stupidity.

So I was working on a exercise where I needed to write some sort of state machine.

```

enum STATES{
  STATE_1 = 0,
  STATE_2,
  STATE_3,
  ...
};

/* ... some other code ... */

switch(state) {
case STATE_1:
    // Do something
    state = STATE_2;
    break;
case STATE_2:
    // Do some other stuff
    state = STATE_3;
    break;
case STATE_3:
    // Do the last state of stuff
    // This code never gets called.
    break;
}
```

In this code STATE\_3 is never reached. The code for the enum was working fine, but the state wasn’t being reached. I went over this for a while, until I found out the problem.

```

bool state = STATE_1;
```

The assignment for the state variable had been left over from a previous implementation of the code, and when you set the Boolean value for state = 2;, you get 1, which is true.

Now I don’t expect anyone to be as silly as me and make this mistake, but just in case, learn from my lesson.