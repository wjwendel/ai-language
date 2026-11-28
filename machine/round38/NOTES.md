# Round 38 notes (2026-11-28)
## Holes found
- MNC28 main: a list qualifier written in parentheses after an "A + B + C" list was read as applying to the whole list (2/2 readers, 2/2 decoders). Original: clappers and flashlights for everyone; vests only for those who applied by Dec 20. The frozen rules allow this layout, so it can recur. A fix needs a rule change (e.g. "a qualifier that limits one item goes on that item's own line or right before it; never in parentheses after a list"), which would restart the counter.
- MNC28x ("terse + safety rails"): perfectly faithful (60/60 ×2, 224/224 decode ×2) but only 24.2% o200k vs terse 39.9%. The encoder kept too much wording (full sentences, glosses, Japanese terms in both scripts). The rails themselves cost little; the verbosity is the problem.
- LLMLingua-2 drops most CJK content at both rates.
- 7B prompt with the full original overflows the 7B setup (r37 original runs invalid).
## Next-round fix list
1. **x savings:** build x by taking terse English (written by the encoder) and adding only the rails: actors on triggers, explicit one-noun scope on its own line, exact should/may/must, THE/NOT THE roles. No glosses, no double scripts, no restated headers. Target: at least terse's savings with a clean decode.
2. **Main:** decide whether to promote MNC29 = MNC28 + a one-item-qualifier rule (put the limited item on its own line). Promotion restarts the counter at 0, but the counter is already 0 after this fail.
3. Keep 55-60 questions, the one-noun scope test, the "should" test and the actor-on-trigger tests.
4. Round 39 fully blind (rotate e.g. en / ko / it / ar).
5. Score r38 7B (answers_7b/keep); 7B: shorten the original prompt or raise ctx so the original baseline is valid; bench-v1 on main and x still pending.
