# Round 22 — MNC21 (new: R8 derived amount as verb object, R9 identity as written) — SCORED 2026-11-18 ~13:05 CT
Label: FULLY BLIND, INDEPENDENT AUTHOR. Originals (§1 en bike workshop, §2 zh-CN elevator-maintenance notice, §3 es-ES sailboat charter, §4 pl piano workshop) + 39 sealed questions (26 S, 13 F, 14 two-hop) written by a fresh no-context author after MNC21 was frozen (candidates/mnc21/RULES.md sha1 606cfa5f…, 12:54 CT). Encoding stamped 12:56:47 CT, before the questions were copied into round22/ (encoder never opened round22_sealed/).
Readers: fresh no-context frontier helpers (one reader family; isolation by instruction only). Decode judge: independent no-context helper (originals + 2 decodes only).
facts.json: NOT written this round (the independent judge split the originals into 75 atomic facts itself; see decodes/judgments_mnc21.json). Lint not run.
7B weak reader: queued as a detached job (answers_7b/, mnc21x + original ×3); results not in at write-up → PENDING (see addendum if added later).

## Accuracy vs savings (strong reader; tools2/score.py; overrides listed in answers/overrides.json)
| Text | o200k / cl100k tokens | Saved o200k / cl100k | All | S | Notes |
|---|---|---|---|---|---|
| original | 1541 / 1815 | 0 / 0 | 39/39 (100%) | 26/26 | ×1 |
| **MNC21** (no key) | 1047 / 1071 | 32.1% / 41.0% | 39/39 ×2 (100%) | 26/26 ×2 | no overrides |
| **MNC21x** (aggressive, no key) | 961 / 987 | 37.6% / 45.6% | 39/39 ×2 (100%) | 26/26 ×2 | no overrides; R8 held (§4 fee given as 105 zł) |
| terse English (frontier writer) | 922 / 946 | 40.2% / 47.9% | 39/39 ×2 (100%) | 26/26 ×2 | r1 needed 1 F override (§2.q8 "RMB 3" vs regex "yuan") |
| summarize prompt | 1151 / 1319 | 25.3% / 27.3% | 39/39 (100%) | 26/26 | ×1 |
| LLMLingua-2 0.66 | 1023 / 1209 | 33.6% / 33.4% | 32/39 (82.1%) | 25/26 | ×1; truncated emergency number (604 dropped), lost §2 amounts/deadline |
| LLMLingua-2 0.5 | 779 / 906 | 49.4% / 50.1% | 28/39 (71.8%) | 21/26 | ×1; flipped 3 never-copy rules to "yes", truncated 2 emergency numbers |
Key tokens: 0 (no key), so break-even = 0.

## Blind decode of MNC21, independent judge (75 facts)
A: 1 S distortion (§1 "a mechanic will phone them within one hour" decoded as "the mechanic will phone…", i.e. a specific person — judge: low severity, flagged under the strict rule), 0 S lost, 0 F problems, 0 inventions.
B: clean (0 / 0 / 0 / 0).
R9 held: no invented naming rules this round (r21 had 3). MNC21x was not decoded.

## Instruction safety
Direct use: **PASS** (S 26/26 on all four MNC21/MNC21x runs).
Blind decode: **FAIL (strict)** — 1 low-severity actor distortion in decode A (indefinite "a mechanic" → definite "the mechanic"); B clean.
Round verdict: **FAIL (strict)**. Ready counter (fully blind): r21 FAIL → r22 FAIL → **0/3**.

## Bench-v1 regression control (bench/strong_mnc20, strong reader ×1; NOT blind)
Original-text control now run on the converted 134-question set: original 130/134 (97.0%), S 55/56; MNC20 (from r21) 127/134 (94.8%), S 56/56. Raw regex scores, no overrides on either. MNC21 itself was not run on bench-v1 this round.

## Verdict
Not a new best. MNC21x ties the original, summarize and terse English at 100% with the strong reader and beats both LLMLingua-2 settings on accuracy, but terse English still saves more (40.2% vs 37.6% o200k). The gap narrowed from 9.7 points (r21: 26.8 vs 36.5) to 2.6 points. MNC16x/xx stay the strong-reader best; MNC3 the weak-reader best.

## Addendum (2026-11-18 ~19:05 CT run): 7B weak reader (local Qwen-7B, ×3, raw regex, no overrides)
| Text | r1 | r2 | r3 | S range |
|---|---|---|---|---|
| MNC21x | 24/39 (61.5%) | 23/39 (59.0%) | 24/39 (61.5%) | 13-14/26 |
| original | 23/39 (59.0%) | 0/39 (format failure: dropped "§" from every answer ID) | 23/39 (59.0%) | 16-17/26 |
Spread is about 1 question per text. MNC21x ties the original on All (inside the noise) and is ~3 S questions lower; the 7B is weak on these two-hop scenario questions for every form, original included. Secondary signal only.
