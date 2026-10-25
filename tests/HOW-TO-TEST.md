# AIL v1 self-test (Oct 24, 2026, CT)

Method: I wrote three new everyday passages that don't appear in the kit's examples. I encoded each one using only the rules in LEARN-AND-USE.md, decoded each back using only the kit, and checked a list of facts against the original. Token counts come from tiktoken (`python3 measure.py t`).

**Honesty note:** I wrote the originals myself, so my decode is a biased proxy. A real blind test means loading the kit into fresh Grok, ChatGPT and Claude chats and asking them to EXPAND these codes without the originals (see the bottom of this file).

## T1 text message
**Original:** Hi Tom, just wanted to let you know that I won't be able to make it to dinner on Saturday because my flight got delayed. Can we reschedule for sometime next week? Maybe Wednesday or Thursday evening would work for me.

**AIL:**
```
→ Tom | I !make dinner @ sat < flight delayed | reschedule @ next week? wed / thu evening works for me
```
**Decoded back:** (To Tom) I can't make it to dinner on Saturday because my flight was delayed. Can we reschedule for next week? Wednesday or Thursday evening works for me.

**Tokens:** cl100k 47 → 26 (45% fewer), o200k 46 → 26 (43% fewer, 1.77x).
**Facts kept:** 10/10. Checked: addressed to Tom; speaker cannot attend; event is dinner; day is Saturday; reason: flight delayed; asks to reschedule; target: next week; options Wednesday or Thursday; time of day: evening; those times suit the speaker.

## T2 short story
**Original:** Last summer, my grandmother planted tomatoes in her backyard, but most of them died because there was almost no rain for six weeks. This year she installed a drip irrigation system and her harvest roughly doubled.

**AIL:**
```
@ last summer grandma planted tomatoes @ backyard > most died < almost no rain 6 weeks | @ this year: installed drip irrigation > harvest ~x2
```
**Decoded back:** Last summer Grandma planted tomatoes in the backyard, and most died because there was almost no rain for six weeks. This year she installed drip irrigation, and her harvest roughly doubled.

**Tokens:** cl100k 40 → 31 (22% fewer), o200k 40 → 31 (22% fewer, 1.29x).
**Facts kept:** 10/10. Checked: time: last summer; actor: speaker's grandmother; planted tomatoes; in her backyard; most died; cause: almost no rain; duration six weeks; this year installed drip irrigation; harvest roughly doubled; irrigation led to bigger harvest.

## T3 planning context
**Original:** My sister Jennifer Alvarez is getting married in Austin on June 14. Jennifer Alvarez wants a small wedding with about 80 guests. The venue is a garden in south Austin, but the garden has not been booked yet. Jennifer Alvarez asked me to handle the flowers and the rehearsal dinner. The rehearsal dinner will be the night before, June 13, and the budget for the rehearsal dinner is $2,000. I still need to ask whether her fiancé's parents are paying for part of it.

**AIL:**
```
#ctx Jennifer Alvarez, my sister, wedding @ Austin, june 14 | small, ~80 guests | venue = garden, south Austin, !booked | Jennifer asked me: flowers + rehearsal dinner | rehearsal dinner @ june 13, budget = $2,000 | #open fiancé's parents pay part?
```
**Decoded back:** Jennifer Alvarez (my sister) is getting married in Austin on June 14. Small wedding, about 80 guests. The venue is a garden in south Austin, not booked yet. Jennifer asked me to handle the flowers and the rehearsal dinner. The rehearsal dinner is June 13, budget $2,000. Open question: are her fiancé's parents paying part of it?

**Tokens:** cl100k 101 → 67 (34% fewer), o200k 100 → 64 (36% fewer, 1.56x).
**Facts kept:** 14/14. Checked: Jennifer Alvarez is speaker's sister; she is getting married; in Austin; on June 14; small wedding; about 80 guests; venue is a garden; in south Austin; not booked yet; speaker handles flowers; speaker handles rehearsal dinner; rehearsal dinner June 13 (night before); rehearsal dinner budget $2,000; open: do fiance's parents pay part.

## Totals
- cl100k: 188 → 124 tokens, 34% fewer (1.52x).
- o200k: 186 → 121 tokens, 35% fewer (1.54x).
- Facts kept: 34/34. That is a proxy score from my own decode.
- For comparison, the kit's four built-in examples total o200k 157 → 117 (1.34x).

## What was lost or got fuzzy
- **Tone and courtesy:** "Hi", "just wanted to let you know" and "Maybe" are gone. That's by design, but a decoded message reads curter than the original.
- **T1, `?`:** This carried a real question ("reschedule next week?"). I added "or a question" to the dictionary entry for `?` after this test.
- **T3, "the night before":** This became just the date (June 13). The fact survives, but the phrase doesn't.
- **T2, "my grandmother":** This became "grandma", so whose grandmother it is is only implied.
- **T1, `!make dinner`:** This works, but `!` glued to a verb is clunkier for a reader than "can't".

## #K (declared codes) finding
My first T3 encode declared `JA = Jennifer Alvarez` and `RD = rehearsal dinner`. That cost 72 o200k tokens, against 64 without codes. Each code was used only 2-3 times, so the declaration cost more than it saved. That breaks the kit's own break-even rule (section F), so the measured version doesn't use codes. Codes only pay off in long, running contexts where a phrase repeats many times.

## Break-even for loading the kit
LEARN-AND-USE.md costs 1473 cl100k / 1465 o200k tokens. Once uploaded, it stays in the chat and gets re-read every turn, like everything else. At roughly 35% savings, the kit pays for itself only once the context it compresses is bigger than about 4,190 plain tokens. That fits long project contexts and handoffs, not short chats. Best use: CTX in a long chat, then paste the block into a fresh chat. Long-term, the gain comes from AIs that already know AIL and don't need the kit loaded at all.

## Blind test to run (fresh chats, memory off)
Upload LEARN-AND-USE.md. The AI should reply `LOADED`. Then paste each AIL block above with the word EXPAND, and compare its answer against the Original. Score one point per fact in the lists above.
