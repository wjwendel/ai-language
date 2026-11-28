# Round 37 notes (2026-11-28)
## Holes found
- Savings: terse English again saved more (35.9% o200k) than MNC28x (29.1%) and MNC28 main (16.9%). The structural §0 shared-schema idea did not close the gap: its ~161-token key barely pays for itself across three sections, and the compact original (zh/fr/vi) shrinks less overall.
- Separation finally appeared with 59 questions: terse lost the Chinese date-scope question ×2 (qualifier attached to both nouns); LLMLingua lost 7-11. MNC28/MNC28x/original/summarize stayed 59/59.
- x decode slip (S): dropped the actor "customer" from a permission trigger ("string chart request"). Rule for x: every permission trigger keeps its actor (who asks / who sends).
- All four decodes rendered a one-noun Chinese qualifier as ambiguous English ("A and B bought after X"). Decoder prompt could ask to keep qualifier scope unambiguous; for x (English slots) the encoder should write scope explicitly ("e-bikes (any date); e-tricycles only if bought after Mar 1").
- r36 7B scored: MNC28 81.6% ×3 vs original 63.2-68.4% (clear, outside spread), x ties original.
## Next-round fix list
1. **x savings:** the §0 key only pays off on longer inputs. Next: drop the §0 key and instead test terse-English-like slots with AIL safety conventions only where they matter (who/should/must/only/scope), i.e. "terse + safety rails"; measure vs terse on the same passages. Keep actors on every permission trigger; write one-noun qualifiers with explicit scope.
2. Keep MNC28 frozen (7/7 blind passes). Promote x only if it beats terse on savings with 100% safety and a clean decode (promotion restarts the counter).
3. Keep the larger question set (55-60) — it separated texts this round.
4. Round 38 fully blind (rotate e.g. en / ja / de / th or ar). Author: keep the deliberate "should" question and the one-noun qualifier scope test in every everyday section.
5. Score r37 7B (answers_7b/keep); bench-v1 on main and x still pending.

