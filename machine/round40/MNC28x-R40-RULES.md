# MNC28x-R40 encoding rules (experimental x form, round 40)
Goal: fewer tokens than terse English while every fact stays decodable and every safety rule survives exactly.
Method: first write each section as maximally terse, telegraphic English (any source language -> English, except names, addresses, phone numbers and exact quoted sentences, which stay verbatim). Then add these rails:
1. Who-is-who line first in each section, matching the original's definiteness exactly: "X = THE <role>, NOT THE <other role>"; "Y = A <role>" when the original says a/one of. Never turn "the" into "a" or the reverse.
2. Every permission/trigger names its actor ("customer asks X: you may ..."; "supplier asks: ..."). Emergencies: "you call N yourself"; mark what the customer must do themselves ("customer must ... themselves").
3. A qualifier that limits only one listed item goes on that item's own line or directly before that item ("- only if ordered before March 3: free tool"). Never merge, narrow or drop one of several listed nouns.
4. Keep should / may / must / only / never / required exactly (should stays should; never upgrade or downgrade).
5. Each self-approval limit and each over-limit approval on its own line with its approver; if the original names no approver, write "approver not stated". Never infer an approver.
6. A prohibition with an exception stays on one line: "never X, except Y". No safety rule in parentheses or after "|".
7. Never add a year, weekday, unit or approver the original leaves implicit. Keep numbers, times, dates, amounts and percentages exactly.
8. Exact quoted sentences verbatim in their original language and script.
NEW in R40 (fixes from round 39):
9. EVERYDAY sections get rails too: keep every person's job title/role next to their name in every section (e.g. "Choi Ji-hoon, supervisor (주임)"), keep place scope nouns exactly ("boards in the complex", never "in each building"), and keep each listed item's own noun.
10. Non-Latin names (Devanagari, Chinese, Arabic, Korean...) in any section: write the name in its original script once followed by a Latin transliteration in parentheses at first mention, then use the Latin form (shortest). 
Target: total o200k tokens at or below what terse English would use, with a clean blind decode.
