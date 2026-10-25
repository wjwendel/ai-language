# MNC: a machine-native compression code for AI

*Concept: Jordan Wendelken, a business developer and entrepreneur. Designed and measured by AI. Same license as this repository (CC BY 4.0).*

## The picture: teleportation for meaning
Break a message into its atoms. Send only the smallest form that still holds every atom. Reassemble it intact on the other side, in any language. The **key** is the blueprint: one small spec that tells any AI how to put the atoms back together.

AIL (the rest of this repo) is written so people can read it. MNC drops that constraint. Every choice is driven by token cost, because fewer tokens mean less compute, lower latency and less energy. MNC stays auditable in a different way: any AI given the key can decode the payload to plain language, in whatever language you ask for.

## Round 1, blind-tested (2026-10-24)
- **Test set:** 4 everyday passages written natively. Two English (a household plan, a how-to), one Spanish (local news), one Chinese (a family trip plan).
- **Payload size:** 39.0% smaller overall on o200k (938→572 tokens) and 49.5% smaller on cl100k (1153→582).
  - English: 41–46% smaller on both tokenizers.
  - Spanish: 44.9% (o200k) and 53.2% (cl100k).
  - Chinese: 22.7% (o200k, which already packs Chinese tightly) and 53.7% (cl100k).
- **Key size:** 186 tokens (o200k), versus ~1.2k for AIL v2.3. Break-even is about 477 original tokens on o200k and 374 on cl100k.
- **Meaning:** a no-context decoder with only the key and the payload kept **94.5%** of 145 fact checks. English decodes kept 94.8% (91/96). Decodes back into Spanish and Chinese kept 93.9% (46/49). **0 facts lost, 0 invented**, 8 distorted.
- **Comparison:** AIL v2.3 saved 16.4% (o200k) on blind encode.

## Round 2, blind-tested (2026-10-25)
- **Test set:** 4 new passages in 4 languages: English (a pet-sitter note), Spanish (local news), Japanese (an apartment water-outage notice) and French (a roommate's moving-out message).
- **Payload size:** 40.8% smaller on o200k (1123→665) and 50.0% smaller on cl100k (1355→677). Japanese: 53.2% / 64.1%.
- **Key size:** 155 tokens (o200k), down 17% from round 1 while adding every round-1 fix. Break-even is about 380 original tokens (o200k) and 306 (cl100k). Key and payload together are 26.6% (o200k) and 38.5% (cl100k) smaller than the originals.
- **Meaning:** a no-context decoder with only the key and the payload kept **96.6%** of 177 fact checks. English decodes kept 97.1% (99/102). Decodes back into Spanish, Japanese and French kept 96.0% (72/75). **0 lost, 0 invented**, 6 distorted (3 facts, each in two languages).
- **What failed:**
  - "4 stations" came out as "4", with the noun missing.
  - A past-tense cost in news came out in the present tense.
  - "The toilets won't flush" turned into "do not flush".
- **What held in this test:** every hedge, modal, deadline, gendered noun and future-in-news form, which were the round-1 failure types.
- Round-3 fixes are in round2/NOTES.md.

## Round 3, blind-tested (2026-10-25): current best (no-key form)
- **Frontier blind decodes.** A fresh frontier-class helper with no context got only the payload and a one-line task (variant B, no key). It kept **all 178 fact checks**, with 0 lost, 0 invented and **0 of 47 instruction-safety checks failed**. Given the key as well (variant A), it kept 177/178: German "Land" came out as "Staat".
  - The helpers were not part of the encoder's working chain, but they may share its model family, so this is not yet a cross-family test.
- **Size.** With no key, key + payload is 717 tokens on o200k and 734 on cl100k, 33.7% and 45.5% smaller than the originals. r2 was 26.6% and 38.5%.
  - Counting the 36-token task line as a key gives 30.4% and 42.8%.
  - With the 148-token key, savings are 20.1% and 34.5%, below r2, so the keyed version is not the new best.
- **Why r3 counts as the best:** facts kept did not drop (100% vs 96.6%), and key + payload tokens fell. Both are blind results, but the passages differ from r2's and one person scored them.
- The results below come from an earlier, harder test with a local 7B decoder.

- **Test set:** 5 new passages:
  - two assistant-instruction passages: an English brand-outreach routine and a Spanish grocery routine;
  - a Spanish school notice;
  - a Korean family group chat;
  - a German library news item.
- **Blind decoder:** **Qwen2.5-7B-Instruct**, run locally (Q4_K_M, llama.cpp, temperature 0). Each call was fresh and saw only the key and the payload. It is a different model family from the encoder, so the decode is truly blind and independent. It is also much weaker than the frontier-class decoder r2 used.
- **Design changes:**
  - Logic is written as 1-token English words (because, if, not, cannot, need not), not symbols.
  - Small counts are written as number words ("three buses").
  - Tense cue words are scoped to the speaker's line.
  - New `task` section type for orders to an assistant.
- **Results:**

Local-7B results (Qwen2.5-7B, blind; direct-use Q&A was run only on this decoder):

| Config | Key tokens | Key+payload saved (o200k / cl100k) | Facts kept | Instruction-safety failures | Direct-use QA (69 questions) |
|---|---|---|---|---|---|
| MNC3 + key | 148 | 20.1% / 34.5% | 93.3% | 1 / 47 | 95.7% |
| MNC3 + 41-token micro-key | 41 | 29.9% / 42.4% | 94.9% | 3 / 47 | – |
| **MNC3, no key** | 0 | **33.7% / 45.5%** | **96.1%** | **0 / 47** | **98.6%** |
| Original text (same QA) | – | – | – | – | 92.8% |
| Terse English (model) | – | 52.2% / 57.4% | 44.9% | 25 / 47 | 62.3% |
| "Summarize/compress" | – | 30.9% / 34.0% | 46.6% | 16 / 47 | 76.8% |
| LLMLingua-2 (rate 0.66) | – | 35.3% / 32.8% | 64.6% | 18 / 47 | 78.3% |

- **Baselines are smaller.** Terse English and LLMLingua-2 at rate 0.5 (50.5% / 48.7%) save more raw tokens than MNC3. MNC3 keeps far more facts and instruction rules, so it costs the fewest tokens per fact kept.
- **On the 7B decoder alone, r3 would not have qualified:** 96.1% is below r2's 96.6%. On that same decoder, r2's code keeps only 80.8%.
- **The only safety failure with the key:** P5→Spanish, "primero pregunta qué debe retirarse", which dropped who to ask (Jordan).
- **Still failing:**
  - "need not bring money" became "must not" (with the key);
  - "6 or more" became "more than six";
  - Tuesday became Monday in German;
  - with the key, the small model sometimes answered in the wrong language.
- Everything is in round3/: SCORES.md, NOTES.md (holes found and the round-4 list), facts.json, directuse/, baselines/ and FRONTIER_DECODE_PROMPT.md.

## Honest limits
- There have been three rounds. Round 3 was decoded blind by a local 7B model and by fresh frontier-class helpers that may share the encoder's model family. It had a single scorer, and its direct-use test (69 questions on 5 passages) ran only on the 7B model. A cross-family frontier decoder and an independent scorer are still needed. Rounds 1–2: each on 4 passages of ~200-300 words, with one blind decoder per round. Scoring is manual, by the builder. The passages differ between rounds, so rounds are compared on rates, not as a same-passage A/B test. It is a proxy, not a benchmark, and needs larger, cross-model tests with independent scoring.
- Token counts come from OpenAI tokenizers (o200k, cl100k). Energy has not been measured. The energy claim follows from fewer tokens, not from a meter.
- Round 1's 8 distortions came from missing modals ("should" became a statement), news tense ("will help" became "is helping"), grammatical gender not encoded (vecina became vecino), and the encoder dropping "about." The round-2 fixes are in round1/NOTES.md. None of these failure types recurred in the round-2 blind test, which is one decoder on new passages. Round 2's own failures are listed above.
- MNC is complementary to trained compressors (LLMLingua, gist tokens). It needs no training or model access, and a model can write it as well as read it.

## How it works (core ideas)
1. **The token is the unit.** Every symbol was checked with tiktoken. Whole common words are 1 token, while abbreviations often cost 2–3, so MNC keeps full base-form words and drops anything that carries no fact.
2. **Language-neutral grammar.** Relations are single-token symbols in both tokenizers (`< > ? ! + , / ~ ≥ = : → × # @ §`). Content words act as concept labels, using whichever spelling is cheapest, and are rendered in any output language. Names use the cheapest romanization, and native script is restored on output.
3. **Glued numbers.** A space before a digit costs a token, so the code writes `@1345`, `min10`, `age72`, `×2`.
4. **Defaults over words.** A header such as `§3 news es` sets tense, mood, the default actor and the source language.
5. **Operators for logic:** cause, result, condition, negation, change.

## Files (round1/, round2/, round3/)
- `key.md`: the blueprint (machine-only).
- `payload.txt`: the encoded passages.
- `originals.txt`: the source passages.
- `decoded.blind.md`: the blind decoder's output and its list of key gaps.
- `SCORES.md`: fact-by-fact scoring.
- `tokens.json`: all counts.
- `NOTES.md`: design record and the next round's fixes.
- round3/ adds baselines/, decodes/, directuse/ (QA test), control_r2/ and FRONTIER_DECODE_PROMPT.md.
- round2/ also includes `facts.json` (the fact list, written before the decode) and `scores.json` (per-fact marks).

Try it: give a fresh AI `key.md` + `payload.txt` and ask for English, Spanish, Chinese, or any other language.
