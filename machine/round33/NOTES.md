# Round 33 notes (2026-11-22)
## Holes found
- Savings: terse English wins again (42.4% vs MNC28 main 22.3% o200k). MNC28x (all-English slots, telegraphic) reached 41.6% — a tie with terse for the third round running, not a win.
- Main keeps the Korean §2 in compact Korean (497 tokens vs x's 295 in English slots): the biggest single gap between main and x/terse.
- Questions at ceiling again for every faithful text (original, MNC28, MNC28x, terse, summarize all 100%), even with longer instruction sections and three-rule chains. Only LLMLingua separates.
- Author regex for "approver not stated" lacked "does not state" (shared fix applied).
- Decoder B widened a §2 scope ("not together with" → "not during"); payload was faithful — decoder noise, but scope words like 함께/together are fragile.
## Next-round fix list (baselines first)
1. **Savings — terse English wins (42.4% / 55.6%).** MNC28 is now ready (3/3): keep it frozen as the ready reference. In x: drop repeated company names on identity lines, shared conventions instead of repeated words (e.g. one approver line per person listing what they approve), merge inbox/report lines; target ≥48% o200k at 100% S. Run blind decode on x too, since x would be the promotion candidate (promotion restarts the counter).
2. Round 34 fully blind, independent author (copy round33_sealed/AUTHOR-R33.md; rotate e.g. en / zh / de / id); add "does not state" to the approver-not-stated regex instruction.
3. Harder separation: a reader-budget or long-passage stress test (e.g. ≥600-word instruction sections, or all four sections answered in one short-context call), since short passages saturate.
4. Bench-v1 on MNC28 and MNC28x with a strong reader before any formal new-best claim; bench-v2.

