# Episode B2 · Supply

Current animation record (2026-09-16): this storyboard follows `03_Code.py`, including review changes. Keep it synchronized with each animation edit. The kilogram units and bar-cost explanation are now marked in `01_Notes.md` by the editor. Broader animation/narration reconciliation remains deferred; this file records the implemented farm callback, exercises, individual-bar PS introduction, flat bars, synchronized focus/return, and removal of the old one-ton recap.

Styling: CMU serif for titles, definitions, calculations, and exercise cards; CMU sans for the small axis-unit captions. White P stays left of each vertical axis and white Q below each horizontal axis. Red belongs to price/quantity readouts and guides. Every bottom definition uses the same text size as 2.b's Individual Quantity Supplied line: `DEFINITION_SCALE = 0.7443`, centered horizontally with a 0.05-unit bottom margin. Keep that size even for shorter definitions. Remove the old definition before fading the new one in, so they never overlap. Keep definitions and calculations, but leave spoken explanations off the screen. The unplanted farm area is blank. Keep the same visual bar widths on every graph. On the supply graphs, each existing 0.1-wide geometry slice now represents **1 kg**. Graph coordinates remain unchanged in the code; `KG_PER_GRAPH_UNIT = 10` converts quantity readouts and tick labels to kilograms. All quantities stated below are displayed kilograms, not internal graph coordinates. Prices are dollars per kg; the notes establish one market day. No Part A rescaling or worksheet changes belong to this pass.

Side calculations: fade in a subtle grey vertical divider, six units tall and centered vertically on the page. Place it 0.35 units beyond the rightmost horizontal-axis label, including “kilograms,” so those labels stay entirely on the graph side. Center each calculation block horizontally between the divider and the right margin, retaining left alignment within multi-step algebra. Use this layout for quantity, marginal cost, revenue/cost/PS, and the triangle calculation. Fade the divider away when that calculation sequence ends. Keep the expanded numerical area formula centered by sliding its existing prefix into position as the yellow measurements arrive.

## 0.a · Open the episode
- Reuse B1's shared `bumper_raster`, `flicker`, and `bumper_title` helpers for MICROECONOMICS and Part B | Episode 2, then fade in “Supply: a simple way to organize costs.” Retain the 0.a pause and 15 fps playback. The bumper is the exception to keeping the choreography flat in `construct()`.

## 1.a · Recall the buyer’s decision
- Show “Last time…” above B1’s individual demand graph. Use little grey bars below the price and teal CS slices above it. Keep price generic: red “Price” on the vertical side and red $Q_d$ under the dashed quantity drop, with no numerical values. Reveal four gold terms with their white descriptions underneath: Preferences — “Rank the available choices.”; Quantity Demanded — “The quantity a buyer is willing and able to buy at a given price.”; Marginal Benefit — “Is another purchase worth making?”; Consumer Surplus — “The buyer's value above the price.” Split the Quantity Demanded description across two short lines and vertically center the four entries beside the graph. Use CMU serif throughout.

## 2.a · Return to Molly’s farm
- Ask “How much would Molly grow?” Keep the graph on B1’s left stage and Molly’s farm on the right, with its name in white. Green spinach occupies part of the fixed farm outline; leave the rest blank. Center the spinach label below its changing area. Offer $4 with a red ValueTracker readout. Hold the quantity label until the graph tracing in the next beat is complete.

## 2.b · Name and plot her first answer
- Fade in the full-width definition of Individual Quantity Supplied at the tiny bottom margin, with the term gold and the words white. First fade in the horizontal dashed guide and point at (20, 4); next extend the vertical dashed guide down from that point to the quantity axis; only then fade in red $Q_s=20$. Keep white P and Q as axis names. Place sans-serif “dollars per kg” beside P and “kilograms” beside Q, clear of the title, tick numerals, and moving quantity readouts. Omit the former 2.c farm-boundary highlight and explanatory text.

## 2.d · Raise the price
- Roll the same price tracker from $4 to $6. Expand spinach within the fixed farm, with its label following the area's center. Move the red graph dot, both dashed guides, and the $Q_s$ readout together to (40, 6). Retain the first observed point.

## 2.e · Lower the price
- Roll price to $2 and quantity to zero with the red dot, guides, and quantity readout attached. Leave the blank farm outline visible; shrink away the spinach allocation and its label. Add (0, 2).

## 2.f · Name the collection of answers
- Freeze the updaters, then fade out the moving price and quantity readouts, dot, and guides. Connect the three observed answers. Replace the old definition with Individual Supply Curve, removing the old line before fading in the new one.

## 2.g · Name the upward relationship
- Replace the definition with Law of Supply: the quantity supplied of a good rises with its price. Retain the points, curve, and farm.

## 2.h · Keep the line and reveal possible quantities
- Fade the farm and observed points away. Keep B1’s graph-left/math-right layout. Show $P=2+Q_s/10$ above the supply line, label it S, and show faint grey one-kilogram bars with flat tops at each interval's midpoint cost. Start the line at (0, 2); do not extend into negative quantity.

## 3.a · Read quantity at $5
- Show red Price $5, then horizontal and vertical dashed guides and a red dot at (30, 5). Put red $Q_s=?$ below the axis and temporarily hide the answer’s tick numeral. Pause before calculating.

## 3.b · Solve and return the quantity
- Carry a copy of the red input into $5=2+Q_s/10$. Reveal $Q_s=10(5-2)$, then $Q_s=30$. Carry the resulting 30 back to the quantity axis. Keep the guides visible.

## 3.c · Read quantity at $4.50
- Remove the old calculation and answer, then roll the same price tracker to $4.50 with both dashed guides and the dot still attached. Show $Q_s=?$ at 25 kg.

## 3.d · Solve for 25 kg
- Carry 4.50 into the calculation, reveal $Q_s=25$, and return that answer to the graph. Use $4.50=2+Q_s/10$, then $Q_s=10(4.50-2)=25$.

## 3.e · Reverse the question at 10 kg
- Ask “Which spinach is worth growing?” Set red $Q_s=10$, trace up to supply and across toward price, and show red $MC=?$. Use the dot and dashed guides without an extra yellow mark. Fade in the Marginal Cost definition before doing the arithmetic.

## 3.f · Read marginal cost at 10 kg
- Carry 10 into $P=2+10/10$, reveal $P=3$, and carry $3 back to the red MC readout. Use Q=20 later as a graphical stopping point, without a second algebra walkthrough.

## 3.i · Compare the next addition with a $4 price
- Fix the red price line at $4. Keep the red point at Q=10 on supply. Show only MC < P beside the graph; explain the decision aloud.

## 3.j · Reach the stopping point
- Move the red point and its quantity guide to Q=20. Read MC = price = $4 at (20, 4), without another substitution.

## 3.k · Go beyond the stopping point
- Move to Q=30. Show only MC > P beside the graph; explain the decision aloud.

## 3.l · Return to 20 kg
- Return the point to (20, 4), restore $Q_s=20$, and keep the chosen quantity marked.

## 3.m · Connect money costs to opportunity cost
- Remove the comparison and math divider. Replace the definition with Marginal Cost Curve. Bring back Molly’s farm in its original position: white name and outline, green spinach, unused land blank, and the Spinach label following the middle of its area. Keep the supply curve and faint quantity bars visible.
- Move one price tracker from $4 → $6 → $3 → $4. Keep the red price label, horizontal guide, selected point, vertical guide, and $Q_s$ readout attached throughout. The spinach area expands from 20 to 40 kg, contracts to 10, and returns to 20, linking the graph to land and labor moving away from or back to other uses. Add no explanatory text stack. Park at $4 and 20 kg.

## 3.n · Pause for Exercise B2 Q1
- Freeze the farm and graph together, then dim the stage. Show $P=2+\frac{Q_s}{10}$ alone as a centered math block. Below it, ask “What is quantity supplied at 10 galleons?” and “What is marginal cost at 9 pasties?” Match the exercise file exactly. Left-align the heading within the box and slightly indent the questions. Keep CMU serif throughout; omit the setup sentence and “Fractional pasties…” line. Give no answers.

## 4.a · Offer $5
- Restore the stage, fade out the farm, ask “What does Molly gain?”, and offer $5. Keep $P=2+Q_s/10$ and the faint possible quantities visible. Add no yellow interval highlight.

## 4.b.1–4.d.10 · Introduce revenue, cost, and PS on individual bars
- Walk through the ten existing one-kilogram bars from Q=0 to Q=10, in order. Keep the selected grey bar, vertical price axis with ticks and P/unit labels, full red price line and readout, and question title visible. Fade out the horizontal axis and its labels, supply curve, other bars, and completed areas. As supply fades, fade in a horizontal cost line across the selected bar.
- In that same 0.8-second focus move, widen the selected bar to three times its resting width as the surrounding graph fades out. The orange horizontal MC line fades in and widens with the bar. Fade in a small white “1 kg” cue below the widened bar in the same play, with no extra pause. Anchor the bar at its original left edge inside the graph and keep its original baseline and vertical scale. Keep the flat cost height at $2+(Q_{left}+Q_{right})/20$ throughout; only the width changes when shrinking back. Midpoint bars preserve the area under this linear supply curve without requiring a calculation on screen.
- Reveal the full revenue outline up to the existing price line and a white Revenue label just above-right of the bar, clear of the vertical-axis ticks. Pause at `4.b.N`. Keep the red price readout at the vertical axis. Omit the full horizontal axis and per-bar dollar totals; retain the small “1 kg” cue beneath the focused bar at scale 0.7.
- Fade in green cost below the horizontal line, its Cost label, and the red MC label at the line. Pause at `4.c.N` before revealing surplus.
- Fade in orange PS above cost and below price, with a matching PS label. On the first bar, show the Producer Surplus definition after the area appears, and keep it visible through the remaining bars and triangle explanation. Revenue, cost, and PS are all introduced here through labels and areas. Pause at `4.d.N`.
- Stay on the first enlarged bar and move one price tracker through $5 → $3 → $1.50 → $4 → $5. Pause at `4.d.1.price-low` ($3), `4.d.1.no-sale` ($1.50), `4.d.1.price-high` ($4), and `4.d.1.price-reset` ($5). Revenue height, the full graph price line/readout, and PS move together while cost stays fixed. Below cost, leave the bar grey and hide Revenue, Cost, and PS areas/labels; keep the vertical axis, price line, and MC line/readout visible. Restore the areas when price covers cost again.
- Remove the close-up labels and “1 kg” cue, then use one 0.8-second return move: shrink the selected bar and its two areas back into place while the full graph and all other bars fade back in. Keep the cost boundary flat; the orange MC line shrinks and fades out in that same move. Preserve the completed cost and PS areas. Pause at `4.return.N` for bars 1–9 before selecting the next bar. After bar 10 returns, continue directly to the remaining bars. No helper functions and no batch cost-first fill across different bars.

Retired beats: `4.b`, `4.c`, `4.d`, and `4.return.10`. Remove the one-ton brace, Revenue $5 / Cost $2.50 / PS $2.50 recap, and repeated definition reveal. The first-bar view introduces the concepts; the later triangle still calculates total PS.

## 4.e · Reveal cost, then surplus, for each remaining bar
- Continue directly across Q=10 to 30, working left to right one narrow bar at a time: fade in its revenue outline and cost, then its PS, before moving to the next bar. Retain the earlier completed bars and the PS definition. Use flat midpoint cost boundaries here too. Add no running tally; calculate the whole triangle below.

## 4.g · Mark where production stops
- Keep the $5 price readout. Fade in a red dashed horizontal guide to (30, 5) and the point, then the vertical guide down to quantity, then red $Q_s=?$. Hide the tick numeral 30 until the calculation gives the answer. Show MC = P above-left of the dot, clear of the curve and in front. Retain the completed bars and the faint unchosen quantities.

## 4.g.1 · Find the triangle's quantity from the supply equation
- Reuse the established divider and centered right-hand math layout. Carry a copy of the red price 5 into $5=2+Q_s/10$, then reveal $Q_s=10(5-2)$ and $Q_s=30$ in order. Price and quantity stay red in the calculation. Carry the resulting 30 back to the quantity axis, replacing the question mark and restoring its tick numeral. Keep both dashed guides and the point visible throughout.

## 4.h · Recognize the triangle traced by the bars
- Fade out the quantity calculation and MC = P label, leaving the divider. Outline the triangle between the straight supply curve and price. Keep the narrow bars' flat boundaries visible; do not tilt or reshape them. Their midpoint areas sum to the triangle's area for this linear supply curve.

## 4.i · Set up the area equation
- Put orange PS and white $=\frac12$ on the right, followed by yellow h and b. Keep this prefix throughout the calculation.

## 4.j · Locate the intercept in the equation and graph
- Color the 2 in $P=2+Q_s/10$ yellow. Carry a copy to a yellow 2 beside the vertical axis at the supply intercept, with a yellow point at (0, 2). Hide the ordinary tick numeral there. Keep the area formula above the forthcoming height calculation.

## 4.j.1 · Height is price minus the intercept
- Fade in the yellow height segment from 2 to 5, above all fills. Below the area formula on the right, assemble $h=5-2$: copy red 5 from the price readout and yellow 2 from the intercept label. Keep h yellow and the subtraction sign white. Pause before evaluating the difference.

## 4.j.2 · Carry the height back to the triangle
- Reveal yellow $h=3$ beneath the subtraction, then carry the resulting 3 to a yellow $h=3$ label beside the height segment. Keep the subtraction visible for this pause, making clear that the height is the gap from the intercept to the price.

## 4.k · Measure the base
- Fade out the height calculation and temporary intercept point/label; restore the equation's 2 to white and its ordinary axis tick. Keep the measured height and its label. Fade in a yellow base segment for Q=0 to 30, and carry a copy of the solved quantity into yellow $b=30$. Keep the red price and quantity guides above the areas.

## 4.l · Fill in the equation
- Move copies of the yellow measurements into the existing equation: $PS=\frac12(3)(30)=\$45.00$. The height was just derived as $5-2=3$. Do not fade out and rebuild the same prefix.

## 5.a · Pause for Exercise B2 Q2
- Dim the stage. Show $P=2+\frac{Q_s}{10}$ alone as a centered math block, then ask “What is producer surplus at 10 galleons?” Match the exercise file exactly. Use the same left-aligned heading and slightly indented CMU-serif question as Q1. Give no answer on the exercise card.

## 6.a · Compare two sellers at one price
- Ask “What happens when we consider everyone?” Show Molly, Andrew, and a third graph for their combined quantities, aligned to the same price scale. Lower the graphs and their headings slightly to leave more space below the title. Use Molly’s $P=2+Q_s/10$ and Andrew’s $P=2+Q_s/5$. Hold a red horizontal guide at $4 across the graphs; reveal their quantities 20 and 10 kg.

## 6.b · Add quantities at $4
- Carry copies of 20 and 10 into $20+10$ directly below Q=30 on the combined graph's quantity axis. Pause with the addition in place; show no equals sign or question mark.

## 6.b.1 · Reveal the first sum
- Combine the addition into $Q_s=30$ in that same axis position, and mark (30, 4) with its vertical guide.

## 6.c · Raise the common price to $6
- Roll the shared price tracker to $6 with both individual guides attached. Copy 40 and 20 into $40+20$ directly below Q=60 on the combined graph's quantity axis, and pause there. Retain the previous combined point.

## 6.d · Add quantities at $6
- Combine the addition into $Q_s=60$ in that same axis position, mark (60, 6), and draw the combined curve for these two sellers. Keep it explicitly labeled as Molly + Andrew.

## 6.e · Name market supply
- Fade in the Market Supply definition: the sum of sellers’ individual quantities supplied at each price. Point to the horizontal addition at a common price.

## 7.a · Identify surplus on the combined-sellers graph
- Return the shared price tracker to $4, keeping both sellers’ guides and readouts attached. Restore the combined quantity 30 kg and briefly shade PS above the existing combined supply curve and below price, retaining slice divisions. Replace the definition with the area rule for Producer Surplus. Introduce no new equation, numerical example, running tally, or area calculation.

## 8.a · Ask where the common price comes from
- Ask “What determines the price?” Show demand and supply side by side with matching P/Q scales, teal demand and orange supply, white axis names, and “Next time…” in gold at the bottom. Show narrow teal CS slices above price and below demand, and orange PS slices above supply and below price. Keep expenditure and costs as faint grey bars beneath the surplus areas, with other possible quantities also grey. A shared red dashed price line moves up, down, and back a little using one ValueTracker. The surplus slices expand and contract with the chosen quantities, including a partial slice at each moving endpoint. Keep curves and red guides above the fills. Dots and vertical guides stay attached to the two curves; red $Q_d$ and $Q_s$ labels move along their quantity axes in opposite directions. Keep this qualitative, without equations or numerical readouts, and finish with both graphs on screen.
