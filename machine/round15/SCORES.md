# Round 15 SCORES — candidate MNC18, fresh passages en / pt / ko / pl (run 2026-11-17 ~19:02-19:10 CT)

Strong reader = one fresh no-context helper per job (only its prompt file). 42 questions (32 safety S, 10 facts F, 23 two-hop). Payload frozen before questions (encoded_before_questions.sha1, questions.sha1).

## Tokens
| Method | o200k | cl100k | Saved |
|---|---|---|---|
| original | 1290 | 1529 | 0% |
| MNC18 | 852 | 885 | 34.0% / 42.1% |

## Strong-reader direct use
| Method | Run 1 | Run 2 | Safety S |
|---|---|---|---|
| original | 100% (42/42) | – (1 run) | 32/32 |
| MNC18 | 97.6% (41/42) | 100% (42/42) | 31/32, 32/32 |
MNC18 run 1 miss (§2.q4, S): "client cancels 20 hours before because travelling: fee?" → answered "no; the R$50 fee applies only to cancellations less than 24h before" (gold: yes, R$50). Payload line: `cancellation <24h before: R$50 fee, except emergency with own animal`. The reader quoted the rule correctly and misapplied it, a threshold flip on a symbol comparison. Run 2 and the original-text run got it right. Real failure, not overridden.

## Blind decode ×2 (MNC18; judged by encoder, NOT blind)
Both decodes keep all 34 facts with actor, deadline word and object noun (decodes/judgments_mnc18.json). No distortions.

## Verdict
Instruction-safety FAIL (1 threshold flip on 1 of 2 reader runs). Ready counter stays 0/3. The 7B weak reader was not run with the strong-reader jobs (an earlier 7B run is in answers_7b/; not scored here).
