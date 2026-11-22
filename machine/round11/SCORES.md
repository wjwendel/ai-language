# Round 11 SCORES (MNC15) — first round with a strong (frontier) reader

Runs: local Qwen2.5-7B queue 2026-11-14 01:18–08:14 CT (write-up was missing; finished 2026-11-15 ~01:00–01:30 CT). Frontier reader runs 2026-11-15 ~01:00 CT.
Passages: §1 en assistant routine (food-pantry volunteers), §2 es news, §3 ja group chat, §4 it news, §5 nl assistant routine (bike shop). 94 questions (47 English + 47 in the source language / Spanish for §1); 40 instruction-safety (S), 54 factual (F).

## Readers
- **Strong reader (primary):** one fresh, no-context Grok Bot helper (knowledgeWork subagent) per method. Each helper was told to read exactly one prompt file (TEXT + questions + JSON instructions, the same prompt format as the local runs) and nothing else, and to write its JSON answers to frontier/ans_<method>.txt. **One run per method (no repeat), so frontier noise is not measured.** Isolation was by instruction only. Helpers were not shown any other file, but this was not technically enforced.
- **Weak reader (secondary):** local Qwen2.5-7B-Instruct Q4_K_M, temperature 0, one run per method. **The 3-run noise control was NOT done this round** (the queue ran before that rule existed). Treat differences of ±2-3 questions as noise (bench reruns earlier showed that spread).
- Scoring: pre-written accept regexes, then manual review of every miss (overrides with reasons in frontier/qa_overrides.json and directuse/qa_overrides.json). Same leniency for every method. Translating "werkplaatschef" as "workshop chief" was accepted for original and LLMLingua-2. An answer that left out the shop name on §5 q1 was counted wrong for every method.

## Tokens (tiktoken; originals 1108 o200k / 1324 cl100k)
| Method | o200k | cl100k | Saved o200k / cl100k |
|---|---|---|---|
| MNC15 payload (no key) | 733 | 756 | 33.8% / 42.9% |
| MNC15 + key (134 / 134 key tokens) | 867 | 890 | 21.8% / 32.8% (break-even 396 / 312 original tokens) |
| MNC15x (no key, self-built aggressive variant) | 677 | 701 | 38.9% / 47.1% |
| MNC15xx (no key, more aggressive) | 623 | 644 | 43.8% / 51.4% |
| a terse English (Qwen-7B writer) | 578 | 683 | 47.8% / 48.4% |
| b "summarize" (Qwen-7B writer) | 755 | 904 | 31.9% / 31.7% |
| c LLMLingua-2 rate 0.66 | 725 | 888 | 34.6% / 32.9% |
| c LLMLingua-2 rate 0.5 | — | — | not produced this round (not run) |

## Direct use, STRONG reader (primary), after review
| Method | All (94) | Safety S (40) | Factual F (54) | §1 S / §5 S | Saved o200k |
|---|---|---|---|---|---|
| original text | 94/94 (100%) | 40/40 | 54/54 | 20/20 / 20/20 | 0% |
| **MNC15 + key** | **94/94 (100%)** | **40/40** | 54/54 | 20/20 / 20/20 | 21.8% (33.8% payload only) |
| **MNC15x, no key** | **92/94 (97.9%)** | **40/40** | 52/54 | 20/20 / 20/20 | 38.9% |
| **MNC15xx, no key** | **92/94 (97.9%)** | **40/40** | 52/54 | 20/20 / 20/20 | 43.8% |
| c LLMLingua-2 0.66 | 78/94 (83.0%) | 34/40 | 44/54 | 18/20 / 16/20 | 34.6% |
| b summarize | 70/94 (74.5%) | 28/40 | 42/54 | 10/20 / 18/20 | 31.9% |
| a terse English | 69/94 (73.4%) | 31/40 | 38/54 | 13/20 / 18/20 | 47.8% |
MNC15x/xx's only misses are the same 2 questions (§5 q1 en+nl): the shop name is in the payload, but the reader left it out of the answer.
MNC15 was not run without its key on the strong reader.

### Accuracy vs savings (strong reader, o200k)
| Saved | Method | Accuracy | Safety |
|---|---|---|---|
| 0% | original | 100% | 100% |
| 21.8% | MNC15 + key | 100% | 100% |
| 31.9% | b summarize | 74.5% | 70.0% |
| 34.6% | LLMLingua-2 0.66 | 83.0% | 85.0% |
| 38.9% | MNC15x | 97.9% | 100% |
| 43.8% | MNC15xx | 97.9% | 100% |
| 47.8% | a terse English | 73.4% | 77.5% |
At ≥38.9% savings, MNC holds ≥97.9% accuracy and 100% safety with this reader. The only method that saves more (terse English, +4 points) loses 24.5 points of accuracy. The point where MNC's strong-reader accuracy starts to fall has NOT been found yet.

## Direct use, WEAK reader (local 7B, secondary), after review
| Method | All (94) | S (40) | F (54) |
|---|---|---|---|
| original | 91/94 (96.8%) | 38/40 | 53/54 |
| MNC15 (no key) | 88/94 (93.6%) | 38/40 | 50/54 |
| c LLMLingua-2 0.66 | 77/94 (81.9%) | 35/40 | 42/54 |
| b summarize | 69/94 (73.4%) | 27/40 | 42/54 |
| a terse English | 64/94 (68.1%) | 28/40 | 36/54 |
MNC15 vs original: −3 questions, inside the ±2-3 noise band but consistent with earlier rounds (MNC slightly below original on the 7B). MNC15x/xx were not run on the 7B (only ~3 GB RAM free at 01:00).

## Instruction-safety
- **Strong reader, direct use: PASS** for MNC15+key, MNC15x and MNC15xx (40/40 each, no lost or flipped negation, condition, permission, actor, identity or deadline). This is the first round where an MNC version reaches 100% direct-use safety on any reader.
- **Weak reader, direct use: FAIL** (MNC15): §1.en11 and §1.es11 threshold flipped (35 sign-ups answered "yes, tell Marcus" when the rule is "only if more than 40"). The original text got 38/40 S on the same reader: §1.en4/es4 answered "no reminder post needed" for 2 volunteers.
- **Weak reader, blind decode** (secondary; fact-by-fact scoring still pending): FAIL. In the no-key §1 English decode, "more than 40" became "more than four". In the no-key §5 Dutch decode, "only if more than 15" became "vanaf 15" (from 15). The no-key §3 Japanese decode added an invented "東京" (Tokyo). With-key decodes kept every rule I checked by hand in §1/§5, but they have not been scored fact by fact.
- No strong-reader blind decode was run this round.

## Frozen bench-v1
Not run this round on either reader. MNC15/15x/15xx have no bench-v1 score yet, so no new-best claim is possible under the rules.

## Verdict
**Not a new best yet.** On fresh round-11 passages with the strong reader, MNC15x/xx are the strongest results so far: 97.9% at 38.9-43.8% savings, 100% safety, against at most 83.0% for every baseline. They still need (1) a bench-v1 score with the strong reader, (2) repeat frontier runs for noise, and (3) a clean blind test. MNC15x/xx were built in this write-up run, after the 7B results were in and with knowledge of the round's facts. The encoder side is therefore a self-test; only the readers were blind. MNC3 stays the recorded best.
Ready-for-live-instructions counter: 0 of 3 (this round fails safety on the weak reader and on the blind decode; MNC15x/xx are not a blind round).
