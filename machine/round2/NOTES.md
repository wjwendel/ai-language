# MNC-r2: machine-native compression, round 2 (blind-tested 2026-10-25)

Token numbers are measured with tiktoken 0.14.0 (o200k_base, cl100k_base) by `measure.py` → `tokens.json`. Everything from "Files" through "Blind decode plan" was written **before** the blind decode and is left unchanged. The blind result, the scores and the round-3 fix list are at the end.

**Test labels used below**
- SELF-TEST: run by the builder, with no decoding by a fresh model. Covers token counts, the E1-E12 token experiments, and selfcheck.py.
- BLIND TEST: a fresh helper with no context got only key.md + payload.txt (decoded.blind.md). Facts kept is measured only by the blind test.

## Files
- originals.txt: 4 fresh passages written natively, new topics. P1 en, pet-sitter note. P2 es, local news (city bike-share launch). P3 ja, apartment water-outage notice (断水のお知らせ). P4 fr, roommate message about moving out.
- payload.txt: all 4 encoded (§1-§4). Non-header lines start with one space (see design change D1).
- key.md: machine-only decoder spec, 6 lines.
- facts.json: language-neutral fact triples, same schema as r1. 102 facts (P1 27, P2 26, P3 23, P4 26). Qualifiers mark the hedge, modal, tense, gender and deadline details that must survive.
- measure.py → tokens.json: per-passage and pooled savings, key tokens, break-even, total (key + payload), r1-key vs r2-key comparison, all experiments E1-E12, and a symbol audit.
- selfcheck.py → selfcheck.out.txt: encoder self-check (fix 8) that diffs numbers and hedges between source and payload.
- experiments/payload_v2a_preprune.txt: first full encode, before pruning and leading-space alignment.
- experiments/key_v2a_fullops.md: key with the full operator table (177/177), the control for E9.

## Exercise coverage (fix list targets present in sources)
Numbers, clock times, money (€, $, decimal comma 0,50, thousands 2.000 / 1 700), phone numbers, hedges (about/around, unas/alrededor/casi, ごろ/ほど, environ/vers), modals (must/should/can't/might/hope; deberán/podrán/espera; してください/しないでください/おそれ/場合がある; doit/peut/devrait/j'espère), future items inside news (empezará, costará, estudiará), present inside news (ahora es peligroso), gendered nouns (una ciclista with no name, so gender is carried only by `.f`; la concejala and la propriétaire, where a name or title already carries gender), possession (Dr. Patel's clinic, each unit's balcony, mon frère, ton abonnement), locations (pantry bottom shelf, under the flowerpot, 1F entrance, under the sink), and at vs by deadlines (by 7 Fri, by ~20, by Nov10, by Thu evening, avant le 30).

## Token table (self-measured)
| P | lang | orig o200k | payload o200k | saved | orig cl100k | payload cl100k | saved |
|---|---|---|---|---|---|---|---|
| P1 | en | 275 | 186 | 32.4% | 278 | 186 | 33.1% |
| P2 | es | 276 | 172 | 37.7% | 338 | 173 | 48.8% |
| P3 | ja | 316 | 148 | 53.2% | 434 | 156 | 64.1% |
| P4 | fr | 256 | 159 | 37.9% | 305 | 162 | 46.9% |
| all | | 1123 | 665 | 40.8% | 1355 | 677 | 50.0% |

- Whole payload file: 669 o200k / 681 cl100k.
- key.md: **155 o200k / 153 cl100k**. r1 key was 186/185, so -17% while adding every fix.
- Break-even (key / (1 - pooled ratio)): **~380 o200k / ~306 cl100k** original tokens. With the r1 key at the r2 ratio it would be 456/370. r1 actual was 477/374.
- Total (key + payload file) vs originals: 824 vs 1123 o200k (**26.6% saved**), 834 vs 1355 cl100k (**38.5% saved**). With the r1 key the total would be 855/866 (cost comparison only; the r1 key cannot decode r2 syntax).
- r1 reference: 39.0% / 49.5% pooled, so payload compression is about flat (+1.8 / +0.5 pts on different passages). The gains are in the key, break-even and total.
- Per-language: English is the hardest to compress (P1 is fact-dense, 27 facts). Japanese gains the most (o200k 53%, cl100k 64%): a notice register with a lot of politeness boilerplate compresses to almost nothing.

## Design changes and why
D1. **Leading-space line alignment (new idea, kept).** Single-token words carry a leading space (" filler"). At line start, after "\n", the bare form can cost 2 ("filler" = 2). Every non-header line now starts with one space. E1: -8 tokens on both tokenizers; no line got worse; no key cost.
D2. **Lemma-over-symbol (new idea, kept).** If a concept already has a 1-token lemma (must, should, can, cannot, might, may, will, now, hope, by, under, over, in, on, next, before), the payload uses the lemma and the key defines nothing. A symbol costs the same 1 payload token plus key tokens plus a new ambiguity. E5 (modal symbols M/S/C/!C/P/F): +3 payload +17 key = **+20 net**, rejected. This is how fixes 1-5 landed with a smaller key.
D3. **Line-scoped tense/modal.** A will/must/etc. at the start of a line scopes the whole line (all ;-clauses). News keeps past as the default. E12, repeating will per clause: +5, so scoping is kept. Fix 4.
D4. **at vs by (fix 1).** `@HMM` = at a clock time (3-4 digits, 24h). `byN` / `by X` = deadline, using the lemma "by" (" by20" = 2 tokens vs "@<20" = 3).
D5. **Split `<` (fix 2).** ` <` means only "because". Under/over/less/more use the lemmas under/over/almost/before (" under10" = 2, the same as "<10").
D6. **Locative/possessive (fix 5).** Spatial prepositions are always written as lemmas (never dropped, the r1 "number fridge" gap). Possessive uses `'s` only where ownership is not predictable. `X:` = says/topic/list (decoder gap: list colon).
D7. **Money/comma (fix 6).** €/$ glued before the number. `€.5` = €0.50 (E7: the 0.50 form costs +2/+1). `M` = million. Comma = list. Unused unit tags dropped from the key.
D8. **Gender (fix 7).** Glued suffix `.f`/`.m` (".f" is 1 token; "cyclist.f" = 2, the same as "female cyclist", E10a). It is used only when the source marks gender and no name or title already carries it. E10b (unmarked) saves 1 but repeats r1 distortions 4/6, rejected.
D9. **`~` discipline + self-check (fix 8).** selfcheck.py diffs source numbers (digits, number words, month names, HMM split, 24h↔12h, phone digit strings) and hedge words per language against payload `~`/almost. Current result: PASS, with one documented waiver (P1 "twice a day", implied by two listed meal times). Mutation test (dropped `~250`, changed €89→€98): both flagged.
D10. **`=` and `→` senses (fix 9).** `=` is/as/for(purpose); `→` becomes/moved to.
D11. **Decoder rule (fix 10).** "never specialize" sits in key line 1.
D12. **Key trimmed to non-obvious rules (new idea, kept pending blind).** Dropped glosses for universally known notation (+ / ≥ × # M, month-day dates, unit list) and kept a single "unitN amount" rule. E9: full-table key 177/177 → shipped 155/153.
D13. **Time chains (kept).** `@` spans + and - (`@7+~17`, `@9-~15`, `@8-18`). E8: unglued forms +3.
D14. **Dates `MonD` / `WkdD` (kept).** Jun3, Nov14, Fri28 = 2 tokens. E6 (`date3 Jun` style): +4.
D15. **Pruning predictable words.** For example: "twice daily" when two times are listed, "close" in an open-close range, "again", and "funds" after "funded". Pre-prune v2a (no leading space) was 685; after pruning (+1 for "during outage" clarity) 677; after D1 669.
D16. **New header slot `[to]`** for msg/notice (addressee). In msg, a bare verb = request to the addressee.

## Measured experiments (all deltas vs shipped payload file, o200k/cl100k)
| ID | variant | delta | decision |
|---|---|---|---|
| E1 | no leading space on lines | +8/+8 | kept leading space |
| E2 | pre-prune v2a (no lead space) | +16/+16 | pruned |
| E3 | ASCII-fold names (Lucia, Theo, Ines, Lefevre, cafe) | -1/-2 | **rejected**: names are facts, so a diacritic loss risks a wrong spelling |
| E4a | ja names fully native script | +3/+6 | rejected |
| E4b | ja names fully romanized/translated (Green Housing Service, Sakuramachi) | 0/-7 | **rejected**: a translation does not round-trip to グリーン住宅サービス; Sakuramachi→桜町/佐倉町 is ambiguous. Shipped mixed form: loanword part romanized, kanji part native |
| E5 | symbolic modals M/S/C/!C/P/F | +3/+3 payload, +17 key, net +20 | rejected |
| E6 | `date3 Jun` dates | +4/+4 | rejected |
| E7 | €0.50 | +2/+1 | rejected |
| E8 | unglued time chains | +3/+3 | rejected |
| E9 | key with full operator table | 177/177 vs 155/153 | trimmed (blind risk) |
| E10a | "female cyclist" | 0/0 | `.f` kept (grammatical, not semantic) |
| E10b | gender unmarked | -1/-1 | rejected (r1 distortions 4/6) |
| E11 | hyphenated phone numbers | +4/+4 | rejected (digits are kept; formatting is surface) |
| E12 | will per clause | +5/+5 | line scope kept |
Also checked (failure): joining lines with ";" or " ;" or " |" instead of newlines gave 0 to -2 on cl100k only. Newline + leading space is better.
Word-level lint: every payload word is 1 token with a leading space except names and flowerpot/councillor (2). No cheaper synonym was found that keeps the same concept.

## Known risks (pre-blind)
- The trimmed key (D12) relies on the decoder knowing + / ≥ × # M Jun3 Fri28 unaided. This is the biggest new risk.
- Gender: `.f` appears once (P2 cyclist). la concejala relies on "Lucía" and la propriétaire on "Mme". If the decoder writes "el concejal" or "le propriétaire", the "name/title carries gender" rule fails.
- The P3 names rely on the decoder rebuilding サンハイツ from "Sun Heights" and keeping 桜町 / 住宅サービス. Yamamoto→山本 is a likely but not certain reading.
- Phone numbers carry digits only; the hyphenation (555-0142, 03-5550-2871) must be restored from convention.
- P1 "twice a day" is implied only by the two times. Clinic "open @8-18" encodes the source's ambiguous "close at 6" as 18:00 (an encoder inference).
- Tense inside news: "users must register" (deberán) sits on a line-initial-will line, so the future should hold; "Ferrer: project cost" relies on news=past.
- "she should return" (P4) relies on the decoder linking "she" to the owner.
- P2 "asked by this paper" must render as "consultada por este diario".
- The payload and key labels are English-spelled 1-token lemmas used as concept IDs; this is a token-cost result, not a readability choice (same as r1).

## Blind decode plan
- The decoder gets only key.md + payload.txt.
- P1 → English.
- P2 → English and Spanish. P3 → English and Japanese. P4 → English and French.
- Score against facts.json (kept / distorted / lost / invented), with special attention to qualifiers (hedge, modal, tense, gender, deadline).

## Round 2 blind result (BLIND TEST, 2026-10-25)
A fresh no-context helper got only key.md (155 o200k) + payload.txt and wrote decoded.blind.md. P1 → English. P2/P3/P4 → English and the source language (Spanish, Japanese, French). The decode ends with a list of 22 "Ambiguities and key gaps". It was scored strictly against facts.json, which was written before the decode. Full marks are in SCORES.md and scores.json. The scoring is manual, by the builder.

Files added after the blind decode: decoded.blind.md (blind output), SCORES.md, and scores.json.

| Decode | Kept | Distorted | Lost | Facts | Kept % |
|---|---|---|---|---|---|
| P1 en → English | 27 | 0 | 0 | 27 | 100.0% |
| P2 es → English | 24 | 2 | 0 | 26 | 92.3% |
| P2 es → Spanish | 24 | 2 | 0 | 26 | 92.3% |
| P3 ja → English | 22 | 1 | 0 | 23 | 95.7% |
| P3 ja → Japanese | 22 | 1 | 0 | 23 | 95.7% |
| P4 fr → English | 26 | 0 | 0 | 26 | 100.0% |
| P4 fr → French | 26 | 0 | 0 | 26 | 100.0% |
| **English decodes** | **99** | **3** | **0** | **102** | **97.1%** |
| **Source-language decodes** | **72** | **3** | **0** | **75** | **96.0%** |
| **All** | **171** | **6** | **0** | **177** | **96.6%** |

0 lost, 0 invented. The greetings and letter layout carry no new facts and were not counted. In the strict alternative, P2 fact 8 counts as distorted, which gives 169/177 = 95.5%.

**Failures (3 facts, each failed in both decodes):**
1. P2 "cuatro [estaciones] se instalarán en el campus" came out as "4 will be on the campus", with no noun. Encoder dropped the noun and verb; key gap: no number-noun binding.
2. P2 "el proyecto costó" came out in the present tense ("costs" / "cuesta"). Decoder ignored news=past on a `Ferrer:` line; key gap: speaker-line tense and scope are undefined.
3. P3 "toilets won't flush (so store water)" came out as a prohibition ("do not flush"). Encoder wrote `! flush` instead of `cannot flush`, and notice=imperative turned it into a command.

**Pre-blind risk check:**
- Trimmed key (D12): held. `+ ≥ × # M Jun3 Fri28` all decoded correctly unaided.
- Gender: held. una ciclista (`.f`), la concejala (by name) and la propriétaire (by Mme) were all correct.
- Hedges: all `~` and "almost" survived (r1 lost 2). The modals must/should/might/may/cannot/hope were all correct (r1 lost 1). Future inside news (will lines) held (r1 lost 2). The `by` deadlines held.
- P3 names: サンハイツ, 桜町, グリーン住宅サービス and 山本 were correct, but 山本 was a guess (the decoder said so).
- Phone numbers: digits exact, hyphens not restored.
- "She should return" (P4): linked to the owner correctly.
- News tense: failed once, at "Ferrer: project cost" (risk listed above; it materialized).

**Efficiency (SELF-TEST measurement, deterministic):**

| | r1 | r2 |
|---|---|---|
| Payload saved, pooled (o200k / cl100k) | 39.0% / 49.5% | 40.8% / 50.0% |
| Key tokens | 186 / 185 | 155 / 153 |
| Break-even (original tokens) | ~477 / ~374 | ~380 / ~306 |
| Key + payload file saved vs originals | 18.8% / 33.1% (762 vs 938, 771 vs 1153) | 26.6% / 38.5% (824 vs 1123, 834 vs 1355) |
| Facts kept (BLIND) | 94.5% (137/145) | 96.6% (171/177) |
| Lost / invented | 0 / 0 | 0 / 0 |

**New-best verdict: r2 is a NEW BEST.** The published rule is "facts kept must not drop, and payload + key tokens must fall, both measured blind". The passages differ between rounds, so the comparison uses rates:
- Facts kept rose from 94.5% to 96.6% (95.5% under the strict alternative), with 0 lost and 0 invented in both rounds.
- Key tokens fell 17%, from 186/185 to 155/153.
- Break-even fell from ~477/~374 to ~380/~306.
- Key + payload savings rose from 18.8%/33.1% to 26.6%/38.5%.
- Pooled payload savings rose slightly, from 39.0%/49.5% to 40.8%/50.0%.

**Caveats:**
- Payload savings are close to flat. The +1.8/+0.5 points are within passage-to-passage variance, so the real win is the key.
- The passages and languages differ (r1: en, en, es, zh; r2: en, es, ja, fr). Japanese compresses well, which flatters r2.
- Each round had one blind decoder, and the scorer is the builder.
- This is not a same-passage A/B test.

## Round 3 fix list (from the 3 blind failures + the decoder's 22 ambiguity notes)
Key changes must be measured in tokens. Keep a change only if blind facts-kept does not drop and key + payload does not grow.
1. **Inability vs prohibition (failure 3).** Encoder rule: inability or status uses the lemma `cannot`/`won't`. `! verb` in a notice or msg means "don't". Add a selfcheck.py lint that flags every `! verb` in notice/msg sections for review.
2. **Speaker lines (failure 2, ambiguity 8).** Key: `X:` covers that line only, with no carry-over to the next lines, and its content takes the section tense (news=past) unless the line starts with will/now. Alternatively, the encoder writes `cost` as past-tense `paid` where cheaper. Also mark "replied" (`reply:`) when the source says so.
3. **Number-noun binding (failure 1, ambiguities 6-7).** Key: a bare `N adj` right after a count = "N of them" (80 electric). A bare `N in place` must repeat the noun lemma (`4 stations in campus`, +1 token). Encoder self-check: every number needs its noun within the clause.
4. **`/` as or vs clause (ambiguity 1).** Key: `;` = clause, `/` = or. The current `line/;=clause` reads as if `/` is a clause break. The decoder guessed right, but only from context.
5. **`~` scope (ambiguity 2).** Key: `~` binds only the next number. In `@7+~17`, only 17 is approximate.
6. **24h everywhere (ambiguity 3).** Key: HMM is 24h in `@` and `by` (by7 = 07:00, by19 = 19:00). The decode was correct, but only because 24h was assumed.
7. **Missing verbs (ambiguity 4).** Encoder: drop a verb only when it is the single obvious one (pill → take). Otherwise keep it. Key: a dropped verb = the most predictable verb.
8. **Kanji and native-script names (ambiguity 12).** Names whose script cannot be rebuilt from romaji (kanji surnames, place names) stay in native script (山本: E4a cost +3/+6 for all P3 names; measure only the kanji names). Katakana loanwords can stay romanized.
9. **Register (ambiguity 22).** Key: register follows the section type (msg = informal, as written; notice = polite/formal; news = neutral). Consider a 1-token header flag only if the blind decoder still guesses wrong.
10. **Phone formatting (ambiguity 15).** Key: `#digits`, formatted by source-locale convention, or accept bare digits as correct. Decide, and state it in the key.
11. **Smaller items:** `manager office` (管理人室 vs 管理事務所, ambiguity 13): keep the source's specific concept lemma when it exists. Dates without a month (ambiguity 16) are acceptable. Speaker "I/we" naming in msg (ambiguity 21) needs no change.
12. **Test protocol.**
    - (a) Run a second blind decoder from a different model family.
    - (b) Re-encode r1 + r2 passages with the r3 key, so the next comparison includes a same-passage A/B.
    - (c) Have an independent scorer re-score at least one round.
