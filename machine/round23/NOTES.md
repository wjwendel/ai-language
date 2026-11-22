# Round 23 notes (2026-11-18 ~19:15 CT)

## What worked
- Strong-reader direct use 100% ×4 (MNC22, MNC22x) on a fully blind, independent-author round in en/ja/it/sv, including 18 two-hop questions; R7 call numbers, R8 refund amount and R9 identity lines all answered correctly.
- R10 had no test case this round (no indefinite actor in the originals); no actor distortions.
- LLMLingua-2 is now clearly unsafe on mixed-language text: it collapsed the Japanese section and flipped two "never contact" rules at both settings.

## Holes found
1. Threshold scope lost in the over-limit clause: `may confirm custom-cake orders yourself up to €80; above €80: needs Chiara's approval` → decode B "any order above €80". Fix R12: repeat the object in the over-limit clause (`custom-cake orders above €80: need Chiara's approval`); ~2 tokens.
2. R8 added a derived figure (337.50 kr) the original never states; the judge flags it as added content. Fix R8b: when the original gives only a rule ("75% of the course fee") and a base exists elsewhere, keep the rule as written and do not compute the amount unless the original states it.
3. Savings: terse English 39.2% vs MNC22x 36.3% o200k at equal 100%. R11 cuts were too small. Remaining slack: street addresses written in full, `customer` repeated in every line, `yourself` on every may: line (could be one section-level convention), `never:` lists that repeat `contact or copy`, §2 English glosses where a shorter native-script phrase would do.

## Next-round fix list (baselines first)
1. **Savings — a baseline wins:** terse English 39.2% vs MNC22x 36.3% at equal 100% strong-reader accuracy. Target ≥40% at 100% S with MNC23 = MNC22x + R12 + R8b + a section-level convention line instead of repeated `yourself`/`customer` (test it on the strong reader first).
2. Decode the main form ×2 + judge again; the strict decode bar is the binding constraint (3 rounds failed on one low-severity decode slip each).
3. Round 24 fully blind, independent author (copy round23_sealed/AUTHOR-R23.md; rotate languages, e.g. en / ko / pt / nl; add "include one threshold that applies only to one order type" to stress R12).
4. Bench-v1: run MNC22/MNC23 against the original control (97.0%).
5. 7B secondary: score round23/answers_7b when the queue finishes (ANS=answers_7b).
