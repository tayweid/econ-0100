---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

# Episode E1

How sellers choose

This video introduces costs as a way of measuring the tradeoffs firms face.

<!--
Review correction, 2026-10-30: AVC and AFC are now traced from VC and FC by the same division marks as ATC (3.g, 3.h), where they were drawn outright; in 3.l the two chord dots give way to one point of tangency on TC; 3.n.below holds at 30 units instead of 38, where MC and ATC sat almost on each other; Part C's market in 4.d is labeled D / MB and S / MC (his “Show supply and demand intersecting”) and its red crossing now stays on top of the unit's dots at 40; the output braces of 2.f sit a little further from the 50, 71 and 87. The beat lines below are updated to match.
Review correction, 2026-11-04 (Taylor): the braces of 2.f and 2.l are now thick lines lying on the axes; a worked line, TC = FC + L · w = 1,000 + L · 50 = TC, joins the stored results at 2.k and rolls with the output through 2.q; in 3.r the stacked words become TC = VC and ATC = AVC; 1.b drops the seller and labels supply S / MC; the bumper's subtitle is Costs of Production; the MB and MC columns of 4.d are filled at 40% instead of 16%. The beat lines below are updated to match.
Animation storyboard for E1_Animation.py, scene EpisodeE1. Built 2026-10-30 from these notes, the lead animator's beat outline, and the old E1 code (03_Code.py, run in ManimL as E1_Animation_original.py: CostsA and CostsB from the 2020-21 Tutorial 5.1 video, and the 2022 rewrite animation_0 to animation_4). Taylor writes the spoken notes; these comments list the beats in playback order, one comment at the top of each section, with every title, subtitle and bottom line quoted as built. Every beat ends on a literal self.pause in construct().
Playback order: 0 bumper; 1 Intro; 2 Costs from the Production Function; 3 Cost Curves; 4 Marginal Revenue (56 holds).
Carried over from the old code: CostsA's point-by-point mapping from output to labor to cost with the TC curve growing to each new cost point (2.k to 2.o) and its curvature change of F (2.p, now linear and back); CostsB's rise-over-run sweep along TC with MC growing behind it (3.k), its cost equations (FC + VC = TC, MC = ΔTC/ΔQ), the min-ATC point (3.o), AVC moving onto ATC (3.r) and the long-run line; animation_1's production function left and cost graph right with a pan to the averages (2.j, 3.a, 3.f) and its "In the long run, all costs are variable." line; animation_2's labor tracker with input and output brackets (2.b to 2.f). New in this build: the three questions, the seller with a question, the market-structures taxonomy and checklists (section 1); VC = L · w with K · r (2.h, 2.i); the Fixed Costs brace (2.l); the FC/VC bar (3.c); ATC, AVC and AFC traced by dividing TC, VC and FC by Q (3.f to 3.h); the tangent on TC and VC (3.l); the movement along ATC (3.n); the fixed part of cost rolling to zero (3.r); all of section 4. Superseded: animation_0's "Part D" outline card (the bumper and the taxonomy replace it); animation_3 (Cost Curves: some_accounting, create_averages, create_marginal_cost, create_marginal_revenue) and animation_4 (Marginal Revenue: create_marginal_revenue) were empty stubs, and animation_2's create_variable_cost_curve a stub.
References: C2_Animations.py and C3_Animations.py (red readouts on the axes, dashed guides, a grey divider beside the accounting, stored results under the title, trackers), B5_Animation.py (tracker-driven curves redrawn as polylines, rolling numbers), D3_Animation.py (bumper), E4_Animation.py (the taxonomy object, built there first, and the first line of the firm's-problem card with MC orange and MR pink).
Model (one firm for the whole episode, the old CostsB / E2 / E3 costs): output Q = F(L) = 10√L for L workers, 0 to 100; wage w = $50; fixed cost $1,000. So L = Q²/100, VC = w · L = Q²/2, TC = 1,000 + Q²/2, MC = Q, AVC = Q/2, AFC = 1,000/Q, ATC = Q/2 + 1,000/Q, lowest at Q = √2,000 ≈ 44.7 where MC = ATC ≈ 44.7. Labor lines: 25, 50, 75 workers give 50, 70.7, 86.6 units (shown 50, 71, 87; steps 50, 21, 16); 81 workers give 90. Output levels: 0 → 0 workers, $1,000; 20 → 4, $1,200; 50 → 25, $2,250; 80 → 64, $4,200; 30 → 9, $1,450; 90 → 81, $5,050. Linear F (Q = L): 80 units need 80 workers and cost $5,000; TC = 1,000 + 50Q. Division at 50 units: TC = 2,250 and ATC = 45; VC = 1,250 and AVC = 25; FC = 1,000 and AFC = 20 (so 20 + 25 = 45). A chord 20 units wide on TC centered at Q has slope exactly Q = MC (at 55: rise 1,100 over 20). Section 4: an abstract MR = 80 − bQ meets MC = Q at q* = 80/(1 + b): b = 1, 0, 3 give 40, 80, 20. The market of 4.d is Part C's: MB = 12 − Q/5, MC = 2 + Q/20, crossing at 40 units and $4; the 10th unit has MB $10.00 and MC $2.50. Next time: MC = Q with a flat P = MR at 60, and D = 120 − Q with MR = 120 − 2Q (MC = MR at 40); no numbers on screen. Every on-screen number was checked against these formulas (re-checked in review, 2026-10-30: 83 checks, all pass).
Graphs: square 4.2 by 4.2 graphs; production function origin (−5.8, −2.175), cost graph origin (1.8, −2.175); the pan slides both 7.6 to the left, so the cost graph lands at (−5.8, −2.175) and the averages graph takes (1.8, −2.175). Cost graph 0 to 100 units by $0 to $6,000; averages 0 to 100 by $0 to $120 (average curves stop at $105, clear of the axis caption). Section 4: the firm's graph 5.6 wide at (−2.8, −2.175); the market 5.0 wide at (−5.4, −2.175) with the two columns at x = 1.9 and 2.6.
Conventions (E_conventions.md, shared_E.md): plain Scene at 15 fps; the topic title in azure with every word capitalized; a grey subtitle only for stored results here (VC = L · w, AFC + AVC = ATC, the profit lines); one gold line in the bottom strip (scale 0.7443, centered, 0.05 from the bottom) or none; red guides, dots and readouts, prices and costs on the vertical axis, quantities under the horizontal; firm palette: MC orange, TC and ATC purple, VC and AVC pink, FC and AFC grey, F(L) white, demand and P = MR teal, MR pink; one tracker per moving quantity; old text removed before new text fades in. File header in shared_E.md's order (the maniml line and comments, then the PEP 723 block), as E4 and E5.
Not built: the Molly framing (his open question in the Intro); the AVC halves of the two points of interest in Cost Curves (see that section's comment); the labor-and-capital axis of "takes the inputs labor and capital" (the axis stays L; animation_2's L,K relabel was never called).
Choices left for Taylor: (1) The model: F(L) = 10√L, w = $50 and FC = $1,000 were chosen so the costs come out as CostsB's (and E2's and E3's); the old animation_1 used Q = √L, w = 2, FC = 80, and CostsB's rise-over-run used TC = Q²/100 + 10. The wage is on screen in the stored line “w = $50 per worker”, a line written for this build. (2) Lines written or adapted for this build, his to replace: the three questions (his first sentence, with question marks); the checklists for monopoly, monopolistic competition and oligopoly (from his sentences; the competitive one is his); bottom lines 2.e, 2.h, 2.l, 2.n (his “With medium outputs have again increase our costs.” smoothed), 2.p.linear, 3.b, 3.c, 3.e.divide, 3.n.below and 3.n (his AVC sentences said of ATC), 3.p, 4.a, 4.d.market, 4.d.unit, 4.d, 4.f. Trimmed from his sentences: 2.b, 2.f (without “in outputs”), 2.g (“it” for the production function), 2.j, 2.o, 2.q, 3.f, 3.g, 3.j, 3.k.first, 3.l (TC and VC curves), 3.o (without AVC), 3.r, 4.b, 4.c, 4.e (without “then”). His sentences as written: 1.b, 2.c, 2.d, 2.i.capital, 2.i, 2.k (maintenance spelled out), 2.m, 3.d, 3.h, 3.i, 3.m, 3.q. (3) Section 2's title is the notes' heading, every word capitalized, kept for the whole section; it could split into The Production Function and Total Cost. (4) The pan slides the graphs under a fixed title instead of moving a camera. (5) Quantity and cost readouts are numbers only (one quantity per axis, the axes named L, Q and $), not number-and-symbol rows; 4.c labels its quantity q* as the card does. (6) The run and rise are labeled ΔQ and ΔTC (CostsB said Rise) to match MC = ΔTC/ΔQ; the two dots are 20 units apart (CostsB's were 10) so the run, the rise and their labels have room at this scale; the sweep starts at 55 units, not CostsB's 10, so the labels clear FC, and VC steps aside during it. (7) The punch line reads MC = MR, as on his firm's-problem card (E4, E5) and in CostsB; his directions in Marginal Revenue say MR = MC. (8) The thesis is the line under the heading, without a period. (9) 4.f draws the two models as MR shapes (the outline's reading); the taxonomy with both cells boxed is the other reading of “Show the two models on the screen.” (10) 3.n runs below-then-above, left to right; his paragraph says above first. (11) At the end of 3.r the pink VC and AVC lie over TC and ATC; their words stack under TC's and ATC's. (12) 4.d uses Part C's market (MB = 12 − Q/5, MC = 2 + Q/20) for the buyers-and-sellers reminder.
-->

## Intro

<!--
0 · Bumper and 1 · Intro. Beats, as built.
0.a · The shared bumper: raster MICROECONOMICS, flicker, Part E | Episode 1 beneath it, and the subtitle in grey italic under it: “Costs of Production” (Taylor, 2026-11-04; the notes' line under the heading still reads “How sellers choose”). Pause, then clear.
1.a · Title: How Sellers Choose. No subtitle. A numbered list left-aligned with the title, one row per fade: “1. How much to make?”, “2. How many workers to hire?”, “3. How to set prices?”. No bottom text.
1.b · The list stays. Right of it a small graph (P and $/unit up, Q and units across) with an orange supply line labeled S / MC (the placeholder seller and its “?” box were dropped, Taylor, 2026-11-04). Bottom: “What are the incentives that give rise to the supply curve?”
1.c · Clear. Title: Market Structures. The taxonomy, E4's object in D1's Table look (grey rules, red row and column words): columns Homogeneous and Differentiated; rows Many Sellers, Few Sellers, One Seller, the one-seller row without a column rule. The four cells are empty. No bottom text.
1.d · Title: Competitive Firms. The grid shrinks to 0.72 and steps left to the title's margin; Perfect Competition fills its cell (many sellers, homogeneous) inside a red box; right of the grid his checklist, one row per fade: “1. Many sellers”, “2. Many buyers”, “3. Homogeneous goods”. No bottom text.
1.e · Title: Monopoly. Monopoly fills the one-seller row across both columns, the box moves to it, and the checklist becomes “1. One seller”, “2. Many buyers”, “3. Differentiation isn't important”.
1.f · Title: Monopolistic Competition. The many-sellers differentiated cell fills, the box moves, checklist “1. Many sellers”, “2. Many buyers”, “3. Slightly differentiated goods”.
1.g · Title: Oligopoly. The few-sellers homogeneous cell fills, the box moves, checklist “1. Few sellers”, “2. Many buyers”, “3. Homogeneous goods”. The few-sellers differentiated cell stays blank (his oligopoly sells homogeneous goods).
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
2 · Costs from the Production Function. Beats, as built. Title: Costs From The Production Function (the heading, every word capitalized) for the whole section.
2.a · Clear. The production function graph on the left: L and workers across, Q and units up, both 0 to 100; F(L) = 10√L in white, labeled F(L) at its end. No bottom text.
2.b · One tracker (workers) at 25: a red dashed guide drawn up from 25 workers to F, a red dot, then a red dashed guide drawn across to the Q axis; red 25 under the L axis and 50 left of the Q axis. Bottom: “The production function takes inputs and gives us some output quantity.”
2.c · The tracker rolls to 81 workers (90 units), then back to 25 (50 units), 2.4 s each; the dot, guides and both numbers follow. Bottom: “Increasing output means we need more inputs, either from labor or capital.”
2.d · The tracked line stays as the first labor line. A second line drawn up at 50 workers, then its dot and the guide across to 71 (70.7). Bottom: “If we double labor input, quantity goes up but doesn't quite double.”
2.e · A third line drawn up at 75 workers, then its dot and 87 (86.6). Bottom: “A third labor input with the same increase in labor.”
2.f · Thick grey lines lying on the axes, one pair per fade, with small gaps between neighbours: along the L axis for each step of 25 workers (0 to 25, 25 to 50, 50 to 75) and along the Q axis for each output step (0 to 50, 50 to 71, 71 to 87). Bottom: “Diminishing marginal return: more inputs lead to increasingly small increases.”
2.g · The three pairs pulse yellow in turn, 0.8 s each. Bottom: “As it becomes flatter, more inputs lead to more output but less efficiently.”
2.h · In the empty right half: “VC = L · w” (VC pink). Bottom: “The costs going to wages: just the labor hours times the wages.”
2.i.capital · “+ K · r” joins the equation. Bottom: “There's also capital cost we need to think about in practice.”
2.i · “+ K · r” fades out. Bottom: “To keep things simple here, we're going to focus on labor costs.”
2.j · The labor lines, their numbers and the step lines clear; the equation moves under the title as a grey stored result, “VC = L · w”, and “w = $50 per worker” fades in beside it. The cost graph fades in on the right: $ and dollars up, 0 to 6,000; Q and units across, 0 to 100. Bottom: “Quantity of output on the horizontal and value on the vertical.”
2.k · One tracker (the output) at zero: a red dot at 0 on F's Q axis with 0 beside it; then 0 workers under the L axis; then that 0 carried to the cost graph's Q axis; then a red dot at 1,000 on the cost axis with 1,000 beside it, and right of the wage, in the stored-results row, the worked line “TC = FC + L · w = 1,000 + 0 · 50 = 1,000” (TC purple, FC grey, L · w pink, the two numbers red). It reads the same tracker, so it follows every later point and roll, and fades with the other marks between points. Bottom: “With zero output we still have some costs, like maintenance and rent.”
2.l · A thick grey line lying on the cost axis from 0 to 1,000, labeled Fixed Costs in white just left of it; it stays to the end of the section. Bottom: “Even with zero inputs and zero outputs, we still have fixed costs.”
2.m · The zero marks fade and the output steps to 20. Point to it (red dot and 20 on F's Q axis); map it to the inputs (a guide drawn across to F, its dot, a guide drawn down to 4 workers); map it to costs (the 20 carried to the cost graph's Q axis as a guide is drawn up from it, the cost dot appears as TC, purple, grows from 1,000 to it, then a guide drawn across to 1,200 on the cost axis, and TC's label at its end). Bottom: “With low outputs we have higher costs.”
2.n · The same steps at 50 units: 25 workers, 2,250; TC grows to 50. Bottom: “With medium outputs, our costs increase again.”
2.o · The same steps at 80 units: 64 workers, 4,200; TC grows to 80. Bottom: “With high outputs, our costs are higher again.”
2.p.linear · One tracker on F's shape: F straightens into the diagonal and the traced TC into a straight line (1,000 + 50Q); the same 80 units now need 80 workers and cost 5,000, and the numbers roll there. Bottom: “Different production functions tell very different stories about costs.”
2.p · And back: 64 workers, 4,200. The bottom line stays.
2.q · The output rolls 80 → 30 → 90 (2.4 s, then 4 s): workers 64 → 9 → 81, cost 4,200 → 1,450 → 5,050, and TC is traced as far as the point goes. (At 100 the readouts would sit on the axis names.) Bottom: “With diminishing marginal return, the total cost curve becomes steeper.”
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
3 · Cost Curves. Beats, as built. Title: Cost Curves for the whole section.
3.a · The marks, the worked line and the Fixed Costs line fade while TC finishes its last stretch to 100 units. Then the pan: the title becomes Cost Curves (no subtitle) as both graphs slide 7.6 to the left in one 2 s eased move; the production function leaves the frame and the cost graph sits where it was, with room on the right. No bottom text.
3.b · A grey FC line at 1,000 across the cost graph, labeled FC. Bottom: “Fixed costs, like rent, don't vary with inputs.”
3.c · A vertical bar from the Q axis up to TC, grey up to FC and pink above it, labeled VC beside the pink part; one tracker moves it from 70 units to 95, then to 40. Bottom: “Variable costs are the costs that do change with inputs.”
3.d · The bar's label goes. The VC curve (pink, Q²/2 from the origin), labeled VC; a grey divider right of the cost graph, and in the space the pan made “FC + VC = TC” (FC grey, VC pink, TC purple). Bottom: “Total cost is the sum of fixed and variable costs.”
3.e.divide · Under it: FC/Q + VC/Q = TC/Q, each fraction in its color. Bottom: “We find average costs simply by dividing these costs by the quantity.”
3.e · Under that: “AFC + AVC = ATC”. The bottom line stays.
3.f · The divider, the first two rows and the bar clear; the last row moves under the title as a grey stored result, “AFC + AVC = ATC”, and the averages graph fades in on the right ($ and dollars per unit up, 0 to 120; Q and units across). One tracker moves a red point along TC (guides, its cost on the $ axis, its quantity under the axis) and a red point on the averages graph at the same quantity, the cost divided by the quantity, which traces ATC (purple): 10 → 90 units, then back to 50 as ATC completes to 100 and is labeled. Held: 2,250 and 50 on the cost graph, 45 and 50 on the averages graph. The same marks divide VC in 3.g and FC in 3.h. Bottom: “Average total cost: the cost associated with each unit of output.”
3.g · The marks clear and return on VC: the tracker moves the red point along VC from 10 units to 90 and back to 50, and each variable cost divided by its quantity traces AVC (pink, Q/2), which completes to 100 and is labeled AVC. Held: 1,250 and 50 on the cost graph, 25 and 50 on the averages graph. Bottom: “Average variable cost: the costs from variable inputs for each unit of output.”
3.h · The same on the FC line: the red point moves along FC at 1,000 (its guide across runs along the line), and 1,000 divided by each quantity traces AFC (grey, 1,000/Q, from $105), labeled AFC. Held: 1,000 and 50 on the cost graph, 20 and 50 on the averages graph. Bottom: “And the less important average fixed cost.”
3.i · The division marks and AFC fade out. Bottom: “We'll focus on average total cost and average variable cost.”
3.j · “MC = ΔTC/ΔQ” (MC orange) in the open space above TC. Bottom: “Marginal cost: the cost of adding another unit.”
3.k.first · VC and its label step aside. On TC two red dots 20 units apart around 55 units (45 and 65), a yellow dashed run labeled ΔQ and rise labeled ΔTC, and the orange chord through the dots; on the averages graph a red point at 55, the chord's slope, labeled MC. Bottom: “Divide the change in total cost by the change in quantity.”
3.k · One tracker slides the pair up TC to 85 units (4 s); MC (orange) grows behind the red point on the averages graph. The bottom line stays.
3.l · The run shrinks to nothing (2.4 s) and the chord settles onto the tangent, ΔQ and ΔTC fading with it; the two dots give way to one red point of tangency. VC returns with a parallel orange tangent and a red dot at the same quantity; both run down the curves to 30 units while the MC point follows and MC extends down. Bottom: “For very small changes, marginal cost is the slope of the TC and VC curves.”
3.m · The tangents and points clear; MC completes across the graph and keeps its label. Bottom: “If I add one more unit, how much will my cost go up?”
3.n.below · The MC equation clears. One tracker moves a red point along ATC with a red point on MC at the same quantity and a red dashed guide up from the axis: 15 → 30 units, MC under ATC and ATC falling. Bottom: “When MC lies below ATC, ATC bends downward.”
3.n · 30 → 90 units: past the crossing MC lies above ATC and ATC rises. Bottom: “When MC lies above ATC, ATC bends upward.”
3.o · Back to 44.7 units, where the two points meet; they fade and a yellow point marks ATC's lowest point, on MC. Bottom: “The marginal cost curve runs through the minimum of ATC.”
3.p · The yellow point goes and AFC fades back in. Bottom: “ATC is higher than AVC in the short run because we have fixed costs like rent.”
3.q · Bottom: “In the long run, all costs are variable.”
3.r · One tracker (the fixed part of cost) rolls from 1,000 to zero (4 s): the FC line drops to the Q axis and VC rises onto TC; AFC drops to the axis and AVC rises onto ATC (AVC turns U-shaped, its lowest point on MC); TC and ATC do not move. FC's and AFC's words fade; VC's and AVC's stop just under TC's and ATC's, then each pair becomes one word: “TC = VC” at TC's end and “ATC = AVC” just above ATC's end. Bottom: “Fixed cost, and therefore average fixed cost as well, go to zero.”
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
4 · Marginal Revenue. Beats, as built. Title: Marginal Revenue for 4.a to 4.e.
4.a · Clear. “max over q: π = TR − TC” centered (the first line of the firm's-problem card in E4 and E5). Bottom: “In this class, firms aim to maximize profit.”
4.b · “MC = MR” under it (MC orange, MR pink). Bottom: “A firm maximizes profit where marginal cost equals marginal revenue.”
4.c · Both lines move under the title as grey stored results. The firm's per-unit graph ($ and dollars per unit, 0 to 120; Q and units, 0 to 100): MC (orange) and ATC (purple), labeled. MR is a pink line from 80 on the price axis whose slope one tracker tilts: 40 units where it meets MC, then flat (80 units), then steep (20 units), then back (40); a red point where MC = MR, its dashed drop and the rolling quantity under the axis with q* under it. AVC is left off (it shares MR's pink). Bottom: “Think of marginal revenue as some abstract curve that can take many shapes.”
4.d.market · The firm's graph clears. Part C's market, supply and demand: D / MB (teal) and S / MC (orange) on P and $/unit by Q and units, crossing at a red point (40 units, $4). Bottom: “Markets set quantity where marginal benefits equal marginal costs.”
4.d.unit · One unit, the 10th: a white line up from 10 with a teal dot on MB and an orange dot on MC, and a red 10 under the axis; alongside the graph two columns on the same price scale (40% fill, solid top edge, grey base): MB at $10.00 (teal, value on the left) and MC at $2.50 (orange, value on the right), named under the base. Bottom: “Sellers make one more unit while the benefits exceed the cost of adding it.”
4.d · One tracker adds units from 10 to 40 (4 s): the line, dots, number, columns and values roll until both columns read $4.00 at the red crossing, which stays on top of the unit's two dots. Bottom: “Keep adding units until an additional unit breaks even.”
4.e · “MC = MR”, large (MC orange, MR pink), right of the equal columns. Bottom: “The best decision is the quantity where marginal cost equals marginal revenue.”
4.f · Clear. Title: Next Time. Two small panels with white headings, no numbers: Perfect Competition (MC orange and a flat teal line labeled P = MR, a red point where they cross) and Monopoly (D teal, MR pink at twice demand's slope, MC orange, a red point where MC = MR). Bottom: “Marginal revenue in monopoly and perfect competition.”
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
