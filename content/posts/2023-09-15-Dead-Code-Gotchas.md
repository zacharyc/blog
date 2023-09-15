---
title: "Dead Code Gotchas"
date: 2023-09-15T10:25:48-04:00
draft: false
---

I'm in the stage of my career where I've seen a lot of projects from other developers. I've inherited good code and bad code, and there a couple of big gotchas I've been wanting to talk about.

## Comments

### Function Heading Comments

When I was in college, I used to write three line comments for everything

```c
    //------------------------------
    // This Function Squares Pi
    //------------------------------
    float square_pi() {
        ...
    }
```

While this comment isn't wrong, it is unnecessary. The function name `square_pi` says what it does. Putting in the comment adds more lines to the file without providing any real use. Yes, the compiler will remove it so it doesn't hurt the running code, but it is repeating what is written below and the function name should be good enough.

Comments for the sake of writing more lines of code or making your **layout** look a little cleaner is not a great thing. It actually makes your code harder to read because poeple have to scroll to see to get past it. It means developers can see less on screen. Remove them, they aren't helping.

### To Do Comments

Sometimes you are writing code quickly and want to make sure to come back to something. You will leave a note in the comment like:

```c
    if (error != null) {
        // Do something here to record an error
    }
```

I get it. Sometimes there are bigger fish to fry and you need to come back to this comment later and fix it. The problem with the above is that it is easy to miss the fact that you need to come back to it. The trick is to add a common line that is shared across your codebase, something like `// TODO:` to track what changes need to be made later. I personally use `// TODOz:` because it has my name so I know that is a thing I wrote and need to come back to, but is still searchable with "// TODO" when someone is looking through the code base.

### Commented Out Code

STOP SHIPPING COMMENTED OUT CODE!

If you need to comment out a piece of code for a day or two, make sure it is in a branch. Learn to use your version control system more effectively if you need to go abck and find code that was there before. Most of us can learn to use Git or whichever tool we have been using more effectively, but dead code in a master branch is something poeple need to scroll through and is not worth it. Remove it and then find it in your history if you need it again.

## Variable &amp; Function Naming

Unless names are very long and the abbriviation is commonly known, avoid reducing the size of a variable name in code. The clearer the variables are named the easier you code will be to read. Naming somthing `intr` might save you a couple of keys of typing, but it is unclear what `intr` means, "internal"? "inter office"? "int for real"? Typing out the extra characters in the world and definin what the variable means will make it much more readable to others. Any good compiler will clean up your code so the name length won't matter to the code execution, only to the developers reading it. Aim to write clear code.

## End

There are ton of other things that drive me nuts as I'm going through others code, and I'll write about them as I see them. I just wanted to get these off the page before forget them.
