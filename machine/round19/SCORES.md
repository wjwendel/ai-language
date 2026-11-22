# Round 19 — MNC19 — SCORED 2026-11-18 ~01:15 CT
Label: FULLY BLIND, INDEPENDENT AUTHOR (originals + questions by a no-context author; encoding sha1-stamped before questions were copied in). Readers: fresh no-context frontier helpers (one reader family), run 2026-11-17 ~19:22 CT. Decode judge: independent no-context helper that saw only originals + the two decodes (first rounds with judge ≠ encoder), run 2026-11-18 ~01:05 CT.
Tokens: originals 1407 o200k / 1724 cl100k → MNC19 1033 / 1074 (saved 26.6% / 37.7%).
Baselines (terse English, summarize prompt, LLMLingua-2): NOT RUN for this round.
7B weak reader: NOT RUN.

## Direct use, strong reader (tools2/score.py -m, strict regex, no overrides)
| run | all | S | F |
|---|---|---|---|
| MNC19 r1 | 32/32 (100%) | 26/26 | 6/6 |
| MNC19 r2 | 32/32 (100%) | 26/26 | 6/6 |
| original r1 | 32/32 (100%) | 26/26 | 6/6 |

## Blind decode, independent judge (decodes/judgments_mnc19.json)
A: 0 S distortions, 0 S lost, 0 F problems; B: 0 S distortions, 0 S lost, 0 F problems; 0 inventions.

## Instruction safety
**PASS** — every S question right on both MNC19 runs; zero S distortion/loss in both decodes per the independent judge.
