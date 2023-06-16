---
id: 186
title: "The Address of Monkey"
date: "2008-09-06T22:05:44-04:00"
author: zacharyzacharyccom
layout: post
guid: "https://zacharyc.com/?p=186"
permalink: /2008/09/06/the-address-of-monkey/
restapi_import_id:
  - 5b3546f08dfe0
categories:
  - C/C++
---

Have you seen the following C code sample:

```
	char x = 1;
	char c = x["monkey"];
```

Do you know what it the value of c is? Don’t read on unless you want to know the answer and why. The value of c is ‘o’. Why? Well, I wrote some code to start playing around with this. The answer seemed simple, but here were some suggestions about why the answer is ‘o’:

- 1 is the index into the string “monkey”
- There is some magic with math of memory on the stack for the compiler used
- Something else is happening

Okay, it seems relatively trivial now, but when I looked at it it wasn’t. Other people were putting up ideas so I tested them out. Here is my silly test code:

```
#include

void initial_test()
{
	char x = 1;
	char c = x["monkey"];

	printf("What is c:%cn", c);
}

void different_index()
{
	char x = 2;
	char c = x["monkey"];

	printf("What is c:%cn", c);
}

void space_allocation()
{
	char x = 1;
	char v = 'd';
	char c = x["monkey"];

	printf("What is c:%cn", c);
}

int main(int argc, char** argv)
{
	initial_test();
	different_index();
	space_allocation();

	return 0;
}

/* Output:
What is c:o
What is c:n
What is c:o
*/
```

What is actually going on here is really just the associative property of addition. I was telling a friend that I would understand “monkey”\[x\], but not the other way around. This is the quote from my friend (who wishes to remain nameless):

> I mean, technically it’s base_address + sizeof(datatype)\*index. since sizeof(char) == 1, it’s just base_address+index. 1+addressof(“monkey”) or addressof(“monkey”) + 1.. they both work

In the end it was just a fun little exercise.
