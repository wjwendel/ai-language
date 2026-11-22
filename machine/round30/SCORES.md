# Round 30 scores (2026-11-20, run 13:12-~13:45 CT) — fully blind, independent author
Texts: originals.txt written by an independent no-context author (en tree surgery / ko pool lane-rule notice / pt dog walking / nl wine shop; 1,131 words, 1,936 o200k tokens; harder: distractor rules, day-only and group-only rules, "never X unless Y"). 38 questions (28 S, 10 F, 16 two-hop, ~1/3 in Korean/Portuguese/Dutch), sealed until both payloads were encoded (encoded_before_questions.sha1, questions.sha1).
Versions: **MNC27 = new main** (promoted MNC26x' form + R23 no added implicit detail + exception-bearing prohibitions on their own line; candidates/mnc27/RULES.md). Promotion restarts the ready counter. MNC26 (ready version, RULES sha1 6c1bc095, frozen) run alongside as reference.
Readers: fresh no-context frontier helpers (one reader family; isolation by instruction only). Baselines a/b written by separate no-context helpers. Decode judge: independent no-context helper (originals + 2 decodes only). One shared regex fix: §1.q9 reject regex fired on every text's correct "10%" answer because it mentioned the Tuesday-only 15% as explanation; overridden to correct for all texts (answers/overrides.json).

## Accuracy vs savings (strong reader, reviewed)
| Text | Saved o200k / cl100k | Direct use (S) |
|---|---|---|
| MNC27 (main, no key) | 36.6% / 49.7% | 100% ×2 (S 28/28 ×2) |
| MNC26 (ready reference, no key) | 31.5% / 45.7% | 100% ×2 (S 28/28 ×2) |
| original | 0 | 100% |
| terse English | 28.7% / 32.4% | 100% ×2 |
| summarize | 30.6% / 34.0% | 100% ×1 |
| LLMLingua-2 0.66 | 34.3% / 33.6% | 97.4% ×1 (S 28/28; 1 F "not stated") |
| LLMLingua-2 0.5 | 49.3% / 48.8% | 92.1% ×1 (S 27/28: exactly-48h ticket cancel answered "60%/€21" instead of nothing) |
Curve (o200k saved → accuracy): terse 28.7%→100%; summarize 30.6%→100%; MNC26 31.5%→100%; LLMLingua 0.66 34.3%→97.4%; MNC27 36.6%→100%; LLMLingua 0.5 49.3%→92.1%.
Honest read: questions at ceiling for every faithful text again. This round MNC27 saved the most of any text at 100% (7.9 points more than terse English, 6.0 more than summarize, o200k; 17.3 more than terse on cl100k). Terse English this time kept the Korean section in Korean (429 tokens), which lowered its savings; in r29 terse beat the MNC main by 6.1 points. Single reader family, small n.

## Blind decode (MNC27, key-less, 2 decodes; judge: 133 facts, 98 S / 35 F)
A: 131 kept, S distortions 2, S losses 0, F 0/0, added 0. B: identical counts.
Both distortions are encoder-caused and in the everyday Korean §2: (1) "must collect a new card" (받으셔야 합니다) — the payload line dropped "must", decodes read "new cards will be issued to"; (2) contact for "complaints or inquiries" encoded as "questions" only. Instruction sections §1/§3/§4: 0 S errors in both decodes.

## Instruction-safety
MNC27: direct use S 28/28 ×2, but 2 S-tagged decode distortions (both encoder-caused, everyday §2) → under the strict gate (0 S errors anywhere) **FAIL**. Ready counter: **MNC27: 0/3**.
MNC26 (ready reference): direct use S 28/28 ×2; no decode run this round, so this round is not counted toward its streak (its 3/3 from r27-r29 stands).

## Weak reader (local Qwen2.5-7B, secondary)
Round 29 (scored this run, 3 runs each): MNC26 56.4/61.5/59.0%, MNC26x' 56.4/53.8/59.0%, original 59.0% ×3 — all inside the spread, ties.
Round 30 (3 runs each, raw regex, no overrides): MNC26 68.4/68.4/63.2%, MNC27 57.9/57.9/50.0%, original 63.2/63.2/60.5%. MNC26 ties or slightly beats the original; MNC27 is below the original's spread for the weak reader (the more aggressive form costs a small model accuracy).

## Bench-v1
Not run (at ceiling); still owed for MNC27 before any formal new-best claim.

## Gmail
No new xAI or Anthropic reply since the Oct 24 auto-replies.
