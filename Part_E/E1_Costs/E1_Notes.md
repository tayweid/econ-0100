---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

# Episode E1

How sellers choose

This video introduces costs as a way of measuring the tradeoffs firms face.

### Class on March 23

start with production data from last time

show the marginal product of labor

talk about Cobb Douglas

do the thing on the board with the increase in labor and the increase in output

show how this relates to costs through wages and fixed costs

talk about TC and VC and FC

then do averages

then do marginal cost

<!--
Consolidated 2026-11-11. The beat tables below are the November 9 animation review (E1_Storyboard_Revision.md) folded into these notes, its text unchanged (a vertical bar inside a table cell is written ∣). Rows 0.a, 1.a, 1.b, 2.h, 2.i.capital, 2.i, 3.e.divide and 3.e, and the “As built” sentence of 2.a, are carried from the October 30 comments and checked against E1_Animation.py. The October 30 comments (review corrections, build history, references, the $50-wage model, choices left for Taylor) are in _archive/2026-11-11_consolidation/E1_Notes_before_consolidation.md, and the review sheet is beside it.
Animation: E1_Animation.py, scene EpisodeE1. Playback order: 0 bumper; 1 Intro; 2 Costs from the Production Function; 3 Cost Curves; 4 Marginal Revenue (48 holds). Section 3 teaches 3.g (AVC), 3.h (AFC), 3.f (ATC), then 3.i.
Conventions and model. Keep the semester’s graphite background, azure topic titles, fixed-size gold teaching lines, white curve names, red tracing guides and readouts, grey contextual marks, and shared firm palette. The production function remains $Q = 10\sqrt{L}$, with labor measured in hours, a \$100 hourly wage, and \$1,000 fixed cost. Thus $L = Q^2/100$, variable cost is $Q^2$, and total cost is $1,000 + Q^2$. Reuse B2′s axis-coordinate polygons: adjoining rectangles, colored one-point outlines, and 35% colored fill. Each bar represents exactly one output unit. Earlier production bars recede to grey 10% fill and 35% outline opacity as the current bar is copied into its cost counterpart. Production bar widths show total labor required at each output level; cost bar heights show total cost at each output level. These sampled levels are not sums of rectangle areas. Use B2′s axis-label placement throughout E1: the white vertical-axis symbol sits to the left of the axis top, with its grey sans-serif unit caption immediately to its right; the horizontal-axis symbol sits below the axis end, with its unit caption immediately to its right on the same centerline. Use the existing small-graph text scales, with 0.35 spacing beside vertical symbols and 0.30 beside horizontal symbols. The grey 1,000 readout stays at the fixed-cost level on the cost axis. Temporarily hide it when the moving red cost readout occupies the same position.
Wage-dependent cost curves. At a wage of \$100 per hour, MC = 2Q, AVC = Q, and ATC = Q + 1,000/Q. The cost-curves section keeps the construction view: horizontal axes end at 70 units, TC at \$5,000 and average/marginal cost at \$144. Curves and bars run through output 60, leaving space for labels. Average-cost sweeps stop at 60 with their tracing points; the above-minimum comparison reaches 55. The minimum of ATC is at Q = √1,000, about 31.6, so the below-minimum demonstration holds at 20 units. Keep the ATC and AVC endpoint labels separated.
No beat in this animation for these directions in the prose: the linear production function and the labor sweep (old 2.p.linear, 2.q), the tangent on TC and VC (old 3.k.first, 3.l), and the marginal-revenue graph, market recap and next-time preview (old 4.c to 4.f, deferred to the next animation by the review). Spoken notes still need reconciliation after the author’s prose pass.
-->

## Intro

<!--
0 · Bumper and 1 · Intro. Beats, current build.
|   |   |
| --- | --- |
| 0.a | The shared bumper: raster MICROECONOMICS, flicker, Part E ∣ Episode 1 beneath it, and the subtitle in grey italic under it: “Costs of Production” (Taylor, 2026-11-04; the notes' line under the heading still reads “How sellers choose”). Pause, then clear. |
| 1.a | Title: How Sellers Choose. No subtitle. A numbered list left-aligned with the title, one row per fade: “1. How much to make?”, “2. How many workers to hire?”, “3. How to set prices?”. No bottom text. |
| 1.b | The list stays. Right of it a small graph (P and $/unit up, Q and units across) with an orange supply line labeled S / MC (the placeholder seller and its “?” box were dropped, Taylor, 2026-11-04). Bottom: “What are the incentives that give rise to the supply curve?” |
| 1.c–1.g | Keep the full-size centered matrix and the title “Market Structures” unchanged throughout. Reveal Perfect Competition, Monopoly, Monopolistic Competition, then Oligopoly in their cells, retaining earlier entries. Move the same close-fitting selection box between them with smooth easing. Keep the existing pauses 1.c–1.g. No side checklist, shrinking, repositioning, or title swaps. |

Carried from the October 30 comments; the entries for 1.d to 1.g’s checklists describe beats no longer in the animation.
Cues. 1.a → “In this sequence of videos…”. 1.b → “To this point, we’ve relied heavily on the supply curve…” through “To build a solid foundation…”. 1.c → “Lay out the set of videos on screen using the many, differentiated taxonomy”. 1.d → “The first context will be familiar…”. 1.e → “Second we’re going to look at monopolies…”. 1.f → “Third…”. 1.g → “And finally…”, and “Before dropping the big puchline…” over it.
Not built: “Can I do something with the Molly framing here?” is his open question; the seller is the guide's placeholder circle, not Molly.
-->

In this sequence of videos, we’re going to ask the question: how should sellers choose how much to make, how many workers to hire, and how to set prices?

*Show each of the three questions on the screen*

To this point, we’ve relied heavily on the supply curve to tell us seller’s quantity choices. The supply curve tells us how the choices firms make.

But to really get a handle both on how Molly should choose price, quantity, and inputs, we need to build a model of the incentives she faces, and how these incentives can tell us what she should do. And this is a case when understanding how she choose when faced with incentives not only gives us a picture of the firm, but can also help us find solutions when markets fail.

So that’s the question we’re setting off on in this sequence: what are the incentives that give rise to the supply curve? This question is more complicated than drawing a line, and depends a great deal on the who else is in the market.

*Show the supply curve, and the avatar with a question*

To build a solid foundation for seller’s choices we need to set up the costs and benefits they face.

*Can I do something with the Molly framing here?*

*Lay out the set of videos on screen using the many, differentiated taxonomy*

The first context will be familiar. We’ll look at perfectly competitive firms: firms in markets with many other sellers and many buyers selling homogeneous goods.

*List these out under the header “Competitive Firms” 1. Many sellers, 2. Many buyers, 3. Homogeneous goods*

Second we’re going to look at monopolies: where the firm is the only seller in the market, there are many buyers, and the level of differentiation between goods isn’t important since there is only one seller.

*Show the model*

Third we’re going to look at monopolistic competition: firms that offer slightly differentiated products in a market with many buyers and many sellers.

*Show the model*

And finally we’ll look oligopolies, environments with very few other sellers selling homogeneous goods to many buyers.

*Show the model*

Before dropping the big puchline for how to solve the firm’s problem, we need to build up their cost curves from the production function.

## Costs from the Production Function

<!--
2 · Costs from the Production Function. Beats, current build.
|   |   |
| --- | --- |
| 2.a | Retain the title “Costs From The Production Function” and add the grey subtitle “One example of a production function with diminishing marginal product.” Keep it through 2.i, then replace it with the wage at 2.j. As built: the production function graph on the left, L and worker hours across, Q and units up, both 0 to 100; F(L) = 10√L in white. No bottom text. |
| 2.b | Choose 20 output units on the vertical axis, draw the red guide across to F, then down to 4 labor hours. Bottom: “Choose an output quantity; find the labor hours it requires.” |
| 2.c | One output tracker moves 20 → 30 → 20; the guides, dot, and both numbers remain attached. Bottom: “Increasing output means we need more inputs, either from labor or capital.” |
| 2.d | Keep the first point. Double output to 40. Reveal the grey Q interval and +20 with the across guide, then the grey L interval and +12 with the down guide and 16-hour readout. Bottom: “Doubling output from 20 to 40 requires four times the labor.” |
| 2.e | Keep both earlier points. Add another 20 output units, reaching 60. Reveal its grey Q interval and +20 with the across guide, then its grey L interval and +20 with the down guide and 36-hour readout. Bottom: “Another 20 units require 20 more labor hours.” |
| 2.f | Keep both grey interval pairs, already revealed in 2.d and 2.e. Lines sit 0.14 scene units outside the axes, with small end gaps. The grey difference numbers have their own row/column, clear of the red cumulative readouts. Bottom: “More output requires increasingly large additions to labor.” |
| 2.g | Pulse each pair without resizing or relocating it. Bottom: “Equal additions to output require increasingly more labor.” |
| 2.h–2.i | Preserve the wage equation, temporary capital term, and pauses already in the animation. |
| 2.h | In the empty right half: “VC = L · w” (VC pink). Bottom: “The costs going to wages: just the labor hours times the wages.” |
| 2.i.capital | “+ K · r” joins the equation. Bottom: “There's also capital cost we need to think about in practice.” |
| 2.i | “+ K · r” fades out. Bottom: “To keep things simple here, we're going to focus on labor costs.” |
| 2.j | Clear the comparison marks and wage equation. Keep the production function at its original scale throughout this sequence, with labor and output axes from 0 to 100. Replace the contextual subtitle with “Wage: \$100 per hour”. On the right, introduce a close-up of the first cost bar: 0 to 1.2 units horizontally and \$0 to \$1,200 vertically. Show its grey fixed-cost base, the horizontal FC line, and grey 1,000 on the cost axis. Label the first bar “FC: \$1,000” beside its grey region. The production point and guides identify 1 unit and 0.01 labor hours. Bottom: “Even the first unit includes \$1,000 in fixed cost.” |
| 2.k | Carry a copy of the labor readout to “VC: \$1” beside the first cost bar as its pink variable-cost cap appears. Add the red cost point, guides, quantity 1, and total 1,001. Keep the cap mathematically proportional; the explicit label makes its small value readable. Separate the nearly coincident 1,001 and 1,000 labels vertically. Bottom: “One unit: \$1 in labor cost, plus \$1,000 in fixed cost.” |
| 2.l | Remove the first-unit heading and component labels. Settle the right graph once to 0–70 units and \$0–\$5,000; the left graph does not zoom. Retain the first cost bar, the FC line, the grey 1,000, and the tracked values. Add FC at the right endpoint of its line. Hold before the next transfers. Bottom: “Now follow the same output quantities: 20, 40, and 60.” |
| 2.l.five | Add units 2–5 individually. For each unit, move the red production point to the new output, reveal its pink horizontal production bar, then copy that bar into the corresponding pink cost cap while revealing its grey fixed-cost base. Earlier production bars become faint grey. Use 0.45 seconds to reach the unit and 0.65 seconds for its transfer, with smooth easing. Hold at five. Bottom: “Labor hours become variable cost at the same wage.” |
| 2.m | Continue the same unit-by-unit transfers to 20, with 0.2 seconds to reach each unit and 0.3 seconds to transfer it. Every intermediate unit gets a bar; neither graph changes scale. Then hold on 20 units, 4 labor hours and total cost 1,400. Bottom: “20 units need 4 labor hours: \$400 in variable cost.” |
| 2.n | Continue the same individual transfers through 40. During the buildup: “Each additional unit requires more labor than the one before.” Hold on 40 units, 16 labor hours and total cost 2,600. Bottom: “The next 20 units need 12 more hours: \$1,200 more cost.” |
| 2.o | Continue through 60 without rescaling or regrouping. During the buildup: “More labor for the next unit means a higher cost of producing it.” End with sixty adjoining one-unit bars on each graph and all geometry fixed. Hold on 60 units, 36 labor hours and total cost 4,600. Bottom: “The next 20 units need 20 more hours: \$2,000 more cost.” |
| 2.p | Fade the temporary red guides and readouts, retaining the production and cost bars. Draw TC through the fixed cost-bar tops, from (0, 1,000) to (60, 4,600). FC and its grey 1,000 axis value are already present. No bars or axes move. Bottom: “More labor for each additional unit means increasing marginal cost.” |

Carried from the October 30 comments; the entries for 2.p.linear and 2.q describe beats no longer in the animation.
Cues. 2.a → “To really understand firm behavior…”. 2.b → “… which takes the inputs labor and capital…”. 2.c → “Increasing output means we need more inputs…”. 2.d → “If we double labor input…”. 2.e → “And lets pick a third labor input…”. 2.f → “This is what’s called diminishing marginal return…”. 2.g → “As the production function becomes flatter…”. 2.h → “Increasing labor increases the costs going to wages…”. 2.i.capital and 2.i → “There’s also capital cost…”. 2.j → “Lets keep track of our variable costs…”. 2.k → “With zero output…”. 2.l → “So even with zero inputs and zero outputs…”. 2.m, 2.n, 2.o → the low, medium and high sentences. 2.p.linear and 2.p → “Different shaped production functions…”. 2.q → “With diminishing marginal return, as we add capacity…”.
Not built: the labor-and-capital input axis (see the top comment). “Keep doing this… And run through all three.” is read as a second run through the same three pairs (2.g), not a fourth step. The outline drew the FC line with the Fixed Costs brace in 2.l; it waits for 3.b, where his notes add it (“Add the FC line to the TC graph.”).
-->

To really understand firm behavior, we need to start with the production function …

*Set up the production function*

… which takes the inputs labor and capital and gives us some output quantity.

*Draw a line from labor to quantity.*

Increasing output means we need more inputs, either from labor or capital.

*Move labor up then down, shifting quantity*

If we double labor input, quantity goes up but doesn’t quite double.

*Add another labor line at double the first point, then show the quantity*

And lets pick a third labor input with the same increase in labor.

*Add another labor line at tripple the first point, then show the quantity*

This is what’s called diminishing marginal return: more inputs lead to increasingly small increases in outputs.

*Show a bracket under the input chunk and under the output chunk. And run through all three.*

As the production function becomes flatter, more inputs lead to more output but less efficiently.

*Keep doing this: Show a bracket under the input chunk and under the output chunk. And run through all three.*

Increasing labor increases the costs going to wages, just the labor hours times the wages.

*Show the equation for VC = L \* w*

There’s also capital cost we need to think about in practice, but to keep things simple here we’re going to focus on labor costs.

*Add K r to the equation, but then fade it out*

Lets keep track of our variable costs using the standard graph: quantity of output on the horizontal and value on the vertical.

*Add a cost graph to the right of the production function graph*

With zero output we still have some costs, like maintainace and rent.

*Point to zero outputs, map to the intputs required, then map to costs.*

So even with zero inputs and zero outputs, we still have some costs, what we call fixed costs.

*Show a bracket to the left of the graph saying ‘Fixed Costs’*

With low outputs we have higher costs.

*Point to low outputs, map to the inputs required, then map to costs.*

With medium outputs have again increase our costs.

*Point to medium outputs, map to the inputs required, then map to costs.*

And lastly, with high outputs our costs are higher again.

*Point to high outputs, map to the inputs required, then map to costs.*

Different shaped production functions tell very different stories about the costs of increasing the quantity of output.

*Change the shape of the production function to linear, then back again.*

With diminishing marginal return, as we add capacity, the total cost curve becomes steeper.

*Move labor input around, and map it to total cost, tracing as it goes*

## Cost Curves

<!--
3 · Cost Curves. Beats, current build.
|   |   |
| --- | --- |
| 3.a | Keep the two-second leftward pan, changing the title to “Cost Curves”. The production graph leaves and the cost graph takes its place. This is translation only: the cost graph keeps exactly the same horizontal and vertical scale, curve geometry and FC height. Its sixty bars remain, becoming neutral grey with 8% fill and 25% outline opacity during the pan. Carry the grey 1,000 axis value with the graph. |
| 3.b | FC is already on the graph. Only the teaching line enters: “Fixed costs, like rent, don’t vary with inputs.” |
| 3.c | Keep sixty faint grey one-unit cost bars as context, at the same positions and scale carried through the pan. Keep every bar stationary. Switch the highlight to the current one-unit interval, with a grey fixed-cost base and pink variable-cost portion; no rectangle slides along the axis. Keep the existing quantity motion 50 → 58 → 40. A red dot at TC, a horizontal dashed guide to the dollar axis, the total-cost readout, and the horizontal-axis quantity readout all follow that same tracker. Bottom: “Variable costs are the costs that do change with inputs.” |
| 3.d | Retain the stationary contextual bars and the highlighted FC/VC stack. Fade only the temporary readouts and VC label. Add the divider and equation TC = VC + FC, with total on the left. Do not draw a separate VC curve here. Keep that order through TC/Q = VC/Q + FC/Q and ATC = AVC + AFC. When the average-cost graph enters at 3.f, fade the selected FC/VC highlight but retain all sixty stationary grey TC bars at 8% fill and 25% outline opacity. Introduce the separate VC curve only when it is used to trace AVC in 3.g. |
| 3.e.divide | Under the identity: TC/Q = VC/Q + FC/Q, each fraction in its color. Bottom: “We find average costs simply by dividing these costs by the quantity.” |
| 3.e | Under that: ATC = AVC + AFC. The bottom line stays. |
| 3.f.setup | Move TC = VC + FC above the center of the left graph and ATC = AVC + AFC above the center of the right graph. Preserve the semantic equation colors and align both headings on one baseline. Hold at 3.f.setup before introducing the tracing points. Retain all sixty stationary grey TC bars at 8% fill and 25% outline opacity throughout the average-cost demonstrations. The revised teaching order is 3.g (AVC), 3.h (AFC), 3.f (ATC), then 3.i (their sum); the existing named holds remain attached to their original cost concept. |
| 3.g | Dim TC, FC, and their labels on the left to 22% opacity. Draw VC and emphasize VC and AVC in the identities above the graphs. Begin both tracing points at zero. One quantity tracker moves smoothly from 0 to 60, following VC on the left and drawing AVC on the right, with red guides and numbers on both graphs. Keep the average graph free of bars while tracing the curves. The curve ends at the moving point, and its label fades in during the last ten units. Finish everything together and hold at 3.g; no backward motion or curve-only extension. Bottom: “Average variable cost: variable cost divided by output.” Use fixed dash segments for guides that grow from zero. Average-cost readouts use one decimal place, so values such as 16.7 remain legible without truncating to 16. |
| 3.h | Fade out VC and its label on the left. Dim the completed AVC curve and label on the right to 22%. Restore FC and its label on the left; emphasize FC and AFC in the identities. Begin the FC point at zero output, with no AFC curve or bars drawn. Trace smoothly from 0 to 60. AFC is undefined at zero; keep its point and curve hidden until they enter together at the top of the visible range, then draw only as far as the moving point. Keep bars off the average graph. Stop the curve and point together and freeze them at the 3.h hold. Bottom: “Average fixed cost: the same fixed cost spread over more units.” |
| 3.f | Dim FC and AFC, keep AVC subdued, and restore TC on the left. Emphasize TC and ATC in the identities. Begin TC at Q = 0, where total cost is fixed cost. ATC is undefined at zero, so its point and guides stay hidden until positive output brings the average into the displayed range. Trace from 0 to 60 without average bars. Stop with the point at the curve endpoint, and freeze the curve and label before the 3.f hold. Bottom: “Average total cost: total cost divided by output.” VC remains absent from the left graph. |
| 3.i | Fade the tracing guides and readouts, restore the three average curves, the FC line, and both identities to full emphasis. Only now introduce one stacked bar at the final quantity, 60, with a red 60 below the axis. Use adjoining outlined rectangles over the interval from 59 to 60 with 35% fill. Grow the pink base from zero to AVC, then grow the grey AFC cap from AVC up to ATC. Place a small grey AFC label beside that gap. This shows the two heights adding to ATC without extra algebra. Bottom: “Average total cost is average variable cost plus average fixed cost.” Hold with all three curves visible. Remove the stacked bar, its quantity and gap labels, and the AFC curve when introducing marginal cost at 3.j. |
| 3.j | Clear the TC and FC curves and labels, the grey 1,000, and the two equations. VC has already left after AVC. Retain the sixty stationary grey total-cost bars and subdue ATC and AVC on the right; fade AFC and the temporary sum segments. Highlight adjacent bars 40 and 41 in grey. Put their red quantity labels under the axis, with short leaders separating the close values. Show two red dots at the bar tops and dashed horizontal guides to the vertical axis. Label the two costs 2,600 and 2,681 in red outside that axis; place the close labels in a column farther left, above and below their exact levels with thin elbow leaders. Keep the orange increment immediately beside its interval, in the space between the cost labels and the axis; the leaders pass above and below it. Between those two levels, just outside the vertical axis, draw a short orange interval and label it +81 in the same MC orange, following the earlier production-function interval placement. Remove the “One unit per bar” caption and the old floating increment at the bar top. Bottom: “One more unit adds \$81 to total cost.” |
| 3.k | Show the same increment as a red point on the right, with a red dashed horizontal guide to an orange 81-dollar readout and a red dashed vertical drop to the quantity axis. Both guides track that same point throughout the following sweep. No orange bars cover the average curves. The finite one-unit increment equals MC at the interval midpoint for this quadratic example. Bottom: “Marginal cost is the cost of producing one more unit.” |
| 3.m | Draw the orange MC line as the comparison moves from (40.5, 81) down to the first unit at (0.5, 1). Retain that entire visited section while working upward through the stationary bars to the 60th unit, extending MC when the point passes the previous maximum. Every quantity movement traces MC without erasing what has already been shown. The two quantities, their total costs, the nearby orange marginal-cost difference, and the orange right-axis cost readout update together. The final midpoint is (59.5, 119). The MC label appears during the final part of that same sweep; there is no curve-only extension afterward. Keep ATC and AVC subdued. Bottom: “At higher output, each increase costs more per unit.” For the following MC–ATC comparison, fade the entire total-cost graph, its bars, and all temporary readouts. Slide the average-cost graph into the center without changing its scale; restore ATC and AVC, leaving the space above the graph clear. The average-cost identity stays off screen. Keep this single centered graph through the rest of the cost-curves section. The total-cost graph and its identity do not return. |
| 3.n–3.r | Keep MC, ATC, and AVC centered while the red points compare MC with ATC below and above its minimum. Red dashed horizontal guides meet red ATC and MC labels with q as a subscript on the vertical axis; a red q marks the selected quantity below the horizontal axis. Fade the two separate cost labels as their levels converge to keep them from overlapping. At the minimum, mark the intersection in red and use one red “ATC_q = MC_q” axis label with the guides and q still visible. Remove those annotations at 3.p. AFC stays off the graph for the rest of the section. In 3.q, fade the small-output AVC tail below the visible ATC domain while introducing the long run. In 3.r, raise AVC onto ATC at fixed quantities over their common visible domain, avoiding the near-zero jump. Replace the two endpoint labels with “ATC = AVC.” Bottom: “With all costs variable, average variable cost equals average total cost.” Retain the same axes and scale throughout; no total-cost axes, curves, labels, bars, or identity reappear. |

Carried from the October 30 comments; the entries for 3.k.first and 3.l describe beats no longer in the animation.
Cues. 3.a → “Lets pause and do a little accounting here.”. 3.b → “We just found our total costs…”. 3.c → “Then on top of fixed costs…”. 3.d → “Total cost is the sum…”. 3.e.divide and 3.e → “While these costs are important…”. 3.f → “This gives us average total cost…”. 3.g → “… average variable cost…”. 3.h → “… and the less important average fixed cost.”. 3.i → “We’ll focus on…”. 3.j → “If you’re thinking about the cost of adding one more unit…”. 3.k.first and 3.k → “So to calculate marginal cost…”. 3.l → “For very small changes in quantity…”. 3.m → “The marginal cost curve, then, answers the question…”. 3.n.below and 3.n → “And there are two points of interest here…” through “The same is true for ATC.”. 3.o → “This means the marginal cost curve runs through the minimum…”. 3.p → “And you’ll notice…”. 3.q → “But even if I’m locked into a rental agreement…” and “And this is univeral…”. 3.r → “Rent is a fixed cost in the short run…” through “This idea will be important…”.
Not built: the AVC halves of the two points of interest, “when the marginal cost lies above it, average variable cost bends upward”, “whenever MC lies below it, AVC bends downward”, and the AVC point of “Highlight the minimum of ATC and AVC with points”. In this model AVC = Q/2 is a straight line under MC everywhere (they meet only at zero), so AVC has no lowest point to show; a U-shaped AVC needs a cubic VC (an S-shaped production function), a model choice for Taylor. The ATC version is built, running below-then-above, left to right (his paragraph says above first).
-->

Lets pause and do a little accounting here.

*Pan to the right so that the production function goes away and there’s room on the right of the cost curve for some accounting.*

We just found our total costs, which come from both the costs like rent that don’t vary with inputs, which we’ll call fixed costs.

*Add the FC line to the TC graph.*

Then on top of fixed costs, we have the costs that DO change with inputs, called variable costs.

*Draw a vertical line, with the part above FC colored in, and move it back and forth*

Total cost is the sum of fixed and variable costs.

*Show FC + VC = TC on screen*

While these costs are important, we usually care more about the average costs, which we find simply by dividing these costs by the quantity.

*Divide the costs by Q to show AVC, AFC, and ATC*

This gives us average total cost the cost associated with each unit of output …

*Create ATC on a second graph*

… average variable cost, the costs from variable inputs associated with each unit of output …

*Create AVC on a second graph*

… and the less important average fixed cost.

*Create AFC on a second graph*

We’ll focus on average total cost and average variable cost …

*Fade out AFC*

If you’re thinking about the cost of adding one more unit, however, its useful to also have marginal cost, the cost of adding another unit.

*Show the MC equation*

So to calculate marginal cost, we divide the change in total cost by the change in quantity.

*Show a few changes in quantity and how they map into MC on the second graph.*

For very small changes in quantity the marginal cost is equivalent to the slope of the total cost and variable cost curves.

*Show a tangent line running across TC and VC.*

The marginal cost curve, then, answers the question if I add one more unit, how much will my cost go up?

And there are two points of interest here. Because the AVC is an average of all the variable costs, when the marginal cost lies above it, average variable cost bends upward.

*Show some movement on the graphs*

And whenever MC lies below it, AVC bends downward.

*Show some movement on the graphs*

The same is true for ATC.

*Show some movement on the graphs*

This means the marginal cost curve runs through the minimum of ATC and AVC.

*Highlight the minimum of ATC and AVC with points*

And you’ll notice average total cost is higher than average variable cost. This is true in the short run because we have fixed costs like rent.

*Fade in AFC*

But even if I’m locked into a rental agreement in the short run, I don’t need to sign up for the lease for next year.

And this is univeral: In the long run, all costs are variable.

*Write ‘In the long run, all costs are variable’ on screen*

Rent is a fixed cost in the short run, but a variable cost in the long run. So when we look far enough out, the average variable cost curve and average total cost curve sit ontop of each other.

*Shift the AVC to the ATC and shift AFC to zero.*

And fixed cost, and therefore average fixed cost as well, go to zero.

This idea will be important when we talk about certain types of market environments.

## Marginal Revenue

<!--
4 · Marginal Revenue. Beats, current build.
|   |   |
| --- | --- |
| 4.a | Clear the cost graph and introduce the title “Marginal Revenue”. Center the objective $\max_q \mathrm{TR} - \mathrm{TC}$, with an upward brace spanning only TR − TC and “Profit” above it. Omit the separate π =. Bottom: “In this class, firms aim to maximize profit.” Hold before revealing the solution. |
| 4.b | Add a right-pointing mathematical implication arrow before MC = MR on the line beneath the objective, keeping MC orange and MR pink. Bottom: “A firm maximizes profit by choosing quantity where marginal cost equals marginal revenue.” End the animation on this card. Defer the illustrative marginal-revenue graph, market recap, and competitive-firm/monopoly preview to the next animation; do not include the former 4.c–4.f beats in E1. |

Carried from the October 30 comments; the entries for 4.c to 4.f describe beats no longer in the animation.
Cues. 4.a → “But before we look at specific types of markets…” and “In this class, we’re going look at firms who aim to maximize profit.”. 4.b → “Here’s where I drop the punch line…” and “This is not only going to be crucial…”. 4.c → “We’re going to look at specific shapes marginal revenue can take…”. 4.d.market → “Intuitively, when we’ve thought about buyers and sellers…”. 4.d.unit → “Sellers consider whether making one more unit…”. 4.d → “You can think about MC = MR in a similar way…”. 4.e → “The best decision, then…”. 4.f → “In the next video…”.
-->

But before we look at specific types of markets lets make an assumption about what firm’s aim to accomplish.

In this class, we’re going look at firms who aim to maximize profit.

*Show the equation for profit.*

Here’s where I drop the punch line for the next videos: It turns out a firm maximizes their profits when they set quantity where marginal cost is equal to marginal revenue.

*Show MR = MC on the screen*

This is not only going to be crucial to constructing the supply curve.

We’re going to look at specific shapes marginal revenue can take, but for a second lets just think about it as some abstract curve that can take many shapes.

*Change the slope up and down on the graph*

Intuitively, when we’ve thought about buyers and sellers, we’ve thought about their costs and benefits, and that markets set quantity where Marginal Benefits equal Marginal Costs, and that this was efficient in cases with no externalities.

*Do this with vertical lines representing their costs and benefits alongside the graph.*

*Show supply and demand intersecting*

Sellers consider whether making one more unit, until the benefits no longer exceed the cost of adding an additional unit.

*Show the benefit exceeding the cost*

You can think about MC = MR in a similar way: we want to continue to add units until when adding an aditional unit breaks even.

*Set the vertial lines equal*

The best decision, then, is the quantity where marginal cost equals marginal revenue.

*Show MR = MC on the screen*

In the next video we’ll look at the marginal revenue in Monopoly and Perfect Competition, and how the different incentives between the markets lead the monopolist to not maximize welfare in the market.

*Show the two models on the screen.*
