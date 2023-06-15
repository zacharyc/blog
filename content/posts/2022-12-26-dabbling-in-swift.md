---
id: 2692
title: "Dabbling in Swift"
date: "2022-12-26T01:33:04-05:00"
author: zacharyc
layout: post
guid: "https://zacharyc.com/?p=2692"
permalink: /2022/12/26/dabbling-in-swift/
image: /wp-content/uploads/2022/12/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcHgxMTY5OTI0LWltYWdlLWt3dnc3cmlhLmpwZw-740x430.jpg
categories:
  - Programming
---

For many years of my life I was an iOS Programmer. I worked in Objective-C, but Swift came out while I was working transitioning out of that area. Swift has always been a bit confusing for me, but I have a new complaint today. The amount of changes in Swift has caused a lot of online code to be out of date, and hard to parse.

The problem. I’m looking at my address book and I want to iterate through my contacts. I started by looking at `ABAddressBook`, but it turns out that technology has been depricated. Then I started looking at `CNContactStore` which is the new hotness. There are several fun methods on that object including `unifiedMeContactWithKeys` which is pretty cool. It only returns my contact, not all contacts, but at least I was able to get it work. There is a similar function called

```swift
func unifiedContacts(matching predicate: NSPredicate, keysToFetch keys: [CNKeyDescriptor]) throws -> [CNContact]
```

You try to pass in the truthy predicate and it rejects it. You need to actually use the

`enumerateContacts()` method. Some examples mix strings and other types with keys and that causes problems. Just using a list of Keys worked. Here is the final code that worked:

```swift
//
//  main.swift
//  contactsexport
//
//  Created by Zachary Cohen on 12/23/22.
//

import Foundation
import AddressBook
import Contacts

print("Hello, welcome to the AddressBook Scraper")


var store = CNContactStore()

store.requestAccess(for: .contacts, completionHandler: { (access, accessError) -> Void in
    if access {
        print("access granted")
        print(access)
    }
    else {
        print("access denied")
    }
})


let nameKeys = [
    CNContactNamePrefixKey,
    CNContactGivenNameKey,
    CNContactMiddleNameKey,
    CNContactFamilyNameKey,
    CNContactNameSuffixKey,
    ] as [CNKeyDescriptor]

let allContactKeys = [
    CNContactNamePrefixKey,
    CNContactGivenNameKey,
    CNContactMiddleNameKey,
    CNContactFamilyNameKey,
    CNContactNameSuffixKey,
    CNContactOrganizationNameKey,
    CNContactDepartmentNameKey,
    CNContactJobTitleKey,
    CNContactBirthdayKey,
    CNContactNicknameKey,
    CNContactNoteKey,
    CNContactNonGregorianBirthdayKey,
    CNContactPreviousFamilyNameKey,
    CNContactPhoneticGivenNameKey,
    CNContactPhoneticMiddleNameKey,
    CNContactPhoneticFamilyNameKey,
    CNContactImageDataKey,
    CNContactThumbnailImageDataKey,
    CNContactImageDataAvailableKey,
    CNContactTypeKey,
    CNContactPhoneNumbersKey,
    CNContactEmailAddressesKey,
    CNContactPostalAddressesKey,
    CNContactDatesKey,
    CNContactUrlAddressesKey,
    CNContactRelationsKey,
    CNContactSocialProfilesKey,
    CNContactInstantMessageAddressesKey,
    ] as [CNKeyDescriptor]

do {
    let contactStore = CNContactStore()
    let me = try contactStore.unifiedMeContactWithKeys(toFetch: nameKeys)
} catch let error {
    print("Failed to retreive Me contact: \(error)")
}

do {
    let contactStore = CNContactStore()
    let fetchRequest = CNContactFetchRequest(keysToFetch: allContactKeys)
    try contactStore.enumerateContacts(with: fetchRequest) { con, response in
        print(con);
    }
} catch let error {
    print("Failed to retreive Me contact: \(error)")
}
```

I’m still working on the project and there is bunch more to do this, but this is a start and figured it was worth putting out there.
