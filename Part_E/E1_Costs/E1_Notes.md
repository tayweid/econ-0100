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
|   |   |
| --- | --- |
| Animation | E1_Animation.py, scene EpisodeE1, 48 holds. |
| Model | Q = 10√L with labor in hours, a \$100 wage and \$1,000 fixed cost: TC = 1,000 + Q², MC = 2Q, AVC = Q, ATC = Q + 1,000/Q, lowest at about 31.6 units. |
| Order | The animation traces AVC, then AFC, then ATC (3.g, 3.h, 3.f); the sentence in Cost Curves names them ATC, AVC, AFC and is left in that order. |
| Open | The paragraphs are the old video script and still need reconciling with the animation. “Can I do something with the Molly framing here?” is unanswered. |
| Marked | Everything inside addition marks is Claude’s: short bridges where the animation’s numbers or direction differ from the script. |
| Archive | The October 30 comments and the November 9 review sheet are in _archive/2026-11-11_consolidation/. |
-->

## Intro

<!--
|   |   |
| --- | --- |
| 0.a | Bumper with the subtitle “Costs of Production”. The line under this file’s heading still reads “How sellers choose”. |
-->

In this sequence of videos, we’re going to ask the question: how should sellers choose how much to make, how many workers to hire, and how to set prices?

*Show each of the three questions on the screen*

<!--
|   |   |
| --- | --- |
| 1.a | Title How Sellers Choose. A numbered list: “1. How much to make?”, “2. How many workers to hire?”, “3. How to set prices?”. |
-->

To this point, we’ve relied heavily on the supply curve to tell us seller’s quantity choices. The supply curve tells us how the choices firms make.

But to really get a handle both on how Molly should choose price, quantity, and inputs, we need to build a model of the incentives she faces, and how these incentives can tell us what she should do. And this is a case when understanding how she choose when faced with incentives not only gives us a picture of the firm, but can also help us find solutions when markets fail.

So that’s the question we’re setting off on in this sequence: what are the incentives that give rise to the supply curve? This question is more complicated than drawing a line, and depends a great deal on the who else is in the market.

*Show the supply curve, and the avatar with a question*

<!--
|   |   |
| --- | --- |
| 1.b | A small graph beside the list with an orange supply line, S / MC. “What are the incentives that give rise to the supply curve?” |
-->

To build a solid foundation for seller’s choices we need to set up the costs and benefits they face.

*Can I do something with the Molly framing here?*

*Lay out the set of videos on screen using the many, differentiated taxonomy*

<!--
|   |   |
| --- | --- |
| 1.c–1.g | Title “Market Structures”. The matrix fills one cell per hold: Perfect Competition, Monopoly, Monopolistic Competition, Oligopoly, with one selection box moving between them. |
-->

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

To really understand firm behavior, we need to start with the production function …

*Set up the production function*

<!--
|   |   |
| --- | --- |
| 2.a | Title “Costs From The Production Function”; subtitle “One example of a production function with diminishing marginal product.” The graph of F(L) = 10√L. |
-->

… which takes the inputs labor and capital and gives us some output quantity.

*Draw a line from labor to quantity.*

<!--
|   |   |
| --- | --- |
| 2.b | 20 units, traced across to F and down to 4 labor hours. “Choose an output quantity; find the labor hours it requires.” |
-->

Increasing output means we need more inputs, either from labor or capital.

*Move labor up then down, shifting quantity*

<!--
|   |   |
| --- | --- |
| 2.c | Output moves 20 → 30 → 20. “Increasing output means we need more inputs, either from labor or capital.” |
-->

If we double labor input, quantity goes up but doesn’t quite double.

*Add another labor line at double the first point, then show the quantity*

{++ The animation runs this the other way around: it doubles the output and asks what that takes. Going from 20 units to 40 takes four times the labor, 16 hours instead of 4. ++}

<!--
|   |   |
| --- | --- |
| 2.d | Output doubles to 40: +20 units, +12 hours. “Doubling output from 20 to 40 requires four times the labor.” |
-->

And lets pick a third labor input with the same increase in labor.

*Add another labor line at tripple the first point, then show the quantity*

{++ The same 20 units again, from 40 to 60, take 20 more hours. ++}

<!--
|   |   |
| --- | --- |
| 2.e | On to 60: +20 units, +20 hours. “Another 20 units require 20 more labor hours.” |
-->

This is what’s called diminishing marginal return: more inputs lead to increasingly small increases in outputs.

*Show a bracket under the input chunk and under the output chunk. And run through all three.*

<!--
|   |   |
| --- | --- |
| 2.f | Both interval pairs stay. “More output requires increasingly large additions to labor.” |
-->

As the production function becomes flatter, more inputs lead to more output but less efficiently.

*Keep doing this: Show a bracket under the input chunk and under the output chunk. And run through all three.*

<!--
|   |   |
| --- | --- |
| 2.g | Each pair pulses. “Equal additions to output require increasingly more labor.” |
-->

Increasing labor increases the costs going to wages, just the labor hours times the wages.

*Show the equation for VC = L \* w*

<!--
|   |   |
| --- | --- |
| 2.h | VC = L · w. “The costs going to wages: just the labor hours times the wages.” |
-->

There’s also capital cost we need to think about in practice, but to keep things simple here we’re going to focus on labor costs.

*Add K r to the equation, but then fade it out*

<!--
|   |   |
| --- | --- |
| 2.i.capital | + K · r joins the equation. “There's also capital cost we need to think about in practice.” |
| 2.i | + K · r fades. “To keep things simple here, we're going to focus on labor costs.” |
-->

Lets keep track of our variable costs using the standard graph: quantity of output on the horizontal and value on the vertical.

*Add a cost graph to the right of the production function graph*

{++ Say the wage is \$100 an hour and the fixed cost is \$1,000. ++}

<!--
|   |   |
| --- | --- |
| 2.j | Subtitle “Wage: \$100 per hour”. A close-up of the first cost bar, with its grey fixed-cost base. “Even the first unit includes \$1,000 in fixed cost.” |
-->

With zero output we still have some costs, like maintainace and rent.

*Point to zero outputs, map to the intputs required, then map to costs.*

{++ The very first unit takes a hundredth of an hour, \$1 of labor, on top of the \$1,000. ++}

<!--
|   |   |
| --- | --- |
| 2.k | Its pink variable-cost cap: VC \$1, total 1,001. “One unit: \$1 in labor cost, plus \$1,000 in fixed cost.” |
-->

So even with zero inputs and zero outputs, we still have some costs, what we call fixed costs.

*Show a bracket to the left of the graph saying ‘Fixed Costs’*

<!--
|   |   |
| --- | --- |
| 2.l | The cost graph settles to 0–70 units and \$0–\$5,000, with the FC line. “Now follow the same output quantities: 20, 40, and 60.” |
| 2.l.five | Units 2 to 5, one at a time: each production bar is copied into a cost bar. “Labor hours become variable cost at the same wage.” |
-->

With low outputs we have higher costs.

*Point to low outputs, map to the inputs required, then map to costs.*

{++ 20 units need 4 hours of labor: \$400 of variable cost. ++}

<!--
|   |   |
| --- | --- |
| 2.m | On to 20 units: 4 hours, total cost 1,400. “20 units need 4 labor hours: \$400 in variable cost.” |
-->

With medium outputs have again increase our costs.

*Point to medium outputs, map to the inputs required, then map to costs.*

{++ The next 20 units need 12 more hours: \$1,200 more. ++}

<!--
|   |   |
| --- | --- |
| 2.n | On to 40 units: 16 hours, 2,600. “The next 20 units need 12 more hours: \$1,200 more cost.” |
-->

And lastly, with high outputs our costs are higher again.

*Point to high outputs, map to the inputs required, then map to costs.*

{++ And the 20 after that need 20 more hours: \$2,000 more. ++}

<!--
|   |   |
| --- | --- |
| 2.o | On to 60 units: 36 hours, 4,600. “The next 20 units need 20 more hours: \$2,000 more cost.” |
-->

Different shaped production functions tell very different stories about the costs of increasing the quantity of output.

*Change the shape of the production function to linear, then back again.*

<!--
|   |   |
| --- | --- |
| Not built | The linear production function. |
-->

With diminishing marginal return, as we add capacity, the total cost curve becomes steeper.

*Move labor input around, and map it to total cost, tracing as it goes*

<!--
|   |   |
| --- | --- |
| 2.p | TC is drawn through the bar tops. “More labor for each additional unit means increasing marginal cost.” |
| Not built | The labor-and-capital input axis. “Keep doing this… And run through all three.” is read as a second pass over the same pairs, 2.g. |
-->

## Cost Curves

Lets pause and do a little accounting here.

*Pan to the right so that the production function goes away and there’s room on the right of the cost curve for some accounting.*

<!--
|   |   |
| --- | --- |
| 3.a | Title “Cost Curves”. A pan: the production graph leaves and the cost graph takes its place, its bars fading to grey. |
-->

We just found our total costs, which come from both the costs like rent that don’t vary with inputs, which we’ll call fixed costs.

*Add the FC line to the TC graph.*

<!--
|   |   |
| --- | --- |
| 3.b | “Fixed costs, like rent, don’t vary with inputs.” |
-->

Then on top of fixed costs, we have the costs that DO change with inputs, called variable costs.

*Draw a vertical line, with the part above FC colored in, and move it back and forth*

<!--
|   |   |
| --- | --- |
| 3.c | One bar is highlighted, grey fixed-cost base and pink variable part, as quantity moves 50 → 58 → 40. “Variable costs are the costs that do change with inputs.” |
-->

Total cost is the sum of fixed and variable costs.

*Show FC + VC = TC on screen*

<!--
|   |   |
| --- | --- |
| 3.d | TC = VC + FC beside the graph. |
-->

While these costs are important, we usually care more about the average costs, which we find simply by dividing these costs by the quantity.

*Divide the costs by Q to show AVC, AFC, and ATC*

<!--
|   |   |
| --- | --- |
| 3.e.divide | TC/Q = VC/Q + FC/Q. “We find average costs simply by dividing these costs by the quantity.” |
| 3.e | ATC = AVC + AFC. |
| 3.f.setup | The two identities move above a left graph of totals and a right graph of averages. |
-->

This gives us average total cost the cost associated with each unit of output …

*Create ATC on a second graph*

<!--
|   |   |
| --- | --- |
| 3.f | TC, traced on the left, draws ATC on the right. “Average total cost: total cost divided by output.” |
-->

… average variable cost, the costs from variable inputs associated with each unit of output …

*Create AVC on a second graph*

<!--
|   |   |
| --- | --- |
| 3.g | VC, traced on the left, draws AVC on the right from 0 to 60. “Average variable cost: variable cost divided by output.” |
-->

… and the less important average fixed cost.

*Create AFC on a second graph*

<!--
|   |   |
| --- | --- |
| 3.h | FC, traced on the left, draws AFC on the right. “Average fixed cost: the same fixed cost spread over more units.” |
-->

We’ll focus on average total cost and average variable cost …

*Fade out AFC*

<!--
|   |   |
| --- | --- |
| 3.i | One stacked bar at 60: pink AVC with a grey AFC cap reaching ATC. “Average total cost is average variable cost plus average fixed cost.” |
-->

If you’re thinking about the cost of adding one more unit, however, its useful to also have marginal cost, the cost of adding another unit.

*Show the MC equation*

{++ Take the 41st unit. 40 units cost \$2,600 and 41 cost \$2,681, so that one unit adds \$81. ++}

<!--
|   |   |
| --- | --- |
| 3.j | Bars 40 and 41 are highlighted: 2,600 and 2,681, with an orange +81 between them. “One more unit adds \$81 to total cost.” |
-->

So to calculate marginal cost, we divide the change in total cost by the change in quantity.

*Show a few changes in quantity and how they map into MC on the second graph.*

<!--
|   |   |
| --- | --- |
| 3.k | The same 81 as a point on the right graph. “Marginal cost is the cost of producing one more unit.” |
-->

For very small changes in quantity the marginal cost is equivalent to the slope of the total cost and variable cost curves.

*Show a tangent line running across TC and VC.*

<!--
|   |   |
| --- | --- |
| Not built | The tangent on TC and VC. |
-->

The marginal cost curve, then, answers the question if I add one more unit, how much will my cost go up?

<!--
|   |   |
| --- | --- |
| 3.m | The comparison sweeps down to the first unit and up to the 60th, tracing MC. “At higher output, each increase costs more per unit.” Then the average-cost graph alone, centered. |
-->

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

<!--
|   |   |
| --- | --- |
| 3.n–3.r | MC against ATC below its minimum, above it, and at it (“ATC_q = MC_q”). In 3.q and 3.r the long run: AVC rises onto ATC, labeled “ATC = AVC.” “With all costs variable, average variable cost equals average total cost.” |
| Not built | The AVC versions of the two points of interest: in this model AVC is a straight line under MC, with no lowest point. A U-shaped AVC needs a cubic VC. |
-->

And fixed cost, and therefore average fixed cost as well, go to zero.

This idea will be important when we talk about certain types of market environments.

## Marginal Revenue

But before we look at specific types of markets lets make an assumption about what firm’s aim to accomplish.

In this class, we’re going look at firms who aim to maximize profit.

*Show the equation for profit.*

<!--
|   |   |
| --- | --- |
| 4.a | Title “Marginal Revenue”. $\max_q \mathrm{TR} - \mathrm{TC}$, with a brace naming it Profit. “In this class, firms aim to maximize profit.” |
-->

Here’s where I drop the punch line for the next videos: It turns out a firm maximizes their profits when they set quantity where marginal cost is equal to marginal revenue.

*Show MR = MC on the screen*

<!--
|   |   |
| --- | --- |
| 4.b | An implication arrow and MC = MR beneath it. “A firm maximizes profit by choosing quantity where marginal cost equals marginal revenue.” The animation ends here. |
| Not built | Everything after this point: the marginal-revenue graph, the market recap and the next-video preview are deferred. |
-->

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
