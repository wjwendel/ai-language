# Round 21 notes (encoder, 2026-11-18 ~07:05-07:11 CT)
- Encoded with MNC20 frozen (candidates/mnc20/RULES.md sha1 7e52a438…, mtime 07:04 CT; originals.txt mtime 07:05 CT). No rule changes; round21_sealed/ never opened before step 6 (copied blind).
- Order: facts.json → payload_mnc20 + payload_mnc20x → lint (46/46 both) → tokens → encoded_before_questions.sha1 (07:08:23) → questions copied (07:08:28) → baselines → dispatch.
- §2 (ko notice) is not an instruction section → header `§2` (no "you"); §1/§3/§4 are `you`.
- mnc20x = savings-curve variant only (not the candidate); same safety rules (R7 call-number-first, never: lines, decision words on time/age).
- lint_mnc20x.txt not in encoded_before_questions.sha1 (step list named lint_mnc20.txt only); payload_mnc20x.txt is.
- Caveats: facts.json written by the encoder; lint regexes are loose enough that lint pass ≠ meaning preserved.

# Round 21 notes (2026-11-18 07:00-07:45 CT run)
- MNC20 = MNC19 + R7 (emergency/call number right after "call"). RULES.md header says "~07:10 CT" but the file/sha1 stamp is 07:04 CT (before originals existed at 07:05); the stamp is authoritative.
- Order: MNC20 frozen → independent author writes originals + sealed questions → encoder writes facts.json, payload_mnc20, payload_mnc20x, lint, tokens → stamp → copy questions → readers/baselines → independent judge.
- R7 worked: every emergency answer included the number on both MNC20 runs (r20 hole closed on this round).

## Holes found
1. Derived amounts: "half hourly rate = 150 TL per hour" (MNC20) / "half hourly rate 150 TL/hour" (MNC20x) is ambiguous about whether 150 is the full rate or the charge. MNC20x reader charged 150 instead of 300; the judge flagged both decodes. Fix R8: put the resulting amount directly as the object of the charge verb, and drop the derivation or state it after: `later cancellations: charge 150 TL per hour (half price)` → better without parentheses: `later cancellations: charge 150 TL per hour, which is half the hourly rate`.
2. Identity form `(="title", never "x")` decodes as an invented naming rule when the original only says "X is the title, not x". Fix R9: when the original has no naming rule, write `X = title, not x`; keep `never "x"` only when the original forbids the name/title.
3. 24h-time conversion is harmless for readers but trips English-time regexes; question authors should accept 24h times (16:00) — fix in the author prompt, not in the encoding.

## Next-round fix list (baselines first)
1. **Savings — a baseline wins:** terse English (frontier writer) gets the same 100% at 36.5% vs MNC20 26.8% o200k. LLMLingua-2 0.66 also saves more (32.5%) at lower accuracy. MNC must reach ≥37% at 100% S to justify itself; MNC20x (41.3%) is the candidate base once R8 is applied.
2. MNC21 = MNC20 + R8 + R9; make the aggressive (x) form the main candidate. New fully blind independent-author round 22; also run terse English ×2 so the comparison has the same run count.
3. Bench-v1: run original-text control on bench/strong_mnc20/questions.json and review the 7 F misses, so the regression has a baseline.
4. 7B secondary: only if ≥6 GB free.
