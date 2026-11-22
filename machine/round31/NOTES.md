# Round 31 notes (2026-11-21 ~02:00 CT)

## What worked
- MNC28 (MNC27 + R24) decoded perfectly twice (205/205 facts, 0 S errors) and answered 39/39 ×2: the R24 fix closed the r30 modality / noun-pair slips. Ready counter MNC28: 1/3.
- MNC28x aggressive probe also 39/39 ×2 at 38.5% o200k — no safety slip this time.
- "only X may / Y may only reduce" rules and the unnamed-approver lines held in every faithful text; LLMLingua-2 0.5 invented an approver (Daniel) — the classic failure MNC avoids.

## Holes found
1. Savings: main form 28.1% vs terse English 37.6% (o200k). The main form keeps the everyday CJK section in Chinese line by line (391→373 tokens); terse translated it to English (~297). Translation of CJK into compact English is a real token lever on o200k.
2. §1 English instruction section saved only 19% (404→329) in main: verbose role labels ("operations manager", "need approval of") and full "may approve" phrasing.
3. Questions at ceiling for all faithful texts for the 4th round running; savings is the only separator. Bench-v2 still needed.
4. 7B not run (RAM).

## Next-round fix list (baselines first)
1. **Savings — terse English wins (37.6% / 44.5% vs MNC28 28.1% / 30.8%).** Keep MNC28 frozen for the counter (2 more blind passes needed). In the x form test: (a) CJK/other everyday sections rendered as compact English slots (language-neutral reader-side: allowed since the reader answers in any language) vs kept in source language; (b) MNC28x style headers. Target x ≥45% o200k at 100% strong-reader S.
2. Round 32 fully blind, independent author (copy round31_sealed/AUTHOR-R31.md; rotate e.g. en / ja / es / tr; keep distractors; add a harder question type so faithful texts stop hitting ceiling: e.g. three-rule chains, near-miss numbers).
3. Run the 7B (3 runs) for r31 when ≥6 GB is free.
4. Bench-v1 on MNC28 (strong reader) before any formal new-best claim; build bench-v2.
