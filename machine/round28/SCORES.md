# Round 28 — MNC26 (frozen main, RULES.md sha1 6c1bc095…, unchanged since r27) + MNC26x probe (R21 + aggressive) — SCORED 2026-11-20 ~01:10 CT
Label: FULLY BLIND, INDEPENDENT AUTHOR. Originals (§1 en chimney-sweep business, §2 zh residential-compound smart parcel-locker notice, §3 de pool-care business, §4 pl aquarium service) + 39 sealed questions (25 S, 14 F, 15 two-hop) written by a fresh no-context author (round28_sealed/AUTHOR-R28.md) after MNC26 was frozen. Payloads encoded from originals.txt only and stamped (encoded_before_questions.sha1, 00:59 CT) before questions.json was copied into round28/.
Readers: fresh no-context frontier helpers (one reader family; isolation by instruction only, told to open no file). Baselines a/b written by separate no-context helpers. Decode judge: independent no-context helper (originals + 2 decodes only).
facts.json: not written separately (the judge split the originals into 110 atomic facts, 69 S; decodes/judgments_mnc26.json).

## Accuracy vs savings (strong reader)
Raw regex → reviewed (answers/overrides.json): summ_r1 §3.q6 correct answer with dates written "30.04/15.04" (regex false negative). No other reviews; every other miss below is a real error.
| Text | o200k / cl100k tokens | Saved o200k / cl100k | All (reviewed) | S | Notes |
|---|---|---|---|---|---|
| original | 1572 / 1822 | 0 / 0 | 39/39 (100%) | 25/25 | ×1 |
| MNC26 (main, frozen, no key) | 1025 / 1046 | 34.8% / 42.6% | 39/39 ×2 | 25/25 ×2 | |
| MNC26x (R21 + aggressive, no key) | 945 / 966 | **39.9% / 47.0%** | 38/39, 39/39 | 24/25, 25/25 | run 1 §3.q2 invented an approver: x merged the chemicals limit and the spare-parts approval rule onto one line, so the reader applied Lukas Brandauer's approval to chemical orders over 250€ (original names no approver there) |
| terse English (frontier writer) | 1030 / 1052 | 34.5% / 42.3% | 39/39 ×2 | 25/25 ×2 | |
| summarize prompt | 1325 / 1508 | 15.7% / 17.2% | 39/39 (reviewed) | 25/25 | ×1 |
| LLMLingua-2 0.66 | 1035 / 1185 | 34.2% / 35.0% | 31/39 (79.5%) | 23/25 | ×1; two prohibitions read as permissions (§3 Kessel cc, chlorine dosing), phone number cut, Chinese section facts lost |
| LLMLingua-2 0.5 | 819 / 933 | 47.9% / 48.8% | 27/39 (69.2%) | 20/25 | ×1; 4 prohibitions unreadable ("not stated"), lost cold-chain rules, phone cut |
Key tokens: 0 (no key), break-even = 0.
Curve (o200k saved → strong-reader accuracy, mean of runs): summarize 15.7%→100%; LLMLingua 0.66 34.2%→79.5%; terse 34.5%→100%; MNC26 34.8%→100%; MNC26x 39.9%→98.7% (1 S error in 2 runs); LLMLingua 0.5 47.9%→69.2%.
Honest read: this question set was easy for every faithful text (original, terse, summarize and MNC26 all 100%). MNC26 main and terse English tie on accuracy and savings (34.8% vs 34.5%, inside noise). MNC26x is the only text that saves ~40% while keeping >95%, but it had one safety error, so it is not safe yet. Single reader family, small n.

## Blind decode of MNC26 (main form), independent judge (110 facts, 69 S)
- A: S 0 distorted / 0 lost; F 3 distorted / 0 lost; 0 added.
- B: S 0 distorted / 0 lost; F 3 distorted / 0 lost; 0 added.
Both decodes made the same 3 F distortions: discrete inbox check times (`wkdays 8,13:30h`) read as a time range ("8:00 to 13:30") in §1, §3, §4 — the known r27 hole; R21 (`at 8 + 13:30h`) is in the x form only, because main is frozen for the counter. Judge counted "close the damper themselves" as harmless wording (customer still the actor).

## Instruction safety
MNC26 (main, frozen): direct use S 25/25 ×2; blind decodes 0 S distortions/losses ×2 → **PASS** (same caveat as r27: the judge classes inbox check times as F; counted as F consistently).
Ready counter (fully blind, one frozen main version, 3 consecutive): r27 PASS (MNC26 1/3, after the parent's correction) → **r28 PASS → MNC26: 2/3**.
MNC26x: FAIL as a candidate this round (1 invented approver in direct use).

## Bench-v1
Not run (at ceiling for the strong reader). No formal new-best claim.

## 7B weak reader (secondary)
round28/queue7b.sh (MNC26 main + original ×3) finished 01:19 CT; see addendum below.

## Verdict
Not a new best. MNC26 main: 100% strong-reader accuracy ×2, safety PASS, counter MNC26: 2/3, but only ties terse English on savings this round. MNC26x saves 5.4 points more than terse English (39.9% vs 34.5% o200k) but slipped once on safety.


## 7B addendum (scored 2026-11-20 ~01:20 CT, same run; local Qwen2.5-7B, secondary weak reader, ×3, raw regex, not reviewed)
| Text | run1 | run2 | run3 | spread | S range |
|---|---|---|---|---|---|
| MNC26 (main) | 59.0% | 61.5% | 61.5% | 59.0-61.5% | 64.0% ×3 |
| original | 64.1% | 56.4% | 64.1% | 56.4-64.1% | 60.0% ×3 |
The ranges overlap: a tie inside noise on the weak reader this round (MNC26 S 16/25 vs original 15/25 in every run). Unlike r27 (MNC26x clearly behind), the main form did not lose to the original here.

