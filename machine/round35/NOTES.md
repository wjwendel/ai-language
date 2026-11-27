# Round 35 notes (2026-11-27)
## Holes found
- Savings: terse English beats MNC28 main again (37.7% vs 20.1% o200k). MNC28x beat terse narrowly (40.1% vs 37.7% o200k; 57.9% vs 56.6% cl100k) at 100% ×2 — the first x win over terse at equal strong-reader accuracy since r30 — but x is not promotable yet.
- MNC28x decode slips (both from terse cuts): (1) "NO el shaper" (Andrés is not THE shop's shaper) decoded as "not a shaper" — dropping the article widened a role negation (S); (2) "express = same-day" without the noun decoded as same-day sharpening instead of same-day delivery (F). The r34 approver-merge revert worked: no approver-link errors this round.
- LLMLingua-2 (0.66 and 0.5) lost most of the Japanese §2 facts and named an unstated approver (Salma Haddad) on §4.q4.
- Author gap: two "who must approve" questions (§1.q3, §4.q4) with gold "needs approval, approver not stated" — the scorer counted a bare "not stated" as an abstain, so 6 of 8 faithful runs lost 2 points each. Fixed for all texts alike via overrides.
- Questions still at ceiling for faithful texts (original, main, x, terse, summarize all 100% after the fix) even at ~470-530-word instruction sections.
- 7B: all 9 runs complete this time (no truncation). MNC28 65.0% ×3, original 62.5% ×3, MNC28x 62.5-65.0% — near-identical runs, 1-question margins; every 7B run named an approver for the two unnamed-approver questions.
## Next-round fix list (baselines first)
1. **Savings — terse beats main (37.7% / 56.6%); x beats terse narrowly (+2.4 / +1.3 points).** Keep MNC28 frozen as the ready reference. Fix x's two decode slips: keep definite-article role negations exact ("NOT the shaper" → "NOT shaper-role", never "NOT a shaper"); keep the noun a definition applies to ("express = same-day delivery"). Then run x decode ×2 + bench-v1 on x before any promotion (promotion would restart the ready counter).
2. LLMLingua-2 fails on Japanese (lost most §2 facts at both ratios) — keep it as a baseline, note the language gap.
3. Harder separation: questions at ceiling again for faithful texts — next round try one short-context call answering all four sections at once, or ≥600-word instruction sections.
4. Round 36 fully blind, independent author (copy round35_sealed/AUTHOR-R35.md; rotate e.g. en / ko / pt / hi); author rule: "who approves" questions whose gold is "not stated" must accept a bare "not stated".
5. 7B: scores barely vary across the 3 runs (server-default sampling; answers differ but totals match), so treat 1-question gaps as ties or add runs; the 7B invents approvers where the text names none, a useful weak-reader safety probe.
