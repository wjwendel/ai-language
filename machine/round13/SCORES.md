# Round 13 SCORES (MNC17 / MNC17x / MNC17xx): strong reader primary, fresh passages; blind decode ×2

Run: 2026-11-17 ~01:02–01:25 CT (nightly). All reader and decode runs were done by fresh, no-context Grok Bot helpers (knowledgeWork subagents). Each helper was told to read exactly one prompt file and nothing else. Isolation was by instruction and was not technically enforced. One reader family only.
**Weak reader (local Qwen2.5-7B): NOT run this round** (RAM was fine, ~10.6 GB available, but past 7B calls ran for hours and would not finish inside one nightly round; skipped to keep the round complete). **Frozen bench-v1: NOT run this round** (no MNC17 bench encoding yet; pending). No numbers are claimed for either.

## Passages (fresh, written 2026-11-17)
§1 en instruction (food-bank shift reminders; L2 questions in German), §2 ja news (museum renovation), §3 es family group chat, §4 it municipal notice (waste collection), §5 nl instruction (webshop returns). facts.json (51 facts) was written BEFORE encoding (r12 fix). Payloads were frozen and hashed before the questions were written (encoded_before_questions.sha1). The same agent wrote passages, facts, encodings and questions.

## Versions (no key in any)
- **MNC17**: MNC16 rules + r12 fixes: deadline words kept (before/by/until/within), speaker names instead of "me", neutral section tag (`§N you` for instructions, plain `§N` otherwise; no language code), fact-by-fact check before freezing.
- **MNC17x**: more aggressive (merged lines, dropped predictable words).
- **MNC17xx**: most aggressive (identity + owner rule merged into one line, shorter news slots). Target was ≥50% o200k; reached 46.9%. **Target not met.**

## Tokens (originals 1172 o200k / 1361 cl100k; no key, break-even 0)
| Method | o200k | cl100k | Saved o200k / cl100k |
|---|---|---|---|
| MNC17 | 714 | 732 | 39.1% / 46.2% |
| MNC17x | 641 | 661 | 45.3% / 51.4% |
| **MNC17xx** | 622 | 647 | **46.9% / 52.5%** |
| a terse English (frontier-written) | 763 | 775 | 34.9% / 43.1% |
| c LLMLingua-2 0.5 | 471 | 552 | 59.8% / 59.4%* |
*LLMLingua-2 0.5 output an EMPTY §2 (the Japanese passage was compressed to nothing; tool limitation on unspaced Japanese). Excluding §2: LLMLingua-2 0.5 saves 51.3%, MNC17xx 45.1%, terse 32.6% (o200k). "Summarize/compress" baseline (b) and LLMLingua-2 0.66 were not run this round.

## Direct use, STRONG reader (114 questions: 57 English + 57 in German/Japanese/Spanish/Italian/Dutch; 68 S, 46 F), after review
| Method | Run 1 | Run 2 | Safety S (68) | §1 S / §5 S | Saved o200k |
|---|---|---|---|---|---|
| original | 114/114 | — | 68/68 | 24/24 / 20/20 | 0% |
| MNC17 | 114/114 | — | 68/68 | 24/24 / 20/20 | 39.1% |
| MNC17x | 114/114 | — | 68/68 | 24/24 / 20/20 | 45.3% |
| **MNC17xx** | **114/114** | **114/114** | 68/68 ×2 | 24/24 / 20/20 | **46.9%** |
| a terse English (frontier) | 114/114 | — | 68/68 | 24/24 / 20/20 | 34.9% |
| c LLMLingua-2 0.5 | 82/114 (71.9%) | — | 62/68 (**safety FAIL**: §5 recipient of the 16:00 overview lost ×2; §3 Bizum recipient lost ×2; §2 empty) | 24/24 / 18/20 | 59.8% (51.3% excl. §2) |
LLMLingua-2 0.5 on §1/§3/§4/§5 only: 82/94 (87.2%).
Review: 6 regex false negatives accepted (§3.es10 "frutos secos" = nuts on 5 runs; MNC17xx r2 §5.en3 "Don't send a label; refer them to De Vries"). Overrides with reasons: frontier/overrides.json. Pre-review: every MNC and terse run 113/114, MNC17xx r2 112/114.

**Ceiling warning:** every method except LLMLingua scored 100%. These questions cannot separate MNC17, MNC17x, MNC17xx, terse English and the original. The accuracy-vs-savings curve is flat from 0% to 46.9% savings; the point where strong-reader accuracy breaks was not reached.

## Accuracy vs savings (strong reader, fresh r13, o200k)
| Saved | Method | Accuracy | Safety |
|---|---|---|---|
| 0% | original | 100% | PASS |
| 34.9% | terse English | 100% | PASS |
| 39.1% | MNC17 | 100% | PASS |
| 45.3% | MNC17x | 100% | PASS |
| 46.9% | MNC17xx | 100% ×2 | PASS |
| 51.3% (excl. §2) / 59.8% | LLMLingua-2 0.5 | 87.2% / 71.9% | FAIL |

## Blind decode (MNC17xx, no key, 2 fresh frontier helpers; judged by the encoder agent against facts.json, so the judge is not blind)
- 45/51 facts kept exactly in both decodes; 2 safety distortions + 4 minor F losses/distortions (below); 0 invented.
- **Instruction-safety FAIL (2 distortions, both in both decodes, both encoder slips):**
  1. §1 "tell them to call 911 if serious" → "If the injury is serious, they should call 911": the assistant's action ("tell them") was lost. Encoding was `serious: they call 911`.
  2. §5 "before 16:00 send Ms De Vries an overview of the day's returns" → "send De Vries the day's returns": "overview" was dropped by the encoder (`De Vries gets day's returns`).
- Minor F losses: "public volunteer group" → "public group"; "not set out correctly" → "sorting incorrectly"; Marta's question dropped; "commemorative" dropped.
- r12 holes confirmed fixed: every deadline word kept (before Fri 12:00, before Mar 5, before 16:00, within 1h, until 18:00); `§N you` decoded as "instructions for you" with no invented language rule.
Details: decodes/judgments_mnc17xx.json.

## Verdict
**Not a new best.** MNC17xx matches the original (100% ×2, 68/68 safety) at 46.9% / 52.5% savings, slightly above r12 MNC16xx (45.4% / 51.8%), but bench-v1 was not run (required for a new best) and the blind decode failed safety. MNC16x / MNC16xx stay the strong-reader best; MNC3 stays the weak-reader best. **Ready counter: 0/3.**
Gmail: no new reply from xAI or Anthropic (searched 2026-11-17 ~01:05 CT).
