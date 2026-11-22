# Round 13 NOTES (MNC17 / MNC17x / MNC17xx)

## What changed
- r12 fixes applied: facts.json before encoding; deadline words kept; speaker names; neutral section tag (`§N you` / `§N`, no language code); fact-by-fact check before freezing (it caught a missing announcer "council" and a dropped reason "to keep schedule" before the freeze).
- Three savings points (39.1 / 45.3 / 46.9% o200k) instead of one, for the accuracy-vs-savings curve.
- New language rotation: en(+de questions) / ja / es / it / nl.

## Holes found
1. **The fresh questions are at ceiling for the strong reader.** Original, terse English and all three MNC17 versions scored 114/114. Direct use can no longer rank versions or find the breaking point. The blind decode is now the only test that found anything.
2. **Bare "subject: action" lines lose who acts.** `serious: they call 911` decoded as a statement, losing "you tell them". Keep the assistant's verb for anything the assistant must do or say: `serious: tell them call 911`.
3. **The fact check missed a dropped object noun.** `De Vries gets day's returns` lost "overview". The check must compare the object of every deadline/report line, not only the deadline and recipient.
4. **Savings are stuck below 50% on instruction-heavy text.** Instruction sections cost the most (§1 ~150 of 622 tokens). Each rule needs its trigger, actor, permission and exception. Merging the identity line with the owner rule saved ~10 tokens with no loss on direct use.
5. **LLMLingua-2 deletes unspaced Japanese entirely** (empty §2 at rate 0.5). Its headline 59.8% savings are inflated by that; the fair figure is 51.3% on the other four sections at 87.2% accuracy.

## Next-round fix list (baseline-won metrics first)
1. **Tokens: LLMLingua-2 0.5 still saves more** (51.3% excl. its empty §2, vs MNC17xx 45.1% on the same sections), but at 87.2% accuracy with safety failures. Go for ≥52% with an MNC18 that keeps the assistant's verbs: try dropping articles/possessives everywhere, shared defaults ("never X" lines grouped under one `never:` header per instruction section), and one-line news slots.
2. Fix holes 2-3: keep the assistant's action verb; check every report/deadline object noun before freezing.
3. **Harder questions (bench-v2, frozen):** longer passages (2-3× length), several interacting conditions per rule, exactly-N and date-boundary cases, and questions that need two rules combined. Without this, strong-reader direct use can't rank versions.
4. Build an MNC17-style bench-v1 encoding and run it ×1 as a regression check (required before any new-best claim).
5. 7B ×3 only as a detached job that is written up in the same run or explicitly marked pending.
