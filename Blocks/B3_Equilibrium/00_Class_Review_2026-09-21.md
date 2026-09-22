# B3 · What went wrong in the Sep 21 class (reference for the rebuild)

<!-- Fable, 2026-09-22. Condensed from a multi-lens review of the class export (media/EpisodeB3_present, 547 s of motion, 225 stops), 03_Equilibrium.py, the notes, and B1/B2; each finding was fact-checked against the code. The full machine output is in _archive/2026-09-21_class_review_full.json; the critique of the rebuild outline's first draft is in _archive/2026-09-22_outline_critique_full.json. Taylor's own account is in 00_Outline.md §12. -->

## The diagnosis in one paragraph

Equilibrium is a claim about the whole market: pick a price, count who is willing on each side, compare. The class animation explained everything through one individual-level question — "would this person switch?" — for 386 of 547 seconds, and never counted. So the definition card at `4.a` ("Equilibrium is where no one wants to change," with the Qd = Qs clause dropped) landed on a frame with no price line on the demand side, four idle buyers who visibly *did* want to change, and a gold arrow pointing at a graph tick. The frame that supports the definition — plaza beside the combined graph, one price line, Qs and Qd printed, the left-out people ringed — exists at `5.b`, after the definition, the algebra, and Exercise Q1. Students left with two definitions (people-level from the plaza, curve-level from the algebra) and had to build the bridge themselves.

## Verified findings

- **145 of 225 stops precede the word "equilibrium."** B1 has 75 stops, B2 has 85. One seller's arrival (`3.a.growth.S2`) costs 47 clicks and 119 s with no caption; the price is effectively settled by t = 312 and the next 12 arrivals (73 s, ~40 clicks) change nothing. Three zero-motion clicks sit right before the definition.
- **Every price move before `4.a` is triggered by an arrival.** About 270 s of the build *is* fixed-cast adjustment (unsold sellers cutting, unserved buyers outbidding), but it is never framed as "Qd ≠ Qs at the going price," so it reads as "prices change when people show up" — B5's lesson, not B3's. The notes' "trading gets calmer and calmer" beat does not exist in the animation.
- **No count of Qd vs Qs anywhere before `4.b`;** the demand panel never gets a price line during the build; the side panels sit on opposite edges of the screen.
- **Both halves of the definition share a frame only at `5.h.iii`** (t = 546 of 547).
- **The `5.c`/`5.g` adjustment runs remove the price line and the Qd/Qs readouts while prices move,** use a noisier search rule than the build (random visits, not the full survey), and in the excess run one ask drops to $3.00 and is bid back up — "excess → price falls" is visually contradicted for ~12 stops.
- **Two markets under one title:** "What happens at $3?" covers the aggregate (Qs = 20, Qd = 45, thousands of pounds) and, after a fade to black, the toy (4 vs 8, units). Nothing says they differ; both settle at $4.
- **Notation:** the worked algebra uses a bare Q; the exercise card and B2 use Q_d/Q_s; the step that licenses setting the equations equal is never shown.
- **Stability tests (`5.h`) use only the zero-gain marginal pair,** so the on-screen reason is "can't afford it," not "could buy elsewhere at $4."
- **No opening hold poses the day's question**; the export goes bumper → `2.a`. The notes' 1.a/1.b (recap, floating price with "?") were never built.
- **Notes vs animation:** Amanda-Grace MB $6 in the notes, $7 in code; the notes' 2.a "$2–$6 window" is not drawn; the notes' 3.a/3.b full-market run does not exist.

## What worked and is preserved in the rebuild

- The side-view close-ups (`2.a.i`–`2.b.v`, `5.h.i`/`5.h.ii`) and the green expenditure boundary sliding across to become revenue.
- The bidding war compressed into one 14 s play ending on "Gary: next bid $6.50 > MB $6" (`2.c.iii`).
- "Why is Gary left out?" / "Gary traded at $5.50. Now $6.25 > MB $6." (`3.a.excluded`) — the strongest idea in the build: nothing about Gary changed, the price excluded him.
- `5.a`/`5.d` (line at $3/$6, colored plug-in arithmetic, gold gap) and `5.b`/`5.d.i` (definition card with arrow to ringed buyers / unsold boxes, counts on the adjacent graph).
- `4.c`–`4.e` algebra, `5.g.production` (high-cost sellers stop producing as the price falls), "excess, not surplus."

## Simulated first-year student, in brief

Locked in through the close-ups and the bidding war; drifting from the fourth seller's arrival ("I stop knowing why I'm watching; I believe the prices are going down, but nobody has given me a way to predict where"); bothered at `4.a` ("four buyers are standing there with no spinach — they want to change!"); the click came at `5.b`: "If Qd is bigger than Qs, the difference is a specific set of people who are willing to pay the going price and have nothing, and they are the ones who change it. When Qd = Qs those people don't exist." The missing sentence: *pick any price and count both sides; if the counts differ, the difference is real people who want to trade at that price and can't, and they move the price; $4 is the only price where the counts match.*

## How the rebuild answers it (see 00_Outline.md)

Counts appear whenever a price line exists (on fingers in the small scenes, on the shared Q axis in the big one); the definition lands on the frame with the counts; the growth loop is gone; the big market *is* the algebra market; each adjustment is one boxed deliberation plus one short play with counts rolling; an opener poses the question; prediction holds precede reveals.
