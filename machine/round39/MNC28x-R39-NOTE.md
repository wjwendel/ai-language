# MNC28x round 39 — encoder note
- Read only originals.txt (4 sections: EN shop rules, KO apartment notice, IT roastery rules, AR bookshop rules); wrote payload_mnc28x.txt.
- Wrote terse telegraphic English for every section, then added the 8 rails: who-is-who line first with THE/NOT THE/A/AN matching the original's definiteness; named actors on every permission trigger; one-item qualifiers on their own line/before that item (e.g. coupling tool only if ordered before March 3; heating cable only if damage reported before Jan 15).
- Each self-limit and over-limit approval on its own line with approver; §1 special orders above $250 marked "approver not stated"; no years/weekdays/units added.
- should/may/must/only/never kept as is (Arabic يُستحسن and Italian dovresti → should); exceptions kept on the same line as their prohibition; emergencies say "you call N yourself" and mark what the customer/reporter must do themselves.
- Names, places, inbox addresses and exact quoted sentences kept verbatim in original script (Korean/Arabic names, Italian/Arabic quotes); «fresco»/«محجوز» definitions keep their noun.
- Size (o200k): original 3584 → payload 2149 tokens (40.0% fewer). Margin is thin; the 40% target cost some low-safety detail compression (e.g. "inquiries" wording, dropping "to customer" where clear).
