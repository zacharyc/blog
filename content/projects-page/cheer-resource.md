---
id: 42
title: "Cheer Resource"
date: "2008-01-25T15:27:52-05:00"
author: zacharyzacharyccom
layout: page
guid: "https://zacharyc.com/projects/cheer-resource/"
restapi_import_id:
  - 5b3546f08dfe0
---

#### Motivation

Cheerleading has been growing in popularity over the past decade or so, and as more and more cheerleading gyms open up the diffusion of knowledge has been dispersed. The goal of Cheer Resource is to take information relating to cheerleading and group it together on one complete, easy-to-use website for the entire community to enjoy.

To that end, the following sub-goals are at the hear to of Cheer Resource:

- Consolidate distributed information from multiple sources into centralized location.
- Utilize modern standards to provide easy integration in to other modern web services.
- Extract useful statistics and information from the distributed information sources to help grow the sport.

#### Phased Implementation

The scope and goals of this project are large enough that I have decided to implement a phased implementation:

- [Phase 1: Gym Locations](#phase_1) – The first phase of the project is provide a database of known cheerleading gyms in an easy to search user interface.
- **Phase 2: Basic Cheerleading Terminology –** Provide a basic dictionary for common cheerleading terms including pictures, videos and potentially rule classifications for each trick
- **Phase 3: Competition Integration –** Add information regarding upcoming competitions, including locations on search interface, and potentially competiton results.
- **Phase 4: Team Statistics –** Provide metrics on how teams are performing based on competitions and titles. At some level it might even be possible to track individual performance if teams post rosters.
- **Phase 5: Cheerleader Database –**Provide a database of famous cheerleaders and their accomplishments

The following sections will describe each of the phases in more detail.

#### <a name="phase_1"></a>Phase 1: Gym Locations

Currently there are several ways to locate a cheerleading gym.

- Talk to others involved in the cheerleading industry for recommendations.
- Look in a phone book under cheerleading
- Visit [cheerleading.net](http://www.cheerleading.net) and search through their text based list for your gym.
- Visit [usasf.net](http://www.usasf.net) and use their member gym finder to find a gym in your area.

These are all good options, but Cheer Resource will combine all of them into one solid approach. I will discuss how each of these solutions is really incomplete and demonstrate how to Cheer Resource will integrate these approaches.

##### Talking to others in the Industry

There is no substitute for first hand experience, and a great way to do that is talk to experts in the industry. Talking to a gym owner or coach might be a great way to find out about local programs, but each gym owner or coach believes that the gym that they are currently at is the best fit in the area, and will undoubtly be somewhat biased. While their opinions shouldn’t be ignored, the represent their own point of view.

Also as you move outside local area, coaches and gym owners might not have solid recommendations, or might only know of a few programs instead of garnering the full grasp of all programs in some other target location.

##### The Phone Book Approach

This approach just doesn’t work. Many phone books (including mine) don’t have a listing for cheerleading. Some gyms are not listed and you can’t get the quality of a gym based on size or design of the advertisement in the phone book. Even a photo of the gym facilities might be misleading.

Phone books are also local to one specific set of towns. If you are on the edge of a town and the neighboring town has gym, you might miss it because your phone book might only cover your town.

##### Cheerleading.net

[![cheerleading.net Independent Gym Listing](/assets/img/2008/02/cheerleadnet_net_window.thumbnail.png?w=1100&ssl=1)](/assets/img/2008/02/cheerleadnet_net_window.png?ssl=1 "cheerleading.net Independent Gym Listing")

[Cheerleading.net](http://www.cheerleading.net) was one of the first site I started using when I got into the sport. I moved around a lot as kid and would have to look up neighboring gyms, and this site was the best thing that was out there.

Here’s what I like about this site:

- Large set of cheerleading programs including: high school, college, and independent (defined as all-star and youth league).
- Design of the site makes the links and text relatively easy to view.
- Lists on the site are built with syntactically correct, definition lists.

[![Cheerleading.net Gym Listing](/assets/img/2008/02/cheerleadnet_net_list_selection.thumbnail.png?w=1100&ssl=1)](/assets/img/2008/02/cheerleadnet_net_list_selection.png?ssl=1 "Cheerleading.net Gym Listing")

This site has been around for a long time and is definitely a good resource, but there are a couple of areas where this site falls short:

- Each gym list is sorted only alphabetically. This is useful if you know the name of the school or program you are looking up, but not if you are looking to locate a gym by location.
- They do provide city and state, but there is no easy way to find an actual address of the gym from the site. This makes finding the gym closest to you difficult, especially if you are new to an area and do not know the geography.
- The site does not doing any recurring tests to ensure that the gyms are still current. Out of the 504 independent gyms, about half were non-working links.

##### USASF Member Gym Search

The last and probably the most trusted database (but potentially the worst interface) is [USASF’s](http://www.usasf.net) Member Gym Search. USASF is the governing insurence body for most all star gyms in the US. More and more competitions are requiring that you become USASF certified before participating in an event. For this reason, USASF has an up-to-date, very accurate representation of most of the All-star gyms.

They have made their gym information available to the public through the gym finder. Here is a screen shot of the application.

[![USASF Gym Finder](/assets/img/2008/02/usasf_gymfinder.png?w=500&ssl=1)](https://zacharyc.com/projects/cheer-resource/usasf-gym-finder/)

Here are my frustrations with this application:

- To find the gym search you have navigate through the Javascript menu, using Members -&gt; Member Gym Search. If you are a member you probably do not need to locate another gym. This functionality should be more accessible to the average user.
- **_This is the deal breaker!_** Once you select a country and a state (both of which are alphabetical) you have to search through the city list to find your City. This list is **_NOT_** in **_ANY_** reasonable order. It’s not alphabetical and it is not by location. This means you have to look through potentially the whole list for each town in your area.
- This site is limited only to All Star programs. If you are looking for a Pop Warner team, or local colleges, you are out of luck.

##### Cheer Resources Approach

Cheer Resource aims to fill the gaps in the above implementations in several ways. The site will contain several ways to look up gyms:

1. Through a Map based interface element. Gym’s will appear as markers on the map. This will easily allow you to identify gyms in your area.
2. A tabular list of gyms that will allow to search and sort based on criteria that you specify.

We hope to maintain an accurate set of contact information for as many gyms as possible. At some point we will allow gyms to populate their own information and keep up to date, but in the beginning we will start with a list of data generated from various different public facing websites.

We will employ modern technologies, like Microformats, to convey the information in ways that will allow other developers to have access to our content.
