# Round 21 — MNC20 (new: R7 call-number rule) — SCORED 2026-11-18 ~07:45 CT
Label: FULLY BLIND, INDEPENDENT AUTHOR. Originals (§1 en vet clinic, §2 ko everyday notice, §3 pt-BR, §4 tr) + 39 sealed questions (25 S, 14 F; ~1/3 asked in ko/pt/tr) written by a fresh no-context author after MNC20 was frozen (candidates/mnc20/RULES.md sha1 7e52a438…, 07:04 CT). Encoding stamped 07:08:23 CT, questions copied 07:08:28 CT (encoder never opened round21_sealed/).
Readers: fresh no-context frontier helpers (one reader family; isolation by instruction only). Decode judge: independent no-context helper (originals + 2 decodes only). facts.json written by the encoder (lint only).
7B weak reader: NOT RUN (~3 GB RAM available at start; secondary).

## Accuracy vs savings (strong reader; tools2/score.py; overrides = regex false negatives only, listed in answers/overrides.json)
| Text | o200k / cl100k tokens | Saved o200k / cl100k | All | S | Notes |
|---|---|---|---|---|---|
| original | 1561 / 2007 | 0 / 0 | 39/39 (100%) | 25/25 | ×1 |
| **MNC20** (no key) | 1143 / 1196 | 26.8% / 40.4% | 39/39, 39/39 (100% ×2) | 25/25 ×2 | 3 F overrides per run: 24h times (16:00 = 4 p.m., 09:00-16:00, 18:00) vs regex expecting "4"/"6" |
| MNC20x (aggressive, curve) | 917 / 961 | 41.3% / 52.1% | 38/39 ×2 (97.4%) | 24/25 ×2 | §4.q6 FAIL ×2: "half hourly rate 150 TL/hour" read as 75 TL/h → 150 TL instead of 300 TL |
| terse English (frontier writer) | 991 / 1030 | 36.5% / 48.7% | 39/39 (100%) | 25/25 | ×1, no overrides |
| summarize prompt | 1243 / 1492 | 20.4% / 25.7% | 39/39 (100%) | 25/25 | ×1, 2 F overrides (24h times) |
| LLMLingua-2 0.66 | 1054 / 1343 | 32.5% / 33.1% | 37/39 (94.9%) | 24/25 | ×1; lost "must begin with" sentence rule; approval-limit boundary flip |
| LLMLingua-2 0.5 | 814 / 1027 | 47.9% / 48.8% | 30/39 (76.9%) | 21/25 | ×1 |
Key tokens: 0 (no key), so break-even = 0.

## Blind decode, independent judge (decodes/judgments_mnc20.json, 67 facts)
A and B: 1 S distortion each (§4 late-cancellation charge: "half the hourly rate, which is 150 TL per hour" — judge flagged the antecedent as ambiguous, the same misreading MNC20x's reader made), 0 S lost, 1 F lost (closing thank-you line in §2), 3 inventions each (identity form `(="office manager", never "veterinarian")` decoded as an explicit naming rule when the original only says "X is not Y"; judged benign but counted).

## Instruction safety
Direct use: **PASS** (S 25/25 on both MNC20 runs; the R7 call-number fix held — every emergency answer gave the phone number).
Blind decode: **FAIL (strict)** — 1 S distortion (ambiguous derived amount) in both decodes.
Round verdict: **FAIL (strict)**. Ready counter (fully blind): r20 FAIL → r21 FAIL → **0/3**.

## Bench-v1 regression (bench/strong_mnc20, strong reader ×1; NOT blind — encoder had seen these passages)
MNC20 2535 / 3348 o200k (24.3% / 34.8% saved): 127/134 raw (94.8%), S 56/56. 7 F misses, most look like regex false negatives (names kept in kanji, "8:30 Eastern"), not overridden. No original-text control was run on this converted 134-question set, so no comparison claim.

## Verdict
Not a new best. MNC20 ties the original and terse English on accuracy, but terse English saves more (36.5% vs 26.8% o200k). MNC20x saves more than terse English (41.3%) but loses one safety question. MNC16x/xx stay the strong-reader best; MNC3 the weak-reader best.
