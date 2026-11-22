# Round 25 — MNC24 (MNC23xx form + R14 tell-slot actor, R15 qualifier after noun, R16 no type narrowing, R17 savings) — SCORED 2026-11-19 ~07:05 CT
Label: FULLY BLIND, INDEPENDENT AUTHOR. Originals (§1 en florist, §2 zh community sports-center registration notice, §3 es-MX driving school, §4 pl catering company) + 39 sealed questions (23 S, 16 F, 16 two-hop) written by a fresh no-context author (round25_sealed/AUTHOR-R25.md) after MNC24 was frozen (candidates/mnc24/RULES.md sha1 4784fcc7…, 06:55 CT). Encodings stamped 06:58 CT before questions.json was copied into round25/ (encoded_before_questions.sha1); the encoder never opened round25_sealed/questions.json before stamping.
Readers: fresh no-context frontier helpers (one reader family; isolation by instruction only). Decode judge: independent no-context helper (originals + 2 decodes only; closing courtesy sentences declared out of scope before the run).
facts.json: NOT written (the judge split the originals into 107 atomic facts, 72 S / 35 F; decodes/judgments_mnc24.json).

## Accuracy vs savings (strong reader; tools2/score.py)
Raw regex first; "reviewed" applies answers/overrides.json (8 regex false negatives, all the same cause: `\b462\b` / `\b324\b` fail when 元 directly follows the digits, because a CJK character counts as \w; the amounts were correct).
| Text | o200k / cl100k tokens | Saved o200k / cl100k | All raw → reviewed | S | Notes |
|---|---|---|---|---|---|
| original | 1507 / 1780 | 0 / 0 | 39/39 | 23/23 | ×1 |
| MNC24 (no key) | 1050 / 1078 | 30.3% / 39.4% | 37 → 39/39 ×2 | 23/23 ×2 | |
| **MNC24x** (no key) | 966 / 997 | **35.9% / 44.0%** | 37 → 39/39 ×2 | 23/23 ×2 | |
| terse English (frontier writer) | 993 / 1015 | 34.1% / 43.0% | 37/39 ×2 | 23/23 ×2 | both runs: flipped the §2 qualifier scope (made the "before Mar 10" condition apply to badminton too) → wrong yes/no and wrong amount (¥360 instead of 324) |
| summarize prompt | 1264 / 1440 | 16.1% / 19.1% | 39/39 | 23/23 | ×1 |
| LLMLingua-2 0.66 | 982 / 1171 | 34.8% / 34.2% | 29/39 (74.4%) | 21/23 | ×1; dropped "except Monday", the 480元 fee, the half refund rule, digits of a phone number, garbled a quoted sentence |
| LLMLingua-2 0.5 | 754 / 903 | 50.0% / 49.3% | 26/39 (66.7%) | 19/23 | ×1; lost phone digits, fees, refund rules, two "tell the customer" steps |
Key tokens: 0 (no key), break-even = 0.
Curve (o200k saved → strong-reader accuracy): summarize 16.1%→100%; MNC24 30.3%→100%; terse 34.1%→94.9%; LLMLingua 0.66 34.8%→74.4%; **MNC24x 35.9%→100%**; LLMLingua 0.5 50.0%→66.7%.
R15 is the fix that mattered: the qualifier-scope question that terse English got wrong in both runs was answered correctly in all four MNC24/24x runs. Savings target (≥45% o200k) NOT reached on this set (35.9%); the originals were already fairly dense English/Chinese.

## Blind decode of MNC24 (main form), independent judge (107 facts)
- A: 103 kept; 3 S "distortions", 1 F lost, 0 added. The 3 S items are all the same: the decoder opened §1/§3/§4 with "You are working for <business>" instead of "You are the (inbox) assistant of <business>", which the judge scored as the assistant's own role being generalized. No permission, prohibition, threshold, actor, deadline or name/role rule was changed.
- B: 106 kept; 0 S distortions/losses; 1 F lost; 0 added.
- F lost (both): §1 "a small flower shop" — encoder dropped the descriptor (the name "Florals" carries the type, but "small" was lost).
R14 held: both "tell the customer two things" steps (keep driver still / turn on hazard lights / close the gas valve) stayed the customer's action in both decodes and in all direct-use runs. R15 held in both decodes.

## Instruction safety
Direct use: **PASS** (S 23/23 on all four MNC24/24x runs).
Blind decode: B clean; A has 3 low-severity judge-flagged role-wording items caused by the bare `§N you` header (encoder ambiguity: header does not say "inbox assistant").
Round verdict: **FAIL (strict)** — kept strict, consistent with earlier rounds (e.g. r22 "a mechanic"→"the mechanic"). Ready counter (fully blind): r23 FAIL → r24 FAIL → r25 FAIL → **0/3**.

## Bench-v1 (frozen, 134-question conversion in bench/strong_mnc20; strong reader; raw regex, NOT blind: the bench encoder had seen these passages in earlier rounds)
| Version | Saved o200k / cl100k | Runs | S |
|---|---|---|---|
| original | 0 | 130/134 (97.0%), 131/134 (97.8%) | 55/56, 56/56 |
| MNC24 (bench/versions/mnc24.txt, encoded this run) | 44.6% / 51.9% | 130/134 (97.0%), 128/134 (95.5%) | 56/56 ×2 |
| MNC16x (re-run on the 134-q set this run) | 44.8% / 52.5% | 130/134 (97.0%) ×2 | 56/56 ×2 |
| MNC20 (r21) | 24.3% / 34.8% | 127/134 (94.8%) | 56/56 |
Most MNC misses are regex false negatives shared with MNC16x (ET vs "Eastern", "museum sells no food", "start Oct 1, end Dec 18"); one real shared loss: r5P3.Q4 "to Mom" became "to me (the writer)". MNC24 ties MNC16x inside noise and does not beat it (−0.2 points of savings, −2 questions in one run).

## 7B weak reader (secondary)
Round 24 addendum (queue finished this run; raw regex, no review): MNC23xx 24, 23, 24 /40 (57.5-60%) vs original 26, 27, 27 /40 (65-67.5%). Spread 1 question each; the 7B gap (~7 points) is outside the spread → the weak reader still prefers the original text.
Round 25: queue7b.sh (MNC24x + original ×3) running as a detached job at write-up → see 7B section below if appended, else PENDING.

## Verdict
Not a new best. Fresh blind round: MNC24x beats every baseline (100% ×2 at 35.9% o200k vs terse English 94.9% at 34.1%; LLMLingua-2 0.5 saves more but drops to 66.7%). Frozen bench: MNC24 ties MNC16x (both ≈ original accuracy at ~44.7% saved) but does not beat it. MNC16x/xx stay the recorded strong-reader best; MNC3 the weak-reader best.

## 7B addendum (written 2026-11-19 ~13:05 CT, next routine run; raw regex with the fixed CJK-safe scorer, no manual review)
Queue finished 07:30 CT. MNC24x 16, 17, 14 /39 (35.9-43.6%; S 10-12/23) vs original 30, 29, 31 /39 (74.4-79.5%; S 17-19/23). Spread ≤3 questions each; the gap (~35 points) is far outside the spread → the weak 7B reader cannot use MNC24x without a key; strong-reader results are unaffected. Scorer fix: tools2/score.py now rewrites `\b` next to a digit as digit lookarounds (backup score.py.bak_r25); strong-reader r25 raw scores now equal the reviewed ones (MNC24/24x 39/39 ×2 with no overrides needed for the 元 amounts).
