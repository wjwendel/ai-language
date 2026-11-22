# Round 24 notes (2026-11-19 ~01:15 CT)

## What worked
- MNC23xx (most aggressive form so far on a blind round) held 100% ×2 with the strong reader at 39.6% o200k / 51.2% cl100k — above terse English on savings (35.9%) and accuracy (terse flipped the key-duplication permission in both runs, because it wrote "key duplication confirm any price" without a may/permission word; this supports the may: line rule).
- R12 (object repeated in over-limit clause) and "limit only for X" lines: no scope errors in direct use or decode.
- R8b: no encoder-computed amount this round.

## Holes found
1. Actor drift after `;` inside a "tell customer:" slot: `tell customer: X; also call 911 if …` decoded as an order to the assistant. Fix R14: everything the customer is told goes in one quoted/joined object: `tell customer: X + they should also call 911 if anyone in danger` (keep the actor word "they"/"customer" on any second instruction).
2. Compound condition slots: `other hours or night emergency leaks: 경비실` was parsed as two separate conditions. Fix R15: when a qualifier applies to only one noun, put the noun first and the qualifier after it: `emergency leaks outside office hours or at night: 경비실` (never let "or" join a time-only clause and a noun clause).
3. Encoder narrowed "banho e tosa" (pet grooming) to "dog grooming": R11/R13 descriptor cuts must not translate a business type more narrowly; keep the native phrase or the original's breadth.
4. Dropping the closing courtesy sentence counts as an F loss for the decode judge. Decision: keep dropping it for direct use (it carries no fact) but tell the judge courtesy closings are out of scope, stated before the run.

## Next-round fix list (baselines first)
1. **Savings — LLMLingua-2 0.5 still saves more (47.0% vs MNC23xx 39.6% o200k)**, at 92.5% accuracy. Target: an MNC24xx at ≥45% with 100% strong-reader accuracy (try dropping email domains' repeated `.example`? NO — facts; instead: drop section business line to name only, merge report/deadline lines, use digits-only times `9-17h` everywhere, drop `only` where `wkdays … ; Sat 9:00` already excludes).
2. Make MNC23xx the main form for round 25 (+R14 +R15), decode it ×2 + judge (strict decode is still the binding constraint: 4 rounds failed on encoder ambiguities).
3. Round 25 fully blind, independent author (copy round24_sealed/AUTHOR-R24.md; rotate languages e.g. en / zh / es / pl; require one "tell the customer two things" emergency step and one qualifier that applies to only one of two nouns).
4. Bench-v1: encode MNC23xx and run against the original control (97.0%) — needed before any formal new best.
5. 7B secondary: score round24/answers_7b (ANS=answers_7b) when the queue finishes.
