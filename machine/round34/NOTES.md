# Round 34 notes (2026-11-22)
## Holes found
- Savings: terse English wins again (36.3% vs MNC28 main 16.8% o200k). Main saves least when the English instruction section is already terse (§1 577→536 tokens) and the zh §2 stays in Chinese.
- MNC28x: merging all of one person's approvals onto one line broke two links (Saturday over-limit → Desmond; hotel order >30 pieces → Ratna approves the order, not just discounts). Approver merges are unsafe; keep the approver on the same line as the limit it closes.
- x encoder could not reach 48% without dropping protected facts on this denser text; terse English still reaches 36% — so the gap is wording, not facts.
- Author errors: a two-part question with a one-word gold (§2.q4) and a reject regex that fires on "not ask the customer to call". Fixed in the scorer for all texts alike.
- Questions still at ceiling for faithful texts (original, main, terse, summarize all 100%) even at ~420-word instruction sections.
- 7B truncated 2 of 3 x runs after 10 answers.
## Next-round fix list (baselines first)
1. **Savings — terse English wins (36.3% / 44.4%).** Keep MNC28 frozen as the ready reference. In x: revert the per-person approver merge (r34 failure); keep each over-limit approver on its limit line (e.g. "estimates: may ≤£180; Sat ≤£120; above: Desmond"); instead cut wording terse-style (drop articles/auxiliaries, "may" lines without "approve"). Target: beat terse on o200k at 100% S, with blind decode on x.
2. Round 35 fully blind, independent author (copy round34_sealed/AUTHOR-R34.md; rotate e.g. en / ja / es / ar); author rules: no two-part yes/no questions with a one-word gold; reject regexes must not fire on "do not ask the customer to call".
3. Harder separation: one short-context call answering all four sections, or ≥600-word instruction sections.
4. Bench-v1 on MNC28 and the next x with a strong reader before any formal new-best claim; bench-v2.
5. 7B: raise max_tokens or re-run truncated outputs.
