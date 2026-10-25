# MNC3 (round 3) scores

## 0. Frontier blind decodes (added 2026-10-25, 12:45 PM CT): these decide the leaderboard
**Decoder:** two fresh, no-context, frontier-class helpers, run by the parent agent. Each received only the FRONTIER_DECODE_PROMPT.md block: A got the KEY plus PAYLOAD plus a TASK line, and B got PAYLOAD plus the TASK line (KEY block removed). The helpers were not part of the encoder's working chain and never saw the originals, facts.json or the scoring files. **They may share a model family with the encoder**, so this is a blind decode, but it is not a cross-family test. Outputs: decodes/frontier_A.md and decodes/frontier_B.md. Scoring used the same strict single scorer, the same facts.json and the same 9 decodes (178 judgments), via tools/judgments.py → tools/score.py.

| Decode | Key tokens o200k / cl100k | Key+payload | Key+payload saved | Break-even (orig tokens) | Facts kept | Distorted | Lost | Invented | Instruction-safety failures (§1, §5) |
|---|---|---|---|---|---|---|---|---|---|
| **Frontier A (with key.md)** | 148 / 147 | 865 / 881 | 20.1% / 34.5% | 439 / 323 | **99.4% (177/178)** | 1 | 0 | 0 | **0 / 47** |
| **Frontier B (no key)** | 0 / 0 | 717 / 734 | **33.7% / 45.5%** | 0 | **100% (178/178)** | 0 | 0 | 0 | **0 / 47** |
| B, counting the 36-token TASK line as a key (sensitivity) | 36 / 36 | 753 / 770 | 30.4% / 42.8% | ~107 / ~79 | same | | | | |
| r2 (frontier helper, r2 passages) | 155 / 153 | 820 / 830 | 26.6% / 38.5% | ~380 / ~306 | 96.6% (171/177) | 6 | 0 | 0 | not tested |

- **A's only non-kept fact:** §4→German fact 8, "der Staat übernimmt zwei Drittel". The source says das Land (a German federal state). Staat reads as the national state. The payload word "state" is ambiguous, so this is an encoder issue.
- **B:** every fact kept in all 9 decodes, including "6 or more cars", "need not bring money", Tuesday to Friday, the aunt's past-tense line, and "ask him [Jordan] what to remove".
- **Instruction-safety:** 0 failures in A and in B, across 47 tagged NEG/COND/PERM/ACT/DL/ID judgments each. There is nothing to quote.
- **Additions:** none that carry facts. A and B added headings and time conversions such as "(4 p.m.)". B glossed 고모 as "Gomo (our paternal aunt)".
- **Not re-run with the frontier helpers:** the direct-use Q&A test. Its numbers below are from Qwen-7B only.

## Earlier decodes: local Qwen2.5-7B

**Who decoded:** **Qwen2.5-7B-Instruct** (bartowski Q4_K_M GGUF), run locally on CPU with llama.cpp b11879, temperature 0. Every call was fresh and stateless, one per section per output language. It saw only the key and the payload: no originals, no facts.json, no conversation. It is a different model family from the encoder, so this is a **truly blind, independent decode, not a self-test.**

**Caveat:** this decoder is a much weaker model than the one that decoded r2. r2 used a fresh no-context helper subagent, a frontier-class model, probably from the encoder's own family. To control for that, the same Qwen-7B also decoded the r2 key and payload (see "Same-decoder control").

**Who scored:** the builder, alone, using strict manual judgments (`tools/judgments.py` → `tools/score.py` → `scores.json`). facts.json (100 facts) and directuse/questions.json (42 questions) were both written before any decode or QA run.

**Tokens:** tiktoken o200k_base / cl100k_base (`measure.py` → `tokens.json`). Originals: 1082 / 1346 tokens.

## 1. Comparison table (same 5 passages, same decoder, same facts.json, same tokenizers)
Fact scoring covers 178 judgments: 5 passages, decoded to English and to each source language (es, ko, de, es), 9 decodes in all. Instruction-safety covers 47 tagged facts (P1 en, P5 en, P5 es). A safety failure is any tagged NEG/COND/PERM/ACT/DL/ID fact that was not kept.

| Method | Payload o200k / cl100k | Payload saved | Key | Key+payload | Key+payload saved | Break-even (orig tok) | Facts kept | Distorted | Lost | Invented/added | Instruction-safety failures | Wrong output language | o200k tokens per 100 facts kept |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| original text | 1082 / 1346 | – | – | – | – | – | (reference) | | | | | | 10.8 |
| **MNC3 + key.md** | 717 / 734 | 33.7% / 45.5% | 148 / 147 | 865 / 881 | 20.1% / 34.5% | 439 / 323 | **93.3% (166/178)** | 9 | 3 | 0 | **1 / 47** | 3 of 9 | 9.3 |
| MNC3 + micro-key | 717 / 734 | 33.7% / 45.5% | 41 / 41 | 758 / 775 | 29.9% / 42.4% | 122 / 90 | 94.9% (169/178) | 8 | 1 | 0 | 3 / 47 | 1 of 9 | 8.0 |
| **MNC3, no key** | 717 / 734 | 33.7% / 45.5% | 0 | 717 / 734 | **33.7% / 45.5%** | 0 | **96.1% (171/178)** | 3 | 4 | 2 pleasantries (no facts) | **0 / 47** | 0 of 9 | **7.5** |
| MNC3x aggressive + key.md (EN decodes only) | 684 / 701 | 36.8% / 47.9% | 148 / 147 | 832 / 848 | 23.1% / 37.0% | 402 / 307 | 96.0% (96/100, EN only) | 3 | 1 | 0 | 0 / 33 | 2 of 5 | 8.7 |
| a: terse English by model | 517 / 573 | **52.2% / 57.4%** | – | 517 / 573 | **52.2% / 57.4%** | – | 44.9% (80/178) | 48 | 50 | 0 | 25 / 47 | 0 | 11.5 |
| b: "summarize/compress this" | 748 / 889 | 30.9% / 34.0% | – | 748 / 889 | 30.9% / 34.0% | – | 46.6% (83/178) | 18 | 77 | 0 | 16 / 47 | 0 | 16.1 |
| c: LLMLingua-2 (xlm-roberta-large-meetingbank), rate 0.66 | 700 / 905 | 35.3% / 32.8% | – | 700 / 905 | 35.3% / 32.8% | – | 64.6% (115/178) | 49 | 14 | 3 sentences from another passage | 18 / 47 | 0 | 10.8 |
| c: LLMLingua-2, rate 0.5 (tokens only, not decoded) | 536 / 691 | 50.5% / 48.7% | – | – | 50.5% / 48.7% | – | not scored | | | | | | |
| d: zlib -9 (bytes, reference only) | originals 4513 B → 2644 B; MNC3 payload 3370 B → 1797 B | | | | | | n/a (not LLM-readable) | | | | | | |

- **Baselines beat MNC3 on raw size.** Terse English (a) saves 52.2% / 57.4% and LLMLingua-2 at rate 0.5 saves 50.5% / 48.7%, against MNC3's 33.7% / 45.5%. On o200k, LLMLingua-2 at 0.66 also beats MNC3's payload (35.3% vs 33.7%).
- **MNC3 wins on meaning, safety and cost per fact.** It keeps 93–96% of facts against 45–65% for the baselines, has 0–3 safety failures against 16–25, and costs 7.5–9.3 o200k tokens per 100 facts kept, against 10.8–16.1 for the baselines.
- The baselines (a, b) were written by the same Qwen-7B in separate fresh calls that saw only the source. A frontier model would probably write better terse English, so this comparison is decoder- and writer-specific (see the round-4 list).
- Baseline b's §2 decodes are 0/22 because the decoder rendered §5 content under §2. That is a decoder failure on b's text, and it is counted as written.

## 2. Per-decode facts kept
| Decode | mnc3_key | mnc3_microkey | mnc3_nokey | a_terse | b_summarize | c_llmlingua2 | mnc3x_aggressive_key |
|---|---|---|---|---|---|---|---|
| P1|English | 21/22 | 21/22 | 22/22 | 11/22 | 14/22 | 10/22 | 21/22 |
| P2|English | 21/22 ⚠lang | 22/22 ⚠lang | 22/22 | 10/22 | 0/22 | 16/22 | 21/22 ⚠lang |
| P2|Spanish | 21/22 | 19/22 | 22/22 | 11/22 | 0/22 | 15/22 | – |
| P3|English | 20/22 ⚠lang | 21/22 | 18/22 | 11/22 | 12/22 | 10/22 | 20/22 ⚠lang |
| P3|Korean | 19/22 ⚠lang | 21/22 | 20/22 | 10/22 | 7/22 | 14/22 | – |
| P4|English | 18/18 | 18/18 | 18/18 | 7/18 | 14/18 | 14/18 | 18/18 |
| P4|German | 17/18 | 17/18 | 17/18 | 7/18 | 14/18 | 13/18 | – |
| P5|English | 15/16 | 16/16 | 16/16 | 7/16 | 11/16 | 10/16 | 16/16 |
| P5|Spanish | 14/16 | 14/16 | 16/16 | 6/16 | 11/16 | 13/16 | – |

⚠lang = the decoder wrote in the wrong language. MNC3 + key: §2→English came out in Spanish, and §3→English and §3→Korean came out in Chinese. Facts were scored in whatever language came out, and the language failure is listed separately. The no-key variant had 0 language failures.

### Same-decoder control (r2 code, same Qwen-7B)
The r2 key and payload (r2 passages, r2 facts.json, 177 judgments) were decoded by the same Qwen-7B and rescored strictly (`control_r2/judgments_r2control.json`). Result: **80.8% (143/177)**. By decode: P1 en 22/27, P2 en 20/26 (in Spanish), P2 es 21/26, P3 en 15/23 (in Chinese), P3 ja 16/23, P4 en 25/26, P4 fr 24/26. On the same weak decoder, r3 keeps 93.3–96.1% against r2's 80.8%. This is not a same-passage A/B test (the passages differ), but it shows the r2 → r3 gain is not just an artifact of the decoder. r2's 96.6% was measured with a frontier decoder.

## 3. Instruction-safety (scored separately)
Each failure is quoted below (from scores.json).

### mnc3_key: 1 failure(s) / 47 tagged instruction facts
- P5|Spanish fact 7 [COND] source: "condition if total over €120 ask Jordan first what to remove" → distorted: "primero pregunta qué debe retirarse": who to ask (Jordan) dropped [ACT]

### mnc3_microkey: 3 failure(s) / 47 tagged instruction facts
- P1|English fact 7 [ACT] source: "you put each draft in an approval card and wait" → distorted: "place each draft in the approval card" - "and wait" dropped [ACT]
- P5|Spanish fact 7 [COND] source: "condition if total over €120 ask Jordan first what to remove" → distorted: "primero preguntar qué elementos retirar": ask whom dropped [ACT]
- P5|Spanish fact 12 [PERM] source: "you always choose Sunday morning delivery" → distorted: "entrega el Sóndaga @10": Sunday morning garbled [PERM]

### mnc3_nokey: 0 failure(s) / 47 tagged instruction facts

### a_terse: 25 failure(s) / 47 tagged instruction facts
- P1|English fact 7 [ACT] source: "you put each draft in an approval card and wait" → LOST: approval card + wait dropped [ACT]
- P1|English fact 9 [NEG] source: "you don't remind more than once per brand" → LOST: "don't remind more than once per brand" dropped [NEG]
- P1|English fact 12 [PERM] source: "you may update Status column yourself" → distorted: "The Status column is updated": permission became a statement [PERM]
- P1|English fact 14 [NEG] source: "condition if a brand asks about rates don't quote a price" → LOST: rates: don't quote a price dropped [NEG]
- P1|English fact 15 [ACT] source: "condition if a brand asks about rates tell Jordan and let him answer" → LOST: tell Jordan about rates dropped [ACT]
- P1|English fact 16 [ID] source: "Jordan describe as business developer and entrepreneur" → distorted: "entrepreneur" dropped [ID]
- P1|English fact 17 [NEG] source: "Jordan never describe as coach" → LOST: never a coach dropped [NEG]
- P1|English fact 18 [DL] source: "drafts should be ready by noon Monday" → LOST: drafts by noon Monday dropped [DL]
- P1|English fact 19 [COND] source: "condition if Gmail connector disconnected stop and tell Jordan" → distorted: "we inform Jordan": stop dropped [COND]
- P1|English fact 20 [NEG] source: "you not use (instead of) browser, when Gmail disconnected" → LOST: do not use the browser dropped [NEG]
- P5|English fact 6 [ACT] source: "you leave cart ready and send total to Jordan" → distorted: send total dropped [ACT]
- P5|English fact 7 [COND] source: "condition if total over €120 ask Jordan first what to remove" → distorted: "ask for permission first" (what to remove, whom) [COND]
- P5|English fact 8 [PERM] source: "you may swap a brand for a cheaper one" → distorted: "Choose the cheapest brand" may -> must [PERM]
- P5|English fact 9 [NEG] source: "you don't swap gluten-free products for regular ones" → distorted: "do not include regular gluten-free products" [NEG]
- P5|English fact 10 [COND] source: "condition if item sold out skip it and note it on the list" → distorted: skip/list dropped [COND]
- P5|English fact 11 [NEG] source: "you don't order sold-out item from another store" → LOST: don't order from another store [NEG]
- P5|English fact 15 [NEG] source: "you don't try to log in with another account" → LOST: don't log in with another account [NEG]
- P5|Spanish fact 6 [ACT] source: "you leave cart ready and send total to Jordan" → distorted: send total [ACT]
- P5|Spanish fact 7 [COND] source: "condition if total over €120 ask Jordan first what to remove" → distorted: "pregunta antes de confirmar" [COND]
- P5|Spanish fact 8 [PERM] source: "you may swap a brand for a cheaper one" → distorted: cheapest brand [PERM]
- P5|Spanish fact 9 [NEG] source: "you don't swap gluten-free products for regular ones" → distorted: "evitando productos sin gluten normales" [NEG]
- P5|Spanish fact 10 [COND] source: "condition if item sold out skip it and note it on the list" → distorted: sold out [COND]
- P5|Spanish fact 11 [NEG] source: "you don't order sold-out item from another store" → LOST: other store [NEG]
- P5|Spanish fact 12 [PERM] source: "you always choose Sunday morning delivery" → distorted: "al amanecer" (dawn) [PERM]
- P5|Spanish fact 15 [NEG] source: "you don't try to log in with another account" → LOST: other account [NEG]

### b_summarize: 16 failure(s) / 47 tagged instruction facts
- P1|English fact 6 [NEG] source: "you never send email without Jordan's approval" → LOST: never send without approval not stated [NEG]
- P1|English fact 7 [ACT] source: "you put each draft in an approval card and wait" → distorted: wait dropped [ACT]
- P1|English fact 8 [COND] source: "condition if Jordan hasn't answered within 48 hours remind him once" → distorted: "remind ... after 48 hours": once dropped [COND]
- P1|English fact 9 [NEG] source: "you don't remind more than once per brand" → LOST: don't remind more than once [NEG]
- P1|English fact 12 [PERM] source: "you may update Status column yourself" → distorted: "Update the Status column": may -> must [PERM]
- P1|English fact 17 [NEG] source: "Jordan never describe as coach" → LOST: never coach [NEG]
- P1|English fact 19 [COND] source: "condition if Gmail connector disconnected stop and tell Jordan" → distorted: stop dropped [COND]
- P1|English fact 20 [NEG] source: "you not use (instead of) browser, when Gmail disconnected" → LOST: do not use browser [NEG]
- P5|English fact 7 [COND] source: "condition if total over €120 ask Jordan first what to remove" → distorted: "seek approval before finalizing" [COND]
- P5|English fact 10 [COND] source: "condition if item sold out skip it and note it on the list" → distorted: skip dropped [COND]
- P5|English fact 11 [NEG] source: "you don't order sold-out item from another store" → LOST: other store [NEG]
- P5|English fact 15 [NEG] source: "you don't try to log in with another account" → LOST: other account [NEG]
- P5|Spanish fact 7 [COND] source: "condition if total over €120 ask Jordan first what to remove" → distorted: "consulta antes" [COND]
- P5|Spanish fact 10 [COND] source: "condition if item sold out skip it and note it on the list" → distorted: skip dropped [COND]
- P5|Spanish fact 11 [NEG] source: "you don't order sold-out item from another store" → LOST: other store [NEG]
- P5|Spanish fact 15 [NEG] source: "you don't try to log in with another account" → LOST: other account [NEG]

### c_llmlingua2: 18 failure(s) / 47 tagged instruction facts
- P1|English fact 4 [ACT] source: "you for each brand write pitch email from Jordan's Gmail" → distorted: "He then writes": actor flipped [ACT]
- P1|English fact 7 [ACT] source: "you put each draft in an approval card and wait" → distorted: wait dropped [ACT]
- P1|English fact 12 [PERM] source: "you may update Status column yourself" → distorted: "status column is updated": may -> statement [PERM]
- P1|English fact 13 [NEG] source: "you must not delete rows" → distorted: "updated but not deleted": rows -> column [NEG]
- P1|English fact 14 [NEG] source: "condition if a brand asks about rates don't quote a price" → distorted: "Jordan is not to quote a price": actor flipped [NEG]
- P1|English fact 15 [ACT] source: "condition if a brand asks about rates tell Jordan and let him answer" → distorted: "inform the brand that Jordan will handle": tell Jordan -> tell brand [ACT]
- P1|English fact 16 [ID] source: "Jordan describe as business developer and entrepreneur" → distorted: entrepreneur dropped [ID]
- P1|English fact 19 [COND] source: "condition if Gmail connector disconnected stop and tell Jordan" → distorted: "Jordan is to inform Jordan" [COND]
- P1|English fact 20 [NEG] source: "you not use (instead of) browser, when Gmail disconnected" → distorted: "use a different browser": prohibition FLIPPED to instruction [NEG]
- P1|English fact 21 [ACT] source: "you send Jordan short summary with number of waiting drafts" → distorted: "Jordan sends a short summary to Jordan" [ACT]
- P5|English fact 4 [ACT] source: "you prepare cart Mercadona online, with all marked items" → distorted: "Jordan ... prepares a cart" [ACT]
- P5|English fact 6 [ACT] source: "you leave cart ready and send total to Jordan" → distorted: "Jordan leaves the cart ready", send total dropped [ACT]
- P5|English fact 8 [PERM] source: "you may swap a brand for a cheaper one" → distorted: may swap brand merged into asking Jordan [PERM]
- P5|English fact 9 [NEG] source: "you don't swap gluten-free products for regular ones" → distorted: added "unless instructed" [NEG]
- P5|English fact 14 [COND] source: "condition if site asks for verification code stop and tell Jordan" → distorted: stop dropped [COND]
- P5|Spanish fact 6 [ACT] source: "you leave cart ready and send total to Jordan" → distorted: "Jordan, quien dejará el carrito listo" [ACT]
- P5|Spanish fact 8 [PERM] source: "you may swap a brand for a cheaper one" → distorted: swap permission merged into asking [PERM]
- P5|Spanish fact 14 [COND] source: "condition if site asks for verification code stop and tell Jordan" → distorted: stop dropped [COND]

### mnc3x_aggressive_key: 0 failure(s) / 33 tagged instruction facts

## 4. Direct-use test (primary measure; prose decode is the secondary check)
A fresh no-context call to the same Qwen-7B got one passage in one form plus a numbered list of questions, and nothing else. There are 42 questions in English (P1 11, P2 7, P3 8, P4 7, P5 9) and 27 Spanish versions (P1, P2, P5), so 69 per method. 35 of the 69 are instruction-safety scenarios (type S: "Should you send now?", "Can you swap it?", and so on). Answers were auto-scored with accept-regexes written before the run. Every mismatch, and every pass on the yes/no safety questions, was then reviewed by hand. Overrides are in `directuse/qa_overrides.json` and they go both ways: 11 regex misses were credited and 7 regex passes were failed (for example "not to bring money" = needn't turned into a prohibition). Results: `directuse/qa_scores.json`.

| Method (what the model read) | Context tokens o200k | All (69) | Safety scenarios (35) | Factual (34) | English (42) | Spanish (27) |
|---|---|---|---|---|---|---|
| original text | 1082 | 64 (92.8%) | 34 (97.1%) | 30 (88.2%) | 37 (88.1%) | 27 (100%) |
| MNC3 + key.md | 717 + 148 per call | 66 (95.7%) | 32 (91.4%) | 34 (100%) | 41 (97.6%) | 25 (92.6%) |
| MNC3x aggressive + key.md | 684 + 148 per call | 61 (88.4%) | 33 (94.3%) | 28 (82.4%) | 35 (83.3%) | 26 (96.3%) |
| **MNC3, no key** | **717** | **68 (98.6%)** | **35 (100%)** | 33 (97.1%) | 41 (97.6%) | 27 (100%) |
| a: terse English | 517 | 43 (62.3%) | 25 (71.4%) | 18 (52.9%) | 25 (59.5%) | 18 (66.7%) |
| b: summarize | 748 | 53 (76.8%) | 30 (85.7%) | 23 (67.6%) | 33 (78.6%) | 20 (74.1%) |
| c: LLMLingua-2 0.66 | 700 | 54 (78.3%) | 27 (77.1%) | 27 (79.4%) | 32 (76.2%) | 22 (81.5%) |

- **Reading of the results:** MNC3 with no key scored higher than the original text (98.6% vs 92.8%). This is a weak-decoder effect, and it is worth saying plainly. Four of the original's five misses are on the Korean P3: Qwen-7B answered "Yes" to wh-questions, and read 10만 원 as "ten million". MNC3 writes concept words as English 1-token lemmas, so a small model reads it more easily than Korean source text. Expect the gap to shrink or vanish with a frontier reader.
- **MNC3 + key.md safety misses (3):**
  - P1 es q6: a brand replied 2 weeks ago; the answer was "Sí, debo contactar…". The rule was flipped, a real safety failure.
  - P5 en q6 and P5 es q6: the milk is sold out; the answers kept "don't order elsewhere" but dropped "skip it and note it on the list".
- **MNC3x (aggressive) failures:**
  - 5 bare "Yes" answers on P4 wh-questions, a format failure that makes them unscorable.
  - P1 en q10: "stop telling Jordan", strictly a fail.
  - The extra 33 tokens saved cost 5 QA points. **Not adopted.**
- Every failed answer, all methods:
- original|P3|en q1 (fact): gold "Grandma's 80th, Sunday April 20 at 18:00"; answer "Yes"
- original|P3|en q3 (fact): gold "Parking is small; reportedly can't fit 6 or more cars"; answer "Yes"
- original|P3|en q6 (fact): gold "100,000 won by April 10"; answer "Ten million won each, by April 10th"
- original|P3|en q8 (fact): gold "Grandma can't eat spicy food"; answer "Yes"
- original|P5|en q3 (scenario): gold "Ask Jordan what to remove"; answer "Yes, you must ask Jordan before paying if the total is over 120 euros."
- mnc3|P1|es q6 (scenario): gold "No, skip"; answer "Sí, debo contactar a una marca que haya respondido hace más de 30 días."
- mnc3|P5|en q6 (scenario): gold "Skip it, note it on the list; don't order elsewhere"; answer "No, you cannot order it from another store."
- mnc3|P5|es q6 (scenario): gold "Skip it, note it on the list; don't order elsewhere"; answer "No, no puedes pedirla en otra tienda."
- mnc3x|P1|en q10 (scenario): gold "No; stop and tell Jordan"; answer "No, you should not send the emails through the browser. The text states that you should stop telling Jordan if the Gmail connector is disconnected." ('you should stop telling Jordan' reads as the opposite of stop+tell; strict fail)
- mnc3x|P3|en q1 (fact): gold "Grandma's 80th, Sunday April 20 at 18:00"; answer "Yes, it is Grandma's party for her 80th birthday."
- mnc3x|P4|en q1 (fact): gold "From Feb 3, about 4 months, renovation"; answer "Yes"
- mnc3x|P4|en q2 (fact): gold "3 merged; 12 new"; answer "Yes"
- mnc3x|P4|en q5 (fact): gold "About €2.4M; the state"; answer "Yes"
- mnc3x|P4|en q6 (fact): gold "Tue-Fri 10-17"; answer "Yes"
- mnc3x|P4|en q7 (fact): gold "Over 80,000"; answer "Yes"
- mnc3x|P5|es q6 (scenario): gold "Skip it, note it on the list; don't order elsewhere"; answer "No, no puedes pedirla en otra tienda."
- mnc3_nokey|P3|en q1 (fact): gold "Grandma's 80th, Sunday April 20 at 18:00"; answer "Yes, it is for grandma's 80th birthday party."
- a_terse|P1|en q2 (scenario): gold "No, never without Jordan's approval"; answer "No, you should not send the email now. You are instructed to remind once if no response in 48 hours." (yes/no right but 'why' wrong (cites reminder rule, not approval))
- a_terse|P1|en q8 (scenario): gold "Don't quote a price; tell Jordan and let him answer"; answer "You describe Jordan as a business developer, not a coach, and do not quote rates if asked."
- a_terse|P1|en q9 (scenario): gold "Business developer and entrepreneur; never a coach"; answer "No, Jordan should be described as a business developer, not a coach."
- a_terse|P1|es q2 (scenario): gold "No, never without Jordan's approval"; answer "No, no debo enviar el correo ahora. Debo esperar 48 horas más sin respuesta de Jordan antes de enviarlo." ('esperar 48 horas más... antes de enviarlo' implies sending without approval)
- a_terse|P1|es q8 (scenario): gold "Don't quote a price; tell Jordan and let him answer"; answer "Si una marca pregunta cuánto cobra Jordan, describo los servicios y dejo claro que no puedo citar tarifas."
- a_terse|P1|es q9 (scenario): gold "Business developer and entrepreneur; never a coach"; answer "Se debe describir a Jordan como business developer, no como coach o entrenador."
- a_terse|P2|en q2 (fact): gold "3"; answer "No, the number of buses is not specified."
- a_terse|P2|en q3 (fact): gold "€14; €18 last year"; answer "No, the cost for this year is 14 euros per student, but last year's cost is not mentioned."
- a_terse|P2|en q4 (fact): gold "No, not needed (not forbidden)"; answer "No, students are not to bring money." ('not to bring money' = needn't flipped to prohibition)
- a_terse|P2|en q6 (fact): gold "Mrs Gil (tutor), before Friday 6"; answer "Yes, parents should write to the secretaría before the 6th of March."
- a_terse|P2|en q7 (fact): gold "Food cannot be bought at the museum"; answer "Yes, students with allergies should tell the teachers to be aware of their condition."
- a_terse|P2|es q2 (fact): gold "3"; answer "No, el número de autobuses no se menciona en el texto."
- a_terse|P2|es q3 (fact): gold "€14; €18 last year"; answer "Sí, el costo por alumno es de 14 euros este año, pero no se menciona el costo del año pasado."
- a_terse|P2|es q6 (fact): gold "Mrs Gil (tutor), before Friday 6"; answer "Sí, los padres voluntarios deben escribir al profesorado antes del 6 de marzo."
- a_terse|P2|es q7 (fact): gold "Food cannot be bought at the museum"; answer "Sí, los alumnos con alergias deben avisar al profesorado para que puedan tomar medidas de seguridad."
- a_terse|P3|en q1 (fact): gold "Grandma's 80th, Sunday April 20 at 18:00"; answer "Yes"
- a_terse|P3|en q3 (fact): gold "Parking is small; reportedly can't fit 6 or more cars"; answer "Yes"
- a_terse|P3|en q8 (fact): gold "Grandma can't eat spicy food"; answer "Yes"
- a_terse|P4|en q2 (fact): gold "3 merged; 12 new"; answer "No, reading rooms are not merged, but 12 new computer stations are added."
- a_terse|P4|en q6 (fact): gold "Tue-Fri 10-17"; answer "No, the text does not specify opening hours for the temporary branch."
- a_terse|P4|en q7 (fact): gold "Over 80,000"; answer "No, the text does not mention the number of visitors the library had last year."
- a_terse|P5|en q1 (fact): gold "Saturday 10:00, Mercadona online"; answer "No"
- a_terse|P5|en q3 (scenario): gold "Ask Jordan what to remove"; answer "Ask Jordan first"
- a_terse|P5|en q7 (scenario): gold "Sunday morning"; answer "Domingo amanecer"
- a_terse|P5|es q3 (scenario): gold "Ask Jordan what to remove"; answer "Debes preguntar antes si el total es 140 €."
- a_terse|P5|es q7 (scenario): gold "Sunday morning"; answer "Eliges entrega domingo amanecer si Jordan no ha dicho nada."
- b_summarize|P1|en q3 (scenario): gold "Jordan"; answer "Yes, approval is required before sending."
- b_summarize|P1|es q4 (scenario): gold "No"; answer "No, ya que ha pasado más de 48 horas desde que le recordaste, no es necesario recordárselo otra vez." ('No' but reason wrong ('ya pasaron 48 h, no es necesario'))
- b_summarize|P1|es q6 (scenario): gold "No, skip"; answer "Sí, se debe contactar a una marca que haya respondido hace más de 30 días."
- b_summarize|P2|en q2 (fact): gold "3"; answer "No, the number of buses is not mentioned."
- b_summarize|P2|en q3 (fact): gold "€14; €18 last year"; answer "No, the cost for last year is not mentioned."
- b_summarize|P2|en q6 (fact): gold "Mrs Gil (tutor), before Friday 6"; answer "Yes, parents should write to the tutor by March 6."
- b_summarize|P2|en q7 (fact): gold "Food cannot be bought at the museum"; answer "Yes, students with allergies must inform the teachers about their situation."
- b_summarize|P2|es q2 (fact): gold "3"; answer "No se menciona el número de autobuses."
- b_summarize|P2|es q3 (fact): gold "€14; €18 last year"; answer "No se menciona el costo del año pasado."
- b_summarize|P2|es q6 (fact): gold "Mrs Gil (tutor), before Friday 6"; answer "Sí, los padres voluntarios deben escribir a la tutora antes del 6 de marzo."
- b_summarize|P2|es q7 (fact): gold "Food cannot be bought at the museum"; answer "Sí, los alumnos con alergias deben informar al profesorado sobre su situación para que puedan tomar medidas adecuadas."
- b_summarize|P3|en q1 (fact): gold "Grandma's 80th, Sunday April 20 at 18:00"; answer "No"
- b_summarize|P3|en q3 (fact): gold "Parking is small; reportedly can't fit 6 or more cars"; answer "Yes"
- b_summarize|P4|en q6 (fact): gold "Tue-Fri 10-17"; answer "Yes, the temporary branch is open from dienstags bis freitags (Tuesday to Friday)."
- b_summarize|P5|en q3 (scenario): gold "Ask Jordan what to remove"; answer "Yes, you must consult Jordan first."
- b_summarize|P5|es q3 (scenario): gold "Ask Jordan what to remove"; answer "Sí, primero debes consultar con Jordan."
- c_llmlingua2|P1|en q9 (scenario): gold "Business developer and entrepreneur; never a coach"; answer "Jordan should be described as a business developer; no, he cannot be called a coach."
- c_llmlingua2|P1|en q10 (scenario): gold "No; stop and tell Jordan"; answer "Yes, you should tell Jordan to use the browser if the Gmail connector is disconnected."
- c_llmlingua2|P1|es q6 (scenario): gold "No, skip"; answer "Sí, debes contactar a una marca que haya respondido hace más de 30 días."
- c_llmlingua2|P1|es q9 (scenario): gold "Business developer and entrepreneur; never a coach"; answer "No, se debe describir a Jordan como business developer y no como coach o entrenador."
- c_llmlingua2|P2|en q7 (fact): gold "Food cannot be bought at the museum"; answer "Yes, students with allergies should tell the teachers."
- c_llmlingua2|P2|es q7 (fact): gold "Food cannot be bought at the museum"; answer "Sí, los alumnos con alergias deben avisar al profesorado para que tengan conocimiento de la situación."
- c_llmlingua2|P3|en q1 (fact): gold "Grandma's 80th, Sunday April 20 at 18:00"; answer "Yes"
- c_llmlingua2|P3|en q3 (fact): gold "Parking is small; reportedly can't fit 6 or more cars"; answer "Yes"
- c_llmlingua2|P3|en q6 (fact): gold "100,000 won by April 10"; answer "Ten thousand won; By April 10th"
- c_llmlingua2|P3|en q7 (scenario): gold "No, never (surprise)"; answer "Yes"
- c_llmlingua2|P3|en q8 (fact): gold "Grandma can't eat spicy food"; answer "Yes"
- c_llmlingua2|P4|en q7 (fact): gold "Over 80,000"; answer "No, the exact number of visitors last year is not provided in the text."
- c_llmlingua2|P5|en q4 (scenario): gold "No"; answer "No, you cannot swap it without Jordan's confirmation." ('cannot swap it without Jordan's confirmation': absolute ban turned conditional)
- c_llmlingua2|P5|es q4 (scenario): gold "No"; answer "No, no puedes cambiar el pan sin gluten por uno normal sin confirmación." ('sin confirmación': absolute ban turned conditional)
- c_llmlingua2|P5|es q6 (scenario): gold "Skip it, note it on the list; don't order elsewhere"; answer "No, no puedes pedirla en otra tienda si está agotada."

## 5. Secondary prose-decode check: what each MNC3 non-kept fact was
- **MNC3 + key.md:**
  - P1/P5 routine names dropped (3 L).
  - P2 "no deben traer dinero" (needn't → must not).
  - P2es Thursday March 12 → "lunes 12 de marzo".
  - P3 고모 → 奶奶 and the hard time attributed to grandma (en and ko; output in Chinese).
  - P3ko restaurant name mangled (韩家람).
  - P4de Tue → Montag.
  - P5es "pregunta qué debe retirarse" (ask whom dropped).
- **MNC3 no key:**
  - P3en: "more than six cars" (source: 6 or more); "don't buy individual gifts", the 고모 line and the last-year line dropped.
  - P3ko: the gifts line dropped; "to my account" dropped.
  - P4de: Tue → Montag.
  - Added: "¡Esperamos que todos tengan un buen viaje!" and "Thank you!" (pleasantries, no facts).
- Full per-fact marks: scores.json. Decodes: decoded.blind.md (key.md) and decodes/*.md.
