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
// | Unit revision 2026-10-07: Q is tons; all prices, benefits, and costs are dollars per ton. Keep the simple numerical curves as a rescaled teaching example rather than converting the old physical dataset. Remove grey explanatory captions from exchange close-ups: no average-values note, quantity-change footer, one-ton footer, or prose repeating the surplus result. Keep units on the axes and the active question/takeaway in yellow. CS/PS labels sit beside their regions without leaders; retain purple TS gap guides. MB sits directly left of the MB value line, and MC/MPC directly right of the MC value line, at the same height as that line. Restore the buyer/seller spheres and keep Buyer and Seller beneath their respective spheres in both opening close-ups. Keep value labels attached to the live bars through movement and return zooms.
// | Reveal revision 2026-10-07: each close-up pauses on MB and MC before price, surplus, or a welfare answer. In the opening review, keep the same MB/MC labels, spheres, and Buyer/Seller labels visible continuously. Show the established market price next, then fade in CS/PS. The first exchange asks: Is there a price that would make this exchange work? Fade the question as price appears. Keep the MB = MC exchange free of a price question. Externality comparisons first show private values, then external/social cost, then the welfare result. Ask about increasing/decreasing quantity, not changing it by one.
// | Visual revision 2026-10-07: all bottom teaching text is yellow (DEFINITION). Basic spheres stay fully opaque with depth testing enabled. Add and remove them directly; never opacity-fade spheres or groups containing them, since translucency exposes the rear mesh as internal discs. Unit-surplus comparisons use purple (TOTAL) guides from both bar tops to a labeled vertical gap.
// | Canonical exchange scene: retain the Part B teal buyer and orange seller spheres with shadows in every close-up, including the first exchange and MB = MC equilibrium exchange. Buyer and Seller stay beneath the spheres. Reveal the people with MB/MC and retain them through price, surplus, and welfare reveals; remove them directly only on the return to the market. Names do not replace spheres.
// | Model: MB = 12 − Q/5, MPC = 2 + Q/20, constant external cost 2 dollars per ton. Qm = 40; Qefficient = 32. Each comparison selects one one-ton exchange, with unit values evaluated at its rank on the curves. Add eight individual bars through ton 48, then select ton 48: MB 2.40, MC 4.40, TS −2. Reduce quantity to 35 and select removed ton 36: MB 4.80, MC 3.80, TS +1. With external cost 2 per ton, those same units have social TS −4 and −1. Never use an eight-ton average or multiply the displayed gap by a batch size. The opening close-ups use the boundary values at Q = 0 (MB 12, MC 2) and Q = 40 (MB = MC = 4).
// /plass:comment

=== 1 | Equilibrium and the First Welfare Theorem

#quote(block: true)[
  1.a · Title: Competitive equilibrium. Start with the full Part B spinach market: demand P = 12 − Q/5, supply P = 2 + Q/20, Q in tons, P in dollars per ton. Show equilibrium Q = 40, P = 4. Show faint orange production costs below MC (opacity 0.16), then fade in orange PS first and teal CS second (opacity 0.65), each with its label. The curves form the hard value boundaries. Use only the white abbreviations PS and CS, centered at the centroids of their own surplus triangles; do not spell out the full words. Continuous curves and exact sloping slices retain the B5 model.

]

#quote(block: true)[
  1.a.first.values → 1.a.first · Keep title: Competitive equilibrium; no subtitle. Select the starting exchange at Q = 0 with one thin yellow outline box around its full existing bar slice. Keep the bars teal and orange; do not add selection dots, vertical lines, or extra colored outlines. Pause on the highlighted exchange with no bottom annotation, then carry that same buyer/seller pair into a close-up as the market fades. Show faint full-height bars with hard MB = 12 and MC = 2 edges, the buyer/seller spheres, and Buyer/Seller labels beneath them. Anchor MB/MC labels beside their hard value lines. Omit the extra values/average caption. Withhold the price line, CS/PS fills, and surplus labels. Bottom question: Is there a price that would make this exchange work? Pause on the values. Fade the question as price appears. Keep MB/MC, spheres, and Buyer/Seller visible throughout the following reveals. First reveal the established price 4 line and label. In the next play, fade in stronger teal CS 8 and orange PS 2 above the respective faint bases, together with their surplus labels. Put the CS/PS labels immediately beside the corresponding regions, with no connector lines. Bottom: First exchange: both the buyer and seller gain. Pause again.

]

#quote(block: true)[
  1.a.first.return · Fade the close-up labels and bottom text; carry the same pair back to its original rank as the full market reappears. Merge both columns onto the same full-width market slice, with exact sloping CS/PS/cost boundaries. Fade out the buyer expenditure base as the columns merge. Remove the selected pair overlay and pause on the complete market.

]

#quote(block: true)[
  1.a.last.values → 1.a.last · Keep title: Competitive equilibrium; no subtitle. Put one thin yellow outline box around the last existing exchange at Q = 40, retaining the canonical red intersection marker. Do not add a yellow dot. Pause on the highlighted exchange with no bottom annotation. Fade the box as its marginal buyer/seller pair moves into the close-up on the same scale. First show only MB = MC = 4 dollars per ton, faint bars, hard value edges, and buyer/seller spheres with names underneath. MB and MC labels sit beside the equal-height value lines. Withhold price and the conclusion; pause on the values without asking which price would work. Keep the same MB/MC labels, spheres, and Buyer/Seller visible. Reveal the established price 4 line and label, then the yellow conclusion: At equilibrium, MB = MC = 4 dollars. There is no surplus area. These are exact boundary values, not an average over a finite interval.

]

#quote(block: true)[
  1.a.last.return · Fade the close-up labels and bottom text; carry the equal-value pair back to the same equilibrium point as the full market reappears, with both columns sharing exactly the same horizontal position. Remove the overlay and pause on the full market before asking about the next exchange.

]

#quote(block: true)[
  1.b → 1.b.select · Ask: What happens if we increase quantity? Add eight separate one-ton bars, one after another, beyond Q = 40 through Q = 48. Then clear the question, highlight the last actual bar, ton 48, and pause with no bottom annotation. Only this selected one-ton exchange moves into the close-up.

]

#quote(block: true)[
  1.c.values → 1.c · Carry the selected one-ton pair into the close-up, fading the market. Under the topic title, show the subtitle: The 48th unit: a quantity larger than in equilibrium. First show only faint bars, solid value edges, MB 2.40 and MC 4.40, with each value label at its line. Bottom question: Can any price make this trade worthwhile? Pause. Then reveal the purple gap labeled TS = −2 dollars, which is exactly MB minus MC for this one ton. Show MC \> MB. Bottom: This added ton costs more than it benefits. Keep the context subtitle through the answer, then fade it on the return to the market. No grey footers or aggregate totals.

]

#quote(block: true)[
  1.d · Return this same one-ton pair to its bar at rank 48, with both columns sharing the same horizontal bounds. Restore the full market and remove the eight added bars to return to Q = 40.

]

#quote(block: true)[
  1.e → 1.e.select · Keep title: Competitive equilibrium. Ask: What happens if we decrease quantity? Fade existing one-ton bars from ton 40 down through ton 36, reaching Q = 35. Select ton 36 from the existing market bars: reuse its cost polygon and the buyer bar’s existing demand edge and baseline. Put one thin yellow outline box around the full existing one-ton slice, keeping the bars teal and orange. Clear the question and pause on the highlight with no bottom annotation, then zoom in. Keep both columns in the same original one-unit-wide slice until the close-up separates them.

]

#quote(block: true)[
  1.f.values → 1.f · Carry that one-ton pair into the close-up. Under the topic title, show the subtitle: The 36th unit: a quantity smaller than in equilibrium. First show only MB 4.80 and MC 3.80 beside their hard value lines, faint bars, and spheres. Bottom question: Would removing this ton improve welfare? Pause. Then reveal MB \> MC and the purple gap labeled TS = +1 dollar for this single exchange. Bottom: Removing this ton loses more benefit than it saves in cost. Keep the context subtitle through the answer; omit grey footers.

]

#quote(block: true)[
  1.g · Fade the subtitle, return both columns to the exact original one-ton width and sloping value edges, and restore equilibrium. Retain the existing red curve-intersection marker without adding a yellow dot. Bottom: At equilibrium, MB = MC. Then change title to The First Welfare Theorem. One yellow takeaway, across two lines: When all benefits and costs are counted, competitive equilibrium maximizes total surplus.

]

=== 2 | Gary, Molly, and the people outside the trade

#quote(block: true)[
  2.a · Title: Negative externalities. Bottom: Who else is affected by this trade? Keep this question through the first bystander reveal, then replace it with the takeaway in 2.c. Enter the familiar Part B head-on deliberation: Gary at left, Molly beside him, spheres and shadows under the adjacent teal benefit and orange cost bars. This representative lot uses the averages over Q = 29 to 30: MB 6.10 and MPC 3.475, at price 4. Preserve the prior bar-pair geometry, adapted to leave the right side empty. Carry forward faint bases, strong CS/PS regions, and solid MB/MPC edges; the seller column reaches price above its MC boundary. One lot means one ton; omit the grey footer.

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
  3.d.select → 3.d.values → 3.d.costs → 3.d · Put a thin yellow outline box around the same one added ton at rank 48. Clear the question and pause on the highlight with no bottom annotation. Carry its one-unit-wide pair into the close-up. Repeat the subtitle: The 48th unit: a quantity larger than in equilibrium. First reveal only MSB 2.40 and MPC 4.40 beside their value lines. Bottom: What do the buyer and seller count? Pause. Then reveal external cost 2 stacked above MPC and label MSC 6.40 at its line. Bottom: What changes when we count the external cost? Pause again. Finally reveal TS = −4 dollars for this one ton. Bottom: Adding this ton reduces social welfare. Fade the subtitle when returning to the same one-ton market slice.

]

#quote(block: true)[
  3.e.select → 3.e.values → 3.e.costs → 3.e · Select the same one removed ton at rank 36, copying the existing private-cost and external-cost strips so its market width and sloping edges match exactly. Put a thin yellow outline box around the selected slice and pause with no bottom annotation before zooming in. In the close-up, repeat the subtitle: The 36th unit: a quantity smaller than in equilibrium. First reveal only MSB 4.80 and MPC 3.80 beside their value lines. Bottom: What do the buyer and seller count? Pause. Then reveal external cost 2 and MSC 5.80. Bottom: What changes when we count the external cost? Pause. Finally reveal TS = −1 dollar for this one ton. Bottom: Removing this ton increases social welfare. Fade the subtitle on the return to its original one-ton market slice.

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
