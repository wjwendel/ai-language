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

## Honest limits
- This is one round, on 4 passages of ~200 words, with one blind decoder. It is a proxy, not a benchmark, and needs larger and cross-model tests.
- Token counts come from OpenAI tokenizers (o200k, cl100k). Energy has not been measured. The energy claim follows from fewer tokens, not from a meter.
- The 8 distortions came from missing modals ("should" became a statement), news tense ("will help" became "is helping"), grammatical gender not encoded (vecina became vecino), and the encoder dropping "about." The round-2 fixes are in round1/NOTES.md.
- MNC is complementary to trained compressors (LLMLingua, gist tokens). It needs no training or model access, and a model can write it as well as read it.

## How it works (core ideas)
1. **The token is the unit.** Every symbol was checked with tiktoken. Whole common words are 1 token, while abbreviations often cost 2–3, so MNC keeps full base-form words and drops anything that carries no fact.
2. **Language-neutral grammar.** Relations are single-token symbols in both tokenizers (`< > ? ! + , / ~ ≥ = : → × # @ §`). Content words act as concept labels, using whichever spelling is cheapest, and are rendered in any output language. Names use the cheapest romanization, and native script is restored on output.
3. **Glued numbers.** A space before a digit costs a token, so the code writes `@1345`, `min10`, `age72`, `×2`.
4. **Defaults over words.** A header such as `§3 news es` sets tense, mood, the default actor and the source language.
5. **Operators for logic:** cause, result, condition, negation, change.

## Files (round1/)
- `key.md`: the blueprint (machine-only).
- `payload.txt`: the encoded passages.
- `originals.txt`: the source passages.
- `decoded.blind.md`: the blind decoder's output and its list of key gaps.
- `SCORES.md`: fact-by-fact scoring.
- `tokens.json`: all counts.
- `NOTES.md`: design record and round-2 fixes.

Try it: give a fresh AI `key.md` + `payload.txt` and ask for English, Spanish, Chinese, or any other language.
