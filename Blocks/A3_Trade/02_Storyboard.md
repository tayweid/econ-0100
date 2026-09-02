# Episode A3 | *Specializing and trading can make both parties better off at the same time* — Storyboard (v5, 2026-09-02)

> v5 (nit pass on the v4 render): the derivation pieces pin to the separator's math axis; the
> Spinach caption sits right above the y-axis, off the plot; every offer/endowment point
> carries dashed drop-lines and a LIVE (x, y) readout (commas on the baseline), including the
> wandering white endowment dot; offer dots and the white benchmarks draw above the curves;
> relabels drop onto the true baseline. ⚠ ANDREW'S COUNTER IS NOW 24 S FOR 4 C (RATE 6), not
> rate 5: at rate 5 both offer points coincide at exactly (4, 20) — correct but it reads as a
> bug on screen. The notes' line 25 ("$3.5$" → now "$5$ spinach") needs its one-word swap to
> **6**. The closer reads *We've specialized, traded, and improved with no co-op!* and the
> benchmarks get their own pause before the riders run.
>
> v4 (director's pass on the v3 render): the recap subtitle is *The PPF defines the terms of
> the self-trade* — the Molly-will-accept criterion is saved for its own beat (B06b) right
> before her proposal. The endowment exploration moves the QUIET white dot (it leaves its
> self-trade spot, tries endowments, returns to the specialization point, fades into the glow);
> both specialization points are larger 0.5-opacity GLOW dots, and Andrew's white autarky
> marker is not shown in the offer beats (both markers return as benchmarks for the big trade).
> Captions are baseline-aligned pieces with a smaller (Rate: …) parenthetical. After the
> Pareto definition screen the scene returns at the specialization points and the caption is
> relabelled `Pareto Improvement:`; the closing line is gold CMU — *We've specialized and
> traded with no co-op!*. The window inequality builds piece by piece (1 C · for · 2 S from
> Andrew's boxed entry · < · x S · < · 4 S from Molly's), and the exercise cards now match
> Exercise_A3.md — Q2 | Trade and Q3 | Workable Rates (Changing Labor is parked). Reciprocals
> line: *Opportunity costs are always reciprocals. A workable exchange rate always exists.*
>
> v3 (director's pass on the v2 render): offers are POINTS + bars only — the connecting
> segment and all trade lines are gone (the point vs the PPF is the accept test). Andrew's red
> specialization dot is kept visibly on top of the bars. The caption reads `Molly's proposal:
> 6 S for 4 C (Rate: 1 C = 1.5 S)` — gold label, the rate filing in from the on-screen
> derivation. The negotiation is ONE live tracker: the caption's decimals and both offer
> points roll together (6 → 20 → 12 S). accepts/rejects sit directly UNDER each farmer's rate
> line. Pareto improvement gets a full-frame definition screen (fade out, define, fade back).
> "Still no preferences" is cut. The table screen opens with the gold question `How do we find
> exchange rates that improve both sides?` and the inequality carries units — `1 C for
> 2 S < x S < 4 S` — its bounds flying in from the boxed table entries. The end-of-episode
> number nudge is cut (numbers never change without need).
>
> v2 (director's pass on the v1 render): the co-op recap OPENS the model work — after the
> history card — with the specialization point riding outside the no-specialization line; the
> section title from the self-trade recap on is **Trade**. The trade device is now built from
> ONE concrete proposal at a time: the offer point GROWS out of the endowment with the
> given-up/gained bars (A2's grammar), the exchange rate is set-equal-and-solved on screen
> (`Derivation`) and kept standing top-right, and the negotiation is COUNTER-OFFERS — no
> rate-tracker line sweeps. The dots-become-a-line build, the `Grow/Trade` choice pairs, the
> endowment sweeps, and the ?-corner ride are all cut (the last two deferred to Part B). The
> window inequality lives on the op-cost table, centre screen, and nudges there for the
> nothing-special beat. The final screen is questions + gold `Welcome!` together (gloss and
> `YES!` cut).

Source: `01_Notes.md` (final; rates 1.5 / 5 / 3). Code: `03_Code.py`, one scene `EpisodeA3`,
one flat `construct()`, pause-anchored, 25 stops. Stage-1 verbatim merge of the old scenes:
`_archive/03_Code_stage1_merge.py`. Render: `maniml 03_Code.py EpisodeA3 --render`.

**Numbers.** Window (2, 4). Molly's opening proposal: 6 S for 4 C (rate 1.5, her dream deal) —
her offer point (4, 34) outside her PPF, Andrew's (4, 6) INSIDE his. Andrew counters 4 C for
20 S (rate 5) — his (4, 20) outside, hers (4, 20) inside. Molly counters 12 S for 4 C (rate 3)
— both outside: *Pareto improvement*. Big trade: 3.5 C for 10.5 S at rate 3 → (3.5, 29.5) and
(4.5, 10.5), both better in both goods. Nothing-special nudge on the table: costs 5 / 1/5 and
2.5 / 2/5, window (2.5, 5).

## Beats

### B01 / B01b / B01c | (cold open)
- Bumper: raster MICROECONOMICS; flicker; `Part A | Episode 3`; thesis line. Pause at B01c.

### B02 | (silent)
- `Last Time...` card.

### B03 | "…if not feudalism… or mercantilism… then what?"
- Full-frame gold question: `If not feudalism, then what?` (mostly cam).

### B03b | "One of the first rigorous answers… David Ricardo, writing in 1817."
- Attribution joins: `— David Ricardo, 1817`.

### B04 | "Last time we introduced the idea of a co-op…"
- The co-op graph rebuilds (A2's stage): Molly/Andrew/Co-op PPFs, dots at the equal split.
- Gold line, top: `The choices themselves ARE the technology.`

### B04b | (specialization recap)
- The dots ride to the corners; the co-op dot lands at (8, 40), OUTSIDE the line; FOCUS wiggle.

### B05 | "We talked about self-trades along the PPF…"
- FadeAll; title **Trade**; the two-panel stage (PPFs, under-axis rates, autarky markers).
- The FOCUS self-trade arrows re-draw; gold subtitle: *Molly will accept any trade that's a
  better deal than her self-trade.*

### B06 | "Let's pick some initial endowment…"
- Andrew's panel steps off; definition line in the subtitle slot.
- Molly's endowment dot tries a few spots along her PPF — (0,40) → (5,20) → (2,32) → settles
  all-spinach (0, 40).

### B06b | "Molly proposes: 6 S for 4 C" (director: one concrete trade, grown on screen)
- Caption: `Molly proposes: 6 S for 4 C`.
- The offer point GROWS out of the endowment to (4, 34) — the TRADE segment extending and the
  bars growing with it (carrots gained on x, spinach given up on y): giving up one for the other.

### B06c | (the exchange rate, set equal and solved)
- `Derivation` right of the panel: `4 C = 6 S` → divide by 4 → `1 C = 1.5 S`; it condenses to a
  standing line, top-right: `Exchange Rate: 1 C = 1.5 S` (updates with every offer).
- The full trade line extends through the offer point — outside her PPF: `accepts` joins her
  under-axis rate line.

### B06d | "…it is not terms that Andrew will accept."
- Molly's panel fades; the proposal caption STAYS. Andrew's panel returns; his endowment is the
  red specialization point (8, 0); his white autarky marker stays throughout.
- His offer point grows in to (4, 6) with his bars — landing INSIDE his PPF: `rejects`.

### B07 | "Andrew could counter offer… very nice for him."
- Molly's panel returns. Caption: `Andrew counters: 4 C for 20 S`; standing rate → `1 C = 5 S`.
- Both offer points and trade lines PIVOT on the endowments: his (4, 20) outside → `accepts`;
  hers (4, 20) inside → `rejects`.

### B08 | "Molly counter offers… somewhere in the middle."
- Caption: `Molly counters: 12 S for 4 C`; standing rate → `1 C = 3 S`; pivots again: (4, 28)
  and (4, 12), both OUTSIDE → both `accepts`.

### B08b | "Trading like this is what we call a Pareto improvement."
- Definition line takes the caption slot: `Pareto improvement`: a trade that makes both parties
  better off.

### B09 | "If they trade 3.5 carrots for 10.5 spinach…"
- Offer artifacts clear; TRADE riders run the big trade: (0,40)→(3.5, 29.5), (8,0)→(4.5, 10.5);
  FOCUS wiggles beside the autarky markers — better in BOTH goods.
- Caption: *No co-op required — we've simply specialized and traded.*

### B09b | "…we STILL haven't imposed preferences."
- Caption: *Still no preferences — just the frontier.*

### B10 | "…so long as the exchange rate lives between the two farmers' terms of self-trade…"
- FadeAll; title **Trade**; the op-cost table, centre screen (numerals INK, letters colored).

### B10b | (the window)
- FOCUS boxes on the two carrots-column costs (the bounds); the inequality writes below:
  `2 < exchange rate < 4` (gold).

### B11 | ***Cut to Exercise A3 | Q1.***

### B12 | "…opportunity costs are reciprocals."
- Caption over the table: *Opportunity costs are reciprocals — a workable exchange rate always
  exists.*

### B13 | ***Cut to Exercise A3 | Q2.***

### B14 | "No matter what the original production levels were…"
- The table's costs nudge (5 / 1/5, 2.5 / 2/5) and the window moves with them:
  `2.5 < exchange rate < 5` — nothing special about the numbers.

### B15 / B15b / B15c | "This leaves us two questions… Welcome! We have a lot to do."
- Title *Two Questions*; `1. Where on the PPF should we live?`; `2. Who benefits? How do we
  decide what exchange rate to set?` (white serif, numbered).
- `Welcome! We have a lot to do.` writes in GOLD under the questions, same screen — Part A's
  last word. Runs to black.

## Director notes 6 (2026-09-02, editor session — riders on Taylor's final four)

1. **Note #1 (derivation → caption)**: the proposal caption never transforms — it stands whole,
   and the derivation's result CREATES beside it as the `(Rate: 1 C = 1.5 S)` parenthetical:
   the math produces the rate and nothing else. With the always-on dashed drops and (x, y)
   labels: bind EVERYTHING to the one tracker — dots, drops, coordinate labels, caption
   decimals — Molly's label rides (4, 40−x), Andrew's (4, x). One tracker, one source of truth;
   nothing can drift out of sync during the rolls.
2. **Note #2 (Molly's-counter wonk) — a suspect**: B08's caption takes two changes in quick
   succession (label swap to `Molly counters:`, then the post-definition relabel to
   `Pareto Improvement:`). If both are staged as whole-line transforms, that's exactly the
   note-#3 violation — check that each step transforms ONLY the changing piece.
3. **Note #3's rule is a keeper beyond this episode**: *transform only the text that changes* —
   candidate for the style guide's transitions section after the crunch.
4. **Note #4**: the new pause after the autarky ghosts land makes the stop count 26 — re-anchor.
   Closing caption text to confirm: `We've specialized, traded and improved with no co-op!`
   (serial comma optional — Taylor's call, he uses both).

## Director notes 5 (2026-09-02, editor session — riders on Taylor's seven v3-render notes)

1. **Note #1 (B05 subtitle)**: new line for the text list — `The PPF defines the terms of the
   self-trade.` The script's "Molly will accept any trade that's a better deal than her
   self-trade" stays as VO; its on-screen moment moves later (it's B06b's accept question now).
2. **Note #2 semantics, to confirm**: the BLUE specialization dot (0, 40) never moves; the
   WHITE dot starts where it has been standing (the autarky marker (3, 28)), tours a few
   endowments along the PPF, returns to the specialization corner, and fades INTO the blue glow
   — endowments are choices, and we've chosen all-spinach. If "the initial self trade" meant a
   different start point, correct this.
3. **Note #4 coupling — DECIDED (Taylor, 2026-09-02)**: the two autarky ghosts fade IN at B09
   with the "goal is to do better than the highlighted points in autarky" VO line, take the
   better-in-BOTH-goods wiggle comparison beside the trade riders, then fade out. They exist
   only for this beat; everywhere else the panels carry just the glowing specialization points.
4. **Note #5**: suggest the caption read `We've specialized and traded with no co-op!` —
   hyphenated co-op, matching the course-wide rename.
5. **Note #6 final caption text**: `Opportunity costs are always reciprocals. A workable
   exchange rate always exists.` — two sentences, full stop, no dash.
6. **Note #7 — the exercise cards are two revisions stale.** The current Exercise_A3 is:
   Q1 | Specialization, Q2 | Trade, Q3 | Workable Rates (Q4 is the follow-up, gradescope-only —
   no card). Changing Labor is DROPPED (parked at Practice_Bank/Parked_Q_Changing_Labor.md), so
   the second cut beat dies. The notes put all three questions at ONE stop, after the
   shift-toward-specialties paragraph. Staging suggestion: three sequential cards with pauses
   (B11 / B11b / B11c), one question each — matching how the class actually runs (work Q1, work
   Q2 and collect answers on the board, then Q3 names the window the board is already showing).
   Card texts verbatim from Exercise_A3.md.

## Director notes 4 (2026-09-01, editor session — riders on Taylor's nine v2-render notes)

1. **Note #1's full sweep**: the leftover line artifacts live in three places, not one — B06b's
   TRADE segment, B06c's "full trade line extends through the offer point," and B07's "trade
   lines PIVOT." All three go; accept/reject reads off the POINT against the PPF everywhere.
   (This completes the line-out-of-A3 decision — nothing line-shaped remains.)
2. **Notes #3 + #4 interplay**: with the number tracker, the caption can't flip give-order per
   proposer — keep one canonical caption `x S for 4 C` with x rolling 6 → 20 → 12, and let the
   SPEAKER LABEL carry who's proposing. Two label wordings are now in play ("Molly proposes:"
   v2 / "Molly's proposal:" this round) — pick one and hold it.
3. **Note #4 bonus check**: with C fixed at 4, the rolling x moves both offer points PURELY
   VERTICALLY — Molly's slides (4, 40−x), Andrew's (4, x) — so the tracker morph is a clean
   two-dot elevator, no diagonal drift. (The fixed-4C design pays for itself here.)
4. **Note #8 staging**: the two boxed table entries travel INTO the inequality — Andrew's `2 S`
   cell to the left bound, Molly's `4 S` cell to the right, the unknown `x S` (TRADE) between:
   `for 1 C:  2 S < x S < 4 S`. New subtitle question for the text-review list: `How do we find
   exchange rates that improve both sides?`
5. **Note #9**: B14 goes static — no nudge, no number changes; the nothing-special sentence
   runs as VO over the standing table (a FOCUS pulse at most).
6. **Note #2**: Andrew's red specialization dot (8, 0) is staged at B06d but evidently not
   rendering — surface it from the moment his panel returns, white autarky marker (4, 8) alongside.
7. **Note #7 script coupling**: the "STILL haven't imposed preferences" sentence in the notes is
   now redundant with the closing question's own gloss ("Nothing we've done so far has said
   anything about preferences") — struck in the notes as an optional cut, Taylor's call.

## On-screen text for review (animator-written)
- `Trade`, `Two Questions` (titles); `Molly proposes: 6 S for 4 C`, `Andrew counters: 4 C for
  20 S`, `Molly counters: 12 S for 4 C`; `Exchange Rate: 1 C = …` (standing, top-right);
  `accepts` / `rejects`; `2 < exchange rate < 4` and its nudged form; the B09/B09b/B12 caption
  lines; `If not feudalism, then what?`.

## Deferred (director, 2026-09-01)
- The endowment sweep along the PPF (trade line pivoting to the corner) and the ?-corner ride —
  both saved for Part B (B0 opens on exactly that question).
- The one-unit-increments / dots-become-a-line build — cut in favour of the grown offer point.

## Old-element map
Bumper → B01; last_time → B02; guild-recap scene → B04; questions scene → B15; animation_4's
trade intro → B06–B06d; the animation_5 tracker machine → the offer pivots (B07–B08) and the
standing rate; drafts v1/v2, the vertical number lines, and animation_old were earlier versions
of the same device (stage-1 archive holds them verbatim).
