# Round 32 scores (2026-11-21, run ~13:18-13:50 CT) — fully blind, independent author
Texts: originals.txt written by an independent no-context author (en home-organizing service / ja neighbourhood disaster-drill notice / es self-service laundromat / tr carpet washing; 1,946 o200k tokens; distractor rules, day-only and group-only rules, "only X may" rules, "never X unless Y", type-only self-approval limits, near-miss numbers and three-rule chains requested). 40 questions (27 S, 13 F, 14 two-hop, about 1/3 in Japanese/Spanish/Turkish). questions.json sealed in round32_sealed until both payloads were encoded and hashed (encoded_before_questions.sha1).
Versions: **MNC28 = main, frozen** (MNC28-RULES.md sha1 f70a3563, identical to round 31). MNC28x = experimental probe (bare "you" headers, short approval phrasing, '/' units, everyday Japanese §2 rendered as compact English slots with people's names kept in kanji).
Readers: fresh no-context frontier helpers (one reader family; isolation by instruction only). Baselines a/b written by separate no-context helpers. Decode judge: independent no-context helper (originals + 2 decodes only).
Scorer changes (applied to all texts alike): one shared regex fix (approver-not-stated questions §1.q2/§3.q3 now also accept "does not state"); two scorer overrides on original_r1 only (§2.q4 and §3.q6: bare "no" is the correct answer to what was asked; the regex also wanted extra detail). Without the overrides the original scores 38/40.

## Accuracy vs savings (strong reader)
| Text | Saved o200k / cl100k | Direct use, all (S) |
|---|---|---|
| MNC28 (main, no key) | 24.7% / 31.5% | 100% ×2 (S 27/27 ×2) |
| MNC28x (probe, no key) | 36.8% / 47.5% | 100% ×2 (S 27/27 ×2) |
| original | 0 | 100% ×1 (with 2 overrides; 95% strict) |
| terse English | 39.0% / 49.3% | 100% ×2 |
| summarize | 26.0% / 28.0% | 100% ×1 |
| LLMLingua-2 0.66 | 43.7% / 44.9% | 77.5% ×1 (S 27/27; lost most of the Japanese section, F 4/13) |
| LLMLingua-2 0.5 | 54.8% / 55.8% | 70.0% ×1 (S 23/27 — **safety failures**: invented approvers on §1.q5 and §3.q3, dropped "team on the way" in the §4 emergency step) |
Curve: every faithful text (MNC28, MNC28x, terse, summarize) sits at 100% up to 39% savings; above that only LLMLingua was tested and it loses facts (0.66) and safety (0.5). The question set is still at ceiling for faithful texts, so the curve cannot separate them.

## Instruction-safety
MNC28 S 27/27 ×2; blind decode (2 decodes, independent judge, 147 facts: 105 S, 42 F): A and B kept 147/147, 0 distorted, 0 lost, 0 added. **PASS.**

## Weak reader (local Qwen2.5-7B Q4_K_M, secondary, 3 runs each)
MNC28 45.0 / 55.0 / 57.5%; MNC28x 52.5 / 50.0 / 50.0%; original 50.0 / 47.5 / 45.0%. Spreads overlap: ties.

## Ready counter
Main form unchanged (sha1 f70a3563) and round 32 passed: **MNC28: 2/3**. MNC26 keeps its earlier 3/3 as reference.

## Verdict
Not a new best. Terse English saved the most of any text at 100% (39.0% / 49.3%); MNC28x was close (−2.2 o200k, −1.8 cl100k); MNC28 main saved 14.3 points less than terse on o200k. Bench-v1 not run this round.
