# MNC3: machine-native compression, round 3 (blind-tested 2026-10-25)

Concept: Jordan Wendelken, business developer and entrepreneur. Designed, encoded and scored by AI.

## Blind status
- **Frontier blind decodes (these decide the leaderboard):** two fresh, no-context, frontier-class helpers, run by the parent agent. Each got only the FRONTIER_DECODE_PROMPT.md block: A with the key, B without it.
  - They were not part of the encoder's working chain, but **they may share a model family with the encoder**. That makes this a blind test, not a cross-family one.
  - **Results:** A kept 99.4% (177/178) and B kept 100% (178/178), with 0 lost, 0 invented and 0/47 instruction-safety failures in each. Details are in SCORES.md §0.
- **Decoder:** Qwen2.5-7B-Instruct, Q4_K_M GGUF, local CPU, llama.cpp b11879, temperature 0.
  - Every call was fresh and stateless: one per section × output language, and one per passage × question language for direct use.
  - It saw only the key and the payload (or only a baseline's text). It never saw the originals, facts.json or this conversation.
  - It is a different model family from the encoder. **This is a truly blind, independent decode, not a self-test.**
- **Compared with r2:** r2 was decoded by a fresh no-context helper subagent, a frontier-class model that was probably the encoder's own family. Qwen-7B is much weaker. This lowers absolute scores and causes wrong-language output, so r2 and r3 percentages are not like-for-like.
  - A same-decoder control (r2 code decoded by Qwen-7B) is in SCORES.md §2: r2 80.8% vs r3 93.3–96.1%.
- **Scorer:** the builder, alone (strict manual judgments). facts.json and questions.json were written before any decode or QA run.
- Baselines a and b were written by the same Qwen-7B in fresh calls that saw only the source.

## Files
- `originals.txt`: 5 passages.
  - P1 en: assistant brand-outreach routine (instruction).
  - P2 es: school-trip notice.
  - P3 ko: family group chat.
  - P4 de: library news.
  - P5 es: assistant grocery routine (instruction).
  - Totals: 1082 o200k / 1346 cl100k tokens.
- `key.md`: 148/147 tokens.
- `experiments/key_micro.md`: 41/41 tokens.
- `payload.txt`: the shipped encoding, v3b. 717/734 tokens.
- Experiment payloads:
  - `experiments/payload_v3x_aggressive.txt`: 684/701 tokens.
  - `experiments/payload_v3a_prepune.txt`: 729/747 tokens.
- `facts.json`: 100 facts, with safety tags NEG/COND/PERM/ACT/DL/ID on P1 and P5.
- `scores.json`: per-fact marks. Built by `tools/score.py` from `tools/judgments.py`.
- `tokens.json`: built by `measure.py`.
- `selfcheck.py` and `selfcheck.out.txt`: encoder lint, PASS with waivers.
- `decoded.blind.md`: MNC3 + key.md.
- `decodes/`: micro-key, no-key, MNC3x, and baselines a, b, c.
- `baselines/`: a_terse, b_summarize, c_llmlingua2 at r0.66 and r0.5.
- `control_r2/`: the r2 code decoded by Qwen-7B, plus its judgments.
- `directuse/`:
  - questions.json, answers.json, qa_overrides.json, qa_scores.json.
  - Built by `tools/qa.py` and `tools/qa_score.py`.
- `FRONTIER_DECODE_PROMPT.md`: a ready prompt for a fresh frontier no-context decode (round-4 item 1).

## Design changes vs r2
1. **Logic as 1-token English lemmas instead of symbols.**
   - The r2 operators `< > ? ! / = →` were replaced by because, so, if, not, don't, never, cannot, need not, or, becomes.
   - Payload cost is the same (1 token each), the key is smaller, and nothing is ambiguous.
   - This removes the r2 "can't flush → don't flush" class by construction: modals are written as themselves.
2. **Number words for small counts** ("three buses"). " 3" costs 2 tokens (space + digit), while " three" costs 1, and the number is welded to its noun. This targets the r2 "4 [stations]" failure.
3. **Tense cues** (was, will, last yr). Unmarked means present. `X:` = speaker, and the cue applies to that line only. This targets the r2 "costó → cuesta" failure.
4. **New `task` section type** (orders to you). Instruction passages keep never/don't/may/must/if/unless/only as words.
5. **Native script for Korean names** (민준, 한가람, 고모). `age80` replaces `80th`.
6. **Pruning (v3a → v3b):** −12 / −13 tokens with no fact loss in the self-check.

## Did the 3 r2 failures get fixed? (blind, Qwen-7B)
- **Number-noun binding: FIXED in this test.**
  - three buses, twelve people, two volunteers, three reading rooms and twelve computer stations were kept in every MNC3 decode and every QA answer.
  - The P3 "≥6 cars" is a separate issue: it came out as "more than six". That is a comparator problem, not binding.
- **Tense on speaker lines: MOSTLY FIXED.**
  - "last yr same trip was €18" was kept in all 6 MNC3 P2 decodes.
  - Vogel's past-tense visitor count was kept.
  - The P3 고모 / last-year line failed in other ways: with the key, the speaker became 奶奶; with no key, the line was dropped.
- **Modal negation: PARTLY FIXED.**
  - need-not (P4), cannot board, cannot eat spicy and cannot borrow magazines were kept everywhere.
  - **Still failing:** with key.md, P2 "need not bring money" came out as "no deben traer dinero" (must not). The same happened in MNC3x. No-key and micro-key kept it.

## Results (details: SCORES.md)

| | r2 (frontier decoder, r2 passages) | r3 MNC3 + key.md | r3 MNC3 no key (best r3 config) | r3 micro-key |
|---|---|---|---|---|
| **Facts kept, frontier blind helper** | 96.6% (171/177) | **99.4% (177/178)**, frontier A | **100% (178/178)**, frontier B | not run |
| Instruction-safety, frontier | not tested | 0/47 | 0/47 | – |
| Facts kept, Qwen-7B blind | 96.6% (171/177) | 93.3% (166/178) | 96.1% (171/178) | 94.9% (169/178) |
| Lost / invented | 0 / 0 | 3 / 0 | 4 / 0 facts (2 pleasantries added) | 1 / 0 |
| Distorted | 6 | 9 | 3 | 8 |
| Key tokens o200k / cl100k | 155 / 153 | 148 / 147 | 0 | 41 / 41 |
| Payload saved | 40.8% / 50.0% | 33.7% / 45.5% | 33.7% / 45.5% | 33.7% / 45.5% |
| Key+payload saved | 26.6% / 38.5% | 20.1% / 34.5% | **33.7% / 45.5%** | 29.9% / 42.4% |
| Break-even (orig tokens) | ~380 / ~306 | 439 / 323 | 0 | 122 / 90 |
| Instruction-safety failures | (not tested) | 1/47 | **0/47** | 3/47 |
| Direct-use QA (69) | (not tested) | 95.7% | **98.6%** (original text: 92.8%) | not run |
| Same Qwen-7B on r2 code | 80.8% (143/177) | | | |

**Instruction-safety, MNC3 + key.md, the only failure:** P5→Spanish, "primero pregunta qué debe retirarse". It dropped who to ask (Jordan) [COND/ACT]. No-key: 0 failures.

**Frontier verdict (supersedes the Qwen-only verdict below): YES, r3 with no key is the new best.**
- **Facts kept:** frontier B kept 100% (178/178), which is at least r2's 96.6%.
- **Tokens:** key+payload is 717/734, saving 33.7% / 45.5%, against r2's 820/830 (26.6% / 38.5%). It is lower in absolute tokens and better as a rate, and both results are blind.
- **Sensitivity check:** counting B's 36-token TASK instruction as a key, B still saves 30.4% / 42.8%. r2's decoder prompt was not counted either.
- **r3 with key.md (frontier A) does NOT qualify.** Facts kept is 99.4%, but key+payload saves only 20.1% / 34.5%, which is below r2.
- **Limits:**
  - the frontier helpers may share the encoder's model family;
  - scoring was done by one person, the builder;
  - the passages differ from r2's;
  - the direct-use Q&A test was not re-run with a frontier model.

**Qwen-only verdict (kept for the record): NO, by the rule.** The best r3 config (no key) keeps 96.1% of facts, below r2's 96.6%. That breaks "facts kept must not drop", even though key+payload tokens fell (33.7% vs 26.6% saved on o200k).
- The comparison is confounded: r3 was decoded by a far weaker 7B model, and the passages are different.
- On the same decoder, r2 code scores 80.8% against r3's 93.3–96.1%. That is strong evidence r3 is better, but it is not the rule's measurement.
- r2 stays **CURRENT BEST** until a frontier blind decode of r3 (round-4 item 1) reaches ≥96.6%.
- The payload alone compresses less than r2 (33.7% vs 40.8% o200k). The two instruction passages carry many 1-token logic words that cannot be dropped: P1 saves 22%, P5 29%.

## Baselines (same passages, decoder, facts.json and tokenizer)
- **a, terse English:** 52.2% / 57.4% saved, 44.9% facts kept, 25/47 safety failures, QA 62.3%.
- **b, summarize:** 30.9% / 34.0% saved, 46.6% kept, 16/47 safety failures, QA 76.8%.
- **c, LLMLingua-2 at rate 0.66:** 35.3% / 32.8% saved, 64.6% kept, 18/47 safety failures, QA 78.3%.
  - It ran successfully: microsoft/llmlingua-2-xlm-roberta-large-meetingbank, CPU, llmlingua 0.2.2.
  - Its compressed text itself drops "hasn't" and "instead of", which leads to "use a different browser" and to Korean never-tell flipped into "please tell".
- **c, LLMLingua-2 at rate 0.5:** 50.5% / 48.7% saved. Measured for tokens only, not decoded.
- **d, zlib:** bytes only. It is not LLM-readable, so it is reference only.
- **Baselines BEAT MNC3 on raw token savings.** a beats it on both tokenizers, c at 0.5 beats it on o200k and cl100k, and c at 0.66 beats it on o200k.
- MNC3 beats every baseline on facts kept, safety and QA accuracy, and on tokens per fact kept: 7.5 o200k tokens per 100 facts kept with no key, against 10.8 for the original and LLMLingua-2, 11.5 for terse and 16.1 for summarize.

## Holes found (things a human-style design would not exploit)
1. **English 1-token lemmas are the cheapest concept IDs in every source language.**
   - 必须 costs 2/4 tokens vs " must" 1/1. 因为 costs 3 vs because 1.
   - Language-neutral in practice means English lemmas plus native-script names.
2. **A digit after a space costs 2 tokens.** " three" is 1 token and also binds the number to its noun, so the fix and the saving are the same move.
3. **Punctuation glued to a word costs about 1 token each.** `\n ` costs 2 tokens per line. Dropping `+` and `:` saves 19 tokens on 5 passages (MNC3x), but direct-use accuracy fell 7 points, so the saving is not free.
4. **The key can be replaced by conventions the decoder already knows.** On Qwen-7B, *no key* beat both keys on facts (96.1% vs 93.3%), safety (0 vs 1–3) and QA (98.6% vs 95.7%).
   - The key's wording ("§N type lang", "fluent prose in asked lang") pulled a small model into the wrong output language.
   - The cheapest key is 0 tokens. This must be re-checked on a frontier decoder.
5. **The compressed form can be easier for a small model than the source.** QA on MNC3 (98.6%) beat QA on the original text (92.8%), mostly on Korean, because MNC3 normalizes content to high-frequency English lemmas. Compression can double as normalization.
6. **Native-script names cost more on cl100k** (민준 2/5 vs Minjun 2/2), but romanizing loses fidelity. The best spelling choice differs by tokenizer.
7. **`MonD` reads as a time** ("Mon9" → "lunes a las 9:00"). Date and time glued forms collide.
8. **The decode target does not need to be prose.** Direct-use QA shows the payload works as a query-able fact store, and a structured-facts decode (one triple per line) would be scoreable mechanically.

## Round-4 fix list
1. **DONE:** frontier blind decode. A scored 99.4% and B scored 100%; see SCORES.md §0. **Next:** run the same prompt on a frontier model from a *different* family (cross-family check), and re-run the direct-use Q&A on frontier models.
2. **Same-passage A/B.** Re-encode the r2 passages with r3 rules, so rounds compare on identical text, not rates.
3. **Independent scorer.** A second scorer, or a model scorer with the rubric, re-marks scores.json and qa_scores.json.
4. **Ship no key by default.** On both decoders, no key beat key.md on facts and tokens. Keep key.md only as a fallback spec for weak decoders, and re-test whether a 41-token micro-key helps. **Key causes wrong-language output** on Qwen-7B (3 of 9 decodes with key.md). Either ship no key, or put the language as a full word in the target language (e.g. "Write in English.") outside the key. Test both.
5. **needn't → must not** (P2, key.md and MNC3x). Try "no need bring money" or "money optional" and test it blind.
6. **≥N renders as "more than N".** Use "six or more cars".
7. **Routine names dropped with key.md** (P1/P5 fact 1). Mark titles explicitly, e.g. `title weekly grocery routine`.
8. **Date-time collision** (`Mon9`, `Fri6` read as times). Write `Mon Mar9` / `Fri Mar6` or `9th`.
9. **Weekday drift** (Tue → Montag in German, all three configs). Investigate the "Tue-Fri" range form and try "Tuesday to Friday".
10. **Actor drop in "ask first"** (P5es). Write "ask Jordan first what to remove" with no elision.
11. **Baselines beat MNC3 on raw tokens** (terse 52%, LLMLingua-2 at 0.5 50% vs 33.7%). Close the gap without losing safety:
    - (a) drop articles and auxiliaries that terse English drops, but keep every logic word;
    - (b) test LLMLingua-2 with a force-keep list of negations and modals as a hybrid;
    - (c) re-run baseline a with a frontier writer for a fair comparison.
12. **Instruction passages compress poorly** (P1 22%, P5 29%). Try section-level defaults such as `task` meaning "you" is the actor, and dropping "you"/"each:".
13. **Structured-facts decode target.** Ask the decoder for triples and score them mechanically against facts.json.
14. **Per-tokenizer spelling table** (names, CJK) chosen at encode time.
15. **QA format failures** ("Yes" answers to wh-questions on MNC3x/P4). Add a one-line answer-format instruction for every method, or score them separately.
16. **MNC3x pruning** saved 33 tokens but cost 7 QA points. Only adopt pruning that passes blind QA.

17. **"state" is ambiguous for German Land** (frontier A rendered it as Staat). Write `Land` or `federal state`.
18. **Weak-decoder gap.** No key scored 100% on the frontier helper but 96.1% on Qwen-7B. Decide which decoder class the published claims target, and report both.
