---
title: "Cedar Unit Testing"
date: 2024-01-24T13:58:06-05:00
draft: false
---

Almost 13 years ago, my life changed. I had recently left Motorola after Google acquired us and was looking for my next opportunity when I found a company called Cabulious, which was pretty quickly renamed to [Flywheel](https://www.crunchbase.com/organization/flywheel-software). When I joined, they asked me if I'd be interested in working on the mobile team, specifically iOS, despite having minimal experience in Objective-C.

When I joined the company, they sent me to New York to work with our Pivotal Labs Team (we could only get the team in NY, not the one in California, because they were too busy). The leader of our project, Adam, was one of the maintainers of Cedar, an Objective-C Unit testing framework that Pivotal Labs used to build TDD code. Cabulous had just hired a new leadership and was taking the existing product that had been written in some language that could be ported to both iOS and Android and shifting it to native products to increase the reliability and stability of the project.

TDD, or test-driven design, is one of the significant principles of Pivotal Labs. The notion is that you write a test describing something you want your software to do that it currently doesn't do, watch it fail, and then write the most straightforward code to make it pass. If there is another condition you need, write that in as well.

At the time, Apple's unit testing software wasn't what we needed, so we worked with [Cedar](https://github.com/cedarbdd/cedar). If you look at the project, it hasn't been updated in a LONG time, and that is because most new software for Apple devices is being written in Swift. Also, Apple has improved its unit testing offerings to the point where a 3rd party option isn't needed.

Here's some Cedar code from the website:

```objective-c
describe(@"Example specs on NSString", ^{
    it(@"lowercaseString returns a new string with everything in lower case", ^{
        [@"FOOBar" lowercaseString] should equal(@"foobar");
    });

    it(@"length returns the number of characters in the string", ^{
        [@"internationalization" length] should equal(20);
    });

    describe(@"isEqualToString:", ^{
        it(@"should return true if the strings are the same", ^{
            [@"someString" isEqualToString:@"someString"] should be_truthy;
        });

        it(@"should return false if the strings are not the same", ^{
            [@"someString" isEqualToString:@"anotherString"] should be_falsy;
        });
    });
});
```

This should seem very similar if you are familiar with RSpec or other options.

While working on our project at Flywheel, our tests grew very complex. Because a bunch of our code was UI-based, we would end up writing these very long, complicated, nested code chains, and when something needed to change, we would spend a lot of time rewriting the tests under the UI.

Coming in, I was very optimistic about TDD, but after working with the massive amounts of tests we wrote, I'm a little less rigid with my practice. I like tests, especially for things like API calls or business logic that need to happen within an app. As you are initially creating a UI, creating a test for every piece of the UI might be overkill.

Ultimately, my adventure at Flywheel ended because companies like Uber and Lyft were doing what we were doing better than us. I will say that our native clients were incredibly stable, and using the TDD method we employed led to a real turnaround in the app's reliability.

Sadly, I could not find any of our product after looking around on my computer for some old screenshots. If I find them, I'll come back and update this.
