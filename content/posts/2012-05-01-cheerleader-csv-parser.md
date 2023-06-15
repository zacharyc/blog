---
id: 1104
title: 'Cheerleader CSV Parser'
date: '2012-05-01T15:29:09-04:00'
author: zacharyzacharyccom
layout: post
guid: 'https://zacharyc.com/?p=1104'
permalink: /2012/05/01/cheerleader-csv-parser/
restapi_import_id:
    - 5b3546f08dfe0
categories:
    - General
---

The other week we decided to send out a mass email to our cheerleading team in order to get information from each cheerleader. The problem was that we didn’t want to send sizing data about other cheerleaders. This meant a custom written emails for each cheerleader. We had an excel spreadsheet, I exported it to CSV and then wrote a ruby parser to generate custom email files for each cheerleader.

<https://gist.github.com/2568583.js>

There is some room for improvement:

- Parameterize the inputs. Pass in the CSV, destination folder, a template file
- Use a template file for emails. Instead of manually including the message