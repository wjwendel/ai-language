# Round 27 — MNC26 (MNC25x form promoted to main + R20 unnamed-approver marker) — SCORED 2026-11-19 ~19:05 CT
Label: FULLY BLIND, INDEPENDENT AUTHOR. Originals (§1 en roofing company, §2 ko apartment-complex bulky-waste collection notice, §3 it window-cleaning company, §4 sv heat-pump service company) + 40 sealed questions (28 S, 12 F, 13 two-hop) written by a fresh no-context author (round27_sealed/AUTHOR-R27.md, adds "gold must not assume anything the text doesn't state") after MNC26 was frozen (candidates/mnc26/RULES.md sha1 6c1bc095…, ~18:55 CT). Encodings stamped before questions.json was copied into round27/ (encoded_before_questions.sha1); the encoder never opened the sealed questions before stamping.
Readers: fresh no-context frontier helpers (one reader family; isolation by instruction only). Decode judge: independent no-context helper (originals + 2 decodes only).
facts.json: NOT written (the judge split the originals into 142 atomic facts, 78 S; decodes/judgments_mnc26.json).

## Accuracy vs savings (strong reader)
Raw regex → reviewed (answers/overrides.json): terse §2.q1 ×2 time-format false negatives ("7–10 AM"); terse_r1 §3.q3 said "approver not stated" (correct, regex tripped on the parenthetical name). No other reviews.
Key finding: §3 of the original says condo/shop quotes "always need approval" without naming the approver. The ORIGINAL-text reader, the summarize reader, one terse reader and LLMLingua 0.5 all named Chiara Bonetti (an invented approver = S error). MNC26/26x (R20 marker `approver not named`) got it right in all 4 runs.
| Text | o200k / cl100k tokens | Saved o200k / cl100k | All raw → reviewed | S reviewed | Notes |
|---|---|---|---|---|---|
| original | 1632 / 2002 | 0 / 0 | 39/40 (97.5%) | 27/28 | ×1; §3.q3 invented approver |
| MNC26 (main, no key) | 1030 / 1066 | 36.9% / 46.8% | 40/40 ×2 | 28/28 ×2 | |
| MNC26x (aggressive, no key) | 1018 / 1055 | 37.6% / 47.3% | 40/40 ×2 | 28/28 ×2 | only 12 tokens shorter than main this round |
| terse English (frontier writer) | 992 / 1021 | **39.2% / 49.0%** | 38, 38 → 40/40, 39/40 | 28/28, 27/28 | run 2 invented approver (§3.q3) |
| summarize prompt | 1247 / 1464 | 23.6% / 26.9% | 39/40 | 27/28 | ×1; invented approver |
| LLMLingua-2 0.66 | 1106 / 1357 | 32.2% / 32.2% | 38/40 (95.0%) | 27/28 | ×1; lost per-door wardrobe price; dropped "070" prefix + "yourself" in emergency step |
| LLMLingua-2 0.5 | 860 / 1039 | 47.3% / 48.1% | 29/40 (72.5%) | 24/28 | ×1; two prohibitions flipped to "yes" (§1.q4, §4.q6), invented approver, lost phone prefix |
Key tokens: 0 (no key), break-even = 0.
Curve (o200k saved → strong-reader accuracy, mean of runs): summarize 23.6%→97.5%; LLMLingua 0.66 32.2%→95.0%; MNC26 36.9%→100%; MNC26x 37.6%→100%; terse 39.2%→98.75%; LLMLingua 0.5 47.3%→72.5%.
Honest read: MNC26 is the only text family with 100% S in every run (4/4, incl. the aggressive form), and it beats the original text itself on this set, but terse English still saves 2.3 points more (o200k) at 98.75%. Single reader family, small n: the 1-question gaps are inside plausible noise.

## Blind decode of MNC26 (main form), independent judge (142 facts, 78 S)
- A: S 0 distorted / 0 lost; F 6 distorted / 0 lost; 0 added. The 6 F items are one encoding ambiguity ×3 sections: `wkdays 7:30,13h` (two check times) decoded as a window "from 7:30 to 13:00".
- B: 142/142 kept, 0 distorted, 0 lost, 0 added.
Both decodes wrote "approver not named" for §3; the judge counted it as accurate, not added.

## Instruction safety
MNC26 (main form): direct use S 28/28 ×2; blind decodes 0 S distortions/losses (judge). → **PASS**, with one caveat: the judge classed inbox check times as F; if they were treated as S, decode A would fail. Fix R21 next round (write `at 7:30 + 13h`).
Ready counter (fully blind, main form, 3 consecutive): r25 FAIL → r26 PASS → **r27 PASS → 2/3**.

## Bench-v1
Not run (at ceiling for the strong reader). No formal new-best claim.

## 7B weak reader (secondary)
round27/queue7b.sh (MNC26x + original ×3) started 18:59 CT as a detached job; PENDING at write-up — score next run with `ANS=answers_7b python3 tools2/score.py round27`.

## Verdict
Not a formal new best (no bench run; terse English saves more). Main form safety-clean for the second blind round in a row (counter 2/3) and the only form with perfect S accuracy across all runs.

## Counter correction (2026-11-19, parent)
r26 used MNC25 and r27 used MNC26 (the rules changed: x form promoted plus R20 marker), so under the one-frozen-version rule the strict counter is **MNC26: 1/3**, not 2/3. Keep the MNC26 main form frozen (no R21 in main; put R21 only in x) so r28 and r29 can count.

## 7B addendum (scored 2026-11-20 ~01:00 CT routine run; local Qwen2.5-7B, secondary weak reader, ×3)
| Text | run1 | run2 | run3 | spread | S range |
|---|---|---|---|---|---|
| MNC26x | 55.0% | 47.5% | 55.0% | 47.5-55.0% | 50.0-64.3% |
| original | 67.5% | 72.5% | 75.0% | 67.5-75.0% | 75.0% ×3 |
Raw regex scores (not reviewed). The ranges do not overlap: on the weak 7B reader the MNC26x form LOSES to the original text by ~12-25 points. The weak-reader gap is real and unresolved; MNC is a strong-reader format.
