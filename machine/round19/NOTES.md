# Round 19 notes
- Encoded with MNC19 frozen (candidates/mnc19/RULES.md sha1 018f157b…), no rule changes; only encoder wording fitted to facts.json lint before questions were seen.
- Order: facts.json → payload → lint → tokens → encoded_before_questions.sha1 → copy sealed questions → questions.sha1 → dispatch prompts. Timestamps in the .sha1 files.
- Decode judge will be an independent no-context helper (JUDGE-R19-20.md) that sees only originals + decodes — first round family where judge ≠ encoder.
- Caveats: one reader family; isolation by instruction only; facts.json written by the encoder.

## Scoring 2026-11-18 ~01:15 CT
- Result: safety PASS (direct 26/26 ×2, judge 0 S distortions ×2). Ties original at 100%.
- Holes: none found in this round. Baselines and 7B not run — next round must run at least terse English + LLMLingua-2 on fresh passages so savings can be compared.
