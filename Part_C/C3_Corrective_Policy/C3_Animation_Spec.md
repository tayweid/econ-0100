# C3 Corrective Policy: animation spec

Scene: `Part_C/C3_Corrective_Policy/C3_Animations.py`, class `C3`. Forms are copied from `Part_C/C1_Externalities/C1_Animations.py` (EXT stacks, MSC/MSB, the two-question close-up language at HEAD) and `Part_C/C2_Taxes_and_Subsidies/C2_Animations.py` (spread close-up geometry, the narrow government bar, opaque strips, dashed `MC + tax` / `MB − tax` lines, the price-axis wedge, icon verdicts). Style rules: `Blocks/_Style_Guide.md` §§2, 3, 6, 8, 9.

This replaces the earlier spec of the same name. Decisions, 2026-10-14:

1. **Set the close-ups up like C2's welfare close-up** (`6.a`: the two price lines, the government's bar between them, the `CS` and `PS` fills that show who wants the trade at those prices), with the pink EXT stack and the two questions added and no welfare amounts on the fills. The bar sits at the same heights on the market and in the close-up at every unit.
2. **Read the market question in two parts, buyer then seller**, each with its own pause, before the verdict.
3. **Show once, on the market, that the policy curve lands on the social curve**: `MC + tax` on `MSC` for the tax, `MB + subsidy` on `MSB` for the subsidy. One beat each, as the explanation of why the wedge stops exactly at Q*.
4. No `MC + tax` or `MB + subsidy` in the close-ups; prices live on the market and in the close-ups, as in C2.

## 1. Model and numbers (C1's market)

MB = 12 − Q/5, MC = 2 + Q/20, equilibrium (40, 4). External cost 2 per ton: MSC = 4 + Q/20, Q* = 32. External benefit 2 per ton: MSB = 14 − Q/5, Q* = 48.

| | Q | P_b | P_s | revenue / cost | external cost / benefit over Q |
|---|---|---|---|---|---|
| corrective tax 2 | 32 | 5.60 | 3.60 | 64 | 64 |
| corrective subsidy 2 | 48 | 2.40 | 4.40 | 96 | 96 |

Close-up units, with the prices of the corrected market:

| unit | MB | MC | EXT | social | buyer: MB vs P_b | seller: MC vs P_s | market | society |
|---|---|---|---|---|---|---|---|---|
| 36th (tax) | 4.80 | 3.80 | 2 | MSC 5.80 | 4.80 < 5.60 | 3.80 > 3.60 | cross | cross, would lose $1 |
| 24th (tax) | 7.20 | 3.20 | 2 | MSC 5.20 | 7.20 > 5.60 | 3.20 < 3.60 | check | check, TS $2 |
| 44th (subsidy) | 3.20 | 4.20 | 2 | MSB 5.20 | 3.20 > 2.40 | 4.20 < 4.40 | check | check, TS $1 |
| 52nd (subsidy, optional) | 1.60 | 4.60 | 2 | MSB 3.60 | 1.60 < 2.40 | 4.60 > 4.40 | cross | cross, would lose $1 |

At every unit the bar between the prices is as tall as the EXT block, which is why the two answers agree.

## 2. Market: the landing beat (tax)

Keep the existing sequence (1.a recap, the planner's two prices in 2.a–2.e, the wedge off the price axis in 3.a) and add one beat after the wedge is stuck at 32 and its two prices are read:

- **3.a.curve · Seen as a cost to sellers.** Opaque green strips (`STRIP_OPACITY = 1.0`, `set_z_index(-1)` so the solid curves stay whole) sweep onto the 40 cost bars from the left, covering the pink EXT strips; the dashed orange `MC + tax` fades in and lies on the solid MSC. The two names at the right end fade out and one `$\mathrm{MSC} = \mathrm{MC} + \mathrm{tax}$` (INK, 0.7) fades in. The wedge, dots and readouts stay. Bottom: `A \$2 higher cost to sellers lifts MC onto MSC: the market stops where society would.` Pause.
- Then the strips and the dashed line fade (the merged name returns to `MSC`) before 3.b, so the welfare beats draw on the C1 market as now.

Subsidy mirror, after 4.g (wedge stuck at 48, prices read):

- **4.g.curve · Seen as a benefit to buyers.** Opaque green strips hang under MB over the 48 tons, covering the pink; dashed teal `MB + subsidy` lies on MSB; names merge to `$\mathrm{MSB} = \mathrm{MB} + \mathrm{subsidy}$`. Bottom: `A \$2 higher benefit to buyers lifts MB onto MSB: the market reaches what society wants.` Pause. Fade back before 4.h.

The dial (3.g) is unchanged: with the wedge driven by the tracker nothing in it needs the strips.

## 3. Close-ups: set up like C2's welfare close-up, read in two parts

Model the C3 close-ups on C2's `6.a` (Welfare With A Tax, first unit): the two price lines with their names and numbers, the government's bar between the prices in the gap, and the surplus fills that show who wants the trade at those prices. The fills carry **names only** (`CS`, `PS`), no welfare amounts; the only amount on a fill is the bar's `tax` / `\$2` (the policy's size). The society side adds C1's pink stack and its one value, as C1 HEAD draws it.

Geometry as C3 already has it (C2's spread layout: `BUYER_LEFT = -1.76`, `SELLER_LEFT = 0.66`, `BAR_WIDTH = 1.1`, `TAX_LEFT = -0.40`, `TAX_WIDTH = 0.80`, base −2.05; use C2's `DETAIL_SCALE = 0.68` rather than 0.55 so the close-ups match C2's). People: Buyer at −1.6, Bystanders at 0, Seller at 1.6. Questions `Will they exchange?` at (−4.8, −3.05) and `Is it good for society?` at (4.8, −3.05), scale 0.60, DEFINITION, on screen from `.values` to `.return`.

Objects, 36th unit under the tax:

- Buyer column: faint teal to MB 4.80, solid edge, `$\$4.80$` outside left, `MB` on the bar.
- Seller column: faint orange to MC 3.80 with `MC` on it, pink `EXT` block 3.80→5.80, solid orange MSC edge at 5.80 with `MSC` just above it inside the column, `$\$3.80$` and `$\$5.80$` outside right (drop C1's pink measure; `$\$5.80$` carries it and the column is busy).
- Price lines: `P_b` at 5.60 and `P_s` at 3.60 spanning x from −2.6 to 1.9, names riding the lines at x = −2.25 (P_b above its line, P_s below), numbers `$\$5.60$` and `$\$3.60$` at the left ends (C2's form).
- The tax: the green bar in the gap from 3.60 to 5.60, between the prices, at `SURPLUS_OPACITY` so it sits with the fills, labeled `tax` / `\$2` on the bar only.
- Fills, when they exist: `CS` in the buyer column from P_b up to MB (teal, `SURPLUS_OPACITY`, name centered on it) and `PS` in the seller column from MC up to P_s (orange). At the 36th unit neither exists, since MB sits below P_b and MC above P_s; at the 24th both do.

Reveal order (pause ids are suggestions; keep C3's existing stems):

1. **`.values`** Bars, numbers, names, pink stack with MSC, people, both questions. Pause.
2. **`.prices`** Both price lines with their names and numbers, and the green bar between them. Pause.
3. **`.buyer`** Part one, the buyer, against `P_b`. If MB clears the price, the `CS` fill rises from the P_b line to the MB edge. If not, a purple bracket at x = −4.25 between the MB and P_b heights (guides from the left edges of their numbers) marks the shortfall. Bottom: `The buyer: value \$4.80 against a price of \$5.60.` Pause.
4. **`.seller`** Part two, the seller, against `P_s`. If MC sits under the price, the `PS` fill rises from the MC edge to the P_s line. If not, the purple bracket between 3.60 and 3.80 at x = −4.25 (guides from the seller's cost, projected across the buyer column skipping the bar and numbers as C2 does, and from `$\$3.60$`). Bottom: `The seller: cost \$3.80 against a price of \$3.60.` Pause.
5. **`.private`** One verdict left of the price numbers: red cross (36th) or green check (24th). Bottom: `Neither side wants this trade at these prices.` or `Both sides want this trade at these prices.` Pause.
6. **`.social.compare`** Guides from MB (segments skipping the bar and the seller column's interior) and from the right edge of `$\$5.80$` to x = 4.25, bracket 4.80→5.80. Pause.
7. **`.social`** Red cross with `DWL \$1` (C1 HEAD's icon-plus-one-value group), or at the 24th a green check with `TS \$2`. Bottom: `Good: this trade would have cost society \$1.` / `Good: this trade is worth \$2 to society.` Pause.
8. **`.return`** Everything close-up fades; the pair carries back to its slice. Pause.

The 24th unit: `The buyer: value \$7.20 against a price of \$5.60.` with the `CS` fill 5.60→7.20; `The seller: cost \$3.20 against a price of \$3.60.` with the `PS` fill 3.20→3.60; check; society check with `TS \$2`.

The 44th unit under the subsidy is the mirror: pink `EXT` on the buyer column 3.20→5.20 under the solid teal MSB edge (`MSB` above it, `$\$5.20$` outside left); `P_s` at 4.40 above `P_b` at 2.40 with the green `subsidy` / `\$2` bar between them; seller column faint to MC 4.20. Buyer part: `CS` fill from 2.40 up to 3.20, bottom `The buyer: value \$3.20 against a price of \$2.40.`; seller part: `PS` fill from 4.20 up to 4.40, bottom `The seller: cost \$4.20 against a price of \$4.40.`; green check, `Both sides want this trade at these prices.`; society: MSB against MC, green check with `TS \$1`, `Good: this trade is worth \$1 to society.` Optional 52nd: no fills, two shortfall brackets, cross, cross with `DWL \$1`.

What the picture says at a glance: the bar between the prices is as tall as the EXT block, so a unit the market keeps is one society wants, and a unit it drops is one society would have lost on.

## 4. Forms to copy exactly

- Numbers `Tex(r'$\$4.80$', color=DEMAND).scale(0.72)`; names `Tex('MB', color=DEMAND).scale(0.58).set_z_index(3)`; price names `Tex(r'$P_b$', color=GUIDE).scale(0.58)`; bar label `VGroup(Tex('tax', color=INK), Tex(r'\$2', color=INK)).arrange(DOWN, buff=0.06).scale(0.55).set_z_index(3)`; merged market name `Tex(r'$\mathrm{MSC} = \mathrm{MC} + \mathrm{tax}$', color=INK).scale(0.7)`.
- Guides `DashedLine(..., color=TOTAL, stroke_width=1.4)`, brackets `Line(..., color=TOTAL, stroke_width=3)` at x = ±4.25; verdicts: `VMobject(color=EFFICIENT, stroke_width=5).set_points_as_corners([[-0.28, 0, 0], [-0.08, -0.20, 0], [0.32, 0.27, 0]]).scale(0.85)` and `VGroup(Line([-0.22, -0.22, 0], [0.22, 0.22, 0], color=GUIDE, stroke_width=5), Line([-0.22, 0.22, 0], [0.22, -0.22, 0], color=GUIDE, stroke_width=5)).scale(0.85)`; society group `VGroup(icon, Tex(r'DWL \$1', color=INK)).arrange(DOWN, buff=0.16).scale(0.70)`.
- Bottom lines `Tex(..., color=DEFINITION).scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)`, measured width under 11.8 units.
- Opacities: the green bar and the landing-beat strips opaque (the policy being introduced); the government's money in welfare beats at `SURPLUS_OPACITY` like CS and PS.
- Spheres added and removed directly, never faded; one flat `construct()`; literal `self.pause('id')`; `fixed(...)` on every flat object; updaters read attributes on the mobject; never morph text or dashed lines of different length (crossfade); a `FadeOut` inside a `Succession` restores its object when its turn ends.

## 5. Checking without the viewer

```bash
PYTHONPATH=/Applications/ManimLive.app/Contents/Resources/python \
/Users/taylorjweidman/.local/share/uv/claerbout/maniml/bin/python -m maniml C3_Animations.py C3 --export-checkpoints
```

Run it from a scratch copy of the block folder with `_Assets` and `Sim` symlinked beside it, never inside the repo (it writes `media/`). One PNG per play and per pause; the bumper adds ten hidden plays before the first beat.
