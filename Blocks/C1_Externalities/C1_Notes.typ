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

== Episode C1 | Externalities

// plass:comment
// | Animation storyboard for C1_Animations.py, scene C1. New introduction requested 2026-10-06. Taylor is writing the spoken notes; the quote blocks below are animation directions, not replacement prose.
// | References: B4_Animation.py welfare and head-on deliberation; B5_Animation.py continuous market; C3_Corrective_Policy/03_Code.py legacy externalities scenes.
// | Bar revision 2026-10-07: start with the full market, carry the first exchange into a close-up and back, then carry the exact marginal exchange at Q = 40 into a close-up and back. No subtitles on these close-ups. MB and MC have hard value edges; base regions use opacity 0.16, CS/PS use 0.65. Buyer column ends at MB, seller column ends at price/revenue with MC marked inside. No green payment fill. Capitalize every word in topic titles. Topic titles stay stable while yellow teaching lines change.
// | Unit revision 2026-10-07: Q is tons; all prices, benefits, and costs are dollars per ton. Keep the simple numerical curves as a rescaled teaching example rather than converting the old physical dataset. Remove grey explanatory captions from exchange close-ups: no average-values note, quantity-change footer, one-ton footer, or prose repeating the surplus result. Keep units on the axes and the active question/takeaway in yellow. CS/PS labels sit beside their regions without leaders; retain purple TS gap guides. MB sits directly left of the MB value line, and MC directly right of the MC value line, at the same height as that line. Restore the buyer/seller spheres and keep Buyer and Seller beneath their respective spheres in both opening close-ups. Keep value labels attached to the live bars through movement and return zooms.
// | Reveal revision 2026-10-07: each close-up pauses on MB and MC before price, surplus, or a welfare answer. In the opening review, keep the same MB/MC labels, spheres, and Buyer/Seller labels visible continuously. Show the established market price next, then fade in CS/PS. The first exchange asks: Is there a price that would make this exchange work? Fade the question as price appears. Keep the MB = MC exchange free of a price question. Externality comparisons first show private values, then external/social cost, then the welfare result. Ask about increasing/decreasing quantity, not changing it by one.
// | Visual revision 2026-10-07: all bottom teaching text is yellow (DEFINITION). Basic spheres stay fully opaque with depth testing enabled. Add and remove them directly; never opacity-fade spheres or groups containing them, since translucency exposes the rear mesh as internal discs. Unit-surplus comparisons use purple (TOTAL) guides from both bar tops to a labeled vertical gap.
// | Canonical exchange scene: retain the Part B teal buyer and orange seller spheres with shadows in every close-up, including the first exchange and MB = MC equilibrium exchange. Buyer and Seller stay beneath the spheres. Reveal the people with MB/MC and retain them through price, surplus, and welfare reveals; remove them directly only on the return to the market. Names do not replace spheres.
// | Subtitle style: all prose subtitles use CMU Sans, CAPTION grey, scale 0.8, left-aligned with the title and 0.10 units below it. Use the shared subtitle() defaults; never book=True for these context lines.
// | Notation: retain MB and MC throughout this negative-externality lesson. The total cost is MSC = MC + EXT; EXT is the external cost per ton. Benefit remains MB because this example has no external benefit.
// | Model: MB = 12 − Q/5, MC = 2 + Q/20, constant external cost 2 dollars per ton. Q-hat = 40; Q-star = 32. Each comparison selects one one-ton exchange, with unit values evaluated at its rank on the curves. Add eight individual bars through ton 48, then select ton 48: MB 2.40, MC 4.40, TS −2. Reduce quantity to 35 and select removed ton 36: MB 4.80, MC 3.80, TS +1. With external cost 2 per ton, revisit only the 36th unit: social TS −1 and DWL 1, with the worked MSC calculation. Skip the repeated 48th-unit Social Welfare example. Never use an eight-ton average or multiply the displayed gap by a batch size. The opening close-ups use the boundary values at Q = 0 (MB 12, MC 2) and Q = 40 (MB = MC = 4).
// /plass:comment

=== 1 | Equilibrium and the First Welfare Theorem

#quote(block: true)[
  1.a · Title: Competitive Equilibrium. Start with the full Part B spinach market: demand P = 12 − Q/5, supply P = 2 + Q/20, Q in tons, P in dollars per ton. Show equilibrium Q = 40, P = 4. Show faint orange production costs below MC (opacity 0.16), then fade in orange PS first and teal CS second (opacity 0.65), each with its label. The curves form the hard value boundaries. Use only the white abbreviations PS and CS, centered at the centroids of their own surplus triangles; do not spell out the full words. Continuous curves and exact sloping slices retain the B5 model.

]

#quote(block: true)[
  1.a.first.values → 1.a.first · Keep title: Competitive Equilibrium; no subtitle. Select the starting exchange at Q = 0 with one thin yellow outline box around its full existing bar slice. Keep the bars teal and orange; do not add selection dots, vertical lines, or extra colored outlines. Pause on the highlighted exchange with no bottom annotation, then carry that same buyer/seller pair into a close-up as the market fades. Show faint full-height bars with hard MB = 12 and MC = 2 edges, the buyer/seller spheres, and Buyer/Seller labels beneath them. Anchor MB/MC labels beside their hard value lines. Omit the extra values/average caption. Withhold the price line, CS/PS fills, and surplus labels. Bottom question: Is there a price that would make this exchange work? Pause on the values. Fade the question as price appears. Keep MB/MC, spheres, and Buyer/Seller visible throughout the following reveals. First reveal the established price 4 line and label. In the next play, fade in stronger teal CS 8 and orange PS 2 above the respective faint bases, together with their surplus labels. Put the CS/PS labels immediately beside the corresponding regions, with no connector lines. Bottom: First exchange: both the buyer and seller gain. Pause again.

]

#quote(block: true)[
  1.a.first.return · Fade the close-up labels and bottom text; carry the same pair back to its original rank as the full market reappears. Merge both columns onto the same full-width market slice, with exact sloping CS/PS/cost boundaries. Fade out the buyer expenditure base as the columns merge. Remove the selected pair overlay and pause on the complete market.

]

#quote(block: true)[
  1.a.last.values → 1.a.last · Keep title: Competitive Equilibrium; no subtitle. Put one thin yellow outline box around the last existing exchange at Q = 40, retaining the canonical red intersection marker. Do not add a yellow dot. Pause on the highlighted exchange with no bottom annotation. Fade the box as its marginal buyer/seller pair moves into the close-up on the same scale. First show only MB = MC = 4 dollars per ton, faint bars, hard value edges, and buyer/seller spheres with names underneath. MB and MC labels sit beside the equal-height value lines. Withhold price and the conclusion; pause on the values without asking which price would work. Keep the same MB/MC labels, spheres, and Buyer/Seller visible. Reveal the established price 4 line and label, then the yellow conclusion: At equilibrium, MB = MC = 4 dollars. There is no surplus area. These are exact boundary values, not an average over a finite interval.

]

#quote(block: true)[
  1.a.last.return · Fade the close-up labels and bottom text; carry the equal-value pair back to the same equilibrium point as the full market reappears, with both columns sharing exactly the same horizontal position. Remove the overlay and pause on the full market before asking about the next exchange.

]

#quote(block: true)[
  1.b → 1.b.select · Ask: What happens if we increase quantity? Add eight separate one-ton bars, one after another, beyond Q = 40 through Q = 48. Match the existing bars’ spacing, fills, and sloping curve boundaries; do not add horizontal value caps or a staircase along demand or supply. Then clear the question, highlight the last actual bar, ton 48, and pause with no bottom annotation. Only this selected one-ton exchange moves into the close-up.

]

#quote(block: true)[
  1.c.values → 1.c · Carry the selected one-ton pair into the close-up, fading the market. Under the topic title, show the subtitle: The 48th unit: a quantity larger than in equilibrium. First show only faint bars, solid value edges, MB 2.40 and MC 4.40, with each value label at its line. Bottom question: Can any price make this trade worthwhile? Pause. Then reveal the grey loss gap with two adjacent labels: signed TS = −2 dollars in purple and DWL = 2 dollars in white. The negative TS is MB minus MC for this one ton; DWL is the positive amount of surplus lost by adding it. Show MC \> MB. Bottom: Negative TS means deadweight loss: a reduction in total surplus. Keep the context subtitle through the answer, then fade it on the return to the market. No grey footers or aggregate totals.

]

#quote(block: true)[
  1.d · Return this same one-ton pair to its bar at rank 48, with both columns sharing the same horizontal bounds. Restore the full market and remove the eight added bars to return to Q = 40.

]

#quote(block: true)[
  1.e → 1.e.select · Keep title: Competitive Equilibrium. Ask: What happens if we decrease quantity? Fade existing one-ton bars from ton 40 down through ton 36, reaching Q = 35. Select ton 36 from the existing market bars: reuse its cost polygon and the buyer bar’s existing demand edge and baseline. Put one thin yellow outline box around the full existing one-ton slice, keeping the bars teal and orange. Clear the question and pause on the highlight with no bottom annotation, then zoom in. Keep both columns in the same original one-unit-wide slice until the close-up separates them.

]

#quote(block: true)[
  1.f.values → 1.f · Carry that one-ton pair into the close-up. Under the topic title, show the subtitle: The 36th unit: a quantity exchanged in equilibrium. First show only MB 4.80 and MC 3.80 beside their hard value lines, faint bars, and spheres. Bottom question: Would removing this ton improve welfare? Pause. Then reveal MB \> MC and a grey loss gap with signed TS = +1 dollar in purple and DWL = 1 dollar in white beside it. The exchange itself yields positive surplus; the DWL arises from removing it and forgoing that surplus. Bottom: Removing this ton creates \$1 of deadweight loss. Keep the context subtitle through the answer; omit grey footers.

]

#quote(block: true)[
  1.g · Fade the subtitle, return both columns to the exact original one-ton width and sloping value edges, and restore equilibrium. Retain the existing red curve-intersection marker without adding a yellow dot. Bottom: At equilibrium, MB = MC. Then change title to The First Welfare Theorem. One yellow takeaway, across two lines: When all benefits and costs are counted, competitive equilibrium maximizes total surplus.

]

=== 2 | Gary, Molly, and the people outside the trade

#quote(block: true)[
  2.a · Title: Negative Externalities. Subtitle from the start: A cost paid by others outside the market. Set it in grey CMU Sans, left-aligned and 0.10 units below the title, matching all C1 context subtitles. Keep this subtitle through 2.f. Leave the bottom text empty until the costs are stacked in 2.c. Enter the familiar Part B head-on deliberation: Gary at left, Molly beside him, spheres and shadows under the adjacent teal benefit and orange cost bars. Use the 20th one-ton exchange, with marginal values at Q = 20: MB 8, MC 3, and price 4. Gary gains CS 4 and Molly gains PS 1. Keep the bar height within the existing body area on a common 0.44-unit-per-dollar scale. Preserve the prior bar-pair geometry, adapted to leave the right side empty. Carry forward faint bases, strong CS/PS regions, and solid MB/MC edges; the seller column reaches price above its MC boundary. One lot means one ton; omit the grey footer.

]

#quote(block: true)[
  2.b · One small grey bystander appears centered beneath the purple external-cost text, with a narrow pink cost bar directly above them: 0.25 dollars per ton. Center the label Bystander beneath the sphere. Above the cost, add the grey heading Externalized cost per ton and show only \$0.25 in pink, without /ton in the number. Keep that cost above the person as the other people arrive. No yellow prompt. Gary and Molly’s bars and price do not move.

]

#quote(block: true)[
  2.c.people → 2.c · Reveal seven more small grey bystanders, each with a separate narrow pink cost bar directly above them. When the second person appears, change Bystander to Bystanders. Recenter the growing row beneath the purple text after every addition; move each person and their cost bar together. Keep the Bystanders label centered below the row through stacking. Keep all eight bars above their respective people, with matching heights and no overlap, and pause. Leave the bottom text empty. Only after all eight people and their bars are visible, move the eight costs into one stack totaling 2 dollars per ton. Keep the grey Externalized cost per ton heading above the arithmetic 8 × \$0.25 = \$2; omit /ton from the arithmetic. All eight people remain below. Then show the yellow takeaway on one centered line: Exchanges between buyer and seller in the market can impose a cost on others.

]

#quote(block: true)[
  2.d · Keep the Negative Externalities title and A cost paid by others outside the market. subtitle visible. Go directly from Gary and Molly with the stacked bystander costs to the two full-market graphs: the market’s MB, MC, and equilibrium on the left, and externalized cost per ton on the right. Omit the small one-trade external-cost graph and the second buyer–seller example. Carry Gary and Molly’s bars into their Q = 19 to 20 slice for the 20th ton, sharing its full width and matching the sloping cost, CS, and PS boundaries. Fade the buyer expenditure base during the merge. Carry the pink stack into the same quantity interval on the right. Remove the people and close-up labels during the pullback. Both graphs use Q = 0 to 60 with matching horizontal scales. Center each tons caption directly beneath its Q at the right end of the horizontal axis. Add an orange 2 just left of the market’s vertical axis at the MC intercept; retain it when this graph recenters and enlarges for Social Welfare. Place Externalized cost per ton just above the right graph’s vertical axis, with the first letter E aligned to the axis. Pause with only Gary and Molly’s exchange and its matching external-cost rectangle filled; keep the other exchanges unfilled.

]

#quote(block: true)[
  2.f · Sweep from left to right across the other equilibrium exchanges. Reveal each exchange’s faint orange production cost and stronger orange PS and teal CS together with its matching pink external-cost bar on the right. Keep the existing Gary–Molly slice visible throughout the sweep. The completed external-cost rectangles cover Q = 0 to 40 at height 2. Show Q = 40 and total external cost of 80 dollars, then pause. No extra yellow narration during the sweep.

]

=== 3 | Constructing marginal social cost

#quote(block: true)[
  3.a · Remove the Negative Externalities subtitle when changing the title to Marginal Social Cost. Bottom: What is the full cost of a trade? Clear the question before showing the equation at right in 3.b. Fade the demand curve, benefit bars, surplus labels, and equilibrium annotations. Keep the private cost bars and MC curve on the left and the externality rectangles on the right.

]

#quote(block: true)[
  3.b.words → 3.b · Move the external-cost rectangles across one by one onto the tops of the matching private-cost slices. Each pink strip is height 2 above MC; its sloping edges follow MC exactly. Fade the now-empty external-cost axes. Introduce the solid orange upper boundary and label MSC; keep MSC solid in every later graph view. Show faint potential strips past the current quantity so MSC is defined across the graph. Leave the bottom text empty. In the open space to the right, use a subtle grey divider and show the full-word equation: Marginal social cost = Marginal cost + External cost. Put Marginal social cost above the equals-and-sum line for readable spacing. Use orange for the cost terms, pink for external cost, and white for the operators. Pause on the full words, then transform the corresponding terms into one line: MSC = MC + EXT. Pause again. Keep the graph curve labeled MC, and retain MB when demand returns; do not introduce MPC or MPB.

]

#quote(block: true)[
  3.c · Title: Social Welfare. Add the grey CMU Sans subtitle: The welfare of everyone, not just buyers and sellers in the market. Place it 0.10 units below the title, left-aligned. Keep this topic title through the 36th-unit example and its return to the market. Replace this subtitle with the unit-specific subtitle in the close-up, restore it on the return to the market, and remove it when the title changes to Efficient Quantity. Fade the right-side equation and divider before recentering and enlarging the combined graph. Restore demand as MB, keep supply labeled MC, and plot unchanged private equilibrium Q-hat = 40, P-hat = 4. Use hats for the inefficient market equilibrium on both graphs. Put P-hat = 4 to the left of the vertical axis at height 4, with a dashed red horizontal guide from the axis to the equilibrium point. Keep the price label on its axis throughout the later market views. The MSC intersection is not a new market equilibrium. Bottom: Would reducing quantity improve welfare? Pause before revealing an answer. Go directly to the 36th-unit example in 3.e; omit the 48th-unit Social Welfare close-up.

]

#quote(block: true)[
  3.e.select → 3.e.values → 3.e.external → 3.e.price → 3.e.surplus → 3.e.extension → 3.e.formula → 3.e.substitution → 3.e.result → 3.e.costs → 3.e → 3.e.return · Select the one exchanged ton at rank 36, copying the existing private-cost and external-cost strips so its market width and sloping edges match exactly. Put a thin yellow outline box around the selected slice and pause with no bottom annotation before zooming in. Repeat the subtitle: The 36th unit: a quantity exchanged in equilibrium. Position the whole exchange in the left half through the detached-bystander setup and worked MSC calculation. Preserve the filled pink EXT region on top of MC as it comes out of the market. Show MB 4.80, MC 3.80, and EXT 2 beside their value edges, with buyer and seller spheres and one grey sphere labeled Bystanders between them. Pause. Move the existing EXT rectangle to the right, together with the grey sphere and its label, while showing the yellow note: Buyers and sellers only consider their private costs and benefits. Route the EXT bar above the MC label and the grey sphere below the other people during travel. Fade the moving cost and Bystanders labels before travel, then reveal them at the destination. Above the detached bar, keep the grey heading Externalized cost per ton and show just 2 in pink; no repeated arithmetic, stacked pieces, or crowd of bystanders. Pause. While EXT stays off to the right, show the red market-price line at 4 and its label to the left of the buyer bar; keep MB and MC visible beside their value edges. Pause, then shade and label PS 0.20 in orange between MC 3.80 and price 4, followed by CS 0.80 in teal between price 4 and MB 4.80. Place CS beside its region; use a short orange pointer to keep the small PS label clear of MC. Keep the private-costs-and-benefits note visible and pause on both private gains. Fade the price, both surplus regions, and their labels and pointer completely before returning EXT. Move the same filled rectangle back onto MC, from 3.80 to 5.80, restore EXT 2 beside it, and move the grey sphere and Bystanders label back between Buyer and Seller on their common baselines. Clear the side heading and yellow note. Keep the pink region shaded at opacity 0.65 throughout. Pause. Fade in a thin grey vertical separator and MSC = MC + EXT in the right half. On the line below, copy MC 3.80 and EXT 2 from the bar labels into MSC = 3.80 + 2, one value at a time. Pause, simplify to MSC = 5.80, and pause again. Move MSC and 5.80 to the rectangle's top boundary, removing the equals sign and working equation; show the orange MSC value edge at that height. Keep MB, MC, EXT, and all three spheres and labels visible. Pause, then clear the divider and smoothly recenter the complete exchange. Shade the seller-side region between MB 4.80 and MSC 5.80 in grey, and reveal the grey loss gap with signed TS = −1 dollar in purple and DWL = 1 dollar in white beside it. This harmful exchange contributes one dollar of DWL while it occurs. Bottom: Removing this ton eliminates 1 dollar of deadweight loss. Remove all three spheres and their labels and fade the subtitle on the return to its original one-ton market slice. Carry the same grey DWL region back to the 36th-unit slice, using its existing width and exact sloping boundaries between MB and MSC. Keep this single grey bar visible on the full market, with no new annotation, through the search for efficient quantity.

]

=== 4 | Efficient quantity and deadweight loss

#quote(block: true)[
  4.a → 4.a.select → 4.a.exchange → 4.a.return · Title: Efficient Quantity. Continue the fundamentals from the old animation_0 and Externalities scenes in C3_Corrective_Policy/03_Code.py: hold private demand, supply, and equilibrium fixed while comparing social marginal benefits and costs. Move an evaluation guide left from 40 until MB = MSC at Q = 32. Label the efficient quantity Q-star = 32 and retain the separate Q-hat = 40 marker. Bottom: Social welfare is maximized where MB = MSC. At Q = 32, clear the note, put a yellow outline around the existing 32nd-unit bars, clear the yellow point and evaluation line, and pause. Zoom that exchange into the canonical close-up, fading the market and its markers. Keep the Efficient Quantity title and add the grey CMU Sans subtitle: The 32nd unit: the efficient quantity. Show the buyer and seller spheres with one grey Bystanders sphere between them and labels underneath. Keep the pink EXT region filled on top of MC. Place MB 5.60 and MSC 5.60 beside their equal-height value edges, MC 3.60 beside its edge, and EXT 2 beside the pink region. Show TS = 0 in purple and DWL = 0 in white at right; there is no grey loss region for this exchange. Bottom: For this exchange, MB = MSC and there is no deadweight loss. Pause. Clear the people, labels, result, and subtitle, then carry the bars back to their exact original market slice. Restore the efficient-quantity markers and the 36th-unit grey DWL bar before proceeding to the full set of DWL bars.

]

#quote(block: true)[
  4.b · Title: Deadweight Loss. Retain the 36th-unit grey bar while adding the other grey social-loss bars between 32 and 40. Keep all eight as separate one-ton bars, matching the widths and gaps of the existing exchange bars and following the sloping MSC and MB boundaries. Do not merge them into a triangle. Retain the separate bars through the remaining Efficient Quantity scenes. Label DWL. Keep the pink external-cost strips visually distinct: total external damage is not DWL. Bottom: These trades create deadweight loss because social cost exceeds benefit.

]

#quote(block: true)[
  4.c.comparison → 4.c.beneficial → 4.c.values → 4.c.exchange → 4.c · Return title to Efficient Quantity. Keep the market graph and both quantity markers visible, and show Q-star < Q-hat in the yellow bottom strip. Pause on this comparison before fading it out and introducing the final question. Move the evaluation marker to Q = 24, where MB is greater than MSC. Bottom: Are some exchanges worthwhile even with externalities on others? Replace the evaluation line with a yellow outline around the existing 24th-unit bars, pause, then zoom into the canonical exchange close-up. Fade the market and its DWL bars and markers during the zoom. Add the grey CMU Sans subtitle: The 24th unit: a quantity below the efficient quantity. Keep the teal buyer and orange seller spheres, with one grey Bystanders sphere between them and labels underneath. Show MB 7.20, MC 3.20, filled pink EXT 2, and MSC 5.20 beside their respective value edges. Use one common vertical scale for all three bars, leaving space below the subtitle. Pause on the values and question before revealing the answer. Shade the buyer's benefit above MSC in teal and show TS = 2 in purple and DWL = 0 in white at right. Keep the yellow question. Pause, then clear the people and detail labels, carry the exchange back to its exact market slice, restore the separate grey DWL bars and markers, and return the evaluation marker to 32. Stop here for the current intro build; preserve the old notebook’s positive-externality and corrective-policy material as the source for later notes.

]
