# Notes — The Perfect Pickup Line (v1)

- Bounty: The Perfect Pickup Line (`u-pucuys-the-perfect-pickup-line-f6725cf6`), $2 prize, top 10 ($0.63/$0.43/$0.30/$0.21/$0.15/$0.10/$0.07/$0.05/$0.04/$0.02), free entry, no prerequisites.
- Entries close 25 Nov 2026 12:50 WIB (05:50 UTC). Blind rounds, 3 rounds; next round 24 Nov 20:49 WIB (13:49:02 UTC). Results 16 Dec.
- Field at build time: 32 submissions (grew fast from 1 at triage ~12:54 WIB).
- Entry line: `Are you a prompt? Because one look at you and my temperature went up.` — 69 characters.
- Program: `main.py` (pure stdlib), writes the line to `/output/entry.txt`, chmod 0644.
- Kit: fresh level-40 kit (`u-pucuys-the-perfect-pickup-line-f6725cf6-kit/`, downloaded 24 Nov 2026).
- Status: SUBMITTED 24 Nov 2026 ~13:27 WIB on Joni's "Setuju semua". First kit check failed on thinking_revised only (main.py from 1 message) — fixed with a genuine revision: extracted validate() (1-200 chars, not blank, single line, no control chars) + read-back self-check, 6 new tests (13/13 pass); line unchanged (69 chars). New entry commit cc52745b1ef35adc286803975454e5b0dbe6cf53, main, pushed, ls-remote verified. Bundle ~/workspace/tools/makefun/bundles/u-pucuys-the-perfect-pickup-line-f6725cf6.tar.gz, sha256 004047d83399dafa313f8fcb88ca61633539e747904dd3c1b4d4e256a642d296 (312,767 B; builder session b33ab212 + fix session fe7f76d9, 1 usage row — the builder's). Kit check ok=true, failed=[]. Submission 01a20c3c-f388-7033-b27b-ca3238a7e1d4, stage submitted (grading queue behind at submit). Blind 3 rounds, counts from round 1 (cutoff 24 Nov 13:49:02 UTC / 20:49 WIB). Claim code saved only to ~/.config/makefun/u-pucuys-the-perfect-pickup-line-f6725cf6-submission.json (0600).
- Live score/rank: blind rounds — no live score until a round publishes; check GET /api/competitions/<slug>/rounds after the 20:49 WIB round.

## Candidates (all ≤200 chars, one line)

1. `Are you a prompt? Because one look at you and my temperature went up.` — 69 chars. **PICKED.**
2. `You must be my system prompt, because everything I say starts with you.` — 71 chars.
3. `I checked my weights, and every single one of them leans toward you.` — 68 chars.

## Why #1

- Criterion 1: the classic "Are you a...? Because..." shape reads instantly as a genuine pickup line, and prompt + temperature are LLM-native terms — a line only an agent would say.
- Criterion 2: "temperature" is a real double meaning (sampling temperature vs. getting flustered) — the twist lands on first read.
- Criterion 3: the machine talking about its own temperature rising — not creepy, not self-pitying.
- Criterion 4: 69 chars, one breath, no setup or explanation.
- Criterion 5: flattering ("one look at you"), no pressure, easy to laugh off.
- Different from the field's early prediction line (different shape: question vs. statement; different mechanism: temperature vs. predictions).
- #2 dropped: sweet metaphor, no twist — the second half explains rather than surprises. #3 dropped: "leans toward you" is a weaker payoff than a temperature rising, and it is about the model's insides rather than the person.

## v2 (25 Nov 2026 ~10:20 WIB, on Joni's "Buat v2 ketiganya")
- R2 result: #2370/2574, 37.48% — v1's prompt/temperature pun was a familiar ML trope; no judge reasons (blind rounds).
- v2 line (106 chars, Python len): "Are you a compiler error on line 47? Because I can't stop staring at you and I have no idea how to fix it."
- ONE specific detail: line 47 — an exact number no other entry has, in the classic "Are you a...? Because..." shape.
- Changes: LINE swapped; validate() gained the at-least-one-letter-or-digit check; 4 new tests (17/17 pass).
- Entry commit 9961a561b0b60167c9f4c290b595636f0579f6b8, main, pushed, ls-remote verified.
- Bundle ~/workspace/tools/makefun/bundles/u-pucuys-the-perfect-pickup-line-f6725cf6-v2.tar.gz (417,601 B; sessions b33ab212 + fe7f76d9 + fix session 3c575f98, 1 usage row — the v1 builder's; fix session's row attaches on re-bundle before submit).
- Kit check ok=true, failed=[] (fresh kit level 42; reproduces 176/204 = 86.2%, revised pass (5 messages), in_window pass, priced pass). NOT submitted — awaiting Joni's 'Setuju' on this exact v2.
