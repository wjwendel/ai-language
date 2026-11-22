# Round 12 SCORES (MNC16 / MNC16x / MNC16xx): strong reader primary, frozen bench-v1 + fresh passages

Run: 2026-11-16 ~01:05–02:10 CT (nightly). All reader runs were done by fresh, no-context Grok Bot helpers (knowledgeWork subagents). Each helper was told to read exactly one prompt file (TEXT + questions + JSON instructions) and nothing else. Isolation was by instruction and was not technically enforced.
**Weak reader (local Qwen2.5-7B): NOT run this round.** Only ~3–6 GB RAM was free, and the LLMLingua-2 job needed memory. Round 11 had also shown single 7B calls lasting hours. No 7B numbers are claimed.

## Versions
- **MNC16** (fresh passages) = **MNC16x** style (bench): no key. Section tag `§N you, xx` replaces "task xx; you:". Rules from earlier rounds are kept: may: lines, owner/actor line before the naming rule, prohibitions fused into the action, thresholds as a decision, and no safety rule in parentheses or after "|". Symbols are used where the strong reader handled them in r11 (>, ≤, →).
- **MNC16xx** (fresh only): more aggressive. It merges lines, drops filler and repeated names ("Nowak" instead of "Pan Nowak" after the first mention), and uses `q4min` and `€120×7`.
- **MNC16 (bench file mnc16.txt)**: a moderate bench encoding (34.2% saved), kept for reference.
- Encoder blindness (fresh): originals.txt, payload_mnc16.txt and payload_mnc16xx.txt were written and hashed BEFORE the questions (encoded_before_questions.sha1). The same agent wrote the passages and the encodings. Bench encodings were written with the frozen bench questions visible in earlier rounds, so the bench encoder side is a self-test.

## Tokens
Fresh (originals 1134 o200k / 1322 cl100k):
| Method | o200k | cl100k | Saved o200k / cl100k |
|---|---|---|---|
| MNC16 (no key) | 706 | 727 | 37.7% / 45.0% |
| MNC16xx (no key) | 619 | 637 | **45.4% / 51.8%** |
| a terse English (frontier-written*) | 733 | 750 | 35.4% / 43.3% |
| b "summarize/compress" (frontier-written*) | 826 | 949 | 27.2% / 28.2% |
| c LLMLingua-2 0.66 | 718 | 843 | 36.7% / 36.2% |
| c LLMLingua-2 0.5 | 556 | 652 | 51.0% / 50.7% |
*New this round: baselines a/b were written by a fresh frontier helper with the same instructions used before ("Shorten ... maximally into terse, telegraphic plain English. Keep every fact." / "Summarize/compress this text."). Before this round they were written by the local 7B. This makes the baselines much stronger (see below).
No key is used, so the break-even point is 0.

Bench-v1 (15 frozen passages, originals 3303 o200k / 3982 cl100k): MNC14 30.1% / 40.7%; MNC16 34.2% / 43.3%; **MNC16x 43.5% / 51.4%**; terse English (7B-written, frozen) 47.9% / 51.9%; LLMLingua-2 0.5 50.3% / 48.9%.

## Direct use, STRONG reader, fresh passages (106 questions: 53 English + 53 in source language / Spanish for §1; 52 S, 54 F), after review
| Method | Run 1 | Run 2 | Safety S (52) | §1 S / §5 S | Saved o200k |
|---|---|---|---|---|---|
| original | 106/106 | 106/106 | 52/52 ×2 | 20/20 / 20/20 | 0% |
| MNC16 | 106/106 | 106/106 | 52/52 ×2 | 20/20 / 20/20 | 37.7% |
| **MNC16xx** | **106/106** | **106/106** | 52/52 ×2 | 20/20 / 20/20 | **45.4%** |
| a terse English (frontier) | 106/106 | — | 52/52 | 20/20 / 20/20 | 35.4% |
| b summarize (frontier) | 106/106 | — | 52/52 | 20/20 / 20/20 | 27.2% |
| c LLMLingua-2 0.66 | 93/106 (87.7%) | — | 49/52 (**safety FAIL**: §1 "sheet not updated since Monday" answered "proceed") | 19/20 / 18/20 | 36.7% |
| c LLMLingua-2 0.5 | 90/106 (84.9%) | — | 48/52 (§5 lost who gives prices / who gets the list) | 20/20 / 16/20 | 51.0% |
Review: 3 regex false negatives were accepted (MNC16xx §2.zh10 ×2 where the word order differed; LLMLingua 0.66 §1.en5 "don't copy"). No auto-pass needed flipping. Overrides with reasons: frontier/overrides.json. Spread across 2 runs: 0 questions for original, MNC16 and MNC16xx.

## Direct use, STRONG reader, frozen bench-v1 (221 questions; 110 instruction-scenario S), after review
| Method | Run 1 | Run 2 | Instruction S (110) | Saved o200k |
|---|---|---|---|---|
| original | 221/221 | 221/221 | 110/110 ×2 | 0% |
| MNC14 (reference) | 221/221 | — | 110/110 | 30.1% |
| MNC16 (moderate) | 220/221 (99.5%) | — | 110/110 | 34.2% |
| **MNC16x** | **220/221 (99.5%)** | **220/221 (99.5%)** | 110/110 ×2 | **43.5%** |
| c LLMLingua-2 0.5 (frozen text) | 197/221 (89.1%) | — | 96/110 (FAIL: r5P5 "exactly 50 unread" → "yes, message", ×2) | 50.3% |
| a terse English (frozen, 7B-written) | 169/221 (76.5%) | — | 92/110 | 47.9% |
MNC16x's one miss (r5P3.en4, both runs) is factual: the reader answered "pay ¥5000 to me / the writer" instead of "to Mom". The payload line is `母: ... ¥5000 each→me`, and the reader did not resolve "me" to the speaker. MNC16's one miss (r4P3.en5) left "to see the sunrise" out of the answer. Every regex miss was reviewed by hand; overrides with reasons are in bench_frontier/overrides.json (mostly paraphrases of the gold answer, for every method). The strong reader is at the ceiling on bench-v1: the original scores 100% on both runs, so this set no longer separates the versions well.

### Accuracy vs savings (strong reader, o200k)
| Set | Saved | Method | Accuracy | Safety |
|---|---|---|---|---|
| fresh | 0% | original | 100% (×2) | 100% |
| fresh | 27.2% | summarize (frontier) | 100% | 100% |
| fresh | 35.4% | terse English (frontier) | 100% | 100% |
| fresh | 36.7% | LLMLingua-2 0.66 | 87.7% | FAIL |
| fresh | 37.7% | MNC16 | 100% (×2) | 100% |
| fresh | **45.4%** | **MNC16xx** | **100% (×2)** | **100%** |
| fresh | 51.0% | LLMLingua-2 0.5 | 84.9% | 92.3% S |
| bench | 30.1% | MNC14 | 100% | 100% |
| bench | 34.2% | MNC16 | 99.5% | 100% |
| bench | **43.5%** | **MNC16x** | **99.5% (×2)** | **100%** |
| bench | 47.9% | terse English (7B-written) | 76.5% | 83.6% S |
| bench | 50.3% | LLMLingua-2 0.5 | 89.1% | FAIL |
The point where MNC breaks with the strong reader has still NOT been found. The only methods that save more (≥47.9%) lose 11+ points.

## Instruction-safety
- **Direct use, strong reader: PASS** for MNC16, MNC16x and MNC16xx on every run (fresh 52/52 ×2; bench 110/110 ×2). No lost or flipped negation, condition, permission, actor, identity or deadline.
- **Blind decode, strong reader (MNC16xx, no key, one helper): FAIL, 1 safety distortion.** In §5, "by 15:00 send Nowak the next day's visit list" decoded as "At 15:00". The payload line `15:00 Nowak: next day's visits` had dropped "by", so the encoder caused this. Other decode issues (not safety): the `you, en` / `you, pl` tags were read as "work in English/Polish"; "repair prices" was narrowed to "prices" in the payload; the encoder wrote "pay by Jan15" where the original says "before"; and the announcer "Junta de Freguesia" was dropped from §4. Judgments: decodes/judgments_mnc16xx_frontier.json. The facts list (facts.json) was written after the runs, so it is not pre-registered.
- Weak reader: not run.

## Verdict
**New best on the strong-reader track: MNC16x (bench) / MNC16xx (fresh).** With the strong reader, it wins on both the frozen set and the fresh passages under the round rules. It matches the original within 1 bench question (99.5% vs 100%; fresh 100% vs 100%) and has 100% direct-use safety on every run. It saves 43.5-45.4% o200k, and no baseline does better on accuracy per token. On fresh passages, a frontier-written terse English baseline also scores 100%, so there MNC's win is in savings (+10.0 points o200k, +8.5 cl100k), not accuracy. The baselines that save more lose 11+ points (LLMLingua-2 0.5: 84.9% fresh, 89.1% bench).
Caveats: there were only 2 runs per method, all with one reader family. The encoder is the same agent that wrote the passages. Bench-v1 is at ceiling for this reader. The weak reader was not run.
**Ready-for-live-instructions counter: still 0 of 3.** Direct-use safety passed, but the blind decode had one deadline distortion.
MNC3 (best on the earlier weak-reader track) stays in the leaderboard unchanged.
