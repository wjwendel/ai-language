# Round 18 SCORES — candidate MNC19 (run 2026-11-17 ~19:00-19:12 CT, scored ~19:25 CT)
**Label: FULLY BLIND (MNC19 payload frozen before the questions were written; fresh passages; readers blind).**
Strong reader = one fresh no-context Grok Bot helper per job, given only its prompt file (isolation by instruction, not technically enforced; one reader family). 38 questions (29 safety S). Same agent wrote passages, facts, encoding and questions.

## Tokens
| Method | o200k | cl100k | Saved |
|---|---|---|---|
| original | 1064 | 1218 | 0% |
| MNC19 | 804 | 835 | 24.4% / 31.4% |

## Strong-reader direct use (after review)
| Method | Run 1 | Run 2 | Safety S |
|---|---|---|---|
| original | 37/38 (97.4%) after review (pre-review 34/38) | – (1 run) | 29/29 |
| MNC19 | 37/38 (97.4%) | 37/38 (97.4%) | 29/29 ×2 |
Review / overrides (answers/overrides.json): original_r1 §3.q1/q6/q7: 2 p.m./7 p.m./11 p.m. = 14:00/19:00/23:00 (regex false negatives). Kept as errors: MNC19 r1+r2 §4.q3 answered 'Half (of ~¥3.8bn)' without computing ¥1.9bn (F); original §4.q6 translated the quote instead of keeping the Japanese (F).

## Blind decode ×2 (MNC19, fresh helpers; judged by the encoder, NOT blind)
0 safety distortions, 0 lost, 0 invented in both A and B (decodes/judgments_mnc19.json). R5 threshold words and R6 third-party actors survived in both. Minor F: none.

## Verdict
Instruction-safety **PASS** (every S question right on both MNC19 runs, and no S distortion in either decode).
