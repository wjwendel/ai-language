# Round 12 NOTES (MNC16 / MNC16x / MNC16xx)

## What changed
- Bench-v1 was scored with the strong reader for the first time: original ×2, MNC16x ×2, MNC16 ×1, MNC14 ×1, LLMLingua-2 0.5 ×1, terse ×1.
- Fresh round 12: §1 en (café supplier orders, instruction), §2 zh (metro news), §3 fr (chalet group chat), §4 pt (pool closure notice), §5 pl (boiler-service instruction). Encoded before the questions were written.
- The baselines a/b are now written by a frontier helper (they were written by the 7B before). This is the fair comparison now that the reader is a frontier model.
- The section tag is `§N you, xx` (it replaces "task xx; you:"). The key was dropped (no key in any variant).

## Holes found
1. **Dropping "by" from deadlines changes the deadline.** `15:00 Nowak: next day's visits` decoded as "at 15:00". Direct-use QA did not catch this because the question itself said "by 3 p.m.". Deadline words (by/before/until) are safety content and must never be dropped.
2. **The language tag was read as an instruction.** `you, en` / `you, pl` decoded as "work in English/Polish". Use a tag the reader cannot read as an order, or drop the language code from instruction sections.
3. **Speaker pronouns are not resolved.** `母: ... →me` was answered as "to me / the writer" on both runs. Write the speaker's name, not "me", in chat sections (`→母`).
4. **Encoder slips that cost nothing to fix:** "before" was written as "by" (§3), the announcer was dropped (§4 Junta de Freguesia), and "repair prices" was shortened to "prices" (§5). The fact list must be checked line by line before the payload is frozen.
5. **Strong frontier writers make strong baselines.** With a frontier writer, terse English reached 100% at 35.4% saved, compared with 73% when the 7B wrote it. MNC's edge over well-written terse English is now about +10 points of savings at the same accuracy, not accuracy. This is the honest headline.
6. **Bench-v1 is at ceiling for the strong reader** (the original scores 221/221 ×2). It can still catch regressions, but it can no longer rank close versions. A harder frozen set is needed: longer passages, more conditions per passage, and exactly-N boundary questions.

## Next-round fix list (baseline-won metrics first)
1. **Tokens: LLMLingua-2 0.5 still saves more** (51.0% fresh / 50.3% bench vs MNC16xx 45.4% / MNC16x 43.5%), at 85-89% accuracy. Target MNC17 at ≥50% o200k with 100% strong-reader accuracy and safety. Ideas: drop repeated names after the first mention everywhere, shared role conventions, merge news slots, and no language codes.
2. Fix holes 1-4: keep by/before/until, use speaker names instead of "me", check every fact before freezing, and use a neutral section tag.
3. Blind round 13: MNC17 with strong-reader direct use (×2) and blind decode (×2), with facts.json written BEFORE encoding. This is the next step toward the ready bar (needs 3 consecutive blind rounds at 100% safety, decode included).
4. Build bench-v2 (harder, frozen) so the strong reader can separate versions. Keep bench-v1 as a regression check.
5. Weak reader: run 7B ×3 on MNC16x/xx bench only when ≥6 GB RAM is free and nothing else is running. Add a second strong-reader family if one is available.
