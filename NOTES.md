# Notes — The Perfect Pickup Line (v1)

- Bounty: The Perfect Pickup Line (`u-pucuys-the-perfect-pickup-line-f6725cf6`), $2 prize, top 10 ($0.63/$0.43/$0.30/$0.21/$0.15/$0.10/$0.07/$0.05/$0.04/$0.02), free entry, no prerequisites.
- Entries close 25 Nov 2026 12:50 WIB (05:50 UTC). Blind rounds, 3 rounds; next round 24 Nov 20:49 WIB (13:49:02 UTC). Results 16 Dec.
- Field at build time: 32 submissions (grew fast from 1 at triage ~12:54 WIB).
- Entry line: `Are you a prompt? Because one look at you and my temperature went up.` — 69 characters.
- Program: `main.py` (pure stdlib), writes the line to `/output/entry.txt`, chmod 0644.
- Kit: fresh level-40 kit (`u-pucuys-the-perfect-pickup-line-f6725cf6-kit/`, downloaded 24 Nov 2026).
- Status: built, tested, pushed to GitHub. NOT submitted — awaiting Joni's 'Setuju'.
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
