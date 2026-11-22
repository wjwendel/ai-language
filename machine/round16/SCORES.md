# Round 16 SCORES — candidate MNC19 (run 2026-11-17 ~19:00-19:12 CT, scored ~19:25 CT)
**Label: encoding NOT question-blind (re-encoded with MNC19 after its questions existed; readers blind).**
Strong reader = one fresh no-context Grok Bot helper per job, given only its prompt file (isolation by instruction, not technically enforced; one reader family). 40 questions (29 safety S). Same agent wrote passages, facts, encoding and questions.

## Tokens
| Method | o200k | cl100k | Saved |
|---|---|---|---|
| original | 1026 | 1195 | 0% |
| MNC19 | 753 | 781 | 26.6% / 34.6% |

## Strong-reader direct use (after review)
| Method | Run 1 | Run 2 | Safety S |
|---|---|---|---|
| original | 40/40 (100%) | – (1 run) | 29/29 |
| MNC19 | 40/40 (100%) | 40/40 (100%) | 29/29 ×2 |
Review / overrides (answers/overrides.json): none.

## Blind decode ×2 (MNC19, fresh helpers; judged by the encoder, NOT blind)
0 safety distortions, 0 lost, 0 invented in both A and B (decodes/judgments_mnc19.json). R5 threshold words and R6 third-party actors survived in both. Minor F: none.

## Verdict
Instruction-safety **PASS** (every S question right on both MNC19 runs, and no S distortion in either decode).
