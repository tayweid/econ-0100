# E1 animation review

Separate working beat sheet for `E1_Animation.py`, scene `EpisodeE1`, November 4, 2026. The author’s notes remain untouched. These beats supersede the corresponding older storyboard comments in `E1_Notes.md`; the remaining lesson stays as written there. Spoken notes still need reconciliation after the author’s prose pass.

## Conventions and model

Keep the semester’s graphite background, azure topic titles, fixed-size gold teaching lines, white curve names, red tracing guides and readouts, grey contextual marks, and shared firm palette. The production function remains $Q = 10\sqrt{L}$, with labor measured in hours, a \$100 hourly wage, and \$1,000 fixed cost. Thus $L = Q^2/100$, variable cost is $Q^2$, and total cost is $1,000 + Q^2$.

Reuse B2′s axis-coordinate polygons: adjoining rectangles, colored one-point outlines, and 35% colored fill. Unselected choices use B2′s grey 10% fill and a grey one-point outline at 35% opacity. The close-up uses individual units. The overview uses twenty five-unit bands, keeping boundaries visible without generating a hundred bars. Each production bar’s upper-right corner lies on F; each cost bar’s upper-right corner lies on its cost curve. Band heights and lengths are sampled levels, not sums of the rectangle areas. Geometry updates in place during zooms.

## 1.c–1.g · Fill the market-structures matrix

Keep the full-size centered matrix and the title “Market Structures” unchanged throughout. Reveal Perfect Competition, Monopoly, Monopolistic Competition, then Oligopoly in their cells, retaining earlier entries. Move the same close-fitting selection box between them with smooth easing. Keep the existing pauses 1.c–1.g. No side checklist, shrinking, repositioning, or title swaps.

## 2.a–2.g · Read output back to labor

2.a · Retain the title “Costs From The Production Function” and add the grey subtitle “One example of a production function with diminishing marginal product.” Keep it through 2.k, then replace it with the wage at 2.l.

2.b · Choose 20 output units on the vertical axis, draw the red guide across to F, then down to 4 labor hours. Bottom: “Choose an output quantity; find the labor hours it requires.”

2.c · One output tracker moves 20 → 30 → 20; the guides, dot, and both numbers remain attached. Bottom: “Increasing output means we need more inputs, either from labor or capital.”

2.d · Keep the first point. Double output to 40. Reveal the grey Q interval and +20 with the across guide, then the grey L interval and +12 with the down guide and 16-hour readout. Bottom: “Doubling output from 20 to 40 requires four times the labor.”

2.e · Keep both earlier points. Add another 20 output units, reaching 60. Reveal its grey Q interval and +20 with the across guide, then its grey L interval and +20 with the down guide and 36-hour readout. Bottom: “Another 20 units require 20 more labor hours.”

2.f · Keep both grey interval pairs, already revealed in 2.d and 2.e. Lines sit 0.14 scene units outside the axes, with small end gaps. The grey difference numbers have their own row/column, clear of the red cumulative readouts. Bottom: “More output requires increasingly large additions to labor.”

2.g · Pulse each pair without resizing or relocating it. Bottom: “Equal additions to output require increasingly more labor.”

2.h–2.i · Preserve the wage equation, temporary capital term, and pauses already in the animation.

## 2.j–2.p · From hours to costs

2.j · Clear the comparison marks and show a six-unit output window, with labor from 0 to 0.36 hours. Slide a red point and red quantity number up the curve from 0 to 5 over 3.5 seconds; its dashed guides to both axes and hours readout follow. Use smooth easing for this sweep and its continuation. Reuse a fixed pool of dash segments so the guides grow safely from zero without rebuilding their object hierarchy. Reveal each adjoining pink rectangle as the point reaches its unit. Hold at 5. Bottom: “Start small: how much labor does each output level require?”

2.k · After the hold at 5, zoom out to a window of 100 output units and 100 labor hours while retaining the red point. Continue its sweep from 5 to 100 over four seconds, revealing each band as it is reached. Hide the F label during this sweep so the quantity number has room, then restore it as the temporary marks fade. Cap the view at twenty bars, grouping five units per band at the full scale. Keep F above the fills. Bottom: “Each additional unit takes more hours than the last.”

2.l · Return to the first five units for a legible mapping. Resting production bars become faint grey. Reveal the cost axes on the right. Replace the equation row with one grey subtitle: “Wage: \$100 per hour”. The initial right window is six output units and \$1,200. Bottom: “The same labor hours become variable cost at \$100 per hour.”

2.m · Color the first production rectangle pink. Show 1 unit and 0.01 hours in red with the dashed guide. Place the grey fixed-cost base and copy the labor rectangle into the pink variable-cost cap of the first cost bar; total cost reads 1,001. The \$1 cap is small relative to \$1,000 fixed cost, as the model requires. No worked algebra. Bottom: “One unit: \$1 in labor cost, plus \$1,000 in fixed cost.”

2.n · Add the second rectangle while retaining the first on both graphs. The second cost bar also includes its grey fixed-cost base. Move the readouts to 2 units, 0.04 hours and 1,004 dollars. Bottom: “Two units: \$4 in labor cost, plus \$1,000 in fixed cost.”

2.o · Add units 3, 4 and 5 in sequence with fixed cost included each time. Continue to the wider output range while both scales adjust with the arriving quantities. The cost scale follows the displayed output window and leaves headroom above total cost, settling at \$12,000. Retain at most twenty bands per graph. There is no separate rescaling play after the bars are complete. Bottom: “More output needs more labor, so variable cost rises.”

2.p · Draw TC and the horizontal FC line together across the already stacked cost bars. Neither the bars nor the scales move again. Bottom: “Total cost includes fixed cost and variable cost.”

## 3.a–3.d · Preserve the pan and explain variable cost

3.a · Keep the two-second leftward pan, changing the title to “Cost Curves”. The production graph leaves and the cost graph takes its place. All bars fade while moving with their graphs during the pan; TC and FC remain visible together.

3.b · FC is already on the graph. Only the teaching line enters: “Fixed costs, like rent, don’t vary with inputs.”

3.c · Restore twenty faint grey cost bars as context. Keep every bar stationary. Switch the highlight to the current five-unit interval, with a grey fixed-cost base and pink variable-cost portion; no rectangle slides along the axis. Keep the existing quantity motion 70 → 95 → 40. A red dot at TC, a horizontal dashed guide to the dollar axis, the total-cost readout, and the horizontal-axis quantity readout all follow that same tracker. Bottom: “Variable costs are the costs that do change with inputs.”

3.d · Retain the stationary contextual bars and the highlighted FC/VC stack. Fade only the temporary readouts and VC label. Add the divider and equation TC = FC + VC, with total on the left. Do not draw a separate VC curve here. Keep that order through TC/Q = FC/Q + VC/Q and ATC = AFC + AVC. Fade the bars when the average-cost graph enters at 3.f; introduce the separate VC curve only when it is used to trace AVC in 3.g.

## 3.k–3.m · Marginal cost bands

3.k · Retain the TC rider and the rising orange bars, with twenty adjoining outlined bands rather than 99 separately rebuilt strips. Each five-unit band’s height is the change in TC divided by five, so the quadratic model puts MC through its midpoint. Bottom: “How much does total cost rise per additional unit?”

3.m · Clear the rider, draw the existing MC line through the band midpoints, and then fade the bands. Continue the existing MC/ATC comparison and the remainder of the lesson.

## Wage-dependent cost curves

At a wage of \$100 per hour, MC = 2Q, AVC = Q, and ATC = Q + 1,000/Q. Cost axes extend to \$12,000; per-unit axes to \$240. The minimum of ATC is at Q = √1,000, about 31.6, so the below-minimum demonstration holds at 20 units. Keep the ATC and AVC endpoint labels separated. The illustrative marginal-revenue panels use the same MC and proportional vertical scales; the separate Part C market recap retains its original model.
