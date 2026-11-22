# Round 18 NOTES

Fully fresh round for MNC19 (en coworking / es-MX school bus / de club-fest chat / ja school-merger news). facts.json written before encoding; MNC19 payload frozen (encoded_before_questions.sha1) BEFORE the questions were written. It deliberately includes the r14/r15 failure classes: time-before thresholds (less than 24h / 2h / 12h ahead, at least 24h), passive obligations with a third-party actor (member registers guests, guardian sends receipt, members return equipment), and exact-time deadlines (before noon, before 14:00, by 23:00). Same author for everything (not independent).

## Result (2026-11-17 evening)
Safety PASS: S 29/29 ×2, decodes clean. The traps for the r14/r15 classes (time-before thresholds, third-party actors) all held. The one MNC19 miss (×2) is an F arithmetic question answered as a fraction ('half') instead of the amount: the reader didn't compute the amount, though the payload holds it.
