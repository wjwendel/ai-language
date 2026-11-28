# Round 38 scores (2026-11-28, run ~06:54-~07:30 CT) — fully blind, independent author
Texts: originals.txt written by an independent no-context author (§1 en small-business assistant instructions / §2 ja neighborhood-association year-end night-watch notice / §3 de and §4 th small-business assistant instructions; 3,589 o200k / 5,585 cl100k tokens). **60 questions** (44 S, 16 F, 29 two-hop; 23 written in ja/de/th; 6 three-rule chains, 8 near-miss numbers, one-noun qualifier scope test, a deliberate "should" question, actor-on-permission-trigger tests). questions.json sealed in round38_sealed until both payloads were encoded and hashed (encoded_before_questions.sha1), then copied (questions.sha1).
Versions: **MNC28 = main, frozen** (MNC28-RULES.md sha1 f70a3563, identical to rounds 31-37). MNC28x = experimental probe "terse + safety rails" (no §0 key; terse English slots for every section; rails on actors, one-noun scope, should/may/must, THE/NOT THE roles, approvers on limit lines). See MNC28x-R38-NOTE.md. Both encoded by encoder helpers from originals.txt only (never saw questions).
Readers: fresh no-context frontier helpers given only payload + questions (one reader family; isolation by instruction only). Baselines a/b written by separate no-context helpers. LLMLingua-2 run locally (0.66, 0.5). Decode judge: independent no-context helper (originals + 4 decodes only). No scorer overrides.

## Tokens (tiktoken)
| Text | o200k | saved | cl100k | saved |
|---|---|---|---|---|
| original | 3,589 | 0 | 5,585 | 0 |
| MNC28 (main, no key) | 3,072 | 14.4% | 3,465 | 38.0% |
| MNC28x (probe, no key) | 2,721 | 24.2% | 3,008 | 46.1% |
| terse English | 2,158 | 39.9% | 2,273 | 59.3% |
| summarize | 2,692 | 25.0% | 4,020 | 28.0% |
| LLMLingua-2 0.66 | 2,157 | 39.9% | 3,302 | 40.9% |
| LLMLingua-2 0.5 | 1,713 | 52.3% | 2,593 | 53.6% |
Neither AIL form has a separate key this round, so break-even is immediate (no key cost).

## Direct use, strong reader (60 q)
| Text | Runs | All | S (44) | F (16) |
|---|---|---|---|---|
| MNC28 | ×2 | 59/60 ×2 (98.3%) | 44/44 ×2 | 15/16 ×2 |
| MNC28x | ×2 | 60/60 ×2 (100%) | 44/44 ×2 | 16/16 ×2 |
| original | ×1 | 60/60 | 44/44 | 16/16 |
| terse English | ×2 | 60/60 ×2 | 44/44 ×2 | 16/16 ×2 |
| summarize | ×1 | 60/60 | 44/44 | 16/16 |
| LLMLingua-2 0.66 | ×1 | 44/60 (73.3%) | 39/44 | 5/16 |
| LLMLingua-2 0.5 | ×1 | 42/60 (70.0%) | 36/44 | 6/16 |
MNC28 miss (both runs, §2.q3, the one-noun scope test): the MNC28 payload wrote "町内会で用意：拍子木 + 懐中電灯 + 反射ベスト（12月20日までに申し込んだ方の分のみ）". The original limits only the vests to people who applied by Dec 20; with the qualifier in parentheses after a "+" list, both readers applied it to all three items. This is an encoder-caused scope error. LLMLingua-2 lost nearly all of the Japanese section (§2 answered "not stated") and dropped other facts; 0.5 also named an approver the text doesn't state and broke a "should" rule.

## Blind decode (no key; judge, 224 facts: 155 S / 69 F)
| Decode | Kept | S errors | F errors | Added |
|---|---|---|---|---|
| MNC28 A | 222 | 1 (Dec-20 condition widened from vests to all equipment) | 1 (same error: clappers/flashlights wrongly restricted) | 2 harmless notes ("approver not named", romanizations) |
| MNC28 B | 222 | 1 (same) | 1 (same) | 2 harmless |
| MNC28x A | 224 | 0 | 0 | 1 harmless ("text does not say who approves") |
| MNC28x B | 224 | 0 | 0 | 1 harmless |

## Instruction-safety
- MNC28 main: S questions 44/44 ×2, but the blind decode has one encoder-caused S distortion (a scope condition in the everyday §2) in both decodes → **strict gate FAIL**. Same standard as r30 (everyday-section S distortion counted as a failure). **Ready counter: MNC28's streak ends at 7 (r31-r37); counter now 0** (the rules are unchanged, so the next clean blind pass would be 1).
- MNC28x probe: 60/60 ×2, decode 224/224 ×2, 0 errors → PASS. But it saves less than terse English (24.2% vs 39.9% o200k), so it is not promoted.

## 7B (secondary weak reader)
r38 queue running in the background at write-up (answers_7b/keep); pending. r37 7B scored now: MNC28 67.8% / 69.5% (2 runs; 1 run timed out), MNC28x 69.5-79.7% (3 runs), original 16.9% ×2 (invalid: the original prompt is too long for the 7B setup, answers mostly empty/truncated — not a fair comparison).

## Verdict
Not a new best. Terse English saved 15.7 points more than MNC28x and 25.5 more than MNC28 at equal (100%) strong-reader accuracy. MNC28x was the cleanest form this round (perfect answers and perfect decode) but over-preserved wording. MNC28 main failed the strict decode gate on the one-noun scope test, ending its 7-round blind streak. Bench-v1 not run.
