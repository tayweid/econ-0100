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
// | Visual revision 2026-10-07: all bottom teaching text is yellow (DEFINITION). Spheres keep depth testing enabled with smoother meshes, so their rear faces do not show through. Unit-surplus comparisons use purple (TOTAL) guides from both bar tops to a labeled vertical gap.
// | Model: MB = 12 − Q/5, MPC = 2 + Q/20, constant external cost 2 dollars per pound. Qm = 40; Qefficient = 32. Exact continuous interval areas; lot-comparison bar heights are interval averages. The introductory marginal-exchange close-up uses the exact boundary at Q = 40, where MB = MC = 4.
// /plass:comment

=== 1 | Equilibrium and the First Welfare Theorem

#quote(block: true)[
  1.a · Title: Competitive equilibrium. Start with the full Part B spinach market: demand P = 12 − Q/5, supply P = 2 + Q/20, Q in thousands of pounds, P in dollars per pound. Show equilibrium Q = 40, P = 4. Show faint orange production costs below MC (opacity 0.16), then consumer surplus in teal and producer surplus in orange (opacity 0.65). The curves form the hard value boundaries. Use white labels inside the stronger fills for contrast. Continuous curves and exact sloping slices retain the B5 model.

]

#quote(block: true)[
  1.a.first · Keep title: Competitive equilibrium; no subtitle. Select the first lot on the market graph, then carry that buyer/seller pair into a close-up as the market fades. Use the exact averages over Q = 0 to 1: MB 11.90 and MC 2.025 dollars per pound, at price 4. The buyer has a faint teal base below price and stronger teal CS above it; the seller has faint orange cost below MC and stronger orange PS up to price. Solid teal/orange edges mark MB/MC; a red line marks price. Label CS 7.90 and PS 1.975 dollars per pound beside their regions. Bottom: First exchange: both the buyer and seller gain.

]

#quote(block: true)[
  1.a.first.return · Fade the close-up labels and bottom text; carry the same pair back to its original rank as the full market reappears. Remove the selected pair overlay and pause on the complete market.

]

#quote(block: true)[
  1.a.last · Keep title: Competitive equilibrium; no subtitle. Select the exact intersection at Q = 40, P = 4, then carry its marginal buyer/seller pair into the close-up on the same scale as the first example. Both MB and MC are exactly 4 dollars per pound. Both faint bars end at price; there is no CS/PS region or surplus leader. Label the values per pound at Q = 40. Bottom: At equilibrium, MB = MC = 4 dollars. These are marginal boundary values, not averages over the whole 39–40 lot used later in the removal experiment.

]

#quote(block: true)[
  1.a.last.return · Fade the close-up labels and bottom text; carry the equal-value pair back to the equilibrium point as the full market reappears. Remove the overlay and pause on the full market before asking about the next exchange.

]

#quote(block: true)[
  1.b · Increase quantity from 40 to 41 while keeping the equilibrium price reference at 4. Highlight the added interval, with its buyer and seller bars side by side. Ask whether this trade improves welfare.

]

#quote(block: true)[
  1.c · Carry those same two bars into the B4 close-up, fading the market. Their heights are the interval averages: MB 3.90 and MC 4.025 dollars per pound. Thin purple horizontal guides connect both bar tops to a purple vertical gap labeled TS = −125 dollars for the full lot. Bottom: One more trade adds more cost than benefit. The 1,000-pound lot loses 125 dollars; do not confuse the average heights with the exact boundary values.

]

#quote(block: true)[
  1.d · Return the bars to their original interval and zoom back out. Restore Q = 40.

]

#quote(block: true)[
  1.e · Keep title: Competitive equilibrium. Decrease quantity from 40 to 39. Grey the lost surplus slice and select the removed buyer/seller pair.

]

#quote(block: true)[
  1.f · Carry that same pair forward. Average MB is 4.10, average MC is 3.975; the removed trade had positive surplus of 125 dollars per 1,000-pound lot. Connect both bar tops to the purple gap labeled TS = +125 dollars; below it, state that removing the trade loses 125 dollars. Bottom: One fewer trade removes more benefit than cost.

]

#quote(block: true)[
  1.g · Return the pair to the graph and restore equilibrium. Mark the exact curve intersection. Bottom: At equilibrium, MB = MC. Then change title to The First Welfare Theorem. One yellow takeaway, across two lines: When all benefits and costs are counted, competitive equilibrium maximizes total surplus.

]

=== 2 | Gary, Molly, and the people outside the trade

#quote(block: true)[
  2.a · Title: Negative externalities. Bottom: Who else is affected by this trade? Keep this question through the first bystander reveal, then replace it with the takeaway in 2.c. Enter the familiar Part B head-on deliberation: Gary at left, Molly beside him, spheres and shadows under the adjacent teal benefit and orange cost bars. This representative lot uses the averages over Q = 29 to 30: MB 6.10 and MPC 3.475, at price 4. Preserve the prior bar-pair geometry, adapted to leave the right side empty. Carry forward faint bases, strong CS/PS regions, and solid MB/MPC edges; the seller column reaches price above its MC boundary. One lot means 1,000 pounds.

]

#quote(block: true)[
  2.b · One small grey bystander appears off to the right. Reveal a pink external-cost piece above that person: 0.25 dollars per pound. Gary and Molly’s bars and price do not move.

]

#quote(block: true)[
  2.c · Reveal seven more small grey bystanders, each bearing another 0.25 dollars per pound from this same trade. Move each new piece into the same stack; eight pieces total 2 dollars per pound. All eight people remain below the stack. Bottom: One trade can impose small costs on many other people.

]

#quote(block: true)[
  2.d · Fade in a separate external-cost graph on the right, with quantity horizontal and external cost per pound vertical. Carry the eight pieces into a single one-lot rectangle of height 2, retaining seams between the pieces. Label the area: 2,000 dollars of external cost. This is total harm from one trade, not deadweight loss.

]

#quote(block: true)[
  2.e · Zoom the Gary–Molly pair down and reveal a second pair for the next lot, Q = 30 to 31: average MB 5.90, MPC 3.525. Add a second equal rectangle to the external-cost graph. Update the second pair’s CS, PS, and hard value edges to its own values. Its two parts correspond to two separate trades; the same bystanders can be affected by both.

]

#quote(block: true)[
  2.f · Keep the existing Negative externalities title on screen throughout the zoom-out; do not fade it in again. Pull back to the full market on the left and the full external-cost graph on the right. The two representative trades land at their own ranks, Q = 29 to 31, as the other lots appear. Retain faint production costs and stronger CS/PS on the market graph, with no overlapping expenditure fill. Both graphs use Q = 0 to 60 with matching horizontal scales. External-cost rectangles cover Q = 0 to 40 at height 2; total external cost is 80,000 dollars.

]

=== 3 | Constructing marginal social cost

#quote(block: true)[
  3.a · Title: Marginal social cost. Bottom: What is the full cost of a trade? Replace the question with the definition in 3.b. Fade the demand curve, benefit bars, surplus labels, and equilibrium annotations. Keep the private cost bars and MPC curve on the left and the externality rectangles on the right.

]

#quote(block: true)[
  3.b · Move the external-cost rectangles across one by one onto the tops of the matching private-cost slices. Each pink strip is height 2 above MPC; its sloping edges follow MPC exactly. Fade the now-empty external-cost axes. Introduce the dashed orange upper boundary and label MSC. Bottom: Marginal social cost = private cost + external cost. Show faint potential strips past the current quantity so MSC is defined across the graph.

]

#quote(block: true)[
  3.c · Title: Social welfare. Keep this topic title through both quantity comparisons and their returns to the market. Recenter and enlarge the combined graph. Restore demand as MPB = MSB, keep supply labeled MPC, and plot the unchanged private equilibrium Qm = 40, P = 4. The MSC intersection is not a new market equilibrium. Bottom: Would one more trade or one fewer trade improve welfare? Pause before revealing an answer.

]

#quote(block: true)[
  3.d · Select the added lot from 40 to 41, then carry the bar pair forward. Average MSB 3.90; private cost 4.025 with the pink external cost of 2 stacked above it. MSC 6.025 exceeds MSB. Purple guides connect both bar tops to the purple gap, labeled TS = −2,125 dollars for the lot. Bottom: One more trade reduces social welfare. Return to the same graph.

]

#quote(block: true)[
  3.e · Select the removed lot from 39 to 40 and bring it forward. Average MSB 4.10; private cost 3.975 plus external cost 2 gives MSC 5.975. The private gain is smaller than the harm to bystanders. Purple guides connect both bar tops to the purple gap, labeled TS = −1,875 dollars for the lot; removing this negative-surplus trade improves welfare. Bottom: One fewer trade increases social welfare. Return to the graph.

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
