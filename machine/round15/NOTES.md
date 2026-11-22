# Round 15 NOTES

Prepared in the 2026-11-17 sprint with the frozen MNC18 candidate; same author for passages, facts, encoding and questions (not independent). Scored 2026-11-17 evening.

## Holes
1. **Symbol thresholds still flip on a strong reader** (1 of 2 runs): `cancellation <24h before: R$50 fee` → 20 h was judged "no fee". Bare `<N` before a time-before phrase is ambiguous to read ("less than 24h" vs "more than 24h ahead"). The original Portuguese wording ("menos de 24 horas de antecedência") was answered right.
2. Decodes clean: R1-R3 (deadline words, `tell X:`, object nouns) held on all 34 facts in both decodes. The r12/r13 slip classes did not recur.

## Fix list for MNC19 (fix only failing classes)
1. Thresholds as a decision in words, no bare `<`/`>` on time-before or age/date comparisons: `cancel less than 24h before appointment → fee R$50` (keep `≤`/`>` only on plain amounts, where no flip has been seen with the strong reader).
2. (from round 14) Passive obligations keep their actor: `customer submits invoice info within 30d of order; later → forward 王磊`.
