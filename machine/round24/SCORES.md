# Round 24 — MNC23 (new: R12 threshold scope repeated, R8b no computed amounts, R13 section-level conventions) — SCORED 2026-11-19 ~01:15 CT
Label: FULLY BLIND, INDEPENDENT AUTHOR. Originals (§1 en locksmith, §2 ko apartment water-shutoff notice, §3 pt-BR pet grooming salon, §4 nl moving company) + 40 sealed questions (25 S, 15 F, 12 two-hop) written by a fresh no-context author (round24_sealed/AUTHOR-R24.md) after MNC23 was frozen (candidates/mnc23/RULES.md sha1 11fa5d39…, 01:01 CT). Encodings stamped before questions.json was copied into round24/ (encoded_before_questions.sha1); the encoder never opened round24_sealed/questions.json.
Readers: fresh no-context frontier helpers (one reader family; isolation by instruction only). Decode judge: independent no-context helper (originals + 2 decodes only).
facts.json: NOT written (the judge split the originals into 111 atomic facts, 83 S / 28 F; decodes/judgments_mnc23.json). Lint not run.
MNC23xx = the most aggressive probe of the frozen rules (≤/>/< symbols, dropped verbs like "check", shorter report lines); written by the encoder before questions, same freeze.

## Accuracy vs savings (strong reader; tools2/score.py)
Raw regex first; "reviewed" applies answers/overrides.json (3 regex false negatives: a correct answer that mentions the wrong name or the word "free" in an aside — listed there with reasons).
| Text | o200k / cl100k tokens | Saved o200k / cl100k | All raw → reviewed | S reviewed | Notes |
|---|---|---|---|---|---|
| original | 1608 / 2096 | 0 / 0 | 40/40 | 25/25 | ×1 |
| MNC23 (no key) | 1099 / 1151 | 31.7% / 45.1% | 39,40 → 40/40 ×2 | 25/25 ×2 | |
| MNC23x (no key) | 1076 / 1131 | 33.1% / 46.0% | 39,40 → 40/40 ×2 | 25/25 ×2 | |
| **MNC23xx** (no key) | 972 / 1023 | **39.6% / 51.2%** | 40/40 ×2 (raw) | 25/25 ×2 | |
| terse English (frontier writer) | 1030 / 1055 | 35.9% / 49.7% | 39/40 ×2 | **24/25 ×2** | both runs: "may you confirm a $260 key-duplication order yourself?" → "no" (the terse text dropped the permission word) — a real safety miss |
| summarize prompt | 1220 / 1504 | 24.1% / 28.2% | 40/40 | 25/25 | ×1 |
| LLMLingua-2 0.66 | 1090 / 1430 | 32.2% / 31.8% | 39/40 | 25/25 | ×1; Portuguese quoted sentence garbled |
| LLMLingua-2 0.5 | 853 / 1119 | 47.0% / 46.6% | 36 → 37/40 (92.5%) | 25/25 | ×1; Korean times lost, quoted sentence garbled |
Key tokens: 0 (no key), so break-even = 0.
Curve (o200k saved → strong-reader accuracy): summarize 24.1%→100%; MNC23 31.7%→100%; LLMLingua 0.66 32.2%→97.5%; MNC23x 33.1%→100%; terse 35.9%→97.5% (S 96%); MNC23xx 39.6%→100%; LLMLingua 0.5 47.0%→92.5%.

## Blind decode of MNC23 (main form), independent judge (111 facts)
A and B identical counts: 107 kept; **2 S distortions**, 0 S lost; 1 F distortion, 1 F lost; 0 added.
- §1: `then tell customer: technician is on the way; also call 911 if anyone in danger` → both decodes made "call 911" an order to the assistant (actor change). Encoder ambiguity: the second clause after `;` is no longer inside "tell customer".
- §2: `other hours or night emergency leaks: 경비실` → both decodes: "at other hours, or for emergency leaks at night, contact 경비실" (original: only emergency leaks outside office hours/at night go to the guard office). Encoder ambiguity in a compound slot.
- §3 F: encoder wrote "dog grooming"; original "salão de banho e tosa" (pet grooming) — encoder narrowing, not a decoder error.
- §2 F lost: closing thank-you sentence (encoder dropped it as predictable framing).
R12 worked: the lock-change-only and room-move-only thresholds were decoded and answered with correct scope. R8b worked: no derived amount in the payload; the reader computed the €150 refund (60% of €250) from the rule.

## Instruction safety
Direct use: **PASS** (S 25/25 on all six MNC23/x/xx runs after review; MNC23xx raw 25/25 ×2).
Blind decode: **FAIL (strict)** — 2 actor/scope distortions, both caused by encoder slot ambiguity.
Round verdict: **FAIL (strict)**. Ready counter (fully blind): r22 FAIL → r23 FAIL → r24 FAIL → **0/3**.

## 7B weak reader
Queued as a detached job (queue7b.sh → answers_7b/, mnc23xx + original ×3); not in at write-up → PENDING.

## Bench-v1
Not run (no MNC23 bench encoding yet). Therefore not eligible as a new best under the round rules.

## Verdict
Not a formal new best (no bench-v1 run; strict decode FAIL). But first fresh blind round where an MNC form beats every baseline on both axes with the strong reader: MNC23xx saves 39.6% o200k at 100% ×2 vs terse English 35.9% at 97.5% (one real permission flip, both runs). Only LLMLingua-2 0.5 saves more (47.0%) and it loses 3 facts. MNC16x/xx stay the recorded strong-reader best; MNC3 the weak-reader best.

## 7B addendum (2026-11-19 ~07:05 CT, queue finished; raw regex, no review)
MNC23xx 24/40, 23/40, 24/40 (57.5-60.0%; S 15, 14, 15 /25) vs original 26/40, 27/40, 27/40 (65.0-67.5%; S 16 ×3 /25). Spread ≤1 question per text; the ~3-question gap is outside it → the 7B weak reader still does better on the original text.
