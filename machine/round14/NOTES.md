# Round 14 NOTES (sprint 2026-11-17): MNC18 candidate + bench-v2

## What changed
1. **Slip-class rules frozen as the MNC18 candidate before any test** (candidates/mnc18/RULES.md):
   - R1 deadline words come from a fixed set (before / by / at / until / within / after / from), placed before the time. They are never dropped or swapped. "No later than" and its equivalents in other languages map to `by`.
   - R2 `tell <who>: <action>` / `ask <who>: …`. A bare `<who>: <action>` is banned in instruction sections, and every action line starts with the assistant's verb.
   - R3 the object noun and scope qualifiers of every action, report or deadline line are kept.
   - R4 a mechanical lint: facts.json carries `must` regexes per fact, written before encoding. The payload is frozen only when 100% pass.
2. **bench-v2 built and frozen.** 6 passages (en/de/fr/ja/es/zh), 2,217 o200k tokens, 65 facts and 89 questions (61 safety, 40 two-hop). The questions were written after the encodings were frozen.
3. **Fresh rounds 15, 16 and 17 prepared and frozen** (en/pt/ko/pl, en/it/nl/zh, en/fr/ja/de; 42, 40 and 36 questions).

## Holes / findings so far (encoder side; no strong-reader data yet)
1. **Dense passages cut savings.** On bench-v2, MNC18 saves 32.7% o200k (round 15 34.0%, round 16 27.8%). MNC17xx saved 46.9% on round 13's lighter passages. When every clause carries a condition, an actor or a boundary, there's little filler left to drop, and the R1-R3 rules add a few tokens back (`tell X:`, `by`). The real savings ceiling for safety-complete text is lower than earlier rounds suggested.
2. **Word abbreviation doesn't save tokens.** A trial MNC18zz (mgr, OK, →, cust, biz d …) saved only 0.2 points over MNC18z (38.9% vs 38.7%). It also introduced meaning risks: "approved list" became "OK list", and "HQ office manager" became "HQ mgr". It was discarded (bench-v2/notbench/). Savings have to come from structure (grouped `never:` lines, merged rule lines, a shared section frame), not from shorter words.
3. **The lint caught one form slip before freezing** ("other-week make-up", fixed). That was the r13 "overview" class: catching it now costs nothing.
4. **LLMLingua-2 still truncates Japanese and Chinese** (both rates on §4; spliced fragments in §6 at 0.5). Report its savings both with and without those sections.
5. **The 7B weak reader breaks on long question lists** (ID shifts). Next time, split the weak-reader prompts per section, or drop the 7B for bench-v2.

## Next
Dispatch the strong-reader jobs (../SPRINT-DISPATCH.md), then score. If MNC18 passes, rounds 15 and 16 decide the counter. If it fails, write MNC19 (fix only the failing class), re-freeze it, re-encode every round no reader has seen, and restart the counter at 0.

## Strong-reader results (2026-11-17 evening): see SCORES.md
- Direct use: MNC18 and MNC18z 100% ×2 (61/61 safety), equal to the original; terse English 95.5%, LLMLingua-2 0.66 79.8%, 0.5 61.8%.
- **Baseline wins first:** LLMLingua-2 0.5 saves more tokens (57.0% vs MNC18z 38.7%), but at 61.8% accuracy. No baseline matches MNC on accuracy.
- Hole: passive obligation lost its actor in both blind decodes (P6.6 invoice info: customer submits → "you provide"). Fix: keep the actor on every obligation line (MNC19 rule 2).
- Savings: MNC18z (grouped `never:` lines, `(=` identity form) held 100% at +6 points over MNC18. Its lint misses were form-only. Next: make MNC18z's structural cuts the MNC19 default and fix the lint regexes to accept those forms.
