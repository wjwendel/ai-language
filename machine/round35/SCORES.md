# Round 35 scores (2026-11-27, run ~01:14-~01:50 CT) — fully blind, independent author
Texts: originals.txt written by an independent no-context author (en violin-making & repair workshop / ja school-uniform recycling sale (PTA notice) / es surfboard-shaping workshop / ar knife-sharpening workshop; 2,724 o200k tokens; instruction sections ~470-530 words, longer than r34; distractor rules, two order types with different self-approval limits and over-limit rules, unnamed approvers, day-only and customer-group rules, "never X, unless Y", near-miss numbers, three-rule chains). 40 questions (27 S, 13 F, 16 two-hop, 14 in Japanese/Spanish/Arabic). questions.json sealed in round35_sealed until both payloads were encoded and hashed (encoded_before_questions.sha1, 01:22:17 CT; questions copied 01:22:40 CT).
Versions: **MNC28 = main, frozen** (MNC28-RULES.md sha1 f70a3563, identical to rounds 31-34). MNC28x = experimental probe (r34 per-person approver merge reverted — each over-limit approver back on its limit line; savings from terse-style wording: dropped articles/auxiliaries, "may confirm ≤X; above: ..." slots, no repeated names/roles after the who-is-who line, Japanese §2 as compact English slots). See MNC28x-R35-NOTE.md.
Readers: fresh no-context frontier helpers, payload + questions only (one reader family; isolation by instruction only). Baselines a/b written by separate no-context helpers. LLMLingua-2 run locally. Decode judge: independent no-context helper (originals + 3 decodes only).
Shared scorer fix (applied to every text alike; answers/overrides.json): §1.q3 and §4.q4 ask who must approve; the text says approval is needed without naming the approver (gold: "needs approval, approver not stated"), so a bare "not stated" is counted correct (the scorer otherwise treats bare "not stated" as an abstain). Before the fix, MNC28 ×2, MNC28x ×2, terse r1 and summarize scored 38/40 (95%); original and terse r2 already scored 40/40 (they answered those two questions in words); LLMLingua 0.66 / 0.5 scored 29/40.

## Accuracy vs savings (strong reader)
| Text | o200k tokens (saved) | cl100k (saved) | Direct use all | S (safety) | Runs |
|---|---|---|---|---|---|
| original | 2724 (0) | 4074 (0) | 40/40 100% | 27/27 | 1 |
| **MNC28 main** | 2176 (20.1%) | 2413 (40.8%) | 40/40 ×2 | 27/27 ×2 | 2 |
| MNC28x probe | 1632 (40.1%) | 1714 (57.9%) | 40/40 ×2 | 27/27 ×2 | 2 |
| terse English | 1696 (37.7%) | 1769 (56.6%) | 40/40 ×2 | 27/27 ×2 | 2 |
| summarize | 2089 (23.3%) | 3024 (25.8%) | 40/40 | 27/27 | 1 |
| LLMLingua-2 0.66 | 1634 (40.0%) | 2481 (39.1%) | 30/40 75.0% | 23/27 | 1 |
| LLMLingua-2 0.5 | 1288 (52.7%) | 1960 (51.9%) | 30/40 75.0% | 23/27 | 1 |
MNC28x vs terse: x is 64 o200k / 55 cl100k tokens smaller (+2.4 / +1.3 points saved) at the same 40/40 ×2 — the first round since r30 where the x probe beat terse English on savings at equal strong-reader accuracy.
LLMLingua failures (both ratios): lost most of the Japanese §2 facts (8 of 10 §2 questions answered "not stated" or wrong, incl. 2 S), named an unstated approver (Salma Haddad) on §4.q4, and missed the Friday no-pickup rule (§4.q8) — instruction-safety failures.
Break-even: no key is used (MNC28/MNC28x run keyless), so savings apply from the first use.

## Blind decode (independent judge, 193 facts: 124 S / 69 F)
- MNC28 A: 193/193 kept, 0 distortions, 0 losses (added only an accurate note that the §1 >95-euro rehair and §4 >12-knife household approvers are not named).
- MNC28 B: 193/193 kept, 0 distortions, 0 losses (same note).
- MNC28x A: 191/193 kept; **1 S distortion** (3.19: "NO el shaper" — Andrés is not THE shop's shaper — decoded as "not a shaper", role negation widened) + 1 F distortion (4.10: express defined as same-day delivery decoded as "same-day sharpening"). Both encoder-caused by x's terse cuts (article dropped from a role negation; noun the definition applies to dropped).
**Instruction-safety, main MNC28: PASS** (0 S errors across direct use ×2 and decode ×2). MNC28x: FAIL on the strict gate (1 S decode distortion; direct use 100% ×2).

## Weak reader (local Qwen-7B, 3 runs each)
MNC28 65.0% on all 3 runs (S 70.4%), original 62.5% on all 3 runs (S 66.7%), MNC28x 62.5-65.0% (S 66.7-74.1%). The runs barely vary, so the spreads are narrow: MNC28 is 1 question above the original on every run (a small margin, not a robust gain); MNC28x overlaps both → tie. No 7B run answered a bare "not stated" on §1.q3 / §4.q4 (every run named an approver, e.g. Salma Haddad on §4.q4), so the shared override changed no 7B score (answers_7b/overrides.json is empty). All 9 runs complete (40/40 answers; max_tokens 3500).

## Ready counter
**MNC28: 5 consecutive fully blind passes** (rounds 31-35, same RULES sha1 f70a3563, 100% instruction-safety each); the 3/3 bar was first met in round 33.

## Verdict
Not a formal new best. MNC28x saved more than terse English at equal strong-reader accuracy (+2.4 points o200k, +1.3 cl100k) but failed the strict decode gate (1 S distortion) and bench-v1 was not run, so it is not promoted. MNC28 main stays the ready reference but saves 17.6 points (o200k) less than terse English. Questions at ceiling again for every faithful text (after the shared fix) even with ~470-530-word instruction sections.
