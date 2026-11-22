# Round 33 scores (2026-11-22, run ~01:17-~02:10 CT) — fully blind, independent author
Texts: originals.txt written by an independent no-context author (en sign-making workshop / ko district free health-checkup notice / fr bookbinding-restoration workshop / vi tile-setting business; 1,345 words, 2,184 o200k tokens; instruction sections 300-380 words; distractor rules, day-only and group-only rules, "only X may" rules, "never X unless Y", type-only self-approval limits, near-miss numbers, three-rule chains). 39 questions (27 S, 12 F, 20 two-hop, about 1/3 in Korean/French/Vietnamese). questions.json sealed in round33_sealed until both payloads were encoded and hashed (encoded_before_questions.sha1).
Versions: **MNC28 = main, frozen** (MNC28-RULES.md sha1 f70a3563, identical to rounds 31-32). MNC28x = experimental probe (telegraphic "may ≤N" lines, no company descriptors, ALL non-English sections incl. §3/§4 instructions and §2 everyday notice rendered as compact English slots; names and verbatim customer sentences kept in original script).
Readers: fresh no-context frontier helpers (one reader family; isolation by instruction only). Baselines a/b written by separate no-context helpers. LLMLingua-2 run locally. Decode judge: independent no-context helper (originals + 2 decodes only).
Scorer change (applied to all texts alike): one shared regex fix — §1.q6 (approver not stated) now also accepts "does not state" (the original's reader answered correctly in those words). Before the fix the original scored 38/39.

## Accuracy vs savings (strong reader)
| Text | o200k tokens (saved) | cl100k (saved) | Direct use all | S (safety) | Runs |
|---|---|---|---|---|---|
| original | 2184 (0) | 2936 (0) | 39/39 100% | 27/27 | 1 |
| **MNC28 main** | 1696 (22.3%) | 1975 (32.7%) | 39/39 ×2 | 27/27 ×2 | 2 |
| MNC28x probe | 1275 (41.6%) | 1322 (55.0%) | 39/39 ×2 | 27/27 ×2 | 2 |
| terse English | 1258 (42.4%) | 1303 (55.6%) | 39/39 ×2 | 27/27 ×2 | 2 |
| summarize | 1508 (31.0%) | 1956 (33.4%) | 39/39 | 27/27 | 1 |
| LLMLingua-2 0.66 | 1437 (34.2%) | 1932 (34.2%) | 36/39 92.3% | 26/27 | 1 |
| LLMLingua-2 0.5 | 1120 (48.7%) | 1485 (49.4%) | 33/39 84.6% | 23/27 | 1 |
LLMLingua failures: 0.66 named an approver the text leaves unstated (§1.q6) and missed two Korean facts (one flipped yes→no, one arithmetic answer "not stated"); 0.5 also named a wrong approver for §3, flipped a §3 discount permission (yes→no) and dropped the tell-the-customer callback step from the §3 emergency (§3.q9). Both are instruction-safety failures.
Break-even: no key is used (MNC28/MNC28x run keyless), so savings apply from the first use.

## Blind decode (MNC28 main; 2 decoders, independent judge, 138 facts: 95 S / 43 F)
- A: 138/138 kept, 0 distortions, 0 losses.
- B: 137/138 kept; 1 F distortion (§2 flu shots "not given together with the screenings" decoded as "not given during the period" — decoder-caused; the payload keeps 함께 "together").
- Both added "(the approver is not named)" on the §1 custom-sign refund rule — accurate, carried from the payload's explicit "approver not named" marker; not a meaning change.
- Close calls the judge did not count: dropped "exact" before quoted sentences (sentences kept verbatim); "full age" for the 65+ discount.
**Instruction-safety: PASS** (0 S errors across direct use ×2 and decode ×2).

## Weak reader (local Qwen-7B, 3 runs each)
MNC28 66.7-76.9% (S 70.4-81.5%), MNC28x 51.3-66.7% (S 55.6-66.7%), original 53.8% all three runs (S 51.9%). MNC28 is above the original's range on all 3 runs (weak-reader gain outside the spread); MNC28x overlaps the original (tie). Weak-reader result is secondary.

## Ready counter
**MNC28: 3/3** (rounds 31, 32, 33 — fully blind, same RULES sha1 f70a3563, 100% instruction-safety each). MNC28 now meets the ready-for-live-instructions bar as defined for this project. (MNC26 reached 3/3 on r27-r29 earlier.)

## Verdict
Not a new best on savings: terse English saves 20.1 points (o200k) more than MNC28 main at equal accuracy. MNC28x is within 0.8 points (o200k) / 0.6 (cl100k) of terse at 100% — a tie. Bench-v1 not run this round. Questions were again at ceiling for every faithful text; only LLMLingua failed.

