---
id: 1125
title: 'Fav Icon Continued'
date: '2012-05-08T15:22:38-04:00'
author: zacharyzacharyccom
layout: post
guid: 'https://zacharyc.com/?p=1125'
permalink: /2012/05/08/fav-icon-continued/
restapi_import_id:
    - 5b3546f08dfe0
categories:
    - 'Make Something Manifesto'
---

I was working on setting up a favicon for this site. You can see it here:

[![Z in circle](https://zacharyc.com/wp-content/themes/zackmatic/images/favicon.ico)](https://zacharyc.com/wp-content/themes/zackmatic/images/favicon.ico)

The process was simple. I created a mock in Sketch using the Futura Font for the “Z”. I then brought the image into Icon Composer, and exported it as an ICO. I modified the functions.php for the theme to include a function for rendering the link tag in the `wp_head`, and that should be it. It’s not appearing for me yet, but I assuming it’s a cache issue for now.