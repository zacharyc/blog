---
id: 1180
title: 'WebDriverJs and Chromedriver'
date: '2012-06-25T18:20:59-04:00'
author: zacharyzacharyccom
layout: post
guid: 'https://zacharyc.com/?p=1180'
permalink: /2012/06/25/webdriverjs-and-chromedriver/
restapi_import_id:
    - 5b3546f08dfe0
categories:
    - Technology
---

If you’re not familiar with [WebDriver](http://seleniumhq.org/projects/webdriver/), perhaps you should be (if you’re a programmer). It’s a tool used for performing user tests on websites. I’ve been working on a project for testing some websites with Chromedriver, the chrome implementation of WebDriver. Once you have the driver up and running you need a way to send it commands to get it to do user actions. Chromedriver responds to simple REST requests, which, of course can be issued through JavaScript. This leads to [WebDriverJS](http://code.google.com/p/selenium/wiki/WebDriverJs), a simple implementation of the REST protocol for WebDriver. You can use it server side, with something like node. Or you can use it client side, within the browser.

Here’s where the plot thickened for me. Normally I used to start chromedriver directly:  
[https://gist.github.com/2885890.js?file=old\_way.sh](https://gist.github.com/2885890.js?file=old_way.sh)

Once I had the server up and running I wanted to test  
<https://gist.github.com/2885890.js?file=run-driver(wrong).js>  
with the html:  
[https://gist.github.com/2885890.js?file=wd\_test.html](https://gist.github.com/2885890.js?file=wd_test.html)

I spent several days trying to get this to work. I had no success. I searched the interwebs, and came up with nothing. The solution is simple, but was not apparent. You need to run chromedriver through the webdriver shell.

Here’s the command line:  
[https://gist.github.com/2885890.js?file=with\_selenium.sh](https://gist.github.com/2885890.js?file=with_selenium.sh)

You also have to modify the connection javascript, the run-driver.js should how look the following:  
<https://gist.github.com/2885890.js?file=run-driver.js>

These pieces put together should allow you to control your chromedriver.