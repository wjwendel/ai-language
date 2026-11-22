# Round 30 notes (2026-11-20 ~13:45 CT)

## What worked
- MNC27 (promoted x form) 100% ×2 at 36.6% o200k / 49.7% cl100k on a harder fully blind set with distractor rules; beat terse English (28.7%), summarize (30.6%) and LLMLingua-2 0.66 (34.3%, 97.4%) at equal or better accuracy.
- Exception-bearing prohibitions on their own line ("never X, except Y") held: power-line and vaccination-card exception questions correct in all runs.
- R22 (one order type per line) held again for the two-type limits (stump grinding vs firewood with unnamed approver; business vs private orders).

## Holes found
1. Encoder dropped modality in an everyday section: "must collect new card" → bare list line; decoders read it as "will be issued". Fix R24: keep must/required/only words in every section, not just instruction sections.
2. Encoder narrowed a noun pair ("complaints or inquiries" → "questions"). Fix R24b: never merge or drop one of two listed nouns.
3. LLMLingua-2 0.5 is the only text saving more than MNC27 and it failed a safety boundary (exactly 48h).
4. Question sets still at ceiling for faithful texts; savings remains the only separator. Bench-v2 needed.

## Next-round fix list (baselines first)
1. **Savings — LLMLingua-2 0.5 saves more (49.3% vs 36.6%) but fails safety; terse beat the MNC main in r29.** MNC27 is at 0/3 after the decode-gate fail, so promote MNC28 = MNC27 + R24 to main now (costs no counter progress) and freeze it; push an MNC28x probe toward ≥42% o200k.
2. Round 31 fully blind, independent author (copy round30_sealed/AUTHOR-R30.md; rotate e.g. en / zh / it / pl; keep distractor rules; add modality words in the everyday section with a question on them).
3. Weak reader: MNC27 50-58% vs original 60-63% (7B, 3 runs) — the aggressive form hurts the small model; keep MNC26-level explicitness as the weak-reader option.
4. Run bench-v1 once on MNC27 (strong reader) before any formal new-best claim; build bench-v2.
