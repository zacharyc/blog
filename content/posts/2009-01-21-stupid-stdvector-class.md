---
id: 459
title: "Stupid std::vector Class"
date: "2009-01-21T17:44:25-05:00"
author: zacharyzacharyccom
layout: post
guid: "https://zacharyc.com/?p=459"
permalink: /2009/01/21/stupid-stdvector-class/
restapi_import_id:
  - 5b3546f08dfe0
categories:
  - C/C++
---

The Standard Template Library in C++ is nice to provide us with a bunch of different container classes so we don’t have to re-invent the wheel every time we write new code. One of the classes is called “Vector”, if you aren’t familiar with it, you might not get too much out of this post. But basically, it is a dynamically growing array. Meaning it has contiguous memory and can be indexed like a regular array. It’s a great class and I use it all over the place, but for the second time in one week I find it lacking.

I’m working on some code where I have two vectors of the same type. I want to concatenate one on the end of the other.

```
  std::vector firstVector;
  std::vector secondVector;

  // I want to do the following, but its not legal
  firstVector.append(secondVector);
```

This doesn’t work. There is no append method for std::vector. It turns out that the correct code for this is:

```
  std::vector firstVector;
  std::vector secondVector;

  firstVector.insert(firstVector.end(), secondVector.begin(), secondVector.end());
```

This frustrates me. Append seems like a logical function to include. I’m relatively new C++ developer, having been working in the language intensely for only about a year. My guess is I will reverse my opinion over time, but it just seems like an append() makes sense.

There is also the potential benefit, depending on the implementation of std::vector. Insert requires you to pass in three iterators. Because an append function would have access to the internals of each vector you wouldn’t necessarily need to do the look up of each iterator, which might save a few lines of code. These lines of code might be dwarfed by the amount of code you would need to check the parameter being passed to an append function, I’m not sure.

Regardless of whether or not it is more efficient, I still feel like append() makes sense, conceptually and I would like to see it in future versions of the STL.

(again, I reserve the right to change my opinion in the not too distant future)
