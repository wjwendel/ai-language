# Round 40 notes (2026-11-28)
## What happened
- MNC28 main (frozen): clean blind pass (59/59 ×2, decode 194/194 ×2). Counter MNC28 2/3.
- MNC28x-R40: the two new rails (titles/scope nouns in everyday sections; Latin transliteration for non-Latin names) worked for faithfulness: 100% ×2 and 0 S decode errors, only the §2 addressee lost. But savings fell to 33.4% o200k (r39: 40.0%), under terse English (38.9%). The encoder said the cost came mostly from keeping names in both scripts and the who-is-who boilerplate.
- Baselines: summarize turned a "should" into required and widened an exception; LLMLingua-2 lost Chinese facts and the Friday-only scope.
## Next-round fix list
1. **x cost cuts:** names in Latin transliteration only, with the original script only where the original's script is itself tested (e.g. a quoted sentence); one shared who-is-who line per section without repeated "THE"/"NOT THE" where the original has no contrast; write the terse layer the way the terse writer does (it beat x by ~180 tokens). Target: x ≤ terse tokens with 0 S decode errors.
2. **x everyday sections:** keep the notice's addressee (cheap, 2-3 tokens).
3. Main: keep MNC28 frozen (counter 2/3; the next clean blind round makes 3/3).
4. Round 41 fully blind (rotate e.g. en / ja / fr / sw), 55-60 q, keep the should-test, "the vs a", one-item qualifier, title and scope tests.
5. Score r40 7B (answers_7b/keep) when the queue finishes; bench-v1 on main and x still pending.
