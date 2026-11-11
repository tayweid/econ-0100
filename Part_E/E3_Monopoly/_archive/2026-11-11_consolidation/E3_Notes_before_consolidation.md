---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

# Monopoly | Episode E3

*Market power breaks the efficiency of markets.*

<!--
Review correction, 2026-10-30: the subtitle "One seller, many buyers." now stays in place from 1.b to 6.d while the titles change around it (the build removed it and faded it back in with every new title, against this storyboard's "Subtitle stays"). The demand row is typeset "D: P = 100 - 1/2 Q" (it rendered as "D : P"). The live profit row gives the = signs and the dot after the parenthesis the same room as the card's rows, and each policy row's $ sits against its number. Nothing else on screen changed.
Animation storyboard for E3_Animation.py, scene EpisodeE3. Built 2026-10-30 from these notes (a transcript of the old 5.3 monopoly video with three directions), the old animation code ported in E3_Animation_original.py (MonopolisticComp: initialize, monopoly_sol and monopoly(alpha, truth, q, tax, lumpsum)) and the old video's thumbnail (q = 50, p = 75, mc = 50, atc = 45, profit 1500, the grey triangle). Taylor writes the spoken notes; these comments list the beats in playback order, with every on-screen line quoted as built.
Playback order: 0 bumper; 1 Monopoly (from the first paragraph to "So the MPB satisfies the law of demand."); 2 Marginal Revenue (to "Using this equation gives us the value…"); 3 The Monopolist's Problem (to "And this is really coming from the fact…"); 4 Changes In Demand (the two paragraphs on preferences); 5 Deadweight Loss (the four grey-triangle paragraphs); 6 taxes and subsidies (to the end of the notes before Next Video); 7 Next Time.
References: E4_Animation.py (the market-structures taxonomy object and its red box, the firm's-problem card), C2_Animations.py (the grey divider at x = 2.45 with a side panel of colored rows, two-row quantity readouts, readouts nudged apart when close), C3_Animations.py and B5_Animation.py (one set of ValueTrackers drives every curve, dot, guide, strip and rolling number; a grey ghost of the old demand), E5_Animation.py (P* in demand's teal and ATC* in ATC's purple, orange profit strips, the yellow Q_sp marker, grey DWL strips), D3_Animation.py (bumper; the taxonomy's box moving to the next cell).
Model (MonopolisticComp, demand share alpha = 2): demand P = 100 - Q/2 (foot at 200), MR = 100 - Q (foot at 100, half of demand's), MC = q, ATC = q/2 + 1000/q (minimum 44.7 at 44.7). MR = MC: q = 100 - q, q* = 50; P* = 100 - 50/2 = 75; ATC* = 25 + 20 = 45; profit (75 - 45) x 50 = 1,500. Section 2: P(20) = 90, P(30) = 85, TR1 = 1,800, TR2 = 2,550, change 10 x 85 - 20 x 5 = 850 - 100 = 750, MR = 750/10 = 75 = MR(25); the sweep's window [Q, Q + 10] runs from Q = 20 to 90, each step's MR equals MR at the midpoint, ending at MR(95) = 5. Check: q = 60 gives P 70, ATC 46.67, profit 1,400; q = 40 gives P 80, ATC 45, profit 1,400. Demand down (alpha from 2 to 4/3: P = 100 - 3Q/4, MR = 100 - 3Q/2): q* = 40, P* = 70, ATC* = 45, profit 1,000. Socially efficient Q_sp = 200/3 = 66.7, where demand meets MC; DWL = 208.3, never shown as a number. Per-unit tax 20 (MC + 20, ATC + 20): q* = 40, P* = 80, ATC* = 65, profit 600, government 20 x 40 = 800 (the band from ATC 45 to 65). Lump-sum tax 1,000 (a fixed cost: ATC + 1000/q): q* = 50, ATC* = 65, profit 500, government 1,000. Subsidy 100/3 = 33.33 per unit (MC - s, ATC - s): q* = 66.7 = Q_sp, P* = 66.67, ATC* = 15.00, profit 3,444, government cost 2,222, no DWL. Subsidy plus a lump-sum tax of 3,000: ATC* = 60, profit 444, government 3,000 - 2,222 = 778. Every number on screen was checked against these formulas (scratchpad e3/model_check.py, 159 checks, all pass), and the scene's own model lambdas give the same values at every hold (e3/code_check.py).
Graph: one market graph, 0 to 200 units by 0 to 120 $/unit, 6.8 by 4.6 units, origin (-5.5, -2.225); MC orange to (110, 110), ATC purple from q = 9.6 (109) to 140, demand teal from (0, 100) to (200, 0) named D / MB just above its lower end, MR pink from (0, 100) to (100, 0) named at its foot. The side panel starts at x = 2.75, right of C2's grey divider at x = 2.45. The dashed policy curves stop at 110 $/unit; a dashed ATC's name keeps 0.14 clear of ATC's own name (0.3 for 6.d's two-line name), above it for a tax or lump sum, below it for a subsidy.
Conventions (E_conventions.md, shared_E.md): plain Scene at 15 fps; the topic title in azure with every word capitalized; the grey CMU Sans subtitle One seller, many buyers. as context from 1.b on; one gold line in the bottom strip (scale 0.7443, centered, 0.05 from the bottom, all under 11.8 units wide) or none; MC orange, ATC purple, demand teal, MR pink; red MR = MC dot, red quantity guide and two-row quantity readout; P* dashed in demand's teal and ATC* dashed in ATC's purple (the style guide's monopoly rule); profit orange strips, government green strips, DWL grey strips, each a stack of one-unit strips with names only; text replaced by removing the old line before the new one fades in; every changing number rolls on a tracker. File header in shared_E.md's order (the maniml line and comments, then the PEP 723 block), imports of style.py only.
Not built: MonopolisticComp's monopolistic-competition entry and exit cycles and MonopolisticCompB's outro (old 5.4 material, not in this semester's plan; still in E3_Animation_original.py). The old mc readout (mc = 50): only q*, P* and ATC* are read off. A second pair of points in section 2: the old code never built the zoom, so one sweep of the same pair traces MR instead. Step 5 of the firm's card (stay or exit): not in these notes. The Next Video paragraphs' monopolistic competition: 7.a cues the duopoly instead. Numbers for the DWL, the government's revenue and the subsidy's cost: the areas carry names only; the profit row carries profit.
Choices left for Taylor: (1) Lines written for this build, his to replace: the subtitle "One seller, many buyers." (E4's, from E1's notes), "MR starts with demand at 100 and falls twice as fast." (2.c), "No deadweight loss, positive government revenue, and less profit." (6.d, summarizing his last three paragraphs), "What happens with two sellers?" (7.a). Verbatim or nearly: 2.b.first, 2.b.second, 2.b.split, 3.b, 3.e.sixty, 3.e.forty, 6.a, 6.c.shift's first line. Trimmed from his sentences: 1.a, 1.b, 1.c, 2.a, 2.b, 2.c.trace, 3.a, 3.c, 3.d, 3.e, 4.a (his "shifts in" said as "shifts down"), 5.a.efficient, 5.a, 6.a.shift, 6.b.shift, 6.b, 6.c.shift's second line, 6.c (his "yellow area" is green here). (2) The old code's model throughout, including its demand share alpha for section 4: demand pivots down about 100 rather than shifting in parallel; 4/3 was picked for whole numbers (40, 70, 45, 1,000); the old loop's first step was 1.344. (3) The lump-sum tax is drawn as a fixed cost, ATC + 1000/q, as the notes describe it; the old code added a constant to ATC, which gives the same ATC* = 65 at q* = 50 but a different curve. (4) Policy sizes: the tax of 20 is the old code's; the lump sums of 1,000 and 3,000 are mine; the subsidy 100/3 is forced by Q_sp = 200/3. (5) Notation: the card's q*, P*, ATC*, π* for the monopolist and E5's Q_sp (yellow) for the efficient quantity, rather than Part C's hats on the market outcome and Q* for efficient. (6) Prices read to two places (75.00) because 3.e and 6.c have thirds; the card's worked rows keep whole numbers (75). (7) Demand is named D / MB (the style guide's four monopoly curves are MC, ATC, MB, MR; E4 and E5 write D), above its lower end because its foot sits at the divider. (8) The card is E4's (curve names colored); step 5 is left out; E5 draws the card differently. (9) Section 2's gain and loss colors: new units teal, the price cut red. (10) The subsidy's green band lies inside the profit (the government pays that part of it) and is drawn over it. (11) Area names (Profit, GOV, DWL) carry a thin halo in the background color because MR, MC and ATC cross the profit rectangle. (12) The taxonomy is E4's object, built before E1's; E1, E3, E4 and E5 should share one.
-->

<!--
0 · Bumper and 1 · Monopoly. Beats, as built.
0.a · The shared bumper: raster MICROECONOMICS, flicker, Part E | Episode 3 beneath it, and the italic thesis in grey under it: "The fewer sellers, the worse." (the notes' italic line). Pause, then clear.
1.a.last · Title: Perfect Competition. No subtitle. E4's market-structures taxonomy centered in the body (grey rules, red row and column words, white cells): columns Homogeneous and Differentiated; rows Many Sellers (Perfect Competition, Monopolistic Competition), Few Sellers (Oligopoly, the differentiated cell blank), One Seller (Monopoly, across both columns). A red box around Perfect Competition, last episode's cell. No bottom text.
1.a · The box moves to Monopoly (0.8 s); title Monopoly; then the bottom line: "A monopolist operates in a market with many buyers and one seller."
1.b · The taxonomy fades. Subtitle: "One seller, many buyers." The graph: P and $/unit at the top of the price axis, Q and units at the end of the quantity axis; MC (orange) from the origin to (110, 110) and ATC (purple) from 109 at q = 9.6 down through its minimum near (44.7, 44.7) and up to (140, 77.1), named MC and ATC at their right ends. The grey divider and the rows "MC = q" (orange) and "ATC = 1/2 q + 1000/q" (purple). Bottom: "As with competitive firms, the production function gives MC and ATC."
1.c · Demand (teal) from 100 on the price axis to its foot at 200 units, named D / MB just above its lower end, and the teal 100 on the price axis; the row "D: P = 100 - 1/2 Q" (teal). Bottom: "Unlike competitive firms, a monopolist faces downward-sloping demand."
Cues. 1.a.last → "But to get a better handle on the marginal revenue curve…". 1.a → "Show 'Monopoly' on screen" and "Monopolist firm operates in markets…". 1.b → "Like last time…" and "Create MC and ATC on the graph". 1.c → "And similar to competitive firms…" through "So the MPB satisfies the law of demand."
-->

But to get a better handle on the marginal revenue curve, lets consider firms who face no competition: Monopoly firms.

*Show ‘Monopoly’ on screen*

Monopolist firm operates in markets with many buyers and one seller.

Like last time with perfectly competitive firms monopolous have a production function which tells us marginal cost curve and an average total cost curve.

*Create MC and ATC on the graph*

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
2 · Marginal Revenue. Beats, as built. The old code never built the notes' "zoom in on two points"; this is the plain two-point version from the outline, with the notes' numbers (20 units at 90, 30 units at 85), then one sweep of the same pair that traces MR.
2.a · Title: Marginal Revenue. Subtitle stays: "One seller, many buyers." The MC and ATC rows leave the panel; the demand row moves to the top; the row "MR = ΔTR / ΔQ" (MR pink) appears below it. Bottom: "Marginal revenue: the change in revenue over the change in quantity."
2.b.first · The first point: a teal dot on demand at (20, 90), a red dashed drop to the quantity axis with 20 over Q1 (red), a teal dashed guide to the price axis with P1 = 90 (teal). Its revenue, 20 units by 90, as teal one-unit strips. Row: "TR1 = 90 × 20 = 1,800" (TR1 teal). Bottom: "Here we're going from a quantity of 20 to a quantity of 30."
2.b.second · A second dot rides demand from the first to (30, 85) on one tracker (2.4 s); its drop and price guide follow. The revenue strips split as it moves: the band from 85 to 90 over the first 20 units turns red (the price cut on the units already sold) and the 10 new units at 85 fill in strong teal. Then P2 = 85 (nudged under P1) and 30 over Q2 fade in (the two quantity rows step 0.08 apart so 20 and 30 do not touch), and the row "TR2 = 85 × 30 = 2,550". Bottom: "So we see the price go down, but the quantity go up."
2.b.split · Row: "ΔTR = 10 × 85 - 20 × 5 = 750" (the gain teal, the loss red, matching the strips); the red band flashes yellow once. Bottom: "So these two factors are moving in opposite directions."
2.b · Row: "MR = 750 / 10 = 75" (MR and 75 pink); a pink dot at (25, 75), halfway between the two quantities. Bottom: "Monopolists are the only seller in the market, so they control the price."
2.c.trace · The readouts and the four worked rows fade (0.6 s); one sweep (4 s) moves the pair along demand from 20 and 30 to 90 and 100, the red and teal strips following, while the pink dot traces a pink line from (25, 75) to (95, 5). Bottom: "Using this equation gives us the value for the marginal revenue curve."
2.c · The pair, its strips and the trace give way to the whole MR line (pink) from (0, 100) to (100, 0), named MR at its foot; the row "MR = 100 - Q" (pink) under the demand row. Bottom: "MR starts with demand at 100 and falls twice as fast."
Cues. 2.a → "To get a sense…" through "And the equation for marginal revenue…". 2.b.first → "So here we're going…" and "Here we're going from a quantity of 20 to a quantity of 30." 2.b.second → "And you can see the price is going down…" through "So we see the price go down…". 2.b.split → "So these two factors…". 2.b → "And this is different…" through "…And so do control the price." 2.c.trace and 2.c → "Using this equation gives us the value for the marginal revenue curve…".
-->

To get a sense of where the marginal revenue curve is coming from.

Let’s zoom in on two points. On the marginal private benefit curve.

Remember the marginal revenue curve is the revenue associated with increasing the quantity by some given amount.

And the equation for marginal revenue is just the change in revenue over the change in quantity.

So here we’re going from a quantity of 90 to a quantity of 85. And you can see that the price.

Here we’re going from a quantity of 20 to a quantity of 30.

And you can see the price is going down due to the law of demand.

It’s going down from 90 to 85, respectively.

So we see the price go down, but the quantity go up.

So these two factors are moving in opposite directions.

And this is different than perfectly competitive firms because.

In contrast to perfectly competitive firms where the price.

Where they had very little effect on the market monopolists are the only seller in the market. And so do control the price.

Using this equation gives us the value for the marginal revenue curve and you can sort of see where it’s coming from.

<!--
3 · The Monopolist's Problem. Beats, as built. The panel becomes E4's firm's-problem card, steps 1 to 4, each with its worked row; step 5 (stay or exit) is not in these notes.
3.a · Title: The Monopolist's Problem. Subtitle stays. The panel's rows give way to "max over q: π = TR - TC" and "1. MC = MR → q*" (MC orange, MR pink); a red dot where MR meets MC at (50, 50); the worked row "q = 100 - q, so q* = 50" (q orange, 100 - q pink, q* = 50 red); then the red dashed drop and 50 over q* (red) under the axis. Bottom: "To solve any firm's problem, set marginal cost equal to marginal revenue."
3.b · "2. q* → D → P*" (D teal); the drop rises from the dot to demand at (50, 75) (0.8 s); a teal dot, a teal dashed guide to the price axis and P* = 75.00 (teal, the monopoly rule: each readout dashed in its own curve's color); the worked row "P* = 100 - 1/2 · 50 = 75" (75 teal). Bottom: "Using quantity with the demand curve allows us to find price."
3.c · "3. q* → ATC → ATC*" (ATC purple); a purple dot on ATC at (50, 45), a purple dashed guide and ATC* = 45.00 (purple); the worked row "ATC* = 1/2 · 50 + 1000/50 = 45" (45 purple). Bottom: "Quantity with the average total cost curve gives the average total cost."
3.d · "4. π* = (P* - ATC*) · q*"; orange one-unit strips from ATC* up to P* over the 50 units (2 s), named Profit; the worked row "π* = (75 - 45) · 50 = 1,500" (1,500 orange). Bottom: "Price, average total cost and quantity give us the firm's profits."
3.e.sixty · The stars come off the readouts (P =, ATC =, q) and the worked profit row becomes a live row "π = (70.00 - 46.67) · 60 = 1,400", every number rolling; one tracker moves the quantity from 50 to 60 (2.4 s): the drop, the teal and purple dots and guides, P and ATC on the axis and the profit strips all follow; the red MR = MC dot stays at (50, 50). Bottom: "If we increase the quantity to 60, their profit goes down."
3.e.forty · The quantity rolls to 40: P = 80.00, ATC = 45.00, profit 1,400. Bottom: "If we lower the quantity to 40, their profit also goes down."
3.e · Back to 50 (2.4 s); the stars return (P* = 75.00, ATC* = 45.00, q*, "π* = (75.00 - 45.00) · 50 = 1,500"). Bottom: "MC = MR solves the firm's profit maximization problem."
Cues. 3.a → "With these tools in hand…" through "This gets this gives us quantity…". 3.b and 3.c → "Using quantity with the demand curve…". 3.d → "Using price average total cost…". 3.e.sixty → "And here we can verify…" and "If we increase the quantity to 60…". 3.e.forty → "And if we lower the quantity to 40…". 3.e → "And this is really coming from the fact…".
-->

With these tools in hand, let’s go back and think about the monopolist problem. How they set how a monopolist would set quantity.

How a monopolist would set price and quantity.

To do this remember the solution to every firms optimization problem is to set marginal cost equal to marginal revenue.

This gets this gives us quantity. And using quantity we can then use.

Using quantity with the demand curve allows us to find price. And similarly with the average total cost curve allows us to find the average total cost.

Using price average total cost and. Quantity allows us to find the firms profits.

And here we can verify that marginal cost equally marginal revenue actually solves the firms profit maximization problem.

If we increase the quantity to 60. Their profit goes down.

And if we lower the quantity to 40 their profit also goes down.

And this is really coming from the fact that as we increase quantity price also goes down from the law of demand and if we decrease quantity prices going up by the law of demand but not fast enough to compensate for the lower quantity.

<!--
4 · Changes In Demand. Beat, as built.
4.a · Title: Changes In Demand. Subtitle stays. The worked rows for steps 1 to 3 leave and the card closes up around the four steps and the live profit row. A thin grey ghost of demand stays where it was; the old code's demand share rolls from 2 to 4/3 (2.4 s): demand and MR pivot down about 100 (feet at 133 and 67), D / MB and MR ride their curves, the red dot slides down MC, and q* 50 → 40, P* 75.00 → 70.00, ATC* 45.00 → 45.00 (it dips to 44.72 on the way) and π* 1,500 → 1,000 roll. Bottom: "When demand shifts down, the firm's quantity and profit go down." (the notes say "shifts in"; Taylor's rule since 09-30 is up/down).
Cues. 4.a → both paragraphs.
-->

And when preferences in the market change. Quantity. When preferences in the market change the firms optimization problem. The solution to the firms optimization problem also changes.

When the demand curve shifts in. Quantity. The firms quantity also shifts in and the profit goes down. And as you would expect the profit also goes down.

<!--
5 · Deadweight Loss. Beats, as built.
5.a.efficient · Demand rolls back (2.4 s) and the ghost fades. Title: Deadweight Loss. Subtitle stays. Bottom: "The socially efficient quantity: where the MC and MB curves intersect." Then a yellow dot where MC meets demand at (66.7, 66.7), a yellow dashed drop and 66.7 over Q_sp (yellow) under the axis, beside the red 50 over q*.
5.a · Grey strips from MC up to demand over every unit from 50 to 66.7 (1.6 s), named DWL just above demand. Bottom: "Deadweight loss: the quantity not provided where MB exceeds MC."
Cues. 5.a.efficient and 5.a → these four paragraphs.
-->

The great triangle in this model represents. The grey triangle in this model represents stigly loss, which is.

The great triangle in this model represents dead weight loss, which is associated with a.

Which is associated with the quantity with a marginal private benefit, exceeding the marginal cost or the supply curve.

And the great triangle in this model is dead weight loss, which is associated with the quantity that’s not provided in the market where marginal private benefit exceeds marginal cost.

<!--
6 · Taxes and subsidies. Beats, as built. Four trackers (a per-unit tax, a lump-sum tax, a per-unit subsidy, and demand) drive every mark; the panel keeps the card's four steps and the live profit row, with the policy's size rolling in a green row under it. The green government band runs between the firm's true ATC and its ATC under the policy, over the q* units; profit runs from the policy ATC up to P*; DWL runs from MC up to demand between q* and Q_sp.
6.a.shift · Title: A Per-Unit Tax. Subtitle stays. Row: "Tax per unit = $0" (green). Bottom: "We shift marginal cost and average total cost up by the tax." The tax rolls 0 → 20 (3.2 s): a dashed orange copy of MC rises to (0, 20)–(100, 120), named MC + tax, and a dashed purple copy of ATC rises by 20, named ATC + tax; the red dot slides down MR to (40, 60), q* 50 → 40, P* 75.00 → 80.00, ATC* 45.00 → 65.00 (now on the dashed ATC), π* 1,500 → 600; the profit strips shrink to 65..80 over 40 units, the green band fills 45..65, the grey DWL widens to 40..66.7.
6.a · The band is named GOV. Bottom: "As the tax goes up, quantity goes down and deadweight loss goes up."
6.b.shift · GOV's name leaves; the tax rolls back to 0. Title: A Lump-Sum Tax. Row: "Lump-sum tax = $0". Bottom: "A lump-sum tax shifts only the average total cost." The lump sum rolls 0 → 1,000 (3.2 s): the dashed ATC rises as ATC + 1000/q (a fixed cost; the old code added a constant, which gives the same 65 at q* = 50), named ATC + lump sum; MC does not move and q* stays 50; ATC* 45.00 → 65.00, π* 1,500 → 500, the green band fills 45..65 over 50 units.
6.b · GOV. Bottom: "This transfers some of the firm's profits to the government."
6.c.shift · GOV's name leaves; the lump sum rolls back to 0. Title: A Per-Unit Subsidy. Row: "Subsidy per unit = $0.00"; the live profit row now shows the quantity to two places (50.00), since the subsidy's quantity is 200/3. Bottom: "Subsidies tend to increase the quantity exchanged in the market." The subsidy rolls 0 → 33.33 (3.2 s): dashed MC - subsidy and ATC - subsidy move down; the red dot slides down MR to (66.7, 33.3); q* 50 → 66.7 (the red quantity row fades as it reaches the yellow 66.7 over Q_sp), P* 75.00 → 66.67, ATC* 45.00 → 15.00, π* 1,500 → 3,444 (the row reads (66.67 - 15.00) · 66.67 = 3,444); the DWL strips close to nothing; the green band now lies below ATC, 15..48.3 over 66.7 units, inside the profit; the name Profit sits on the part above ATC. Then the bottom line: "Quantity reaches the socially efficient quantity: zero deadweight loss."
6.c · GOV. Bottom: "The green area represents a negative government revenue." (his line, with green for the old yellow)
6.d · Title: A Subsidy And A Lump-Sum Tax. A second row "Lump-sum tax = $0" under the subsidy row. The lump sum rolls 0 → 3,000 (3.6 s) with the subsidy kept: the dashed curve becomes ATC - subsidy + lump sum (a two-line name set 0.3 under ATC's name, beside its curve's end); q* stays 66.7; ATC* 15.00 → 60.00, π* 3,444 → 444; the green band shrinks to nothing (at a lump sum of 2,222) and grows again above ATC, 48.3..60: positive revenue. Bottom: "No deadweight loss, positive government revenue, and less profit."
Cues. 6.a.shift → "This model also allows us…" through "So because we're applying a tax to every individual unit…". 6.a → "As the tax goes up…". 6.b.shift → "This is one kind of tax…" through "So this ship's only the average total cost." 6.b → "And what this does is essentially transfer…" and "What you can see here…". 6.c.shift → "But what if we included a subsidy…" through "Where quantity is equal to the socially efficient quantity…". 6.c → "But one of the problems here…" through "We're the yellow area…". 6.d → "So what if we include both…" to the end of the section.
-->

This model also allows us to look at the effect of taxes on the monopolists solution and government revenue.

Profit and dead weight loss.

So if we impose a tax instead of using a tax wedge, we’re just going to shift the the cost curve for the firm.

So we shift the marginal cost and the average total cost up by the amount of the tax.

Remember marginal cost. Captures the costs associated with adding one more unit.

So when we include a tax the costs are going up by the amount exactly equal to the tax.

And the same is true for average total cost.

We’re saying average show cost is the cost associated with the total number of units sold divided by the total number of units.

So because we’re applying a tax to every individual unit, we’re just increasing the average by the amount of attacks.

As the tax goes up quantity goes down and dead weight loss goes up.

This is one kind of tax but we also have another type of tax at our disposal called a lump, sum tax. So a lump, sum tax. A lump sum tax is simply taxing the firm, independently of how much they’re producing.

We typically don’t look at these types of taxes in competitive markets, but when we look at monopolies, lumpsum taxes can be useful and we’re going to demonstrate why. So first introducing a lump sum tax because it doesn’t depend on. Because the value of the tax doesn’t depend on how much is being produced or simply taxing the firm for existing. It doesn’t affect the marginal cost curve.

We’re not shifting the cost curve up by any given amount or essentially just increasing the fixed cost for the firm.

So this ship’s only the average total cost.

And what this does is essentially transfer some of the firms profits to the government. So one of the worries.

What you can see here with the tax and the lumpsum tax neither policy is effective at increasing the quantity to the socially efficient quantity where the marginal cost curve and the marginal product private benefit curve intersect.

But what if we included a subsidy we’ve looked at subsidies in the past and we’ve said subsidies increase.

Subsidies tend to increase the quantity exchanged in the market.

Here if we impose a subsidy on the monopolist. Their marginal cost curve the shifts out. And they’re intersection point with the marginal revenue curve also shifts out. And if we do it appropriately we can find attacks.

Where quantity is equal to the socially efficient quantity giving us zero dead weight loss.

But one of the problems here is that we’re transferring wealth from the government to the firm.

We’ve increased the firms profits and we’ve. Imposed a cost on the government.

We’re the yellow area represents a negative government revenue.

So what if we include both a tax and a lump, sum tax?

That gives us something like the following. Here we’ve increased the quantity.

Here we’ve increased the quantity to something like to something close to the socially efficient quantity and we effectively eliminated dead weight loss.

We’ve also generated positive revenue for the firm by simultaneously subsidizing quantity exchanged. By effective by subsidizing the. By. By including a subsidy and a lump, sum tax. We’ve changed the firms marginal incentives by rewarding them. By rewarding the firm for selling.

But we’ve also taken away some of their profits using a lump, sum tax.

## Next Video

<!--
7 · Next Time. Beat, as built. The notes' next video, monopolistic competition, is not taught this semester; E4 is the duopoly, so the cue points there.
7.a · Everything on screen freezes and fades (0.8 s). Title: Next Time. No subtitle. The taxonomy from 1.a returns with the red box on Monopoly; the box moves to Oligopoly (0.8 s), where E4 opens. Bottom: "What happens with two sellers?"
-->

In the next video we’re going to look at monopolistically competitive firms firms that have a similar model to monopolies, but are competitive in a waste in a similar way to perfectly competitive firms.

The model look very similar to monopolous, but we’re also going to have an element of dynamics where firms enter an exit based on their profits.
