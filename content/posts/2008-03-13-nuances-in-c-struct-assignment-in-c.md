---
id: 59
title: 'Nuances in C: Struct Assignment in C'
date: '2008-03-13T16:09:00-04:00'
author: zacharyzacharyccom
layout: post
guid: 'https://zacharyc.com/2008/03/13/nuances-in-c-struct-assignment-in-c/'
permalink: /2008/03/13/nuances-in-c-struct-assignment-in-c/
restapi_import_id:
    - 5b3546f08dfe0
categories:
    - C/C++
    - Programming
tags:
    - Structs
---

When I started this post, it was going to be a revolutionary post, talking about something that was really bothering me. As I have spent more time thinking about this, the answer seems so simple and obvious, still there was a time where I did not get this concept, so I here is a brief post on the topic,

The question is, in straight C, will this work:  
``

```

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct point_t {
  int x,y;
} Point;

int main(int argc, char **argv)
{
  Point a,b;
  int c[4] = {1, 2, 3, 4};

  b = c;

  printf("b(%p) is now b[x] = %d, b[y] = %dn", &b, b.x, b.y);

  return 0;
}
```

In C++ this works no problem. Structs are teated like classes where all members have public scope. Assigning one struct to another simple implements the copy constructor that is created by the C++ language, but what about straight C?

Well, like I said the answer is the obvious one, IT WORKS! The reason this originally confused me was because you **CAN’T** do this:

```

   int a[4] = { 1, 2, 3, 4};
   int b[4];

   b = a;
```

Why not? The compiler knows how big each of these integer arrays are. If you run `sizeof(a);` and it will give you the same thing as `sizeof(b);`. Copying an array is as simple as copying over the bytes (bit for bit), using `memset()` or something similar.

The reason structs work and arrays don’t is simple. Basically we are doing a type check on the object. If the object is a struct of defined type, we know how to do an assignment because we have the size. If the item is an array of integers, we would have to do a size comparison and the compiler doesn’t do that.

Okay, so I hope that explains the obvious, good luck.