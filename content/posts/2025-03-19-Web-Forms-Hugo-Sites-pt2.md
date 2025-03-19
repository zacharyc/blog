---
title: "Web Forms Hugo Sites - Part 2"
date: 2025-03-19T18:16:36-04:00
draft: false
---

## Designing The Table

Building on [Web Forms On Hugo Sites - Part 1]({{< relref "2025-03-18-Web-Forms-Hugo-Sites-pt1" >}}), the next step, discusses the database table. Database normalization is usually something I'm particularly interested in. Still, for the sake of simplicity, the approach here is designed for speed of entry and retrieval and not for minimization of data. If, for some reason, space becomes the more significant concern, there is room for optimization in this design.

Each form question will be tagged with the form and submission. For example, if Alice submits a form with a collection of answers and Bob submits it with different answers, the question and answers will be tied to the submissions from Alice and Bob, respectively.

Here is the thought process:
![ER diagram for the form field entery table](/assets/img/2025/03/form-erd.png)

Creating the table in Postgres is pretty simple:
![Schema of the form from Postico 2](/assets/img/2025/03/form-data-table.png)
The only additions from the diagram above are adding the ID and setting it as a primary key. Also, the data_added is just a timestamp. Timezone shouldn't be needed because we will use the `NOW()` function to determine the timezone by the server and the user submitting the form.

## Conclusion

This is a small part of the project; I am just creating the table. Next, the code is written on the server side to insert data into the table. Then, it's on to building the JS on the static site side to call the serverless function.
