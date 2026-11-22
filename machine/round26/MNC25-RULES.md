# MNC25 encoding rules — CANDIDATE (frozen 2026-11-19 12:59 CT, before any round-26 text existed)

MNC25 = MNC24 (candidates/mnc24/RULES.md, R1-R17 and all earlier safety rules unchanged) + R18 + R16b + R19.
Main form: payload_mnc25.txt. Aggressive probe: payload_mnc25x.txt (R19 pushed further, target ≥40% o200k on fresh text).
Rounds ≤25 cannot count for MNC25. Round 26 (independent author, written after this freeze) is its first eligible blind round.

## R18 Role word in the header
- Instruction sections open `§N you=<role as written, short>` (e.g. `§1 you=inbox assistant`), never a bare `you`.

## R16b Keep descriptors the name does not state
- Size/type/quality adjectives of the business or people (`small`, `family-run`) stay unless the name already says them.

## R19 Savings (from round-25 fix list)
- Approval lines as `X approves: <object>` only when X was already named with role on the who-is-who or owner line; otherwise `need approval of X, <role>`.
- Drop articles/`of`/`the` inside rule lines; drop `all`/`every` only where the slot is already universal (keep them in quantifier-scope rules and in R15 qualifier lines).
- One business line per section: `<name>, <descriptor>, owner <name>`; inbox + times on the same line.
- Everyday sections: drop field labels the value makes obvious (`registration`, `fee`) unless two values could be confused.
- All safety rules unchanged (may: lines, who-is-who before naming, prohibitions folded into action, thresholds as decision, R12, R14 tell-slot, R15 qualifier after noun, R7, R8b, R9, R10; no safety rule in parentheses or after "|").
