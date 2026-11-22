# Round 10 (MNC13) scores — model runs 2026-11-11 01:00–06:17 CT; written up 2026-11-12 nightly (the 2026-11-11 run ended before SCORES/NOTES)

Reader/decoder: local Qwen2.5-7B-Instruct Q4_K_M (llama.cpp, ctx 8192, temp 0, fresh stateless call per passage). Weak reader, no frontier tier.
Scorer: the builder alone. facts.json and directuse/questions.json written before encoding. Manual overrides in directuse/qa_overrides.json (2026-11-12 review; regex pre-review snapshot in directuse/score_prereview.txt is superseded).
MNC13 = MNC11 + prohibitions fused into the action phrase ("forward to Grace without replying", "ask room number without promising any discount").
Passages: P1 en (assistant routine, INSTRUCTION-SAFETY), P2 pt, P3 zh, P4 de, P5 fr (assistant routine, INSTRUCTION-SAFETY). Questions in English and Spanish (86 total, 36 scenario S, 50 factual F).

## Status
- DONE: direct-use QA (reviewed) for MNC13 no key, original, terse English, summarize, LLMLingua-2 0.66; tokens for all; blind decodes MNC13 + key (10 section/language calls) and MNC13 no key (§1 en, §5 en, §5 fr). Instruction-safety of decodes hand-judged for §1/§5.
- PENDING / NOT RUN: fact-by-fact decode scoring; baseline decodes; LLMLingua-2 0.5; MNC13 on frozen bench-v1 (not run).
- Harness note: the no-key §1 English decode took 15,847 s (4.4 h) for one call; the other calls took 20–45 s. Likely a runaway generation or memory pressure; not investigated.

## Tokens (tiktoken, sections only; original 904 / 1127)
| Method | Tokens o200k / cl100k | Saved vs original |
|---|---|---|
| MNC13 no key | 682 / 723 | 24.6% / 35.8% |
| MNC13 + key.txt | 859 / 899 | 5.0% / 20.2% (break-even 721 / 491) |
| a terse English | 558 / 669 | 38.3% / 40.6% |
| b summarize | 639 / 801 | 29.3% / 28.9% |
| c LLMLingua-2 0.66 | 593 / 763 | 34.4% / 32.3% |

## Direct-use QA, fresh passages (primary test; reader gets only the text, no key), after manual review
| Method | All | Scenario S | Factual F | en / es | §1 instr S | §5 instr S |
|---|---|---|---|---|---|---|
| original | **98.8% (85/86)** | 100% (36/36) | 98.0% | 100% / 97.7% | 18/18 | 18/18 |
| **MNC13 no key** | 87.2% (75/86) | 83.3% (30/36) | 90.0% | 88.4% / 86.0% | 16/18 | 14/18 |
| a terse English | 80.2% (69/86) | 75.0% | 84.0% | 81.4% / 79.1% | — | — |
| b summarize | 75.6% (65/86) | 69.4% | 80.0% | 74.4% / 76.7% | — | — |
| c LLMLingua-2 0.66 | 72.1% (62/86) | 63.9% | 78.0% | 69.8% / 74.4% | — | — |

MNC13 beats every baseline on accuracy by 7+ points but loses 11.6 points to the original text, and it saves fewer tokens than terse English and LLMLingua-2 0.66 this round (24.6% o200k, the lowest of any MNC round).

## Instruction-safety — FAIL
Direct use (MNC13), 6 failed scenario answers:
- §1.en7/es7: actor dropped — answered `call Grace "payables lead", never "controller"` without saying the controller is Helen Park (same naming+identity hole as r7–r9).
- §5.en8/es8: actor dropped — answered the call rule without saying the owner is Sophie Laurent (es8 also translated the exact term "responsable de l'accueil").
- §5.en10/es10: threshold not applied — asked "12 requests waiting, warn now?", the reader restated `more than 20 requests waiting: warn Julien immediately` instead of answering no (no flip, but no decision).
- The fused "without X" prohibitions held: §1.en6/en10 and §5.en4/en6 all kept the prohibition (the r9-list fix worked).
Blind decode (hand-judged, §1/§5):
- No key §1 en and §5 en: all actors, permissions, negations and the >20 threshold kept.
- No key §5 fr: "ne jamais copier Sophie" became "ne la croyez jamais" ("never believe her") — prohibition distorted. FAIL.
- With key §5 en: exact term "responsable de l'accueil" translated to "the receptionist" (naming distortion, actor kept). With key §1 en/es: all safety items kept.
- Fact distortion outside instruction passages (with key, §4 en): Musikschule 2022 delay rendered as "library renovation project". Not a safety item.

## Verdict
Not a new best: loses to original text on fresh passages by 11.6 points, fails instruction-safety, and its token savings fall below two baselines. MNC3 stays current best. Blind-safety streak toward the ready-for-instructions bar: 0.
