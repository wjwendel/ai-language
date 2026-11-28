# Round 36 notes (2026-11-28)
## Holes found
- Savings: terse English won again (42.1% / 65.6%) over MNC28x (39.6% / 63.1%) and MNC28 main (21.6% / 48.5%), all at 38/38 ×2 with the strong reader. r35's narrow x win did not repeat; x vs terse is now 1 win / several losses — x has not shown a reliable savings edge.
- x's r35 decode slips were fixed (definite role negations, noun-specific definitions) — the THE/NOT THE form cost few tokens and decoded exactly.
- New x slips (both from terse cuts, both F by the judge): "small" dropped ×3; "should start" → bare "start" decoded as "must start" (modality strengthening). Rule for x: keep should/may/must words exactly (R24 already says this for main).
- Questions still at ceiling for every faithful text (original, main, x, terse, summarize all 100%) even with longer sections; only LLMLingua separates (Korean scope flip, lost Korean limit, ambiguous "Mehra").
- Scorer: "2F" abbreviation missed by an author regex (shared fix); bare "not stated" now accepted when gold says not stated (permanent score.py change).
- 7B queue slow: the original (6,276 cl100k) is near the 8,192 context; results pending.
## Next-round fix list
1. **Savings:** terse beats x on 4 of the last 6 rounds. Stop tuning wording against terse; test a structural idea in x instead: (a) shared-schema lines across the three instruction sections (one header defining slot order: inbox | times | reply deadlines | roles | limits | never | emergency | reports), so slot names are not repeated; (b) drop restatements the questions never need but keep every fact (e.g. "limit only RTW" when the next line already scopes it) — check with decode. Keep should/may/must modality words exact.
2. Keep MNC28 frozen (6/6 blind passes). Promotion of x only if it beats terse on savings, 100% safety and clean decode, and promotion restarts the counter.
3. Harder separation: ceiling persists. Next round try one combined call with all four sections + ~60 questions, or a weaker frontier reader setting (short answer budget), so differences can show.
4. Round 37 fully blind (rotate e.g. en / zh / fr / th or vi). Author: accept "2F"-style floor abbreviations; avoid two people sharing a surname unless a question needs it.
5. Score r36 7B results (answers_7b/keep) when the queue finishes; bench-v1 on main and x still pending.
