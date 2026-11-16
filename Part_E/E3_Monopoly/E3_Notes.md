---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

# Monopoly | Episode E3

*Market power breaks the efficiency of markets.*

| Minutes | Animation or board work | Purpose |
| --- | --- | --- |
| Warmup | Exercise E3 Warmup on the board | Predict what one more sale adds when the price has to fall. |
| 0–3 | Bumper (`0.a`), then `1.a.last` through `1.c` | One seller; downward-sloping demand; choose a trial quantity and ask its price. |
| 3–11 | Play through `2.c` | Marginal revenue from two points, then the whole MR curve. |
| 11–15 | Hide projection; Q1 on board | Compute MR between two other points. |
| 15–22 | Resume at `2.d` through `3.e` | Bring in costs, then MR = MC, price, average total cost read from the curve, and profit; check 40 and 20. |
| 22–27 | Hide projection; Q2 on board | Solve the monopolist’s problem with a different demand. |
| 27–29 | Resume to `4.a` | A fall in demand. |
| 29–34 | Resume through `5.a`; Q3 on board | The efficient quantity and deadweight loss. |
| 34–47 | Resume through `6.d` | Per-unit tax, lump-sum tax, subsidy, subsidy with a lump-sum tax. |
| 47–50 | Resume to `7.a` | Preview two sellers and E4. |

{++ This table is a proposal. It has not been timed against a run-through. All four policies stay, in minutes 34–47. ++}

<!--
|   |   |
| --- | --- |
| Model | MC = 2q, with E3 fixed cost 1,200, so ATC = q + 1200/q. Demand P = 120 − Q, so MR = 120 − 2Q. q\* = 30, P\* = 90, ATC\* = 70, profit 600, Q_sp = 40. E1 and E2 retain their existing cost models. |
| Sequence | Demand and the quantity/price question come first. Keep Monopoly as the title throughout. Use two one-unit TR-to-MR calculations: first 1 to 2 in the close-up, then 25 to 26 on the full graph. Plot the two MR results and connect them before demonstrating a quantity sweep. Keep the TR area visible as quantity, price and their guides move together. Demand and TR stay grey during this derivation, while MR is blue and price/quantity inputs remain red. MC enters after MR; the Maximize Profit panel leads through quantity and price before ATC appears in step 3. Demand and its D/MB label stay grey throughout. Read ATC from its curve without dwelling on its formula. After calculating profit, a separate paired-graph sequence shows green profit against quantity while the monopoly graph follows the same output. Keep the green profit bars and plain white Profit label visible through the comparison. Then show the monopoly graph alone for a smaller demand shift, keeping profit positive; the math panel returns only for policy comparisons. The older prose below still needs reconciliation with this order. |
| Open | The first paragraph continues a preview that E2 no longer gives. |
| Open | The prose is still the 2020 dictation. Three strikes mark numbers the new model moved. |
| Exercise | Exercise/Exercise_E3.md, its solution guide and Gradescope sheet now contain the warmup and Q1 to Q3. Full-screen exercise cards now hold the prompts for board work: warmup before the bumper, Q1 after the MR sequence, Q2 after the profit comparison, and Q3 after DWL. Cards use E2’s gold heading, muted setup, white lettered questions and opaque graphite ground. Advancing restores the preceding graph; no solutions appear on the cards. The timing table’s older hide-projection directions still need reconciliation. |
| Open | The timing table is untested, and Taxes and Subsidies is seven holds. |
| Open | E2’s yellow notes and rounded readouts are not applied here. |
| Open | The demand pivot and the policy sizes (20, 500, 1,800) are Claude’s picks. |
| Open | E2 moves to this demand line after class; nothing it displays changes. |
| Marked | Everything inside addition marks is Claude’s: the bridge sentence, the warmup, Q1 to Q3 and the next-time line. |

| Past notes | Taylor’s class notes from November 2022 and 2023 in _Schedule.md, and the Week 11 introduction, are placed at the top of the Monopoly section, unmarked. The 2022 note is a plan for this lesson: MR from two quantities, the same steps as perfect competition, and the conclusions. |
| Archive | Earlier notes, code and builds are in _archive/2026-11-11_consolidation/. |
-->

## {++ Exercise E3 | Warmup ++}

{++ You sell 20 units at \$100 each. To sell 30 units, you must lower the price to \$90 on every unit. ++}

{++ a) What is total revenue at 20 units? At 30 units?\
b\) How much additional revenue do the 10 extra units bring in, on average, per unit?\
c\) Why is your answer to b less than \$90? ++}

<!--
|   |   |
| --- | --- |
| 0.warmup | Show the Exercise E3 warmup card before the bumper, then fade it out. Students work on the board. Answers: a) \$2,000 and \$2,700; b) \$70 per additional unit on average; c) the original 20 units each lose \$10. The animation later illustrates the same idea with one-unit changes. |
-->

## Monopoly

{++ From the November 12, 2023 class notes: ++}

- Firm’s problem algorithm
- Monopoly
- Monopolist MR: zoom in to see the slope
- Monopolist’s Problem
- Implications
- Oligopoly Teaser

{++ From the November 13, 2022 class notes: ++}

the main idea is that monopolies have a very different mr curve put up the solution steps for perfect competition and the graphs introduce monopoly give the intuition for why MR isn’t a line do this by picking two quantities and asking the price that’s required to sell everything do some actual math here, showing MR then show the profit maximization thing again, that the only difference is that MR isn’t horizontal maybe emphasize that rationality happens on the margin then do the solution using the steps already on the board close with the conclusions that because firms have power, they pick quantity too low, this makes DWL, and they don’t operate at minATC but there are similar situations, but where we’re somewhere in between monopoly and perfect competition this is next class

{++ From the Week 11 introduction in the 2022 and 2023 notebooks: ++}

On Thursday we’ll continue building our model of Monopoly Firms, firms with no competition. The main idea is that both the demand curve and marginal revenue curves are downward sloping, where for perfectly competitive firms both D and MR were flat lines at the market price. We’ll use this model to discuss welfare implications and policy options.

{++ Last time the firm was one of many: one more unit sold at the market price, so marginal revenue was the price. Today the firm is the only seller. ++}

But to get a better handle on the marginal revenue curve, lets consider firms who face no competition: Monopoly firms.

<!--
|   |   |
| --- | --- |
| 0.a | Bumper with the thesis line. |
| 1.a.last | Title Monopoly. Three rows pair Many Sellers with Perfect Competition, Few Sellers with Oligopoly, and One Seller with Monopoly. Only the rows are separated by lines; there is no column heading or vertical rule. The red box is on Perfect Competition. |
-->

*Show ‘Monopoly’ on screen*

Monopolist firm operates in markets with many buyers and one seller.

<!--
|   |   |
| --- | --- |
| 1.a | The box moves to Monopoly; title Monopoly. “A monopolist operates in a market with many buyers and one seller.” |
-->

Like last time with perfectly competitive firms monopolous have a production function which tells us marginal cost curve and an average total cost curve.

*Create MC and ATC on the graph*

<!--
|   |   |
| --- | --- |
| 1.b | The table fades. Subtitle “One seller, many buyers.” Demand and its equation appear together in grey, without a separate D label. The intercept stays at 120 on the vertical axis. Mark 25 on the quantity axis before zooming. “How much should we produce, and at what price?” |
-->

And similar to competitive firms monopolists also face a marginal private benefit curve or what we often call the demand curve.

*Add the Demand curve*

But unlike the perfectly competitive firm, the monopolist faces a downward sloping demand curve. the marginal revenue curve and the marginal private benefit curve are downward sloping.

Similar to perfectly competitive firms monopolists also face a marginal private benefit curve in a marginal revenue curve where for the.

For the perfectly competitive firm the marginal private benefit curve and the marginal revenue curve.

Where the same and they also equaled the price.

For the monopolist though, the marginal private benefit curve and the marginal revenue curve are downward sloping and remember we when we talked about the demand curve.

And remember the marginal private benefit curve is just another name for the demand curve.

So the MPB satisfies the law of demand.

<!--
|   |   |
| --- | --- |
| 1.c | Expand the view to show quantities from zero to 25, carrying the existing 25 tick to the right edge so the scale change is clear. Then mark a trial quantity of one. Trial quantities and prices use bare numbers, with short leaders keeping crowded readouts attached to their actual values. “If we produce one unit, what price lets us sell it?” |
-->

## Marginal Revenue

To get a sense of where the marginal revenue curve is coming from.

Let’s zoom in on two points. On the marginal private benefit curve.

Remember the marginal revenue curve is the revenue associated with increasing the quantity by some given amount.

And the equation for marginal revenue is just the change in revenue over the change in quantity.

<!--
|   |   |
| --- | --- |
| 2.a | Keep the Monopoly title. Trace up from one to demand, then left to the price axis. “Demand tells us: one unit sells for \$119.” No cost curves or MR formula yet. |
-->

So here we’re going from a quantity of 90 to a quantity of 85. And you can see that the price.

Here we’re going from a quantity of 20 to a quantity of 30.

<!--
|   |   |
| --- | --- |
| 2.b.question | Keep the demand equation above its curve. Introduce the Total Revenue calculation panel and the first total to calculate. “Total Revenue is price times quantity: TR = P × Q.” |
| 2.b.first.inputs | Copy the graph’s price and quantity into TR₁ = 119 × 1. |
| 2.b.first | Evaluate the first total: 119. Show total revenue with visibly separate vertical bars; keep that treatment as quantity and price move. |
-->

And you can see the price is going down due to the law of demand.

It’s going down from ~~90 to 85~~ {++ 100 to 90 ++}, respectively.

So we see the price go down, but the quantity go up.

<!--
|   |   |
| --- | --- |
| 2.b.more | Keep the first calculation and the revenue area visible. “How does Total Revenue change when we increase quantity by one?” |
| 2.b.price | Increase quantity to two, moving the price, guides and TR area together. Keep the original guides for comparison. “To sell two units, the price falls to \$118 on each unit.” |
| 2.b.second.inputs | Copy the new price and quantity into TR₂ = 118 × 2 below the first total. |
| 2.b.second | Evaluate the second total: 236. Keep both totals visible. |
-->

So these two factors are moving in opposite directions.

<!--
|   |   |
| --- | --- |
| 2.b.definition | Introduce Marginal Revenue by copying the quantity-subscripted TR labels into MR = TR₂ − TR₁. |
| 2.b.split | Copy the two calculated totals into 236 − 119. Keep both TR rows visible. |
-->

And this is different than perfectly competitive firms because.

In contrast to perfectly competitive firms where the price.

Where they had very little effect on the market monopolists are the only seller in the market. And so do control the price.

<!--
|   |   |
| --- | --- |
| 2.b | Evaluate marginal revenue: the next unit adds 117. Mark the corresponding MR point. |
| 2.b.repeat.second | Keep the first MR dot, return to the full graph, and repeat at 25 to 26 units. TR rises from 2,375 to 2,444; MR is 69. Plot this second MR dot. The revenue bars follow the price and quantity. |
-->

Using this equation gives us the value for the marginal revenue curve and you can sort of see where it’s coming from.

<!--
|   |   |
| --- | --- |
| 2.c | Connect the two calculated MR points and extend the line to the axes. Show MR = 120 − 2Q. “Two points give us the marginal revenue line.” |
| 2.c.trace | After the two examples and their line, move quantity along demand and show MR moving along the established line. The vertical revenue bars move with quantity and price. “As quantity rises, each additional unit adds less revenue.” |
-->

### {++ Whiteboard | Exercise Q1 ++}

{++ Demand is $P = 120 - Q$, and the firm charges the same price for every unit. ++}

{++ a) Find the price and total revenue at $Q = 40$ and at $Q = 50$. ++}

{++ b) Calculate the change in total revenue, then marginal revenue averaged over these 10 additional units. ++}

<!--
|   |   |
| --- | --- |
| 2.c.exercise | After 2.c.trace and before costs enter, cover the graph with the Exercise E3 Q1 card. Retain the demand setup and both prompts; restore the graph on advance. Board-work answer: prices 80 and 70; TR goes from 3,200 to 3,500; ΔTR = 10 × 70 − 40 × 10 = 300, so MR = 30. |
-->

## The Monopolist’s Problem

<!--
|   |   |
| --- | --- |
| 2.d | Start the Maximize Profit panel, then introduce the objective. Bring in MC alone after the MR curve is established. Keep demand grey; ATC waits until step 3. |
-->

With these tools in hand, let’s go back and think about the monopolist problem. How they set how a monopolist would set quantity.

How a monopolist would set price and quantity.

To do this remember the solution to every firms optimization problem is to set marginal cost equal to marginal revenue.

This gets this gives us quantity. And using quantity we can then use.

<!--
|   |   |
| --- | --- |
| 3.a | Step 1: how much to produce? Locate MR = MC and drop to q\*. Show the two equations, bring their expressions together, and solve q\* = 30. |
-->

Using quantity with the demand curve allows us to find price. And similarly with the average total cost curve allows us to find the average total cost.

<!--
|   |   |
| --- | --- |
| 3.b | Step 2: find the highest price that sells all 30 units. Go up to demand, substitute q\* into P = 120 − q, then trace left to P\* = 90. |
| 3.c | Step 3: introduce ATC and read ATC\* = 70 at q\* = 30. Show its point and guide to the axis, without dwelling on the cost formula. |
-->

Using price average total cost and. Quantity allows us to find the firms profits.

<!--
|   |   |
| --- | --- |
| 3.d | Step 4: find profit from price, average total cost and quantity. π\* = (90 − 70) · 30 = 600, shown as green vertical profit bars with a plain white Profit label. |
-->

And here we can verify that marginal cost equally marginal revenue actually solves the firms profit maximization problem.

If we increase the quantity to ~~60~~ {++ 40 ++}. Their profit goes down.

<!--
|   |   |
| --- | --- |
| 3.e.setup | After calculating profit, replace the math panel with a graph of profit against quantity and make room beside the monopoly graph. Keep the green profit bars on the monopoly graph and transfer the current result, 30 units and profit 600, to the new graph. “MC = MR solves the firm’s profit maximization problem.” |
| 3.e.more | Increase quantity to 40: profit falls to 400. The changing profit bars and the point on the new graph move together, tracing the profit curve. “If we increase the quantity to 40, their profit goes down.” |
-->

And if we lower the quantity to ~~40~~ {++ 20 ++} their profit also goes down.

<!--
|   |   |
| --- | --- |
| 3.e.less | Lower quantity to 20: profit is 400 again. Continue tracing the profit curve while the monopoly graph follows the same quantity. “If we lower the quantity to 20, their profit also goes down.” |
-->

And this is really coming from the fact that as we increase quantity price also goes down from the law of demand and if we decrease quantity prices going up by the law of demand but not fast enough to compensate for the lower quantity.

<!--
|   |   |
| --- | --- |
| 3.e | Return to 30 and the peak of the profit curve, 600. “MC = MR solves the firm’s profit maximization problem.” |
-->

### {++ Whiteboard | Exercise Q2 ++}

{++ Suppose demand rises to $P = 160 - Q$, so $MR = 160 - 2Q$. The monopolist’s marginal cost is still $MC = 2Q$, with fixed cost of 1,200. Its cost curves are shown below. ++}

{++ a) Calculate and graph the profit-maximizing quantity. ++}

{++ b) Calculate and graph the price that lets the firm sell that quantity. ++}

{++ c) Calculate and graph the firm’s maximum profit.\
(*Hint: $ATC$ at the profit-maximizing quantity is 70.*) ++}

<!--
|   |   |
| --- | --- |
| 3.e.exercise | After the profit comparison, show the Exercise E3 Q2 card with the higher-demand setup, all three prompts and the supplied ATC = 70 hint. Students use the handout cost curves. Restore the paired graphs before continuing to the demand shift. Board-work answer: 160 − 2q = 2q, so q\* = 40; P\* = 120; ATC\* = 70; profit (120 − 70) × 40 = 2,000. |
-->

## Changes In Demand

And when preferences in the market change. Quantity. When preferences in the market change the firms optimization problem. The solution to the firms optimization problem also changes.

When the demand curve shifts in. Quantity. The firms quantity also shifts in and the profit goes down. And as you would expect the profit also goes down.

<!--
|   |   |
| --- | --- |
| 4.a | Return to the monopoly graph alone, with no math sidebar. Demand pivots down to P = 120 − 1.4Q: q\* falls to 25, P\* to 85, ATC\* rises to 73, and profit falls to 300. Keep the smaller green profit area visible. “When demand shifts down, the firm’s quantity and profit go down.” |
-->

## Deadweight Loss

The great triangle in this model represents. The grey triangle in this model represents stigly loss, which is.

The great triangle in this model represents dead weight loss, which is associated with a.

Which is associated with the quantity with a marginal private benefit, exceeding the marginal cost or the supply curve.

And the great triangle in this model is dead weight loss, which is associated with the quantity that’s not provided in the market where marginal private benefit exceeds marginal cost.

<!--
|   |   |
| --- | --- |
| 5.a.efficient | Demand rolls back. A red dot and dashed guide at (40, 80), with red 40 over Q_sp. “The socially efficient quantity: where the MC and MB curves intersect.” |
| 5.a | Grey strips from MC up to demand, 30 to 40, named DWL. “Deadweight loss: the quantity not provided where MB exceeds MC.” |
-->

### {++ Whiteboard | Exercise Q3 ++}

{++ Return to the original demand: $P = 120 - Q$, with $MR = 120 - 2Q$ and $MC = 2Q$. The monopolist chooses $Q = 30$ and $P = 90$. There are no externalities. ++}

{++ a) At $Q = 30$, buyers’ willingness to pay is 90 and marginal cost is 60. Why does the monopolist stop here instead of producing where $P = MC$? ++}

{++ b) Calculate and mark the socially efficient quantity. ++}

{++ c) Calculate and shade the deadweight loss from monopoly. ++}

<!--
|   |   |
| --- | --- |
| 5.a.exercise | After DWL and before policy, show the Exercise E3 Q3 card. Explicitly return to the original demand, retain the no-externalities assumption, and show all three prompts for board work using the handout graph. Restore the graph on advance. a) At 30, MR = MC = 60; beyond 30, MR is below MC because extra sales require a lower price on all units. b) 120 − Q = 2Q gives the efficient quantity 40. c) DWL = 0.5 × (40 − 30) × (90 − 60) = 150. |
-->

## Taxes and Subsidies

This model also allows us to look at the effect of taxes on the monopolists solution and government revenue.

Profit and dead weight loss.

So if we impose a tax instead of using a tax wedge, we’re just going to shift the the cost curve for the firm.

So we shift the marginal cost and the average total cost up by the amount of the tax.

Remember marginal cost. Captures the costs associated with adding one more unit.

So when we include a tax the costs are going up by the amount exactly equal to the tax.

And the same is true for average total cost.

We’re saying average show cost is the cost associated with the total number of units sold divided by the total number of units.

So because we’re applying a tax to every individual unit, we’re just increasing the average by the amount of attacks.

<!--
|   |   |
| --- | --- |
| 6.a.shift | The calculation panel returns for the policy comparison. A per-unit tax of 20 raises MC and ATC. q\* falls to 25, P\* rises to 95, ATC\* to 93, and profit falls to 50. Government revenue appears and DWL widens. |
| 6.a | The green band is named GOV. “As the tax goes up, quantity goes down and deadweight loss goes up.” |
-->

As the tax goes up quantity goes down and dead weight loss goes up.

<!--
|   |   |
| --- | --- |
| 6.a | Hold through this sentence. |
-->

This is one kind of tax but we also have another type of tax at our disposal called a lump, sum tax. So a lump, sum tax. A lump sum tax is simply taxing the firm, independently of how much they’re producing.

We typically don’t look at these types of taxes in competitive markets, but when we look at monopolies, lumpsum taxes can be useful and we’re going to demonstrate why. So first introducing a lump sum tax because it doesn’t depend on. Because the value of the tax doesn’t depend on how much is being produced or simply taxing the firm for existing. It doesn’t affect the marginal cost curve.

We’re not shifting the cost curve up by any given amount or essentially just increasing the fixed cost for the firm.

So this ship’s only the average total cost.

<!--
|   |   |
| --- | --- |
| 6.b.shift | Remove the per-unit tax and add a lump-sum tax of 500. Only ATC shifts; q\* stays 30, ATC\* becomes 86.67 (rounded), and profit falls from 600 to 100. |
-->

And what this does is essentially transfer some of the firms profits to the government. So one of the worries.

What you can see here with the tax and the lumpsum tax neither policy is effective at increasing the quantity to the socially efficient quantity where the marginal cost curve and the marginal product private benefit curve intersect.

<!--
|   |   |
| --- | --- |
| 6.b | GOV is named. “This transfers some of the firm’s profits to the government.” |
-->

But what if we included a subsidy we’ve looked at subsidies in the past and we’ve said subsidies increase.

Subsidies tend to increase the quantity exchanged in the market.

Here if we impose a subsidy on the monopolist. Their marginal cost curve the shifts out. And they’re intersection point with the marginal revenue curve also shifts out. And if we do it appropriately we can find attacks.

Where quantity is equal to the socially efficient quantity giving us zero dead weight loss.

<!--
|   |   |
| --- | --- |
| 6.c.shift | Remove the lump sum and add a per-unit subsidy of 40. q\* rises to 40 = Q_sp, P\* falls to 80, ATC\* to 30, and profit rises to 2,000. Quantity reaches the socially efficient level: zero deadweight loss. |
-->

But one of the problems here is that we’re transferring wealth from the government to the firm.

We’ve increased the firms profits and we’ve. Imposed a cost on the government.

We’re the yellow area represents a negative government revenue.

<!--
|   |   |
| --- | --- |
| 6.c | GOV is named on the green band below ATC, the paragraph’s “yellow area”. “The green area represents a negative government revenue.” |
-->

So what if we include both a tax and a lump, sum tax?

That gives us something like the following. Here we’ve increased the quantity.

Here we’ve increased the quantity to something like to something close to the socially efficient quantity and we effectively eliminated dead weight loss.

We’ve also generated positive revenue for the firm by simultaneously subsidizing quantity exchanged. By effective by subsidizing the. By. By including a subsidy and a lump, sum tax. We’ve changed the firms marginal incentives by rewarding them. By rewarding the firm for selling.

But we’ve also taken away some of their profits using a lump, sum tax.

<!--
|   |   |
| --- | --- |
| 6.d | Keep the subsidy and add a lump-sum tax of 1,800. ATC\* rises from 30 to 75 and profit falls from 2,000 to 200. “No deadweight loss, positive government revenue, and less profit.” |
-->

## Next Video

~~In the next video we’re going to look at monopolistically competitive firms firms that have a similar model to monopolies, but are competitive in a waste in a similar way to perfectly competitive firms.~~

~~The model look very similar to monopolous, but we’re also going to have an element of dynamics where firms enter an exit based on their profits.~~

{++ Next time: what happens with two sellers? ++}

<!--
|   |   |
| --- | --- |
| 7.a | The graph fades while the Monopoly title stays. The same three-row table returns, and the box moves from Monopoly to Oligopoly. “What happens with two sellers?” |
-->
