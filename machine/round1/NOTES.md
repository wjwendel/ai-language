# MNC-r1: machine-native compression, round 1

All counts come from tiktoken (o200k_base, cl100k_base) via `measure.py`, which writes `tokens.json`. Nothing has been decoded yet. A separate blind decoder will get only `key.md` + `payload.txt`.

## Files
- originals.txt: 4 everyday passages written natively. P1 en household plan, P2 en how-to (repotting), P3 es local news (bakery fire), P4 zh family trip plan.
- payload.txt: all 4 encoded (one file, sections §1-§4).
- key.md: machine-only decoder spec (no human prose). Earlier human-readable version saved as experiments/key_v1_humanprose.md (585/594 tokens).
- facts.json: language-neutral fact triples (96 facts: 25/22/21/28) for scoring.
- tokens.json, measure.py: measurements.
- experiments/native_lemma_{es,zh}.txt: same code, but content words kept in the source language (control test).

## Token table
| P | lang | orig o200k | payload o200k | saved | orig cl100k | payload cl100k | saved |
|---|---|---|---|---|---|---|---|
| P1 | en | 224 | 131 | 41.5% | 227 | 133 | 41.4% |
| P2 | en | 238 | 128 | 46.2% | 238 | 129 | 45.8% |
| P3 | es | 247 | 136 | 44.9% | 295 | 138 | 53.2% |
| P4 | zh | 229 | 177 | 22.7% | 393 | 182 | 53.7% |
| all | | 938 | 572 | 39.0% | 1153 | 582 | 49.5% |

Whole payload file (with headers/newlines between sections): 576 o200k / 586 cl100k.
key.md (machine-only): 186 o200k / 185 cl100k, down from 585/594 for the human-prose v1 (-68%). Break-even (key / (1 - pooled ratio)): about 477 original tokens on o200k, 374 on cl100k (v1 was 1,499 / 1,199). (AIL v2.3: ~1.2k-token key, breaks even at ~4k-12k.)
Reference: AIL v2.3 blind encode saved 16.4% (o200k). r1 English alone saves 41-46%.

## Per-language findings
- Spanish costs more than English as raw text (cl100k: 295 for 189 words), but it encodes into about the same payload size as English. So non-English input saves more: es 53.2% on cl100k and 44.9% on o200k.
- Chinese on cl100k: 393 → 182 (53.7%), the biggest saving. On o200k, Chinese is already dense (229 tokens for 311 characters), so the saving drops to 22.7%. The newer tokenizer narrows the gap.
- Control test, keeping source-language content words with the same symbols: es 157/188 (36.4%/36.3%) and zh 220/331 (3.9%/15.8%). Both are worse than the pivot labels. So using cheapest-token concept labels is a measured win, not a habit. Chinese content words alone barely compress on o200k.

## Design ideas (and why)
0. **Key is a machine spec.** Telegraphic rules, symbol tables, no explanations or examples; any AI that loads it can still render plain language, which is how audits happen.
1. **Tokens are the unit, not letters.** Every choice was checked with tiktoken. Whole common words with a leading space are 1 token, while abbreviations often cost 2-3, so the code keeps full lemmas and drops only words that carry no facts (articles, auxiliaries, most prepositions, pronouns, tense).
2. **Language-neutral grammar plus cheapest-token concept labels.** Relations use only symbols that are verified single tokens in both tokenizers (with a leading space): `< > ? ! + , / ~ ≥ = : → × # @ §`. Content slots hold the cheapest single-token label for each concept. Because of how the tokenizers were built, those labels happen to be spelled as English lemmas, but they work as concept IDs: the decoder renders them in any requested language. Names use the cheapest standard romanization or exonym, and the native script is restored on output.
3. **Number gluing.** A space before a digit costs its own token (" 9" = 2), so numbers are glued to a symbol or unit: `@9`, `@1345`, `min10`, `age72`, `in12`, `×2`. Unit-before-number form (`in2`) is 2 tokens, while "2in" or "2 inches" cost 3.
4. **Defaults instead of words.** The `§N type lang` header sets mood/tense and the default actor (plan → I/future, news → past/3rd person, howto → you/imperative). One line or `;` is one clause, and an actor carries across `+`/`>`. That removes most pronouns and all tense markers.
5. **Logic as operators.** Cause `<`, result/then `>`, condition `? A > B`, negation `!`, change `→`. Each replaces multi-token phrases like "because the", "if ... then", "do not", "will now be moved to".

## Known risks / losses to check in blind decode
- Surface loss by design: exact wording, emphasis, and some grammatical gender (P3 "vecina" is encoded as gender-free `neighbor`, so a Spanish decode may say "vecino").
- Ambiguity spots: `@430` (4:30 a.m., which the 24h rule covers), `date11`, actor carry-over in P1 line 2 (Maya vs writer for recycling; the rule says `;` resets to default actor "I").
- The key is now machine shorthand (owner rule: nothing needs to be human-readable; auditability = any AI with the key decodes to plain language). Its terse rules are the biggest new risk: the blind decode tests whether 186 tokens is enough.
- Key tokens are tracked as a first-class metric next to payload tokens; every future round reports both.
- The payload still looks word-like only because single-token English lemmas are the cheapest tokens; that is a token-cost result, not a readability choice.

## Blind decode plan (for the next step)
- The decoder gets only key.md + payload.txt.
- P1, P2: decode to English.
- P3 (es) and P4 (zh): decode **both into English and back into their source language** (Spanish, Simplified Chinese), to test language-neutral round trips.
- Score against facts.json: fraction of facts intact, wrong, or missing, plus any invented facts.

## Round 1 blind result
94.5% of 145 fact judgments kept, with 0 lost and 0 invented. English decodes kept 94.8% (91/96) and source-language decodes kept 93.9% (46/49). See SCORES.md. All 8 distortions trace to 4 causes: missing modals, news tense, gender not encoded, and the encoder dropping `~`.

## Round 2 fix list (from scored distortions + decoder's reported key gaps)
1. **`@` at vs by.** `@N` = at; add a deadline form (`@<N` = by/before N). Spell out that HMM may be 3 or 4 digits (@630 = 6:30).
2. **Split `<`.** Keep ` <` = because only. Under/less-than gets its own token (e.g. `lt`-style glued prefix or `≤`); check single-token cost first.
3. **Modals.** Add compact marks for must/should/can/can't/want/hope (e.g. `!` stays plain "not", and a prefix set such as `M`=must, `S`=should, `C`=can, `!C`=can't). Measure the token cost. Fixes distortion 1 and decoder gaps 7, 23.
4. **Tense inside news.** Default stays past; add a future/plan mark and a "now/current" mark (e.g. `+>` future). Fixes distortions 5 and 7.
5. **Location/possession.** Add one locative operator (on/at/in) and one possessive (X's), and define the list colon separately from `X:` (said/handles).
6. **Define `¥`/currency** and the comma; drop unused unit tags (`y`) from the key to save tokens.
7. **Gender / grammatical features.** Add an optional feature suffix for gendered languages (e.g. `neighbor.f`). Use it only when the source marks gender, and measure the cost. Fixes distortions 4 and 6.
8. **Encoder discipline.** Every "about/approximately" in the source must become `~` (distortions 2 and 3). Add an encoder self-check that diffs numbers and hedges against the source.
9. **`=` and `→` senses.** `=` also serves "for/as" (purpose) and `→` "replaced by / moved to"; state both in one line.
10. **Decoder rule.** "Never upgrade a generic noun to a more specific one" (distortion 8).
Each fix must keep the key small: report key tokens and payload tokens together, and keep a change only if facts-kept rises without a net token loss.
