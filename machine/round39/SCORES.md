# Round 39 scores (2026-11-28, run ~09:51-~10:35 CT) — fully blind, independent author
Texts: originals.txt written by an independent no-context author (§1 en model-railway shop assistant instructions / §2 ko apartment-complex everyday notice / §3 it and §4 ar small-business assistant instructions; 3,584 o200k / 5,328 cl100k tokens). **58 questions** (43 S, 15 F; three-rule chains, near-miss numbers, one-item list-qualifier test, "the" vs "a" identity tests, "should" test, actor-on-trigger tests; about 1/3 written in ko/it/ar). questions.json sealed in round39_sealed until both payloads were encoded and hashed (encoded_before_questions.sha1), then copied (questions.sha1).
Versions: **MNC28 = main, frozen** (MNC28-RULES.md sha1 f70a3563, identical to rounds 31-38). MNC28x (r39) = experimental probe: terse English written first by the encoder, then only safety rails added (THE/NOT THE/A identity lines, actor on triggers, one-item qualifiers on their item, exact should/may/must, one approver per limit line). See MNC28x-R39-NOTE.md. Both encoded by encoder helpers from originals.txt only (never saw questions).
Readers: fresh no-context frontier helpers given only the text + questions (one reader family; isolation by instruction only). Baselines a/b written by separate no-context helpers. LLMLingua-2 run locally (0.66, 0.5). Decode judge: independent no-context helper (originals + 4 decodes only). Scoring: the authors' regexes, no scorer overrides.

## Tokens (tiktoken)
| Text | o200k | saved | cl100k | saved |
|---|---|---|---|---|
| original | 3584 | 0 | 5328 | 0 |
| MNC28 (main) | 2516 | 29.8% | 2667 | 49.9% |
| MNC28x (probe) | 2149 | 40.0% | 2292 | 57.0% |
| terse English (a) | 2095 | 41.5% | 2187 | 59.0% |
| summarize (b) | 2455 | 31.5% | 3417 | 35.9% |
| LLMLingua-2 0.66 | 2382 | 33.5% | 3518 | 34.0% |
| LLMLingua-2 0.5 | 1833 | 48.9% | 2685 | 49.6% |
No key for any version (break-even 0).

## Direct use, strong reader (58 q)
| Text | run 1 | run 2 | notes |
|---|---|---|---|
| original | 58/58 | – | |
| MNC28 | 58/58 | 58/58 | S 43/43 ×2 |
| MNC28x | 58/58 | 57/58 | r2 miss §4.q5: answered the correct approver but in Arabic script ("سلمى حداد") because the payload kept the name in Arabic; the regex wants Latin "Salma Haddad". Counted as a miss (no overrides); likely a script artifact, not a safety flip. |
| terse | 58/58 | 58/58 | |
| summarize | 58/58 | – | |
| LLMLingua-2 0.66 | 57/58 | – | §1.q15 said "required" for a "should" rule (should→must flip) |
| LLMLingua-2 0.5 | 51/58 | – | 4 S misses (should→must, incomplete emergency phone numbers ×2, a permission flip), 3 F misses (Korean/Arabic facts) |

## Blind decode (independent judge; 196 facts, 130 S / 66 F)
| Decode | kept | S errors | F errors | added |
|---|---|---|---|---|
| MNC28 A | 195 | 0 | 1 lost ("shared" inbox) | 1 accurate note (approver not named) |
| MNC28 B | 195 | 0 | 1 lost (same) | same note |
| MNC28x A | 194 | 1 lost (§2 Choi Ji-hoon's title 주임 / supervisor dropped) | 1 lost ("shared") | same note |
| MNC28x B | 192 | 1 lost (same title) | 2 distorted (§2 "bulletin boards in the complex" → "in each building"; leftover "insulation" → "covers") + 1 lost | note + "in each building" |

## Verdict
- **MNC28 main: PASS** (S 43/43 ×2, decode 0 S errors ×2; the only loss is the F word "shared"). Rules unchanged since r31, so **ready counter: MNC28 1/3** (restarted at 0 after the r38 fail).
- **MNC28x probe: decode FAIL** (an identity title lost in both decodes, encoder-caused). Savings 40.0% o200k, up from 24.2% in r38, but still 1.5 points under terse English.
- **Not a new best.** Terse English saved the most of any text at 100% ×2 (41.5% o200k). LLMLingua-2 0.66 matched MNC28x-level savings but flipped a "should" to "required".

## 7B (secondary weak reader)
r39 7B queue started in the background (3 runs × MNC28 / original / MNC28x); pending at write-up. r38 7B scored now (60 q): MNC28 38-40/60 (63.3-66.7%), MNC28x 40-42/60 (66.7-70.0%), original 41-42/60 (68.3-70.0%) — spreads overlap, treated as ties.
Bench-v1: not run this round.
Gmail: checked; no new xAI/Anthropic reply about AIL (latest are the already-reported Nov 23 messages).

