---
id: 1376
title: 'D600 Shutter Speed'
date: '2015-04-20T06:52:21-04:00'
author: zacharyzacharyccom
layout: post
guid: 'https://zacharyc.com/?p=1376'
permalink: /2015/04/20/d600-shutter-speed/
restapi_import_id:
    - 5b3546f08dfe0
categories:
    - Photo
---

The D600 is a great camera and my first full frame camera. I’ve had it for several years now but to be honest, I haven’t taken the time to become an expert in the use of the camera. As a traditionalist I’ve used the different modes on the camera but only recently have I ventured into some of the other modes and advanced metering modes.

Over the past couple of months I’ve shot several cheerleading events. When I shoot these events I normally take the pictures and convert them quickly to JPEG for the coaches to review. I started shooting directly in JPEG fine. I could fit more pictures on the card and it seemed like camera could take them quicker. The problem was that at NCA nationals I wanted higher quality images so I wanted to shoot raw.

Things were going pretty well and I was happy with the shots I was getting until right at finals I made a terrible mistake. I switched memory cards because my card in slot 1 ran out of space. The problem was that I replaced the card with a slower memory card. Just as we were performing in Challengers cup, my camera speed went down significantly. After the performance I started to do the math.

| Image Format | Image Size | Buffer |
|---|---|---|
| NEF (RAW), Lossless compressed, 12-bit | 23.4 MB | 22 |
| NEF (RAW), Lossless compressed, 14-bit | 29.2 MB | 16 |
| NEF (RAW), Compressed, 12-bit | 20.7 MB | 27 |
| NEF (RAW), Compressed, 14-bit | 25.4 MB | 16 |
| JPEG Fine Large | 12.4 MB | 57 |
| JPEG Fine Medium | 7.4 MB | 100 |
|  
If a lossless 14 bit NEF is roughly 30 megs, and my memory card has a write speed of 40 megs, you are copying less than 2 images per second. At that pace, it doesn’t matter if your camera can take 5 to 6 frames a second, if you eclipse your buffer space you will be waiting for images to copy before you can take another frame. During a 2 minute 30 second routine, getting stopped up can be a serious problem. It turns out that there are several speeds of SD cards you can buy. My original cards were 95mb/second (which actually write at about 90mb/second) my second card was only 40. I’ve rectified the problem by purchasing two more 95mb/second cards. This leads to the following math:

| Image Format | Pictures Copied Per second |
|---|---|
| NEF (RAW), Lossless compressed, 12-bit | 3.846 images/second |
| NEF (RAW), Lossless compressed, 14-bit | 3.082 images/second |
| NEF (RAW), Compressed, 12-bit | 4.348 images/second |
| NEF (RAW), Compressed, 14-bit | 3.543 images/second |
| JPEG Fine Large | **7.258 images/second** |
| JPEG Fine Medium | **12.162 images/second** |

The D600 has a frames per second limit of 5.5 frames per second. What this table shows is that in order to get maximum number of frames per second with a 95 mb/second you need to shoot in JPEG.

Anyway, I hope this helps anyone who ran into my issue.