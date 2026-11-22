# Round 20 notes
- Encoded with MNC19 frozen (candidates/mnc19/RULES.md sha1 018f157b…), no rule changes; only encoder wording fitted to facts.json lint before questions were seen.
- Order: facts.json → payload → lint → tokens → encoded_before_questions.sha1 → copy sealed questions → questions.sha1 → dispatch prompts. Timestamps in the .sha1 files.
- Decode judge will be an independent no-context helper (JUDGE-R19-20.md) that sees only originals + decodes — first round family where judge ≠ encoder.
- Caveats: one reader family; isolation by instruction only; facts.json written by the encoder.

## Scoring 2026-11-18 ~01:15 CT
- Result: strict safety FAIL on direct use (1 run omitted the lifeguard's phone number in an emergency answer); decodes PASS.
- Hole: emergency contact numbers attached to a call step can be dropped by a reader when the step is compressed ("call X yourself"). Fix to try: R7 — keep the number adjacent to the verb ("call 604 555 017 (lifeguard Kamil Nowak)") so it can't be read as optional.
- Fix list (baselines first): savings on independent-author prose are only 26-28% o200k (terse English and LLMLingua-2 0.5 saved more on earlier rounds) — run baselines on r19/r20 originals; bench-v1 regression for MNC19 still not run, so no new-best claim.
