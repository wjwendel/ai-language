# Round 23 — MNC22 (new: R10 indefinite actors, R11 cut predictable framing) — SCORED 2026-11-18 ~19:15 CT
Label: FULLY BLIND, INDEPENDENT AUTHOR. Originals (§1 en print shop, §2 ja neighborhood autumn-festival notice, §3 it pastry shop, §4 sv climbing gym) + 40 sealed questions (27 S, 13 F, 18 two-hop) written by a fresh no-context author (round23_sealed/AUTHOR-R23.md) after MNC22 was frozen (candidates/mnc22/RULES.md sha1 ba71eb3c…, 19:00 CT). Encodings stamped 19:03 CT (encoded_before_questions.sha1) before questions.json was copied into round23/; the encoder never opened round23_sealed/questions.json.
Readers: fresh no-context frontier helpers (one reader family; isolation by instruction only). Decode judge: independent no-context helper (originals + 2 decodes only).
facts.json: NOT written (the judge split the originals into 63 atomic facts; decodes/judgments_mnc22x.json). Lint not run.
7B weak reader: queued as a detached job (queue7b.sh → answers_7b/, mnc22x + original ×3); not in at write-up → PENDING.

## Accuracy vs savings (strong reader; tools2/score.py, raw regex, NO overrides on any file)
| Text | o200k / cl100k tokens | Saved o200k / cl100k | All | S | Notes |
|---|---|---|---|---|---|
| original | 1542 / 1810 | 0 / 0 | 40/40 (100%) | 27/27 | ×1 |
| **MNC22** (no key) | 1003 / 1043 | 35.0% / 42.4% | 40/40 ×2 (100%) | 27/27 ×2 | |
| **MNC22x** (aggressive, no key) | 983 / 1023 | 36.3% / 43.5% | 40/40 ×2 (100%) | 27/27 ×2 | |
| terse English (frontier writer) | 937 / 963 | 39.2% / 46.8% | 40/40 ×2 (100%) | 27/27 ×2 | |
| summarize prompt | 1200 / 1376 | 22.2% / 24.0% | 40/40 (100%) | 27/27 | ×1 |
| LLMLingua-2 0.66 | 887 / 1017 | 42.5% / 43.8% | 28/40 (70.0%) | 24/27 | ×1; reduced the Japanese §2 to 83 tokens (all §2 facts lost); flipped Victor/Jonas "never contact" to "yes"; quoted sentences truncated |
| LLMLingua-2 0.5 | 717 / 825 | 53.5% / 54.4% | 22/40 (55.0%) | 19/27 | ×1; same §2 loss; flipped 2 never-contact rules; emergency number truncated (§3 "812 5530") |
Key tokens: 0 (no key), so break-even = 0.

## Blind decode of MNC22x (the more aggressive form), independent judge (63 facts)
A: 0 S distortions, 0 S lost, 0 F problems.
B: **1 S distortion** — §3 `above €80: needs Chiara's approval` decoded as "Any order above €80 needs Chiara's approval" (approval scope widened from custom-cake orders to all orders).
Both decodes reproduced the encoder-added derived figure "337.50 kr for the intro course"; the judge lists it as added content not stated in the original (arithmetic correct, behaviour unchanged). This is an encoding addition from R8, not a decoder invention.

## Instruction safety
Direct use: **PASS** (S 27/27 on all four MNC22/MNC22x runs).
Blind decode: **FAIL (strict)** — decode B widened an approval threshold's scope.
Round verdict: **FAIL (strict)**. Ready counter (fully blind): r21 FAIL → r22 FAIL → r23 FAIL → **0/3**.

## Bench-v1
Not run this round (time kept for the fresh blind round).

## Verdict
Not a new best. MNC22/MNC22x tie the original, terse English and summarize at 100% with the strong reader and beat both LLMLingua-2 settings by 30-45 points on accuracy, but terse English still saves more (39.2% vs 36.3% o200k; gap 2.9 points, r22: 2.6). R11 framing cuts did not move savings on new text (MNC22x 36.3% vs MNC21x 37.6% on r22). MNC16x/xx stay the strong-reader best; MNC3 the weak-reader best.
