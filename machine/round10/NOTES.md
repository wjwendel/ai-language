# Round 10 NOTES (MNC13) — local blind test only

## What MNC13 changed (from MNC12 failure / round-9 fix list)
1. Base MNC11 (best compact form; MNC12's boundary lines and "skip next rule" pointers dropped).
2. Prohibitions fused into the action phrase: `forward to Grace without replying`, `ask room number without promising any discount`, `email vendor once asking for it, without adding row until vendor replies`.
Fresh passages: P1 en routine, P2 pt, P3 zh, P4 de, P5 fr routine.

## Results in one line
Fresh 87.2% vs original 98.8% (baselines 72–80%). Saved 24.6% / 35.8% (terse English 38.3%, LLMLingua-2 0.66 34.4% save more). Instruction-safety FAIL (4 actor-drops, 2 unapplied thresholds in direct use; one distorted prohibition in no-key French decode). Not a new best.

## Holes found
1. **Token savings regressed to 24.6% o200k**, lowest MNC round, and two baselines save more. "without X" fusion and full-word thresholds cost tokens; the fresh passages (pt/de/fr) also contain many exact source-language terms MNC keeps verbatim.
2. **Actor+naming hole still open (4th round running).** `Helen Park = controller` / `Sophie Laurent = owner` on their own lines; the reader answers only the `call` half. Every line-layout fix so far (separate line, actor first, fused) has failed on this reader.
3. **Rule-restating instead of deciding.** On "12 requests waiting, warn now?" the reader copied the rule line `more than 20 requests waiting: warn Julien immediately` as its answer. Condition lines in `X: Y` form invite verbatim copying; original prose did not have this problem.
4. **Fused "without X" prohibitions worked** in direct use (no lost negation on §1/§5). Keep.
5. **Fact losses on non-instruction passages:** dropped the date (Nov22 → "next weekend", §3), turned "half day" extra into "extra day" (§3 es), and named the city instead of Petra Hoffmann for "who" (§4) — the payload puts the place before the speaker, so a weak reader binds the wrong entity.
6. **No-key French decode turned "never copy Sophie" into "never believe her"** — `cc` abbreviation is not safe across languages; spell the action.
7. **Harness:** one decode call ran 4.4 h; add a per-call max-tokens cap and wall timeout to decode.py. The 2026-11-11 run again stopped before the write-up; the write-up should run before (not after) long decode queues finish, or be its own small step.

## Next-round fix list (baseline-won metrics first)
1. Token savings (terse English and LLMLingua-2 win): get back ≥30% o200k. Measure where MNC13 spends tokens vs terse English on P2/P4/P5 and cut there (e.g. drop "@" time markers when a number is unambiguous, drop repeated section headers).
2. Actor+naming: stop trying line layouts; test answer-shaped identity, e.g. one line `controller: Helen Park (not Grace); call Grace "payables lead"`, A/B on bench r5P1 and fresh §1.en7/§5.en8. If it still fails, accept that this 7B reader needs the original sentence for naming+identity and keep those sentences unencoded (measure the token cost).
3. Condition lines: write thresholds so they read as a decision, e.g. `warn Julien only if more than 20 waiting`, and check whether the reader still copies the rule.
4. Keep entity-first ordering for "who" facts (speaker before place); keep exact dates even when a relative phrase exists.
5. Spell `cc` as "copy"; keep "without X" fusion.
6. Harness: cap decode tokens and per-call time; bench MNC13/MNC14 on frozen bench-v1; pending fact-by-fact decode scoring.
