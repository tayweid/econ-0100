---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

# Monopoly | Episode E3

*Market power breaks the efficiency of markets.*

| Minutes | Animation or board work | Purpose |
| --- | --- | --- |
| Warmup | Exercise E3 Warmup on the board | Predict what one more sale adds when the price has to fall. |
| 0–3 | Bumper (`0.a`), then `1.a.last` through `1.c` | One seller; the same costs as E2; downward-sloping demand. |
| 3–11 | Play through `2.c` | Marginal revenue from two points, then the whole MR curve. |
| 11–15 | Hide projection; Q1 on board | Compute MR between two other points. |
| 15–22 | Resume through `3.e` | MR = MC, then price, average total cost, and profit; check 40 and 20. |
| 22–27 | Hide projection; Q2 on board | Solve the monopolist’s problem with a different demand. |
| 27–29 | Resume to `4.a` | A fall in demand. |
| 29–34 | Resume through `5.a`; Q3 on board | The efficient quantity and deadweight loss. |
| 34–47 | Resume through `6.d` | Per-unit tax, lump-sum tax, subsidy, subsidy with a lump-sum tax. |
| 47–50 | Resume to `7.a` | Preview two sellers and E4. |

{++ This table is a proposal. It has not been timed against a run-through. All four policies stay, in minutes 34–47. ++}

<!--
E3 consolidation, 2026-11-11. This file now follows E2_Notes.md: a timing table, then Taylor's paragraphs in their original order, each followed by a two-column table of the holds it cues, as built in E3_Animation.py (scene EpisodeE3, 30 holds). Every paragraph of Taylor's is still here, word for word. The only marks on his text are strikes, each beside its replacement. Everything Claude added is inside addition marks, except the section headings (the animation's own titles) and the timing table.

Where the earlier material went. The October 30 build log, its "Choices left for Taylor" and the old per-section beat lists are in _archive/2026-11-11_consolidation/E3_Notes_before_consolidation.md. The same folder holds 01_Notes.md (the same prose without comments), 02_Storyboard.md (an empty stub), 03_Code.py and E3_Animation_original.py (the old code and its runnable port), and E3_Animation_before_cost_switch.py (the October 30 animation on the old model). The port's monopolistic-competition scenes, the only part of it this episode does not use, have a live copy beside their notes at EX_Monopolistic_Competition/E3_Animation_original.py. The old _Unplaced.md (the monopolistic-competition opening line and the Broomsticks vignette) is now EX_Monopolistic_Competition/_Unplaced_from_E3.md.

Model of record, changed 2026-11-11: one firm and one demand line for E2, E3 and E4. Costs are E1 and E2's: TC = 1000 + q^2, MC = 2q, ATC = q + 1000/q. Demand: P = 120 - Q, so MR = 120 - 2Q; E4 uses the same line. MR = MC: 120 - 2q = 2q, q\* = 30; P\* = 90; ATC\* = 63.33; profit (90 - 63.33) x 30 = 800. Marginal revenue from two points: 20 units at 100 and 30 units at 90; TR 2,000 and 2,700; change 10 x 90 - 20 x 10 = 700; MR = 70 = MR(25). Check: q = 40 gives P 80, ATC 65, profit 600; q = 20 gives P 100, ATC 70, profit 600. Demand down to P = 120 - 2Q (MR = 120 - 4Q): q\* = 20, P\* = 80, ATC\* = 70, profit 200. Efficient quantity Q_sp = 40, where demand meets MC at 80; deadweight loss 150, never shown as a number. Per-unit tax 20: q\* = 25, P\* = 95, ATC\* = 85, profit 250, government 500. Lump-sum tax 500: q\* = 30, ATC\* = 80, profit 300, government 500. Subsidy 40 per unit: q\* = 40 = Q_sp, P\* = 80, ATC\* = 25, profit 2,200, government cost 1,600. Subsidy with a lump-sum tax of 1,800: ATC\* = 70, profit 400, government 1,800 - 1,600 = 200. These were read off the rendered holds on 2026-11-11 and match. Graph: 0 to 120 units by 0 to 140 \$/unit; demand runs to its foot at 120 units and MR to its foot at 60. An earlier build the same day used P = 120 - Q/2 (q\* = 40, P\* = 100); it is in the archive as E3_Animation_demand_120_minus_half_Q.py. It was dropped because the duopoly on that line does not come out whole.

STUCK. These need Taylor; nothing here was decided for him.
1. The opening. The first paragraph ("But to get a better handle on the marginal revenue curve") continues a preview that E2 no longer gives: E2 now ends on the spinach closer. A bridge sentence is offered before it.
2. The prose is the 2020 dictation, false starts included (the fourth to eighth paragraphs of Monopoly, "from a quantity of 90 to a quantity of 85", the first three Deadweight Loss paragraphs). All of it is kept as is; the rewrite is Taylor's.
3. Numbers the cost switch moved. The two points now sit at prices 100 and 90 (the notes say 90 and 85), and the check quantities are 40 and 20 (the notes say 60 and 40). Three strikes mark these. The hold names 3.e.sixty and 3.e.forty keep their old names so the IDs stay stable.
4. No opener story, no warmup hold, and no exercise cards exist in the animation, and there is no Exercise folder. The warmup and Q1 to Q3 below exist only in these notes.
5. Time. Decided 2026-11-11: all four policies stay in E3. What is still open is the fit: the timing table is a proposal, and Taxes and Subsidies is seven holds in thirteen minutes.
6. E2's conventions have not been applied: E3 keeps one gold line at the bottom (E2 uses yellow notes), two-decimal readouts (E2 rounds), the side-panel card (E2 builds calculations line by line), and the taxonomy opening.
7. Changes In Demand pivots demand about 120, down to P = 120 - 2Q. The notes say "shifts in". The size of the pivot is Claude's pick.
8. Policy sizes are Claude's picks, except the subsidy of 40, which Q_sp = 40 forces: tax 20, lump sums 500 and 1,800.
9. "The yellow area" in the subsidy paragraph is green on screen.
10. The two Next Video paragraphs describe monopolistic competition, which this semester does not teach; they are struck, not removed. That material's notes are EX_Monopolistic_Competition/01_Notes.md.
11. The earlier thesis, "The fewer sellers, the worse.", left the bumper for Taylor's new one. E5 Wrap-Up has no thesis line yet and it may fit there.
12. Layout to look at: in 6.a the Profit, GOV and DWL names and three dots crowd around 25 units; in 6.d the green band is thin and its name small.
13. Still open from the October 30 build: the subtitle "One seller, many buyers." and the other lines written for the build; q\*, P\*, ATC\* and Q_sp against Part C's hats; step 5 of the firm's card (stay or exit) is left out; E5 moved to this market on 2026-11-11 too; its notes list what that leaves open.
14. Plass's round-trip check was not run on this file: the importer is no longer in the Trash. The syntax copies E2_Notes.md.
15. E2 still draws its market demand as P = 120 - 2Q/3 with Q in thousands. Taylor's plan is to move it to this episode's line, P = 120 - Q read in thousands, after class. Nothing E2 displays changes: its market quantity is never shown as a number, and its prices, firm quantities, profits and the spinach closer's numbers do not depend on the slope of demand.

ADDITIONS, all Claude's and all marked: the bridge sentence at the top of Monopoly; the warmup; Whiteboard Q1, Q2 and Q3; the Next time line. Each is a suggestion to cut or rewrite.
-->

## {++ Exercise E3 | Warmup ++}

{++ You sell 20 units at \$100 each. To sell 30 units, you have to lower the price to \$90 on every unit. ++}

{++ a\) What is revenue at 20 units? At 30 units? ++}

{++ b\) How much revenue did each of the 10 extra units add? ++}

{++ c\) Each extra unit sold for \$90. Why did it add less than \$90? ++}

<!--
Not built: the animation has no warmup hold. The numbers are the ones Marginal Revenue uses, so the animation answers the warmup at 2.b.

Answers: a) \$2,000 and \$2,700; b) \$700 over 10 units, \$70 each; c) the 20 units already being sold each lost \$10, \$200 in all.
-->

## Monopoly

{++ Last time the firm was one of many: one more unit sold at the market price, so marginal revenue was the price. Today the firm is the only seller. ++}

But to get a better handle on the marginal revenue curve, lets consider firms who face no competition: Monopoly firms.

<!--
|   |   |
| --- | --- |
| 0.a | Play the E3 bumper: Part E ∣ Episode 3, with the italic thesis in grey beneath it. It reads “Market power breaks the efficiency of markets.”, the thesis at the top of these notes. |
| 1.a.last | Title: Perfect Competition, with no subtitle. Center the market-structures taxonomy: columns Homogeneous and Differentiated; rows Many Sellers (Perfect Competition, Monopolistic Competition), Few Sellers (Oligopoly, the differentiated cell blank), One Seller (Monopoly, across both columns). A red box sits on Perfect Competition, last episode’s cell. No bottom line. |
-->

*Show ‘Monopoly’ on screen*

Monopolist firm operates in markets with many buyers and one seller.

<!--
|   |   |
| --- | --- |
| 1.a | Move the red box to Monopoly and change the title to Monopoly. Gold line: “A monopolist operates in a market with many buyers and one seller.” |
-->

Like last time with perfectly competitive firms monopolous have a production function which tells us marginal cost curve and an average total cost curve.

*Create MC and ATC on the graph*

<!--
|   |   |
| --- | --- |
| 1.b | Fade the taxonomy. Start the subtitle “One seller, many buyers.”, which stays through 6.d. Draw the graph, 0 to 120 units by 0 to 140 \$/unit: MC in orange from the origin to (60, 120) and ATC in purple from 118 at 9.2 units down through its minimum near (31.6, 63.2) and up to (85, 96.8). These are E2’s curves. Add the grey divider and the rows MC = 2q and ATC = q + 1000/q. Gold line: “As with competitive firms, the production function gives MC and ATC.” |
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
| 1.c | Draw demand in teal from 120 on the price axis to its foot at 120 units, the right edge of the graph. Name it D / MB just above its lower end, and mark the teal 120 on the price axis. Add the row D: P = 120 − Q. Gold line: “Unlike competitive firms, a monopolist faces downward-sloping demand.” |
-->

## Marginal Revenue

To get a sense of where the marginal revenue curve is coming from.

Let’s zoom in on two points. On the marginal private benefit curve.

Remember the marginal revenue curve is the revenue associated with increasing the quantity by some given amount.

And the equation for marginal revenue is just the change in revenue over the change in quantity.

<!--
|   |   |
| --- | --- |
| 2.a | Title: Marginal Revenue. The cost rows leave the panel, the demand row moves to the top, and MR = ΔTR / ΔQ appears below it. Gold line: “Marginal revenue: the change in revenue over the change in quantity.” |
-->

So here we’re going from a quantity of 90 to a quantity of 85. And you can see that the price.

Here we’re going from a quantity of 20 to a quantity of 30.

<!--
|   |   |
| --- | --- |
| 2.b.first | Mark the first point on demand: a teal dot at (20, 100), a red dashed drop to the quantity axis with 20 over Q₁, and a teal dashed guide to the price axis with P₁ = 100. Fill its revenue, 20 units by 100, with teal one-unit strips. Row: TR₁ = 100 × 20 = 2,000. Gold line: “Here we’re going from a quantity of 20 to a quantity of 30.” |
-->

And you can see the price is going down due to the law of demand.

It’s going down from ~~90 to 85~~ {++ 100 to 90 ++}, respectively.

So we see the price go down, but the quantity go up.

<!--
|   |   |
| --- | --- |
| 2.b.second | A second dot rides demand from the first point to (30, 90). The revenue strips split as it moves: the band from 90 to 100 over the first 20 units turns red, the price cut on the units already sold, and the 10 new units at 90 fill in strong teal. Then show P₂ = 90 under P₁, 30 over Q₂, and the row TR₂ = 90 × 30 = 2,700. Gold line: “So we see the price go down, but the quantity go up.” |
-->

So these two factors are moving in opposite directions.

<!--
|   |   |
| --- | --- |
| 2.b.split | Row: ΔTR = 10 × 90 − 20 × 10 = 700, with the gain in teal and the loss in red to match the strips. The red band flashes yellow once. Gold line: “So these two factors are moving in opposite directions.” |
-->

And this is different than perfectly competitive firms because.

In contrast to perfectly competitive firms where the price.

Where they had very little effect on the market monopolists are the only seller in the market. And so do control the price.

<!--
|   |   |
| --- | --- |
| 2.b | Row: MR = 700 / 10 = 70, with MR and 70 in pink. Add a pink dot at (25, 70), halfway between the two quantities. Gold line: “Monopolists are the only seller in the market, so they control the price.” |
-->

Using this equation gives us the value for the marginal revenue curve and you can sort of see where it’s coming from.

<!--
|   |   |
| --- | --- |
| 2.c.trace | Fade the readouts and the four worked rows. One four-second sweep moves the pair along demand from 20 and 30 to 50 and 60, the red and teal strips following, while the pink dot traces a line from (25, 70) to (55, 10). Gold line: “Using this equation gives us the value for the marginal revenue curve.” |
| 2.c | Replace the pair, its strips and the trace with the whole MR line in pink from (0, 120) to (60, 0), half of demand’s 120 units, named MR at its foot. Add the row MR = 120 − 2Q under the demand row. Gold line: “MR starts with demand at 120 and falls twice as fast.” |
-->

### {++ Whiteboard | Exercise Q1 ++}

{++ > Demand is still $P = 120 - Q$. Find marginal revenue between 40 and 50 units. ++}

<!--
Not built: no exercise card in the animation.

Answer: the prices are 80 and 70. TR goes from 80 × 40 = 3,200 to 70 × 50 = 3,500. ΔTR = 10 × 70 − 40 × 10 = 300, so MR = 30, which is 120 − 2 · 45.
-->

## The Monopolist’s Problem

With these tools in hand, let’s go back and think about the monopolist problem. How they set how a monopolist would set quantity.

How a monopolist would set price and quantity.

To do this remember the solution to every firms optimization problem is to set marginal cost equal to marginal revenue.

This gets this gives us quantity. And using quantity we can then use.

<!--
|   |   |
| --- | --- |
| 3.a | Title: The Monopolist’s Problem. The panel becomes the firm’s card: max over q of π = TR − TC, then step 1, MC = MR → q\*. Put a red dot where MR meets MC at (30, 60), show the worked row 2q = 120 − 2q, so q\* = 30, then draw the red dashed drop with 30 over q\* under the axis. Gold line: “To solve any firm’s problem, set marginal cost equal to marginal revenue.” |
-->

Using quantity with the demand curve allows us to find price. And similarly with the average total cost curve allows us to find the average total cost.

<!--
|   |   |
| --- | --- |
| 3.b | Step 2: q\* → D → P\*. The drop rises from the red dot to demand at (30, 90). Add a teal dot, a teal dashed guide to the price axis and P\* = 90.00. Worked row: P\* = 120 − 30 = 90. Gold line: “Using quantity with the demand curve allows us to find price.” |
| 3.c | Step 3: q\* → ATC → ATC\*. Add a purple dot on ATC at (30, 63.33), a purple dashed guide and ATC\* = 63.33. Worked row: ATC\* = 30 + 1000/30 = 63.33. Gold line: “Quantity with the average total cost curve gives the average total cost.” |
-->

Using price average total cost and. Quantity allows us to find the firms profits.

<!--
|   |   |
| --- | --- |
| 3.d | Step 4: π\* = (P\* − ATC\*) · q\*. Fill orange one-unit strips from ATC\* up to P\* over the 30 units and name the area Profit. Worked row: π\* = (90 − 63.33) · 30 = 800. Gold line: “Price, average total cost and quantity give us the firm’s profits.” |
-->

And here we can verify that marginal cost equally marginal revenue actually solves the firms profit maximization problem.

If we increase the quantity to ~~60~~ {++ 40 ++}. Their profit goes down.

<!--
|   |   |
| --- | --- |
| 3.e.sixty | The stars come off the readouts and the worked profit row becomes a live row with every number rolling. Move the quantity from 30 to 40: the drop, the teal and purple dots and guides, P and ATC on the axis and the profit strips all follow, while the red MR = MC dot stays at (30, 60). The row ends at π = (80.00 − 65.00) · 40 = 600. Gold line: “If we increase the quantity to 40, their profit goes down.” The hold keeps its name from the old model, where this quantity was 60. |
-->

And if we lower the quantity to ~~40~~ {++ 20 ++} their profit also goes down.

<!--
|   |   |
| --- | --- |
| 3.e.forty | Roll the quantity to 20: P = 100.00, ATC = 70.00, profit 600 again. Gold line: “If we lower the quantity to 20, their profit also goes down.” The hold keeps its name from the old model, where this quantity was 40. |
-->

And this is really coming from the fact that as we increase quantity price also goes down from the law of demand and if we decrease quantity prices going up by the law of demand but not fast enough to compensate for the lower quantity.

<!--
|   |   |
| --- | --- |
| 3.e | Return to 30 and restore the stars: P\* = 90.00, ATC\* = 63.33, q\*, and π\* = (90.00 − 63.33) · 30 = 800. Gold line: “MC = MR solves the firm’s profit maximization problem.” |
-->

### {++ Whiteboard | Exercise Q2 ++}

{++ > Demand rises to $P = 160 - Q$, so $MR = 160 - 2Q$. Costs are unchanged. Find the monopolist’s quantity, price, and profit. ++}

<!--
Not built: no exercise card in the animation.

Answer: 160 − 2q = 2q, so q\* = 40; P\* = 160 − 40 = 120; ATC\* = 40 + 1000/40 = 65; profit (120 − 65) × 40 = 2,200.
-->

## Changes In Demand

And when preferences in the market change. Quantity. When preferences in the market change the firms optimization problem. The solution to the firms optimization problem also changes.

When the demand curve shifts in. Quantity. The firms quantity also shifts in and the profit goes down. And as you would expect the profit also goes down.

<!--
|   |   |
| --- | --- |
| 4.a | Title: Changes In Demand. The worked rows for steps 1 to 3 leave and the card closes up around the four steps and the live profit row. Leave a thin grey ghost of demand where it was, then pivot demand down about 120 to P = 120 − 2Q: demand now reaches the axis at 60 units and MR at 30, D / MB and MR ride their curves, and the red dot slides down MC. The readouts roll: q\* 30 → 20, P\* 90.00 → 80.00, ATC\* 63.33 → 70.00 and π\* 800 → 200. Gold line: “When demand shifts down, the firm’s quantity and profit go down.” |
-->

## Deadweight Loss

The great triangle in this model represents. The grey triangle in this model represents stigly loss, which is.

The great triangle in this model represents dead weight loss, which is associated with a.

Which is associated with the quantity with a marginal private benefit, exceeding the marginal cost or the supply curve.

And the great triangle in this model is dead weight loss, which is associated with the quantity that’s not provided in the market where marginal private benefit exceeds marginal cost.

<!--
|   |   |
| --- | --- |
| 5.a.efficient | Roll demand back and fade the ghost. Title: Deadweight Loss. Gold line: “The socially efficient quantity: where the MC and MB curves intersect.” Then add a yellow dot where MC meets demand at (40, 80), a yellow dashed drop, and 40 over Q_sp under the axis, beside the red 30 over q\*. |
| 5.a | Fill grey strips from MC up to demand over every unit from 30 to 40, and name the area DWL just above demand. Gold line: “Deadweight loss: the quantity not provided where MB exceeds MC.” |
-->

### {++ Whiteboard | Exercise Q3 ++}

{++ > At 30 units, buyers will pay about \$90 for the next unit and it costs about \$60 to make. Why doesn’t the monopolist sell it? ++}

<!--
Not built: no exercise card in the animation.

Answer: to sell one more unit the monopolist lowers the price on all 30 units already being sold. The next unit adds about \$60 to revenue (MR = 120 − 2 · 30 = 60) and about \$60 to cost. Beyond 30, each further unit adds less to revenue than to cost, even though buyers value it above its cost.
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
Four trackers (a per-unit tax, a lump-sum tax, a per-unit subsidy, and demand) drive every mark in this section. The panel keeps the card’s four steps and the live profit row, with each policy’s size rolling in a green row under it. The green government band runs between the firm’s true ATC and its ATC under the policy, over the q\* units; profit runs from the policy ATC up to P\*; DWL runs from MC up to demand between q\* and Q_sp.

|   |   |
| --- | --- |
| 6.a.shift | Title: A Per-Unit Tax. Add a green row under the profit row: Tax per unit = \$0. Gold line: “We shift marginal cost and average total cost up by the tax.” Roll the tax from 0 to 20. A dashed orange copy of MC rises by 20, named MC + tax, and a dashed purple copy of ATC rises by 20, named ATC + tax. The red dot slides up MR to (25, 70). The readouts roll: q\* 30 → 25, P\* 90.00 → 95.00, ATC\* 63.33 → 85.00, now on the dashed ATC, and π\* 800 → 250. The profit strips shrink to the band from 85 to 95 over 25 units, a green band fills 65 to 85, and the grey DWL widens to the units from 25 to 40, its name moving inside it. |
| 6.a | Name the green band GOV. Gold line: “As the tax goes up, quantity goes down and deadweight loss goes up.” |
-->

As the tax goes up quantity goes down and dead weight loss goes up.

<!--
|   |   |
| --- | --- |
|  | Hold 6.a through this sentence. |
-->

This is one kind of tax but we also have another type of tax at our disposal called a lump, sum tax. So a lump, sum tax. A lump sum tax is simply taxing the firm, independently of how much they’re producing.

We typically don’t look at these types of taxes in competitive markets, but when we look at monopolies, lumpsum taxes can be useful and we’re going to demonstrate why. So first introducing a lump sum tax because it doesn’t depend on. Because the value of the tax doesn’t depend on how much is being produced or simply taxing the firm for existing. It doesn’t affect the marginal cost curve.

We’re not shifting the cost curve up by any given amount or essentially just increasing the fixed cost for the firm.

So this ship’s only the average total cost.

<!--
|   |   |
| --- | --- |
| 6.b.shift | Remove GOV’s name and roll the tax back to 0. Title: A Lump-Sum Tax. Row: Lump-sum tax = \$0. Gold line: “A lump-sum tax shifts only the average total cost.” Roll the lump sum from 0 to 500. The dashed ATC rises as ATC + 500/q, a fixed cost, named ATC + lump sum. MC does not move and q\* stays 30. ATC\* rolls 63.33 → 80.00 and π\* 800 → 300, and the green band fills 63.33 to 80 over 30 units. |
-->

And what this does is essentially transfer some of the firms profits to the government. So one of the worries.

What you can see here with the tax and the lumpsum tax neither policy is effective at increasing the quantity to the socially efficient quantity where the marginal cost curve and the marginal product private benefit curve intersect.

<!--
|   |   |
| --- | --- |
| 6.b | Name the band GOV. Gold line: “This transfers some of the firm’s profits to the government.” |
-->

But what if we included a subsidy we’ve looked at subsidies in the past and we’ve said subsidies increase.

Subsidies tend to increase the quantity exchanged in the market.

Here if we impose a subsidy on the monopolist. Their marginal cost curve the shifts out. And they’re intersection point with the marginal revenue curve also shifts out. And if we do it appropriately we can find attacks.

Where quantity is equal to the socially efficient quantity giving us zero dead weight loss.

<!--
|   |   |
| --- | --- |
| 6.c.shift | Remove GOV’s name and roll the lump sum back to 0. Title: A Per-Unit Subsidy. Row: Subsidy per unit = \$0. Gold line: “Subsidies tend to increase the quantity exchanged in the market.” Roll the subsidy from 0 to 40. Dashed MC − subsidy and ATC − subsidy move down, and the red dot slides down MR to (40, 40). The readouts roll: q\* 30 → 40, its red quantity row fading as it reaches the yellow 40 over Q_sp, P\* 90.00 → 80.00, ATC\* 63.33 → 25.00 and π\* 800 → 2,200. The DWL strips close to nothing. The green band now lies below ATC, from 25 to 65 over 40 units, inside the profit, and the name Profit sits on the part above ATC. Then change the gold line: “Quantity reaches the socially efficient quantity: zero deadweight loss.” |
-->

But one of the problems here is that we’re transferring wealth from the government to the firm.

We’ve increased the firms profits and we’ve. Imposed a cost on the government.

We’re the yellow area represents a negative government revenue.

<!--
|   |   |
| --- | --- |
| 6.c | Name the band GOV. Gold line: “The green area represents a negative government revenue.” The paragraph’s “yellow area” is this green band. |
-->

So what if we include both a tax and a lump, sum tax?

That gives us something like the following. Here we’ve increased the quantity.

Here we’ve increased the quantity to something like to something close to the socially efficient quantity and we effectively eliminated dead weight loss.

We’ve also generated positive revenue for the firm by simultaneously subsidizing quantity exchanged. By effective by subsidizing the. By. By including a subsidy and a lump, sum tax. We’ve changed the firms marginal incentives by rewarding them. By rewarding the firm for selling.

But we’ve also taken away some of their profits using a lump, sum tax.

<!--
|   |   |
| --- | --- |
| 6.d | Title: A Subsidy And A Lump-Sum Tax. Add a second row under the subsidy row: Lump-sum tax = \$0. Keep the subsidy and roll the lump sum from 0 to 1,800. The dashed curve becomes ATC − subsidy + lump sum, a two-line name under ATC’s own. q\* stays 40. ATC\* rolls 25.00 → 70.00 and π\* 2,200 → 400. The green band shrinks to nothing at a lump sum of 1,600 and grows again above ATC, from 65 to 70: positive revenue. Gold line: “No deadweight loss, positive government revenue, and less profit.” |
-->

## Next Video

~~In the next video we’re going to look at monopolistically competitive firms firms that have a similar model to monopolies, but are competitive in a waste in a similar way to perfectly competitive firms.~~

~~The model look very similar to monopolous, but we’re also going to have an element of dynamics where firms enter an exit based on their profits.~~

{++ Next time: what happens with two sellers? ++}

<!--
|   |   |
| --- | --- |
| 7.a | Freeze and fade everything. Title: Next Time, with no subtitle. Bring back the taxonomy with the red box on Monopoly, then move the box to Oligopoly, where E4 opens. Gold line: “What happens with two sellers?” |
-->
