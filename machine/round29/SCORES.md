# Round 29 — MNC26 (frozen main, RULES.md sha1 6c1bc095…, unchanged since r27) + MNC26x' probe (R21 + R22 + aggressive) — SCORED 2026-11-20 ~07:30 CT
Label: FULLY BLIND, INDEPENDENT AUTHOR. Originals (§1 en tailoring shop, §2 ja community-center room-rental notice, §3 es wedding-photography studio, §4 tr beekeeping-supplies shop) + 39 sealed questions (23 S, 16 F, 19 two-hop) written by a fresh no-context author (round29_sealed/AUTHOR-R29.md) after MNC26 was frozen. Payloads encoded from originals.txt only and stamped (encoded_before_questions.sha1, 06:58 CT) before questions.json was copied into round29/.
Readers: fresh no-context frontier helpers (one reader family; isolation by instruction only, told to open no file). Baselines a/b written by separate no-context helpers. Decode judge: independent no-context helper (originals + 2 decodes only).
Process note: a first batch of 8 reader answers could not be mapped reliably to their texts (a harness bookkeeping slip, not a reader result); it was discarded unscored (answers_unmapped/) and all 8 reader runs were redone with explicit mapping. Only the redone runs are scored.
facts.json: not written separately (the judge split the originals into 90 atomic facts, 61 S; decodes/judgments_mnc26.json).

## Accuracy vs savings (strong reader)
Raw regex scoring; no overrides needed.
| Text | o200k / cl100k tokens | Saved o200k / cl100k | All | S | Notes |
|---|---|---|---|---|---|
| original | 1406 / 1703 | 0 / 0 | 39/39 (100%) | 23/23 | ×1 |
| MNC26 (main, frozen, no key) | 998 / 1046 | 29.0% / 38.6% | 39/39 ×2 | 23/23 ×2 | |
| MNC26x' (R21 + R22 + aggressive, no key) | 900 / 952 | 36.0% / 44.1% | 39/39 ×2 | 23/23 ×2 | R22 (one order type per line) held: both bespoke ">$20 approver not named" answers correct |
| terse English (frontier writer) | 913 / 941 | **35.1% / 44.7%** | 39/39 ×2 | 23/23 ×2 | |
| summarize prompt | 1175 / 1388 | 16.4% / 18.5% | 39/39 | 23/23 | ×1 |
| LLMLingua-2 0.66 | 757 / 907 | 46.2% / 46.7% | 29/39 (74.4%) | 22/23 | ×1; Japanese §2 cut to 32 tokens, all 9 §2 facts lost |
| LLMLingua-2 0.5 | 587 / 706 | 58.3% / 58.5% | 25/39 (64.1%) | 18/23 | ×1; §2 lost, emergency phone and customer-action steps cut |
Key tokens: 0 (no key), break-even = 0.
Curve (o200k saved → strong-reader accuracy): summarize 16.4%→100%; MNC26 29.0%→100%; terse 35.1%→100%; MNC26x' 36.0%→100%; LLMLingua 0.66 46.2%→74.4%; LLMLingua 0.5 58.3%→64.1%.
Honest read: questions again at ceiling for every faithful text. On savings terse English beats MNC26 main by 6.1 points (o200k) and ties MNC26x' (36.0% vs 35.1% o200k; cl100k terse 44.7% vs 44.1%). Single reader family, small n.

## Blind decode of MNC26 (main form), independent judge (90 facts, 61 S)
- A: S 0 distorted / 0 lost; F 0 distorted / 0 lost; 2 added.
- B: S 0 distorted / 0 lost; F 0 distorted / 0 lost; 2 added.
Added items (both decodes): (1) the year "2026" on the §2 booking-open date — this came from the encoder: the payload wrote "2026 Dec 1" while the original gives only 12月1日（火）; an encoder inference (F, not S), counted as a hole; (2) a note that the approver of bespoke discounts over $20 is not named — correct per R20 marker, not a distortion.
The r27/r28 discrete-time hole did not recur (no time-range readings; the original said "do not check at other times", encoded as "no other times").

## Instruction safety verdict
MNC26 main: S 23/23 ×2 direct use, 0 S errors in both blind decodes → **PASS**. Third consecutive fully blind round on the same frozen main (RULES.md sha1 6c1bc095): r27 PASS, r28 PASS, r29 PASS → **ready counter MNC26: 3/3** — AIL MNC26 meets the stated bar for live instructions (3 consecutive blind rounds at 100% instruction-safety, strong reader). Caveats: one reader family; question sets at ceiling; terse English is equally safe and saves more on this round.

## Weak reader (local Qwen2.5-7B, secondary)
Queued as a detached job (round29/queue7b.sh: mnc26, mnc26x, original ×3). Pending at write-up; to be scored next run.

## Frozen bench-v1
Not run this round (at ceiling for the strong reader). Pending.
