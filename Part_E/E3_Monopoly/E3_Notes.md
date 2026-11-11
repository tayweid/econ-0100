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
| 15–22 | Resume through `3.e` | MR = MC, then price, average total cost, and profit; check 50 and 30. |
| 22–27 | Hide projection; Q2 on board | Solve the monopolist’s problem with a different demand. |
| 27–29 | Resume to `4.a` | A fall in demand. |
| 29–34 | Resume through `5.a`; Q3 on board | The efficient quantity and deadweight loss. |
| 34–47 | Resume through `6.d` | Per-unit tax, lump-sum tax, subsidy, subsidy with a lump-sum tax. |
| 47–50 | Resume to `7.a` | Preview two sellers and E4. |

{++ This table is a proposal. It has not been timed against a run-through. All four policies stay, in minutes 34–47. ++}

<!--
E3 consolidation, 2026-11-11. This file now follows E2_Notes.md: a timing table, then Taylor's paragraphs in their original order, each followed by a two-column table of the holds it cues, as built in E3_Animation.py (scene EpisodeE3, 30 holds). Every paragraph of Taylor's is still here, word for word. The only marks on his text are strikes, each beside its replacement. Everything Claude added is inside addition marks, except the section headings (the animation's own titles) and the timing table.

Where the earlier material went. The October 30 build log, its "Choices left for Taylor" and the old per-section beat lists are in _archive/2026-11-11_consolidation/E3_Notes_before_consolidation.md. The same folder holds 01_Notes.md (the same prose without comments), 02_Storyboard.md (an empty stub), 03_Code.py and E3_Animation_original.py (the old code and its runnable port), and E3_Animation_before_cost_switch.py (the October 30 animation on the old model). The port's monopolistic-competition scenes, the only part of it this episode does not use, have a live copy beside their notes at E5_Policy_and_Market_Power/E3_Animation_original.py. The old _Unplaced.md (the monopolistic-competition opening line and the Broomsticks vignette) is now E5_Policy_and_Market_Power/_Unplaced_from_E3.md.

Model of record, changed 2026-11-11 to E1 and E2's firm. Costs: TC = 1000 + q^2, MC = 2q, ATC = q + 1000/q. Demand: P = 120 - Q/2, so MR = 120 - Q. MR = MC: 120 - q = 2q, q\* = 40; P\* = 100; ATC\* = 65 (the value students found in Exercise E2 Q1c); profit (100 - 65) x 40 = 1,400. Marginal revenue from two points: 20 units at 110 and 30 units at 105; TR 2,200 and 3,150; change 10 x 105 - 20 x 5 = 950; MR = 95 = MR(25). Check: q = 50 gives P 95, ATC 70, profit 1,250; q = 30 gives P 105, ATC 63.33, profit 1,250. Demand down to P = 120 - Q (MR = 120 - 2Q): q\* = 30, P\* = 90, ATC\* = 63.33, profit 800. Efficient quantity Q_sp = 48, where demand meets MC at 96; deadweight loss 80, never shown as a number. Per-unit tax 30 (E2's spinach cost): q\* = 30, P\* = 105, ATC\* = 93.33, profit 350, government 900. Lump-sum tax 1,000: q\* = 40, ATC\* = 90, profit 400, government 1,000. Subsidy 24 per unit: q\* = 48 = Q_sp, P\* = 96, ATC\* = 44.83, profit 2,456, government cost 1,152. Subsidy with a lump-sum tax of 2,000: ATC\* = 86.50, profit 456, government 2,000 - 1,152 = 848. Every one of these was read off the rendered holds on 2026-11-11 and matches. Graph: 0 to 120 units by 0 to 140 \$/unit; MR runs to its foot at 120 units, where demand is still at 60.

STUCK. These need Taylor; nothing here was decided for him.
1. The opening. The first paragraph ("But to get a better handle on the marginal revenue curve") continues a preview that E2 no longer gives: E2 now ends on the spinach closer. A bridge sentence is offered before it.
2. The prose is the 2020 dictation, false starts included (the fourth to eighth paragraphs of Monopoly, "from a quantity of 90 to a quantity of 85", the first three Deadweight Loss paragraphs). All of it is kept as is; the rewrite is Taylor's.
3. Numbers the cost switch moved. The two points now sit at prices 110 and 105 (the notes say 90 and 85), and the check quantities are 50 and 30 (the notes say 60 and 40). Three strikes mark these. The hold names 3.e.sixty and 3.e.forty keep their old names so the IDs stay stable.
4. No opener story, no warmup hold, and no exercise cards exist in the animation, and there is no Exercise folder. The warmup and Q1 to Q3 below exist only in these notes.
5. Time. Decided 2026-11-11: all four policies stay in E3. What is still open is the fit: the timing table is a proposal, and Taxes and Subsidies is seven holds in thirteen minutes.
6. E2's conventions have not been applied: E3 keeps one gold line at the bottom (E2 uses yellow notes), two-decimal readouts (E2 rounds), the side-panel card (E2 builds calculations line by line), and the taxonomy opening.
7. Changes In Demand pivots demand about 120, down to P = 120 - Q. The notes say "shifts in". The size of the pivot is Claude's pick.
8. Policy sizes are Claude's picks, except the subsidy of 24, which Q_sp = 48 forces: tax 30, lump sums 1,000 and 2,000.
9. "The yellow area" in the subsidy paragraph is green on screen.
10. The two Next Video paragraphs describe monopolistic competition, which this semester does not teach; they are struck, not removed. That material's notes are E5_Policy_and_Market_Power/01_Notes.md.
11. The earlier thesis, "The fewer sellers, the worse.", left the bumper for Taylor's new one. E5 Wrap-Up has no thesis line yet and it may fit there.
12. Layout to look at: in 6.a the Profit, GOV and DWL names and three dots crowd around 30 units; the dashed policy curves brush MC's name in 6.a and 6.c; D / MB sits under the demand line with the policy names above it.
13. Still open from the October 30 build: the subtitle "One seller, many buyers." and the other lines written for the build; q\*, P\*, ATC\* and Q_sp against Part C's hats; step 5 of the firm's card (stay or exit) is left out; E4 and E5 still use the handwritten sheet's market (D: P = 200 - Q/2, MC = 20 + q), so E3's monopoly is not E5's.
14. Plass's round-trip check was not run on this file: the importer is no longer in the Trash. The syntax copies E2_Notes.md.

ADDITIONS, all Claude's and all marked: the bridge sentence at the top of Monopoly; the warmup; Whiteboard Q1, Q2 and Q3; the Next time line. Each is a suggestion to cut or rewrite.
-->

## {++ Exercise E3 | Warmup ++}

{++ You sell 20 units at \$110 each. To sell 30 units, you have to lower the price to \$105 on every unit. ++}

{++ a\) What is revenue at 20 units? At 30 units? ++}

{++ b\) How much revenue did each of the 10 extra units add? ++}

{++ c\) Each extra unit sold for \$105. Why did it add less than \$105? ++}

<!--
Not built: the animation has no warmup hold. The numbers are the ones Marginal Revenue uses, so the animation answers the warmup at 2.b.

Answers: a) \$2,200 and \$3,150; b) \$950 over 10 units, \$95 each; c) the 20 units already being sold each lost \$5, \$100 in all.
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
| 1.c | Draw demand in teal from 120 on the price axis to (120, 60) at the right edge of the graph; its foot, 240 units, is off the graph. Name it D / MB under the line near the right edge, and mark the teal 120 on the price axis. Add the row D: P = 120 − ½Q. Gold line: “Unlike competitive firms, a monopolist faces downward-sloping demand.” |
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
| 2.b.first | Mark the first point on demand: a teal dot at (20, 110), a red dashed drop to the quantity axis with 20 over Q₁, and a teal dashed guide to the price axis with P₁ = 110. Fill its revenue, 20 units by 110, with teal one-unit strips. Row: TR₁ = 110 × 20 = 2,200. Gold line: “Here we’re going from a quantity of 20 to a quantity of 30.” |
-->

And you can see the price is going down due to the law of demand.

It’s going down from ~~90 to 85~~ {++ 110 to 105 ++}, respectively.

So we see the price go down, but the quantity go up.

<!--
|   |   |
| --- | --- |
| 2.b.second | A second dot rides demand from the first point to (30, 105). The revenue strips split as it moves: the band from 105 to 110 over the first 20 units turns red, the price cut on the units already sold, and the 10 new units at 105 fill in strong teal. Then show P₂ = 105 under P₁, 30 over Q₂, and the row TR₂ = 105 × 30 = 3,150. Gold line: “So we see the price go down, but the quantity go up.” |
-->

So these two factors are moving in opposite directions.

<!--
|   |   |
| --- | --- |
| 2.b.split | Row: ΔTR = 10 × 105 − 20 × 5 = 950, with the gain in teal and the loss in red to match the strips. The red band flashes yellow once. Gold line: “So these two factors are moving in opposite directions.” |
-->

And this is different than perfectly competitive firms because.

In contrast to perfectly competitive firms where the price.

Where they had very little effect on the market monopolists are the only seller in the market. And so do control the price.

<!--
|   |   |
| --- | --- |
| 2.b | Row: MR = 950 / 10 = 95, with MR and 95 in pink. Add a pink dot at (25, 95), halfway between the two quantities. Gold line: “Monopolists are the only seller in the market, so they control the price.” |
-->

Using this equation gives us the value for the marginal revenue curve and you can sort of see where it’s coming from.

<!--
|   |   |
| --- | --- |
| 2.c.trace | Fade the readouts and the four worked rows. One four-second sweep moves the pair along demand from 20 and 30 to 90 and 100, the red and teal strips following, while the pink dot traces a line from (25, 95) to (95, 25). Gold line: “Using this equation gives us the value for the marginal revenue curve.” |
| 2.c | Replace the pair, its strips and the trace with the whole MR line in pink from (0, 120) to (120, 0), named MR at its foot. Add the row MR = 120 − Q under the demand row. Gold line: “MR starts with demand at 120 and falls twice as fast.” |
-->

### {++ Whiteboard | Exercise Q1 ++}

{++ > Demand is still $P = 120 - \tfrac{1}{2}Q$. Find marginal revenue between 60 and 70 units. ++}

<!--
Not built: no exercise card in the animation. The prices at these two quantities are 90 and 85, the pair in the dictated notes.

Answer: TR goes from 90 × 60 = 5,400 to 85 × 70 = 5,950. ΔTR = 10 × 85 − 60 × 5 = 550, so MR = 55, which is 120 − 65.
-->

## The Monopolist’s Problem

With these tools in hand, let’s go back and think about the monopolist problem. How they set how a monopolist would set quantity.

How a monopolist would set price and quantity.

To do this remember the solution to every firms optimization problem is to set marginal cost equal to marginal revenue.

This gets this gives us quantity. And using quantity we can then use.

<!--
|   |   |
| --- | --- |
| 3.a | Title: The Monopolist’s Problem. The panel becomes the firm’s card: max over q of π = TR − TC, then step 1, MC = MR → q\*. Put a red dot where MR meets MC at (40, 80), show the worked row 2q = 120 − q, so q\* = 40, then draw the red dashed drop with 40 over q\* under the axis. Gold line: “To solve any firm’s problem, set marginal cost equal to marginal revenue.” |
-->

Using quantity with the demand curve allows us to find price. And similarly with the average total cost curve allows us to find the average total cost.

<!--
|   |   |
| --- | --- |
| 3.b | Step 2: q\* → D → P\*. The drop rises from the red dot to demand at (40, 100). Add a teal dot, a teal dashed guide to the price axis and P\* = 100.00. Worked row: P\* = 120 − ½ · 40 = 100. Gold line: “Using quantity with the demand curve allows us to find price.” |
| 3.c | Step 3: q\* → ATC → ATC\*. Add a purple dot on ATC at (40, 65), a purple dashed guide and ATC\* = 65.00. Worked row: ATC\* = 40 + 1000/40 = 65. Gold line: “Quantity with the average total cost curve gives the average total cost.” |
-->

Using price average total cost and. Quantity allows us to find the firms profits.

<!--
|   |   |
| --- | --- |
| 3.d | Step 4: π\* = (P\* − ATC\*) · q\*. Fill orange one-unit strips from ATC\* up to P\* over the 40 units and name the area Profit. Worked row: π\* = (100 − 65) · 40 = 1,400. Gold line: “Price, average total cost and quantity give us the firm’s profits.” |
-->

And here we can verify that marginal cost equally marginal revenue actually solves the firms profit maximization problem.

If we increase the quantity to ~~60~~ {++ 50 ++}. Their profit goes down.

<!--
|   |   |
| --- | --- |
| 3.e.sixty | The stars come off the readouts and the worked profit row becomes a live row with every number rolling. Move the quantity from 40 to 50: the drop, the teal and purple dots and guides, P and ATC on the axis and the profit strips all follow, while the red MR = MC dot stays at (40, 80). The row ends at π = (95.00 − 70.00) · 50 = 1,250. Gold line: “If we increase the quantity to 50, their profit goes down.” The hold keeps its name from the old model, where this quantity was 60. |
-->

And if we lower the quantity to ~~40~~ {++ 30 ++} their profit also goes down.

<!--
|   |   |
| --- | --- |
| 3.e.forty | Roll the quantity to 30: P = 105.00, ATC = 63.33, profit 1,250 again. Gold line: “If we lower the quantity to 30, their profit also goes down.” The hold keeps its name from the old model, where this quantity was 40. |
-->

And this is really coming from the fact that as we increase quantity price also goes down from the law of demand and if we decrease quantity prices going up by the law of demand but not fast enough to compensate for the lower quantity.

<!--
|   |   |
| --- | --- |
| 3.e | Return to 40 and restore the stars: P\* = 100.00, ATC\* = 65.00, q\*, and π\* = (100.00 − 65.00) · 40 = 1,400. Gold line: “MC = MR solves the firm’s profit maximization problem.” |
-->

### {++ Whiteboard | Exercise Q2 ++}

{++ > Demand rises to $P = 150 - \tfrac{1}{2}Q$, so $MR = 150 - Q$. Costs are unchanged. Find the monopolist’s quantity, price, and profit. ++}

<!--
Not built: no exercise card in the animation.

Answer: 150 − q = 2q, so q\* = 50; P\* = 150 − 25 = 125; ATC\* = 50 + 1000/50 = 70; profit (125 − 70) × 50 = 2,750.
-->

## Changes In Demand

And when preferences in the market change. Quantity. When preferences in the market change the firms optimization problem. The solution to the firms optimization problem also changes.

When the demand curve shifts in. Quantity. The firms quantity also shifts in and the profit goes down. And as you would expect the profit also goes down.

<!--
|   |   |
| --- | --- |
| 4.a | Title: Changes In Demand. The worked rows for steps 1 to 3 leave and the card closes up around the four steps and the live profit row. Leave a thin grey ghost of demand where it was, then pivot demand down about 120 to P = 120 − Q: demand now reaches the axis at 120 units and MR at 60, D / MB slides along its line and MR rides its foot, and the red dot slides down MC. The readouts roll: q\* 40 → 30, P\* 100.00 → 90.00, ATC\* 65.00 → 63.33 and π\* 1,400 → 800. Gold line: “When demand shifts down, the firm’s quantity and profit go down.” |
-->

## Deadweight Loss

The great triangle in this model represents. The grey triangle in this model represents stigly loss, which is.

The great triangle in this model represents dead weight loss, which is associated with a.

Which is associated with the quantity with a marginal private benefit, exceeding the marginal cost or the supply curve.

And the great triangle in this model is dead weight loss, which is associated with the quantity that’s not provided in the market where marginal private benefit exceeds marginal cost.

<!--
|   |   |
| --- | --- |
| 5.a.efficient | Roll demand back and fade the ghost. Title: Deadweight Loss. Gold line: “The socially efficient quantity: where the MC and MB curves intersect.” Then add a yellow dot where MC meets demand at (48, 96), a yellow dashed drop, and 48 over Q_sp under the axis, beside the red 40 over q\*. |
| 5.a | Fill grey strips from MC up to demand over every unit from 40 to 48, and name the area DWL just above demand. Gold line: “Deadweight loss: the quantity not provided where MB exceeds MC.” |
-->

### {++ Whiteboard | Exercise Q3 ++}

{++ > At 40 units, buyers will pay about \$100 for the next unit and it costs about \$80 to make. Why doesn’t the monopolist sell it? ++}

<!--
Not built: no exercise card in the animation.

Answer: to sell one more unit the monopolist lowers the price on all 40 units already being sold. The next unit adds about \$80 to revenue (MR = 120 − 40 = 80) and about \$80 to cost. Beyond 40, each further unit adds less to revenue than to cost, even though buyers value it above its cost.
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
| 6.a.shift | Title: A Per-Unit Tax. Add a green row under the profit row: Tax per unit = \$0. Gold line: “We shift marginal cost and average total cost up by the tax.” Roll the tax from 0 to 30, the cost E2’s spinach closer puts on each unit. A dashed orange copy of MC rises by 30, named MC + tax, and a dashed purple copy of ATC rises by 30, named ATC + tax. The red dot slides up MR to (30, 90). The readouts roll: q\* 40 → 30, P\* 100.00 → 105.00, ATC\* 65.00 → 93.33, now on the dashed ATC, and π\* 1,400 → 350. The profit strips shrink to the band from 93.33 to 105 over 30 units, a green band fills 63.33 to 93.33, and the grey DWL widens to the units from 30 to 48, its name moving inside it. |
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
| 6.b.shift | Remove GOV’s name and roll the tax back to 0. Title: A Lump-Sum Tax. Row: Lump-sum tax = \$0. Gold line: “A lump-sum tax shifts only the average total cost.” Roll the lump sum from 0 to 1,000. The dashed ATC rises as ATC + 1000/q, a fixed cost, named ATC + lump sum. MC does not move and q\* stays 40. ATC\* rolls 65.00 → 90.00 and π\* 1,400 → 400, and the green band fills 65 to 90 over 40 units. |
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
| 6.c.shift | Remove GOV’s name and roll the lump sum back to 0. Title: A Per-Unit Subsidy. Row: Subsidy per unit = \$0. Gold line: “Subsidies tend to increase the quantity exchanged in the market.” Roll the subsidy from 0 to 24. Dashed MC − subsidy and ATC − subsidy move down, and the red dot slides down MR to (48, 72). The readouts roll: q\* 40 → 48, its red quantity row fading as it reaches the yellow 48 over Q_sp, P\* 100.00 → 96.00, ATC\* 65.00 → 44.83 and π\* 1,400 → 2,456. The DWL strips close to nothing. The green band now lies below ATC, from 44.83 to 68.83 over 48 units, inside the profit, and the name Profit sits on the part above ATC. Then change the gold line: “Quantity reaches the socially efficient quantity: zero deadweight loss.” |
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
| 6.d | Title: A Subsidy And A Lump-Sum Tax. Add a second row under the subsidy row: Lump-sum tax = \$0. Keep the subsidy and roll the lump sum from 0 to 2,000. The dashed curve becomes ATC − subsidy + lump sum, a two-line name under ATC’s own. q\* stays 48. ATC\* rolls 44.83 → 86.50 and π\* 2,456 → 456. The green band shrinks to nothing at a lump sum of 1,152 and grows again above ATC, from 68.83 to 86.50: positive revenue. Gold line: “No deadweight loss, positive government revenue, and less profit.” |
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
