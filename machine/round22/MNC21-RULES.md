# MNC21 encoding rules — CANDIDATE (frozen 2026-11-18 ~13:00 CT, before any round-22 text existed)

MNC21 = MNC20 (candidates/mnc20/RULES.md = MNC19 + R7, all rules unchanged) + R8 + R9.
The AGGRESSIVE form (former "x" form) is now the main candidate: drop "you", articles, filler and anything a reader can predict; one handle per person after first mention; dense slot lines. Payload name: payload_mnc21.txt. A less aggressive control form (MNC20-style density with R8/R9) is payload_mnc21c.txt.
Built after seeing the round-21 result; rounds ≤21 cannot count for MNC21. Round 22 (independent author, written after this freeze) is MNC21's first eligible blind round.

## R8 A derived amount is stated as the object of its verb
- Write the resulting amount directly after the charge/pay/refund verb: `charge 300 TL` / `charge 150 TL per hour, which is half the hourly rate`.
- Never leave the antecedent ambiguous (`half hourly rate = 150 TL per hour`). The derivation, if kept, comes after the result in words, never in parentheses.
- When the original gives only a rule (e.g. "half the fee"), keep the rule and also give the base it applies to on the same line.

## R9 Identity: say exactly what the original says
- Original only says "X is the <title>, not <other>": write `X = title, not other`.
- Use `never "x"` (naming/addressing ban) only when the original actually forbids calling/addressing/describing X that way.
- A "never contact/copy Y" rule stays its own prohibition with its object (in the `never:` line), never folded into the identity slot.
