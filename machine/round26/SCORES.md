# Round 26 — MNC25 (MNC24 + R18 role word in header, R16b keep descriptors, R19 savings) — SCORED 2026-11-19 ~13:10 CT
Label: FULLY BLIND, INDEPENDENT AUTHOR. Originals (§1 en furniture upholsterer, §2 ja city-library year-end schedule, §3 fr ceramics studio, §4 tr rooftop solar installer) + 39 sealed questions (25 S, 14 F, 16 two-hop) written by a fresh no-context author (round26_sealed/AUTHOR-R26.md) after MNC25 was frozen (candidates/mnc25/RULES.md sha1 efaaeee4…, 12:59 CT). Encodings stamped before questions.json was copied into round26/ (encoded_before_questions.sha1); the encoder never opened the sealed questions before stamping.
Readers: fresh no-context frontier helpers (one reader family; isolation by instruction only). Decode judge: independent no-context helper (originals + 2 decodes only).
facts.json: NOT written (the judge split the originals into 119 atomic facts, 78 S; decodes/judgments_mnc25.json).
Scorer: tools2/score.py now CJK-safe (digit lookarounds instead of `\b`).

## Accuracy vs savings (strong reader)
Raw regex → reviewed (answers/overrides.json). One shared review: §1.q2 gold says Marta Quill approves cushion quotes over $350, but the original only says "anything above $350 needs approval" without naming the approver; the original-text reader also answered "approver not stated". Every answer that said "needs approval, approver not stated" is reviewed as correct for every text; an answer that names a specific approver other than Marta is reviewed wrong. Other reviews are time-format regex false negatives ("3:00 p.m.", "16h") and 佐伯美穂 vs "Saeki".
| Text | o200k / cl100k tokens | Saved o200k / cl100k | All raw → reviewed | S reviewed | Notes |
|---|---|---|---|---|---|
| original | 1553 / 1920 | 0 / 0 | 36 → 39/39 | 25/25 | ×1 |
| MNC25 (main, no key) | 1062 / 1101 | 31.6% / 42.7% | 38, 37 → 39/39 ×2 | 25/25 ×2 | |
| MNC25x (aggressive, no key) | 978 / 1016 | **37.0% / 47.1%** | 36, 38 → 38/39, 39/39 | **24/25**, 25/25 | run 1 named Lena Harlow (owner) as approver for cushion quotes > $350: an invented actor (the original names none). Real S error. |
| terse English (frontier writer) | 1015 / 1047 | 34.6% / 45.5% | 38 → 39/39 ×2 | 25/25 ×2 | clean this round |
| summarize prompt | 1270 / 1521 | 18.2% / 20.8% | 38 → 39/39 | 25/25 | ×1 |
| LLMLingua-2 0.66 | 984 / 1209 | 36.6% / 37.0% | 32 → 34/39 (87.2%) | 23/25 | ×1; lost the Japanese due-date extension + CD/DVD rule, the 9,000 TL deposit amount, the inverter emergency step |
| LLMLingua-2 0.5 | 787 / 969 | 49.3% / 49.5% | 28 → 29/39 (74.4%) | 19/25 | ×1; also flipped two permission/prohibition answers (§1.q8, §3.q8 "yes" instead of "no") |
Key tokens: 0 (no key), break-even = 0.
Curve (o200k saved → strong-reader accuracy, mean of runs): summarize 18.2%→100%; MNC25 31.6%→100%; terse 34.6%→100%; LLMLingua 0.66 36.6%→87.2%; MNC25x 37.0%→98.7% (one S slip); LLMLingua 0.5 49.3%→74.4%.
Honest read: on this set terse English matches MNC25 on accuracy and saves 3 points more. MNC25x saves 2.4 points more than terse but had one invented-actor answer in 1 of 2 runs. The §1 "needs approval" with no named approver is a gap in the original that the aggressive form tempted the reader to fill (the owner line sits right above it).

## Blind decode of MNC25 (main form), independent judge (119 facts, 78 S)
- A: 119/119 kept, 0 distorted, 0 lost, 0 added.
- B: 119/119 kept, 0 distorted, 0 lost, 0 added.
R18 (role word in header) fixed the round-25 "You are working for" items; R16b kept "furniture upholsterer", "ceramics studio", "rooftop solar panel installer", "shared inbox". The Japanese one-noun qualifier (magazines borrowed Dec 15 or later; kamishibai any date) held in every MNC run and both decodes.

## Instruction safety
MNC25 (main form): direct use S 25/25 ×2, both blind decodes clean → **PASS**. First clean main-form round since r18.
MNC25x (aggressive probe): 1 invented-actor answer → would FAIL; it is not the main form.
Ready counter (fully blind, main form, 3 consecutive): r24 FAIL → r25 FAIL → **r26 PASS → 1/3**.

## Bench-v1
Not run this round (bench-v1 is at ceiling for the strong reader; r25 showed MNC24 ≈ MNC16x ≈ original). No new-best claim is possible without it, and terse English already matches MNC25 on the fresh set.

## 7B weak reader (secondary)
round26/queue7b.sh (MNC25x + original ×3) started 13:04 CT as a detached job; PENDING at write-up — score next run with `ANS=answers_7b python3 tools2/score.py round26`.

## Verdict
Not a new best. Main form MNC25 is safety-clean (direct use + both decodes), so the ready counter moves to 1/3, but terse English matches it at 3 points more savings on this set. MNC16x/xx stay the strong-reader best; MNC3 the weak-reader best.
