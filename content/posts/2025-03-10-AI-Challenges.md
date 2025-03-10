---
title: "AI Challenges"
date: 2025-03-10T12:42:13-04:00
draft: false
tags: ["AI", "Programming"]
cover:
  image: "/assets/img/2025/03/zack-abstract.jpeg"
  alt: "An AI generated headshot from 2022."
  caption: ""
  relative: false
---

I have a running conversation with my friend Scott about how good modern generative LLMs are at solving problems. What roles will they replace? Will we be out of work in the next couple of years?

It is true; Copilot is a must-have in VSCode. It often saves time when writing repetitive code in commonly used programming languages. When I want to know some piece of information, better and quicker results can be had by asking an LLM than searching and reading through all the ad-dense articles on the internet.

The argument is that AI is currently solving a different problem than what humans solve. The internet is not new. The information for solving most of your coding problems has been available if you know where to look. And if it isn't readily available on the internet, the AI can't do the deep reasoning of linking obscure topics together. That's just not what it is made for. Instead of using Let Me Google That For You, you can now send people a response from ChatGPT.

In the process of trying to understand the competitive advantage of [Gluino](https://gluino.io), I asked an Agent the simple question: "Where does AI let users down?" The response was interesting enough that it is worth an entire post.

## Factual Inaccuracies and Hallucinations

> AI models sometimes generate information that sounds plausible but is factually incorrect or entirely made up—a phenomenon often referred to as “hallucination.” This can be problematic when users rely on the AI for accurate, reliable information.

_From ChatGPT_

The issue is that these LLMs are only as strong as their training data. Many modern LLMs take years to train, and so oftentimes, the most recent data that is being used in the LLM is several years old. Other times, the of older events may be harder to find. [Here](https://onefoottsunami.com/2025/01/23/not-so-super-apple/) is an article about how wrong Siri is about Super Bowl winners.

The real issue is the same thing I've been complaining about for years with AIs. While their level of accuracy is continually improving, their certainty in their results is unwavering. AI comes back very confident about its answers, even if they might be wrong. This is not a new problem. [This](https://youtu.be/yJD1Iwy5lUY?si=TBXaB17QhjQXxBQj) YouTube video is a parody of a guy acting like Google. One person asks, "Vaccines cause autism." Google shows a bunch of evidence disproving it, the user changes the prompt "vaccines cause autism true," and Google can return one result, which leads the person to say, "I knew it." This is confirmation bias, and very common in human behavior.

The more significant problem could be that if users learn information from AI and treat it as fact without researching the truth, falsities could spread more quickly. The repercussions of these inaccuracies could be significant over time.

### Context and Nuance

> While AI can handle many straightforward tasks, it may struggle with understanding complex contexts, subtle nuances, or ambiguous queries. For example, in conversations involving irony, sarcasm, or cultural references, the AI might misinterpret the intent, leading to inappropriate or off-target responses.

Context is perhaps the most important part of any situation. While this is something that we learn throughout our life, this is something that is very challenging for computers. The context in which a question is asked matters. Asking an AI a question is asking it in the context of the training data provided.

The example I've used here is the recommendation letter for one of my former students for a job. I have the context of knowing the person and having worked with them in the past. The AI hasn't. The letter I got out of ChatGPT was written with passion but without any details or context on our interactions in the past. Some of this can be mitigated by improving your prompt. Prompt Engineering is an entire science at this point. Still, the response is only as good as the context you give it, and many AIs will have a limitation on the number of tokens they can take in as context. Sometimes, even when more context is provided the response is still off.

### Handling Ambiguity

> When faced with vague or ambiguous questions, AI might provide answers that are too generic or miss the user's intended meaning. This can be frustrating, especially if the query requires deep insight or specialized knowledge.

This is similar to lack of context. Ambiguity can often be resolved by having more context. The abilility to decode what is meant by a question, or ask for clarification appropriatly is something that AI is still working on. As context improves, I guess ambiguity will also become less of a concern.

### Bias and Representation

> AI models are trained on large datasets from the internet, which can include biased or unbalanced perspectives. As a result, the outputs might inadvertently reflect or amplify these biases, potentially leading to skewed or unfair responses.

Because of the nature of the training data set, AI can only know areas where it has been trained. It is only as good as the data you provide it. It cannot empathize, interpret, and extract. These are skills that allow humans to relate to one another.

Again, this boils down to context for me. If you take, for example, accounts from enslaved people during the period before the Civil War, the amount of context we have is limited because of the systemic barriers to literacy provided to those who were enslaved. The documents of the time will present the world in a way that is more representative of those who had more unrestricted access.

### Lack of Explainability

> Many AI models operate as “black boxes,” meaning they do not provide transparent reasoning behind their responses. Users who need to understand how a decision was reached may find this lack of explainability limiting, especially in critical applications like healthcare or legal advice.

Like reading a random page on the Internet without looking at the source, AI can produce information that is perceived as valid and accurate. However, the lack of proof associated with AI responses can lead to distrust.

### Limited Real-Time Understanding

> AI systems often rely on data that isn’t updated in real time. This means they might not be aware of the most recent events or developments, leading to outdated information in fast-changing fields.

This combines the first two issues: factual inaccuracies and a lack of context. It concerns training data. A model uses data that is captured and trained. Data created after the capture is unused and unavailable to the model.

### Overreliance on Patterns

> AI is excellent at detecting and mimicking patterns in data, but it can struggle with genuinely novel or creative problem-solving that falls outside the patterns it has learned. This can result in responses that are formulaic or less innovative when a truly new perspective is needed.

In asking for further clarification here, ChatGPT says:

> It **struggles with unique, unexpected, or illogical situations** because it tries to apply familiar structures.

The example I liked the most is: If you asked AI to complete the pattern 2, 4, 8, 16, 31, it might respond with 62 as the following number in the sequence. The issue is that 31 breaks the sequence, and humans will often ask what is going on, while AI will follow the doubling pattern.

### Ethical and Privacy Concerns

> In some cases, the ways AI handles data can raise ethical or privacy issues. For instance, when generating content based on personal data or sensitive topics, the AI might inadvertently produce content that users find invasive or ethically questionable.

However, morality is a complex process that needs to be taught to computers.

## Conclusion

Many of these issues overlap and impact one another. The fundamental design of modern Generative AIs leads to many of these issues, but none diminishes the product's usefulness.

The most striking area of AI is to give you a starting point. Starting with a premise and using AI to start you down a path, even if it is wrong, at least gets you moving. You can realize that the information it's giving you is not what you need, but then, voila, you now know what you need, and it has gotten the ball rolling.

Tools like [Gluino](https://gluino.io) aim to solve some of the problems inherent in these tools. As the Technology space develops, I'm sure even more will help with these challenges.

While AI is fabulous and does help with many knowledge worker tasks, AI by itself is not enough to replace the creativity and intelligence of the workforce. It can be helpful as a tool but still requires operators and people to check its work. I disagree with my friend Scott, who says AI might put us out of a job. AI will likely augment our jobs, just as other tools like Google and Stack Overflow helped engineers in the past.
