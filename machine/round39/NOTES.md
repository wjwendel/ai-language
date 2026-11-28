# Round 39 notes (2026-11-28)
## What happened
- MNC28 main (frozen): clean blind pass (58/58 ×2, decode 195/196 ×2, the only loss an F word). Counter MNC28 1/3.
- MNC28x "terse first, then rails": savings jumped from 24.2% to 40.0% o200k (terse 41.5%), and direct use stayed at 100%/98.3% (the one miss was an Arabic-script name). But the decode lost a person's job title in the Korean everyday section (both decodes), and one decode widened a place and narrowed a noun. The rails covered instruction sections; the everyday section had no rail for titles.
- The r38 one-item-qualifier hole did not recur this round (the author's three-item list was handled by both forms).
## Next-round fix list
1. **x rails for everyday sections:** keep every person's title/role next to their name in every section (not only instruction sections); keep place scope nouns exactly ("in the complex", not "in each building"); keep each listed item's own noun. Target: x ≥ terse savings with a clean decode.
2. **x script rule:** give a Latin transliteration once after any non-Latin name in an instruction section (costs a few tokens; avoids answers that a Latin-only check can't match), or ask the author for regexes that accept both scripts.
3. Main: keep MNC28 frozen (counter 1/3). MNC29 (one-item qualifier rule) only if the hole recurs.
4. Round 40 fully blind (rotate e.g. en / zh / es / hi), 55-60 q, keep the "the vs a" and one-item list tests.
5. Score r39 7B (answers_7b/keep) when the queue finishes; bench-v1 on main and x still pending.

