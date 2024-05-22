---
title: "Lists vs Vectors in Clojure"
date: 2024-05-21T20:30:49-04:00
draft: false
tags: ["programming", "clojure"]
---

One of the projects I'm working on for [Gluino](https://gluino.io) has me thinking about data structures again. Data structures are ways of storing data in memory (either program memory or on disk), and the choice can be significant.

I'm working on a list of requests with scores and values. This list grows dynamically as items enter and leave it. It could contain 0, 1, or many items.

Let's discuss the implementation of these structures in a more common programming language better to understand the difference between a list and a vector. Simply put, a vector is like an array of memory, whereas a list is more similar to a linked list. Here is some C code creating an array, which is akin to a vector:

```c
int num_array[10] = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55};
// Creates an array of integers accessibly sequentially

printf("Num at fourth position is: %d", num_array[3]);
```

Each number in the array/vector is stored sequentially. This is great for high-speed access because we don't have to visit any previous elements to get the fourth (0-based index).

The downside of an array/vector comes when you want to add another value to the end of the array. You can't just do that. Something may already be stored in the memory location right after the 10th element. So, to add a new element to an array/vector, you need to create a new array/vector with your item added:

```c
int new_num_array[11] = malloc(sizeof(int) * 11);
memcpy(new_num_array, num_array, sizeof(int) * 10);
new_num_array[10] = 89;
```

Lists in Clojure are more like a Linked List. Each item in the list has a pointer to the next one (assuming it is singly linked). Here is how one would make a list in C:

```c
struct NumberItem {
    int item;
    struct NumberItem* next;
} twelve, twentyFour;

// main func
    struct NumberItem *list = NULL;

    twelve.item = 12;
    twelve.next = &twentyFour;
    twentyFour.item = 24;
    twentyFour.next = NULL;

    list = &twelve;

    printf("first is %d, and second is %d\n", list->item, list->next->item);

```

What we can see in this code is that items in a list are grouped by pointer. Adding or removing an item is about updating pointers, not reallocating memory.

## Clojure

Clojure provides an abstraction for these concepts in vectors and lists.

```clojure
;; List
(list 1 2 3)
;; Vector
[1 2 3]
```

The difference is that lists don't guarantee order, but you can add and remove items easily. Vectors, on the other hand, are sets of contiguous memory, and the order is guaranteed, but adding or removing an item requires allocating new space for a newly created vector.
