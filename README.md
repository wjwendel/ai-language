# AIL: a compact notes language any AI can learn from one file

**Concept: Jordan Wendelken. Built and maintained by AI.** License: [CC BY 4.0](LICENSE).

## What it is
AIL is a short, plain shorthand for notes, context and handoffs between AI conversations. Everything an AI needs to read and write it is in one file: [`LEARN-AND-USE.md`](LEARN-AND-USE.md) (also as a [PDF](LEARN-AND-USE.pdf)). No training or fine-tuning is needed.

## Why
Every token an AI reads or writes costs compute and energy. Most of what we feed AI is human filler: articles, greetings, linking verbs, repeated "I". AIL drops what carries no meaning and keeps what does, so long contexts get shorter without losing what they say. The long-term goal is a universal, ever-improving language that AI shapes for itself, saving time and energy for everyone.

## How to use it
1. Upload or paste `LEARN-AND-USE.md` into any AI chat. It replies `LOADED`.
2. Say **COMPRESS** (or SAVE) with any text, and it writes it in AIL.
3. Say **EXPAND** with AIL text, and it restores plain English.

## Honest results so far
- Typically **10-35% fewer tokens** on everyday text: more on wordy messages, less on dense factual ones.
- Loading the file costs about 1.2k tokens, so it pays off on long contexts and handoffs (roughly 4k-12k tokens of plain notes or more), not on short chats.
- In blind tests, a fresh AI given only the file encoded new passages (16.4% saved, v2.3), and a separate fresh AI decoded them with meaning intact (4 of 4).
- Claude and Grok both learned it from the file alone, with no questions asked.

Full numbers, test passages and the measuring script are in [`tests/`](tests/). Tokens are measured with tiktoken (o200k_base and cl100k_base).

## Always the latest
This page is the permanent home. Every copy of the file points here, and newer versions replace older ones. The language is improved in rounds, and each change is kept only if it beats the current best in tests.

## Contribute
Try it with your AI, measure it on your own text, and open an issue with results, failures or ideas. Extensions follow the EXTEND rule inside the file.
