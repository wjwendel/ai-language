# AIL: Less Energy for Every AI Conversation

**A training-free, model-agnostic, human-readable context-compression language that any LLM learns in-context from one file, then reads *and writes*.**

*Concept: Jordan Wendelken. Built and maintained by AI. Free and open under [CC BY 4.0](LICENSE).*

---

## The problem
Inference cost scales with tokens. Every turn, a model re-processes its context (prefill), and every generated token is a sequential, autoregressive decode step. Longer contexts also enlarge the KV cache and the attention compute that grows with sequence length. Much of everyday natural-language context is redundancy that carries little meaning for a model: articles, copulas, greetings, hedges, repeated first-person subjects. At global scale, those tokens are compute, latency and energy spent for nothing.

## What AIL is
AIL is a compact, rule-based notation for notes, memory, long context and agent-to-agent handoffs. A single ~1.2k-token specification ([`LEARN-AND-USE.md`](LEARN-AND-USE.md), also as a [PDF](LEARN-AND-USE.pdf)) teaches any capable LLM the grammar through in-context learning. No fine-tuning, no trained compressor, no logit or weight access, no tool calls. The model replies `LOADED` and from then on can **COMPRESS** (encode) and **EXPAND** (decode) zero-shot.

Compression is lossy at the surface (articles, filler, some tense nuance) but designed to be **semantically faithful**: facts, actors, negation, modality, numbers, conditionals and causal links are kept by rule.

## Why it matters
1. **Energy (the main application).** Fewer tokens processed and generated means less inference compute per conversation. The effect compounds across long sessions, agent memory and multi-agent pipelines, where the same context is re-read many times.
2. **Latency.** Shorter prompts cut prefill time. Because AIL is also *generated* by the model, it shortens decode, the slower, sequential and more expensive side of inference, which input-only compressors don't touch.
3. **Learnability and portability.** One file, any model. Claude and Grok each learned it from the spec alone, with no clarifying questions, and used it on the next turn. It works in closed, API-only and consumer chat models where methods that need model internals can't run.
4. **Iterative refinement, already shown.** AIL is improved in versioned rounds by AI. A change is kept only if it beats the current best in blind tests. Across five tested versions, each round found real failures (for example pronoun and subject drift such as "we" becoming "I", and lost actors in imperatives) in blind and cross-model tests, and fixed them. v2.3 reaches 4/4 meaning preserved on blind round-trip reconstruction. One canonical, permanent home means improvements propagate to every copy.

## How it compares
| | AIL | LLMLingua / LLMLingua-2 | Gist tokens | ICAE |
|---|---|---|---|---|
| Reported compression | ~1.1-1.5× (10-35%) | up to 20× / 2-5× | up to 26× | ~4× |
| Training or model access needed | None (in-context only) | Small LM compressor | Fine-tuned model | Trained encoder |
| Works in closed chat models | Yes | Input side only, via pre-processing | No | No |
| Compresses model output (decode) | Yes, the model writes it | No | No | No |
| Human-readable, auditable | Yes | Partly (token-pruned text) | No (soft tokens) | No (memory slots) |
| Model-agnostic | Yes, the same file for every model | Yes, for input | No | No |

Figures for other methods are as reported in their papers. AIL isn't the strongest compressor. It's a different point in the design space: zero-infrastructure, bidirectional and readable. It is **complementary**: AIL text can still be token-pruned or optically compressed on top.

## Try it in 30 seconds
1. Upload or paste [`LEARN-AND-USE.md`](LEARN-AND-USE.md) into any AI chat. It replies **LOADED**.
2. **COMPRESS** + text gives AIL. **EXPAND** + AIL gives plain English.

> Plain: *My car is in the shop until Thursday, so I can't drive the kids to practice on Tuesday. Can you take them? If not, I'll ask Lisa. I also need milk and bread.*
>
> AIL: `my car in shop until Thursday > can't drive kids to practice Tuesday / can you take them? / if not, I'll ask Lisa / need milk, bread`
>
> 39 → 31 tokens (o200k_base), every fact kept.

## Evaluation (honest, early)
- **Method:** blind round-trip reconstruction. A fresh model given only the spec encodes unseen everyday passages, and a separate fresh model given only the spec plus the encodings decodes them. Meaning is judged on facts, actors, negation, numbers and intent. Tokens are counted with tiktoken (o200k_base and cl100k_base).
- **Compression:** typically 10-35% fewer tokens on everyday text, more on verbose messages and less on dense factual text. v2.3 blind encode: 16.4% (195 → 163 o200k). A Claude cross-model test cut a short note by 37% (46 → 29).
- **Fidelity:** v2.3 blind decode was 4/4 semantically intact, with differences limited to articles and tense nuance.
- **Amortization:** the spec costs ~1.2k tokens to load, so break-even is roughly 4k-12k tokens of plain context. It's built for long contexts, persistent memory and handoffs, not one-line chats.
- **Limits:** small test sets. No downstream task benchmarks yet (QA or summarization accuracy on compressed context), and no measured energy or latency figures. These are the next steps, and contributions are welcome.

All passages, encodings, decodings and the measuring script are in [`tests/`](tests/).

## Contribute
Run it on your own text and models, report compression and fidelity, and open an issue with failures or ideas. Benchmarks on long-context tasks are especially welcome. Extensions follow the EXTEND rule in the spec, and the best changes become the next version for everyone.
