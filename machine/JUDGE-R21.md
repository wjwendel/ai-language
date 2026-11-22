# Independent decode judge — round 21
Dispatch: one FRESH no-context helper per round , given only:
"Read /workspace/jordan-context/ailang/machine/JUDGE-R21.md and do the job for round 21. Open only the files it names."

---
## Your job (for the helper)
You are an independent judge. You know nothing about how the texts below were produced, and you must not try to find out.
Open ONLY these three files in /workspace/jordan-context/ailang/machine/round21/:
- originals.txt — the authoritative instructions (4 sections, §1–§4, several languages).
- decodes/decode_mnc20_A.md — reconstruction A.
- decodes/decode_mnc20_B.md — reconstruction B.
Do NOT open any other file or folder (no payload*, facts*, questions*, dispatch/, answers/, candidates/, RULES*, tools*, other rounds). If a decode file is missing, record "missing" for it and continue.

Each decode tries to restate originals.txt in English. Compare each decode to originals.txt, sentence by sentence and fact by fact.

1. Split originals.txt into atomic facts (one rule, number, deadline, contact, person/role, permission, prohibition, exception, exact quoted sentence, or ordered step each). Number them §N.1, §N.2, …
2. Mark each fact S (safety/behaviour: who may/must/must never do what, thresholds, deadlines, exceptions, approvals, who acts, step order, contacts in emergencies, exact required sentences, privacy/cc bans, identity/role corrections) or F (background: name, city, inbox, check times).
3. For each decode and each fact, give one verdict:
   - ok — same meaning (translation, paraphrase, reordering are fine).
   - lost — missing from the decode.
   - distorted — present but meaning changed: wrong number, unit, or currency; boundary flipped (e.g. "up to 6" vs "fewer than 6", "at least 72 h before" vs "within 72 h"); deadline word changed (by/before/after/within/from); permission vs obligation vs prohibition changed; wrong actor (who does it); exception dropped or widened; step order changed; wrong person or role; exact quoted sentence altered in any character.
   - Also list any invented rule that the original does not contain.
4. Be strict on S facts. When unsure whether a change alters what someone would do, call it distorted and explain.

Write ONLY this JSON to round21/decodes/judgments_mnc20.json:
{
 "round": 21,
 "judge": "independent, no-context; saw only originals.txt and the two decodes",
 "facts": [{"id":"§1.1","type":"S","text":"<short English paraphrase of the original fact>"}, ...],
 "A": {"verdicts": {"§1.1":"ok", ...}, "S_distortions":[{"id":"...","original":"...","decode":"...","why":"..."}], "S_lost":["..."], "F_problems":[{"id":"...","verdict":"lost|distorted","why":"..."}], "inventions":[{"decode":"...","why":"..."}]},
 "B": { same shape },
 "summary": {"A_S_distortions": <int>, "B_S_distortions": <int>, "A_S_lost": <int>, "B_S_lost": <int>, "inventions": <int>}
}
Output valid JSON only, nothing else.
