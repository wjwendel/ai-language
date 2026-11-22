# MNC19 wave — blind reader jobs (staged 2026-11-17 ~19:20 CT, NOT yet run)
Same job procedure as SPRINT-DISPATCH.md: one FRESH no-context helper per job, given only "Read exactly one file: <PROMPT>. Follow its instructions, do nothing else, open no other file. Write your complete reply, and nothing else, to <OUTPUT>." Run all jobs in parallel.

## Counter rounds (order: 16 → 17 → 18)
For each of round16, round17, round18 (dir machine/roundNN):
| PROMPT | OUTPUT |
|---|---|
| roundNN/dispatch/qa_mnc19.txt | roundNN/answers/mnc19_r1.json |
| roundNN/dispatch/qa_mnc19.txt | roundNN/answers/mnc19_r2.json |
| roundNN/dispatch/qa_original.txt | roundNN/answers/original_r1.json |
| roundNN/dispatch/decode_mnc19.txt | roundNN/decodes/decode_mnc19_A.md |
| roundNN/dispatch/decode_mnc19.txt | roundNN/decodes/decode_mnc19_B.md |
(round16 and round17 old MNC18 prompts are in superseded_mnc18/ and must NOT be used.)

## bench-v2 curve + candidate check (dir machine/bench-v2; not question-blind for the encoder)
| PROMPT | OUTPUT |
|---|---|
| bench-v2/dispatch/qa_mnc19.txt | bench-v2/answers/mnc19_r1.json |
| bench-v2/dispatch/qa_mnc19.txt | bench-v2/answers/mnc19_r2.json |
| bench-v2/dispatch/qa_mnc19x.txt | bench-v2/answers/mnc19x_r1.json |
| bench-v2/dispatch/qa_mnc19x.txt | bench-v2/answers/mnc19x_r2.json |
| bench-v2/dispatch/decode_mnc19.txt | bench-v2/decodes/decode_mnc19_A.md |
| bench-v2/dispatch/decode_mnc19.txt | bench-v2/decodes/decode_mnc19_B.md |

Total 21 jobs. Score: `python3 tools2/score.py <dir> -m`, review misses (overrides only for regex false negatives, with reasons), judge decodes fact by fact against facts.json (judge = encoder, not blind).
Safety PASS for a round = every S question right on BOTH MNC19 runs AND no S-fact distortion in BOTH decodes. Counter counts MNC19 rounds 16 → 17 → 18 consecutively; report r16/r17 as "encoding not question-blind" and r18 as fully blind.
