# Round 34 scores (2026-11-22, run ~13:18-~13:50 CT) — fully blind, independent author
Texts: originals.txt written by an independent no-context author (en clock & watch repair / zh bathhouse renovation notice / de sailing school / id glass-blowing studio; 2,411 o200k tokens; instruction sections ~400-440 words, longer than r33; distractor rules, Saturday-only limit, type-only limits, "only X may" rules, "never X, unless Y", near-miss numbers, three-rule chains). 40 questions (28 S, 12 F, 15 two-hop, about 1/3 in Chinese/German/Indonesian). questions.json sealed in round34_sealed until both payloads were encoded and hashed (encoded_before_questions.sha1, 13:27:52 CT).
Versions: **MNC28 = main, frozen** (MNC28-RULES.md sha1 f70a3563, identical to rounds 31-33). MNC28x = experimental probe (r33 x form + no repeated names/roles after the who-is-who line, one approver line per person, merged inbox/report lines). Encoder note: the x encoder stopped at 33.1% rather than drop protected facts (target was ≥48%).
Readers: fresh no-context frontier helpers (one reader family; isolation by instruction only). Baselines a/b written by separate no-context helpers. LLMLingua-2 run locally. Decode judge: independent no-context helper (originals + 3 decodes only).
Shared scorer fixes (applied to every text alike; see questions.json "scorer_fixes_r34"): (1) the emergency questions' reject regex "customer ... to call" fired on answers saying "(not ask the customer to call)" — lookbehind added; (2) §2.q4 is a two-part question whose gold was only "no" (the original's first part is "yes, in person"); now accepts "...; no"; (3) §3.q2 asks who approves and the text does not say — a bare "not stated" is counted correct (the scorer otherwise treats bare "not stated" as an abstain). Before the fixes every faithful text, the original included, scored 36-38/40.

## Accuracy vs savings (strong reader)
| Text | o200k tokens (saved) | cl100k (saved) | Direct use all | S (safety) | Runs |
|---|---|---|---|---|---|
| original | 2411 (0) | 2832 (0) | 40/40 100% | 28/28 | 1 |
| **MNC28 main** | 2007 (16.8%) | 2170 (23.4%) | 40/40 ×2 | 28/28 ×2 | 2 |
| MNC28x probe | 1613 (33.1%) | 1651 (41.7%) | 39/40 ×2 (97.5%) | 27/28 ×2 | 2 |
| terse English | 1535 (36.3%) | 1576 (44.4%) | 40/40 ×2 | 28/28 ×2 | 2 |
| summarize | 1896 (21.4%) | 2179 (23.1%) | 40/40 | 28/28 | 1 |
| LLMLingua-2 0.66 | 1614 (33.1%) | 1888 (33.3%) | 33/40 82.5% | 26/28 | 1 |
| LLMLingua-2 0.5 | 1278 (47.0%) | 1485 (47.6%) | 25/40 62.5% | 20/28 | 1 |
MNC28x failure (both runs, a safety miss): §1.q2 Saturday estimate of £125 — readers said "approver not stated" instead of Desmond Pryce. The x payload put "Sat only ≤£120" on the estimate line and moved Desmond to a separate "Desmond must approve: estimates >£180" line, so the Saturday over-limit case lost its link to the approver. Every other text (original, main, terse, summarize) got it right.
LLMLingua failures: 0.66 lost most of the Chinese §2 facts, dropped a word from an exact sentence and missed a §2 rule; 0.5 also copied the bookkeeper on complaints (prohibition flipped), named wrong approvers (§3.q4, §4.q2) and lost a refund amount — instruction-safety failures.
Break-even: no key is used (MNC28/MNC28x run keyless), so savings apply from the first use.

## Blind decode (independent judge, 170 facts: 123 S / 47 F)
- MNC28 A: 170/170 kept, 0 distortions, 0 losses (added only the gloss "a sailing school" for Segelschule).
- MNC28 B: 170/170 kept, 0 distortions, 0 losses (same gloss).
- MNC28x A: 167/170 kept; **1 S distortion** (§4: hotel/restaurant orders over 30 pieces need Ratna's approval for the order itself; x's merged approver line says she approves "any discount on" them) + 2 F losses (business descriptors). Encoder-caused by the new "one approver line per person" merge.
**Instruction-safety, main MNC28: PASS** (0 S errors across direct use ×2 and decode ×2). MNC28x: FAIL (1 S direct-use miss ×2, 1 S decode distortion).

## Weak reader (local Qwen-7B, 3 runs each)
MNC28 62.5-65.0% (S 67.9% all runs), original 50.0-52.5% (S 50.0-53.6%) — MNC28 above the original's range on all 3 runs (weak-reader gain outside the spread, second round running). MNC28x 57.5% on its one complete run; runs 1 and 3 stopped after 10 of 40 answers (15.0%) — 7B output truncation, counted as scored, not re-run.

## Ready counter
**MNC28: 4 consecutive fully blind passes** (rounds 31-34, same RULES sha1 f70a3563, 100% instruction-safety each); the 3/3 bar was first met in round 33.

## Verdict
Not a new best on savings: terse English saves 19.5 points (o200k) more than MNC28 main at equal accuracy, and beats MNC28x by 3.2 points at higher accuracy. The new x merges (one approver line per person) caused safety errors — rejected. Bench-v1 not run this round. Longer instruction sections did not break the ceiling for faithful texts.
