# Episode A3 | *Specializing and trading can make both parties better off at the same time* — Storyboard (v1, 2026-09-01)

Source: `01_Notes.md` (FINAL, 2026-09-01 editor session — history detour opens the episode
after the recap, Pareto christened at the accept moment, Society's PPF parked at
`Societys_PPF.md`, the episode ends on "Welcome!"). Code: `03_Code.py`, one scene `EpisodeA3`, one flat `construct()`,
pause-anchored (`# Bxx` sections, unnamed `self.pause()`). The stage-1 verbatim merge of the old
scenes is archived at `_archive/03_Code_stage1_merge.py`. Render: `maniml 03_Code.py EpisodeA3 --render`.

The episode's stage is A2's closing stage, carried forward: the two same-scale panels (Molly
left, Andrew right), farmer names under the axes grown into their self-trade rates, autarky
markers at (3, 28) and (4, 8). The new device is the **trade line**: TRADE-pink, drawn through
an endowment, pivoting on it (never anchored to the intercepts — the contrast the notes flag),
its slope the exchange rate, driven by a rate tracker so offers, rejections, the window, and the
corner sweeps are all one mechanism.

**Numbers** (RESOLVED 2026-09-01 — the notes now carry the corrected set). Window: any rate
strictly between the self-trade rates 2 and 4 benefits both. The demo/opening rate is **1.5**
(the notes' one-unit example, and Molly's dream deal — Andrew's line falls inside his PPF, he
rejects), Andrew's counter is **5** (Molly rejects), the middle is **3** (both accept; *Pareto
improvement*). The concrete point-trade is give 6 S / get 4 C at 1.5: Molly (0,40)→(4,34)
outside her PPF, Andrew (8,0)→(4,6) INSIDE his — the point beats answer both accept questions
before the line exists. The worked ending trade is unchanged: at rate 3,
3.5 C for 10.5 S; post-trade Molly (3.5, 29.5), Andrew (4.5, 10.5) — both better in both goods
than autarky.

**Old-element map** (everything serves a beat): bumper → B01; last_time → B02; the guild-recap
scene → B03; the questions/gains scene → B18–B19; animation_4's trade-line intro → B06–B08; the
animation_5 tracker machine (trade lines, rate sweeps, benefit beats) → B07–B12 and B16; the
v1/v2 drafts and the vertical-number-line fragment are earlier versions of the same device —
their beats all appear via the final machinery; animation_old was unused in the original.

## Beats

### B01 / B01b / B01c | (cold open)
- Bumper: raster MICROECONOMICS fades in; flicker; `Part A | Episode 3`.
- Thesis line: *Specializing and trading can make both parties better off at the same time.*
- Pause lands at B01c, as in A1/A2.

### B02 | (silent)
- `Last Time...` card.

### B03 | "Last time we introduced the idea of a co-op… without needing to work more or to develop better technology."
- A2's closing stage rebuilds: both panels, PPFs, autarky markers, under-axis rate lines
  (`Molly: 1 C = 4 S`, `Andrew: 1 C = 2 S`).

### B03b | "The choices themselves ARE the technology."
- The line writes in the centred subtitle slot, DEFINITION gold — the recap's keeper.

### B04 | "…the origin of the study of economics… began as a question… if not feudalism… or mercantilism… then what?"
- FadeAll; the question writes full-frame, gold: `If not feudalism, then what?`
- Mostly cam; the card holds under the history paragraph.

### B04b | "One of the first rigorous answers came from the model we started last time, David Ricardo, writing in 1817."
- Attribution joins, quote-style: `— David Ricardo, 1817` (CAPTION, offset right).

### B05 | "We talked about self-trades along the PPF and left by asking what exchange rates each farmer would accept…"
- FadeAll; the two-panel stage returns; the FOCUS self-trade arrows re-draw on both panels.
- Gold line, top: *Molly will accept any trade that's a better deal than her self-trade.* (A2's hook, answered this episode).

### B06 | "Let's pick some initial endowment… If Molly grows only spinach, her initial endowment is all spinach, (0, 40)."
- Title *The Trade Line*; Molly's panel front and centre (Andrew's steps off, as A2's B16).
- Definition line, bottom strip: `Initial Endowment` *is how much of both goods Molly has.*
- FOCUS ring lands on the endowment dot at (0, 40).

### B06b | (director 2026-09-01: one specific trade first, as a point — no line yet)
- Gold question, subtitle slot: `Would Molly accept this trade?`
- The trade: give 6 S, get 4 C. TRADE dot at (4, 34) with dashed drops; A2-style bars on the
  axes — carrots gained (0→4, CARROTS), spinach given up (34→40, SPINACH).
- The point sits visibly OUTSIDE her PPF — the accept criterion, planted before the line exists.

### B06c | (the exchange rate, derived on screen the op-cost way)
- `Derivation` (A2's numerals-only machinery) on the right: `4 C = 6 S` → divide by 4 → `1 C = 1.5 S`.

### B06d | (the same trade, from Andrew's side)
- Andrew's panel returns (it stays for the rest of the episode); gold question: `Would Andrew accept the same trade?`
- TRADE dot at (4, 6) — he gives 4 C (bar 4→8), gains 6 S (bar 0→6); INSIDE his PPF — he won't accept.

### B06e | "If she kept trading at this rate, we can see all her possible endowments after trade." ***Show in one-unit increments.***
- Points and bars clear; the standing rate takes the subtitle slot: `Exchange Rate: 1 C = 1.5 S`.
- TRADE dots step in one per unit: (1, 38.5), (2, 37), (3, 35.5), (4, 34), (5, 32.5), (6, 31);
  caption at the first step: `+1 C, −1.5 S`.

### B06f | "We can represent these points with a line. Just like with the PPF, the slope of the line represents the exchange rate."
- The trade line Creates through the dots (TRADE); dots fade into it.
- Caption near the line: `slope = exchange rate`.

### B07 | ***Show: the trade line doesn't anchor to the axis intercepts — it pivots on the initial endowment. Draw that contrast deliberately.***
- FOCUS pulses on the PPF's two intercepts (its anchors), then a FOCUS ring on the endowment dot.
- The rate tracker wiggles (2.5 → 3.2 → 1.8 → 2.5): the line visibly pivots on the endowment
  while the PPF stands still.

### B08 | "If the trade line lives outside Molly's PPF… she will accept. If it is on the inside… she will reject."
- Rate sweeps to 4.5: line falls inside her PPF → `rejects` (NASH) joins her under-axis line.
- B08b: back out to 1.5 → `accepts` (EFFICIENT).

### B09 | "For a trade to work, both sides must be willing… While this example is very nice for Molly, it is not terms that Andrew will accept."
- Andrew's trade line joins on his panel (present since B06d), through his endowment (8, 0).
- The rate already sits at 1.5 (Molly's dream deal): his line draws inside his PPF → `rejects`.

### B09b | "Andrew could counter offer with terms that are very nice for him…"
- Rate sweeps to **5**: Andrew `accepts`, Molly `rejects`.

### B09c | "Molly counter offers with a trade that lives somewhere in the middle… Trading like this is what we call a Pareto improvement."
- Rate settles at **3**: both `accept` (both EFFICIENT).
- Definition line, bottom strip: `Pareto improvement` — a trade that makes both parties better off. [term gold; wording from the notes when final]

### B10 | "What I've shown here is a small trade… If they trade 3.5 carrots for 10.5 spinach, both farmers have more of both crops…"
- The endowment dots ride their trade lines: Molly (0,40) → (3.5, 29.5); Andrew (8,0) → (4.5, 10.5).
- The autarky markers ghost beside them; EFFICIENT wiggle on both riders — better in BOTH goods.
- Caption: *no co-op required — we've simply specialized and traded.*

### B10b | "And it's important to note here that we STILL haven't imposed preferences."
- Caption line, bottom strip: *Still no preferences — just the frontier.*

### B11 | "You can see that so long as the exchange rate lives between the two farmers' terms of self-trade, they can be made better off…"
- The two under-axis rate lines FOCUS-box (the bounds); a live rate readout joins: `r = 3`.
- Rate sweeps 3 → 4 (Molly's accept flips exactly at 4) → 3 → 2 (Andrew's flips) → 3.
- The window lands as a gold line: `2 < rate < 4`.

### B12 | "Growing a carrot herself costs Molly 4 spinach but buying one costs 3… Both farmers go all the way to their corners."
- Choice pairs, A0's green/red boxes: Molly `Grow(1 C) = 4 S` (NASH) vs `Trade(1 C) = 3 S` (EFFICIENT); Andrew mirrored (`1/2 C` vs `1/3 C`).

### B12b / B12c | ***Show: slide Molly's endowment along her PPF toward all-spinach — the trade line pivots with it and sweeps outward, reaching furthest at the corner. Then the same on Andrew's side.***
- Molly's endowment tracker slides (3, 28) → (0, 40), the trade line translating with it — furthest reach at the corner. Pause.
- Andrew's slides (4, 8) → (8, 0), same sweep. Pause.

### B13 | ***Cut to Exercise A3 | Q1.***
- Exercise card (sans body): specialize and trade — 1 R for ___ F.

### B14 | "…each farmer will always have a comparative advantage in one of the goods… opportunity costs are reciprocals."
- Caption line: *Opportunity costs are reciprocals — an exchange rate that works always exists.*

### B15 | ***Cut to Exercise A3 | Q2.***
- Exercise card: McGonagall doubles her hours — old and new PPF, new opportunity cost, effect on the trade.

### B16 | "This isn't some mathematical sleight of hand. No matter what the original production levels were…"
- Both PPFs nudge (Molly's intercept 40 → 44, Andrew's 16 → 20) with the rate-3 trade lines held: both still `accept` — nothing special about the numbers.

### B17 | "We've done something extraordinary here…" (cam)
- No code; the two-panel stage holds.

### B18 | ***Show: the specialization corner rides along the PPF with a "?" — hold it as the two questions land.***
- A FOCUS `?` dot rides Molly's PPF away from the corner and back.

### B18b / B18c | "This leaves us two questions…"
- Title *Two Questions*; numbered, white CMU serif (the A2 pattern):
  `1. Where on the PPF should we live?`
  `2. Who benefits? How do we decide what exchange rate to set?`

### B18d | "Notice every rate in the window splits the gains differently. Close to 2 is Molly's dream deal. Close to 4 is Andrew's."
- The gloss joins under the questions, narrator sans, CAPTION: `Close to 2 is Molly's dream deal. Close to 4 is Andrew's.`

### B19 | "Is there some coordination device that would make this possible? The answer here again is YES!"
- `YES!` in FOCUS, A2's scale.

### B20 | "Interaction between decision-makers like this is central to what we do in microeconomics. Welcome! We have a lot to do."
- `Welcome! We have a lot to do.` writes, INK, full-frame — Part A's last word.
- No next-time card: the notes end here; runs to black.

## On-screen text for review (animator-written)
- `The Trade Line`, `Two Questions` (section titles); `Would Molly accept this trade?` /
  `Would Andrew accept the same trade?`; `Exchange Rate: 1 C = 2.5 S`; `slope = exchange rate`, `+1 C, −2.5 S`,
  `r = 3`, `2 < rate < 4`, `accepts` / `rejects`; the B10/B10b/B14 caption lines (distilled from
  the notes' sentences); `If not feudalism, then what?` (his words).

## Director notes (2026-09-01, editor session — responding to Taylor's render notes; additive, beats above untouched)

1. **Rate swap RESOLVED**: the notes now read 1.5 / 5 / 3 (¶ fills swapped; endowment walk lands
   at (1, 38.5)). One consequence: the one-unit demo (B06b) should run at **1.5 too, not 2.5** —
   the script's "This example so far has been very nice for Molly… not terms Andrew will accept"
   refers to the demo's own rate, so the demo and B09 must share it. New dots: (1, 38.5),
   (2, 37), (3, 35.5), (4, 34), (5, 32.5), (6, 31); caption `+1 C, −1.5 S`; B08's accept-return
   goes to 1.5.

2. **Taylor's render note — one specific trade first, as a point, no line.** Proposed restage of
   the trade-line intro, numbers worked out (all consistent with the staged 1.5/5/3 set):
   - *The offer*: one specific trade, big enough to see — **3 C for 4.5 S**. A TRADE dot lands at
     (3, 35.5) from Molly's endowment (0, 40), with A2-style dashed guides to both axes:
     `+3 C`, `−4.5 S`. No line yet.
   - *Would she accept?* Compare to her self-trade: growing 3 C herself costs 12 S (ghost the
     move along her PPF); this trade costs 4.5 S. Accept.
   - *Rate derivation* (Taylor's second render note): `4.5 S = 3 C` → divide through by 3 — A1's
     op-cost move in the A2 Derivation pattern, numerals transform, letters pinned — landing
     `1.5 S = 1 C`, christened `exchange rate`.
   - *Same trade, Andrew's panel*: (8, 0) → (5, 4.5), guides `−3 C`, `+4.5 S`. His self-trade for
     those 3 C would yield 6 S > 4.5 → reject. Both-sides logic lands on POINTS before any line
     exists.
   - *Then* the existing line beats (B06c/B07/B08) reframed as "every trade at this rate at
     once": one-unit dots trace, line through them, pivot contrast, accept/reject geometry.
   - *Counter and middle as exact trades, derived on screen*: `15 S = 3 C → 5 S = 1 C`;
     `9 S = 3 C → 3 S = 1 C`. The ending trade then derives `10.5 S = 3.5 C → 3 S = 1 C` — the
     SAME rate as the small middle deal. Two different-sized trades, one rate: that invariance is
     the reason we simplify to a rate at all, and it is the B1 bridge (a price is a rate).
   - **Script coupling**: this restage puts Andrew's point-check before the trade line; the
     notes currently introduce the line first (¶15–23). If Taylor adopts it, the notes need a
     reorder pass (editor side, after Wednesday). The current beat order stays teachable as-is
     meanwhile — the point beats can live inside B06b before B06c without contradicting the VO.

## Open questions
- The B16 robustness nudge is staged minimally (one intercept nudge per farmer); could grow into
  a proper tracker sweep if it earns it.
