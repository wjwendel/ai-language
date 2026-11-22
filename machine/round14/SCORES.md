# Round 14 SCORES — bench-v2 first blind scoring, candidate MNC18 (sprint 2026-11-17)

Round 14 = the first scoring of the new frozen bench-v2 (machine/bench-v2). The passages are new and no reader has seen them. MNC18 and MNC18z were frozen at 18:30 CT, before the questions were written. The rules were frozen at 18:27 CT (candidates/mnc18/RULES.md, sha1 6b2018e3…).

## Status: STRONG-READER RUNS NOT DONE — no primary result yet
This sprint's executor could not launch fresh no-context helpers, so the strong-reader runs could not happen here. The jobs are staged in ../SPRINT-DISPATCH.md: 13 QA jobs, 2 blind decodes and 1 terse-English writer. **No accuracy, safety or decode result is claimed for the strong reader.** The readiness counter does not move.

## Tokens (bench-v2 originals 2,217 o200k / 2,712 cl100k; no key)
| Method | o200k | cl100k | Saved o200k / cl100k | Saved o200k excl. §4 ja + §6 zh |
|---|---|---|---|---|
| MNC18 (candidate) | 1,491 | 1,579 | 32.7% / 41.8% | 32.2% |
| MNC18z (curve only) | 1,358 | 1,439 | 38.7% / 46.9% | 38.7% |
| LLMLingua-2 0.66 | 1,425 | 1,758 | 35.7% / 35.2% | 33.8% |
| LLMLingua-2 0.5 | 954 | 1,144 | 57.0% / 57.8%* | 49.3% |
| terse English (separate helper) | pending | pending | – | – |
*LLMLingua-2 cuts unspaced Japanese and Chinese short. At 0.5, §4 ja keeps only its first sentence and the email address (86.7% "saved"), and §6 zh is spliced from fragments. At 0.66, §4 also stops mid-passage. Its headline savings include the deleted content.

Lint (R4, facts.json must-regexes): MNC18 65/65. MNC18z 58/65 (all 7 misses are the grouped `never:` form and the `木村早苗 (=` form, which the regexes don't recognise. They are form misses, not content losses; checked by hand).

## Secondary weak reader (local Qwen2.5-7B Q4_K_M, temp 0, ×1, raw regex score before review)
| Method | All (89) | Safety S (61) | Facts F (28) | Two-hop (40) |
|---|---|---|---|---|
| original | 47/89 (52.8%) | 27/61 | 20/28 | 18/40 |
| MNC18 | 63/89 (70.8%) | 37/61 | 26/28 | 27/40 |
| MNC18z | 49/89 (55.1%) | 31/61 | 18/28 | 22/40 |
The 7B can't handle an 89-question prompt reliably. In both runs it shifted answers onto the wrong question IDs for long stretches (original: §2, §4, §6; MNC18: §6 and §4 q13-14). Both scores are dominated by that, so this is **not evidence that MNC18 beats the original**. It only says the shorter input left the 7B less confused. Treat it as noise and a harness limit. Raw files: bench-v2/answers_7b/.

---
## STRONG-READER RESULTS (run 2026-11-17 ~19:02-19:12 CT; one fresh no-context helper per job, each got only its prompt file)
Scored with tools2/score.py (89 questions: 61 safety S, 28 facts F, 40 two-hop). Overrides (answers/overrides.json): 3 regex false negatives accepted (original_r2 §6.q1 "10 a.m./4 p.m." = 10:00/16:00; terse_r1/r2 §1.q12 "open-orders summary, Thursdays by 3pm"). No real error flipped.

| Method | o200k / cl100k | Saved o200k / cl100k | Run 1 | Run 2 | Safety S |
|---|---|---|---|---|---|
| original | 2,217 / 2,712 | 0 / 0 | 100% | 100% | 61/61 ×2 |
| **MNC18** | 1,491 / 1,579 | 32.7% / 41.8% | **100%** | **100%** | 61/61 ×2 |
| **MNC18z** | 1,358 / 1,439 | **38.7% / 46.9%** | **100%** | **100%** | 61/61 ×2 |
| terse English (written by a separate fresh helper) | 1,560 / 1,599 | 29.6% / 41.0% | 95.5% | 95.5% | 60/61 ×2 (§6 "before 12:00" deadline flipped to "by 12:00 is fine") |
| LLMLingua-2 0.66 | 1,425 / 1,758 | 35.7% / 35.2% | 79.8% | – | 46/61 |
| LLMLingua-2 0.5 | 954 / 1,144 | 57.0% / 57.8%* | 61.8% | – | 34/61 |
*includes the Japanese/Chinese content LLMLingua-2 deletes (§4 ja → 51 tokens, 26 of its 34 misses are "not stated").
Terse English misses: 3 original-language quotes translated instead of kept (F), 1 deadline flip (S).

**Accuracy-vs-savings on bench-v2 (strong reader):** MNC18z 100% @ 38.7% > MNC18 100% @ 32.7% > LLMLingua-2 0.66 79.8% @ 35.7% ; terse 95.5% @ 29.6% ; LLMLingua-2 0.5 61.8% @ 57.0%. MNC18z is the only method that is both more accurate and smaller than terse English and LLMLingua-2 0.66. LLMLingua-2 0.5 is the only method that saves more, at a 38-point accuracy loss.

## Blind decode ×2 (MNC18, fresh helpers; judged by the encoder, NOT blind; decodes/judgments_mnc18.json)
Both decodes keep all 65 facts except one S-fact actor shift, the same in both: P6.6 "the customer must submit invoice info within 30 days of the order" → "you provide the invoice info if the request is within 30 days". Threshold and fallback (later → forward to 王磊) kept. Encoder cause: the payload line `invoice requests: invoice info within 30d of order` has no actor. **Under the round rule this is a safety FAIL (actor).** Minor in effect, but it's the passive-obligation class.

## Verdict
Direct-use instruction-safety PASS (61/61 on both MNC18 runs, and on both MNC18z runs). Blind-decode safety FAIL (1 actor shift ×2). Round 14 does **not** count toward the ready counter. Not a new best: no bench-v1 regression run for MNC18 yet; and bench-v2 is new, so no earlier version has a score on it.
