---
id: 171
title: 'MFC&#8217;s Radio Button Hack'
date: '2008-09-04T16:15:51-04:00'
author: zacharyzacharyccom
layout: post
guid: 'https://zacharyc.com/?p=171'
permalink: /2008/09/04/mfcs-radio-button-hack/
restapi_import_id:
    - 5b3546f08dfe0
categories:
    - Programming
    - Usability
---

**Disclaimer:** I am a mac user, but a windows programmer.

MFC is Microsoft’s old Window framework. Basically it is an object oriented wrapper around the traditional Win32 programming environment presented by Microsoft to help develop windows. Win32 is many years old, and so is MFC. Microsoft’s new frameworks, .NET and WPF (Windows Presentation Framework) are supposedly better than MFC, but I have yet to play with them.

MFC has tools for many different types of controls, from buttons to dialogs, windows, and menus. MFC allows the user to create the button, override some basic functionality, provide message callbacks and otherwise manipulate the application. Buttons are particularly interesting because the base class for [buttons](http://msdn.microsoft.com/en-us/library/yf1wax6c(VS.80).aspx) actually provides a ton of functionality for many different types of buttons. From this one class, you can get push buttons, check boxes, radio buttons, owner draw buttons (the programmer handles the rendering of these buttons), etc.

<figure aria-describedby="caption-attachment-172" class="wp-caption alignright" id="attachment_172" style="width: 240px">[![A Group of Radio Buttons](https://i0.wp.com/zacharyc.com/wp-content/uploads/2008/09/radiobuttons.png?resize=240%2C105&ssl=1 "Radio Buttons")](https://i0.wp.com/zacharyc.com/wp-content/uploads/2008/09/radiobuttons.png?ssl=1)<figcaption class="wp-caption-text" id="caption-attachment-172">A Group of Radio Buttons</figcaption></figure>

I have several problems with this class design, but today I just want to talk about my gripe with Radio Buttons. The term [radio button](http://en.wikipedia.org/wiki/Radio_button) comes from the buttons on old car radios, where only one button could be pushed at any one time. Radio buttons on a computer form, are by definition grouped with other radio buttons so that only one in the group can be selected at any one time. Any time a user selects another button in the group, the previously selected button should become unselected.

Taking this even further, logically, you should only use a radio button in certain situations. You have several options, usually less than 10, and you want the user to select from one of them. You should be able to have a default option set, and this choice should somewhat make sense. This functionality is very similar to a drop down box. In a drop down, you have a bunch of options (please put them in some order), where the user should select only one item. The difference in use between radio and drop downs depends on your application, but in general, you can put more items into a drop down. Drop downs will take up less screen real estate, but not all the choices may be obvious to the user, and sometimes the user may select the first option that seems relevant rather than looking through the whole list. In a radio group, all the options are present at the start.

This brings me to my gripe. MFC radio buttons are just the same as any other CButton. The way you define that a radio button is a radio button is by passing a style flag that is either `BS_RADIOBUTTON` or `BS_AUTORADIOBUTTON`. The difference is that auto radio buttons will look to be part of a group. This group is defined by ORing the `BS_AUTORADIOBUTTON` style with `WS_GROUP` for the first element of a group. All subsequent radio buttons will be part of that group until you create another `WS_GROUP`.

This upsets me because radio buttons in a group are associated with the other buttons in that group. They shouldn’t just be loosely coupled like this. It puts a lot more responsibility on the programmer to understand how the grouping is done. If you look at the picture above, you will notice it is from my Mac. In Interface Builder, Apple does not provide you with individual radio buttons, it instead provides an object called a “Radio Group”. This group is a collection of radio buttons that handles all the magic I wish existed in MFC. To be fair, Apple’s implementation is pretty new, they have redefined the way to create code on the Mac no less than 8 years ago with release of OS X. Microsoft’s MFC is much older than that and they have new technologies out there which probably better handle this problem. My issue is simply that I am working with legacy code here, and am incredibly frustrated by the lack of UI thought that went into designing this library in the beginning.