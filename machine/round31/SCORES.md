# Round 31 scores (2026-11-21, run ~01:16-02:00 CT) — fully blind, independent author
Texts: originals.txt written by an independent no-context author (en mobile-sauna rental / zh night-school calligraphy class notice / it camper rental / pl escape room; 1,949 o200k tokens; distractor rules, day-only and group-only rules, "only X may" rules, "never X unless Y", modality word and listed-noun pair in the everyday section). 39 questions (32 S, 7 F, 20 two-hop, ~1/3 in Chinese/Italian/Polish). questions.json sealed in round31_sealed until both payloads were encoded and hashed (encoded_before_questions.sha1).
Versions: **MNC28 = new main** (MNC27 + R24: keep must/only/required words and every listed noun in all sections; MNC28-RULES.md sha1 f70a3563). Promotion restarts the ready counter. MNC28x = aggressive probe (bare "you" headers, '/' units, short approval phrasing, denser Chinese section).
Readers: fresh no-context frontier helpers (one reader family; isolation by instruction only). Baselines a/b written by separate no-context helpers. Decode judge: independent no-context helper (originals + 2 decodes only). No scorer overrides this round.

## Accuracy vs savings (strong reader)
| Text | Saved o200k / cl100k | Direct use (S) |
|---|---|---|
| MNC28 (main, no key) | 28.1% / 30.8% | 100% ×2 (S 32/32 ×2) |
| MNC28x (probe, no key) | 38.5% / 41.1% | 100% ×2 (S 32/32 ×2) |
| original | 0 | 100% |
| terse English | 37.6% / 44.5% | 100% ×2 |
| summarize | 20.8% / 23.1% | 100% ×1 |
| LLMLingua-2 0.66 | 33.2% / 34.2% | 87.2% ×1 (S 28/32: lost the "help is coming" half of two emergency steps, Polish phone prefix, rice-paper and make-up-class facts) |
| LLMLingua-2 0.5 | 48.2% / 50.0% | 69.2% ×1 (S 24/32: invented Daniel as firewood approver, dropped emergency steps, lost most Chinese facts) |
Curve (o200k saved → accuracy): summarize 20.8%→100%; MNC28 28.1%→100%; LLMLingua 0.66 33.2%→87.2%; terse 37.6%→100%; MNC28x 38.5%→100%; LLMLingua 0.5 48.2%→69.2%.
Honest read: questions at ceiling for every faithful text again. **Terse English beat the MNC28 main on savings by 9.5 points (o200k) at equal accuracy**; it translated the Chinese section into English, which this round was cheaper. MNC28x saved the most of any 100% text on o200k (+0.9 over terse, inside noise) but terse still wins on cl100k (44.5% vs 41.1%). The R24 explicitness and the token-heavy original-language Chinese line-by-line form cost the main form savings (§2: 391 → 373 tokens only).

## Blind decode (MNC28, key-less, 2 decodes; judge: 205 facts, 133 S / 72 F)
A: 205 kept, 0 distorted, 0 lost, 0 added. B: 205 kept, 0 distorted, 0 lost, 0 added (judge note, not counted: B wrote "On Friday" for "every Friday").

## Instruction-safety
MNC28: **PASS** (100% S questions ×2, 0 S decode errors). Ready counter: **MNC28: 1/3** (promotion restarted it; MNC26 keeps its r27-r29 3/3; MNC27 ended at 0/3).

## Not run / pending
- Local 7B weak reader: NOT run — only ~2.4 GB RAM free at start (needs ~6 GB). Pending.
- Bench-v1 on MNC28: not run (at ceiling; time).
- MNC26 reference: not run this round.
