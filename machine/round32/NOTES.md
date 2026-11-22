# Round 32 notes (2026-11-21)
## Holes found
- Savings: terse English again wins (39.0% vs MNC28 24.7%, MNC28x 36.8% o200k). MNC28's English instruction sections keep long phrasing ("may approve", "must be approved by", "then tell customer") — that is where terse gains.
- MNC28x's English rendering of the Japanese everyday section cut §2 from 419 to 306 tokens and held 100% — compact English slots for non-English everyday sections work with a strong reader.
- Questions still at ceiling for every faithful text despite three-rule chains and near-miss numbers; only LLMLingua fails. Harder probes are needed to separate faithful forms.
- Original text strict-scored 38/40 because two regexes demanded detail not asked for (overrides recorded).
## Next-round fix list (baselines first)
1. **Savings — terse English wins (39.0% / 49.3%).** Keep MNC28 frozen (one more blind pass reaches 3/3). In the x form: telegraphic verbs in instruction lines ("ok ≤N" style approved only if safety holds), drop company descriptors, English slots for all non-English sections; target ≥45% o200k at 100% S.
2. Round 33 fully blind, independent author (copy round32_sealed/AUTHOR-R32.md; rotate e.g. en / ko / fr / vi); make regexes accept a bare correct yes/no when the question asks only yes/no.
3. Harder separation: add a long-passage stress test (≥600 words per instruction section) or a reader-budget test, since short passages saturate.
4. Bench-v1 on MNC28 (strong reader) before any formal new-best claim; bench-v2.
