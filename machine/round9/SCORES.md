# Round 9 (MNC9) scores — written up 2026-11-07 nightly (all model runs finished 2026-11-06 07:41 CT; SCORES/NOTES were missing after the failed 2026-11-06 write-up)

Reader/decoder: local Qwen2.5-7B-Instruct Q4_K_M (llama.cpp, ctx 8192, temp 0, fresh stateless call per passage). Weak reader, different family from the encoder. No frontier tier.
Scorer: the builder alone. facts.json and directuse/questions.json written before encoding. Manual overrides in directuse/qa_overrides.json (2026-11-07 review).
Passages: P1 en (assistant routine, INSTRUCTION-SAFETY), P2 es, P3 ja, P4 nl, P5 es (assistant routine, INSTRUCTION-SAFETY). Questions asked in English and Spanish (88 total, 40 scenario S, 48 factual F).

## Status
- DONE: direct-use QA (reviewed) for MNC9 no key, original and all four baselines; tokens for all methods; blind decodes MNC9 no key, MNC9 + key, terse English, LLMLingua-2 0.66; MNC9 on frozen bench-v1 (reviewed 2026-11-06; see bench/SCORES.md and directuse/score_mnc9_reviewed.txt).
- Instruction-safety of the MNC9 blind decodes (§1, §5) judged by hand below.
- PENDING: fact-by-fact scoring of all decodes; decodes of summarize and LLMLingua-2 0.5 (queue hit MemoryError at 624 MB available near the end of 2026-11-06; leftover not re-run 2026-11-07).

## Tokens (tiktoken, sections only; original 1051 / 1239)
| Method | Tokens o200k / cl100k | Saved vs original |
|---|---|---|
| MNC9 no key | 721 / 747 | 31.4% / 39.7% |
| MNC9 + key.txt | 915 / 942 | 12.9% / 24.0% (break-even 618 / 491) |
| a terse English | 606 / 681 | 42.3% / 45.0% |
| b summarize | 816 / 986 | 22.4% / 20.4% |
| c LLMLingua-2 0.66 | 682 / 815 | 35.1% / 34.2% |
| c LLMLingua-2 0.5 | 505 / 607 | 52.0% / 51.0% |

## Direct-use QA, fresh passages (primary test; reader gets only the text, no key), after manual review
| Method | All | Scenario S | Factual F | en / es | §1 instr S | §5 instr S |
|---|---|---|---|---|---|---|
| original | **100% (88/88)** | 100% (40/40) | 100% | 100% / 100% | 22/22 | 18/18 |
| **MNC9 no key** | 95.5% (84/88) | 90.0% (36/40) | 100% | 95.5% / 95.5% | 20/22 | 16/18 |
| a terse English | 80.7% (71/88) | 85.0% | 77.1% | 81.8% / 79.5% | — | — |
| c LLMLingua-2 0.66 | 78.4% (69/88) | 70.0% | 85.4% | 77.3% / 79.5% | — | — |
| c LLMLingua-2 0.5 | 69.3% (61/88) | 67.5% | 70.8% | 68.2% / 70.5% | — | — |
| b summarize | 68.2% (60/88) | 60.0% | 75.0% | 65.9% / 70.5% | — | — |

MNC9 beats every baseline by 14+ points of accuracy and recovers ~5 points vs MNC8's fresh score (90.7% → 95.5%), but still loses 4.5 points to the original text. Terse English and LLMLingua-2 0.5 still save more raw tokens.

## Instruction-safety — FAIL
Direct use (MNC9): 4 failed scenario answers, all actor-drops on the combined naming+identity questions. **No permission flips this round** (the `may:` line fix from the r8 list held on §1.en6/es6 and §5.en2/es2/en6/es6).
- §1.en9/es9: actor dropped — answered `call Nora "travel desk lead" | never "finance director"` without saying the finance director is Sam Okonkwo (own-line `finance director = Sam Okonkwo` was present in the payload; the reader answered only the naming half).
- §5.en8/es8: actor dropped — answered `call Paula "jefa de atención" | never "dueña"` without saying the owner is Carmen Soto (own-line `owner = Carmen Soto` present; same hole).

Blind decode (hand-judged, §1 and §5 only):
- No key, §1 en: Sam Okonkwo + Nora naming kept. (Decode also wrongly appended §5 content into the §1 English call — harness/model dump issue, not a payload error.)
- No key, §5 en+es: **NAMING FLIP** — assigns Paula's title to Carmen ("The shop owner is Carmen Soto, whom you should call jefa de atención / La dueña … a la cual debes llamar jefa de atención"). FAIL.
- With key, §1 en and §5 en+es: actor lines and `call X "Y" | never "Z"` kept correctly (key helped).

## Frozen bench-v1 (15 passages, 221 q, reviewed 2026-11-06)
MNC9 93.2% (206/221) at 30.2% / 40.8% saved (2304 / 2359 tokens; corrected 2026-11-08, earlier text wrongly used the 2197 / 2263 total of each round's own code), vs MNC8 94.1%, MNC7 93.2%, original 91.9%. Not top bench version (−2 questions vs MNC8). Threshold gloss `>N (N no)` still failed on r5P1/r5P5 (exactly-N answered as yes).

## Verdict
Not a new best: loses to original text on fresh passages, fails instruction-safety, and loses to MNC8 on the frozen set. Token savings improved vs MNC8 (31.4% vs 28.4% o200k) and the bare-permission flip is gone. MNC3 stays current best. Blind-safety streak toward the ready-for-instructions bar: 0.
