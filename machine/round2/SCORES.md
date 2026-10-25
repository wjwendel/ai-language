# MNC-r2 blind decode scores

Decoder: a fresh helper with no context, given only key.md (155 o200k tokens) and payload.txt. Output: decoded.blind.md. Scored strictly against facts.json (102 language-neutral facts, written before the decode ran). Each fact is marked kept, distorted or lost. P1 (English source) was decoded into English. P2 (Spanish), P3 (Japanese) and P4 (French) were each decoded twice, into English and back into the source language, and both decodes are scored. Same method as round1/SCORES.md.

Scoring is manual, by the same assistant that built the round. The decode is blind; the scoring is not.

| Decode | Kept | Distorted | Lost | Facts | Kept % |
|---|---|---|---|---|---|
| P1 en → English | 27 | 0 | 0 | 27 | 100.0% |
| P2 es → English | 24 | 2 | 0 | 26 | 92.3% |
| P2 es → Spanish | 24 | 2 | 0 | 26 | 92.3% |
| P3 ja → English | 22 | 1 | 0 | 23 | 95.7% |
| P3 ja → Japanese | 22 | 1 | 0 | 23 | 95.7% |
| P4 fr → English | 26 | 0 | 0 | 26 | 100.0% |
| P4 fr → French | 26 | 0 | 0 | 26 | 100.0% |
| **All English decodes** | **99** | **3** | **0** | **102** | **97.1%** |
| **Source-language decodes (es, ja, fr)** | **72** | **3** | **0** | **75** | **96.0%** |
| **All judgments** | **171** | **6** | **0** | **177** | **96.6%** |

Lost facts: 0. Invented facts: 0.

Not counted as invented (no new facts):
- Letter layout in §1 and §4 ("Hi Sam,", "Hi Théo,", "Hugs, Inès"). The greetings exist in the sources, and the sign-off is in the payload.
- The §3 English decode adds the gloss "(Green Housing Services)" and "(桜町)" beside the romanized names. These are translations.

## Every distortion and its cause
These are 3 distinct facts, each failed in both decodes, for 6 judgments in total.

| # | Passage / decode | Fact | What happened | Cause |
|---|---|---|---|---|
| 1 | P2 → en | 4 **stations** will be installed on the university campus | "4 will be on the university campus". The noun is missing, and the decoder flagged that it could mean 4 bikes. | **Encoder** (primary): the payload `4 in university campus` dropped the noun and the verb (se instalarán). **Key gap**: there is no number-noun binding rule. |
| 2 | P2 → es | same | "y 4 en el campus universitario". "Estaciones" and "se instalarán" were lost. | Encoder + key gap (same as #1) |
| 3 | P2 → en | Ferrer explained the project **cost** (past) ~€1.2M | "the project costs about €1.2 million" (present tense) | **Decoder** (primary): the key says news=past, but the decoder read the `Ferrer:` lines as present-tense reported speech. **Key gap**: the key doesn't define tense or scope for speaker (`X:`) lines, and the English lemma "cost" is tense-ambiguous. |
| 4 | P2 → es | same | "el proyecto cuesta" instead of "costó" | Decoder + key gap (same as #3) |
| 5 | P3 → en | Toilets **cannot** flush during the outage (an inability, which is why residents must store water) | "Do not flush the toilet during the outage" became a prohibition, and the "so store water" link was lost | **Encoder** (primary): it wrote `toilet ! flush` instead of the 1-token lemma `cannot` (rule D2). Under the notice=imperative default, `!` correctly decodes as "don't". |
| 6 | P3 → ja | same | "トイレを流さないでください" instead of "トイレの水も流れませんので" | Encoder (same as #5) |

Cause tally (judgments): encoder primary 4, decoder primary 2. A key gap contributed to all 6. There were no hedge, modal, gender, deadline or number errors. The round-1 failure types (modal, news future, gender, dropped `~`, over-specification) did not recur.

## Borderline calls (judged kept, recorded so they can be challenged)
- **P2 fact 8, "most stations" in the center.** "Most will be…" and "La mayoría estarán…" have no noun. This is the same elision as the source sentence, and the nearest antecedent is "25 stations", so it was judged kept. Strict alternative: mark it distorted for the same cause as #1, which gives **169/177 = 95.5%**. That is still above r1.
- **P2 fact 21, city hall "replied".** It was rendered as "said" / "afirmó", because the encoder wrote `city hall:`. The reply link is implicit from the order of sentences.
- **P3 fact 22, 山本.** The output is correct, but the decoder says it guessed the kanji. This is a key gap: names in kanji aren't carried. Counted as kept, but by luck.
- **P3 fact 21.** The English decode gives a mixed-script name, "Green住宅サービス", plus a gloss. The Japanese decode is exact.
- **P4 fact 5, French.** In "on doit avoir fini le ménage jeudi soir", "au plus tard" is dropped, but the perfect infinitive still sets completion by Thursday evening.
- **Phone numbers (P1, P3).** All digits are exact, but the hyphenation (555-0142, 03-5550-2871) was not restored. This is surface formatting only.
- **P1 `by7 Fri`.** The 24h rule gave 07:00, which is correct here (7 a.m.).
- **P1 fact 21.** Clinic hours of 08:00 to 18:00 match facts.json. Reading "close at 6" as 18:00 was an encoder inference.

Full per-fact marks: scores.json.
