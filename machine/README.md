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

## Round 2, blind-tested (2026-10-25): current best
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

## Honest limits
- There have been two rounds, each on 4 passages of ~200-300 words, with one blind decoder per round. Scoring is manual, by the builder. The passages differ between rounds, so rounds are compared on rates, not as a same-passage A/B test. It is a proxy, not a benchmark, and needs larger, cross-model tests with independent scoring.
- Token counts come from OpenAI tokenizers (o200k, cl100k). Energy has not been measured. The energy claim follows from fewer tokens, not from a meter.
- Round 1's 8 distortions came from missing modals ("should" became a statement), news tense ("will help" became "is helping"), grammatical gender not encoded (vecina became vecino), and the encoder dropping "about." The round-2 fixes are in round1/NOTES.md. None of these failure types recurred in the round-2 blind test, which is one decoder on new passages. Round 2's own failures are listed above.
- MNC is complementary to trained compressors (LLMLingua, gist tokens). It needs no training or model access, and a model can write it as well as read it.

## How it works (core ideas)
1. **The token is the unit.** Every symbol was checked with tiktoken. Whole common words are 1 token, while abbreviations often cost 2–3, so MNC keeps full base-form words and drops anything that carries no fact.
2. **Language-neutral grammar.** Relations are single-token symbols in both tokenizers (`< > ? ! + , / ~ ≥ = : → × # @ §`). Content words act as concept labels, using whichever spelling is cheapest, and are rendered in any output language. Names use the cheapest romanization, and native script is restored on output.
3. **Glued numbers.** A space before a digit costs a token, so the code writes `@1345`, `min10`, `age72`, `×2`.
4. **Defaults over words.** A header such as `§3 news es` sets tense, mood, the default actor and the source language.
5. **Operators for logic:** cause, result, condition, negation, change.

## Files (round1/ and round2/)
- `key.md`: the blueprint (machine-only).
- `payload.txt`: the encoded passages.
- `originals.txt`: the source passages.
- `decoded.blind.md`: the blind decoder's output and its list of key gaps.
- `SCORES.md`: fact-by-fact scoring.
- `tokens.json`: all counts.
- `NOTES.md`: design record and the next round's fixes.
- round2/ also includes `facts.json` (the fact list, written before the decode) and `scores.json` (per-fact marks).

Try it: give a fresh AI `key.md` + `payload.txt` and ask for English, Spanish, Chinese, or any other language.
