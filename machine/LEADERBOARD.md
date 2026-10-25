# Machine-native code (MNC) leaderboard

All token counts are from tiktoken. Facts kept = strict blind-decode scoring against a language-neutral fact list (a decoder with no context, given only the key and the payload).

| Round | Passages | Payload saved o200k | Payload saved cl100k | Key tokens o200k / cl100k | Break-even (orig tokens) o200k / cl100k | Facts kept (all decodes) | Lost | Invented |
|---|---|---|---|---|---|---|---|---|
| r1 (2026-10-24) | 4 (2 en, 1 es, 1 zh) | 39.0% (938→572) | 49.5% (1153→582) | 186 / 185 | ~477 / ~374 | 94.5% (137/145) | 0 | 0 |

r1 per language (o200k / cl100k saved): en 41.5% and 46.2% / 41.4% and 45.8%; es 44.9% / 53.2%; zh 22.7% / 53.7%.

Reference: human-readable AIL v2.3 saved 16.4% (o200k) on blind encode, with a ~1.2k-token key.

Rule for a new best: facts kept must not drop, and payload + key tokens must fall, both measured blind.
