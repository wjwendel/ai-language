# bench-v2 (frozen 2026-11-17)

Harder frozen benchmark built because the strong reader hit 100% on bench-v1 and on round 12-13 fresh questions.

- 6 passages, 2,217 o200k / 2,712 cl100k tokens (about 1.9x round 13): §1 en dental-office orders/billing (instruction), §2 de property management (instruction), §3 fr cycling-plan news, §4 ja cram-school parent desk (instruction), §5 es owners'-meeting minutes, §6 zh tea-shop after-sales (instruction).
- Density: tiered approval thresholds with "even if" overrides, a temporary delegation (leave until Dec 4), emergency exceptions to cost limits, nested permissions (may X only if A and B; otherwise Y), exact boundaries (exactly $400, €250, 7th day incl., exactly 3 days, 12:00 sharp, 1 March, 12-year-old), quoted strings in 4 scripts, money/percent arithmetic.
- 65 facts (44 safety) in facts.json, written BEFORE encoding, each with `must` regexes for the R4 lint.
- 89 English questions (61 safety, 40 two-hop: combine two rules or compute), written AFTER the MNC18/MNC18z encodings were frozen (encoded_before_questions.sha1 18:30 CT; questions.sha1 later). Gold answers self-checked against the accept/reject regexes (0 failures).
- Same agent wrote passages, facts, encodings and questions (not independent). Readers must be fresh no-context helpers (see ../SPRINT-DISPATCH.md).
- Scoring: tools2/score.py (regex + reviewed overrides with reasons).
- Versions frozen for the first scoring: original, MNC18 (candidate), MNC18z (aggressive, curve only), LLMLingua-2 0.66 and 0.5 (CPU, run before questions existed). Terse English: writer prompt staged for a separate helper.
