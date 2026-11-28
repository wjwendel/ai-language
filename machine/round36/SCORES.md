# Round 36 scores (2026-11-28, run ~00:56-~01:30 CT) — fully blind, independent author
Texts: originals.txt written by an independent no-context author (en hat-making workshop / ko neighborhood seed library spring lending notice / pt-BR artisanal cheese shop / hi typewriter repair shop; 3,534 o200k tokens; instruction sections longer than r35, ~560-650 words requested; distractor rules, two refund types with different self-approval limits and over-limit rules, unnamed approvers, definite-role identity rules, noun-specific definitions, day-only and customer-group rules, "never X, unless Y", near-miss numbers, three-rule chains). 38 questions (24 S, 14 F, 22 two-hop, ~14 in Korean/Portuguese/Hindi). questions.json sealed in round36_sealed until both payloads were encoded and hashed (encoded_before_questions.sha1, 01:03:48 CT; questions copied right after).
Versions: **MNC28 = main, frozen** (MNC28-RULES.md sha1 f70a3563, identical to rounds 31-35). MNC28x = experimental probe (r35 x + definite-article role negations "THE owner, NOT THE head milliner" + every definition keeps its noun). See MNC28x-R36-NOTE.md.
Readers: fresh no-context frontier helpers, payload + questions only (one reader family; isolation by instruction only). Baselines a/b written by separate no-context helpers. LLMLingua-2 run locally. Decode judge: independent no-context helper (originals + 4 decodes only).
Scorer changes (applied to every text alike): (1) tools2/score.py now counts a bare "not stated" as an answer, not an abstain, when the gold itself says "not stated" (r35 fix-list item; affects §1.q2, §3.q4, §4.q2). (2) answers/overrides.json: §2.q8 accept regex missed "2F" (standard abbreviation of 2nd floor / 2층); 4 answers using "2F" (MNC28x ×2, terse ×2) counted correct. Before fix (2), MNC28x ×2 and terse ×2 scored 37/38.

## Accuracy vs savings (strong reader)
| Text | o200k tokens (saved) | cl100k (saved) | Direct use all | S (safety) | Runs |
|---|---|---|---|---|---|
| original | 3534 (0) | 6276 (0) | 38/38 100% | 24/24 | 1 |
| **MNC28 main** | 2769 (21.6%) | 3230 (48.5%) | 38/38 ×2 | 24/24 ×2 | 2 |
| MNC28x probe | 2134 (39.6%) | 2318 (63.1%) | 38/38 ×2 | 24/24 ×2 | 2 |
| terse English | 2045 (42.1%) | 2156 (65.6%) | 38/38 ×2 | 24/24 ×2 | 2 |
| summarize | 2571 (27.2%) | 4294 (31.6%) | 38/38 | 24/24 | 1 |
| LLMLingua-2 0.66 | 2313 (34.6%) | 4185 (33.3%) | 35/38 92.1% | 24/24 | 1 |
| LLMLingua-2 0.5 | 1780 (49.6%) | 3211 (48.8%) | 34/38 89.5% | 23/24 | 1 |
Terse English beat MNC28x by 89 o200k / 162 cl100k tokens (2.5 / 2.5 points) at the same 38/38 ×2 — the r35 x win over terse did not repeat.
LLMLingua failures: both ratios lost the Korean seed limit (§2.q1 "not stated") and flipped the Korean scope test (§2.q2/q3: the "before Mar 10" qualifier applied to the wrong noun); 0.5 also answered "Mehra (the owner)" for the ₹1,501 repair refund (ambiguous: the text has two Mehras; S fail).
Break-even: no key (MNC28/MNC28x run keyless), so savings apply from the first use.

## Blind decode (independent judge, 213 facts: 126 S / 87 F)
- MNC28 A: 212/213 kept; 0 S errors; 1 F distortion (§2 "spring operation starts this year" decoded as "opens for the first time this spring" — decoder-side; payload says 올해 봄 운영 시작).
- MNC28 B: 212/213 kept; 0 S errors; same F distortion; 3 accurate added notes ("approver not named").
- MNC28x A: 209/213 kept; **0 S errors**; 3 F losses ("small" dropped from the business descriptions in §1/§3/§4 — encoder cut) + 1 F distortion (§1 order confirmations "should start" decoded as "must start" — encoder dropped "should"; the judge marked it F, but it is a modality strengthening and is treated here as a near-miss).
- MNC28x B: same as A, plus 3 accurate "approver not named" notes.
The r35 x slips are fixed: definite role negations ("THE head milliner, NOT THE owner") and noun-specific definitions (bespoke vs repair "express"; manual vs electric "full servicing") decoded exactly in both x decodes.
**Instruction-safety, main MNC28: PASS** (0 S errors across direct use ×2 and decode ×2). MNC28x: 0 S errors in direct use ×2 and decode ×2, but a modality change (should → must) from a terse cut, so not a clean decode.

## Weak reader (local Qwen-7B, 3 runs each)
Pending at write-up: the detached queue (queue7b.sh → answers_7b/keep/) was still running (MNC28 run 1 done). Results to be scored in the next round. The original is 6,276 cl100k tokens, so its 7B prompt may hit the 8,192-token context; truncation will be reported, not hidden.

## Ready counter
**MNC28 (RULES sha1 f70a3563): 6 consecutive fully blind passes (r31-r36); ready bar (3/3) met since r33.** MNC28x not promoted (lost savings to terse; decode not clean), so the counter is unchanged.
Bench-v1: not run this round.

## Weak reader update (scored 2026-11-28 ~04:25 CT in the round-37 run)
Queue finished 01:35 CT, all 9 runs complete. MNC28 81.6% ×3 (S 91.7-95.8%), original 63.2-68.4% (S 62.5-70.8%), MNC28x 63.2-71.1% (S 70.8-79.2%). MNC28 is above the original on every run, outside the spread; MNC28x overlaps the original (tie). No truncation observed (original prompt 7,349 tokens; completions ~490).
