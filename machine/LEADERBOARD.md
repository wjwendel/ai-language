# Machine-native code (MNC) leaderboard

All token counts are from tiktoken. Facts kept = strict blind-decode scoring against a language-neutral fact list (a decoder with no context, given only the key and the payload).

| Round | Passages | Payload saved o200k | Payload saved cl100k | Key tokens o200k / cl100k | Break-even (orig tokens) o200k / cl100k | Facts kept (all decodes) | Lost | Invented |
|---|---|---|---|---|---|---|---|---|
| r1 (2026-10-24) | 4 (2 en, 1 es, 1 zh) | 39.0% (938→572) | 49.5% (1153→582) | 186 / 185 | ~477 / ~374 | 94.5% (137/145) | 0 | 0 |
| **r2 (2026-10-25), current best** | 4 (1 en, 1 es, 1 ja, 1 fr) | 40.8% (1123→665) | 50.0% (1355→677) | 155 / 153 | ~380 / ~306 | 96.6% (171/177) | 0 | 0 |

r1 per language (o200k / cl100k saved): en 41.5% and 46.2% / 41.4% and 45.8%; es 44.9% / 53.2%; zh 22.7% / 53.7%.

r2 per language (o200k / cl100k saved): en 32.4% / 33.1%; es 37.7% / 48.8%; ja 53.2% / 64.1%; fr 37.9% / 46.9%.

Key + payload file vs originals: r1 18.8% / 33.1% saved; r2 26.6% / 38.5% saved.

**Why r2 is the new best:** blind facts kept rose from 94.5% to 96.6% (0 lost, 0 invented in both rounds), the key shrank from 186 to 155 tokens, and break-even fell from ~477 to ~380 (o200k). The passages differ between rounds, so the comparison uses rates. Payload savings are about flat (+1.8 / +0.5 points), so the gain comes from the key.

Reference: human-readable AIL v2.3 saved 16.4% (o200k) on blind encode, with a ~1.2k-token key.

Rule for a new best: facts kept must not drop, and payload + key tokens must fall, both measured blind.
