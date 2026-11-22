# MNC26 encoding rules — CANDIDATE (frozen 2026-11-19 ~19:00 CT, before any round-27 text existed)

MNC26 = MNC25 (candidates/mnc25/RULES.md; R1-R19 and all earlier safety rules unchanged), with the MNC25x (aggressive) form promoted to the main form, + R20.
Main form: payload_mnc26.txt (MNC25x-level compression + R20). Aggressive probe: payload_mnc26x.txt (push §-instruction sections further: drop words the reader can predict, target ≥40% o200k).
Rounds ≤26 cannot count for MNC26. Round 27 (independent author, written after this freeze) is its first eligible blind round.

## R20 Unnamed approver marker
- When the original requires approval/permission but names no approver, write `need approval, approver not named`. Never leave a bare `need approval` next to a named person's line. No parentheses for this marker.
- When the original names the approver, keep `need approval of X, <role>` (R19).
