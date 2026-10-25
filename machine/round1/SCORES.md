# MNC-r1 blind decode scores

Decoder: a helper with no context, given only key.md (186 o200k tokens) and payload.txt. Scored strictly against facts.json (96 language-neutral facts). Each fact is marked kept, distorted or lost. P3 (Spanish source) and P4 (Chinese source) were each decoded twice, into English and back into the source language, and both decodes are scored.

| Decode | Kept | Distorted | Lost | Facts | Kept % |
|---|---|---|---|---|---|
| P1 en → English | 24 | 1 | 0 | 25 | 96.0% |
| P2 en → English | 20 | 2 | 0 | 22 | 90.9% |
| P3 es → English | 19 | 2 | 0 | 21 | 90.5% |
| P3 es → Spanish | 19 | 2 | 0 | 21 | 90.5% |
| P4 zh → English | 28 | 0 | 0 | 28 | 100.0% |
| P4 zh → Chinese | 27 | 1 | 0 | 28 | 96.4% |
| **All English decodes** | **91** | **5** | **0** | **96** | **94.8%** |
| **Source-language decodes (es, zh)** | **46** | **3** | **0** | **49** | **93.9%** |
| **All judgments** | **137** | **8** | **0** | **145** | **94.5%** |

Lost facts: 0. Invented additions: 0. The decoder listed its inferences under "Ambiguities and key gaps" instead of adding facts.

## Every distortion and its cause
| # | Passage / decode | Fact | What happened | Cause |
|---|---|---|---|---|
| 1 | P1 en | nobody should make plans after 17:00 | Became a statement: "We have no plans after 17:00" | Key gap: no modal/obligation marker |
| 2 | P2 en | pot about 2 inches wider | Decoded as exactly "2 inches" | Encoder dropped `~` (in2) |
| 3 | P2 en | root ball top about 1 inch below rim | Decoded as exactly "1 inch" | Encoder dropped `~` (in1) |
| 4 | P3 en | neighbor is female (vecina) | Gender-neutral "neighbor" | Gender not encoded (encoder/key gap) |
| 5 | P3 en | city hall will offer help | "is helping" | Key gap: news = past, no future/plan marker |
| 6 | P3 es | una vecina | "un vecino" (wrong gender) | Gender not encoded |
| 7 | P3 es | ofrecerá ayuda | "está ayudando" | Key gap: news tense |
| 8 | P4 zh | 下午三点的火车 (train) | "坐高铁" (bullet train) for the return | Decoder over-specified, carrying over "bullet train" from the outbound leg |

Cause tally: key gaps 3 (modal 1, news tense 2), gender not encoded 2, encoder drops 2, decoder over-specification 1.

## Judged equivalent (not penalized)
- P1 fact 9 is kept implicitly ("Leo has a soccer game. Daniel will drive").
- "Sensitive stomach" / 肠胃不好 for weak stomach.
- "Until 12:00" for "until noon".
- Accent restored on Río.
- All Chinese place names and 小明 came out correct.

Full per-fact marks: scores.json.
