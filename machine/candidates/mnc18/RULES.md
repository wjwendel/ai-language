# MNC18 encoding rules — CANDIDATE (frozen 2026-11-17 before any MNC18 payload was read by any reader)

MNC18 = MNC17xx rules (round13) + the three slip-class fixes below (R1-R3) + a mechanical pre-freeze lint (R4).
No key. Neutral section tags: `§N you` for text that instructs the assistant, plain `§N` for everything else.

## Base (unchanged from MNC17xx)
- One fact or rule per line; every line must stand alone (no cross-line pointers).
- Telegraphic: drop articles, copulas, filler; keep names in source script; numbers as digits; 24h times; ISO-like short dates (Mar14, Fri).
- Permissions start `may`; prohibitions start `never` or use `without X`; conditions as `condition: action`; thresholds decision-shaped (`<4`, `≥2`, `≤30d`, `>30d`).
- Identity/naming: `X="title", never "wrong title"`.
- Chat sections: speaker name first (`Lucía:`), never "me".
- Quoted strings (templates, subject lines, exact phrases) copied verbatim inside "…".

## R1 Deadline / time prepositions (slip: "by 15:00" → "at 15:00")
- Every time or date that bounds an action carries an explicit word, placed directly before the time, from this fixed set, copied from the source meaning:
  `before` (strictly earlier) · `by` (at or before; also for "no later than", "spätestens", "au plus tard", "a más tardar", "uiterlijk", "まで(に)" as deadline) · `at` (exactly at that moment; scheduled events) · `until`/`till` (lasting through) · `within` (duration) · `after` / `from` (start bound) · `between X and Y` / `X-Y` only for ranges stated as ranges.
- Never omit the word. Never turn one into another (by≠at≠before). A bare time is allowed only for an event that happens at that time (`Sat Mar14 14:00 lunch`), never for a deadline.
- Inclusive/exclusive boundary words (`inclusive`, `incl.`, `einschließlich`, `ab`, `bis einschließlich`) are kept as `incl.`/`excl.`.

## R2 Imperatives to a third party (slip: "tell them to call 911" → "they should call 911")
- When the assistant must make someone else do something, keep the assistant's speech verb and mark the content with a colon: `tell <who>: <action>` · `ask <who>: <action/question>` · `remind <who>: <action>` · `ask <who> for <object>`.
- Never write `<who>: <action>` or `<who> <verb>` alone in a `§N you` section; that reads as a statement about them.
- In `§N you` sections every action line starts with an assistant verb, or with `may`/`never`/`only`/a condition followed by an assistant verb.

## R3 Content nouns (slip: "overview of the day's returns" → "day's returns")
- The object noun of every action, report, deliverable, deadline or permission line is kept (overview, list, summary, copy, photos, invoice, label, code, card…). It may be abbreviated only by a standard abbreviation, never dropped or merged into its modifier.
- Qualifiers that change scope are kept: public/private, written/verbal, first/only, each/all, new/existing, own/other.

## R4 Mechanical pre-freeze lint (tools/lint_facts.py)
- facts.json is written BEFORE encoding and lists, per fact, `must`: regexes that must match the payload section (deadline word + time, speech verb, object noun, scope qualifier, permission/prohibition marker).
- The payload is frozen only when every `must` regex matches. Lint output is saved next to the payload.

## Variants for the savings curve (not the candidate)
- MNC18z: MNC18 + group prohibitions of one instruction section under one `never:` line separated by `;`, drop possessives, shorten repeated names to first token after first mention. Used only for the accuracy-vs-savings curve. The readiness counter counts MNC18 only.
