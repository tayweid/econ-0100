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
// | Bar revision 2026-10-07: start with the full market, carry the first exchange into a close-up and back, then carry the exact marginal exchange at Q = 40 into a close-up and back. No subtitles on these close-ups. MB and MC have hard value edges; base regions use opacity 0.16, CS/PS use 0.65. Buyer column ends at MB, seller column ends at price/revenue with MC marked inside. No green payment fill. Topic titles stay stable while yellow teaching lines change.
// | Unit revision 2026-10-07: Q is tons; all prices, benefits, and costs are dollars per ton. Keep the simple numerical curves as a rescaled teaching example rather than converting the old physical dataset. Remove the values/average captions. CS/PS labels sit beside their regions without leaders; retain purple TS gap guides. MB sits directly left of its full benefit bar and MC/MPC directly right of its cost region. Keep value labels attached to the live bars through movement and return zooms.
// | Reveal revision 2026-10-07: each close-up pauses on MB and MC before price, surplus, or a welfare answer. Externality comparisons first show private values, then external/social cost, then the welfare result. Ask about increasing/decreasing quantity, not changing it by one.
// | Visual revision 2026-10-07: all bottom teaching text is yellow (DEFINITION). Spheres keep depth testing enabled with smoother meshes, so their rear faces do not show through. Unit-surplus comparisons use purple (TOTAL) guides from both bar tops to a labeled vertical gap.
// | Model: MB = 12 − Q/5, MPC = 2 + Q/20, constant external cost 2 dollars per ton. Qm = 40; Qefficient = 32. Quantity comparisons use exact averages over Q = 40 to 48 and Q = 32 to 40 (8 tons each). The opening close-ups use the boundary values at Q = 0 (MB 12, MC 2) and Q = 40 (MB = MC = 4).
// /plass:comment

=== 1 | Equilibrium and the First Welfare Theorem

#quote(block: true)[
  1.a · Title: Competitive equilibrium. Start with the full Part B spinach market: demand P = 12 − Q/5, supply P = 2 + Q/20, Q in tons, P in dollars per ton. Show equilibrium Q = 40, P = 4. Show faint orange production costs below MC (opacity 0.16), then consumer surplus in teal and producer surplus in orange (opacity 0.65). The curves form the hard value boundaries. Use white labels inside the stronger fills for contrast. Continuous curves and exact sloping slices retain the B5 model.

]

#quote(block: true)[
  1.a.first.values → 1.a.first · Keep title: Competitive equilibrium; no subtitle. Select the starting exchange at Q = 0 and carry its buyer/seller pair into a close-up as the market fades. Show faint full-height bars with hard MB = 12 and MC = 2 edges, and party labels. Omit the extra values/average caption. Withhold the price line, CS/PS fills, and surplus labels. Bottom question: What price would make both people willing to trade? Pause. Then reveal price 4, stronger teal CS 8 and orange PS 2 above the respective faint bases. Put the CS/PS labels immediately beside the corresponding regions, with no connector lines. Bottom: First exchange: both the buyer and seller gain. Pause again.

]

#quote(block: true)[
  1.a.first.return · Fade the close-up labels and bottom text; carry the same pair back to its original rank as the full market reappears. Merge both columns onto the same full-width market slice, with exact sloping CS/PS/cost boundaries. Fade out the buyer expenditure base as the columns merge. Remove the selected pair overlay and pause on the complete market.

]

#quote(block: true)[
  1.a.last.values → 1.a.last · Keep title: Competitive equilibrium; no subtitle. Select the exact intersection at Q = 40 and carry its marginal buyer/seller pair into the close-up on the same scale. First show only MB = MC = 4 dollars per ton, faint bars, and hard value edges. Withhold price and the conclusion. Bottom question: What price would make this exchange possible? Pause. Then reveal price 4 and the yellow conclusion: At equilibrium, MB = MC = 4 dollars. There is no surplus area. These are exact boundary values, not an average over a finite interval.

]

#quote(block: true)[
  1.a.last.return · Fade the close-up labels and bottom text; carry the equal-value pair back to the same equilibrium point as the full market reappears, with both columns sharing exactly the same horizontal position. Remove the overlay and pause on the full market before asking about the next exchange.

]

#quote(block: true)[
  1.b · Ask: What happens if we increase quantity? Move the evaluated quantity from 40 to 48 while keeping the equilibrium price reference at 4. Highlight the whole added interval and the buyer/seller rectangles representing its average values. The exact loss triangle has corners (40,4), (48,2.4), and (48,4.4).

]

#quote(block: true)[
  1.c.values → 1.c · Carry the selected pair into the close-up, fading the market. First show only the full faint bars, solid value edges, average MB 3.20 and MC 4.20 dollars per ton, and the quantity change 40 to 48 tons. Bottom question: Can any price make these added trades worthwhile? Pause before any purple gap, TS value, inequality, or answer. Then connect the bar tops to a purple gap labeled TS = −8 dollars for the full increase. Show MC \> MB. Bottom: Increasing quantity adds more cost than benefit.

]

#quote(block: true)[
  1.d · Return both bars to the same full quantity interval, restoring its exact sloping curve boundaries, and zoom back out. Restore Q = 40.

]

#quote(block: true)[
  1.e · Keep title: Competitive equilibrium. Ask: What happens if we decrease quantity? Move evaluated quantity from 40 to 32. Fade all eight removed cost/CS/PS slices, highlight the exact lost-surplus triangle with corners (32,3.6), (40,4), and (32,5.6), and select the rectangles representing the removed interval’s averages.

]

#quote(block: true)[
  1.f.values → 1.f · Carry that same pair into the close-up. First show only average MB 4.80 and MC 3.80 dollars per ton, the faint bars with hard value edges, and the decrease from 40 to 32 tons. Bottom question: Would removing these trades improve welfare? Pause. Then reveal MB \> MC, the purple gap labeled TS = +8 dollars for these trades, and the fact that removing them loses 8 dollars. Bottom: Decreasing quantity removes more benefit than cost.

]

#quote(block: true)[
  1.g · Return the pair to the graph and restore equilibrium. Mark the exact curve intersection. Bottom: At equilibrium, MB = MC. Then change title to The First Welfare Theorem. One yellow takeaway, across two lines: When all benefits and costs are counted, competitive equilibrium maximizes total surplus.

]

=== 2 | Gary, Molly, and the people outside the trade

#quote(block: true)[
  2.a · Title: Negative externalities. Bottom: Who else is affected by this trade? Keep this question through the first bystander reveal, then replace it with the takeaway in 2.c. Enter the familiar Part B head-on deliberation: Gary at left, Molly beside him, spheres and shadows under the adjacent teal benefit and orange cost bars. This representative lot uses the averages over Q = 29 to 30: MB 6.10 and MPC 3.475, at price 4. Preserve the prior bar-pair geometry, adapted to leave the right side empty. Carry forward faint bases, strong CS/PS regions, and solid MB/MPC edges; the seller column reaches price above its MC boundary. One lot means one ton.

]

#quote(block: true)[
  2.b · One small grey bystander appears off to the right. Reveal a pink external-cost piece above that person: 0.25 dollars per ton. Gary and Molly’s bars and price do not move.

]

#quote(block: true)[
  2.c · Reveal seven more small grey bystanders, each bearing another 0.25 dollars per ton from this same trade. Move each new piece into the same stack; eight pieces total 2 dollars per ton. All eight people remain below the stack. Bottom: One trade can impose small costs on many other people.

]

#quote(block: true)[
  2.d · Fade in a separate external-cost graph on the right, with quantity horizontal and external cost per ton vertical. Carry the eight pieces into a single one-lot rectangle of height 2, retaining seams between the pieces. Label the area: 2 dollars of external cost. This is total harm from one trade, not deadweight loss.

]

#quote(block: true)[
  2.e · Zoom the Gary–Molly pair down and reveal a second pair for the next lot, Q = 30 to 31: average MB 5.90, MPC 3.525. Add a second equal rectangle to the external-cost graph. Update the second pair’s CS, PS, and hard value edges to its own values. Its two parts correspond to two separate trades; the same bystanders can be affected by both.

]

#quote(block: true)[
  2.f · Keep the existing Negative externalities title on screen throughout the zoom-out; do not fade it in again. Pull back to the full market on the left and the full external-cost graph on the right. The two representative trades land at their own ranks, Q = 29 to 31, as the other lots appear. Each trade’s buyer and seller pieces share the full width of its market slice and match its cost, CS, and PS regions exactly; fade the buyer expenditure base during the merge. Retain faint production costs and stronger CS/PS on the market graph, with no overlapping expenditure fill. Both graphs use Q = 0 to 60 with matching horizontal scales. External-cost rectangles cover Q = 0 to 40 at height 2; total external cost is 80 dollars.

]

=== 3 | Constructing marginal social cost

#quote(block: true)[
  3.a · Title: Marginal social cost. Bottom: What is the full cost of a trade? Replace the question with the definition in 3.b. Fade the demand curve, benefit bars, surplus labels, and equilibrium annotations. Keep the private cost bars and MPC curve on the left and the externality rectangles on the right.

]

#quote(block: true)[
  3.b · Move the external-cost rectangles across one by one onto the tops of the matching private-cost slices. Each pink strip is height 2 above MPC; its sloping edges follow MPC exactly. Fade the now-empty external-cost axes. Introduce the dashed orange upper boundary and label MSC. Bottom: Marginal social cost = private cost + external cost. Show faint potential strips past the current quantity so MSC is defined across the graph.

]

#quote(block: true)[
  3.c · Title: Social welfare. Keep this topic title through both quantity comparisons and their returns to the market. Recenter and enlarge the combined graph. Restore demand as MPB = MSB, keep supply labeled MPC, and plot unchanged private equilibrium Qm = 40, P = 4. The MSC intersection is not a new market equilibrium. Bottom: Would increasing or decreasing quantity improve welfare? Pause before revealing an answer.

]

#quote(block: true)[
  3.d.select → 3.d.values → 3.d.costs → 3.d · Select the increase from Q = 40 to 48 and carry the average-value bars forward. First reveal only average MSB 3.20 and MPC 4.20 dollars per ton, with no pink cap or welfare answer. Bottom: What do the buyer and seller count? Pause. Then reveal external cost 2 stacked above MPC and label MSC 6.20. Bottom: What changes when we count the external cost? Pause again. Finally show the purple gap and TS = −24 dollars for the added 8 tons. Bottom: Increasing quantity reduces social welfare. Return to the same graph.

]

#quote(block: true)[
  3.e.select → 3.e.values → 3.e.costs → 3.e · Select the decrease from Q = 40 to 32 and carry the removed interval’s average-value bars forward. First reveal only average MSB 4.80 and MPC 3.80 dollars per ton. Bottom: What do the buyer and seller count? Pause. Then reveal external cost 2 and MSC 5.80. Bottom: What changes when we count the external cost? Pause. Finally show the purple gap labeled TS = −8 dollars for these trades; removing them increases welfare by 8 dollars. Bottom: Decreasing quantity increases social welfare. Return to the same graph.

]

=== 4 | Efficient quantity and deadweight loss

#quote(block: true)[
  4.a · Title: Efficient quantity. Continue the fundamentals from the old animation_0 and Externalities scenes in C3_Corrective_Policy/03_Code.py: hold private demand, supply, and equilibrium fixed while comparing social marginal benefits and costs. Move an evaluation guide left from 40 until MSB = MSC at Q = 32. Retain the separate Qm = 40 marker. Bottom: Social welfare is maximized where MSB = MSC.

]

#quote(block: true)[
  4.b · Title: Deadweight loss. Accumulate the grey social-loss slices between 32 and 40, then show the exact triangle between MSC and MSB. Label DWL. Keep the pink external-cost strips visually distinct: total external damage is not DWL. Bottom: These trades cost society more than they benefit society.

]

#quote(block: true)[
  4.c · Return title to Efficient quantity. Show an evaluation marker at Q = 24, where MSB is greater than MSC, then return it to 32. Bottom: Some production is worthwhile even when it causes harm. Stop here for the current intro build; preserve the old notebook’s positive-externality and corrective-policy material as the source for later notes.

]
