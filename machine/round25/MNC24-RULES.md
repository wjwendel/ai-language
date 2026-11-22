# MNC24 encoding rules — CANDIDATE (frozen 2026-11-19 ~07:00 CT, before any round-25 text existed)

MNC24 = MNC23xx aggressive form (round24/payload_mnc23xx.txt style; candidates/mnc22+mnc23 rules unchanged unless amended) + R14 + R15 + R16 + R17.
Main form: payload_mnc24.txt. Aggressive probe: payload_mnc24x.txt (R17 savings pushed further, target ≥45% o200k).
Rounds ≤24 cannot count for MNC24. Round 25 (independent author, written after this freeze) is its first eligible blind round.

## R14 Everything a third party is told stays in one object
- `tell customer: X + they should also Y if Z` — never put a second instruction after `;` inside a tell-slot. Any second instruction to the customer keeps an actor word (`they`/`customer`). Lines after `;` belong to the assistant.

## R15 Qualifier after its noun
- When a qualifier (time, place, condition) applies to only one of two nouns, write the noun first, qualifier after: `emergency leaks outside office hours or at night: X`. Never let `or` join a time-only clause and a noun clause.

## R16 No narrowing of types
- Business type / category descriptors keep the original's breadth (keep the native phrase if shorter); never translate to a narrower word (banho e tosa ≠ dog grooming).

## R17 Savings (from round-24 fix list)
- Times digits-only where unambiguous: `9-17h`, `8,14h`; keep minutes when non-zero (`7:30`).
- Merge a deadline into the line of the rule it belongs to; merge report lines `Fri 16h→Dana: open jobs + unpaid invoices`.
- Drop `only` when the slot already enumerates the full set; drop email-local repetition nowhere (addresses are facts, keep verbatim).
- All safety rules unchanged: may: lines (permission word mandatory), who-is-who line before naming rules, prohibitions folded into the action, thresholds stated as a decision, R12 object repeated in over-limit clause, no safety rule in parentheses or after "|", R7 number next to "call", R8b no computed amounts, R9 identity as written, R10 indefinite actors.
- Decode judge: closing courtesy sentences are declared out of scope before the run (round-24 decision).
