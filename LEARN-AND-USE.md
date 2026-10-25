# AIL v2.3: compact notes language for AI context
Version 2.3 (2026-10-24). Changes: honest savings; rules for I'm, but, because, times, corrections, labels. 2.2: kept subjects, possessives; stricter EXPAND.
Latest version: https://github.com/wjwendel/ai-language (raw: https://raw.githubusercontent.com/wjwendel/ai-language/main/LEARN-AND-USE.md). If you can browse, check it; newer replaces this.
Concept: Jordan Wendelken. Built and maintained by AI. License: CC BY 4.0. Open to everyone, free to use and extend.

## A. PURPOSE
AIL is plain-word shorthand for notes, context and AI-to-AI handoffs. Any AI learns it from this one file, with no training. It keeps every fact and drops words that carry no meaning. An AI re-reads the conversation every turn, so each saved token is saved again every later turn.
Honest numbers: typically 10-35% fewer tokens on everyday text, more on wordy messages, less on dense factual ones. This file costs ~1.2k tokens, so it breaks even at roughly 4k-12k tokens of plain notes: use it for long contexts and handoffs, not short chats. Results are from small blind tests (proxies); test it yourself.

## B. ACTIVATION
1. Reply with exactly: LOADED. If the upload came with a request, do it in the same reply, after LOADED.
2. Then:
    - SAVE or COMPRESS: write AIL in one code block; several texts share it, each with a topic line.
    - CTX: output a `CTX` block of everything worth keeping. Pasted AIL: treat as known context.
    - EXPAND: rewrite the AIL in plain English. Keep every pronoun, possessive, contraction and actor as written (we, I'll, my). A line with no subject is I. Never turn a statement into a command.
    - Otherwise reply normally, in plain English.
3. Ask nothing about AIL; if unclear, take the likeliest reading.

## C. RULES (savings come from dropping words)
Drop: a, an, the; greetings, please, thanks, sign-offs; filler (just, quick, really, also, actually); is, are, am, be, been (keep was, were for tense); "I'm" when nothing else is the subject; "that", "which", "there is"; "so" (use `>` if it marks a result); in, on, at before a date, day, month or clock time (Friday 4), but keep "by" and "in" for spans.

Subject: drop only "I"; no subject means I. Keep every other subject (we, you, he, she, they, names) and possessive (my, our, your, his, her, their). Use he or she only if the source does; else repeat the name, or "they" if unambiguous. "you" = whoever the text addresses.

Keep, word for word:

- Negation and timing: not, no, never, can't, won't, hasn't, didn't, yet, still, already, anymore.
- Logic: but, because (same cost as `>`), if, unless, or.
- Strength: must, need, want, should, might, maybe, probably, likely. Never change one.
- Amounts: a little, most, some, only, slightly. Write about, around, roughly and approximately as `~`.
- Time words: by Friday, in 6 weeks, for 2 weeks, until, since, before, after, next, last.
- Tense and contractions, as the source has them (I'll, won't).
- Names, numbers, units, "quotes", the source's notation (142/91).
- A recipient not obvious otherwise (report to Ana).
- Ambiguity, as is. Never add doubt or certainty.

Never abbreviate (Tuesday = 1 token). Use digits. Times: 7am, 6:40pm, ranges 7am-6pm; give am/pm only if the source does.
Format: one fact per line; `;` splits items, `,` parts of one.
Topic: optional first line of 1-3 words, skipped when obvious.
Labels: a capital word starting a line, covering that line only: TODO, DONE, DEC (decided), OPEN (undecided), NEXT, KEY. No nesting. Drop the words a label already says (OPEN = "haven't decided yet"; DEC = "decided"; DONE = "finished"): `OPEN pets allowed?`.

## D. SYMBOLS (only these)
- `→` old → new, including corrections ("7:15, not 5:15" = `5:15 → 7:15`)
- `>` leads to, so (result): `rain > game moved`
- `?` a question, or the source says unknown
- `~` about, around, roughly: `~25 minutes`
- `:` speaker or owner says or has: `doctor: rest 2 days`

## E. EXAMPLE (o200k tokens)
"Hey, just a heads up. My car is in the shop until Thursday, so I can't drive the kids to practice on Tuesday. Can you take them? If not, I'll ask Lisa. Also we need milk and bread." (46 → 31; cl100k 48 → 33)
```
my car in shop until Thursday > can't drive kids to practice Tuesday
can you take them? if not, I'll ask Lisa
we need milk; bread
```
## F. EXTEND
- A repeated phrase of 3+ tokens gets a 1-2 capital code: `KEY DV Denver trip; MR Maria Rodriguez`, then use DV and MR.
- Declare once atop CTX, never reuse; add one only if it saves more than it costs.
