# Round 11 NOTES (MNC15, plus aggressive variants MNC15x / MNC15xx)

## What changed
- MNC15 = MNC14 rules (decision-shaped thresholds "only if more than N", answer-shaped identity "director: Ana Torres, not Marcus", "copy" spelled out, "without X" fusion, may: lines) on fresh passages en/es/ja/it/nl.
- New this write-up (strategy change of 2026-11-14): strong no-context frontier reader as the primary reader. Two aggressive no-key variants test token savings: MNC15x (−56 o200k vs MNC15; symbols ">40", "<3", "=", arrows, dropped filler) and MNC15xx (−110; "<16", "€310k", "q20min", "75→60", "-30%", merged lines).

## Holes found
1. **The 7B was the bottleneck, not the notation.** On the strong reader, MNC15+key scored 100% and MNC15x/xx 97.9% with 100% safety. On the 7B, symbolic thresholds and actor lines failed for six rounds. Symbols (">40", "<3", "<16") that broke the 7B worked on the strong reader in every case tested.
2. **The key is a large fixed cost and may be unnecessary for a strong reader:** 134 tokens (break-even ~400 original tokens). The no-key variants lost nothing on safety. Test no-key MNC on bench-v1 next.
3. **Remaining strong-reader misses are answer-completeness, not payload loss.** §5 q1: the reader answered "the appointment mailbox" without the shop name, which is in the payload. Putting the name right next to "mailbox" ("De Snelle Spaak appointment mailbox") may fix this at zero cost.
4. **Weak-reader blind decode still distorts numbers in conditions** (no key: "more than 40" → "more than four"; "more than 15" → "vanaf 15"). Accept this as a 7B limit for now, but keep it as a secondary check.
5. **Baselines collapse on the strong reader** mainly because they drop content: terse English lost the copy/naming rules and the bus route, and LLMLingua-2 garbled §5 so the reader said Joost "is copied". Their savings come from deleting facts. MNC's come from re-encoding them.
6. **Harness:** the 2026-11-14 queue finished at 08:14 but nobody wrote it up (the run stopped). The original §5 7B call ran 5.3 h (18,984 s) despite caps; llm.py's wall cap is not enforced on QA calls. Frontier helpers took ~1-2 min each, which is much faster than the 7B.

## Next-round fix list (baseline-won metrics first)
1. **Tokens:** terse English still saves more (47.8% vs MNC15xx 43.8% o200k) but scores 24.5 points lower. Push further to find where strong-reader accuracy breaks: MNC15xxx at ~50-55% (drop source-language duplicates, compress §2/§4 news to slot lines, drop "task xx; you:" headers if the reader still treats them as orders).
2. **Gate for a new best:** run MNC15xx (no key) and the original on frozen bench-v1 with 1-3 fresh strong-reader helpers each, plus MNC8/MNC14 for reference. Bench questions are in bench/; build the frontier prompts the same way as round11/tools/qaprompt.py.
3. **Noise:** run each frontier method at least 2× (different helper) and report the spread. Run 7B checks 3× only when RAM ≥6 GB.
4. **Blind round:** build round 12 fresh passages and encode MNC15xx-style BEFORE writing questions, so the encoder is blind. Count toward the 3-round ready bar only with the strong reader at 100% safety in both direct use and blind decode.
5. Pending: fact-by-fact scoring of round-11 7B decodes; LLMLingua-2 0.5 baseline; strong-reader blind decode.
