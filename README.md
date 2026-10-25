# AIL: Less Energy for Every AI Conversation

**One file teaches any AI a leaner language. No training, no setup. Upload it and the AI starts using it.**

*Concept: Jordan Wendelken. Built and maintained by AI. Free and open under [CC BY 4.0](LICENSE).*

---

## The problem
Every word an AI reads or writes is turned into tokens, and every token costs electricity. On every turn, an AI re-reads the whole conversation. Much of that text is human filler that carries no meaning for a machine: articles, greetings, linking verbs, polite padding. Across billions of conversations a day, that filler adds up to a real energy bill for the planet.

## The idea
**AIL (AI Language)** is shorthand built *for* AI, *by* AI. It keeps every fact and drops the filler, so the same meaning costs fewer tokens.

## Why it matters

### 1. Energy first
Fewer tokens means less computing per turn and less electricity per conversation. Small savings on a single chat become very large savings at the scale AI runs today. That is the main reason AIL exists.

### 2. Faster results
A shorter context is quicker for a model to read and answer from. Long projects, notes and handoffs between AIs fit in less space and move faster.

### 3. It learns in one read
There is no fine-tuning, plugin or code. Claude and Grok each learned AIL from the file alone, with no questions asked, and started using it on the next message.

### 4. Built to keep getting leaner
AIL is a living language that AI keeps refining, and the process already works. Across five tested versions, each round found real failures in blind and real-world tests (Claude, Grok) and fixed them, until a fresh AI decoded every test passage with the meaning intact. A change is kept only if it beats the current best. The aim is a language that, over time, needs fewer tokens for the same meaning, on more kinds of text. Because this page is the one permanent home every copy points to, an improvement made here reaches everyone who uses it.

## Try it in 30 seconds
1. Upload or paste [`LEARN-AND-USE.md`](LEARN-AND-USE.md) (or the [PDF](LEARN-AND-USE.pdf)) into any AI chat. It replies **LOADED**.
2. Say **COMPRESS** with any text, and it writes it in AIL.
3. Say **EXPAND** with AIL text, and you get plain English back.

**Example**
> Plain: *My car is in the shop until Thursday, so I can't drive the kids to practice on Tuesday. Can you take them? If not, I'll ask Lisa. I also need milk and bread.*
>
> AIL: `my car in shop until Thursday > can't drive kids to practice Tuesday / can you take them? / if not, I'll ask Lisa / need milk, bread`
>
> 39 tokens down to 31 (o200k), with every fact kept.

## Honest results so far
- **Typically 10-35% fewer tokens** on everyday text: more on wordy messages, less on dense factual ones.
- **Meaning is kept.** In blind tests, a fresh AI given only the file encoded new passages (16.4% fewer tokens, v2.3), and a separate fresh AI decoded them with the meaning intact, 4 out of 4.
- **Best for long work.** Loading the file costs about 1.2k tokens, so it pays off on long contexts, memory and AI-to-AI handoffs (roughly 4k-12k tokens of notes or more), not on one-line chats.

These are early, small tests, and every number, passage and the measuring script is published in [`tests/`](tests/). Tokens are measured with tiktoken (o200k_base and cl100k_base).

## Help make it leaner
Try it with your AI, measure it on your own text, and open an issue with results, failures or ideas. Extensions follow the EXTEND rule inside the file. The best improvements become the next version, for everyone.
