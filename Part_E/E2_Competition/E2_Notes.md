---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

# Episode E2

The revenue side

<!--
Review correction, 2026-10-30 (fresh-eyes review): every area name now sits at the spot nearest its area's centre that keeps clear of MC, ATC and the area's edges; before, ATC ran through TR and the profit name and MC through TC. The profit box is named π, not “Profit”: the word could not sit in the q = 40 box clear of ATC (shared_E.md allows Profit or π). 3.c pulses the profit box instead of its name, and the title The Long Run now starts at 3.f.exit, so it holds through all of 3.f. The beat lines below are updated to match; they supersede the first build's 2.b.revenue, 2.b.cost, 2.c.area, 3.c, 3.f.exit and 3.f.
Animation storyboard for E2_Animation.py, scene EpisodeE2. Built 2026-10-30 and rendered headlessly (132 checkpoints, 43 holds, every hold reviewed). Taylor writes the spoken notes; these comments list the beats in playback order, with every on-screen line quoted as built.
Playback order: 0 bumper; 1 Perfect Competition (the paragraphs before “At this price, what quantity…”, with the second pass's five conditions as the checklist); 2 Profit (“At this price, what quantity…” through MOVE PRICE AROUND); 3 The Market, then Entry And Exit and The Long Run (“To think about how…” to the end of the first pass); 4 Next Time. The second pass (Perfect Competition, Profit) tells the same story; its directions are served by the beats named under its headings.
References: E2_Animation_original.py (PerfectCompA: the cost graph, the flat price at 80, the TR and TC boxes, the profit box sweeping q; PerfectCompB: the market left of the firm, supply turning about the origin as firms enter, one price for both graphs, the closing zero-profit sentence), E4_Animation.py (the market-structures taxonomy, the same object and red box), C2_Animations.py (graph left of a grey divider with a panel on the right, two-row quantity readouts, one-unit strips, readout groups), C3_Animations.py and B5_Animation.py (one tracker drives a moving curve, its dot, guides and rolling numbers), D3_Animation.py (bumper and holds).
Model (03_Code.py, shared with E1 and E3): MC = q, ATC = q/2 + 1000/q, AVC = q/2, FC = 1000, so TC = q²/2 + 1000; ATC is lowest at q = √2000 = 44.72, where MC = ATC = 44.72. The firm takes the price 80: MR = 80 = MC gives q* = 80, ATC 52.50, TR 6,400, TC 4,200, π = 2,200. At q = 40: ATC 45.00, TR 3,200, TC 1,800, π = 1,400; q = 50: TR 4,000, TC 2,250, π = 1,750; q = 100: ATC 60.00, TR 8,000, TC 6,000, π = 2,000. Price 60: q* 60, ATC 46.67, TR 3,600, TC 2,800, π = 800; price 90: q* 90, ATC 56.11, TR 8,100, TC 5,050, π = 3,050. The market (Q in thousands): D: P = 100 − Q, S: P = Q/α through the origin, α growing as firms enter, so P* = 100/(1 + α) and Q* = 100 − P*; P* = 80 at α = ¼ (Q* = 20). Entry and exit stops: P* 60 (Q* 40, π = 800), 50 (Q* 50, TR 2,500, TC 2,250, π = 250), 30 (Q* 70, q* 30, ATC 48.33, TR 900, TC 1,450, π = −550; AVC 15, FC 1,000, so the loss is FC less q(P − AVC) = 1,000 − 450), 48 (Q* 52, TR 2,304, TC 2,152, π = 152), then 44.72 (Q* 55, q* shown as 45, TR = TC = 2,000, π = 0). Every number on screen was recomputed from these formulas (63 checks, all pass).
Graphs: both share one price scale, 0–120 $/unit over 4.6 units, on one baseline. The firm's graph is 0–120 units over 4.2 (P, $/unit; q, units); the market's 0–120 thousand over 2.6 (P, $/unit; Q, 1,000 units), unit captions under P. The firm's graph sits centered in section 1, left of a grey divider with the profit panel in section 2, and right of the market in 1.e and section 3. The bars stand on a grey floor at the graphs' baseline, 0.44 units of height per $1,000, total and name in two rows under each bar.
Conventions (E_conventions.md, shared_E.md): plain Scene at 15 fps; the topic title in azure with every word capitalized; a grey CMU Sans subtitle only for context; one gold line in the bottom strip (scale 0.7443, centered, 0.05 from the bottom) or none; firm palette MC orange, ATC purple, AVC pink, FC grey, the firm's price and the market's demand teal, profit orange, loss red; one-unit strips for every area on a graph; red guides, dots and quantity readouts; per-unit dollars with two decimals, totals and quantities whole; one tracker for the price and one for the firm's quantity drive every representation (they move together once q* = P); text replaced by removing the old line before the new one fades in. File header in shared_E.md's order, imports of style.py only.
Not built: DO SOMETHING HAPPY ON SCREEN is only a plain yellow pulse of the profit box and the bar's orange piece (3.c); DO SOMETHING is read as the exit move (3.f.exit). A price below AVC: with AVC = q/2 the firm's AVC at q* = P is always P/2, so this model never shuts down in the short run; 3.e shows the keep-operating case only. MC readouts on the price axis (old PerfectCompA's “MC =”): the MC dot alone carries marginal cost. The ATC readout in section 3 (removed so the red price line can cross into the firm's axis). The number of firms (1,000α, 250 at the start). The firm's-problem card (shared_E.md lets E2 cue it; not cued). The marginal revenue curve the header sentence promises (“This video builds the marginal revenue curve…”): only the Next Time cue. The old Week 5 outline intro and the “Can competitive firms maintain profits?” card.
Choices left for Taylor: (1) The thesis is the header line, “The revenue side”, set in grey italics without a period; it is plain text in these notes and describes marginal revenue rather than competition. (2) Lines written or adapted for this build, his to replace: the subtitle “One firm among many.”; the checklist's “A homogeneous good” and “No externalities” (from “selling a homogeneous good” and “with no externalities”); 1.d, 2.c.area, 2.d.past and 2.e (his sentences with their openings cut: “This means…”, “Proft is the difference…, so…”, “And as I hinted,”, “Back to our question:”); 1.e.out “Zoomed in on one firm, the demand curve looks flat.” (his sentence rearranged); 2.b.cost “Profit is the difference between these two areas.” (his, with “Proft” spelled out); 2.d.question “Should we increase our quantity by 10?” (the second pass's “we can ask whether we should increase our quantity by 10” as a question); 3.b.demand and 3.b.supply (his sentences trimmed to “Demand: …”, “Supply: …”); 3.d.entry “New firms open up, so the supply curve shifts down.” (his shifts out, said down); 3.d (his sentence recast around “a negative profit”); 3.e.fc (his sentence as a question); 3.e “Price is above AVC, so the loss is smaller than the fixed cost.” (written); 3.f.exit and 3.f.cycle (his sentences shortened, in and out said up and down); 3.f (his, without “This gives us the”); 4.a “What happens to marginal revenue when demand slopes down?” (written from the header). Titles The Market, Entry And Exit, The Long Run and Next Time are written; Perfect Competition and Profit are his headings. (3) FC = 1000 puts the long run at 44.72, so q* shows 45 beside P* = 44.72; FC = 800 would make it exactly q* = P* = 40. (4) The loss stop is P* = 30 (old PerfectCompB's first step was 33.33); at 40 the loss box was too thin to read. (5) The bars keep one scale throughout, so small profits (152, 250) are thin slivers. (6) The zoom in 1.e is new: a small yellow box at the market's crossing grows into a yellow frame on the firm's graph. (7) Readout colors: the firm's price teal and its ATC purple, each in its own curve's color as the monopoly rule asks; the market's P* red; quantities red. (8) The taxonomy is E4's object with its red box; the wiggles are the style guide's yellow Indicate pulse. (9) The profit box is named π, a size up (0.9) from the word names, since “Profit” would not fit the q = 40 box clear of the ATC curve; the loss box keeps “Loss”. (10) Per-unit prices show two decimals (80.00, 45.00), the conventions brief's rule; the lead's outline had asked for whole dollars except the long-run 44.72.
-->

This video builds the marginal revenue curve, showing how marginal revenue changes when demand moves from a flat to downward sloping.

<!--
0 · Bumper and 1 · Perfect Competition. Beats, as built.
0.a · The shared bumper: raster MICROECONOMICS, flicker, Part E | Episode 2 beneath it, and the header line in grey italics under it: “The revenue side”. Pause, then clear.
1.a · Title: Perfect Competition. The market-structures taxonomy (E4's object, D1's Table look): columns Homogeneous and Differentiated; rows Many Sellers (Perfect Competition, Monopolistic Competition), Few Sellers (Oligopoly, the differentiated cell blank), One Seller (Monopoly across both columns). A red box around Perfect Competition. No subtitle, no bottom text.
1.b.buyers → 1.b.sellers → 1.b.good → 1.b.externalities → 1.b · The taxonomy leaves. A small market graph on the left and the second pass's five conditions in grey on the right, centered as one block; each lights white on its own hold: “1. Many buyers” with demand (teal, D), “2. Many identical sellers” with supply (orange, S), “3. A homogeneous good”, “4. No externalities”, “5. Low barriers to entry”. No bottom text.
1.c · The market and the list leave. The firm's graph, centered: MC orange, ATC purple named at its upper left, a yellow dot at the bottom of ATC. Subtitle: “One firm among many.” No bottom text.
1.d · A flat teal line at 80, named “P = MR”, with 80.00 in teal on the price axis. Bottom: “Competitive firms are what we call price takers.”
1.e.out · The firm's graph slides right and the market returns on the left; a small yellow box appears where supply meets demand (20, 80), then a copy of it grows into a yellow frame on the firm's graph. Bottom: “Zoomed in on one firm, the demand curve looks flat.”
1.e · A red dot on the flat line, its dashed drop and the two-row readout 60 over q; one eased wiggle 60 → 90 → 30 → 60 while the market and the price stay put. Bottom: “This firm changing quantity has no real effect on the price.”
Cues. 1.a → “We’re going to start with perfect competition.” 1.b.* → “We have many identical firms…” through “…we’re assuming they don’t exist.”, or the second pass's list. 1.c → SET UP THE FIRM’S COSTS. 1.d → “Firms in competitive markets…” and “This means competitive firms are what we call price takers.” 1.e.out and 1.e → “So despite the law of demand…” and TRY TO ZOOM OUT AND WIGGLE.
-->

We’re going to start with perfect competition. We have many identical firms, low barriers to entry, selling a homogeneous good.

*SHOW THE SUPPLY CURVE*

We also have many buyers.

*SHOW THE DEMAND CURVE*

And even though we haven’t introduced externalities in these videos yet, it’s important to mention that we’re assuming they don’t exist.

*SET UP THE FIRM’S COSTS*

Firms in competitive markets are just one of many, which means their choice of quantity has no real effect on the market price.

*DRAW IN THE DEMAND CURVE, WHICH IS ALSO THE PRICE*

This means competitive firms are what we call price takers. So despite the law of demand, because there are many buyers and sellers, the demand curve looks flat when we’re zoomed in on one firm. This firm changing quantity has no real effect on the price.

*TRY TO ZOOM OUT AND WIGGLE THE INDIVIDUAL FIRM TO SHOW ITS SMALL*

<!--
2 · Profit. Beats, as built.
2.a.word · Title: Profit (no subtitle). The market and the zoom marks leave and the firm's graph slides left; a grey divider and the word “Profit” right of it. No bottom text.
2.a · “Profit” turns into π, then “= TR − TC” (π orange, TR teal, TC purple). Bottom: “Profit is everything left over after we’ve paid our costs.”
2.b.revenue · q = 40: the red drop to the price line and 40 over q; then total revenue as 40 one-unit teal strips up to 80, named TR in its upper part, right of ATC. No bottom text.
2.b.cost · A purple dashed guide to ATC at 40 and 45.00 in purple on the price axis; then total cost as 40 purple strips up to 45, named TC above MC, which crosses the area from its corner. Bottom: “Profit is the difference between these two areas.”
2.b · The two areas pour into two bars right of the graph, one slice per unit, on a grey floor; the names TR and TC move under them, with 3,200 and 1,800 above the names. Bottom stays.
2.c.area · The difference on the graph: 40 orange strips between 45 and 80, named π (white), right of the ATC curve that cuts across the box. From here on the name π (or Loss) rides with the box, always clear of MC and ATC, and fades when the box is too thin to hold it. Bottom: “So we usually just look at the difference on the graph.”
2.c.side · A copy of the profit strips flies to the side and becomes the top of the TR bar above the TC bar, in orange; “π = 1,400” in orange above the bars. Bottom stays.
2.c · The equation grows: “π = TR − TC = q(P − ATC)”. No bottom text.
2.d.question · A red dot on MC at q = 40 (marginal cost 40, below the price). Bottom: “Should we increase our quantity by 10?”
2.d.ten · q rolls 40 → 50: the box, bars and numbers roll together (45.00, 4,000, 2,250, π = 1,750). Bottom stays.
2.d.past · Bottom: “Profit will continue to rise until MR = MC, then it will fall.” q rolls 50 → 100 in one motion; π peaks at 2,200 at 80 and ends at 2,000 (ATC 60.00, TR 8,000, TC 6,000); the MC dot climbs above the price line.
2.d · q rolls back to 80 (52.50, 6,400, 4,200, π = 2,200). Bottom stays.
2.e · The readout's q becomes q* and the MC dot, now on the price line, pulses. Bottom: “How much should the firm choose to produce? At MC = MR!”
2.f.low → 2.f.high → 2.f · Bottom: “This is an example of marginal thinking.” The price and q* roll together, q* riding MC: 80 → 60 (46.67, 3,600, 2,800, π = 800), → 90 (56.11, 8,100, 5,050, π = 3,050), → 80.
Cues. 2.a.word and 2.a → “At this price, what quantity maximizes…”, or the second pass's TRANSFORM THE WORD PROFIT INTO PI and PROFIT = REVENUE - COSTS. 2.b.* → SHOW THE TWO AREAS… and GRAPH TOTAL REVENUE AND TOTAL COST. 2.c.area → “Proft is the difference between these two areas…”. 2.c.side → TRANSFORM THE DIFFERENCE AREA INTO THE PROFIT SYMBOL ON THE SIDE. 2.c → “Which is mathematically equivalent to Q(P-ATC)”. 2.d.question and 2.d.ten → “If we start with a small quantity…”. 2.d.past and 2.d → “And as I hinted…”. 2.e → “Back to our question…”. 2.f.* → “This is an example of marginal thinking…”.
-->

At this price, what quantity maximizes the firm’s profits? Profit is everything left over after we’ve paid our costs, which is TR - TC.

*SHOW THE TWO AREAS ON THE COST GRAPH, THEN HAVE THEM TRANSITION TO A TWO VERTICAL LINES TO THE RIGHT OF THE GRAPH*

Proft is the difference between these two areas, so we usually just look at the difference on the graph.

*SHOW THE DIFFERENCE AREA*

Which is mathematically equivalent to Q(P-ATC)

*ADD TO THE PROFIT EQUATION*

If we start with a small quantity, we wonder whether we should increase quantity.

*MOVE QUANTITY UP, SHIFT THE AREAS*

And as I hinted, profit will continue to rise until MR = MC, then it will fall.

*MOVE QUANTITY UP AND DOWN, SHIFTING THE AREAS*

Back to our question: How much should the firm choose to produce? At MC = MR!

*SHOW MC = MR ON SCREEN*

This is an example of marginal thinking. Our best decision involves thinking on the margin, thinking about the more or one less. When we choose based on whether we should change in little steps instead of big chunks, we can add clarity our decisionmaking.

*MOVE PRICE AROUND, AND SHOW HOW PROFIT CHANGES*

<!--
3 · The Market. Beats, as built.
3.a · Title: The Market. The equation and the ATC guide and readout leave; the firm's graph, its bars and the divider move right; the market's axes return on the left and a copy of the firm's flat line turns into the market's demand; supply fades in. Bottom: “So we need to zoom back out to see the whole market.”
3.b.demand · Bottom: “Demand: the willingness to pay of many people, all added together.” Demand pulses yellow.
3.b.supply · Bottom: “Supply: the willingness to sell of many sellers, all added together.” Supply pulses yellow.
3.b.equilibrium · Bottom: “We find equilibrium by intersecting the supply and demand curves.” A red dot where they cross, dashed guides, “P* = 80.00” on the market's price axis and 20 over Q*.
3.b · The red dashed price line runs on from the market to the firm's price axis; the firm's own 80.00 leaves. Bottom: “This is where the price for the firm comes from.”
3.c · Bottom: “At this price, the firm is making a profit, which is nice for them.” The profit box and the orange top of the TR bar pulse yellow.
Cues. 3.a → “To think about how the firm’s decisions relate to equilibrium…” and TRANSFORM THE FLAT DEMAND CURVE…. 3.b.demand and 3.b.supply → the two WIGGLE paragraphs. 3.b.equilibrium → FIND EQUILIBRIUM ON THE GRAPH. 3.b → “This is where the price for the firm comes from.” and PAUSE. 3.c → DO SOMETHING HAPPY ON SCREEN.
-->

To think about how the firm’s decisions relate to equilibrium, we need to think about the market as a whole. So we need to zoom back out to see the whole market.

*TRANSFORM THE FLAT DEMAND CURVE INTO A COMPETITIVE MARKET ON THE LEFT*

The demand curve is just the willingness to pay of many people all added together.

*WIGGLE DEMAND*

And the supply curve is the willingness to sell of many sellers all added together.

*WIGGLE SUPPLY*

We find equilibrium by intersecting the supply and demand curves.

*FIND EQUILIBRIUM ON THE GRAPH*

This is where the price for the firm comes from.

*PAUSE*

At this price, the firm is making a profit, which is nice for them.

*DO SOMETHING HAPPY ON SCREEN*

<!--
3 · Entry And Exit, The Long Run. Beats, as built.
3.d.entry · Title: Entry And Exit. Bottom: “New firms open up, so the supply curve shifts down.” Supply turns down about the origin; P* rolls 80 → 60 on the market and the firm's flat line follows; q* rides MC to 60; the box, bars and π roll (π = 800).
3.d.zero · Bottom: “Firms will continue to enter until there is no profit left.” P* 60 → 50 (π = 250; the box is a sliver and its name fades).
3.d · Bottom: “A negative profit is what we sometimes call a loss.” P* 50 → 30: the box flips above the price, turns red and is named Loss; the TC bar's top turns red; “π = −550” in red (TR 900, TC 1,450).
3.e.avc · AVC (pink) joins the firm's graph with a pink dot at q* = 30, AVC 15, below the price. Bottom: “Firms earning a loss will exit the market if price is below their AVC.”
3.e.fc · The floor grows a third slot: a grey FC bar, 1,000 over FC. Bottom: “Is operating with a loss better than exiting and paying the fixed cost?”
3.e · A copy of the red loss piece slides into the base of the FC bar: 550 against 1,000. Bottom: “Price is above AVC, so the loss is smaller than the fixed cost.”
3.f.exit · Title: The Long Run. AVC, the FC bar and the copy leave and the floor shrinks back. Bottom: “A loss in the long run: firms exit, supply shifts up, the price rises.” Supply turns up; P* 30 → 48; the box is orange again (π = 152).
3.f.cycle · Bottom: “A profit: new firms enter, supply shifts down, the price falls.” One eased motion in and out: the price falls past 44.72 to 43.74 (a small loss), comes back to 44.90 and settles at 44.72.
3.f · The yellow dot at the bottom of ATC pulses under the red MC = MR dot; P* = 44.72, Q* 55, q* 45, TR = TC = 2,000, π = 0. Bottom: “Zero profit condition: in the long run, firms earn zero profit.”
Cues. 3.d.entry → “But profit is nice for everyone…” and SHIFT THE SUPPLY CURVE OUT. 3.d.zero → “This lowers the price…” and SHIFT THE SUPPLY CURVE TOWARD ZERO PROFIT. 3.d → “When price is low…” and SHIFT SUPPLY OUT, SHIFTING PRICE DOWN. 3.e.avc → “Firms earning a loss will exit…”. 3.e.fc → ADD A FC LINE NEXT TO THE TC, TR LINES. 3.e → “The firm needs to decide…” and SHOW LOSS > FC WHEN P > AVC. 3.f.exit → “In the long run, if price is below the firm’s ATC…” and DO SOMETHING. 3.f.cycle → “And if the price is above the firm’s ATC…” and SHIFT SUPPLY IN AND OUT. 3.f → “Combined, the only long-run stable position…”.
-->

But profit is nice for everyone, so new firms open up to get in on some of that profit. New firms means the supply curve shifts out.

*SHIFT THE SUPPLY CURVE OUT*

This lowers the price, which lowers profit for the firm. Firms will continue to enter until there is no profit left.

*SHIFT THE SUPPLY CURVE TOWARD ZERO PROFIT*

When price is low, firms are making a negative profit, or what we sometimes call a loss.

*SHIFT SUPPLY OUT, SHIFTING PRICE DOWN*

Firms earning a loss will exit the market if price is below their AVC.

*ADD A FC LINE NEXT TO THE TC, TR LINES*

The firm needs to decide whether operating with a loss is better than exiting and paying the fixed cost.

*SHOW LOSS > FC WHEN P > AVC*

In the long run, if price is below the firm’s ATC, they’re making a loss in the long run, and they exit, shifting the supply curve in, and the price up.

*DO SOMETHING*

And if the price is above the firm’s ATC, they’re making a profit, and new firms enter, shifting the supply curve out, and the price down.

*SHIFT SUPPLY IN AND OUT*

Combined, the only long-run stable position is when price is equal to ATC and MC, which also corresponds with zero profit. This gives us the zero profit condition: In the long run, firms earn zero profit.

<!--
4 · Next Time. Beats, as built.
4.a · Title: Next Time. The market, the bars, the readouts and the yellow dot leave; the firm's graph returns to center and its flat line tilts into a downward-sloping D. Bottom: “What happens to marginal revenue when demand slopes down?”
Cue. 4.a → the end of the first pass; the header's “This video builds the marginal revenue curve…” is the next episode's job.
-->

## Perfect Competition

<!-- Second pass over section 1: its five conditions are the 1.b checklist, ZOOM IN ON ONE AND WIGGLE THE QUANTITY is 1.e.out and 1.e, and “price takers” is 1.d. -->

We’re gonna start with a perfectly competitive market with 1) many buyers, 2) many identical sellers, 3) selling a homogeneous good, 4) with no externalities, and 5) low barriers to entry.

*SHOW EACH OF THESE ITEMS ON SCREEN*

Competitive markets are composed of many sellers, so any one firm has no real control over the market price.

So despite the law of demand because there are many buyers in many sellers the demand curve looks flat when we’re zoomed in on the firm.

*ZOOM IN ON ONE AND WIGGLE THE QUANTITY*

This means competitive firms are what we call price takers.

So the firm’s decision is to choose the best quantity given the market price. What should the firm try to do?

## Profit

<!-- Second pass over sections 2 and 3: TRANSFORM THE WORD PROFIT INTO PI is 2.a, GRAPH TOTAL REVENUE AND TOTAL COST is 2.b, TRANSFORM THE DIFFERENCE AREA INTO THE PROFIT SYMBOL ON THE SIDE is 2.c.side, and the rest follows sections 2 and 3. -->

The first goal we embew firms with is to maximize their profits. There are others, but this is the simplest and most basic.

*TRANSFORM THE WORD PROFIT INTO PI*

Profit is everything left over after we’ve paid our costs.

*PROFIT = REVENUE - COSTS*

Graphically, profit is the difference between the two areas representing total revenue and total cost.

*GRAPH TOTAL REVENUE AND TOTAL COST*

*TRANSFORM THE DIFFERENCE AREA INTO THE PROFIT SYMBOL ON THE SIDE*

If we start with a small quantity we can ask whether we should increase our quantity by 10.

We can watch profits as we continue to increase.

As I hinted in the last video price will continue to rise.

As I hinted in the last video profit will continue to rise until marginal revenue is equal to marginal cost.

Then as we continue past this point profit will fall.

So back to our question. How much should the firm choose to produce?

They will choose to produce they should choose to produce where.

Marginal cost is equal to marginal revenue.

This is an example of marginal thinking: Our best decision involves thinking on the margin thinking about one more or one less.

So to think about to think about how the firm’s decision relates to equilibrium, we need to think about the market as a whole.

So we need to zoom back out to see the whole market.

The demand curve is just the willingness to pay of many buyers. All added together.

And the supply curve is the willingness to sell of many sellers all added together.

And as we’ve always done we find equilibrium by intersecting the supply curve with the demand curve.

And this gives us our equilibrium in the market.

This is where the this is where the price for the firm comes from.

At this price the firm is making a profit, which is nice for them. But profit is nice for everyone.

So in the presence of profits new firms are going to open up to get in on some of that profit.

And when new firms enter the market this means the supply curve shifts out because there are more sellers selling.

When the supply curve shifts out this low is the price which lowers profits for the firm.

When the prices low firms are making a negative profit.

When the price is low firms are making a negative profit or what we sometimes call a loss.

Firms earning the loss will exit the market if their price is below.

A lower price lowers the the optimal quantity the firm should produce and it.

Ended means some firms will drop out of the market.

In the long run if price is below the firms average total cost, they’re making a loss in the long run in the exit.

Shifting the supply curve in and the price up.

And if the price is above the firms average total cost, they’re making a profit and new firms enter shifting the supply curve out in the price down.

Combined the only stable position in the long run is when price is equal to average total cost and equal to marginal cost which also corresponds with zero profit.

This gives us the zero profit condition.

In the long run in competitive markets firms earn zero profit.
