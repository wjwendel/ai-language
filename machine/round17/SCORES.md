# Round 17 SCORES — candidate MNC19 (run 2026-11-17 ~19:00-19:12 CT, scored ~19:25 CT)
**Label: encoding NOT question-blind (re-encoded with MNC19 after its questions existed; readers blind).**
Strong reader = one fresh no-context Grok Bot helper per job, given only its prompt file (isolation by instruction, not technically enforced; one reader family). 36 questions (25 safety S). Same agent wrote passages, facts, encoding and questions.

## Tokens
| Method | o200k | cl100k | Saved |
|---|---|---|---|
| original | 982 | 1170 | 0% |
| MNC19 | 740 | 772 | 24.6% / 34.0% |

## Strong-reader direct use (after review)
| Method | Run 1 | Run 2 | Safety S |
|---|---|---|---|
| original | 36/36 (100%) after review (pre-review 35/36) | – (1 run) | 25/25 |
| MNC19 | 36/36 (100%) | 36/36 (100%) | 25/25 ×2 |
Review / overrides (answers/overrides.json): original_r1 §4.q7 '6 p.m.' = 18:00 (regex false negative).

## Blind decode ×2 (MNC19, fresh helpers; judged by the encoder, NOT blind)
0 safety distortions, 0 lost, 0 invented in both A and B (decodes/judgments_mnc19.json). R5 threshold words and R6 third-party actors survived in both. Minor F: decode A+B: Freiburg 'decided' became 'announced' (encoder wrote no verb; F, not safety).

## Verdict
Instruction-safety **PASS** (every S question right on both MNC19 runs, and no S distortion in either decode).
