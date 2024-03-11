---
title: "Paying for Versions or Subscriptions?"
date: 2024-03-06T17:59:49-05:00
draft: false
---

As someone who writes and uses software, I'm often on the fence about how software should be priced. There are programs that are priced per version and those that come with a subscription. There is even a new class of software that is subscribed for updates, but if your update subscription ends, you can still use the latest version of the software you have.

Software is a tricky business, and pricing it is hard.

## Model 1: Pay Per Version

Traditionally, this was my favorite way to buy software. This is also a more traditional way of purchasing software. Back in the day, you would buy a license to a software version, e.g., Adobe Creative Cloud 6 (CC6), and you would get updates to that version and continue to get updates. If Adobe created a version of CC7 with new features, you would either have to pay an upgrade fee or buy the new license. This made sense when your software came on a CD, and you needed to buy the latest version on a new CD.

New software versions were usually substantial. The difference between CC6 and CC7 might have been significant and be a real incentive for the consumer to return and spend more money on the next version. If the updated features weren't significant enough, the public might skip a version. This provided a significant incentive for developers to build really strong versions.

Many programs were released this way that have a very fond place in my heart:

- [Transmit](https://panic.com/transmit/) by [Panic](https://panic.com)
- [OmniGraffle](https://www.omnigroup.com/omnigraffle) by [OmniGroup](https://www.omnigroup.com)
- [TextMate](https://macromates.com)
- [BBEdit](https://www.barebones.com/products/bbedit/) by [BareBones](https://www.barebones.com)

To name a few.

The problem with the model is that there is a lot of pressure on the company and the software to build compelling features for you year after year. If a bunch of bug fixes are required (whether it is the developers' fault or the platform's fault), it might be hard to get a new compelling release.

## Model 2: Subscription Pricing

Adobe switched to this model years ago. In this model, you pay a fee per month or year to use a piece of software. This model originally came around with the SaaS (Software as a Service) model. In the SaaS world, this makes sense. Each month, you must pay for servers, electricity, internet, and other required services. Software manufacturers saw how deterministic the forecasting for SaaS was and started offering subscriptions for their software.

There are benefits for the consumer as well. Instead of spending a thousand dollars for a version of Adobe Creative Cloud, you could spend 50/month and get the same thing, with updates. Adobe could use the subscription numbers to forecast the hiring and maintenance of products. Adobe has funds to pay for their developers to fix bugs, even if major features take a couple of years to develop.

Aside from Adobe, many other desktop products have been added to this model. Notably, Microsoft Office has a subscription payment model. Another piece of design software, Sketch, does the same thing. Even Panic has a model similar to this for one of its pieces of software.

Another factor was the comfortability of consumers in switching to this model. Paying for software tools was like paying for a utility. As SaaS companies started around 2000, many consumers were already paying for online licenses for software that felt similar.

Put that together, and there are many services charging like this. Some of these, I will argue, don't fit this model and should be paid once, not as a subscription. The industry is moving this way.

## Model 3: Hybrid

There is a third model that some developers use. Here is an example from [Panic's Nova](https://nova.app):

![Nova Pricing Page](/assets/img/2024/03/nova-pricing-page.png)

In this model, you pay a flat fee for the product and a year of updates. At the end of the year, if you are happy with the software and don't need updates, you can continue using the latest version of Nova without having to pay.

This is a hybrid of both worlds because the developer can offer new features to incentivize you to renew your purchase at the end of the year, but if you aren't excited about the roadmap, you can just keep the version you have.

This also solves the problem of buying software at the end of a version. For example, you can buy version 4 of Transmit two weeks before version 5 because you will automatically get the updates.

## Challenges with the Subscription Model

The bottom line is that there are some secret problems with the subscription model for non-SaaS software.

### 1: Some Products don't get updates

One of the subscriptions I pay for is [Headspace](https://www.headspace.com). This is a meditation app. They charge about $70/year for their subscription service. I use Headspace daily, or at least I try to. The price per day of use is reasonable. The problem is that I need to start using the same track repeatedly. I'm not using the new features. I don't care about them. Their new editions of the app have made it HARDER for me to do what I want. One interesting cloud feature they have is that it tracks the number of minutes I've spent meditating and day streaks (how many days I've meditated). Still, I don't know if this feature is worth $70/year.

### 2: Versioning apps is Now Crazy

CI/CD (continuous integration/continuous deployment) has caused an exciting development issue. Instead of one major version of software year, a couple of security patches, many products have countless updates yearly. They may release one new version every week, with several additional rollbacks or spontaneous updates. This means while you might be using Adobe Lightroom 2024, you might be using the most up-to-date sub-version of it. You should update it pretty frequently (thinking of the SmugMug Plugin for Lightroom, which I must update EVERY time I use it). Updating may require you to download and wait to use the software. These downloads can be annoying. It gets even worse if the upgrade requires you to restart your computer.

The other problem is that tutorials you might find on the web might need to be compatible with the current version of your software. This has always been the case, but these tutorials get out of date faster with even more versions.

### 3: Forgetting about auto-renewal subscriptions

There have been times when I've forgotten about a software renewal and paid for a renewal that I didn't really need or want. Managing subscriptions is a new challenge, hence the need for apps like Rocket Money that try to identify subscriptions you are no longer using.

Some software companies bank on users needing more time to cancel their subscriptions. Some services even make it very challenging to cancel (e.g., requiring you to contact support).

## Conclusion

There is a space for all pricing models in this world. It only becomes problematic when one company dominates an area and limits the available models. Adobe did that for a while with the CC licensing, but now there are competitors like a Solo License of Sketch or products released by Affinity.

I have always preferred paying for software that I own instead of subscriptions. That being said, there are certain products, like Adobe CC, that I do pay for.

I guess I lament that we are in this world with constant subscriptions.
