# Round 40 scores (2026-11-28, run ~12:56-~13:35 CT) — fully blind, independent author
Texts: originals.txt written by an independent no-context author (§1 en stained-glass studio assistant instructions / §2 zh residential-complex everyday notice / §3 es and §4 hi small-business assistant instructions; 3,200 o200k / 5,565 cl100k tokens). **59 questions** (40 S, 19 F; 23 hop-2/three-rule chains, near-miss numbers, one-item qualifier scope, "the" vs "a" identity, a deliberate "should" (recommended, not required) test, a job-title question and a place-scope question in §2; about 1/3 written in zh/es/hi). questions.json sealed in round40_sealed until both payloads were encoded and hashed (encoded_before_questions.sha1), then copied (questions.sha1).
Versions: **MNC28 = main, frozen** (MNC28-RULES.md sha1 f70a3563, identical to rounds 31-39). MNC28x-R40 = experimental probe: r39 "terse first, then rails" + two new rails (everyday sections keep titles next to names, exact place-scope nouns and each listed noun; non-Latin names get a Latin transliteration at first mention). See MNC28x-R40-RULES.md and MNC28x-R40-NOTE.md. Both encoded by encoder helpers from the rules + originals.txt only (never saw questions).
Readers: fresh no-context frontier helpers given only the text + questions (one reader family; isolation by instruction only). Baselines a/b written by separate no-context helpers. LLMLingua-2 run locally (0.66, 0.5). Decode judge: independent no-context helper (originals + 4 decodes only). Scoring: the authors' regexes, no scorer overrides.

## Tokens (tiktoken)
| Text | o200k | saved | cl100k | saved |
|---|---|---|---|---|
| original | 3200 | 0 | 5565 | 0 |
| MNC28 (main) | 2330 | 27.2% | 2572 | 53.8% |
| MNC28x-R40 (probe) | 2131 | 33.4% | 2306 | 58.6% |
| terse English (a) | 1954 | 38.9% | 2076 | 62.7% |
| summarize (b) | 2258 | 29.4% | 3647 | 34.5% |
| LLMLingua-2 0.66 | 2091 | 34.7% | 3707 | 33.4% |
| LLMLingua-2 0.5 | 1600 | 50.0% | 2851 | 48.8% |
No key for any version (break-even 0).

## Direct use, strong reader (59 q)
| Text | run 1 | run 2 | notes |
|---|---|---|---|
| original | 59/59 | – | |
| MNC28 | 59/59 | 59/59 | S 40/40 ×2 |
| MNC28x-R40 | 59/59 | 59/59 | S 40/40 ×2 |
| terse | 59/59 | 59/59 | |
| summarize | 57/59 | – | §1.q12 treated a "should" (recommended) as required; §4.q14 widened an exception (said "yes" where the exception does not cover the case) — both safety misses |
| LLMLingua-2 0.66 | 53/59 | – | 3 S misses (should→required, Friday-only 2-hour deadline applied generally, a Chinese permission lost) + 3 F misses in §2 (arithmetic, contact title, board scope) |
| LLMLingua-2 0.5 | 46/59 | – | 6 S misses (incl. naming an approver the text does not name; one emergency answer gave the right number but also mentioned the shop number, which the reject regex counts as a miss) + 7 F misses |

## Blind decode (independent judge; 194 facts, 136 S / 58 F)
| Decode | kept | S errors | F errors | added |
|---|---|---|---|---|
| MNC28 A | 194 | 0 | 0 | none |
| MNC28 B | 194 | 0 | 0 | 1 accurate note (approver not named) |
| MNC28x A | 193 | 0 | 1 lost (§2 addressee "各位居民 / all residents") | same accurate note |
| MNC28x B | 193 | 0 | 1 lost (same) | same accurate note |
The judge treated two wording differences as harmless: MNC28 decodes drop "exact(ly)" before required sentences but quote them verbatim; "over 75" vs "75 or over" for the ambiguous Chinese 以上.

## Verdict
- **MNC28 main: PASS** (S 40/40 ×2, decode 194/194 ×2). Rules unchanged since r31, so **ready counter: MNC28 2/3**.
- **MNC28x-R40 probe: clean** (100% ×2, decode 0 S errors; the new rails fixed the r39 title loss) **but saves less**: 33.4% o200k vs 40.0% in r39, 5.5 points under terse English. Not promoted.
- **Not a new best.** Terse English saved the most of any text at 100% ×2 (38.9% o200k). Summarize and LLMLingua-2 both had safety misses.

## 7B (secondary weak reader)
r40 7B queue started in the background (3 runs × MNC28 / original / MNC28x); pending at write-up. r39 7B scored now (58 q): MNC28 37-40/58 (63.8-69.0%), MNC28x 42-43/58 (72.4-74.1%), original 39/58 ×3 (67.2%). MNC28 overlaps the original (tie); MNC28x was slightly above both on this weak reader.
Bench-v1: not run this round.
Gmail: not checked this run (already checked earlier today; once per day).
