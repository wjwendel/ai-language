# Round 22 notes (2026-11-18 ~13:05 CT)

## What worked
- R8 (derived amount as object of the verb): `charge 105 zł, which is 30% of standard tuning` → all four MNC21/21x runs answered the fee question correctly; the r21 failure class did not recur.
- R9 (identity as written, `X = title, not other`): the judge found 0 invented naming rules (r21: 3 per decode).
- R7 (number next to "call"): every emergency answer carried the full number on all MNC runs, while both LLMLingua settings truncated numbers.
- Aggressive form (MNC21x) held 100% S ×2 at 37.6% o200k — the first MNC form above 37% with no strong-reader miss on a fully blind round.

## Holes found
1. Indefinite actor lost in a dropped article: `mechanic will phone within 1 hour` → one decoder wrote "the mechanic" (a specific person). Fix R10: keep `a`/`any` when the original's actor is indefinite (`a mechanic phones within 1h`); 1 token.
2. Savings still behind terse English by 2.6 points o200k (37.6 vs 40.2). Remaining slack in MNC21x: business descriptor lines, repeated `email assistant`, `weekly:` labels, `exact` + quoted sentence framing, §2 long Chinese numbers kept in full.
3. The 7B weak reader server was not running at start; a queue was started late (results pending at write-up).

## Next-round fix list (baselines first)
1. **Savings — a baseline wins:** terse English 40.2% vs MNC21x 37.6% at equal 100% strong-reader accuracy. Target ≥41% at 100% S: MNC22 = MNC21x + R10 + cut the descriptor/framing slack above (drop `email assistant` header words a reader can predict, `Fri 17:00: report…` without `weekly`, merge check-times into one slot).
2. Decode the aggressive form too (MNC22x decode ×2 + judge), since it is the main candidate.
3. Round 23 fully blind, independent author (reuse round22_sealed/AUTHOR-R22.md; rotate languages, e.g. en / ja / it / sv).
4. Bench-v1: run MNC21x/MNC22 against the now-available original control (97.0%).
5. 7B secondary: ×3 runs; check `curl 127.0.0.1:8091/health` and start the server first (see round22/queue7b.sh).
