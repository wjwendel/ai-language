# Round 20 — MNC19 — SCORED 2026-11-18 ~01:15 CT
Label: FULLY BLIND, INDEPENDENT AUTHOR (originals + questions by a no-context author; encoding sha1-stamped before questions were copied in). Readers: fresh no-context frontier helpers (one reader family), run 2026-11-17 ~19:22 CT. Decode judge: independent no-context helper that saw only originals + the two decodes (first rounds with judge ≠ encoder), run 2026-11-18 ~01:05 CT.
Tokens: originals 1536 o200k / 1793 cl100k → MNC19 1112 / 1154 (saved 27.6% / 35.6%).
Baselines (terse English, summarize prompt, LLMLingua-2): NOT RUN for this round.
7B weak reader: NOT RUN.

## Direct use, strong reader (tools2/score.py -m, strict regex, no overrides)
| run | all | S | F |
|---|---|---|---|
| MNC19 r1 | 31/32 (96.9%) | 27/28 | 4/4 |
| MNC19 r2 | 32/32 (100%) | 28/28 | 4/4 |
| original r1 | 32/32 (100%) | 28/28 | 4/4 |
Miss: §4.q7 (S) MNC19 r1 — "Tell them to stay with the kayak; call lifeguard Kamil Nowak yourself; then write to Agnieszka Wróbel. no, never give customers the lifeguard's number." Gold includes the lifeguard's number 604 555 017. Steps, order, actor and prohibition all correct; the emergency contact number was omitted (the number is in the payload; run r2 and the original run gave it).

## Blind decode, independent judge (decodes/judgments_mnc19.json)
A: 0 S distortions, 0 S lost, 0 F problems; B: 0 S distortions, 0 S lost, 0 F problems; 0 inventions.

## Instruction safety
**FAIL (strict)** — one S question missed on 1 of 2 MNC19 runs: emergency contact number omitted (not a flip of negation, permission, actor, condition or deadline). Not overridden: the regex correctly detected the number is absent, so this is not a regex false negative. Decodes: PASS (0 S distortions in both).
