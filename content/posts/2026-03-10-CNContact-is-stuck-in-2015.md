---
title: "CNContact Is Stuck in 2015"
date: 2026-03-10T11:15:55-06:00
draft: false
tags: ["contacts", "apple", "programming", "projects"]
---

**Apple's contact framework doesn't understand how we actually connect.**

---

In my [previous post]({{< relref "2026-03-07-Your-Contacts-App-Is-Broken.md" >}}), I wrote about how Apple's Contacts app treats your relationships like a filing cabinet — a flat list of static cards with no context, no history, and no awareness of how people actually matter to you. That's a product problem. But it's also a technical one.

Underneath the Contacts app sits a framework called `CNContact`, introduced at WWDC 2015 as a replacement for the widely despised `AddressBook.framework`. AddressBook was a C-based API with no Objective-C layer, opaque types like `ABRecordRef`, and virtually no error handling. When Apple announced its deprecation, the WWDC audience cheered — one of the loudest reactions in the conference's history.

`CNContact` was a genuine improvement. Type-safe. Thread-safe immutable objects. A `keysToFetch` system that lets you load only the properties you need. It's a well-engineered API for an outdated model. Because while the engineering got better, the underlying concept of what a contact _is_ didn't change at all. A person is still a card with fields on it. Name, phone number, email, address.

It's 2026 and that model is broken.

---

## What CNContact Actually Is

`CNContact` is an immutable object representing a single contact record. You access the database through `CNContactStore`, and when you fetch contacts, you specify which properties you want via `keysToFetch` — conceptually similar to a SQL `SELECT` where you name your columns.

A contact has string properties for names (`givenName`, `familyName`, `middleName`), and multi-value properties for phone numbers, email addresses, and postal addresses. Those multi-value fields use `CNLabeledValue` — an immutable tuple pairing a label (like "home" or "work") with a value (like the phone number itself). Modification goes through `CNMutableContact`, a mutable subclass. A `CNContactType` enum distinguishes between people and organizations, though the distinction is thin — the same flat field structure applies to both.

The engineering is competent. The problem is what the engineering models.

---

## A Contact Is Not a Business Card

`CNContact` knows a person's name, phone numbers, email addresses, physical addresses, birthday, organization, and social profiles. That's what you'd find on a business card, plus a birthday.

It doesn't know when you last spoke to this person, how you met them, who introduced you, or what your relationship actually is. It can't tell you whether someone is important to you right now or someone you haven't spoken to in three years. It doesn't understand any connection between this person and your other contacts. There's no concept of interaction history, relationship strength, or the social graph between the people in your life.

`CNContact` models a person as a _record_. It does not model a _relationship_. In 2026, the relationship is the valuable part. The phone number is the least interesting thing about someone in your network — what you can't easily recover is _context_.

The model doesn't even work well for its most basic use case. There's a single `organizationName` field — one company per contact. People consult, freelance, change jobs, hold board seats. `CNContact` can't represent any of that. It's not a model of a person or a business. It's a model of one person at one company at one point in time.

Apple does expose a `contactRelations` field — you can label someone as a spouse, parent, or assistant. But it's a string label, not a link. It doesn't point to another `CNContact`. You can't traverse your network. You can't ask "show me everyone connected to Sarah." The relationships, like everything else in this framework, are flat text on a card.

The notes field is singular — one freeform text blob per contact. If you want to track conversations over time, or keep structured notes about multiple interactions, you're appending to a wall of unstructured text. No timestamps, no separation, no history.

There is no concept of archiving. A contact exists or it's deleted. There's no "inactive" state, no way to move someone to the back of the drawer without losing them entirely.

---

## The Identifier Problem

Every `CNContact` has an `identifier` property — a string that should uniquely identify the contact. The natural instinct is to use this as a foreign key, linking your app's data to a specific person.

That instinct will hurt you.

The identifier is local to the device. The same human being on your iPhone and your iPad will have different identifiers. The identifier isn't stable across backup and restore cycles. Developers on Apple's own forums have reported that the _same contact_ accessed through different code paths on the _same device_ returns different identifiers — share a contact from Contacts.app and you get one with an `:ABPerson` suffix, select it via `CNContactPickerViewController` and you get a different one without it.

Apple can correlate contacts across devices because they control iCloud and the sync engine beneath the framework. Third-party developers cannot. The workaround is rolling your own matching logic — normalized phone numbers, email addresses, name combinations — essentially rebuilding deduplication from scratch.

If you want to build anything that tracks a contact over time — notes, interaction history, relationship metadata — you can't reliably key it to a `CNContact`. The identifier that's supposed to be your anchor is quicksand.

---

## The Frozen Schema

So the identifier is unreliable. Could you at least store your additional data _on_ the contact itself?

No.

`CNContact` has a fixed set of properties. No custom fields, no metadata dictionary, no extension points. The schema is what Apple decided a contact needed in 2015, and it hasn't meaningfully expanded since. "Last contacted," "relationship strength," "met at WWDC 2024" — anything not on Apple's predetermined list requires your own data store.

That data store needs a key to link back to the contact, which brings you directly back to the identifier problem. You're building on a foundation that shifts under your feet.

Even the simplest CRM systems offer custom fields, tags, activity timelines, and relationship types. `CNContact` isn't missing features — it's missing the _concept_ that a contact might mean something different to different people and different apps.

---

## Your Data Lives on Apple's Terms

I'll save the full portability deep-dive for a future post, but the short version: getting your contacts _out_ of Apple's ecosystem is harder than it should be.

The only native export format is vCard. No CSV, no JSON, no bulk API. On iOS, you can share one contact at a time. Export is all-or-nothing per contact — you can't select which fields to include. Import vCards back in and you'll likely create duplicates, because the "unified contact" system that deduplicates on-device doesn't survive a round trip.

Your contacts flow into Apple's ecosystem with minimal friction. Getting them out requires workarounds and third-party tools. This asymmetry is not accidental.

---

## Built for a World That Doesn't Exist Anymore

The `keysToFetch` system is well-designed. The immutable/mutable pattern is sound. `CNLabeledValue` is a good abstraction for multi-value properties. Apple's engineers built a competent framework.

They built it to digitize the Rolodex, and they succeeded. `CNContact` is an excellent digital Rolodex card.

The problem is that we don't live in a Rolodex world. Our relationships are contextual, dynamic, and cross-platform. A contact isn't a card with a name and number — it's a node in a network, with history, context, and meaning that changes over time. `CNContact` doesn't model any of that. Its closed schema means you can't teach it to.

It's a 2015 solution to a 1985 problem, and it's the foundation that every app on Apple's platforms is expected to build on when it wants to work with the people in your life.

---

## What's Next

I've spent enough time studying this framework to understand that patching it isn't the answer.

The problems compound. There's no stable identifier, so you can't reliably extend a contact with your own data. There's no extensible schema, so you can't store that data on the contact itself. And there's no universal key to map against — some contacts are unique by phone number, some by email, some by name and company, some by something else entirely. Every contact is a special case.

You could try to build a mapping layer on top of `CNContact`. Normalize phone numbers, deduplicate emails, fuzzy-match names. But you'd be building an increasingly fragile bridge between your data and a foundation that was never designed to support it. At some point, the cost of maintaining that bridge exceeds the cost of building something new.

The model needs to change. Not the UI on top of it, not the permissions around it, not the visual design — the model itself. What a contact is. How identity works. How relationships are represented. How your data moves between devices and platforms.

I'm working on that. More soon.
