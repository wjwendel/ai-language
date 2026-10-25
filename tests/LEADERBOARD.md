
## Kit versions (blind encode, o200k)
- v1: 27% saved (185->135), meaning held on blind decode
- v2: 17% saved (199->166), file 1,177 tokens
- v2.1: 20.6% saved (209->166), blind decode 4/4 meaning intact, file 1,177 tokens. CURRENT BEST.

## External tests (Jordan, 2026-10-24)
- Claude v2.1: COMPRESS car/kids/Lisa/milk note 46->29 o200k (37%), all facts kept; fresh-chat EXPAND rebuilt all facts; one slip: "we need" -> "I need" (subject rule). Fix next: keep we/they subject when not I.
- Grok v2.1: EXPAND of same short note: facts kept but "I'll ask Lisa" -> "ask Lisa" (actor lost), "we need" -> "I need", "my car" -> "the car". Fix next: rule that EXPAND must keep every pronoun/actor and contraction exactly as encoded (I'll, my, we), never convert to imperative; subject rule keep we/they.
- v2.2: blind encode 14.3% (182->156); kept we/my/I'll.
- v2.3: blind encode 16.4% (195->163), blind decode 4/4 meaning intact (only articles/tense nuance). File 1,250 o200k. CURRENT BEST, publish candidate. Next fixes: commands with no subject read vs I-rule (mark imperatives), keep recipient name (e.g. Mom) when you is otherwise unclear.
