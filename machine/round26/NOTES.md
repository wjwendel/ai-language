# Round 26 notes (2026-11-19 ~13:10 CT)

## What worked
- R18: `§N you=<role>` header removed the round-25 role-wording decode errors (both decodes 119/119).
- R16b: descriptors kept.
- R15 qualifier-after-noun held again on a Japanese one-noun scope (magazines Dec 15+, kamishibai any date).
- Scorer CJK fix (digit lookarounds) removed the 元-type false negatives.

## Holes found
1. Unnamed approver: original "anything above $350 needs approval" names no one. MNC25x put the owner line right above `>$350: need approval`, and one reader filled the gap with the owner (invented actor). Fix R20: when the original names no approver, write `need approval, approver not named` (+3 tokens; no parentheses for safety content). Never let an unnamed approval sit next to a named person's line without that marker.
2. Savings: terse English 34.6% vs MNC25 31.6% at equal accuracy. MNC25x 37.0% only wins with the safety slip. The gain must come from §1/§4-style instruction text where MNC is longest relative to terse (§1: MNC25 280 vs terse 257 tokens).
3. Question gold over-inferred an approver (§1.q2). Author brief should say: gold must not name anything the original doesn't state.

## Next-round fix list (baselines first)
1. **Savings — terse English wins at equal accuracy (34.6% vs MNC25 31.6%)**: MNC26 main = MNC25x form (37.0%) + R20 (unnamed approver marker). Goal: MNC26 main ≥36% with S 100% ×2 and clean decodes.
2. Round 27 fully blind, independent author (copy round26_sealed/AUTHOR-R26.md; rotate languages e.g. en / ko / it / sv; add "gold answers must not name or assume anything the text doesn't state").
3. Score round26/answers_7b (queue started 13:04 CT) and append to round26/SCORES.md.
4. Bench: build a harder bench-v2 strong-reader set before any new-best claim (bench-v1 is at ceiling).
5. Ready counter is 1/3 for the main form; keep the main form's safety rules frozen except R20.
