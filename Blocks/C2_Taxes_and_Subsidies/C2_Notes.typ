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
// | Animation storyboard for C2_Animations.py, scene C2. New animation set drafted 2026-10-09 to follow C1_Animations.py directly. Taylor's spoken notes stay in 01_Notes.typ; the quote blocks below are animation directions, not replacement prose. The old animation (03_Code.py, the 2022 Taxes scene) is untouched and supplied the flow: tax on sellers, tax on buyers, the same outcome, the tax wedge slid in from the left, welfare areas, changing the tax, incidence under different slopes. Subsidies are new, as the mirror of the wedge.
// | References: C1_Animations.py for the market, the one-ton close-up with buyer and seller spheres, the yellow selection box, the carry-out and return zooms, the grey DWL slices, and the side equation with a grey divider; B5_Animation.py for tracker-driven curves and rolling readouts; _Style_Guide.md §5 for the tax model invariants (wedge parked left of the axes, slid in until it gets stuck; incidence stacked off-axis, buyer share teal, seller share orange).
// | Model: the C1 spinach market, MB = 12 − Q/5 and MC = 2 + Q/20, Q in tons, prices in dollars per ton, equilibrium Q = 40 and P = 4. A 2-dollar tax: Q = 32, buyers pay 5.60, sellers receive 3.60, revenue 64, DWL 8, incidence 1.60 on buyers and 0.40 on sellers. A 5-dollar tax: Q = 20, 8 and 3, revenue 100, DWL 50. A 2-dollar subsidy: Q = 48, sellers receive 4.40, buyers pay 2.40, government cost 96, DWL 8. These land exactly on C1's tons: the 32nd ton (MB 5.60, MC 3.60) is C1's efficient quantity with a 2-dollar external cost, the 36th ton (MB 4.80, MC 3.80, TS +1) is C1's removed ton, and the 48th ton (MB 2.40, MC 4.40, TS −2) is C1's added ton. The close-ups reuse those exact values and scales.
// | Conventions carried from C1: titles name the topic with every word capitalized; grey CMU Sans subtitles at scale 0.6, 0.10 below the title; one yellow (DEFINITION) teaching line in the bottom strip at scale 0.7443, centered; one-ton bars with a 0.08 gap, faint base 0.16, strong CS/PS 0.65; MB left of its value edge, MC right of its edge, at the edge's height; price readouts on the vertical axis; thin yellow selection box, pause with no bottom text, then zoom; spheres fully opaque with depth testing, added and removed directly, never faded; Buyer teal, Seller orange, and here a green Government sphere between them, labeled Government.
// | Tax conventions new in C2: tax money is GOV green. In a close-up the tax is a green slice of height 2 with a white "Tax $2" label inside it; it sits in whichever column hands the money over. On the market, revenue is the green rectangle between the two prices over the exchanged tons, labeled Tax revenue in white. The taxed supply or demand curve is the same color as the original, dashed, labeled MC + tax or MB − tax at its right end; no intercept numeral, since 4 would sit on top of P_s = 3.60. The wedge is a thick green segment with small end caps and a green "$2 tax" label, left of the segment while it slides and above its top end to the right once stuck, clear of the curves, the price readouts, and the revenue and DWL fills; for a subsidy it is reversed and parked right of the axes. The untaxed price is a grey dashed reference line only when incidence is measured. The CS and PS fills rest from 3.a until 6.b, so the strips and the wedge read cleanly; the faint cost bars stay. Tons beyond the taxed quantity fade to 0.05, as in C1.
// | Not built: a recap of C1's externality; the corrective tax (C3). Section 10 is only the next-time cue. Open for Taylor: the Government sphere in GOV green extends the token to a party (the guide lists GOV for money areas only); render it in INK if that is preferred.
// /plass:comment

=== 0 | Bumper

#quote(block: true)[
  0.a · The shared bumper: raster MICROECONOMICS, flicker, then Part C | Episode 2 beneath it, and the italic thesis in grey: Governments can change your behavior. Pause, then clear.

]

=== 1 | Last time: the market

#quote(block: true)[
  1.a · Title: Competitive Equilibrium. Subtitle: A market without externalities. The C1 opening market, unchanged: axes 0–60 tons by 0–13 dollars, D / MB from 12 and S / MC from 2 with their intercept numerals, the red equilibrium dot, dashed guides, P\* = 4 on the axis and Q = 40 below, faint orange cost bars under MC for the 40 tons. Then PS with its label, then CS with its label, both short white labels at their triangles’ centroids. Pause.

]

=== 2 | A tax on one exchange

#quote(block: true)[
  2.a.select → 2.a.values → 2.a · Title: A Per-Unit Tax. Subtitle: The government collects \$2 on each ton exchanged. Put one thin yellow box around the first exchange, the Q = 0 slice, and pause with no bottom text. Carry that pair into the close-up as the market fades, on the smaller first-ton scale (0.35 per dollar): faint bars, hard MB \$12 and MC \$2 edges with their labels bound to the bars, and the teal Buyer and orange Seller spheres with names beneath. Pause on the values. Then the red Price \$4 line and label at far left; then CS \$8 and PS \$2 with their labels. Then add a green Government sphere between the two people, labeled Government. Bottom: Who hands the \$2 to the government? Pause.

]

#quote(block: true)[
  2.b · The seller hands it over. Fade the PS \$2 label, then fade in a green slice in the seller column from MC \$2 up to the \$4 price with the white label Tax \$2 inside it while the orange PS fill drops out beneath it: the seller collects \$4 and keeps only the cost. Bottom: If the seller hands it over, the seller collects \$4 but keeps only \$2. Pause.

]

#quote(block: true)[
  2.c · The buyer hands it over. Move the same green slice, label and all, into the buyer column, now sitting from \$4 up to \$6; shrink the teal CS region to the span from \$6 to MB \$12, remove CS \$8 and fade in CS \$6; restore the orange PS \$2 region and its label in the seller column. Bottom: If the buyer hands it over, the buyer pays \$6 and the seller receives \$4. Pause.

]

#quote(block: true)[
  2.d → 2.d.return · Name the two prices. Replace the Price \$4 label with a red P_s \$4 at the same height, and add a red P_b \$6 at far left at the top of the green slice with a short red line across the buyer column. Bottom: Either way, the price buyers pay exceeds the price sellers receive by \$2. Pause. Then remove the Government sphere with the other people, fade the price labels, CS label, green slice, and bottom text, and carry the pair back to its market slice as the full market reappears, the MB and MC labels riding the bars as they fade; pause on the market.

]

=== 3 | A tax on sellers

#quote(block: true)[
  3.a · Title: A Tax On Sellers. Subtitle: Sellers hand \$2 per ton to the government. Bottom: Each ton now costs sellers \$2 more to bring to market. Fade the old equilibrium marker, the CS and PS fills, and their labels as the title changes. Sweep left to right, stacking a green strip of height 2 onto the top of each of the 40 cost bars, following the MC slope exactly, with faint green strips beyond ton 40 so the taxed curve is defined across the graph. Then the dashed orange taxed supply from (0, 4) to (60, 7), labeled MC + tax at its right end. Pause.

]

#quote(block: true)[
  3.b.quantity → 3.b · Bottom: Where does the taxed supply meet demand? Red dot where MB meets MC + tax at (32, 5.6); dashed red vertical to the axis with Q = 32; fade the cost bars and strips for tons 33–40 to almost nothing. Pause. Then the dashed red horizontal from the dot to the axis with P_b = 5.60, then a second red dot on the original MC at Q = 32 with its dashed horizontal to the axis and P_s = 3.60. Bottom: 32 tons: buyers pay \$5.60, and sellers keep \$3.60 after the tax. Pause.

]

=== 4 | A tax on buyers

#quote(block: true)[
  4.a · Title: A Tax On Buyers. Subtitle: Buyers hand \$2 per ton to the government. Remove the green strips, the dashed supply and its label, and the taxed guides; restore the 40-ton market with its equilibrium marker. Bottom: After the tax, buyers will pay sellers \$2 less for each ton. Sweep left to right, hanging a green strip of height 2 beneath the demand curve on each of the 40 buyer bars, with faint strips through ton 50. Then the dashed teal taxed demand from (0, 10) to (50, 0), labeled MB − tax at its right end. Pause.

]

#quote(block: true)[
  4.b.quantity → 4.b → 4.c · Bottom: Where does the taxed demand meet supply? Red dot where MB − tax meets MC at (32, 3.6); dashed red vertical with Q = 32; fade tons 33–40 and the old equilibrium marker. Pause. Then the dashed horizontal to the axis with P_s = 3.60, then a red dot on the original MB at Q = 32, a dashed vertical from the lower dot up to it, and its dashed horizontal with P_b = 5.60. Bottom: 32 tons again: sellers receive \$3.60, and buyers pay \$3.60 + \$2 = \$5.60. Pause. Then replace the bottom line: It doesn’t matter who hands over the tax: same quantity, same two prices. Pause.

]

=== 5 | The tax wedge

#quote(block: true)[
  5.a · Title: The Tax Wedge. No subtitle. Remove the dashed demand, its label, the strips and the guides, and restore the plain 40-ton market with no equilibrium marker. Park a thick green vertical segment of height 2 (from 3.6 to 5.6) with small end caps left of the axes at Q = −9, labeled \$2 tax in green to its left. Bottom: Slide the tax in from the left until it gets stuck between the curves. One eased tracker slides it to Q = 32. Pause.

]

#quote(block: true)[
  5.b · Red dots at both ends of the stuck wedge, dashed red horizontals to the axis with P_b = 5.60 and P_s = 3.60, a dashed red vertical with Q = 32, and tons 33–40 faded. Bottom: The tax wedge: the buyers’ price minus the sellers’ price equals the tax. Pause.

]

#quote(block: true)[
  5.c.wedge → 5.c.substitute → 5.c.simplify → 5.c.solve → 5.c · Shift and shrink the market to the left, fade in a thin grey divider and the worked solution at right, one line per pause through Q = 32, then the two price lines in successive plays before the single 5.c pause: P_b − P_s = 2 (prices red, the tax green); (12 − Q/5) − (2 + Q/20) = 2 (demand teal, supply orange); 10 − Q/4 = 2; Q = 32 in red, already on the axis since 5.b; then P_b = 12 − 32/5 = 5.60 and P_s = 2 + 32/20 = 3.60. Bottom through the first four lines: Use the wedge equation and the two curves to solve for the quantity. Bottom at the prices: Then read each price from its own curve. Then fade the math and divider and restore the market’s position.

]

=== 6 | Welfare with a tax

#quote(block: true)[
  6.a.select → 6.a.prices → 6.a · Title: Welfare With A Tax. Subtitle: 32 tons exchanged: buyers pay \$5.60 and sellers receive \$3.60. Yellow box around the first exchange, whose overlay carries no fills yet; pause with no bottom text. Zoom on the first-ton scale with Buyer, Government and Seller spheres, faint bars, MB \$12 and MC \$2 bound to the bars. Then both red price lines across the bars with P_b \$5.60 and P_s \$3.60 at far left. Pause. Then, one play each: PS \$1.60 in orange from MC to P_s in the seller column; the green Tax \$2 slice from P_s to P_b in the buyer column, label inside; CS \$6.40 in teal from P_b to MB. Bottom: The tax moves \$2 of surplus to the government; the exchange still happens. Pause.

]

#quote(block: true)[
  6.b · Remove the people, fade the price, PS, Tax and CS labels and the bottom text, and carry the pair back to its slice as the market reappears with the taxed guides, the MB and MC labels riding the bars as they fade; the pair fades as the first ton’s fills arrive. Sweep left to right over tons 1–32, each bar showing faint cost, orange PS up to 3.6, green tax from 3.6 to 5.6, and teal CS above 5.6, with the white labels PS, Tax revenue, and CS placed on their regions; the wedge, its dots and guides stay above the fills. Bottom: Tax revenue: \$2 × 32 tons = \$64. Pause.

]

#quote(block: true)[
  6.c.question → 6.c.select → 6.c.values → 6.c.prices → 6.c · Bottom: What about the tons no longer exchanged? Pause on the question. Then clear it, fade in the 36th ton’s existing cost base and buyer bar with a yellow box, and pause with no bottom text. Zoom on the C1 detail scale (0.68 per dollar): subtitle The 36th unit: exchanged before the tax, not after it. MB \$4.80, MC \$3.80, three spheres. Bottom: Does this exchange happen with the tax? Pause. Then the red P_b \$5.60 line above MB and P_s \$3.60 line below MC, labels at far left. Bottom: Buyers would pay more than MB, and sellers would get less than MC. Pause. Then shade the buyer column between MC and MB in grey and show the grey gap at right with TS = +\$1 in purple, DWL = \$1 in white, and MB \> MC in white beneath. Bottom: The tax removes this ton, creating \$1 of deadweight loss. Pause.

]

#quote(block: true)[
  6.d · Remove the people and labels, carry the pair and its grey bar back to the 36th slice as the market reappears with the section subtitle (32 tons exchanged: buyers pay \$5.60 and sellers receive \$3.60.), then add the other seven grey one-ton DWL slices for tons 33–40 between MC and MB, with the label DWL beside them. Bottom: The tax removes exchanges where MB exceeded MC: deadweight loss. Pause.

]

=== 7 | Changing the tax

#quote(block: true)[
  7.a.zero → 7.a.five → 7.a · Title: Changing The Tax. No subtitle. Crossfade the bars into continuous regions driven by one tax tracker: faint cost under MC, orange PS, the green revenue rectangle, teal CS, and the grey DWL triangle, each with a rolling label on it (CS \$102.40, PS \$25.60, Tax \$64.00, DWL \$8.00). The wedge, its label, dots, guides and axis readouts P_b, P_s and Q roll on the same tracker; the two price readouts part slightly as the wedge closes so they never overprint. Bottom: What happens as the tax changes? Roll the tax from 2 to 0. Bottom: With no tax, buyers and sellers face the same price: the untaxed equilibrium. Pause. Bottom again: What happens as the tax changes? Roll from 0 to 5. Pause. Bottom: A larger tax raises more revenue, up to a point, but DWL grows faster. (Revenue 40t − 4t² peaks at exactly t = 5 in this market, hence the qualifier.) Roll back to 2. Pause.

]

=== 8 | Tax incidence

#quote(block: true)[
  8.a · Title: Tax Incidence. Subtitle: How the \$2 tax is split between buyers and sellers. Fade the regions and their labels; keep the wedge, guides and readouts. Add a grey dashed reference at the untaxed price 4 from the axis to the old equilibrium point, ending in a grey dot there. Off the axis to the left, stack the incidence: a teal segment from 4 up to P_b labeled 1.60 and an orange segment from P_s up to 4 labeled 0.40, labels to the left in their colors. Bottom: Buyers pay \$1.60 more than before; sellers receive \$0.40 less. Pause.

]

#quote(block: true)[
  8.b → 8.c → 8.d · Bottom: What if buyers are more responsive to price? Rotate demand about the untaxed equilibrium point to a flatter slope (1/20 instead of 1/5) on a tracker; the wedge, guides, readouts and stack follow. Bottom: More elastic demand: buyers bear less of the tax. Pause, then rotate back. Bottom: What if sellers are less responsive to price? Rotate supply to a steeper slope (1/5 instead of 1/20). Bottom: Less elastic supply: sellers bear more of the tax. Pause, then rotate back. Bottom: The side less responsive to price bears more of the tax. Pause. The intercept numerals leave while the curves rotate; the curve labels ride the curves.

]

=== 9 | A per-unit subsidy

#quote(block: true)[
  9.a · Title: A Per-Unit Subsidy. Subtitle: The government pays \$2 on each ton exchanged. Fade the wedge, stack, guides and readouts; restore the plain market with only the faint cost bars and no markers. Park a reversed green wedge right of the axes at Q = 66, from 2.4 to 4.4, labeled \$2 subsidy to its right. Bottom: Sellers now receive \$2 more than buyers pay. Slide it in from the right. One eased tracker slides it to Q = 48. Pause.

]

#quote(block: true)[
  9.b → 9.b.wedge → 9.b.substitute → 9.b.simplify → 9.b.solve → 9.b.prices → 9.c · Red dots at the wedge ends, dashed horizontals with P_s = 4.40 and P_b = 2.40, a dashed vertical with Q = 48, and eight added one-ton cost bars through ton 48 matching the existing bars; the orange 2 at the axis leaves while P\_b = 2.40 sits beside it. Bottom: Subsidy wedge: the sellers’ price minus the buyers’ price equals the subsidy. Pause. Then the same side solve as 5.c for skill C2.2: shrink the market left, grey divider, lines P_s − P_b = 2; (2 + Q/20) − (12 − Q/5) = 2; Q/4 − 10 = 2; Q = 48, one per pause, with the bottom line Use the subsidy wedge and the two curves to solve for the quantity; then P_s = 2 + 48/20 = 4.40 and P_b = 12 − 48/5 = 2.40 with Then read each price from its own curve, one pause, and restore the market. Then the green rectangle between 2.4 and 4.4 over 0–48 at the same strength as the tax revenue, labeled Subsidy cost in white in its upper left, above MC, which bisects the rectangle. Bottom: Government cost: \$2 × 48 tons = \$96. Pause.

]

#quote(block: true)[
  9.d.select → 9.d.values → 9.d.prices → 9.d · Yellow box around the 48th bar; pause with no bottom text. Zoom on the detail scale: subtitle The 48th unit: exchanged only with the subsidy. MB \$2.40, MC \$4.40, three spheres. Bottom: Why does this exchange happen? Pause. Then the red P_b \$2.40 line at the buyer’s MB and P_s \$4.40 at the seller’s MC, labels at far left, and the green Subsidy \$2 slice from 2.40 to 4.40 in the seller column, label inside. Bottom: The buyer pays \$2.40, the government adds \$2, and the seller receives \$4.40. Pause. Then shade the buyer column between MB and MC in grey (the cost above the buyer’s value; the seller column holds the subsidy slice) and show the grey gap with TS = −\$2 in purple, DWL = \$2 in white, and MC \> MB in white beneath. Bottom: This ton costs \$2 more than it is worth: deadweight loss. Pause.

]

#quote(block: true)[
  9.e · Remove the people and labels, carry the pair and grey bar back to the 48th slice, where the lot rejoins the other seven, as the market reappears with the section subtitle (The government pays \$2 on each ton exchanged.), then add the other seven grey DWL slices for tons 41–48 between MB and MC, labeled DWL. Bottom: A subsidy adds exchanges where MC exceeds MB: deadweight loss. Pause.

]

=== 10 | Next time

#quote(block: true)[
  10.a · Title: Next Time. Subtitle: Last time, a \$2 external cost made 32 tons the efficient quantity. Fade the subsidy objects, restore the plain market with its intercept numerals, and show the \$2 tax wedge stuck at Q = 32 with its dots, guides and readouts. Bottom: Next time: can a tax correct an externality? Pause.

]
