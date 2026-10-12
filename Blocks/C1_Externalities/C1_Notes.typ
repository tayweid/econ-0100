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
// | Subtitle style: all prose subtitles use CMU Sans, CAPTION grey, scale 0.6, left-aligned with the title and 0.10 units below it. This is 25% smaller than the former 0.8 scale. Use the shared subtitle() defaults; never book=True for these context lines.
// | Vertical intercepts: label MB/demand 12 in teal and MC/supply 2 in orange on every market graph. When MSC appears, show its orange intercept 4; when MSB appears, show its teal intercept 14. Place each number left of the vertical axis at its curve height and reveal or remove it with that curve. At the shared MSC-intercept and market-price level, put red P-hat = immediately before the single orange 4, avoiding a duplicate numeral while keeping the price on the vertical axis.
// | Notation: retain MB and MC throughout. For negative externalities, MSC = MC + EXT and benefit remains MB. For positive externalities, MSB = MB + EXT and cost remains MC. EXT is the external cost or benefit per ton in its respective example.
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
  2.b · One small pink bystander appears centered beneath the purple external-cost text, with a narrow pink cost bar directly above them: 0.25 dollars per ton. Center the label Bystander beneath the sphere. Above the cost, add the grey heading Externalized cost per ton and show only \$0.25 in pink, without /ton in the number. Keep that cost above the person as the other people arrive. No yellow prompt. Gary and Molly’s bars and price do not move.

]

#quote(block: true)[
  2.c.people → 2.c · Reveal seven more small pink bystanders, each with a separate narrow pink cost bar directly above them. When the second person appears, change Bystander to Bystanders. Recenter the growing row beneath the purple text after every addition; move each person and their cost bar together. Keep the Bystanders label centered below the row through stacking. Keep all eight bars above their respective people, with matching heights and no overlap, and pause. Leave the bottom text empty. Only after all eight people and their bars are visible, move the eight costs into one stack totaling 2 dollars per ton. Keep the grey Externalized cost per ton heading above the arithmetic 8 × \$0.25 = \$2; omit /ton from the arithmetic. All eight people remain below. Then show the yellow takeaway on one centered line: Exchanges between buyer and seller in the market can impose a cost on others.

]

#quote(block: true)[
  2.d · Keep the Negative Externalities title and A cost paid by others outside the market. subtitle visible. Go directly from Gary and Molly with the stacked bystander costs to the two full-market graphs: the market’s MB, MC, and equilibrium on the left, and externalized cost per ton on the right. Omit the small one-trade external-cost graph and the second buyer–seller example. Carry Gary and Molly’s bars into their Q = 19 to 20 slice for the 20th ton, sharing its full width and matching the sloping cost, CS, and PS boundaries. Fade the buyer expenditure base during the merge. Carry the pink stack into the same quantity interval on the right. Remove the people and close-up labels during the pullback. Both graphs use Q = 0 to 60 with matching horizontal scales. Center each tons caption directly beneath its Q at the right end of the horizontal axis. Add an orange 2 just left of the market’s vertical axis at the MC intercept; retain it when this graph recenters and enlarges for Social Welfare. Place Externalized cost per ton just above the right graph’s vertical axis, with the first letter E aligned to the axis. Pause with only Gary and Molly’s exchange and its matching external-cost rectangle filled; keep the other exchanges unfilled.

]

#quote(block: true)[
  2.f · Sweep from left to right across the other equilibrium exchanges. Reveal each exchange’s faint orange production cost and stronger orange PS and teal CS together with its matching pink external-cost bar on the right. Keep the existing Gary–Molly slice visible throughout the sweep. The completed external-cost rectangles cover Q = 0 to 40 at height 2. Show Q = 40 and total external cost of 80 dollars, then pause. No extra yellow narration during the sweep.

]

=== 3 | Constructing marginal social cost

#quote(block: true)[
  3.a · Remove the Negative Externalities subtitle when changing the title to Marginal Social Cost. Add the grey CMU Sans subtitle: All the costs to society of one more unit of the good. Keep it through the cost construction and equation, then remove it with the title when switching to Social Welfare. Bottom: What is the full cost of a trade? Clear the question before showing the equation at right in 3.b. Fade the demand curve, benefit bars, surplus labels, and equilibrium annotations. Keep the private cost bars and MC curve on the left and the externality rectangles on the right.

]

#quote(block: true)[
  3.b.words → 3.b · Move the external-cost rectangles across one by one onto the tops of the matching private-cost slices. Each pink strip is height 2 above MC; its sloping edges follow MC exactly. Fade the now-empty external-cost axes. Introduce the solid orange upper boundary and label MSC; keep MSC solid in every later graph view. Keep pink strips at opacity 0.8 only through the actually exchanged quantity, Q = 40, matching the extent of the seller cost bars. Extend the MSC curve across the graph without filling unexchanged quantities. Leave the bottom text empty. In the open space to the right, use a subtle grey divider and show the full-word equation: Marginal social cost = Marginal cost + External cost. Put Marginal social cost above the equals-and-sum line for readable spacing. Use orange for the cost terms, pink for external cost, and white for the operators. Pause on the full words, then transform the corresponding terms into one line: MSC = MC + EXT. Pause again. Keep the graph curve labeled MC, and retain MB when demand returns; do not introduce MPC or MPB.

]

#quote(block: true)[
  3.c · Title: Social Welfare. Add the grey CMU Sans subtitle: The welfare of everyone, not just buyers and sellers in the market. Place it 0.10 units below the title, left-aligned. Keep this topic title through the 40th-unit example and its return to the market. Replace this subtitle with the unit-specific subtitle in the close-up, restore it on the return to the market, and remove it when the title changes to Negative Externality. Fade the right-side equation and divider before recentering and enlarging the combined graph. Restore demand as MB, keep supply labeled MC, and plot unchanged private equilibrium Q-hat = 40, P-hat = 4. Use hats for the inefficient market equilibrium on both graphs. Put P-hat = 4 to the left of the vertical axis at height 4, with a dashed red horizontal guide from the axis to the equilibrium point. Keep the price label on its axis throughout the later market views. The MSC intersection is not a new market equilibrium. Bottom: Would reducing quantity improve welfare? Pause before revealing an answer. Go directly to the 40th-unit example in 3.e; omit the 48th-unit Social Welfare close-up.

]

#quote(block: true)[
  3.e.select → 3.e.values → 3.e.private.compare → 3.e.private → 3.e.social.compare → 3.e → 3.e.return · Begin at the 40th unit, the private equilibrium. Zoom directly into the centered compact layout with MB and MC at 4 and MSC at 6, names on bars, monetary values beside their boundaries, EXT inside the faint pink bar and its dashed pink 2-dollar measure outside. Keep the buyer, pink bystander and seller together underneath. Show both yellow questions immediately, one on each side. Pause on the values, then show private measurement, pause, and reveal Indifferent (MB = MC). Show social measurement, pause, then reveal No, TS = −2 and DWL = 2. Do not detach EXT, introduce a separate price/CS/PS demonstration, or repeat the MSC calculation here. Return to the full market with no grey loss overlay. The moving guide alone owns the market loss shading.


]

#quote(block: true)[
  3.f.36.select → 3.f.36.values → 3.f.36.private → 3.f.36.loss → 3.f.36.return · Start the dashed yellow guide at 40 and sweep to 36, turning only the passed loss slices grey. Freeze those opacities while zooming into unit 36 so the market can fade cleanly. Show MB 4.80, MC 3.80, MSC 5.80 and the two decisions with the same compact labels and pause-before-answer convention. Private exchange receives a green check; social value is negative, TS = −1 and DWL = 1. Return with the four already-swept grey slices intact, no isolated grey bar at unit 36, and the yellow guide still at 36. Continue the same sweep to 32, progressively revealing the remaining loss slices, then inspect social efficiency. Do not repeat the equilibrium close-up or reset the guide to 40.


]

In every two-decision externality close-up, keep the monetary values outside the bars at the exact height of their respective boundaries. Put MB inside the buyer bar just below its top, MC inside the seller bar just below its top, and MSC immediately above the social-cost top. Center EXT inside the faint pink region. Place a full-opacity pink dashed vertical measure just to the right of the pink bar, spanning MC to MSC, with $2 beside its midpoint. Use equal faint base opacity for all underlying bars; welfare fills still reveal separately. These compact labels replace the combined side labels in the individual beat descriptions below. Preserve the original single-decision competitive-market close-ups at the beginning. Begin the 40th-unit introduction directly in this compact layout with both questions visible. Clear the compact labels and pink measurement with each return to the market.

For the centered negative-externality exchange close-ups (3.e, the 3.f.36 example, 4.a, and 4.c), use two persistent question headings: Will they exchange? on the left and Is it good for society? on the right. First project MB and MC left with purple dashed guides and measure their vertical difference. Reveal the private answer, then pause at the corresponding .private beat. MB > MC means Yes; MB = MC at unit 40 means Indifferent, with no private gap. Next project MB and MSC right and reveal the social answer together with signed TS and DWL. At unit 36, private willingness coexists with a social loss (TS = −1, DWL = 1); at unit 40, private indifference coexists with TS = −2 and DWL = 2. At unit 32, label the social answer Neutral: MB = MSC, TS = 0, DWL = 0. At unit 24, both answers are Yes, with TS = 2 and DWL = 0. Guides break around existing value labels; coincident values share a single level without an artificial vertical gap. Fade both question headings, answers, and guides before returning to the market, retaining the previously specified grey market loss bars. These paired measurements replace the standalone welfare result blocks described in the individual beats.

=== 4 | Efficient quantity and deadweight loss

The negative-externality section ends at 4.c.comparison, combining the completed DWL graph with the quantity inequality. After 4.b, shift the entire graph and its DWL bars, labels, and quantity markers 2.5 units left. Show Q-star < Q-hat on the right under the title Negative Externality. Add the yellow bottom takeaway: Markets for goods with negative externalities produce too much. Pause on this summary, then continue directly to the positive-externality sequence in section 5. Preserve the optional beneficial-exchange detour in the source without playing it.

#quote(block: true)[
  4.a → 4.a.private → 4.a.exchange → 4.a.return · Title: Negative Externality. Continue the fundamentals from the old animation_0 and Externalities scenes in C3_Corrective_Policy/03_Code.py: hold private demand, supply, and equilibrium fixed while comparing social marginal benefits and costs. Continue the dashed yellow evaluation guide left from 36 until MB = MSC at Q = 32, turning each remaining one-ton loss slice grey as the guide passes across its width. Tie the grey opacity directly to the guide quantity, keep the already swept loss bars visible, and retain all eight bars when the guide reaches 32; thereafter keep it fixed as the Q-star guide. Label the quantities with compact two-line stacks directly below their own guides: yellow Q-star above 32 and red Q-hat above 40. Align both values on one row, without equals signs or vertical staggering, leaving room for the bottom note. Bottom: Social welfare is maximized where MB = MSC. At Q = 32, clear the note, put a separate yellow outline around the existing 32nd-unit bars, retain the efficient point and dashed guide until the zoom begins, and continue without a pause. Zoom that exchange into the canonical close-up, fading the market and its markers. Keep the Negative Externality title and add the grey CMU Sans subtitle: The 32nd unit: the efficient quantity. Show the buyer and seller spheres with one pink Bystanders sphere between them and labels underneath. Use the same faint base opacity for the pink EXT region and the teal and orange bars. Place MB 5.60 and MSC 5.60 beside their equal-height value edges, MC 3.60 beside its edge, and a compact pink $2 centered inside the faint pink region, without the EXT prefix. Project the shared MB/MSC height to the right with a purple dashed guide, leaving the MSC label clear. Place TS = 0 in purple and DWL = 0 in white together beside that level. Since the boundaries coincide, show no vertical gap or grey loss region. Fade the guide with the close-up labels on return. Bottom: For this exchange, MB = MSC and there is no deadweight loss. Pause. Clear the people, labels, result, and subtitle, then carry the bars back to their exact original market slice. Restore the efficient-quantity markers, restoring all eight swept grey DWL bars with the market.

]

#quote(block: true)[
  4.b · Title: Negative Externality: DWL. Add the grey CMU Sans subtitle: Overproduction of goods that are too costly to society. Keep it through this DWL sequence and remove it when returning to the Efficiency title. Keep all eight grey loss bars already revealed by the moving yellow guide in 4.a. Do not run a separate reveal here. Keep all eight as separate one-ton bars, matching the widths and gaps of the existing exchange bars and following the sloping MSC and MB boundaries. Do not merge them into a triangle. Retain the separate bars through the remaining Negative Externality scenes. Label DWL. Keep the pink external-cost strips at opacity 0.8 throughout the DWL reveal: total external damage is not DWL. Bottom: These trades create deadweight loss because social cost exceeds benefit.

]

#quote(block: true)[
  4.c.comparison → 4.c.beneficial → 4.c.values → 4.c.private → 4.c.exchange → 4.c · Return title to Negative Externality. Keep the market graph and both quantity markers visible, and show a prominent Q-star < Q-hat result in the open upper-right area. Set the equation at scale 1.3, with Q-star yellow, Q-hat red, and the comparison sign white; label the quantities Efficient quantity and Market quantity in grey underneath their respective symbols. Show the yellow takeaway: Markets for goods with negative externalities produce too much. End the negative-externality section on this comparison, then continue to section 5. The following final-question material is retained for future use. Keep the dashed Q-star guide fixed at 32 while selecting the exchange at Q = 24, where MB is greater than MSC. Bottom: Are some exchanges worthwhile even with externalities on others? Fade in a new yellow outline around the existing 24th-unit bars without moving or removing the dashed Q-star guide. Pause, then zoom into the canonical exchange close-up. Fade the market and its DWL bars and markers during the zoom. Add the grey CMU Sans subtitle: The 24th unit: a quantity below the efficient quantity. Keep the teal buyer and orange seller spheres, with one pink Bystanders sphere between them and labels underneath. Show MB 7.20, MC 3.20, filled pink EXT 2, and MSC 5.20 beside their respective value edges. Use one common vertical scale for all three bars, leaving space below the subtitle. Pause on the values and question before revealing the answer. Shade the buyer's benefit above MSC in teal and show TS = 2 in purple and DWL = 0 in white at right. Keep the yellow question. Pause, then clear the people and detail labels, carry the exchange back to its exact market slice, restore the separate grey DWL bars and markers, including the dashed guide still fixed at 32. Continue directly to the brief positive-externality sequence below; preserve corrective-policy material for later notes.

]

=== 5 | Positive externalities

#quote(block: true)[
  5.a.words → 5.a · Title: Positive Externalities. Subtitle: A benefit received by others outside the market. Use the smaller grey CMU Sans subtitle, scale 0.6, left-aligned 0.10 units beneath the title. Transition directly from the completed negative-externality example to the same private market, with MB = 12 − Q/5 and MC = 2 + Q/20. Retain Q-hat = 40 and P-hat = 4, with the price on the vertical axis. Skip the crowd, cost stacking, and repeated arithmetic. Add a constant external benefit of 2 above MB, never above MC. Pink one-ton strips follow the demand slope, at opacity 0.8 through the market quantity and invisible beyond it, matching the extent of the production-cost bars; MC remains unchanged. Draw a solid teal MSB boundary at 14 − Q/5 and retain MB below it. On the right of a subtle grey divider, introduce Marginal social benefit = Marginal benefit + External benefit, with benefit terms teal, external benefit pink, and operators white. Pause, then transform to MSB = MB + EXT and pause. Keep the bottom teaching strip empty during this definition.

]

#quote(block: true)[
  5.b · Fade the definition and divider, recenter and enlarge the graph, and mark the efficient quantity where MSB meets MC: Q-star = 48, with a dashed yellow vertical guide. Preserve the red private market equilibrium at Q-hat = 40 and P-hat = 4. Stagger the quantity labels vertically so both remain readable. Show Q-hat < Q-star prominently in the upper right at scale 1.3, matching the negative-externality comparison: Q-hat red, Q-star yellow, and the comparison sign white. Place grey Market quantity and Efficient quantity labels beneath their respective symbols on one aligned row. Keep the bottom strip clear. Pause. Keep the Positive Externalities title and its subtitle.

]

#quote(block: true)[
  5.c.select → 5.c.values · Clear the bottom comparison and put one thin yellow box around the existing 44th-unit slice, using the same one-ton width and gaps. Pause, then carry that slice into the canonical buyer–seller close-up while the market fades. The subtitle becomes: The 44th unit: an exchange the market leaves out. Keep the teal Buyer and orange Seller spheres, with one pink Bystanders sphere between them and all labels beneath. Show MB 3.20 on the buyer side and MC 4.20 on the seller side. The filled pink EXT 2 region sits above the buyer's MB, reaching MSB 5.20; there is no external cost added to MC. Place each value label beside its exact edge, and EXT beside the pink region. Use the same common vertical scale as the preceding social-welfare close-ups. Bottom: What does society lose when this exchange is left out? Pause on these values before showing the welfare result. The values establish that private MB is less than MC, while social benefit exceeds MC.

]

#quote(block: true)[
  5.c.loss · Shade the buyer-side region between MC 4.20 and MSB 5.20 in grey. Show the one-dollar gap with purple guides and two labels at right: signed TS = +1 in purple and DWL = 1 in white. TS is the surplus the exchange would create; DWL is that surplus forgone because the exchange does not occur. Bottom: Leaving out this exchange creates 1 dollar of deadweight loss. Keep the pink benefit visible below the grey region and retain all three people and their labels. Pause.

]

#quote(block: true)[
  5.d · Remove the people and close-up labels, and carry the same grey loss region back onto the 44th-unit market slice, bounded by MC below and MSB above. Restore the market and its quantity markers and context subtitle. Add the other grey one-ton DWL bars between Q-hat = 40 and Q-star = 48, retaining the 44th-unit bar. Keep all eight bars separate, with the existing widths, gaps, and exact sloping boundaries; never merge them into a triangle. Label DWL above the grey bars. Bottom: The market leaves out worthwhile exchanges, creating deadweight loss. Stop here; no further arithmetic, repeated equilibrium close-up, or corrective policy in this short extension.

]

Graph externality bars use opacity 0.8 and appear only for units actually exchanged (Q ≤ 40 in these markets), matching the extent of the seller cost bars. Keep that opacity through the negative-externality efficiency and DWL sequences; do not dim it when revealing DWL. Curves still extend across the full quantity axis. Close-up fill opacities remain independently specified.

Two-decision pacing: both question headings are yellow. Reveal each set of dashed measurement guides and its MB comparison first, then pause at .private.compare or .social.compare before revealing the answer. Use a green check mark in place of Yes on either side. Keep Indifferent, Neutral, and No for their existing cases. Reveal the social TS/DWL values and welfare shading with the social answer after its pause. The existing answer holds remain.
