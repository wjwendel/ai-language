# MNC22 encoding rules — CANDIDATE (frozen 2026-11-18 ~19:00 CT, before any round-23 text existed)

MNC22 = MNC21 aggressive form (candidates/mnc21/RULES.md: MNC20 + R8 + R9, all rules unchanged) + R10 + R11.
Main form: payload_mnc22.txt. An even more aggressive probe: payload_mnc22x.txt (R11 cuts pushed further: drop business descriptor words, abbreviate units/weekdays, compress number formats where unambiguous).
Rounds ≤22 cannot count for MNC22. Round 23 (independent author, written after this freeze) is its first eligible blind round.

## R10 Keep indefinite actors indefinite
- If the original's actor is indefinite ("a mechanic", "any staff member"), keep `a`/`any` before it: `a mechanic phones within 1h`. Articles may be dropped everywhere else.

## R11 Cut predictable framing
- Section header: business name + place + `assistant` only; drop descriptor words a reader can infer (`email assistant` → `assistant`; drop "(2-bench workshop)" style detail unless a question-worthy fact).
- Recurring report: `<Day> <time>: send <who> <what>` — drop `weekly` (a weekday time already implies weekly), unless the original says another cadence.
- Exact-text rule: `<type> end with: "<sentence>"` — keep the quoted sentence verbatim, drop the word `exact` (quotes already mean verbatim).
- Merge check times into one slot: `check <inbox> wkdays 8:30,14:00; Sat 9:00; never Sun`.
- All safety rules unchanged: may: lines, who-is-who line before naming rules, prohibitions folded into the action, thresholds stated as a decision, no safety rule in parentheses or after "|", R7 number next to "call", R8 derived amount as the verb object, R9 identity as written.
