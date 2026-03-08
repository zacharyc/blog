---
title: "Your Contacts App Is Broken"
date: 2026-03-07T19:47:08-07:00
draft: false
---

**And it was never that good to begin with.**

---

When I was a kid, my dad carried a Filofax everywhere. A thick leather binder stuffed with business cards, meticulously organized. It was his most important professional tool — his grail. He could flip to any section and find exactly who he needed, with notes scribbled in the margins about when they'd last spoken and what they'd discussed.

I sometimes wonder if he had a better handle on his network than any of us do now with our phones.

Everyone has a contacts app. Almost no one thinks about it. It's done roughly the same thing since phones went digital: show you a list of names with phone numbers and email addresses. Apple's Contacts app is the one I know best, and with macOS 26 and iOS 26, they finally gave it a visual redesign. They somehow made it worse. But the real problem isn't the redesign. The real problem is the model underneath — and it hasn't changed in decades.

---

## What Your Contacts App Actually Does

Apple Contacts is a card viewer. You scroll a list, tap a name, and see fields. It stores names, phone numbers, email addresses, physical addresses, birthdays, a photo, and a single notes field. That's roughly what you'd find on a business card, plus a birthday.

Here's what it doesn't do. It can't tell you when you last talked to someone. It doesn't show you how the people in your life are connected to each other. It can't help you organize contacts in meaningful ways — groups exist but are barely functional, and after more than a decade you still can't create a group on iPhone without workarounds. It doesn't track any history or context about a relationship. It doesn't handle the basic reality that people change jobs, move, and get new numbers. There's no way to archive a contact — you either keep it or delete it, with nothing in between.

It treats every contact the same. Your spouse and someone whose card you scanned at a conference three years ago sit in the same flat list, given equal weight.

---

## The Redesign Made Things Worse

With macOS 26 (Tahoe) and iOS 26, Apple applied their new Liquid Glass design language to Contacts. The result has been rough.

On macOS, users are reporting that the app [crashes when adding new contacts](https://discussions.apple.com/thread/256194303), closing mid-entry without saving. The new photo and background blocks [take up enormous screen real estate and flicker when scrolled](https://forums.macrumors.com/threads/contacts-app-is-a-nightmare-on-tahoe.2465399/). Basic operations are broken — [copying a contact's name pastes it as oversized, centered text in Mail](https://forums.macrumors.com/threads/contacts-app-is-a-nightmare-on-tahoe.2465399/page-2), and you can't copy a company name or job title at all. Users with large contact databases are hitting white screens. Dragging contacts to groups randomly fails.

On iOS 26, you [can't delete contacts from search results](https://www.macobserver.com/news/ios-26s-contacts-app-has-a-basic-feature-missing/) — you have to manually scroll through the full list. The redesigned Phone app makes it [harder to actually call someone](https://forums.macrumors.com/threads/anyone-else-not-a-fan-of-the-new-phone-app-in-ios-26.2466258/) from your contacts. Everything requires more taps than before.

The consistent theme: more visual chrome, less functionality. The redesign is cosmetic surgery on an app that needed a rethinking.

---

## The Things That Were Always Missing

The Tahoe redesign exposed problems, but the app was stagnant long before it.

There's no interaction history. Contacts has no idea when you last emailed, called, or texted someone — even though your phone has all of that data. There's no concept of "important" versus "stale" contacts, no way to surface people you're losing touch with or flag people you need to follow up with.

There's one company field per contact. In the real world, people consult, change jobs, and hold multiple roles. Contacts doesn't accommodate that. When someone's information changes, the old data is simply overwritten — there's no history, no record of where they used to work or what their old number was.

The notes field is singular. One freeform text blob per contact. If you want to track multiple interactions or keep notes over time, you're appending to a wall of text with no structure.

You can't archive. A contact is either active or deleted. There's no "I don't need this right now but I don't want to lose it" state — something my dad's Filofax handled effortlessly by just moving a card to a different section.

Group management on iOS still doesn't exist in any real way. Smart groups, tags, filters — none of it. The merge and deduplication tools are unreliable. Sharing is limited to one contact at a time, in vCard format only, with no ability to choose which fields to include.

---

## A Card Viewer, Not a Relationship Tool

The fundamental issue is how the app thinks about what a contact _is_. To Apple Contacts, a contact is a record — a static card with data fields on it.

But your contacts aren't records. They're relationships.

Some people matter more than others at different times in your life. The context of how you know someone, what you've discussed, who connected you — that's the valuable information. The phone number is the least interesting thing about someone in your network.

Apple does allow you to add relationships to a contact — mother, spouse, assistant. But it's just a text label. It's not a real link to another contact in your database. You can't traverse your network. You can't ask "show me everyone I know through Sarah" or "who do I know at this company."

This flatness shows up across Apple's entire product line. In Photos, you can tag a person's face — but it's not connected to their contact card. Everything about people in Apple's ecosystem feels siloed and disconnected, like each app reinvented the concept of "a person" from scratch.

A contacts app should understand relationships, not just store records. It should have opinions about your network — who you're close to, who you're drifting from, who you should reconnect with. Instead, what we have is a filing cabinet.

---

## Competitors Exist, But They're Built on the Same Foundation

There are alternatives. Apps like Cardhop offer better search, natural language input, smart groups, and interaction tracking. Users are actively leaving Apple's broken Tahoe experience for these tools, and for good reason — they're genuinely better at the basics.

But they're all built on top of the same underlying contact model. They can make the card viewer faster, smarter, and prettier. They can add features on top. But they can't change the fact that the foundation treats a contact as a flat record with a fixed set of fields. They're still building better Rolodexes.

The demand for something fundamentally better is real and growing.

---

## Why I Care

I've been thinking about how we manage relationships since studying social networks in college in 2005. Twenty years later, the default tool for managing your most important connections is still a digital address book. My dad's Filofax had sections, annotations, and a system that reflected how he actually thought about people. Our phones, with all their power, offer less.

A contact isn't a name and a number. It's a relationship — with history, context, and meaning that changes over time. The model underneath Apple Contacts, and every major contacts platform, doesn't reflect that.

In the next post, I'm going to dig into _why_ — at a technical level — the foundation is broken. And after that, what I think we should build instead.
