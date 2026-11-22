# Round 28 notes (2026-11-20 ~01:10 CT)

## What worked
- Frozen MNC26 main held: S 25/25 ×2 direct use and 0 S errors in both blind decodes → counter MNC26: 2/3.
- MNC26x aggressive probe reached 39.9% o200k (vs terse English 34.5%) with 1 miss in 78 answers — the savings target (≥40%) is almost reached.
- R20-style faithfulness: main kept "chemicals ≤250€: may confirm" on its own line and named no approver above it; both main readers answered correctly.

## Holes found
1. **x merged two order-type rules on one line** ("care-chemical reorders: may confirm ≤250€; spare parts …: always need approval of Lukas") → reader carried Lukas's approval over to chemicals >250€ (invented approver). Fix R22 (x): one order type / permission scope per line; never put an approval rule on the same line as a different type's limit; when the original states only a limit and no approver for the over-limit case, write nothing extra (no inferred approver). Test in x only.
2. Discrete check times still decoded as ranges (3 F distortions ×2) in main; R21 lives in x and cannot enter main until the counter run finishes or main is promoted.
3. Question set was at ceiling for all faithful texts (original/terse/summarize/MNC26 = 100%); savings is the only separator. Need harder, longer passages (bench-v2) to show differences.

## Next-round fix list (baselines first)
1. **Savings — MNC26 main only ties terse English (34.8% vs 34.5%)**; MNC26x wins (39.9%) but failed once on safety. MNC26x' = x + R22 (never merge two order types / permission scopes on one line) + keep the r28 aggressive edits; target ≥40% at S 100% ×2.
2. Round 29 fully blind, independent author (copy round28_sealed/AUTHOR-R28.md; rotate languages e.g. en / ja / es / tr). Keep MNC26 main frozen (sha1 6c1bc095) so r29 can complete MNC26: 3/3.
3. (done) round28/answers_7b scored: tie with original inside noise.
4. Bench-v2 strong-reader set (longer, harder passages) before any formal new-best claim.
5. After the counter completes (or fails), decide whether to promote x (R21 + R22 + aggressive) to main; promotion restarts the counter at 0.
