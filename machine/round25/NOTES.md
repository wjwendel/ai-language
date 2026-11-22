# Round 25 notes (2026-11-19 ~07:05 CT)

## What worked
- R14 (customer-told instructions in one object with an actor word): all three two-part emergency steps stayed the customer's action in every direct-use run and both decodes. The round-24 hole is closed.
- R15 (qualifier after its noun): the "badminton students + swimming students registered before Mar 10" scope held in all MNC runs and both decodes; terse English got it wrong in both runs (a real accuracy gap vs the best baseline).
- MNC24x beat every baseline on the fresh set with the strong reader.

## Holes found
1. Bare `§N you` header: decoder A wrote "You are working for X" instead of "You are the inbox assistant of X" (3 judge-flagged S items). Fix R18: header carries the role in one token-cheap word: `§1 you=assistant` (or put `assistant` after the business name), never a bare `you`.
2. Descriptor loss: "a small flower shop" dropped because the name implies the type. R16 extension: keep size/type adjectives that the name does not state (`small`).
3. Savings: 35.9% on this set vs LLMLingua-2 0.5 at 50.0% (at 66.7% accuracy). The ≥45% target was not reached on fresh text; on bench MNC24 reached 44.6% but MNC16x is equal.
4. Bench: the helper-encoded versions/mnc24.txt was spot-checked on r3P1 (48h reminder actor = Jordan, correct as in the original).
5. Scorer: `\b` after a number fails when a CJK unit follows (462元). Fix the scorer (use `(?<!\d)462(?!\d)` style lookarounds) instead of overriding each time.

## Next-round fix list (baselines first)
1. **Savings — LLMLingua-2 0.5 still saves more (50.0% vs MNC24x 35.9% o200k)**, but at 66.7% accuracy; terse English is now beaten on accuracy at slightly lower savings (34.1%). Target an MNC25x at ≥40% on fresh text with 100% strong-reader accuracy: shorter section headers, drop `of`/articles inside approval lines, collapse `need approval of X, role` to `X (role) approves` only if a probe shows no actor drift.
2. MNC25 = MNC24 + R18 (role in header) + R16 extension (keep size/type adjectives) ; decode ×2 + judge.
3. Round 26 fully blind, independent author (copy round25_sealed/AUTHOR-R25.md; rotate languages e.g. en / ja / fr / tr; keep the two-part customer step and the one-noun qualifier).
4. Bench: MNC24 ties MNC16x; a harder bench-v2 strong-reader set is needed to separate versions (bench-v1 is at ceiling for the strong reader).
5. Scorer fix for CJK units (hole 5); score round25/answers_7b when the queue finishes.
