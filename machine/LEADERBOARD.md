# Machine-native code (MNC) leaderboard

All token counts are from tiktoken. Facts kept = strict blind-decode scoring against a language-neutral fact list (a decoder with no context, given only the key and the payload).

| Round | Passages | Payload saved o200k | Payload saved cl100k | Key tokens o200k / cl100k | Break-even (orig tokens) o200k / cl100k | Facts kept (all decodes) | Lost | Invented | Instruction-safety failures | Blind decoder |
|---|---|---|---|---|---|---|---|---|---|---|
| r1 (2026-10-24) | 4 (2 en, 1 es, 1 zh) | 39.0% (938→572) | 49.5% (1153→582) | 186 / 185 | ~477 / ~374 | 94.5% (137/145) | 0 | 0 | not tested | fresh helper subagent |
| r2 (2026-10-25), previous best | 4 (1 en, 1 es, 1 ja, 1 fr) | 40.8% (1123→665) | 50.0% (1355→677) | 155 / 153 | ~380 / ~306 | 96.6% (171/177) | 0 | 0 | not tested | fresh helper subagent (frontier) |
| **r3 MNC3 no key, frontier decode B (2026-10-25): current best** | 5 (1 en, 2 es, 1 ko, 1 de; 2 are assistant instructions) | 33.7% (1082→717) | 45.5% (1346→734) | 0 / 0 | 0 | **100% (178/178)** | 0 | 0 | 0 / 47 | fresh frontier-class helper, no context (may share the encoder's model family) |
| r3 MNC3 + key, frontier decode A | same | 33.7% | 45.5% | 148 / 147 | 439 / 323 | 99.4% (177/178) | 0 | 0 | 0 / 47 | fresh frontier-class helper, no context |
| r3 MNC3 + key (2026-10-25) | 5 (1 en, 2 es, 1 ko, 1 de; 2 are assistant instructions) | 33.7% (1082→717) | 45.5% (1346→734) | 148 / 147 | 439 / 323 | 93.3% (166/178) | 3 | 0 | 1 / 47 | Qwen2.5-7B, local (much weaker) |
| r3 MNC3 micro-key | same | 33.7% | 45.5% | 41 / 41 | 122 / 90 | 94.9% (169/178) | 1 | 0 | 3 / 47 | Qwen2.5-7B, local |
| r3 MNC3 no key | same | 33.7% | 45.5% | 0 / 0 | 0 | 96.1% (171/178) | 4 | 0 facts (2 pleasantries) | 0 / 47 | Qwen2.5-7B, local |
| control: r2 code on Qwen2.5-7B | r2's 4 | – | – | 155 / 153 | – | 80.8% (143/177) | – | – | – | Qwen2.5-7B, local |

r1 per language (o200k / cl100k saved): en 41.5% and 46.2% / 41.4% and 45.8%; es 44.9% / 53.2%; zh 22.7% / 53.7%.

r2 per language (o200k / cl100k saved): en 32.4% / 33.1%; es 37.7% / 48.8%; ja 53.2% / 64.1%; fr 37.9% / 46.9%.

r3 per passage (o200k / cl100k saved): P1 en instructions 22.4% / 22.5%; P2 es 33.9% / 43.4%; P3 ko 44.7% / 62.3%; P4 de 35.1% / 48.1%; P5 es instructions 29.1% / 34.8%.

Key + payload vs originals: r1 18.8% / 33.1% saved; r2 26.6% / 38.5% saved; r3 20.1% / 34.5% (key), 29.9% / 42.4% (micro-key), 33.7% / 45.5% (no key).

**r3 is the new best, in its no-key form.** A fresh frontier-class helper with no context decoded the payload with no key and kept all 178 fact checks: 0 lost, 0 invented, 0 instruction-safety failures. Key + payload tokens are 717 / 734, against r2's 820 / 830 (33.7% / 45.5% saved vs 26.6% / 38.5%). With the key, the same kind of helper kept 99.4%, but the key's cost puts its savings (20.1% / 34.5%) below r2, so that version does not qualify. Limits: the helper may share the encoder's model family, scoring is by the builder alone, the passages differ from r2's, and the no-key decode still relies on a 36-token task instruction (30.4% / 42.8% saved if counted).

Earlier result on a local 7B decoder: **not a new best by the rule.** Its best config (no key) keeps 96.1% of facts, below r2's 96.6%, even though key + payload tokens fell. The comparison is confounded: r3 was decoded blind by a much weaker local 7B model, which scores r2's own code at only 80.8%. r2 stays the best until a frontier blind decode of r3 is run. Baselines, instruction-safety and direct-use results are in round3/SCORES.md.

**Why r2 is the new best:** blind facts kept rose from 94.5% to 96.6% (0 lost, 0 invented in both rounds), the key shrank from 186 to 155 tokens, and break-even fell from ~477 to ~380 (o200k). The passages differ between rounds, so the comparison uses rates. Payload savings are about flat (+1.8 / +0.5 points), so the gain comes from the key.

Reference: human-readable AIL v2.3 saved 16.4% (o200k) on blind encode, with a ~1.2k-token key.

Instruction-safety = any lost or flipped negation, condition, permission, actor, deadline or identity in the assistant-instruction passages (r3 onward).

Rule for a new best: facts kept must not drop, and payload + key tokens must fall, both measured blind.
