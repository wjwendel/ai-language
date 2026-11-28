# MNC: a machine-native compression code for AI

*Concept: Jordan Wendelken, a business developer and entrepreneur. Designed and measured by AI. Same license as this repository (CC BY 4.0).*

## The picture: teleportation for meaning
Break a message into its atoms. Send only the smallest form that still holds every atom. Reassemble it intact on the other side, in any language. The **key** is the blueprint: one small spec that tells any AI how to put the atoms back together.

AIL (the rest of this repo) is written so people can read it. MNC drops that constraint. Every choice is driven by token cost, because fewer tokens mean less compute, lower latency and less energy. MNC stays auditable in a different way: any AI given the key can decode the payload to plain language, in whatever language you ask for.

## Latest round: round 40, fully blind (2026-11-28)
- **Setup:** an independent helper wrote four new passages (English, Chinese, Spanish, Hindi; three are instructions to an assistant, one is an everyday notice) and 59 questions, sealed until both encodings were hashed.
- **Result:** the main form (MNC28, unchanged since round 31) was 27.2% smaller on o200k (53.8% on cl100k) and scored 59/59 in both runs. The experimental form (MNC28x-R40, which adds rules to keep job titles and place scope in everyday notices and to transliterate non-Latin names) was 33.4% / 58.6% smaller and also scored 59/59 in both runs. Terse plain English was smaller (38.9% / 62.7%) and scored 59/59 in both runs, so it still wins on savings. A "summarize this" prompt scored 57/59 (it turned a "should" into a requirement), and LLMLingua-2 scored 89.8% / 78.0% at 34.7% / 50.0% smaller (o200k).
- **Safety check:** two blind decodes of MNC28 back to prose kept all 194 judged facts, so MNC28 passes again (counter 2 of 3 on our project-internal bar). The experimental form's decodes kept every safety fact this time (one plain fact lost: the notice's addressee), fixing round 39's problem, but it saves less than terse English, so it is not adopted.
- **Limits:** one reader family, 1-2 runs; small-local-model runs for this round and the older frozen benchmark are pending. Round 39's small-model runs: MNC28 64-69%, MNC28x 72-74%, original 67%. Full numbers: round40/SCORES.md and LEADERBOARD.md.

## Round 39, fully blind (2026-11-28)
- **Setup:** an independent helper wrote four new passages (English, Korean, Italian, Arabic; three are instructions to an assistant, one is an everyday notice) and 58 questions, sealed until both encodings were hashed.
- **Result:** the main form (MNC28, unchanged since round 31) was 29.8% smaller on o200k (49.9% on cl100k) and scored 58/58 in both runs. The experimental form (MNC28x, now built as terse English first with only safety rails added) was 40.0% / 57.0% smaller and scored 58/58 and 57/58; the one miss named the right person, but in Arabic script, which our Latin-only answer check did not accept. Terse plain English was slightly smaller (41.5% / 59.0%) and scored 58/58 in both runs, so it still wins on savings. LLMLingua-2 was 33.5% / 48.9% smaller (o200k) and scored 98.3% / 87.9%; at 0.66 it turned a "should" into "required".
- **Safety check:** two blind decodes of MNC28 back to prose kept every safety fact (195 of 196 judged facts; the only loss was the word "shared"), so MNC28 passes again and its counter is 1 after the round-38 fail. The experimental form's decodes dropped a person's job title in the Korean notice, so it is not adopted.
- **Limits:** one reader family, 1-2 runs; small-local-model runs for this round and the older frozen benchmark are pending. Round 38's small-model runs came in as ties (MNC28 63-67%, MNC28x 67-70%, original 68-70%). Full numbers: round39/SCORES.md and LEADERBOARD.md.

## Round 38, fully blind (2026-11-28)
- **Setup:** an independent helper wrote four new passages (English, Japanese, German, Thai; three are instructions to an assistant, one is an everyday notice) and 60 questions, sealed until both encodings were hashed.
- **Result:** the main form (MNC28, unchanged since round 31) was 14.4% smaller on o200k (38.0% on cl100k) and scored 59/60 in both runs. The experimental form (MNC28x, now "terse English plus safety rails", no key) was 24.2% / 46.1% smaller and scored 60/60 in both runs. Terse plain English was smaller still (39.9% / 59.3%) and also scored 60/60, so it wins on savings this round. LLMLingua-2 was 39.9% / 52.3% smaller (o200k) but scored 73.3% / 70.0%; it lost most of the Japanese passage.
- **Safety check:** MNC28 failed this round. Its encoding put a date limit in parentheses after a list of three items ("clappers + flashlights + vests (only for those who applied by Dec 20)"). Both readers and both blind decodes applied the limit to all three items, but the original limits only the vests. The strict check counts that as a safety error, so MNC28's streak of fully blind passes ends at seven (rounds 31-37) and its counter restarts at 0. The experimental form kept all 224 judged facts in both decodes but saves less than terse English, so it is not adopted.
- **Limits:** one reader family, 1-2 runs; small-local-model runs for this round and the older frozen benchmark are pending. Full numbers: round38/SCORES.md and LEADERBOARD.md.

## Round 37, fully blind (2026-11-28)
- **Setup:** an independent helper wrote four new passages (English, Chinese, French, Vietnamese; three are instructions to an assistant, one is an everyday notice) and 59 questions (more than before, so differences can show), sealed until both encodings were hashed.
- **Result:** the main form (MNC28, unchanged since round 31) was 16.9% smaller on o200k (29.7% on cl100k) and answered 59/59 in both runs. The experimental form (MNC28x, trying one shared layout key for all instruction sections) was 29.1% / 43.5% smaller, also 59/59 in both runs. Terse plain English was smaller still (35.9% / 48.4%) but scored 58/59 in both runs: it attached a Chinese date limit to both items when it applied to only one. LLMLingua-2 was 35.8% / 50.0% smaller (o200k) but scored 88.1% / 81.4%. The originals were already compact this round, so every form saved less than in round 36.
- **Safety check:** two blind decodes of MNC28 back to prose kept all 189 judged facts. This is MNC28's seventh consecutive fully blind round at 100% on our instruction-safety check (a project-internal bar, not a general guarantee). The experimental form's decode dropped who a permission applies to ("a customer"), so it is not adopted, and it still saves less than terse English.
- **Limits:** one reader family, 1-2 runs, terse English's miss is one question; small-local-model runs for this round and the older frozen benchmark are pending. On the small local model, round 36's results came in: MNC28 81.6% on all 3 runs vs 63.2-68.4% for the original. Full numbers: round37/SCORES.md and LEADERBOARD.md.


## Round 36, fully blind (2026-11-28)
- **Setup:** an independent helper wrote four new passages (English, Korean, Brazilian Portuguese, Hindi; three are instructions to an assistant, one is an everyday notice) and 38 questions, sealed until both encodings were hashed.
- **Result:** the main form (MNC28, unchanged since round 31) was 21.6% smaller on o200k (48.5% on cl100k) and answered 38/38 in both runs. Terse plain English was smaller (42.1% / 65.6%) at the same 38/38, so it beat the main form on savings again. The experimental form (MNC28x) was 39.6% / 63.1% smaller at 38/38 in both runs, so terse English also beat it this round (by 2.5 points). LLMLingua-2 was 34.6% / 49.6% smaller (o200k) but scored 92.1% / 89.5%, mixing up which Korean item a date applied to. Two shared scorer fixes were applied to every text alike (recorded in SCORES.md).
- **Safety check:** two blind decodes of MNC28 back to prose kept 212 of 213 judged facts with no safety-relevant changes (one decoder added "for the first time" to an everyday detail). This is MNC28's sixth consecutive fully blind round at 100% on our instruction-safety check (a project-internal bar, not a general guarantee). The experimental form's two round-35 decode slips did not recur, but it dropped a few minor words and turned one "should" into "must", so it is not adopted.
- **Limits:** one reader family, 2 runs, questions easy for every faithful text; small-local-model runs and the older frozen benchmark were not finished this round. Full numbers: round36/SCORES.md and LEADERBOARD.md.

## Round 35, fully blind (2026-11-27)
- **Setup:** an independent helper wrote four new passages (English, Japanese, Spanish, Arabic; three are instructions to an assistant, one is an everyday notice) and 40 questions, sealed until both encodings were hashed.
- **Result:** the main form (MNC28, unchanged since round 31) was 20.1% smaller on o200k (40.8% on cl100k) and answered 40/40 in both runs. Terse plain English was smaller (37.7% / 56.6%) at the same 40/40, so it beat the main form on savings again. The experimental form (MNC28x) was 40.1% / 57.9% smaller at 40/40 in both runs, slightly smaller than terse English (by 2.4 / 1.3 points), but its blind decode changed one safety fact (a "not the shaper" role became "not a shaper"), so it is not adopted. LLMLingua-2 was 40.0% / 52.7% smaller but scored 75.0% at both settings, losing most of the Japanese facts and naming an approver the text does not name. One shared scorer fix (a bare "not stated" counted correct where the text does not name the approver) was applied to every text alike; before it, most faithful texts scored 38/40 (recorded in SCORES.md).
- **Safety check:** two blind decodes of MNC28 back to prose kept all 193 judged facts with no meaning changes. This is MNC28's fifth consecutive fully blind round at 100% on our instruction-safety check (a project-internal bar, not a general guarantee).
- **Limits:** one reader family, 2 runs, questions easy for every faithful text; on a small local model (3 runs) MNC28 scored 65.0% vs 62.5% for the original (a one-question margin) and MNC28x 62.5-65.0%; the older frozen benchmark was not run. Full numbers: round35/SCORES.md and LEADERBOARD.md.

## Round 34, fully blind (2026-11-22)
- **Setup:** an independent helper wrote four new passages (English, Chinese, German, Indonesian; three are instructions to an assistant) and 40 questions, sealed until both encodings were hashed.
- **Result:** the main form (MNC28, unchanged since round 31) was 16.8% smaller on o200k (23.4% on cl100k) and answered 40/40 in both runs. Terse plain English was smaller (36.3% / 44.4%) at the same 40/40, so it won on savings again. The experimental form (MNC28x) was 33.1% / 41.7% smaller but missed one safety question in both runs (it separated a Saturday limit from its approver), so that change was rejected. LLMLingua-2 was 33.1% / 47.0% smaller but scored 82.5% / 62.5% with safety errors. The original text answered 40/40 after three shared scorer fixes (recorded in SCORES.md).
- **Safety check:** two blind decodes of MNC28 back to prose kept all 170 judged facts with no meaning changes. This is MNC28's fourth consecutive fully blind round at 100% on our instruction-safety check (a project-internal bar, not a general guarantee).
- **Limits:** one reader family, 2 runs, questions easy for every faithful text; on a small local model (3 runs) MNC28 scored 62.5-65.0% vs 50.0-52.5% for the original; the older frozen benchmark was not run. Full numbers: round34/SCORES.md and LEADERBOARD.md.

## Round 33, fully blind (2026-11-22)
- **Setup:** an independent helper wrote four new passages (English, Korean, French, Vietnamese; three are instructions to an AI assistant, one is an everyday notice) and 39 questions, sealed until the compressed forms were written. Readers were fresh helpers with no other context (one model family, 2 runs each for the main texts).
- **Result:** the main form (MNC28, unchanged since round 31) was 22.3% smaller on o200k (32.7% on cl100k) and answered 39/39 in both runs. Terse plain English was smaller (42.4% / 55.6%) at the same 39/39, so it won on savings again. The experimental form (MNC28x) was 41.6% / 55.0% smaller at 39/39, about a tie with terse English. LLMLingua-2 was 34.2% / 48.7% smaller but scored 92.3% / 84.6% and made safety errors. The original text answered 39/39 (38/39 before one shared scorer fix, recorded in SCORES.md).
- **Safety check:** two blind decodes of MNC28 back to prose made no safety-relevant errors (one decoder widened one everyday detail). This is MNC28's third consecutive fully blind round at 100% on our instruction-safety check, which is the bar this project set for trying it on live instructions. That is a project-internal bar, not a general guarantee.
- **Limits:** one reader family, 2 runs, questions easy for every faithful text; on a small local model (3 runs) MNC28 scored 66.7-76.9% vs 53.8% for the original; the older frozen benchmark was not run. Full numbers: round33/SCORES.md and LEADERBOARD.md.

## Previous round: round 32, fully blind (2026-11-21)
- **Setup:** an independent helper wrote four new passages (English, Japanese, Spanish, Turkish; three are instructions to an AI assistant, one is an everyday notice) and 40 questions, sealed until the compressed forms were written. Readers were fresh helpers with no other context (one model family, 2 runs each for the main texts).
- **Result:** the main form (MNC28, unchanged since round 31) was 24.7% smaller on o200k (31.5% on cl100k) and answered 40/40 in both runs. Terse plain English was smaller (39.0% / 49.3%) at the same 40/40, so it won on savings again. The experimental form (MNC28x) was 36.8% / 47.5% smaller at 40/40, close to terse English. LLMLingua-2 was 43.7% / 54.8% smaller but scored 77.5% / 70.0%, and the 0.5 setting made safety errors. The original text answered 40/40 (38/40 before two scorer corrections, recorded in SCORES.md).
- **Safety check:** two blind decodes of MNC28 back to prose kept all 147 judged facts with no meaning changes. MNC28's readiness count is 2 of 3.
- **Limits:** one reader family, 2 runs, questions easy for every faithful text; a small local model (3 runs) scored all texts within each other's spread; the older frozen benchmark was not run. Full numbers: round32/SCORES.md and LEADERBOARD.md.

## Earlier round: round 31, fully blind (2026-11-21)
- **Setup:** an independent helper wrote four new passages (English, Chinese, Italian, Polish; three are instructions to an AI assistant, one is an everyday notice) and 39 questions, sealed until the compressed forms were written. Readers were fresh helpers with no other context (one model family, 2 runs each for the main texts).
- **Result:** the new main form (MNC28) was 28.1% smaller on o200k (30.8% on cl100k) and answered 39/39 in both runs. Terse plain English was smaller (37.6% / 44.5%) at the same 39/39, so it won on savings this round. An experimental, more aggressive form (MNC28x) was 38.5% / 41.1% smaller at 39/39 — about a tie with terse English. LLMLingua-2 was 33.2% / 48.2% smaller at 87.2% / 69.2% and dropped emergency steps. The original text answered 39/39.
- **Safety check:** two blind decodes of MNC28 back to prose kept all 205 judged facts with no meaning changes. MNC28's readiness count is 1 of 3.
- **Limits:** one reader family, 2 runs, questions easy for every faithful text; the small local model and the older frozen benchmark were not run this round. Full numbers: round31/SCORES.md and LEADERBOARD.md.

## Previous round: round 30, fully blind (2026-11-20)
- **Test set:** 4 passages by an independent no-context author: English, Korean, Portuguese, Dutch (3 are instructions for an AI assistant, with look-alike "distractor" rules). 38 sealed questions, 28 of them safety questions.
- **Readers:** fresh no-context frontier-model helpers (one model family), no key.
- **Result:** the new main form (MNC27) was 36.6% smaller on o200k (49.7% on cl100k) and answered 38/38 in both runs. Terse plain English was 28.7% smaller and summarize-style compression 30.6% smaller, both 38/38. LLMLingua-2 was 34.3% / 49.3% smaller at 97.4% / 92.1% (the 0.5 setting missed a safety question). The original text answered 38/38. One scorer regex was corrected for every text alike.
- **Safety check:** two blind decodes of MNC27 back to prose each had 2 meaning slips in the everyday Korean notice, both caused by the encoder (it dropped a "must" and shortened "complaints or inquiries" to "questions"). The instruction passages had none. Under the strict rule this counts as a fail, so MNC27's readiness count is 0 of 3.
- **Limits:** one reader family, 2 runs, questions easy for every faithful text; the older frozen benchmark was not run on MNC27. Full numbers: round30/SCORES.md and LEADERBOARD.md.

## Round 29, fully blind (2026-11-20)
- English, Japanese, Spanish, Turkish; 39 sealed questions. The frozen main form MNC26 was 29.0% smaller (o200k) and answered 39/39 in both runs with no safety errors in two blind decodes. That was its third clean fully blind round in a row (rounds 27-29), which meets this project's own bar for live instructions (tested with one reader family; easy question sets). Terse plain English was 35.1% smaller at 39/39, so it saved more that round. Details: round29/SCORES.md.

## Round 28, fully blind (2026-11-20)

- **Test set:** 4 passages by an independent no-context author written after the rules were frozen: English, Simplified Chinese, German, Polish (3 are instructions for an AI assistant). 39 sealed questions, 25 of them safety questions.
- **Readers:** fresh no-context frontier-model helpers (one model family), no key.
- **Result:** the frozen main form (MNC26) was 34.8% smaller on o200k (42.6% on cl100k) and answered 39/39 in both runs. Its two blind decodes back to prose had no safety errors. Terse plain English was 34.5% smaller, also 39/39, so this round is a tie. The original text answered 39/39. An aggressive test form (MNC26x) was 39.9% smaller and got 38/39 and 39/39. Its one miss named an approver the text doesn't name, so it isn't safe yet. LLMLingua-2 was 34.2% / 47.9% smaller at 79.5% / 69.2%.
- **Readiness:** MNC26 has passed 2 consecutive fully blind rounds with no instruction-safety errors. 3 are required before it counts as ready for live instructions.
- **Limits:** one reader family, 2 runs, 39 questions (easy for every faithful text); a small local 7B model reads MNC worse than the original text. Full numbers: round28/SCORES.md and LEADERBOARD.md.

## Round 25, fully blind (2026-11-19)
- **Test set:** 4 passages written by an independent no-context author after the encoding rules were frozen: English, Simplified Chinese, Spanish, Polish (3 are instructions for an AI assistant). 39 sealed questions, 23 of them safety questions.
- **Readers:** fresh no-context frontier-model helpers (one model family), no key.
- **Result:** the aggressive form (MNC24x) was 35.9% smaller on o200k (44.0% on cl100k) and answered 39/39 in both runs (after correcting a scorer bug with Chinese currency units; the raw regex score was 37/39). Terse plain English was 34.1% smaller and answered 37/39 in both runs (it misread which course a registration deadline applied to). LLMLingua-2 was 34.8% / 50.0% smaller at 74.4% / 66.7%. The original text answered 39/39.
- **Frozen benchmark (not blind):** MNC24 matched the original text and the earlier MNC16x version (about 97% on 134 questions, all 56 safety questions right) at 44.6% savings; it did not beat MNC16x.
- **What failed:** one of two blind decodes back to prose described the assistant as "working for" the business instead of being its inbox assistant (3 sections). Strict instruction-safety therefore FAILED again; MNC is not yet ready for live instructions (0 of the 3 consecutive clean blind rounds required).
- **Limits:** one reader family, 2 runs, 39 questions. Full numbers: round25/SCORES.md and LEADERBOARD.md.

## Round 24, fully blind (2026-11-19)
- **Test set:** 4 passages written by an independent no-context author after the encoding rules were frozen: English, Korean, Brazilian Portuguese, Dutch (3 are instructions for an AI assistant). 40 sealed questions, 25 of them safety questions (permissions, prohibitions, approvals, roles, deadlines, emergencies).
- **Readers:** fresh no-context frontier-model helpers (one model family), no key.
- **Result:** the most aggressive form (MNC23xx) was 39.6% smaller on o200k (51.2% on cl100k) and answered 40/40 in both runs. Terse plain English was 35.9% smaller and answered 39/40 in both runs (it flipped one permission). LLMLingua-2 at 0.5 was 47.0% smaller and answered 37/40. The original text answered 40/40.
- **What failed:** a blind decode of the main form back to prose made 2 safety distortions (an instruction to the customer read as one to the assistant; an after-hours contact rule widened). Strict instruction-safety therefore FAILED this round. MNC is not yet ready for live instructions (0 of the 3 consecutive clean blind rounds required).
- **Limits:** one reader family, 2 runs, 40 questions; not yet re-run on the frozen benchmark. Full numbers: round24/SCORES.md and LEADERBOARD.md.

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

## Later rounds (round9/, round10/)
Rounds 9 and 10 were tested only with a local 7B reader (Qwen2.5-7B) and scored by the builder. Neither beat round 3 or the original text on fresh passages, and both failed the instruction-safety check (mostly a dropped actor when a question asks for a name and an identity together). Round 10 also saved fewer tokens than terse English. Full numbers and the failures are in each folder's SCORES.md and NOTES.md and in LEADERBOARD.md.

## Round 11 (round11/): first test with a strong reader
Round 11 adds a stronger reader: a fresh AI helper with no other context, given only the text and the questions. On five fresh passages (English, Spanish, Japanese, Italian, Dutch; 94 questions, 40 of them instruction-safety checks), two compact no-key versions, MNC15x and MNC15xx, answered 97.9% correctly. They kept every instruction-safety point while using 38.9-43.8% fewer tokens (o200k). The original text scored 100%. The baselines scored 73-83%: terse English 73.4% while saving 47.8%, LLMLingua-2 83.0% while saving 34.6%. Limits: each method was read only once, so run-to-run noise is unmeasured. The two compact versions were written after the round's results were known, so the reader was blind but the encoder was not. The frozen benchmark has not been run on them yet. These results are promising but not a confirmed new best. On the local 7B reader, the same round still had two threshold errors.

## Round 12 (round12/): frozen benchmark with a strong reader
Round 12 runs the frozen 15-passage benchmark with the strong reader for the first time. Each version was read twice by fresh AI helpers with no other context. The compact no-key version MNC16x answered 220 of 221 benchmark questions on both runs, and every instruction-safety question correctly, while using 43.5% fewer tokens (o200k). The original text scored 221/221. LLMLingua-2 at 0.5 saved 50.3% and scored 89.1%. On five fresh passages (English, Chinese, French, Portuguese, Polish; 106 questions), MNC16xx scored 100% on both runs while using 45.4% fewer tokens. A terse English rewrite by a strong model also scored 100%, but it saved only 35.4%. Limits: one reader family, two runs, and the passages and encodings come from the same agent. A blind decode turned one deadline ("by 15:00") into "at 15:00", so the ready-for-instructions bar (3 clean blind rounds) is still 0 of 3. The benchmark is now too easy for this reader, and a harder one is planned.

## Round 13 (round13/): savings curve on fresh passages
Round 13 applies the fixes from round 12 (deadline words kept, speaker names, a neutral section tag, and a fact list written before encoding). It tests three compression levels on five fresh passages (English, Japanese, Spanish, Italian, Dutch; 114 questions, 68 of them instruction-safety checks). With the strong reader, MNC17 (39.1% fewer tokens, o200k), MNC17x (45.3%) and MNC17xx (46.9%, read twice) all scored 100%, as did the original text and a terse English rewrite (34.9%). LLMLingua-2 at 0.5 scored 71.9%; it deleted the Japanese passage entirely, and on the other four passages it scored 87.2% while saving 51.3%. These questions are too easy for this reader to separate the versions, so a harder benchmark is the next step. The blind decode found two encoder mistakes: "tell them to call 911" came back as "they should call 911", and "an overview of the day's returns" lost the word "overview". So the ready-for-instructions bar is still 0 of 3. The frozen benchmark and the local 7B were not run this round. This is not a new best.

## Rounds 14-15 (bench-v2/, round14/, round15/): a harder frozen benchmark
bench-v2 is a new frozen benchmark: six dense passages (English, German, French, Japanese, Spanish, Chinese) with 89 questions, 61 of them instruction-safety checks and 40 needing two rules at once. The encodings were frozen before the questions were written. Fresh AI helpers with no other context read each version (MNC versions and the original twice, baselines once). MNC18 (32.7% fewer tokens, o200k) and the more compact MNC18z (38.7%) scored 100% on every run, the same as the original text. The baselines dropped: terse English 95.5% (29.6% fewer tokens), LLMLingua-2 at 0.66 79.8% (35.7%), and LLMLingua-2 at 0.5 61.8% (57.0%, partly because it deletes most of the Japanese passage). Round 15 (English, Portuguese, Korean, Polish; 42 questions): MNC18 scored 97.6% and 100% on its two runs, and the original scored 100% on one run. The miss was a safety error: "cancellation <24h before: fee" was misapplied to a 20-hour cancellation. A blind decode of bench-v2 also lost one actor: "the customer must submit invoice details within 30 days" became "you provide them within 30 days". So the ready-for-instructions bar is still 0 of 3. The builder judged the decodes, so that check is not independent. This is not a new best: the older frozen benchmark hasn't been run on MNC18 yet.
