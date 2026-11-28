# Round 37 scores (2026-11-28, run ~03:52-~04:30 CT) — fully blind, independent author
Texts: originals.txt written by an independent no-context author (en harp workshop / zh residential e-bike charging-shed registration notice / fr and vi small-business assistant instructions; 3,089 o200k / 4,027 cl100k tokens; instruction sections 560-650 words requested, distractor rules, three-rule chains, near-miss numbers, definite-role identity rules, noun-specific definitions, a deliberate "should" (recommended, not required) rule). **59 questions** (43 S, 16 F, 28 two-hop; larger set than r36's 38, per the r36 fix list). questions.json sealed in round37_sealed until both payloads were encoded and hashed (encoded_before_questions.sha1), then copied.
Versions: **MNC28 = main, frozen** (MNC28-RULES.md sha1 f70a3563, identical to rounds 31-36). MNC28x = experimental probe with a structural change: a shared §0 slot-schema key used by all three instruction sections (one line order + templates defined once), should/may/must kept exactly, "small" kept. See MNC28x-R37-NOTE.md. Both encoded by encoder helpers from originals.txt only (never saw questions).
Readers: fresh no-context frontier helpers, payload + questions only (one reader family; isolation by instruction only). Baselines a/b written by separate no-context helpers. LLMLingua-2 run locally. Decode judge: independent no-context helper (originals + 4 decodes only). No scorer overrides this round.

## Accuracy vs savings (strong reader)
| Text | o200k tokens (saved) | cl100k (saved) | Direct use all | S (safety) | Runs |
|---|---|---|---|---|---|
| original | 3089 (0) | 4027 (0) | 59/59 100% | 43/43 | 1 |
| **MNC28 main** | 2566 (16.9%) | 2830 (29.7%) | 59/59 ×2 | 43/43 ×2 | 2 |
| MNC28x probe | 2190 (29.1%) | 2274 (43.5%) | 59/59 ×2 | 43/43 ×2 | 2 |
| terse English | 1980 (35.9%) | 2077 (48.4%) | 58/59 ×2 (98.3%) | 42/43 ×2 | 2 |
| summarize | 2249 (27.2%) | 2819 (30.0%) | 59/59 | 43/43 | 1 |
| LLMLingua-2 0.66 | 1983 (35.8%) | 2638 (34.5%) | 52/59 88.1% | 38/43 | 1 |
| LLMLingua-2 0.5 | 1543 (50.0%) | 2033 (49.5%) | 48/59 81.4% | 36/43 | 1 |
Terse English failed the Chinese scope test in both runs (§2.q2, S): the original limits "bought after March 1" to e-tricycles only (电动自行车和3月1日以后购买的电动三轮车); the terse writer wrote "e-bikes and e-tricycles bought after March 1", so both readers said a January e-bike is not covered (gold: yes). This is the first round in several where a faithful-looking baseline lost a safety question; it is one question on one text, so treat it as a real but narrow failure, not a broad result.
Among texts at 59/59, MNC28x saved the most (29.1% o200k), ahead of summarize (27.2%) and MNC28 main (16.9%); terse English saved 6.8 points more than x but at 58/59.
The original was already compact in o200k (Chinese/French/Vietnamese), so every faithful form saved less than in r36. MNC28x's §0 key costs ~161 o200k tokens; over three sections it barely pays for itself (encoder note).
LLMLingua failures: both ratios lost the Chinese scope/eligibility facts (§2.q2/q3/q5/q13), gave a wrong charging cut-off (§2.q11), named an unstated approver in Vietnamese §4.q7 (S), and mishandled the "should" (recommended) rule (§1.q15); 0.5 also lost the ¥20 deposit and a Vietnamese amount.
Break-even: no key for MNC28 (keyless); MNC28x carries its own in-payload §0 key, already counted in its tokens.

## Blind decode (independent judge, 189 facts: 128 S / 61 F)
- MNC28 A: 189/189 kept; 0 S / 0 F errors (harmless framing only).
- MNC28 B: 189/189 kept; 0 S / 0 F errors.
- MNC28x A: 188/189; **1 S distortion** — §1 "when a customer asks for a string chart" decoded as "if someone requests" (widens who the permission covers). Encoder-caused: the x payload line reads "string chart request: may attach..." and dropped "customer".
- MNC28x B: same 1 S distortion.
- Judge note: all four decodes rendered the Chinese scope as "electric bicycles and electric tricycles purchased after March 1" (ambiguous English); the judge marked it kept since none changes the meaning outright. For MNC28 the payload keeps §2 in Chinese, so this is decoder wording; flagged as a watch item.
**Instruction-safety, main MNC28: PASS** (0 S errors across direct use ×2 and decode ×2). MNC28x: 100% direct use ×2 but 1 S decode distortion → strict gate FAIL, not promoted.

## Weak reader (local Qwen-7B, 3 runs each)
Pending at write-up: detached queue (queue7b.sh → answers_7b/keep/) started ~04:20 CT. To be scored next round.

## Round 36 weak-reader results (scored this run; r36 queue finished 01:35 CT)
MNC28 81.6% ×3 (S 91.7-95.8%), original 63.2-68.4% (S 62.5-70.8%), MNC28x 63.2-71.1% (S 70.8-79.2%). MNC28 is 5-7 questions above the original on every run (outside the spread); MNC28x overlaps the original → tie. Original prompt was 7,349 tokens on the 8,192 context; completions (~490 tokens) fit, so no truncation was observed.

## Ready counter
**MNC28 (RULES sha1 f70a3563): 7 consecutive fully blind passes (r31-r37); ready bar (3/3) met since r33.** MNC28x not promoted (does not beat terse on savings; decode not clean), so the counter is unchanged.
Bench-v1: not run this round.

## Verdict
Not a new best by the promotion rule (x lost savings to terse and failed the decode gate; bench-v1 not run). Honest summary: MNC28 main and MNC28x both held 100% on the strong reader where terse English slipped one Chinese scope question, but terse English still saved more tokens.

