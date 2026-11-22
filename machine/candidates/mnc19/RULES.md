# MNC19 encoding rules — CANDIDATE (frozen 2026-11-17 evening, before any MNC19 payload was read by any reader)

MNC19 = MNC18 R1-R4 (candidates/mnc18/RULES.md, unchanged) + MNC18z structure as the default + two fixes for the round 14/15 failures (R5, R6).
Built after seeing round 14/15 results, so these rules are tuned on those rounds. Only rounds whose passages no reader had seen when MNC19 was frozen (16, 17, 18) can count for MNC19.

## Structure (from MNC18z; held 100% ×2 on bench-v2 with the strong reader, 38.7% vs 32.7% o200k)
- Per instruction section, prohibitions with no condition of their own go on ONE line: `never: A; B; C` (each item is a full action with its object; parenthesised routing is allowed: `answer rent increases (forward to Lindner)`).
- Identity inline at first mention: `Name (="title", never "wrong title")`.
- Approval tiers for one decision go on one line: `<$400 …; $400-$1,500: …; >$1,500: …`.

## R5 Comparisons on time, duration, date or age are written as decision words, never bare symbols
- Use: `less than`, `more than`, `at least`, `at most`/`up to`, `under N years`, `N years or older`, with the anchor spelled out: `cancel less than 24h before appointment → fee R$50`.
- Bare `<`, `>`, `≤`, `≥` are allowed ONLY on plain money or count amounts (`>$1,500`, `≤3 rooms`), where no strong-reader flip has been seen.
- Inclusive/exclusive edges stay explicit (`day 7 incl.`, `Mar 16-Apr 30 incl.`).

## R6 Every obligation keeps its actor
- A line that says something must be done names who does it: the assistant (verb first, R2) or the third party (`customer submits invoice info within 30 days of order`; `tenant shows ID card`).
- Never a bare noun phrase plus a deadline (`invoice info within 30d`).

## R4 lint update (tools2/lint_facts.py, form-aware; facts.json files are NOT edited)
- Before matching, the lint expands `never: A; B` into one `never A` line per item, rewrites `Name (="x"` as `Name="x"`, and maps decision words to symbols for matching only (less than→<, more than→>, at least→≥, at most/up to→≤, under N→<N).
