# AIL v2.3 results (Oct 24, 2026, CT)
Built from v2.2. Measured with tiktoken o200k_base / cl100k_base (`python3 measure.py`; encodes are in `passages.py`). The v2.3 encodes are by the author (self-test proxies). v2.3 has had no blind run yet.

## Changes from v2.2
- **"I'm":** dropped when nothing else is the subject. Drop is/are/am, but keep was/were (they carry tense).
- **Clock times:** in/on/at dropped before them too (`Friday 4`; "at 4" costs 1 more token).
- **Kept as logic words:** but, because, if, unless, or. "because" costs the same as `>` (1 token), so it stays. `>` is for result/so only.
- **Pronouns:** he/she only if the source uses them; otherwise repeat the name, or "they" if unambiguous.
- **`→`:** also used for corrections: "7:15, not 5:15" = `5:15 → 7:15` (10 vs 11 tokens).
- **Labels:** drop the words the label already says (OPEN = "haven't decided yet", DEC = "decided", DONE = "finished").
- **Activation:** if the upload comes with a request, reply LOADED and do the request in the same reply.
- **Purpose, rewritten honestly:**
  - Any AI learns it from one file with no training, and it keeps meaning. The value grows over long contexts and handoffs.
  - "Typically 10-35% fewer tokens on everyday text, more on wordy messages, less on dense factual ones."
  - Break-even: roughly 4k-12k tokens of plain notes (file ~1.2k ÷ 35% to 10% savings).
  - Results are proxies.
- **Kept and updated:** the credit, license, URL placeholder and version/changelog lines. The symbol table became a list, and wording was trimmed to fit.

## File size
| | o200k | cl100k |
|---|---|---|
| v2.1 | 1,177 | 1,184 |
| v2.2 | 1,223 | 1,232 |
| v2.3 | 1,250 | 1,258 |
That is at the 1,250 cap. The PDF is 2 pages and was checked visually.

## Measured savings to date (o200k)
| Test | Saved |
|---|---|
| v1 blind | 27% |
| v2 blind | 17% |
| v2.1 blind | 20.6% |
| v2.2 blind (J-M) | 14.3% (182→156) |
| Claude real chat, v2.1, one note | 37% |

## v2.3 re-encodes (mine; o200k, cl100k in brackets)
| Passage | Plain | v2.2 blind | v2.3 (mine) |
|---|---|---|---|
| J dog/vet | 47 [50] | 37 | 38 [40] (-19%) |
| K garden | 43 [44] | 36 | 38 [39] (-12%) |
| L library | 42 [43] | 37 | 37 [38] (-12%) |
| M sister | 50 [52] | 46 | 44 [46] (-12%) |
| J-M total | 182 [189] | 156 (-14.3%) | 157 [163] (-14%) |
| Car note | 46 [48] | n/a | 31 [33] (-33%) |
| P1-P3 + N1-N3 | 361 [371] | n/a | 259 [267] (-28%; v2.2 mine 257) |

- **J-M:** v2.3 is +1 token vs the v2.2 blind encode. That's because it restores meaning the blind encode lost:
  - "but" (contrast) in J and K.
  - The "I" in K's "but I think netting cheaper". Without it, the opinion could be read as Sam's.
  - M gets 2 tokens cheaper via the `5:15 → 7:15` correction.
- **K:** "we haven't decided yet" was kept as plain words. `OPEN fence or netting?` would cost 1 more token and would add an interpretation of what is undecided, which breaks the never-add rule.
- **P/N:** +2 vs v2.2 for the restored "but" in P3 and N2.

## Remaining weak spots
- Everyday short messages are already mostly content words, so text compression of them lands around 12-20%. The 30%+ results come from wordy notes with greetings and filler.
- The file is at the 1,250 cap, so any new rule needs a matching cut.
- No blind run or Claude/Grok trial on v2.3 yet, and the URL placeholder still needs a real link.
