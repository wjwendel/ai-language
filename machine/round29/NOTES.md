# Round 29 notes (2026-11-20 ~07:30 CT)

## What worked
- Frozen MNC26 main held for the third blind round: S 23/23 ×2, 0 S errors in both decodes → counter MNC26: 3/3 (meets the ready-for-live-instructions bar).
- R22 in x (one order type / permission scope per line) fixed the r28 invented-approver hole: two order types with separate limits (alterations ≤$40 named approver; bespoke ≤$20 approver not named) answered correctly in all runs.
- MNC26x' 100% ×2 at 36.0% o200k (r28 x: 97.4%/100% at 39.9%).

## Holes found
1. Encoder added a year ("2026 Dec 1") the original did not state. Fix R23: never add a year, weekday or unit the original leaves implicit.
2. Savings: terse English 35.1% beats MNC26 main 29.0% (o200k) and ties MNC26x' 36.0%. The main form's "yourself" on may-lines, separate never-lines and spelled-out headers cost ~6 points.
3. Question sets still at ceiling for every faithful text; the only separator is savings. Need bench-v2 (longer/harder passages, more distractor rules).
4. Harness: parallel reader results must be mapped to text names inside the same promise (fixed mid-round; first batch discarded).

## Next-round fix list (baselines first)
1. **Savings — terse English beats MNC26 main (35.1% vs 29.0%) and ties x (36.0%)**. Counter is complete, so the next step is to decide promotion: promote MNC26x' (R21 + R22 + aggressive + R23) to main as MNC27 — promotion restarts the counter at 0 (MNC27 starts at 1 if round 30 passes). Target ≥40% o200k at S 100% ×2.
2. Round 30 fully blind, independent author (copy round29_sealed/AUTHOR-R29.md; rotate languages e.g. en / ko / pt / nl), harder: ≥250 words per section, more distractor rules.
3. Score round29/answers_7b (mnc26, mnc26x, original ×3).
4. Bench-v2 strong-reader set before any formal new-best claim; run bench-v1 once on MNC27.
