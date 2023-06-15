---
id: 1286
title: 'Custom UITableViewCell Layout'
date: '2013-12-27T02:45:42-05:00'
author: zacharyzacharyccom
layout: post
guid: 'https://zacharyc.com/?p=1286'
permalink: /2013/12/27/custom-uitableviewcell-layout/
restapi_import_id:
    - 5b3546f08dfe0
categories:
    - Programming
---

At work we were trying to create a custom UITableViewCell. We wanted something that looked like this:  
[![tip cell](https://i0.wp.com/zacharyc.com/wp-content/uploads/2013/12/photo.png?resize=540%2C160&ssl=1)](https://i0.wp.com/zacharyc.com/wp-content/uploads/2013/12/photo.png?ssl=1)

Here are some of the factors that made this problem more difficult:

- Our one custom cell was in a UITableView of regular cells
- The fonts for each of the items in the cell were pretty consistent with the rest of the table view
- Like every other cell, we wanted to it to be indented based on `cell.separatorInset`

I looked at several ways to approach this. I tried using a custom table view. I tried subclassing a UITableViewCell. I finally landed on trying to override the `tableView:willDisplayCell:forRowAtIndexPath:` and it is worth explaining why.

First approach was getting a custom view in place. I turned this approach down because my view really wasn’t that custom. It was actually a tablevViewCell. It actually looked remarkably close to a standard table view cell. It had a text (in this case an NSAttributedLabel), and a detail text (the amount). Putting in a custom view would have required hard coding the layout to match the rest of the cells in the table and that seemed wrong. I also ran into a bit of confusion around getting my separator to be the correct size.

Then I tried subclassing the UITableViewCell. I know subclassing is frowned upon, but I only wanted to override `layoutSubviews`. I took the accessory view and tried and moved it to an offset of the tip label. I ran into a problem where the textLabel and detailTextLabel font color was being set to gray by the fact that I had userInteractionEnabled set to NO. If that sounds crazy, it should. Here’s a picture of what I saw:

[![cell](https://i0.wp.com/zacharyc.com/wp-content/uploads/2013/12/cell.png?resize=500%2C73&ssl=1)](https://i0.wp.com/zacharyc.com/wp-content/uploads/2013/12/cell.png?ssl=1)

After overriding UILabel and trying to see who was calling setColor on it, I came up with nothing useful. This felt like the wrong approach.

Lastly, I looked at `tableView:willDisplayCell:forRowAtIndexPath:`. When you first get into this method, the cell’s subviews frames have yet to be calculated. I called `[cell layoutSubviews];` which is costly, but get the dimensions I needed. Inserting the the editView after the label is then simple math. Here is what the code roughly looks like.

<https://gist.github.com/zacharyc/8141791.js>  
[gist](https://gist.github.com/zacharyc/8141791)

The downsides of this approach is the double rendering of the cell, but the benefit is that we get to keep our cell as close to factory as possible. In our case, we have one custom drawn cell on the page, so the performance doesn’t take that big of a hit.

There are other approaches to this problem, namely [Mensa Smart Tables](https://github.com/jordanekay/Mensa), but including another library seemed like overkill for what we needed.