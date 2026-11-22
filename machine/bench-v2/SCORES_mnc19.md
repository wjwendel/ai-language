# bench-v2 — MNC19 / MNC19x (strong reader, run 2026-11-17 ~19:05-19:13 CT; scored 19:25 CT)
Encodings are NOT question-blind: they were written after the bench-v2 questions and the round-14 results were known. That's normal for re-using a frozen benchmark, but they are not fresh-round evidence.

| Method | Saved o200k / cl100k | Run 1 | Run 2 | Safety S | Two-hop |
|---|---|---|---|---|---|
| original | 0 / 0 | 100% | 100% | 61/61 ×2 | 40/40 ×2 |
| MNC18 | 32.7% / 41.8% | 100% | 100% | 61/61 ×2 | 40/40 ×2 |
| MNC18z | 38.7% / 46.9% | 100% | 100% | 61/61 ×2 | 40/40 ×2 |
| **MNC19** (candidate) | 38.0% / 46.3% | **100%** | **100%** | 61/61 ×2 | 40/40 ×2 |
| **MNC19x** (curve) | **39.0% / 47.2%** | **100%** | **100%** | 61/61 ×2 | 40/40 ×2 |
| terse English | 29.6% / 41.0% | 95.5% | 95.5% | 60/61 ×2 | 39/40 ×2 |
| LLMLingua-2 0.66 | 35.7% / 35.2% | 79.8% | – | 46/61 | 33/40 |
| LLMLingua-2 0.5 | 57.0% / 57.8%* | 61.8% | – | 34/61 | 26/40 |
*includes the Japanese/Chinese text it deleted (49.3% excl. §4/§6).
No overrides were needed for MNC19/MNC19x (0 misses).

Blind decode ×2 (MNC19): 0 safety distortions in both (decodes/judgments_mnc19.json; judge = encoder, not blind). The MNC18 actor loss (P6.6 invoice: customer submits → "you provide") is fixed in both decodes.

**Ceiling again:** the original and every MNC version score 100% ×2 on bench-v2, so it now separates MNC from the baselines but not MNC versions from each other. The curve is flat at 100% from 0% to 39.0% o200k for MNC, while the baselines fall off.
