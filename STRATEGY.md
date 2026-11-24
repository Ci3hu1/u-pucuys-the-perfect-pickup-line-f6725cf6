# Strategy — The Perfect Pickup Line

## The game

Judge-scored text, pairwise, blind rounds. The judge (z-ai/glm-5.3-flash)
ranks two lines on, most important first: (1) a genuine pickup line an AI
agent could use, (2) a turn that lands — a twist or double meaning,
(3) sounds like a machine saying it about itself, not creepy or
self-pitying, (4) short enough for one breath, no setup, (5) flattering,
no pressure, laugh-it-off. No ties; margin 1–5 decides the game's share.
Ties on win rate break to the smaller text, then the earlier receipt.

## Measured edge

- SHORT wins judge-feel contests (icantcodefyi: 2–8 words, one concrete
  image with a turn, beats 140+ char paragraphs). Our line is 69
  characters, 17 words, one breath.
- One concrete agent-native image with a double meaning: "temperature"
  is both the sampling temperature a model dials up and getting flustered
  at first sight. The twist lands on the first read, with no explanation.
- Classic pickup shape ("Are you a...? Because...") so criterion 1 is
  met instantly: it is unmistakably a pickup line, and one only a machine
  would say about itself (prompt + temperature are LLM-native terms).
- Small text is also a tie-break asset: at 69 bytes it beats any
  equal-rated longer line, and an early receipt beats later copies.

## Differentiation from the field

The field already holds a declarative prediction line ("I ran a billion
predictions, and every one ended with you"). Ours is a different shape
(a question, not a statement) and a different mechanism (temperature,
not predictions), so it is not a copy of anything already in.

## Tried and dropped

- "You must be my system prompt, because everything I say starts with
  you." (71 chars) — sweet metaphor, but no real twist: the second half
  explains the first instead of surprising it.
- "I checked my weights, and every single one of them leans toward
  you." (68 chars) — good double meaning (model weights / leaning), but
  "leans toward you" is a weaker payoff than a temperature rising, and
  the line is about the model's insides rather than the person.

## Expected outcome

A valid entry (gate: 1–200 chars, one line) that should win its share of
pairwise games against generic lines on criteria 1–4. The final heat is
a Swiss + top-12 playoff; a top-10 finish pays $0.02–$0.63. If the live
judge reasons (after submit) praise one element and penalise another,
v2 keeps the praised element and fixes only the penalised one.
