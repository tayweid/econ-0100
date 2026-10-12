// Exported from Plass — exact on typst 0.14.2
#set page(paper: "us-letter", margin: (top: 1in, right: 0.5in, bottom: 1in, left: 0.5in), numbering: "1", number-align: center)
#set par(justify: true, leading: 10.215pt, spacing: 21.465pt)
#set list(spacing: 13.340pt)
#set enum(spacing: 13.340pt)
#set grid.cell(breakable: false)
#show heading.where(level: 1): set text(size: 23.750pt)
#show heading.where(level: 1): set block(above: 26.391pt, below: 25.105pt)
#show heading.where(level: 1): set par(leading: 13.471pt)
#show heading.where(level: 2): set text(size: 17.500pt)
#show heading.where(level: 2): set block(above: 44.650pt, below: 19.937pt)
#show heading.where(level: 2): set par(leading: 9.926pt)
#show heading.where(level: 3): set text(size: 14.375pt)
#show heading.where(level: 3): set block(above: 38.410pt, below: 18.473pt)
#show heading.where(level: 3): set par(leading: 8.153pt)
#show heading.where(level: 4): set text(size: 14.375pt)
#show heading.where(level: 4): set block(above: 38.410pt, below: 18.473pt)
#show heading.where(level: 4): set par(leading: 8.153pt)
#show heading.where(level: 5): set text(size: 14.375pt)
#show heading.where(level: 5): set block(above: 38.410pt, below: 18.473pt)
#show heading.where(level: 5): set par(leading: 8.153pt)
#show heading.where(level: 6): set text(size: 14.375pt)
#show heading.where(level: 6): set block(above: 38.410pt, below: 18.473pt)
#show heading.where(level: 6): set par(leading: 8.153pt)
#show raw.where(block: false): set text(font: "DejaVu Sans Mono", size: 10.000pt)
#show math.equation.where(block: true): set block(above: 21.490pt, below: 23.702pt)
#set text(size: 12.5pt, font: "New Computer Modern", hyphenate: true)
#set math.equation(numbering: "(1)")

== Episode C2 | Taxes and Subsidies

// plass:comment
// | Animation storyboard for C2_Animations.py, scene C2. Drafted 2026-10-09 to follow C1_Animations.py directly; revised 2026-10-12 to Taylor's notes of 2026-10-11 (compact close-ups with the numbers outside the bars and the names on them, the seller and buyer equivalence shown by the animation alone, incidence as two graphs on one screen) and to C1 at HEAD fcf3cbb (one decision language in every paired welfare close-up). Taylor's spoken notes stay in 01_Notes.typ; the quote blocks below are animation directions in playback order, not replacement prose. The old animation (03_Code.py, the 2022 Taxes scene) is untouched and supplied the flow: a tax on one exchange, a tax on sellers, a tax on buyers, the same outcome, the tax wedge slid in from the left, welfare areas, changing the tax, incidence under different slopes, then the subsidy as the mirror of the wedge.
// | References: C1_Animations.py for the market, the compact one-ton close-up (3.f.36 for the geometry; 1.c, 1.f and 3.f.36 at HEAD for the two questions, the icon verdicts and the single welfare value), the yellow selection box, the carry-out and return zooms, the grey DWL slices, and the side equation with a grey divider; B5_Animation.py for tracker-driven curves and rolling readouts; _Style_Guide.md §5 for the tax model invariants (wedge parked left of the axes, slid in until it gets stuck; incidence stacked off-axis, buyer share teal, seller share orange).
// | Model: the C1 spinach market, MB = 12 − Q/5 and MC = 2 + Q/20, Q in tons, prices in dollars per ton, equilibrium Q = 40 and P = 4. A 2-dollar tax: Q = 32, buyers pay 5.60, sellers receive 3.60, revenue 64, DWL 8, incidence 1.60 on buyers and 0.40 on sellers. A 5-dollar tax: Q = 20, 8 and 3, revenue 100, DWL 50. A 2-dollar subsidy: Q = 48, sellers receive 4.40, buyers pay 2.40, government cost 96, DWL 8. Close-up tons: the 1st (MB 12, MC 2) in 2.a and 6.a; the 36th (MB 4.80, MC 3.80, TS +1), the exchange the tax removes, in 6.c (LOST_TON = 35 as an index); the 44th (MB 3.20, MC 4.20, TS −1), the exchange the subsidy adds, in 9.d (ADDED_TON = 43; the lot is added_lots[ADDED_TON − MARKET_Q] wherever the pair is lifted out, returned and rejoined). The 44th replaces the 48th (MB 2.40, MC 4.40) of the first draft.
// | Conventions carried from C1: titles name the topic with every word capitalized; grey CMU Sans subtitles at scale 0.6, 0.10 below the title; one yellow (DEFINITION) line in the bottom strip at scale 0.7443, centered, its measured width under 11.8 units: a question, a definition, a formula or a short takeaway, never a restatement of what the readouts show, and none where a beat lists no bottom text; one-ton bars with a 0.08 gap, faint base 0.16, strong fills 0.65; price readouts on the vertical axis; thin yellow selection box, pause with no bottom text, then zoom; spheres fully opaque with depth testing, added and removed directly, never faded: Buyer teal at x = −1.45, Seller orange at 1.45, and here a green Government sphere at 0 between them, labeled Government, standing where C1's Bystanders stood, so society is everyone on screen and tax money is a transfer inside it. Tons beyond the taxed quantity fade to 0.05, as in C1.
// | Compact close-up convention (C1's 3.f.36): buyer column x from −1.16 to −0.06, seller column from 0.06 to 1.16, base y = −2.05; the first ton at 0.35 per dollar, the detail tons at 0.68; faint base fill with a 3-wide edge in the bar's color at the value; numbers at 0.72 outside the bars at their boundary heights (buyer left, buff 0.25; seller right, buff 0.25, or 0.45 when the green measure sits beside the bar); the names MB and MC at 0.58 on the bars, above or below their edge so they never land on a price line, a strong fill, a tax slice or the grey bar (2.a and 6.a: MB above, MC below; 6.c: both above; 9.d: both below, and MC ends inside the grey bar, as C1's EXT does); price lines red (GUIDE, stroke 2) from x = −2.0 to 1.3 with the name at 0.58 at x = −1.65 and the number at 0.72 left of the line's end; fill labels name and amount together in white at 0.58 centered on the fill (CS $8, PS $2, tax $2, PS $1.60, CS $6.40). The first-ton close-ups 2.a and 6.a are compact in this way but carry no questions.
// | Two-question close-ups (6.c and 9.d), C1 HEAD's language: the yellow questions Will they exchange? at (−4.8, −3.05) and Is it good for society? at (4.8, −3.05), scale 0.60, level with the people's names and clear of them, on screen from .values to .return; purple (TOTAL) dashed guides (1.4) and 3-wide brackets at x = ±3.65; the market side pairs MB with P_b and MC with P_s (MC projected from the seller bar's left edge across the buyer column, the guide skipping the P_s number), the society side pairs MB with MC (the MB guide in two segments that skip the seller column's interior, the MC guide from the MC number's right edge); the green dashed measure at x = 1.45 ($2 tax or $2 subsidy, GOV, stroke 2.5) shows the wedge beside the bars from .private.compare and fades at .social.compare, so no guide crosses it; verdicts are icons only, a green check (EFFICIENT) for yes and a red cross (GUIDE) for no, with no Yes/No words and no inequalities anywhere; the market icon at 0.85 sits left of the brackets at the midpoint of the two market brackets, and the society answer stacks its icon over one welfare value at 0.70 right of its bracket (TS $1 in purple for a beneficial trade, DWL $1 in white for a harmful one); the grey DWL bar (0.8) is the part of the taller bar above the shorter, in 6.c the buyer column from 3.80 to 4.80 and in 9.d the seller column from 3.20 to 4.20; rhythm .values → .private.compare → .private → .social.compare → .loss → .return, the return carrying the pair and its grey bar back to its slice with the section subtitle restored and no bottom text.
// | Tax conventions in C2: tax money is GOV green. In the first-ton close-up the tax is a green slice of height 2 with a white tax $2 label: it stacks on the seller's cost in 2.b, carves the top off the buyer's value in 2.c, and becomes the band across both columns between the two prices in 2.d and 6.a; the single price dims to a reference through 2.b and 2.c and leaves a grey dashed ghost at 4 when it splits in 2.d. The two price names sit outside the pair of price lines, the upper name above the upper line and the lower name below the lower (P_b above and P_s below for the tax, P_s above and P_b below for the subsidy), so neither crosses the ghost or the MC guide. On the market the tax is a green strip of height 2 on every cost bar (3.a), and the same strips fly to hang under the demand curve (4.a); the taxed curve is the original's color, dashed, labeled MC + tax at its right end or MB − tax tucked under its upper stretch, with no intercept numeral. Revenue is the green rectangle between the two prices over the exchanged tons, labeled Tax revenue in white. The wedge is a thick green segment with small end caps and a green $2 tax label, left of it while it slides and above its top end to the right once stuck; for a subsidy it is reversed, parked right of the axes and labeled $2 subsidy to its right. Incidence is two small graphs on one screen (section 8), the left fixed and the right driven by slope trackers, each with a grey dashed reference at the untaxed price and the incidence stacked off-axis at Q = −20. The CS and PS fills rest from 3.a until 6.b, so the strips and the wedge read cleanly; the faint cost bars stay.
// | Choices left for Taylor: the 44th ton rather than the 48th as the subsidy close-up (MB 3.20 against P_b 2.40 and MC 4.20 against P_s 4.40 make the market's answer a clear yes, where the 48th sits on the indifferent edge; its TS −1 mirrors the 36th's +1); the green check keeping C1's EFFICIENT glyph for continuity although it shares GOV's hue, with the Government sphere and the green measure on the same screen; the grey dashed ghosts in 8.b and 8.c of the curve before it rotates (demand, then supply), each fading when the next question arrives; the price names sitting outside the pair of price lines rather than both above their lines; and the first-ton close-ups 2.a and 6.a being compact but carrying no questions, since the two questions belong to the DWL tons alone.
// /plass:comment

=== 0 | Bumper

#quote(block: true)[
  0.a · The shared bumper: raster MICROECONOMICS, flicker, then Part C | Episode 2 beneath it, and the italic thesis in grey: Governments can change your behavior. Pause, then clear.

]

=== 1 | Last time: the market

#quote(block: true)[
  1.a · Title: Competitive Equilibrium. Subtitle: A market without externalities. The C1 opening market, unchanged: axes 0–60 tons by 0–13 dollars, P and \$/ton beside the top of the vertical axis, Q and tons under the end of the horizontal, D / MB from 12 and S / MC from 2 with their intercept numerals, the red equilibrium dot at (40, 4) with dashed guides, P\* = 4 on the axis and Q = 40 below, faint orange cost bars under MC for the 40 tons. Then PS with its label, then CS with its label, both short white labels at their triangles’ centroids. Pause. From here one group carries the whole market out of and back into every close-up.

]

=== 2 | A tax on one exchange

#quote(block: true)[
  2.a.select → 2.a.values → 2.a · Title: A Per-Unit Tax. Subtitle: The government collects \$2 on each ton exchanged. With the title, fade in a copy of the first slice (the first ton, Q = 0 to 1: faint cost base, strong PS and CS, hard MB and MC edges) and one thin yellow box around it; no bottom text. Pause. Then the market and the box fade as the pair transforms (1.6 s) into the first-ton close-up at 0.35 per dollar: a faint teal column from the base up to 12 in x from −1.16 to −0.06, a faint orange column up to 2 from 0.06 to 1.16, hard edges at 12 and 2, and a grey baseline from x = −1.3 to 1.3. Add the Buyer and Seller spheres directly. Fade in the compact labels: \$12 (teal, 0.72) left of the buyer bar at its edge, MB (0.58) above the edge, \$2 (orange) right of the seller bar at its edge, MC below the edge inside the faint cost base. Pause. Then the red price line at 4 from x = −2.0 to 1.3 with Price (0.58) just above it at x = −1.65 and \$4 (0.72) at its left end; then, in one play, the CS fill (4 to 12) and the PS fill (2 to 4) rise to full strength with the white labels CS \$8 and PS \$2 centered on them. Add the Government sphere between the two people. Bottom: Who hands the \$2 to the government? Pause.

]

#quote(block: true)[
  2.b · Seen as a higher cost to the seller. The question leaves. In one 0.6 s play the CS fill drops back to the faint base, the PS fill to nothing, both fill labels fade, the price line dims to 0.3 and Price and \$4 fade; the dim line stays as the reference through 2.b and 2.c. Then fade in a green slice of height 2 (GOV, 0.65) stacked on the seller’s cost from 2 to 4 with tax \$2 (white, 0.58) centered on it, a dashed orange edge across its top at 4 and an orange \$4 outside right at that height: the seller’s cost plus the tax reaches the dim price. Bottom: A \$2 higher cost to the seller. Pause.

]

#quote(block: true)[
  2.c · Seen as a lower benefit to the buyer. The bottom line leaves. In one 1.2 s play the same slice transforms to the top of the buyer’s column, 10 to 12, its label riding, carved out of the buyer’s value; the seller’s dashed edge and \$4 fade; a dashed teal edge at 10 across the buyer column and a teal \$10 outside left fade in. \$12, the solid MB edge and MB above it stay. Bottom: A \$2 lower benefit to the buyer. Pause.

]

#quote(block: true)[
  2.d → 2.d.return · Either way, one price becomes two. The bottom line leaves. The price line returns to full opacity as a grey dashed ghost of it (MUTED, stroke 2, the same span) fades in at 4. A second red line starts hidden under the first; one eased tracker from 0 to 1 (2.0 s) drives the upper line to 4 + 1.6t and the lower to 4 − 0.4t while the slice transforms into a green band across both columns between the two lines, 3.60 to 5.60, with tax \$2 on it; the dashed teal edge and \$10 fade in the first fifth of the same play. After the lines settle, fade in P\_b (red, 0.58) just above the upper line at x = −1.65 and P\_s just below the lower (the ghost at 4 is only 0.40 above it and would cross the name). No numbers on the two prices yet (the market has not been solved) and no green measure (the band carries the amount). Bottom: Either way: two prices, \$2 apart. Pause. Then remove the three spheres; fade the values, the band, both lines, the ghost, the price names and the bottom line (0.4 s); the pair transforms back to its slice as the full market fades in (1.6 s) with its equilibrium marker and its CS and PS fills; the pair fades. Pause.

]

=== 3 | A tax on sellers

#quote(block: true)[
  3.a · Title: A Tax On Sellers. Subtitle: Sellers hand \$2 per ton to the government. Bottom: A \$2 higher cost on every ton. As the title changes, the equilibrium marker and the CS and PS labels fade and the CS and PS fills drop to nothing (they rest until 6.b; the faint cost bars stay). Sweep left to right (2.4 s), stacking a green strip of height 2 (GOV, 0.5) on each of the 40 cost bars, following the MC slope exactly; then faint strips (0.12) for tons 41–60, the dashed orange taxed supply from (0, 4) to (60, 7), and MC + tax at its right end. Pause.

]

#quote(block: true)[
  3.b.quantity → 3.b · The bottom line leaves. Bottom: Where does the taxed supply meet demand? Red dot where demand meets MC + tax at (32, 5.60), dashed red vertical to the axis with Q = 32 below; the cost bars and strips for tons 33–40 fade to 0.05. Pause. Then the dashed red horizontal from the dot to the axis with P\_b = 5.60 at its left; then a second red dot on the original MC at (32, 3.60) with its dashed horizontal and P\_s = 3.60. The question fades (0.4 s); no bottom text. Pause.

]

=== 4 | A tax on buyers

#quote(block: true)[
  4.a · Title: A Tax On Buyers. Subtitle: Buyers hand \$2 per ton to the government. Bottom: A \$2 lower benefit on every ton. Nothing from 3.b leaves: both dots, Q = 32 and both price guides and readouts stay exactly where they are, lifted above the strips. One eased play, 2.6 s: every green strip flies from sitting on its cost bar (2 + q/20 to 4 + q/20) to hanging under the demand curve (10 − q/5 to 12 − q/5), each keeping its opacity (0.5 for tons 1–32, 0.05 for 33–40, 0.12 for 41–50); the 32nd strip pivots in place about the wedge, its edges tilting from the supply slope to the demand slope, and every other strip hinges around it; the faint strips 51–60 fade; the dashed taxed supply crossfades into the dashed teal taxed demand from (0, 10) to (50, 0); MC + tax fades at the start of the play and MB − tax fades in at its end, tucked under the dashed curve’s upper stretch (down and left of (12, 7.60)). The dots, guides and readouts are re-added above the strips. Pause.

]

#quote(block: true)[
  4.b · The marks never moved. The bottom line leaves. A 0.5 s yellow (FOCUS) pulse on the two red dots (scale 1.4) and the Q = 32 readout (scale 1.2): the one visual that says these stayed. Bottom: Same 32 tons, same two prices. Pause.

]

=== 5 | The tax wedge

#quote(block: true)[
  5.a · Title: The Tax Wedge. No subtitle. The bottom line leaves with the old title. With the new title, fade the strips, the dashed demand and its label, the dots, guides and readouts; tons 33–40 back to base opacity. Park a thick green vertical segment of height 2 (from 3.60 to 5.60) with small end caps left of the axes at Q = −9, labeled \$2 tax in green to its left at height 4.60. Bottom: Slide the tax in from the left until it gets stuck between the curves. One eased tracker (2.6 s) slides it to Q = 32. Pause.

]

#quote(block: true)[
  5.b · The bottom line leaves. Red dots at both ends of the stuck wedge, dashed red horizontals to the axis with P\_b = 5.60 and P\_s = 3.60, a dashed red vertical from the axis to the lower end with Q = 32 below, the label moving to the upper right of the top end, and tons 33–40 faded to 0.05. Bottom: The tax wedge: the buyers’ price minus the sellers’ price equals the tax. Pause.

]

#quote(block: true)[
  5.c.wedge → 5.c.substitute → 5.c.simplify → 5.c.solve → 5.c · The bottom line leaves. Shrink the market with its wedge and marks to 0.72 about the origin and shift it left (1.1 s); fade in a thin grey divider at x = 2.45 and the worked solution at right, one line per pause: P\_b − P\_s = 2 (prices red, the tax green); (12 − Q/5) − (2 + Q/20) = 2 (demand teal, supply orange); 10 − Q/4 = 2; Q = 32 in red, already on the axis since 5.b. Bottom through these four: Use the wedge equation and the two curves to solve for the quantity. Bottom at the prices, arriving with the first of them: Then read each price from its own curve. Then, in successive plays before the single 5.c pause, P\_b = 12 − 32/5 = 5.60 and P\_s = 2 + 32/20 = 3.60. Pause. Then fade the math, the divider and the bottom line (0.5 s) and restore the market’s size and position (1.1 s).

]

=== 6 | Welfare with a tax

#quote(block: true)[
  6.a.select → 6.a.prices → 6.a · Title: Welfare With A Tax. Subtitle: 32 tons exchanged: buyers pay \$5.60 and sellers receive \$3.60. With the title, fade in the first slice’s pair and a yellow box around it; the pair shows no split yet (its band, CS and PS are hidden). No bottom text. Pause. Then the market, the wedge with its label and marks, and the box fade as the pair transforms (1.6 s) into the first-ton close-up (0.35 per dollar): faint columns, hard edges, baseline, and the hidden band spanning both columns from 3.60 to 5.60. Add Buyer, Government and Seller directly. Fade in the compact labels \$12 and MB above its edge, \$2 and MC below its edge. Then both red price lines from x = −2.0 to 1.3, their names outside the pair (P\_b above the upper line, P\_s below the lower) and \$5.60 and \$3.60 at their left ends. Pause. Then one play each: the orange PS fill from 2 to 3.60 in the seller column with PS \$1.60; the green band across both columns from 3.60 to 5.60 with tax \$2; the teal CS fill from 5.60 to 12 in the buyer column with CS \$6.40, the bottom line arriving with it. Bottom: Still exchanged: MB above P\_b, MC below P\_s. Pause.

]

#quote(block: true)[
  6.b · Remove the spheres; fade the values, price lines, price names and numbers, fill labels and bottom line (0.4 s); the pair transforms back to its slice as the market, wedge, label and marks return (1.6 s). The pair fades as the first ton’s three fills arrive (0.4 s): orange PS up to 3.60, green tax from 3.60 to 5.60, teal CS above 5.60. Sweep tons 2–32 left to right (lag 0.1, 3 s) with the same three fills; the wedge, its dots and guides are re-added above the fills. Then the white labels PS, Tax revenue and CS on their regions. Bottom: Tax revenue: \$2 × 32 tons = \$64. Pause.

]

#quote(block: true)[
  6.c.question → 6.c.select → 6.c.values · The bottom line leaves. Bottom: What about the tons no longer exchanged? Pause. The question leaves; the 36th ton’s pair (its faint cost base and a hidden buyer bar) fades in with a yellow box around it; no bottom text. Pause. Then the whole welfare market, the box and the subtitle fade as the pair transforms (1.6 s) into the detail close-up (0.68 per dollar): a faint teal column up to 4.80 and a faint orange column up to 3.80. Add Buyer, Government and Seller. Fade in (0.4 s) the hard edges and grey baseline, the compact labels \$4.80 left of the buyer bar, MB above its edge, \$3.80 right of the seller bar (buff 0.45, clear of the measure to come) and MC above its edge (clear of the P\_s line to come), and the new subtitle: The 36th unit: exchanged before the tax. Then the two yellow questions (0.60): Will they exchange? at (−4.8, −3.05) and Is it good for society? at (4.8, −3.05), level with the people’s names. Pause.

]

#quote(block: true)[
  6.c.private.compare → 6.c.private · In one play: both red price lines from x = −2.0 to 1.3, P\_b at 5.60 (its name just above the line at x = −1.65) with \$5.60 at its left end and P\_s at 3.60 (its name just below the line: MC at 3.80 is only 0.20 above it and the MC guide would cross the name) with \$3.60; and the green dashed measure at x = 1.45 from 3.60 to 5.60 with \$2 tax (green, 0.6) to its right, the wedge beside the bars. Then the purple market-side guides and brackets: the buyer pair, dashed guides from the left edges of \$4.80 and \$5.60 to x = −3.65 and a 3-wide bracket there between 4.80 and 5.60; the seller pair, MC projected from the seller bar’s left edge across the buyer column to x = −3.65 in two pieces that skip the \$3.60 number, P\_s from the left edge of \$3.60 to x = −3.65, and the short bracket between 3.60 and 3.80 (both come up short, the seller barely). Pause. Then the market’s answer: one red cross (0.85) left of x = −3.65 at the midpoint of the two brackets, height 4.30. Not exchanged; no words. Pause.

]

#quote(block: true)[
  6.c.social.compare → 6.c.loss → 6.c.return · The measure fades as the society guides fade in: MB at 4.80 in two dashed segments (across the gap between the columns, then from the seller bar’s right edge to x = 3.65), MC from the right edge of \$3.80 to x = 3.65, and the bracket at x = 3.65 between 3.80 and 4.80. Pause. Then, in one 0.5 s play, the grey DWL bar (0.8) in the buyer column from 3.80 to 4.80 (the part of the taller bar above the shorter), society’s answer right of the bracket at the same midpoint, a green check over TS \$1 in purple stacked at 0.70, and the bottom line. Bottom: The tax removes this trade, losing \$1 of surplus. Pause. Then remove the spheres; fade the edges, values, questions, price lines and names, market guides and cross, society guides and answer, the bottom line and the subtitle (0.4 s); the pair and its grey bar transform back to the 36th slice, the bar becoming the full MC-to-MB slice, as the welfare market and the section subtitle return (1.6 s); the pair fades. One grey bar on the 36th slice; no bottom text. Pause.

]

#quote(block: true)[
  6.d · The other seven grey bars for tons 33–40 sweep in (lag 0.18, 1.6 s); then DWL in white (0.8) right of (40, 5.10), clear of S / MC. Bottom: Deadweight loss: the surplus of the tons no longer exchanged. Pause.

]

=== 7 | Changing the tax

#quote(block: true)[
  7.a.zero → 7.a.five → 7.a · Title: Changing The Tax. No subtitle. The bottom line leaves with the old title. In one 1.2 s play the one-ton fills, the grey bars and their labels, the wedge, its label and marks crossfade into continuous regions driven by one tax tracker: faint cost under MC out to the taxed quantity, orange PS, the green tax rectangle, teal CS and the grey DWL triangle, each with a rolling label (CS \$102.40, PS \$25.60, Tax \$64.00, and DWL \$8.00 held beside the apex at (40.5, 5.70)); the wedge with its dots and guides, its rolling \$2 tax label at the upper right of its top end, and the axis readouts P\_b, P\_s and Q roll on the same tracker. The two price readouts part slightly as the wedge closes so they never overprint; the PS label shrinks with its triangle and slides toward the axis rather than crossing MC; the Tax label fades as its band closes. Bottom: What happens as the tax changes? Roll the tax from 2 to 0 (2.2 s). Bottom: No tax: one price, the untaxed equilibrium. Pause. The question returns; roll from 0 to 5 (3.2 s). Pause. Bottom: A larger tax: more revenue, but DWL grows faster. Roll back to 2 (2.2 s). Pause.

]

=== 8 | Tax incidence

#quote(block: true)[
  8.a · Title: Tax Incidence. Subtitle: How the \$2 tax is split between buyers and sellers. Freeze section 7’s rolling numbers and clear their updaters. One play fades the market, the five regions and their labels, the wedge, its label and the three readouts, and fades in two small graphs (axes 0–60 by 0–13, 4.8 by 4.0 units, origins at (−5.3, −2.15) and (2.5, −2.15)), identical at first: D / MB and S / MC with their names inside the plot (D / MB at the upper right of (1, 11.8), S / MC above the curve’s right end, right-aligned to it), intercept numerals 12 and 2, a grey dashed reference at the untaxed price 4 from the axis to a grey dot at (40, 4), the \$2 wedge stuck at 32 with its red end dots, dashed guides, P\_b = 5.60 and P\_s = 3.60 (0.6) left of the axis and Q = 32 below, \$2 tax hanging at the lower right of the sellers’ dot, and the incidence stacked off the axis at Q = −20: a teal segment from 4 up to P\_b labeled 1.60 and an orange segment from P\_s up to 4 labeled 0.40, numbers to the left in their colors. The left graph is static; the right graph’s curves, names, wedge, readouts and stack follow its own demand and supply slope trackers, and its intercept numerals ride outside the group so they can leave on their own. Then bottom: Buyers pay \$1.60 more; sellers receive \$0.40 less. Pause.

]

#quote(block: true)[
  8.b → 8.c → 8.d · The bottom line leaves. Bottom: What if buyers are more responsive to price? as the right graph’s intercept numerals fade and a grey dashed ghost of its demand, behind the curves, fades in. Demand rotates about (40, 4) to slope 0.05 in one eased play (2.4 s); the wedge, dots, guides, readouts and stack follow (Q = 20, P\_b = 5.00, P\_s = 3.00, stack 1.00 and 1.00). Then bottom: Buyers more responsive to price bear less of the tax. Pause. The demand ghost fades; bottom: What if sellers are less responsive to price? with a ghost of the current supply. Supply rotates about (40, 4) to slope 0.2 (2.4 s; demand stays flat): Q = 32, P\_b = 4.40, P\_s = 2.40, stack 0.40 and 1.60, the mirror image of the left graph. Then bottom: Sellers less responsive to price bear more of the tax. Pause. The supply ghost fades. Bottom: The side less responsive to price bears more of the tax. Pause.

]

=== 9 | A per-unit subsidy

#quote(block: true)[
  9.a · Title: A Per-Unit Subsidy. Subtitle: The government pays \$2 on each ton exchanged. The bottom line leaves with the old title. Freeze the right graph’s numbers; both small graphs fade as the full market returns with its faint cost bars at base opacity, its curves and intercept numerals, and no markers or fills. Bottom: Slide the subsidy in from the right until it gets stuck. A reversed green wedge from 2.40 to 4.40 with small end caps, parked right of the axes at Q = 66 and labeled \$2 subsidy to its right at height 3.40; one eased tracker (2.6 s) slides it to Q = 48. Pause.

]

#quote(block: true)[
  9.b → 9.b.wedge → 9.b.substitute → 9.b.simplify → 9.b.solve → 9.b.prices → 9.c · The bottom line leaves. In one 1.6 s play: red dots at both ends of the stuck wedge, dashed horizontals to the axis with P\_s = 4.40 and P\_b = 2.40, a dashed vertical from the axis to the lower end with Q = 48 below, the orange 2 at the axis fading (P\_b = 2.40 sits beside it), and eight one-ton pairs for tons 41–48 (faint cost base, hidden buyer bar) sweeping in (lag 0.3). Bottom: Subsidy wedge: the sellers’ price minus the buyers’ price equals the subsidy. Pause. Then the same side solve as 5.c, for skill C2.2: shrink the market with its wedge, marks and added bars to the left, grey divider, one line per pause: P\_s − P\_b = 2; (2 + Q/20) − (12 − Q/5) = 2; Q/4 − 10 = 2; Q = 48. Bottom through these four: Use the subsidy wedge and the two curves to solve for the quantity. Bottom at the prices: Then read each price from its own curve. Then P\_s = 2 + 48/20 = 4.40 with that line, then P\_b = 12 − 48/5 = 2.40, one pause, and restore the market. Then the green rectangle between 2.40 and 4.40 over tons 0–48 (0.65), labeled Subsidy cost in white at (16, 3.80), above MC, which bisects the rectangle. Bottom: Government cost: \$2 × 48 tons = \$96. Pause.

]

#quote(block: true)[
  9.d.select → 9.d.values · The bottom line leaves. Lift the 44th ton’s pair out of the added bars (the fourth added lot, index 43) and fade in a yellow box around it; no bottom text. Pause. Then the market, wedge, marks, added bars, cost rectangle, the box and the subtitle fade as the pair transforms (1.6 s) into the detail close-up: a faint teal column up to 3.20 and a faint orange column up to 4.20. Add the three spheres. Fade in (0.4 s) the edges and baseline, the compact labels \$3.20 left of the buyer bar, MB below its edge, \$4.20 right of the seller bar (buff 0.45) and MC below its edge (it will end inside the grey bar, as C1’s EXT does), and the new subtitle: The 44th unit: exchanged only with the subsidy. Then both yellow questions, as in 6.c. Pause.

]

#quote(block: true)[
  9.d.private.compare → 9.d.private · In one play: the price lines P\_b at 2.40 (its name just below the line, clear of \$3.20 above) with \$2.40 and P\_s at 4.40 (its name just above the line) with \$4.40, and the green dashed measure at x = 1.45 from 2.40 to 4.40 with \$2 subsidy to its right. Then the purple market-side guides and brackets: the buyer pair, from the left edges of \$3.20 and \$2.40 to x = −3.65 with the bracket between 2.40 and 3.20; the seller pair, MC at 4.20 projected across the buyer column in two pieces that skip the \$4.40 number, P\_s from the left edge of \$4.40, and the short bracket between 4.20 and 4.40. Pause. Then the market’s answer: one green check (0.85) left of x = −3.65 at the midpoint of the two brackets, height 3.70. Exchanged; no words. Pause.

]

#quote(block: true)[
  9.d.social.compare → 9.d.loss → 9.d.return · The measure fades as the society guides fade in: MB at 3.20 in two dashed segments, MC from the right edge of \$4.20 to x = 3.65, and the bracket at x = 3.65 between 3.20 and 4.20. Pause. Then, in one 0.5 s play, the grey DWL bar (0.8) in the seller column from 3.20 to 4.20 (MC’s name stays legible inside it), society’s answer right of the bracket, a red cross over DWL \$1 in white stacked at 0.70, and the bottom line. Bottom: The subsidy adds this trade, creating \$1 of deadweight loss. Pause. Then remove the spheres; fade everything of the close-up and the subtitle (0.4 s); the pair and its grey bar transform back to the 44th slice, the bar becoming the full MB-to-MC slice, as the subsidy market and the section subtitle return (1.6 s); the pair is removed and the lot rejoins its group, so its faint cost bar stays with the other seven. One grey bar on the 44th slice; no bottom text. Pause.

]

#quote(block: true)[
  9.e · The other seven grey bars for tons 41–48 sweep in (lag 0.18, 1.6 s); then DWL in white (0.8) above (44, 4.60), clear of the P\_s guide. Bottom: Deadweight loss: the added tons cost more than they are worth. Pause.

]

=== 10 | Next time

#quote(block: true)[
  10.a · Title: Next Time. Subtitle: Last time, a \$2 external cost made 32 tons the efficient quantity. Only the next-time cue. With the title, fade the subsidy wedge, its label and marks, the added bars, the cost rectangle, the grey bars and DWL; the orange 2 returns to the axis; tons 33–40 fade to 0.05. Then the \$2 tax wedge stuck at Q = 32 with its label, red dots, dashed guides and readouts P\_b = 5.60, P\_s = 3.60 and Q = 32. Bottom: Next time: can a tax correct an externality? Pause.

]
