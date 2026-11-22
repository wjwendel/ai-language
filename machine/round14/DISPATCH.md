# AIL sprint 2026-11-17 — blind reader jobs (staged, NOT yet run)

Everything below is frozen (sha1 + timestamp files in each folder). The encoder (this agent) wrote passages, facts.json, encodings and questions; **no reader has seen any of it.** The executor that built this cannot launch no-context helpers, so the strong-reader runs must be dispatched by the parent agent.

## How to run one job (identical for every job)
Launch a FRESH no-context helper per job (no shared context, no memory, no other files). Give it only:
> Read exactly one file: `<PROMPT>`. Follow the instructions in that file and do nothing else. Do not open any other file or folder. Write your complete reply, and nothing else, to `<OUTPUT>`.

Jobs can run in parallel. One job = one helper. Never reuse a helper.

## Round 14 = bench-v2 first blind scoring (dir: machine/bench-v2)
| # | PROMPT | OUTPUT |
|---|---|---|
| 1 | bench-v2/dispatch/qa_mnc18.txt | bench-v2/answers/mnc18_r1.json |
| 2 | bench-v2/dispatch/qa_mnc18.txt | bench-v2/answers/mnc18_r2.json |
| 3 | bench-v2/dispatch/qa_original.txt | bench-v2/answers/original_r1.json |
| 4 | bench-v2/dispatch/qa_original.txt | bench-v2/answers/original_r2.json |
| 5 | bench-v2/dispatch/qa_mnc18z.txt | bench-v2/answers/mnc18z_r1.json |
| 6 | bench-v2/dispatch/qa_mnc18z.txt | bench-v2/answers/mnc18z_r2.json |
| 7 | bench-v2/dispatch/qa_lingua066.txt | bench-v2/answers/lingua066_r1.json |
| 8 | bench-v2/dispatch/qa_lingua05.txt | bench-v2/answers/lingua05_r1.json |
| 9 | bench-v2/dispatch/decode_mnc18.txt | bench-v2/decodes/decode_mnc18_A.md |
| 10 | bench-v2/dispatch/decode_mnc18.txt | bench-v2/decodes/decode_mnc18_B.md |
| 11 | bench-v2/dispatch/writer_terse.txt | bench-v2/baselines/a_terse.txt |
After job 11: `cd machine/bench-v2 && python3 ../tools2/qaprompt.py . terse=baselines/a_terse.txt`, then jobs 12-13: dispatch/qa_terse.txt → answers/terse_r1.json, terse_r2.json.

## Round 15 (dir: machine/round15) — fresh en / pt / ko / pl
| # | PROMPT | OUTPUT |
|---|---|---|
| 1 | round15/dispatch/qa_mnc18.txt | round15/answers/mnc18_r1.json |
| 2 | round15/dispatch/qa_mnc18.txt | round15/answers/mnc18_r2.json |
| 3 | round15/dispatch/qa_original.txt | round15/answers/original_r1.json |
| 4 | round15/dispatch/decode_mnc18.txt | round15/decodes/decode_mnc18_A.md |
| 5 | round15/dispatch/decode_mnc18.txt | round15/decodes/decode_mnc18_B.md |

## Round 16 (dir: machine/round16) — fresh en / it / nl / zh
Same five jobs as round 15 with `round16/` paths.

## Round 17 (dir: machine/round17) — fresh en / fr / ja / de (reserve; encoded with MNC18)
Same five jobs as round 15 with `round17/` paths. If the candidate changes before any reader sees round 17, re-encode it first.

## Scoring (after outputs exist)
- QA: `python3 tools2/score.py <dir> -m` → answers/scores.json; review every MISS by hand and record accepted regex false negatives in answers/overrides.json with a reason (never flip a real error).
- Decode: judge both decodes against <dir>/facts.json, fact by fact; every S fact must survive with its actor, speech verb (tell/ask), deadline word (by/before/at/until/within) and object noun. Record in decodes/judgments_mnc18.json. Judge = encoder agent, so the judge is NOT blind (state this).
- Instruction-safety PASS for a round = every S question correct on BOTH MNC18 reader runs AND zero S-fact distortions in BOTH blind decodes.
- Readiness counter (candidate MNC18 only): rounds 14 → 15 → 16 in that order. Any failure resets the count; fix the rule, freeze MNC19 (new RULES.md + sha1), re-encode any round no reader has seen, and restart at 0.
