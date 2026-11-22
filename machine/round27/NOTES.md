# Round 27 notes (2026-11-19 ~19:05 CT)

## What worked
- R20 (`approver not named`) fixed the r26 invented-approver slip and even beat the original text: the original, summarize, one terse run and LLMLingua 0.5 all invented Chiara Bonetti as approver for shop/condo quotes; MNC26/26x never did (4/4).
- Promoting the MNC25x form to main lifted savings from 31.6% (r26) to 36.9% with S 100% ×2 and S-clean decodes.
- Author rule "gold must not assume" worked (gold for §3.q3 = approver not stated).

## Holes found
1. `wkdays 7:30,13h` is ambiguous: decode A read two check times as a range (3 sections). Fix R21: `at 7:30 + 13h` for discrete times; ranges keep `7-10h`.
2. Savings: terse English 39.2% vs MNC26 36.9% (o200k). MNC26x was only 12 tokens shorter than main — the aggressive edits were too timid. §2 (everyday Korean) is where MNC is longest relative to terse? No: §2 tied (278 vs 278); MNC is longer on §1 (257 vs 245), §3 (253 vs 238), §4 (242 vs 231). Instruction sections carry the gap.
3. LLMLingua drops leading phone-number prefixes ("070-") — note for baseline analysis.

## Next-round fix list (baselines first)
1. **Savings — terse English wins (39.2% vs MNC26 36.9%)**: MNC27 = MNC26 + R21 + a real aggressive probe on instruction sections: one `never:` line per section for all prohibitions; drop `yourself` after `may` via a section convention line? (test only in x); drop `customer` where the section subject is already the customer; target ≥40% o200k at S 100% ×2.
2. Round 28 fully blind, independent author (copy round27_sealed/AUTHOR-R27.md; rotate languages e.g. en / zh / de / pl).
3. Score round27/answers_7b (queue started 18:59 CT) and append to round27/SCORES.md.
4. Bench-v2 strong-reader set before any formal new-best claim (bench-v1 at ceiling).
5. Ready counter 2/3: keep main-form safety rules frozen except R21 so r28 can complete 3/3.
