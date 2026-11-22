# Round 9 NOTES (MNC9) — local blind test only

## What MNC9 changed (from round-8 fix list)
1. Token cut: drop redundant `you` under `task; you:`; one surname handle per repeated two-word name after first mention (bench).
2. Every permission on a `may:` line, even with no paired prohibition (`may: approve yourself + send …`).
3. Actor/identity as its own line (`finance director = Sam Okonkwo` / `owner = Carmen Soto`) immediately before naming written as `call X "Y" | never "Z"` (self-explaining without key).
4. Optional experiment: strict thresholds spelled `>N (N no)` in task sections only.
Fresh passages: P1 en routine, P2 es, P3 ja, P4 nl, P5 es routine. Built from make_mnc9.py on bench, then encoded fresh.

## Results in one line
Bench 93.2% (below MNC8's 94.1%). Fresh 95.5% vs original 100% (baselines 68–81%). Instruction-safety FAIL (4 actor-drops on naming+identity questions in direct use; no-key blind decode flips Paula/Carmen titles). No permission flips. Not a new best. Token savings back above 30% o200k (31.4%).

## Holes found
1. **Actor still dropped when the question asks naming + identity together.** Own-line `owner = Carmen Soto` / `finance director = Sam Okonkwo` before the `call` line was not enough for direct-use: the reader answers the naming half and stops. Same hole as r7/r8; the "separate line" fix did not close it for this weak reader. (Blind decode with the key does keep both lines.)
2. **No-key blind decode naming flip (§5):** `call Paula "jefa de atención" | never "dueña"` plus `owner = Carmen Soto` was reassembled as "call Carmen jefa de atención". Without the key, the binding of call-target vs owner-line is unstable. With the key it stayed correct.
3. **Threshold gloss `>N (N no)` still fails** on bench r5P1/r5P5 (exactly N answered yes) and was misread in one no-key §5 decode as "(40 or more)". Drop or replace next round; it costs tokens and does not help this reader.
4. **Token savings:** baselines still win raw tokens (terse 42.3%, LLMLingua-2 0.5 52.0% vs MNC9 31.4%), though at 14–27 points lower accuracy. Key.txt is 194 o200k — key+payload savings fall to 12.9%; no-key remains the fair comparison.
5. **Harness:** §1 English no-key decode concatenated §5 content into the same reply (one call dumping two sections). Treat as a dump bug; do not score that appended block as §1. Write-up was again the failure mode on 2026-11-06 (queue ALLDONE, no SCORES/NOTES) — this file closes that.
6. **Permission fix worked:** every `may:` line held on fresh §1/§5 (no r8-style flip next to a negative block). Keep that rule.

## Next-round fix list (baseline-won metrics first)
1. Token savings (baselines win): stay ≥30% o200k; test dropping the `(N no)` gloss and any remaining spelled-out words the 7B already predicts from `may:`/`never:`/`call` conventions; measure on bench first.
2. Actor+naming as one forced answer slot the reader cannot split: try `Nora = travel desk lead; Sam Okonkwo = finance director` (both identities on one line, no separate call rule) OR put the identity inside the call line as `call Nora "travel desk lead" | never "finance director" (=Sam Okonkwo)` — A/B on bench r5P1 naming+cc questions and fresh §1.en9/§5.en8.
3. No-key naming binding: if no-key remains the published config, the call-target must be unambiguous without the key (avoid owner-line + call-line pairs that a weak decoder can swap).
4. Drop threshold gloss experiment unless a new form beats bare `>N` on bench r5P1/r5P5.
5. Pending: fact-by-fact decode scoring; summarize + LLMLingua-2 0.5 decodes (need ≥6 GB RAM).
