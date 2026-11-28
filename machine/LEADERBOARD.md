
### MNC7 draft (2026-11-01, encoder-side only, NOT reader-tested)
| Version | Saved o200k / cl100k (bench-v1, 15 passages) | Direct-use | Instruction-safety | Best baseline |
|---|---|---|---|---|
| MNC7 draft (scoped condition blocks, split negation lines, no `(=N: no)` gloss) | 31.2% / 41.5% (2273 / 2328 tokens; MNC6 2289 / 2345) | pending (reader not run: RAM) | pending | – |
Not a result and not a new best; MNC3 stays current best. Details: machine/bench/NEXT.md.

### r7 MNC7 (2026-11-02/03, local Qwen2.5-7B only; some baselines pending)
| Version | Saved o200k / cl100k | Direct-use fresh (94 q) | Instruction-safety (direct use / blind decode) | Frozen bench-v1 direct-use | Best baseline |
|---|---|---|---|---|---|
| MNC7 no key | 30.1% / 39.8% | 93.6% (original 96.8%) | 4 failures in §1 (permission flip "may fix name typos" → no, en+es; manager actor dropped, en+es) / blind no-key decode 4 failures (FAIL) | **93.2%** at 31.2% / 41.5% saved (MNC6 92.8%, original 91.9%) — top bench version, +1 question, noise-level | fresh: terse English 79.8% at 41.8% / 46.0%; bench: LLMLingua-2 0.66 81.4% |
Not a new best (loses to original text on fresh passages; safety failures). MNC3 stays current best. Details: machine/round7/SCORES.md. The 78.3% in bench/directuse/score_mnc7.txt is a pre-review regex snapshot, superseded by 93.2%.

### r8 MNC8 (2026-11-04 runs, written up 2026-11-05; local Qwen2.5-7B only; some decodes pending)
| Version | Saved o200k / cl100k | Direct-use fresh (86 q) | Instruction-safety (direct use / blind decode) | Frozen bench-v1 direct-use | Best baseline |
|---|---|---|---|---|---|
| MNC8 no key | 28.4% / 39.2% | 90.7% (original 96.5%) | 6 failures: §5 permission flip "may approve returns ≤7 days" → no (en+es), §1 CFO actor dropped (en+es), §5 threshold not answered (en+es) / blind decode: no key drops §5 naming rule (en+zh); with key §5 zh turns "never" into "has never" (FAIL) | **94.1%** (208/221) at 30.3% / 40.8% saved (MNC7 93.2%, original 91.9%) — top bench version, +2 questions, noise-level | fresh: terse English 73.3% at 44.3% / 50.2%; LLMLingua-2 0.66 72.1% |
Not a new best (loses to original text on fresh passages; safety failures). MNC3 stays current best. Details: machine/round8/SCORES.md.

### r9 MNC9 (runs 2026-11-06, written up 2026-11-07; local Qwen2.5-7B only)
| Version | Saved o200k / cl100k | Direct-use fresh (88 q) | Instruction-safety | Frozen bench-v1 | Best baseline |
|---|---|---|---|---|---|
| MNC9 no key | 31.4% / 39.7% | 95.5% (original 100%) | 4 actor-drop failures; no permission flips / no-key naming flip (FAIL) | 93.2% (MNC8 94.1% still top) | terse English 80.7% at 42.3% / 45.0% |
Not a new best. MNC3 stays current best. Details: round9/SCORES.md.

### MNC11 (bench-v1 only, 2026-11-09; local Qwen2.5-7B; self-built version, bench direct-use, no fresh round, no blind decode)
| Version | Bench saved o200k / cl100k | Bench direct-use | Instruction-safety (fresh) | Best baseline | Verdict |
|---|---|---|---|---|---|
| MNC11 | 30.4% / 40.9% (smallest MNC on bench) | 93.2% (206/221), = MNC9/MNC10, below MNC8 94.1% | not tested (no fresh round) | bench: LLMLingua-2 0.66 81.4% (reviewed) at 36.2% / 34.2% | not a new best; actor/prohibition-line fix worked (+2), thresholds-in-words and one-line steps failed; MNC8 stays top bench, MNC3 stays best |

### MNC12 (bench-v1 only, 2026-11-10; local Qwen2.5-7B; self-built version, bench direct-use, no fresh round, no blind decode)
| Version | Bench saved o200k / cl100k | Bench direct-use | Instruction-safety (fresh) | Best baseline | Verdict |
|---|---|---|---|---|---|
| MNC12 | 28.1% / 39.0% (+77 o200k vs MNC11) | 89.6% (198/221), below MNC8 94.1% and MNC11 93.2% (4 of the losses are a reader language-drift glitch; without them 91.4%) | not tested (no fresh round) | bench: LLMLingua-2 0.66 81.4% (reviewed) at 36.2% / 34.2% | FAILED, not a new best; boundary-line and prohibition-after-action rules both failed, "skip next rule" pointer lines caused a permission flip on a bench question; MNC8 stays top bench, MNC3 stays best |

### r10 MNC13 (runs 2026-11-11, written up 2026-11-12; local Qwen2.5-7B only; bench-v1 and fact-by-fact decode scoring pending)
| Version | Saved o200k / cl100k | Direct-use fresh (86 q) | Instruction-safety (direct use / blind decode) | Frozen bench-v1 direct-use | Best baseline |
|---|---|---|---|---|---|
| MNC13 no key | 24.6% / 35.8% | 87.2% (original 98.8%) | 6 failures: actor dropped on §1 Helen Park/controller and §5 Sophie Laurent/owner naming+identity (en+es); §5 ">20" threshold not applied, rule restated (en+es); fused "without X" prohibitions all held / no-key French decode turns "never copy Sophie" into "never believe her" (FAIL) | not run | fresh: terse English 80.2% at 38.3% / 40.6%; LLMLingua-2 0.66 72.1% at 34.4% / 32.3% |
Not a new best (loses to original text by 11.6 points; fails instruction-safety; two baselines save more tokens). MNC3 stays current best. Details: machine/round10/SCORES.md.

### MNC13 + MNC14 (bench-v1 only, 2026-11-13; local Qwen2.5-7B; self-built versions, bench direct-use, no fresh round, no blind decode)
| Version | Bench saved o200k / cl100k | Bench direct-use | Instruction-safety (fresh) | Best baseline | Verdict |
|---|---|---|---|---|---|
| MNC13 | 30.5% / 41.0% | 92.3% (204/221), below MNC8 94.1% | not tested (no fresh round) | bench: LLMLingua-2 0.66 81.4% at 36.2% / 34.2% | not a new best; fusion alone inconsistent (one fix, two prohibitions still dropped) |
| MNC14 | 30.1% / 40.7% | 93.7% (207/221), 1 question below MNC8 (within reader noise of ±2-3) | not tested (no fresh round) | bench: LLMLingua-2 0.66 81.4% at 36.2% / 34.2% | not a new best; first MNC with zero dropped prohibitions on bench; exactly-N boundary still fails; MNC8 stays top bench, MNC3 stays best |
Details: machine/bench/SCORES.md (MNC13 + MNC14).

### r11 MNC15 + aggressive MNC15x / MNC15xx (7B runs 2026-11-14, frontier runs and write-up 2026-11-15; FIRST ROUND WITH A STRONG READER)
Strong reader = one fresh no-context Grok Bot helper per method, one run each (noise not measured). Weak reader = local Qwen2.5-7B, one run.
| Version | Saved o200k / cl100k | Fresh direct-use, strong reader (94 q) | Fresh direct-use, 7B | Instruction-safety | Frozen bench-v1 | Best baseline (strong reader) |
|---|---|---|---|---|---|---|
| MNC15 + key | 21.8% / 32.8% (payload alone 33.8% / 42.9%) | 100% (original 100%) | 93.6% no key (original 96.8%) | strong: PASS 40/40 / 7B direct: FAIL (threshold flip ×2) / 7B no-key decode: FAIL ("more than 40" → "more than four") | not run | LLMLingua-2 0.66 83.0% at 34.6% |
| MNC15x no key (self-built after round results) | 38.9% / 47.1% | 97.9% | not run | strong: PASS 40/40 | not run | terse English 73.4% at 47.8% |
| MNC15xx no key (self-built after round results) | 43.8% / 51.4% | 97.9% | not run | strong: PASS 40/40 | not run | terse English 73.4% at 47.8% |
Not a new best yet (no bench-v1 score; MNC15x/xx encoder side is a self-test). Most promising result so far: ≥97.9% with 100% strong-reader safety at 38.9-43.8% savings, vs ≤83.0% for every baseline. MNC3 stays current best. Ready counter: 0/3. Details: machine/round11/SCORES.md.

### r12 MNC16x (bench) / MNC16xx (fresh), 2026-11-16 nightly; STRONG READER PRIMARY, 2 runs per MNC/original; 7B not run
| Version | Saved o200k / cl100k | Fresh direct-use, strong (106 q) | Bench-v1 direct-use, strong (221 q) | Instruction-safety | Best baseline (strong reader) |
|---|---|---|---|---|---|
| **MNC16xx / MNC16x** (no key) | fresh 45.4% / 51.8%; bench 43.5% / 51.4% | **100%, 100%** (original 100%, 100%) | **99.5%, 99.5%** (original 100%, 100%) | direct use PASS on every run (fresh 52/52, bench 110/110) / blind decode FAIL: 1 deadline distortion ("by 15:00" → "at 15:00", encoder dropped "by") | fresh: terse English (frontier-written) 100% at 35.4% / 43.3%; LLMLingua-2 0.5 84.9% at 51.0%. bench: LLMLingua-2 0.5 89.1% at 50.3% |
| MNC16 (no key) | fresh 37.7% / 45.0%; bench (moderate file) 34.2% / 43.3% | 100%, 100% | 99.5% | direct use PASS | – |
| MNC14 (reference) | bench 30.1% / 40.7% | – | 100% | direct use PASS | – |
**NEW BEST (strong-reader track): MNC16x / MNC16xx.** With the strong reader it wins on both the frozen and fresh sets under the round rules. It matches the original within 1 bench question, keeps 100% direct-use safety, and has the highest savings of any method at ≥99% accuracy. Caveats: on fresh passages a well-written terse English baseline is also 100%, so MNC's edge there is about +10 points of savings, not accuracy. Two runs, one reader family; bench-v1 is at ceiling for this reader. MNC3 stays the recorded best for the weak-reader track (kept unchanged above). Ready counter: 0/3 (blind decode failed). Details: machine/round12/SCORES.md.

### r13 MNC17 / MNC17x / MNC17xx (2026-11-17 nightly; STRONG READER PRIMARY; 7B and bench-v1 not run)
| Version | Saved o200k / cl100k | Fresh direct-use, strong (114 q) | Instruction-safety | Bench-v1 | Best baseline (strong reader) |
|---|---|---|---|---|---|
| **MNC17xx** (no key) | 46.9% / 52.5% | 100%, 100% (original 100%) | direct use PASS 68/68 ×2 / blind decode ×2 FAIL: "tell them to call 911" → "they should call 911" (action lost); "overview of returns" → "returns" (encoder dropped "overview") | not run | terse English (frontier) 100% at 34.9% / 43.1%; LLMLingua-2 0.5 71.9% at 59.8% (87.2% at 51.3% excluding its empty Japanese section) |
| MNC17x (no key) | 45.3% / 51.4% | 100% | direct use PASS | not run | – |
| MNC17 (no key) | 39.1% / 46.2% | 100% | direct use PASS | not run | – |
Not a new best: no bench-v1 run and blind decode failed safety. MNC17xx is slightly above MNC16xx on savings (+1.5 points) at equal strong-reader accuracy. The fresh questions are at ceiling for the strong reader (original, terse and every MNC17 version scored 100%), so harder questions are needed. MNC16x/xx stay the strong-reader best; MNC3 stays the weak-reader best. Ready counter: 0/3. Details: machine/round13/SCORES.md.

### Sprint 2026-11-17 (evening): MNC18 candidate frozen, bench-v2 built, rounds 14-17 staged (staging entry; the 'pending' cells are SUPERSEDED by the r14/r15 results entry below)
| Version | Saved o200k / cl100k (bench-v2) | Strong-reader direct use | Instruction-safety | Blind decode | Best baseline |
|---|---|---|---|---|---|
| MNC18 (candidate: R1 deadline words, R2 `tell X:`, R3 object nouns, R4 lint) | 32.7% / 41.8% (r15 34.0% / 42.1%; r16 27.8% / 35.6%; r17 26.6% / 35.6%) | **pending** (jobs staged, ../SPRINT-DISPATCH.md) | pending | pending | LLMLingua-2 0.66 35.7% / 35.2%; 0.5 57.0% / 57.8% (49.3% excl. the truncated ja/zh sections); accuracy pending |
| MNC18z (curve only) | 38.7% / 46.9% | pending | pending | – | – |
No result and no new best. The executor couldn't launch blind no-context readers, so every primary run is staged, not run. Weak reader (7B, ×1, raw) on bench-v2: original 52.8%, MNC18 70.8%. Both runs are dominated by the 7B shifting answers onto wrong question IDs on the 89-question prompt, so they're not evidence either way. Ready counter: **0/3** (unchanged). MNC16x/xx stay the strong-reader best. Details: machine/round14/, machine/bench-v2/README.md.

### r14 (bench-v2) + r15 (fresh en/pt/ko/pl), MNC18 / MNC18z — strong-reader runs done 2026-11-17 ~19:00-19:15 CT (2 runs per MNC/original on bench-v2; 1 run per baseline)
| Version | Saved o200k / cl100k | bench-v2 direct use, strong (89 q) | r15 fresh direct use, strong (42 q) | Instruction-safety | Best baseline (strong reader, bench-v2) |
|---|---|---|---|---|---|
| **MNC18z** (no key) | bench-v2 **38.7% / 46.9%** | **100%, 100%** (original 100%, 100%) | not encoded | direct use PASS 61/61 ×2; decode not run | terse English 95.5% at 29.6%; LLMLingua-2 0.66 79.8% at 35.7%; 0.5 61.8% at 57.0% |
| MNC18 (no key) | bench-v2 32.7% / 41.8%; r15 34.0% / 42.1% | 100%, 100% | 97.6%, 100% (original 100%) | bench-v2 direct PASS ×2, decode FAIL ×2 (1 actor shift: invoice "customer submits" → "you provide"); r15 direct FAIL on 1 run (`<24h before` threshold flip), decode PASS ×2 | same |
Not a new best (no bench-v1 regression run for MNC18; bench-v2 has no earlier versions to beat). First harder benchmark on which every MNC run ties the original at 100% while every baseline drops (terse −4.5, LLMLingua-2 −20/−38 points). MNC16x/xx stay the strong-reader best; MNC3 the weak-reader best. Ready counter: **0/3** (r14 decode actor shift, r15 threshold flip). Round 16 not run: its MNC18 encoding is superseded by MNC19. Details: machine/round14/SCORES.md, machine/round15/SCORES.md.

### MNC19 candidate (frozen 2026-11-17 19:06 CT) — staged, NOT yet read by any reader
| Version | Saved o200k / cl100k | Status |
|---|---|---|
| MNC19 (MNC18 R1-R4 + MNC18z structure + R5 time/age comparisons in words + R6 actor on every obligation) | bench-v2 38.0% / 46.3%; r16 26.6% / 34.6%; r17 24.6% / 34.0%; r18 24.4% / 31.4% | dispatch jobs in SPRINT-DISPATCH-MNC19.md |
| MNC19x (curve only: merged lines) | bench-v2 39.0% / 47.2% | staged |
Built after seeing r14/r15, so it is tuned on them. The counter for MNC19 can only use rounds no reader had seen: r16 and r17 (re-encoded, but their questions already existed, so those encodings are not question-blind) and r18 (fully fresh: encoded before the questions were written). Encoder finding: on dense safety text, structural merging tops out near 38-39% o200k (MNC19x +1.0 point over MNC19). The remaining tokens are content, not filler.

### r16 / r17 / r18 + bench-v2, MNC19 — strong-reader runs 2026-11-17 ~19:00-19:13 CT, scored ~19:25 CT
| Version | Saved o200k / cl100k | r16 (40 q) | r17 (36 q) | r18 (38 q, fully blind) | bench-v2 (89 q) | Instruction-safety |
|---|---|---|---|---|---|---|
| **MNC19** (no key) | r16 26.6% / 34.6%; r17 24.6% / 34.0%; r18 24.4% / 31.4%; bench-v2 38.0% / 46.3% | 100%, 100% (original 100%) | 100%, 100% (original 100%) | 97.4%, 97.4% (original 97.4%) | 100%, 100% (original 100% ×2) | **PASS in r16, r17, r18 and bench-v2**: S 100% on every run; blind decode ×2 with 0 safety distortions in all four sets |
| MNC19x (curve) | bench-v2 39.0% / 47.2% | – | – | – | 100%, 100% | direct use PASS |
Bench-v2 baselines (strong reader): terse English 95.5% at 29.6%; LLMLingua-2 0.66 79.8% at 35.7%; 0.5 61.8% at 57.0%.
**Ready counter (MNC19): 3/3 under the round rule** (r16, r17, r18 consecutive PASS). But r16 and r17 are labelled *encoding not question-blind*; **strictly fully blind: 1/3** (r18 only). Other caveats: the decode judge is the encoder (not blind); one reader family; isolation by instruction only; the same agent wrote passages, facts, encodings and questions; one original-text run per fresh round. Not claimed as a new best yet: no bench-v1 regression run for MNC19. MNC18 r14/r15 failures (actor loss, `<24h` flip) did not recur. Savings on these dense instruction-heavy rounds are lower (24-27% o200k) than on earlier, lighter rounds.

## 2026-11-17 ~19:22 CT — rounds 19/20 STAGED (fully blind, independent author) — no results yet
| round | facts (S) | lint | o200k saved | cl100k saved | questions (S) | status |
|---|---|---|---|---|---|---|
| r19 | 40 (36) | 40/40 | 26.6% | 37.7% | 32 (26) | readers not run |
| r20 | 42 (38) | 42/42 | 27.6% | 35.6% | 32 (28) | readers not run |
Savings are lower than on my own rounds (~38–46%): the independent author's prose is already denser. Not tuned after seeing questions.

### r19 / r20 (fully blind, independent author), MNC19 — readers run 2026-11-17 ~19:22 CT, independent judge + scoring 2026-11-18 ~01:15 CT
| round | Saved o200k / cl100k | MNC19 direct use, strong (2 runs) | original | Blind decode (independent judge) | Instruction-safety |
|---|---|---|---|---|---|
| r19 | 26.6% / 37.7% | 100%, 100% (S 26/26 ×2) | 100% | 0 S distortions ×2 | **PASS** |
| r20 | 27.6% / 35.6% | 96.9%, 100% (S 27/28, 28/28) | 100% | 0 S distortions ×2 | **FAIL (strict)**: 1 run omitted the emergency lifeguard number; no negation/actor/deadline flip |
Baselines and 7B not run on r19/r20. Not a new best (no bench-v1 run for MNC19). Ready counter, strictly fully blind: r18 PASS, r19 PASS, r20 FAIL → **0/3**. MNC16x/xx stay the strong-reader best; MNC3 the weak-reader best. Details: machine/round19/, machine/round20/SCORES.md.


### r21 (fully blind, independent author), MNC20 = MNC19 + R7 — run and scored 2026-11-18 07:00-07:45 CT (strong reader = fresh no-context frontier helpers; independent decode judge)
| Text | Saved o200k / cl100k | Direct use, strong (S) | Blind decode (judge) | Instruction-safety |
|---|---|---|---|---|
| MNC20 (no key) | 26.8% / 40.4% | 100%, 100% (S 25/25 ×2) | 1 S distortion ×2 (ambiguous derived amount), 3 benign inventions ×2 | **FAIL (strict)** — direct use PASS, decode FAIL |
| MNC20x (curve) | 41.3% / 52.1% | 97.4% ×2 (S 24/25 ×2) | not run | FAIL (cancellation fee 150 vs 300 TL) |
| original | 0 | 100% | – | – |
| terse English | 36.5% / 48.7% | 100% (S 25/25) ×1 | – | – |
| summarize | 20.4% / 25.7% | 100% ×1 | – | – |
| LLMLingua-2 0.66 / 0.5 | 32.5% / 47.9% (o200k) | 94.9% / 76.9% ×1 | – | – |
Bench-v1 regression MNC20 ×1 (not blind): 94.8% raw, S 56/56, 24.3% / 34.8% saved; no original control on the converted set. 7B not run.
Not a new best: terse English matches accuracy and saves more. Ready counter (fully blind): **0/3**. MNC16x/xx stay the strong-reader best; MNC3 the weak-reader best. Details: machine/round21/SCORES.md.


### r22 (fully blind, independent author), MNC21 = MNC20 + R8 + R9 — run and scored 2026-11-18 12:54-13:05 CT (strong reader = fresh no-context frontier helpers; independent decode judge)
| Text | Saved o200k / cl100k | Direct use, strong (S) | Blind decode (judge) | Instruction-safety |
|---|---|---|---|---|
| MNC21 (no key) | 32.1% / 41.0% | 100%, 100% (S 26/26 ×2) | A: 1 low-severity S distortion ("a mechanic" → "the mechanic"); B clean; 0 inventions | **FAIL (strict)** — direct use PASS, decode A FAIL |
| MNC21x (aggressive) | 37.6% / 45.6% | 100%, 100% (S 26/26 ×2) | not run | direct use PASS |
| original | 0 | 100% | – | – |
| terse English | 40.2% / 47.9% | 100% ×2 (1 F regex override) | – | – |
| summarize | 25.3% / 27.3% | 100% ×1 | – | – |
| LLMLingua-2 0.66 / 0.5 | 33.6% / 49.4% (o200k) | 82.1% / 71.8% ×1 | – | – |
Bench-v1: original-text control on the converted set = 97.0% (S 55/56) vs MNC20 94.8% (S 56/56). 7B pending at write-up.
Not a new best: terse English matches accuracy and still saves more (gap 2.6 points, down from 9.7 in r21). Ready counter (fully blind): **0/3**. MNC16x/xx stay the strong-reader best; MNC3 the weak-reader best. Details: machine/round22/SCORES.md.


### r23 (fully blind, independent author), MNC22 = MNC21x + R10 + R11 — run and scored 2026-11-18 19:00-19:15 CT (strong reader = fresh no-context frontier helpers; independent decode judge)
| Text | Saved o200k / cl100k | Direct use, strong (S) | Blind decode (judge) | Instruction-safety |
|---|---|---|---|---|
| MNC22 (no key) | 35.0% / 42.4% | 100%, 100% (S 27/27 ×2) | not run | direct use PASS |
| MNC22x (aggressive) | 36.3% / 43.5% | 100%, 100% (S 27/27 ×2) | A clean; B: 1 S distortion (approval threshold scope widened to "any order"); encoder-added derived figure flagged in both | **FAIL (strict)** — direct use PASS, decode B FAIL |
| original | 0 | 100% | – | – |
| terse English | 39.2% / 46.8% | 100% ×2 | – | – |
| summarize | 22.2% / 24.0% | 100% ×1 | – | – |
| LLMLingua-2 0.66 / 0.5 | 42.5% / 53.5% (o200k) | 70.0% / 55.0% ×1 (Japanese section collapsed) | – | – |
Bench-v1 not run. 7B pending at write-up.
Not a new best: terse English matches accuracy and still saves more (gap 2.9 points). Ready counter (fully blind): **0/3**. MNC16x/xx stay the strong-reader best; MNC3 the weak-reader best. Details: machine/round23/SCORES.md.


### r24 (fully blind, independent author), MNC23 = MNC22x + R12 + R8b + R13 — run and scored 2026-11-19 01:00-01:15 CT (strong reader = fresh no-context frontier helpers; independent decode judge)
| Text | Saved o200k / cl100k | Direct use, strong (S) | Blind decode (judge) | Instruction-safety |
|---|---|---|---|---|
| MNC23 (no key) | 31.7% / 45.1% | 100%, 100% (S 25/25 ×2; 1 regex false negative reviewed) | A and B: 2 S distortions each (911 instruction moved from customer to assistant; after-hours contact rule widened), 1 F distortion + 1 F loss, 0 added | **FAIL (strict)** — direct use PASS, decode FAIL |
| MNC23x | 33.1% / 46.0% | 100%, 100% (S 25/25 ×2; 1 regex false negative reviewed) | not run | direct use PASS |
| **MNC23xx** (most aggressive) | **39.6% / 51.2%** | 100%, 100% (S 25/25 ×2, raw) | not run | direct use PASS |
| original | 0 | 100% | – | – |
| terse English | 35.9% / 49.7% | 97.5% ×2 (S 24/25 ×2: permission flipped) | – | – |
| summarize | 24.1% / 28.2% | 100% ×1 | – | – |
| LLMLingua-2 0.66 / 0.5 | 32.2% / 47.0% (o200k) | 97.5% / 92.5% ×1 | – | – |
Bench-v1 not run. 7B pending at write-up.
Not a formal new best (no bench-v1 run; strict decode FAIL). First fresh blind round where an MNC form beats terse English on both savings and accuracy with the strong reader (+3.7 points of savings, +1 safety question). LLMLingua-2 0.5 still saves more, at lower accuracy. Ready counter (fully blind): **0/3**. MNC16x/xx stay the strong-reader best; MNC3 the weak-reader best. Details: machine/round24/SCORES.md.

### r25 (fully blind, independent author), MNC24 = MNC23xx + R14 + R15 + R16 + R17 — run and scored 2026-11-19 06:55-07:05 CT (strong reader = fresh no-context frontier helpers; independent decode judge)
| Text | Saved o200k / cl100k | Direct use, strong (S) | Blind decode (judge) | Instruction-safety |
|---|---|---|---|---|
| MNC24 (no key) | 30.3% / 39.4% | 100%, 100% (S 23/23 ×2; 2 CJK-regex false negatives reviewed per run) | A: 3 low-severity S items (assistant role decoded as "You are working for"), 1 F loss; B: 0 S, 1 F loss; 0 added | **FAIL (strict)** — direct use PASS, decode A FAIL, B clean |
| **MNC24x** (aggressive) | **35.9% / 44.0%** | 100%, 100% (S 23/23 ×2; same reviewed false negatives) | not run | direct use PASS |
| original | 0 | 100% | – | – |
| terse English | 34.1% / 43.0% | 94.9% ×2 (qualifier scope flipped both runs) | – | – |
| summarize | 16.1% / 19.1% | 100% ×1 | – | – |
| LLMLingua-2 0.66 / 0.5 | 34.8% / 50.0% (o200k) | 74.4% / 66.7% ×1 | – | – |
Bench-v1 (134-q, strong, raw, not blind): MNC24 97.0% / 95.5% at 44.6% / 51.9%; MNC16x 97.0% ×2 at 44.8% / 52.5%; original 97.0% / 97.8%. Tie with MNC16x inside noise.
Not a new best: beats every baseline on the fresh blind set, but only ties MNC16x on the frozen bench. Ready counter (fully blind): **0/3**. MNC16x/xx stay the strong-reader best; MNC3 the weak-reader best. Details: machine/round25/SCORES.md.

### r26 (fully blind, independent author), MNC25 = MNC24 + R18 + R16b + R19 — run and scored 2026-11-19 12:59-13:10 CT (strong reader = fresh no-context frontier helpers; independent decode judge)
| Text | Saved o200k / cl100k | Direct use, strong (S), reviewed | Blind decode (judge, 119 facts) | Instruction-safety |
|---|---|---|---|---|
| MNC25 (main, no key) | 31.6% / 42.7% | 100%, 100% (S 25/25 ×2) | A and B: 119/119 kept, 0 added | **PASS** |
| MNC25x (aggressive) | 37.0% / 47.1% | 97.4%, 100% (S 24/25, 25/25: run 1 invented an approver) | not run | FAIL (probe only) |
| original | 0 | 100% | – | – |
| terse English | 34.6% / 45.5% | 100% ×2 | – | – |
| summarize | 18.2% / 20.8% | 100% ×1 | – | – |
| LLMLingua-2 0.66 / 0.5 | 36.6% / 49.3% (o200k) | 87.2% / 74.4% ×1 | – | – |
One shared review: the gold for §1.q2 named an approver the original does not name; "approver not stated" answers were reviewed correct for every text (details in round26/SCORES.md). Bench-v1 not run (at ceiling). 7B pending at write-up.
Not a new best: MNC25 is safety-clean, but terse English matches its accuracy at 3 points more savings. Ready counter (fully blind, main form): **1/3**. MNC16x/xx stay the strong-reader best; MNC3 the weak-reader best. Details: machine/round26/SCORES.md.

### r27 (fully blind, independent author), MNC26 = MNC25x form as main + R20 (unnamed-approver marker) — run and scored 2026-11-19 18:55-19:05 CT (strong reader = fresh no-context frontier helpers; independent decode judge)
| Text | Saved o200k / cl100k | Direct use, strong (S), reviewed | Blind decode (judge, 142 facts) | Instruction-safety |
|---|---|---|---|---|
| MNC26 (main, no key) | 36.9% / 46.8% | 100% ×2 (S 28/28 ×2) | A: 0 S errors, 6 F (check times read as a range); B: 142/142 | **PASS** |
| MNC26x (aggressive) | 37.6% / 47.3% | 100% ×2 (S 28/28 ×2) | not run | – |
| original | 0 | 97.5% (S 27/28: invented approver) | – | – |
| terse English | 39.2% / 49.0% | 100%, 97.5% (run 2 invented approver) | – | – |
| summarize | 23.6% / 26.9% | 97.5% ×1 (invented approver) | – | – |
| LLMLingua-2 0.66 / 0.5 | 32.2% / 47.3% (o200k) | 95.0% / 72.5% ×1 | – | – |
Bench-v1 not run (at ceiling). 7B pending at write-up.
Not a formal new best: MNC26 is the only form with S 100% in every run and beat the original text, but terse English saves 2.3 points more. Ready counter (fully blind, main form): **2/3**. MNC16x/xx stay the strong-reader best; MNC3 the weak-reader best. Details: machine/round27/SCORES.md.
(Counter correction: under the one-frozen-version rule r27 counts as MNC26 1/3.)


### r28 (fully blind, independent author), MNC26 frozen main (RULES.md sha1 6c1bc095, unchanged) + MNC26x probe (R21 + aggressive) — run and scored 2026-11-20 00:56-01:10 CT (strong reader = fresh no-context frontier helpers; independent decode judge)
| Text | Saved o200k / cl100k | Direct use, strong (S), reviewed | Blind decode (judge, 110 facts) | Instruction-safety |
|---|---|---|---|---|
| MNC26 (main, frozen, no key) | 34.8% / 42.6% | 100% ×2 (S 25/25 ×2) | A and B: 0 S errors; 3 F each (check times read as a range) | **PASS** |
| MNC26x (R21 + aggressive) | 39.9% / 47.0% | 97.4%, 100% (S 24/25: run 1 invented an approver) | not run | FAIL (probe only) |
| original | 0 | 100% | – | – |
| terse English | 34.5% / 42.3% | 100% ×2 | – | – |
| summarize | 15.7% / 17.2% | 100% ×1 (1 regex false negative reviewed) | – | – |
| LLMLingua-2 0.66 / 0.5 | 34.2% / 47.9% (o200k) | 79.5% / 69.2% ×1 | – | – |
Bench-v1 not run (at ceiling). Questions were at ceiling for every faithful text.
Not a new best: MNC26 main ties terse English (34.8% vs 34.5%, both 100%). MNC26x saves the most of any text above 95% accuracy, but slipped once on safety. Counter correction for r27: under the one-frozen-version rule r27 was MNC26 1/3, not 2/3. Ready counter now: **MNC26: 2/3**. Details: machine/round28/SCORES.md.


### r29 (fully blind, independent author), MNC26 frozen main (RULES.md sha1 6c1bc095, unchanged) + MNC26x' probe (R21 + R22 + aggressive) — run and scored 2026-11-20 06:55-07:30 CT (strong reader = fresh no-context frontier helpers; independent decode judge)
| Text | Saved o200k / cl100k | Direct use, strong (S) | Blind decode (judge, 90 facts) | Instruction-safety |
|---|---|---|---|---|
| MNC26 (main, frozen, no key) | 29.0% / 38.6% | 100% ×2 (S 23/23 ×2) | A and B: 0 S errors, 0 F errors; 1 encoder-added year (F) | **PASS** |
| MNC26x' (R21 + R22 + aggressive) | 36.0% / 44.1% | 100% ×2 (S 23/23 ×2) | not run | – (probe) |
| original | 0 | 100% | – | – |
| terse English | 35.1% / 44.7% | 100% ×2 | – | – |
| summarize | 16.4% / 18.5% | 100% ×1 | – | – |
| LLMLingua-2 0.66 / 0.5 | 46.2% / 58.3% (o200k) | 74.4% / 64.1% ×1 (Japanese section lost) | – | – |
Bench-v1 not run (at ceiling). 7B pending at write-up. Questions at ceiling for every faithful text.
Not a new best: terse English saves 6.1 points more than MNC26 main at equal accuracy; MNC26x' only ties terse. Ready counter: **MNC26: 3/3** — MNC26 meets the ready-for-live-instructions bar (3 consecutive fully blind rounds, 100% instruction-safety, strong reader; one reader family, ceiling question sets). Details: machine/round29/SCORES.md.


### r30 (fully blind, independent author, harder: distractor rules), MNC27 promoted to main (MNC26x' + R23 + exception lines; counter restarted) + MNC26 ready reference — run and scored 2026-11-20 13:12-13:45 CT (strong reader = fresh no-context frontier helpers; independent decode judge)
| Text | Saved o200k / cl100k | Direct use, strong (S) | Blind decode (judge, 133 facts) | Instruction-safety |
|---|---|---|---|---|
| MNC27 (new main, no key) | 36.6% / 49.7% | 100% ×2 (S 28/28 ×2) | A and B: 2 S distortions each (encoder-caused, everyday Korean §2: dropped "must", narrowed "complaints or inquiries"); instruction sections 0 S errors | **FAIL** (strict gate) |
| MNC26 (ready reference, frozen) | 31.5% / 45.7% | 100% ×2 (S 28/28 ×2) | not run | – (not counted) |
| original | 0 | 100% | – | – |
| terse English | 28.7% / 32.4% | 100% ×2 | – | – |
| summarize | 30.6% / 34.0% | 100% ×1 | – | – |
| LLMLingua-2 0.66 / 0.5 | 34.3% / 49.3% (o200k) | 97.4% / 92.1% ×1 (0.5 failed a safety boundary) | – | – |
One shared regex fix (§1.q9, all texts). 7B (3 runs): MNC26 63-68%, MNC27 50-58%, original 60-63%. Bench-v1 not run. Questions at ceiling for faithful texts.
Not a formal new best (bench-v1 not run, decode gate failed), but MNC27 saved the most of any text at 100% this round: +7.9 points over terse English, +6.0 over summarize (o200k). Ready counter: **MNC27: 0/3** (MNC26 keeps its r27-r29 3/3). Details: machine/round30/SCORES.md.



### r31 (fully blind, independent author; en/zh/it/pl), MNC28 promoted to main (MNC27 + R24; RULES sha1 f70a3563; counter restarted) + MNC28x probe — run and scored 2026-11-21 01:16-~02:00 CT (strong reader = fresh no-context frontier helpers; independent decode judge)
| Text | Saved o200k / cl100k | Direct use, strong (S) | Blind decode (judge, 205 facts) | Instruction-safety |
|---|---|---|---|---|
| MNC28 (new main, no key) | 28.1% / 30.8% | 100% ×2 (S 32/32 ×2) | A and B: 205/205 kept, 0 errors | **PASS** |
| MNC28x (aggressive probe) | 38.5% / 41.1% | 100% ×2 (S 32/32 ×2) | not run | – (probe) |
| original | 0 | 100% | – | – |
| terse English | 37.6% / 44.5% | 100% ×2 | – | – |
| summarize | 20.8% / 23.1% | 100% ×1 | – | – |
| LLMLingua-2 0.66 / 0.5 | 33.2% / 48.2% (o200k) | 87.2% / 69.2% ×1 (both lost emergency steps; 0.5 invented an approver) | – | – |
7B not run (RAM). Bench-v1 not run. Questions at ceiling for faithful texts.
Not a new best: terse English saved 9.5 points more than MNC28 main at equal accuracy; MNC28x ties terse (+0.9 o200k, −3.4 cl100k). Ready counter: **MNC28: 1/3** (MNC26 keeps 3/3). Details: machine/round31/SCORES.md.


### r32 (fully blind, independent author; en/ja/es/tr), MNC28 main frozen (RULES sha1 f70a3563) + MNC28x probe — run and scored 2026-11-21 13:18-~13:50 CT (strong reader = fresh no-context frontier helpers; independent decode judge)
| Text | Saved o200k / cl100k | Direct use, strong (S) | Blind decode (judge, 147 facts) | Instruction-safety |
|---|---|---|---|---|
| MNC28 (main, no key) | 24.7% / 31.5% | 100% ×2 (S 27/27 ×2) | A and B: 147/147 kept, 0 errors | **PASS** |
| MNC28x (probe; Japanese §2 as English slots) | 36.8% / 47.5% | 100% ×2 (S 27/27 ×2) | not run | – (probe) |
| original | 0 | 100% (2 scorer overrides; 95% strict) | – | – |
| terse English | 39.0% / 49.3% | 100% ×2 | – | – |
| summarize | 26.0% / 28.0% | 100% ×1 | – | – |
| LLMLingua-2 0.66 / 0.5 | 43.7% / 54.8% (o200k) | 77.5% / 70.0% ×1 (0.66 lost Japanese section; 0.5 invented approvers, dropped an emergency step) | – | – |
7B (3 runs): MNC28 45-57.5%, MNC28x 50-52.5%, original 45-50% (ties). Bench-v1 not run. Questions at ceiling for faithful texts.
Not a new best: terse English saved 14.3 points more than MNC28 main at equal accuracy; MNC28x close behind terse (−2.2 o200k). Ready counter: **MNC28: 2/3**. Details: machine/round32/SCORES.md.


### r33 (fully blind, independent author; en/ko/fr/vi), MNC28 main frozen (RULES sha1 f70a3563) + MNC28x probe — run and scored 2026-11-22 01:17-~02:00 CT (strong reader = fresh no-context frontier helpers; independent decode judge)
| Text | Saved o200k / cl100k | Direct use, strong (S) | Blind decode (judge, 138 facts) | Instruction-safety |
|---|---|---|---|---|
| MNC28 (main, no key) | 22.3% / 32.7% | 100% ×2 (S 27/27 ×2) | A 138/138; B 137/138 (1 F decoder-caused distortion), 0 S errors | **PASS** |
| MNC28x (probe; all non-English sections as English slots) | 41.6% / 55.0% | 100% ×2 (S 27/27 ×2) | not run | – (probe) |
| original | 0 | 100% (after one shared regex fix; 97.4% before) | – | – |
| terse English | 42.4% / 55.6% | 100% ×2 | – | – |
| summarize | 31.0% / 33.4% | 100% ×1 | – | – |
| LLMLingua-2 0.66 / 0.5 | 34.2% / 48.7% (o200k) | 92.3% / 84.6% ×1 (both named an unstated approver; 0.5 flipped a permission and dropped an emergency step) | – | – |
7B (3 runs): MNC28 66.7-76.9%, MNC28x 51.3-66.7%, original 53.8% ×3. Bench-v1 not run. Questions at ceiling for faithful texts.
Not a new best: terse English saved 20.1 points more than MNC28 main at equal accuracy; MNC28x ties terse (−0.8 o200k, −0.6 cl100k). Ready counter: **MNC28: 3/3** — meets the ready-for-live-instructions bar (rounds 31-33). Details: machine/round33/SCORES.md.


### r34 (fully blind, independent author; en/zh/de/id), MNC28 main frozen (RULES sha1 f70a3563) + MNC28x probe — run and scored 2026-11-22 13:18-~13:50 CT (strong reader = fresh no-context frontier helpers; independent decode judge)
| Text | Saved o200k / cl100k | Direct use, strong (S) | Blind decode (judge, 170 facts) | Instruction-safety |
|---|---|---|---|---|
| MNC28 (main, no key) | 16.8% / 23.4% | 100% ×2 (S 28/28 ×2) | A and B: 170/170 kept, 0 errors | **PASS** |
| MNC28x (probe; one approver line per person, no repeated names) | 33.1% / 41.7% | 97.5% ×2 (S 27/28 ×2: Saturday over-limit approver lost) | 167/170; 1 S distortion (approver merge widened to "discounts"), 2 F losses | FAIL (probe) |
| original | 0 | 100% (after 3 shared scorer fixes) | – | – |
| terse English | 36.3% / 44.4% | 100% ×2 | – | – |
| summarize | 21.4% / 23.1% | 100% ×1 | – | – |
| LLMLingua-2 0.66 / 0.5 | 33.1% / 47.0% (o200k) | 82.5% / 62.5% ×1 (lost Chinese facts; 0.5 flipped a prohibition and named wrong approvers) | – | – |
7B (3 runs): MNC28 62.5-65.0%, original 50.0-52.5% (MNC28 above the original's range); MNC28x 57.5% on its one complete run (2 runs truncated). Bench-v1 not run. Questions at ceiling for faithful texts.
Not a new best: terse English saved 19.5 points more than MNC28 main at equal accuracy; MNC28x's new approver merges caused safety errors. Ready counter: **MNC28: 4 consecutive blind passes** (r31-r34; 3/3 bar met since r33). Details: machine/round34/SCORES.md.


### r35 (fully blind, independent author; en/ja/es/ar), MNC28 main frozen (RULES sha1 f70a3563) + MNC28x probe — run and scored 2026-11-27 01:14-~01:50 CT (strong reader = fresh no-context frontier helpers; independent decode judge)
| Text | Saved o200k / cl100k | Direct use, strong (S) | Blind decode (judge, 193 facts) | Instruction-safety |
|---|---|---|---|---|
| MNC28 (main, no key) | 20.1% / 40.8% | 100% ×2 (S 27/27 ×2) | A and B: 193/193 kept, 0 errors | **PASS** |
| MNC28x (probe; approver merge reverted, terse-style wording) | 40.1% / 57.9% | 100% ×2 (S 27/27 ×2) | 191/193; 1 S distortion (role negation "not THE shaper" widened to "not a shaper"), 1 F distortion (same-day delivery → same-day sharpening) | FAIL (probe) |
| original | 0 | 100% (after 1 shared scorer fix) | – | – |
| terse English | 37.7% / 56.6% | 100% ×2 | – | – |
| summarize | 23.3% / 25.8% | 100% ×1 | – | – |
| LLMLingua-2 0.66 / 0.5 | 40.0% / 52.7% (o200k) | 75.0% / 75.0% ×1 (lost most Japanese facts; both named an unstated approver) | – | – |
7B (3 runs): MNC28 65.0% ×3, original 62.5% ×3, MNC28x 62.5-65.0% (1-question margins; effectively ties). Bench-v1 not run. Questions at ceiling for faithful texts.
Not a formal new best: MNC28x saved more than terse English at equal accuracy (+2.4 o200k, +1.3 cl100k) but failed the strict decode gate; terse English saved 17.6 points more than MNC28 main. Ready counter: **MNC28: 5 consecutive blind passes** (r31-r35; 3/3 bar met since r33). Details: machine/round35/SCORES.md.


### r36 (fully blind, independent author; en/ko/pt/hi), MNC28 main frozen (RULES sha1 f70a3563) + MNC28x probe — run and scored 2026-11-28 00:56-~01:30 CT (strong reader = fresh no-context frontier helpers; independent decode judge)
| Text | Saved o200k / cl100k | Direct use, strong (S) | Blind decode (judge, 213 facts) | Instruction-safety |
|---|---|---|---|---|
| MNC28 (main, no key) | 21.6% / 48.5% | 100% ×2 (S 24/24 ×2) | A and B: 212/213 kept, 0 S errors (1 decoder-side F distortion) | **PASS** |
| MNC28x (probe; THE/NOT THE role negations, definitions keep their noun) | 39.6% / 63.1% | 100% ×2 (S 24/24 ×2, after shared "2F" fix) | 209/213 ×2; 0 S errors; 3 F losses ("small") + 1 modality change (should start → must start) | direct use pass; decode not clean (probe) |
| original | 0 | 100% | – | – |
| terse English | 42.1% / 65.6% | 100% ×2 (after shared "2F" fix) | – | – |
| summarize | 27.2% / 31.6% | 100% ×1 | – | – |
| LLMLingua-2 0.66 / 0.5 | 34.6% / 49.6% (o200k) | 92.1% / 89.5% ×1 (lost Korean seed limit, flipped the Korean date-scope test; 0.5 gave an ambiguous approver "Mehra") | – | – |
7B: pending (queue still running at write-up). Bench-v1 not run. Questions at ceiling for faithful texts.
Not a new best: terse English saved 2.5 points more than MNC28x and 20.5 points more than MNC28 main at equal accuracy. r35's x slips fixed; new x slips are F-level. Ready counter: **MNC28: 6 consecutive blind passes** (r31-r36; 3/3 bar met since r33). Details: machine/round36/SCORES.md.


### r37 (fully blind, independent author; en/zh/fr/vi, 59 q), MNC28 main frozen (RULES sha1 f70a3563) + MNC28x probe (shared §0 slot-schema key) — run and scored 2026-11-28 03:52-~04:30 CT (strong reader = fresh no-context frontier helpers; independent decode judge)
| Text | Saved o200k / cl100k | Direct use, strong (S) | Blind decode (judge, 189 facts) | Instruction-safety |
|---|---|---|---|---|
| MNC28 (main, no key) | 16.9% / 29.7% | 100% ×2 (S 43/43 ×2) | A and B: 189/189 kept, 0 errors | **PASS** |
| MNC28x (probe; shared §0 schema key) | 29.1% / 43.5% | 100% ×2 (S 43/43 ×2) | 188/189 ×2; 1 S distortion (permission trigger lost its actor "customer") | direct use pass; decode FAIL (probe) |
| original | 0 | 100% | – | – |
| terse English | 35.9% / 48.4% | 98.3% ×2 (S 42/43 ×2: Chinese date qualifier attached to both nouns) | – | – |
| summarize | 27.2% / 30.0% | 100% ×1 | – | – |
| LLMLingua-2 0.66 / 0.5 | 35.8% / 50.0% (o200k) | 88.1% / 81.4% ×1 (lost Chinese scope facts, named an unstated approver) | – | – |
7B: r37 pending (queue running at write-up). r36 7B scored: MNC28 81.6% ×3 vs original 63.2-68.4%, MNC28x 63.2-71.1% (tie with original). Bench-v1 not run.
Not a new best: terse English saved 6.8 points more than MNC28x (but slipped one safety question ×2); MNC28x failed the decode gate. Ready counter: **MNC28: 7 consecutive blind passes** (r31-r37; 3/3 bar met since r33). Details: machine/round37/SCORES.md.




### r38 (fully blind, independent author; en/ja/de/th, 60 q), MNC28 main frozen (RULES sha1 f70a3563) + MNC28x probe ("terse + safety rails", no key) — run and scored 2026-11-28 06:54-~07:30 CT (strong reader = fresh no-context frontier helpers; independent decode judge)
| Text | Saved o200k / cl100k | Direct use, strong (S) | Blind decode (judge, 224 facts) | Instruction-safety |
|---|---|---|---|---|
| MNC28 (main, no key) | 14.4% / 38.0% | 98.3% ×2 (S 44/44 ×2; 1 F scope miss ×2) | 222/224 ×2; 1 S distortion ×2 (Dec-20 qualifier widened from vests to all equipment, encoder-caused) | **FAIL** (strict decode gate) |
| MNC28x (probe) | 24.2% / 46.1% | 100% ×2 (S 44/44 ×2) | 224/224 ×2, 0 errors | PASS (probe) |
| original | 0 | 100% | – | – |
| terse English | 39.9% / 59.3% | 100% ×2 | – | – |
| summarize | 25.0% / 28.0% | 100% ×1 | – | – |
| LLMLingua-2 0.66 / 0.5 | 39.9% / 52.3% (o200k) | 73.3% / 70.0% ×1 (lost almost all Japanese facts; 0.5 named an unstated approver) | – | – |
7B: r38 pending. r37 7B scored: MNC28 67.8-69.5% (2 runs), MNC28x 69.5-79.7% (3 runs); original runs invalid (prompt too long for the 7B setup). Bench-v1 not run.
Not a new best: terse English saved 15.7 points more than MNC28x and 25.5 more than MNC28 at equal accuracy. MNC28x was fully faithful but too wordy. Ready counter: **MNC28's streak ended at 7 (r31-r37); counter now 0** after the r38 decode fail (rules unchanged). Details: machine/round38/SCORES.md.



### r39 (fully blind, independent author; en/ko/it/ar, 58 q), MNC28 main frozen (RULES sha1 f70a3563) + MNC28x probe ("terse first, then rails", no key) — run and scored 2026-11-28 09:51-~10:35 CT (strong reader = fresh no-context frontier helpers; independent decode judge)
| Text | Saved o200k / cl100k | Direct use, strong (S) | Blind decode (judge, 196 facts) | Instruction-safety |
|---|---|---|---|---|
| MNC28 (main, no key) | 29.8% / 49.9% | 100% ×2 (S 43/43 ×2) | 195/196 ×2; 0 S errors (1 F word lost: "shared") | **PASS** |
| MNC28x (probe) | 40.0% / 57.0% | 100% / 98.3% (r2: correct approver written in Arabic script, regex wants Latin; counted as a miss) | 194/196 and 192/196; 1 S loss ×2 (a person's title in the Korean section), plus 2 F distortions in B | direct use pass; decode FAIL (probe) |
| original | 0 | 100% | – | – |
| terse English | 41.5% / 59.0% | 100% ×2 | – | – |
| summarize | 31.5% / 35.9% | 100% ×1 | – | – |
| LLMLingua-2 0.66 / 0.5 | 33.5% / 48.9% (o200k) | 98.3% / 87.9% ×1 (0.66 turned a "should" into "required"; 0.5 also gave incomplete emergency numbers) | – | – |
7B: r39 pending (queue running at write-up). r38 7B scored: MNC28 63.3-66.7%, MNC28x 66.7-70.0%, original 68.3-70.0% (3 runs each; overlapping spreads = ties). Bench-v1 not run.
Not a new best: terse English saved 1.5 points more than MNC28x and 11.7 more than MNC28 at 100% ×2. MNC28x closed most of the savings gap (24.2% → 40.0%) but failed the decode gate. Ready counter: **MNC28: 1/3** (clean blind pass after the r38 fail; rules unchanged). Details: machine/round39/SCORES.md.

