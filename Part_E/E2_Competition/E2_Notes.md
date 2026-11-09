---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
plass:
  number-equations: false
---

# E2 | Competitive Firms

Use these notes for the class sequence, lecture, and board-work transitions. The animations introduce new ideas; students attempt the exercise and discuss it at the whiteboard. The outside example opens a question that we resolve at the end.

[Animation](E2_Animation.py) · [Exercise](Exercise/Exercise_E2.md) · [Solutions](Exercise/Exercise_E2_sols.md) · [Gradescope](Exercise/Exercise_E2_gradescope.md)

<!--
Consolidated November 9, 2026. This is the working teaching document. The original notes, alternate dictation, former class plan, old code, and superseded storyboard are preserved in _archive/2026-11-09_consolidation/. Earlier archives remain in _archive/.
The author's first-pass lecture prose and stage directions are retained below, with the shutdown terminology and one reversed loss comparison corrected. Legacy directions that mention side bars, price sweeps, or market reintroductions do not all match the current animation; the current hold comments and E2_Animation.py describe playback. These directions are not requests to rebuild the animation.
Model: TC = 1000 + q^2, MC = 2q, AVC = q, ATC = q + 1000/q. At P = 100, q* = 50 and profit = 1500. The exercise uses other prices for retrieval. No exercise work is performed in the animation.
-->

## Class timing

This is a working time budget, not a video runtime. Stop IDs refer to the current `E2_Animation.py`, scene `EpisodeE2`.

| Minutes | Animation or board work | Purpose |
| --- | --- | --- |
| 0–2 | Opening story and board question | Establish the episode’s question. |
| 2–7 | Play through `1.e.mr` | Market price, price taking, and why MR equals price. |
| 7–9 | Hide projection; Q1a | Retrieve MR with a different price. |
| 9–16 | Resume through `2.e` | Profit, the next-unit comparison, and the chosen quantity. |
| 16–21 | Hide projection; Q1b–c | Choose output and calculate profit. |
| 21–28 | Resume through `3.e` | Entry, losses, and operating versus shutting down. |
| 28–32 | Hide projection; Q2a | Compare two losses at a new price. |
| 32–35 | Resume through `3.f` | Long-run exit and zero economic profit. |
| 35–37 | Hide projection; Q2b–c | Distinguish exit from shutdown; retrieve entry. |
| 37–47 | Keep projection hidden; Q3 | Apply the theory to the fixed-cost shock on the board. |
| 47–49 | Return to the opening question | Students explain the whole adjustment. |
| 49–50 | Resume to `4.a` | Preview downward-sloping firm demand and E3. |

If time slips, shorten the numerical debrief after students have the correct calculation. Protect Q3 and the closing explanation. In a longer class, add the transfer question below rather than a second shock walkthrough.

## Running the room

At each stop, pause playback and hide the projection without advancing. Name the exercise part and put its givens on the board. Students have the prompt on paper.

Give everyone 30–60 seconds alone, then 30 seconds with a neighbor. Ask for a decision and a reason; build the board solution from their answers. Students correct their own work. For Q3, allow two minutes alone and one minute together before discussing. If answers diverge, offer one targeted cue and require another individual answer before explaining.

## Opener

In 2006, an E. coli outbreak was linked to ~~the~~ spinach.[^1] ~~Like other parts of the government,~~ California introduced a leafy-greens food-safety program a year later to make it harder for foodborne illness to spread through crops like spinach. Afterward, growers reported higher costs from this program. What impact ~~did this program~~ {++ would a higher recurring fixed cost ++} have on the market? 

<!--
|   |   |
| --- | --- |
| {++ 0.a ++} | {++ Play the E2 bumper, “Competitive Firms,” after the spoken opener. ++} |
-->

<!-- Editor. The source establishes higher food-safety costs. A recurring fixed expense is the model assumption, not a finding about the program's full market effect. -->

## Competitive markets

We’re going to start with perfect competition.

<!--
|   |   |
| --- | --- |
| {++ 1.a ++} | {++ Show the market-structures grid with Perfect Competition boxed. ++} |
-->

We ~~also~~ have many buyers.

<!--
|   |   |
| --- | --- |
| {++ 1.b.buyers ++} | {++ SHOW THE DEMAND CURVE; reveal “Many buyers.” ++} |
-->

We have many identical firms, ~~low barriers to entry,~~ selling a homogeneous good.

<!--
|   |   |
| --- | --- |
| {++ 1.b.sellers ++} | {++ SHOW THE SUPPLY CURVE; reveal “Many identical sellers.” ++} |
-->

<!--
|   |   |
| --- | --- |
| {++ 1.b.good ++} | {++ Reveal “A homogeneous good.” ++} |
-->

~~And even though we haven’t introduced externalities in these videos yet, it’s important to mention that we’re assuming they don’t exist.~~ {++ We’re also assuming there are no externalities. ++}

<!--
|   |   |
| --- | --- |
| {++ 1.b.externalities ++} | {++ Reveal “No externalities.” ++} |
-->

{++ We also have low barriers to entry. ++}

<!--
|   |   |
| --- | --- |
| {++ 1.b ++} | {++ Reveal “Low barriers to entry.” ++} |
-->

<!--
|   |   |
| --- | --- |
| {++ 1.c ++} | {++ SET UP THE FIRM’S COSTS beside the market: MC and ATC. ++} |
-->

Firms in competitive markets are just one of many, which means their choice of quantity has no real effect on the market price.

<!--
|   |   |
| --- | --- |
| {++ 1.d ++} | {++ DRAW IN THE DEMAND CURVE, WHICH IS ALSO THE PRICE: carry the market price of 100 across to the firm. ++} |
-->

This means competitive firms are what we call price takers. So ~~despite the law of demand, because there are many buyers and sellers,~~ the demand curve looks flat when we’re zoomed in on one firm. This firm changing quantity has no real effect on the price.

> ~~TRY TO ZOOM OUT AND WIGGLE THE INDIVIDUAL FIRM TO SHOW ITS SMALL~~

<!--
|   |   |
| --- | --- |
| {++ 1.e ++} | {++ Change the firm’s quantity while the market price stays fixed. ++} |
-->

{++ So what does one more unit add to revenue? It sells for the market price, and we still get the same price for all the other units. That means the additional revenue from selling one more unit is the price. For a competitive firm, marginal revenue equals price. ++}

<!--
|   |   |
| --- | --- |
| {++ 1.e.mr ++} | {++ Show the equal revenue added by each unit, then label the price line P = MR. ++} |
-->

### ~~Whiteboard Q1a after 1.e.mr~~ {++ Class only — Q1a after 1.e.mr ++}

{++ Exercise Q1a: why is MR the price? ++}

~~{++ Say: “Now close the picture. At a price of 90, what does one more sale add to revenue?” ++}~~

~~{++ Q1a: write $TR(20) = 1800$, $TR(21) = 1890$, so $MR = 90$. Ask why the earlier units still sell for 90. The explanation is price taking, not just the multiplication. Then resume: “Knowing what one more unit brings in lets us compare it with what that unit costs.” ++}~~

## Profit and output

At this price, what quantity maximizes the firm’s profits? Profit is everything left over after we’ve paid our costs, which is TR - TC.

<!--
|   |   |
| --- | --- |
| {++ 2.a ++} | {++ Bring the firm to the center; introduce profit as revenue minus cost. ++} |
-->

> ~~SHOW THE TWO AREAS ON THE COST GRAPH, THEN HAVE THEM TRANSITION TO A TWO VERTICAL LINES TO THE RIGHT OF THE GRAPH~~

<!--
|   |   |
| --- | --- |
| {++ 2.b.revenue ++} | {++ At q = 20 and P = 100, build the revenue area one unit at a time. ++} |
-->

<!--
|   |   |
| --- | --- |
| {++ 2.b.atc.point ++} | {++ Locate ATC at q = 20. ++} |
-->

<!--
|   |   |
| --- | --- |
| {++ 2.b.atc ++} | {++ Trace to the price axis and read ATC = 70. ++} |
-->

<!--
|   |   |
| --- | --- |
| {++ 2.b.cost ++} | {++ Build the cost area one unit at a time. Both areas stay on the graph. ++} |
-->

Profit is the difference between these two areas, so we usually just look at the difference on the graph.

<!--
|   |   |
| --- | --- |
| {++ 2.c.area ++} | {++ SHOW THE DIFFERENCE AREA between price and ATC. ++} |
-->

Which is mathematically equivalent to Q(P-ATC)

> ~~ADD TO THE PROFIT EQUATION~~

<!--
|   |   |
| --- | --- |
| {++ 2.c ++} | {++ Mark the height P − ATC and width q; the bottom line gives q(P − ATC). ++} |
-->

If we start with a small quantity, we wonder whether we should increase quantity.

<!--
|   |   |
| --- | --- |
| {++ 2.d.mc ++} | {++ Read MC at the current quantity. ++} |
-->

<!--
|   |   |
| --- | --- |
| {++ 2.d.unit ++} | {++ Show MR and MC in the Next Unit panel. ++} |
-->

<!--
|   |   |
| --- | --- |
| {++ 2.d.ten ++} | {++ MOVE QUANTITY UP, SHIFT THE AREAS: stop at q = 35. ++} |
-->

And as I hinted, profit will continue to rise until MR = MC, then it will fall.

> ~~MOVE QUANTITY UP AND DOWN, SHIFTING THE AREAS~~

<!--
|   |   |
| --- | --- |
| {++ 2.d.equal ++} | {++ Increase quantity to 50, where MC = MR. ++} |
-->

<!--
|   |   |
| --- | --- |
| {++ 2.d.past ++} | {++ Continue to 60, where MC exceeds MR and profit falls. ++} |
-->

Back to our question: How much should the firm choose to produce? At MC = MR!

<!--
|   |   |
| --- | --- |
| {++ 2.d ++} | {++ Return to q = 50; SHOW MC = MR ON SCREEN. ++} |
-->

<!--
|   |   |
| --- | --- |
| {++ 2.e ++} | {++ Remove the Next Unit panel, mark q\*, and emphasize the MC–MR intersection. ++} |
-->

This is an example of marginal thinking. Our best decision involves thinking on the margin, thinking about the more or one less. When we choose based on whether we should change in little steps instead of big chunks, we can add clarity our decisionmaking.

> ~~MOVE PRICE AROUND, AND SHOW HOW PROFIT CHANGES~~

<!--
|   |   |
| --- | --- |
|  | {++ Hold the chosen quantity. There is no price sweep here in the current animation. ++} |
-->

### Whiteboard Q1b–c after 2.e

{++ Exercise Q1b–c: choose output, then find profit. ++}

~~Q1b–c: write $P = 90$, $MC = 2q$, and $TC = 1000 + q^2$. Students choose $q = 45$. At $q = 40$, $MC = 80 < MR$; at $q = 50$, $MC = 100 > MR$. Increase from 40; decrease from 50. At 45, revenue is 4050, cost is 3025, and economic profit is 1025.~~

~~Draw a small firm graph with MC, ATC, and the price line, locating output first and profit second. Ask: “Why don’t we choose the bottom of ATC?” Quantity maximizes the difference between revenue and cost; minimum ATC is not the general output rule. Use $MC = MR$ on rising MC, subject to the shutdown decision.~~

~~Resume: “What does a profit like this invite other firms to do?” Use the animation to introduce the market adjustment.~~

## Market entry and short-run operation

To think about how the firm’s decisions relate to equilibrium, we need to think about the market as a whole. So we need to zoom back out to see the whole market.

> ~~TRANSFORM THE FLAT DEMAND CURVE INTO A COMPETITIVE MARKET ON THE LEFT~~

<!--
|   |   |
| --- | --- |
| {++ 3.a ++} | {++ Bring back the existing market beside the firm and reconnect their price guides. ++} |
-->

The demand curve is just the willingness to pay of many people all added together.

> ~~WIGGLE DEMAND~~

And the supply curve is the willingness to sell of many sellers all added together.

> ~~WIGGLE SUPPLY~~

We find equilibrium by intersecting the supply and demand curves.

> ~~FIND EQUILIBRIUM ON THE GRAPH~~

This is where the price for the firm comes from.

> PAUSE

<!--
|   |   |
| --- | --- |
|  | {++ Use the existing market picture for this recap; no additional curve reveals or pulses are built here. ++} |
-->

At this price, the firm is making a profit, which is nice for them.

> ~~DO SOMETHING HAPPY ON SCREEN~~

But profit is nice for everyone, so new firms open up to get in on some of that profit. New firms means the supply curve shifts out.

<!--
|   |   |
| --- | --- |
| {++ 3.d.entry ++} | {++ SHIFT THE SUPPLY CURVE OUT; price falls from 100 to 80 and firm output falls to 40. ++} |
-->

This lowers the price, which lowers profit for the firm. Firms will continue to enter until there is no profit left.

<!--
|   |   |
| --- | --- |
| {++ 3.d.zero ++} | {++ SHIFT THE SUPPLY CURVE TOWARD ZERO PROFIT; price reaches about 63.25. ++} |
-->

When price is low, firms are making a negative profit, or what we sometimes call a loss.

<!--
|   |   |
| --- | --- |
| {++ 3.d ++} | {++ SHIFT SUPPLY OUT, SHIFTING PRICE DOWN to 50; the firm produces 25 and earns a loss. ++} |
-->

Firms earning a loss will shut down in the short run if price is below their AVC at the best positive output.

{++ Shutting down means producing nothing this period. We still have to pay the fixed cost. Exiting the industry is a different decision: it lets us avoid those costs in future periods. ++}

> ~~ADD A FC LINE NEXT TO THE TC, TR LINES~~

<!--
|   |   |
| --- | --- |
| {++ 3.e.avc ++} | {++ Add AVC below the price line. ++} |
-->

The firm needs to decide whether operating with a loss is better than shutting down and still paying this period’s fixed cost.

<!--
|   |   |
| --- | --- |
| {++ 3.e.fc ++} | {++ Show fixed cost as the area between AVC and ATC over the chosen output. ++} |
-->

{++ Here, the price is above average variable cost. By operating, the firm earns enough to cover its variable costs and part of its fixed cost. It loses 375 instead of the full fixed cost of 1000. So it keeps operating. ++}

<!--
|   |   |
| --- | --- |
| {++ 3.e ++} | {++ SHOW THE LOSS IS SMALLER THAN FIXED COST WHEN P > AVC; emphasize the loss area. ++} |
-->

### Whiteboard Q2a after 3.e

{++ Exercise Q2a: compare operating with shutting down. ++}

~~Q2a: write $P = 40$, $q = 20$, $TR = 800$, $VC = 400$, and $FC = 1000$. Students compare operating profit of $-600$ with shutdown profit of $-1000$. Operating contributes 400 toward an unavoidable expense. Ask for both losses before accepting “keep operating.”~~

~~Resume: “That tells us what to do this period. It doesn’t tell us whether to stay in this industry indefinitely.”~~

## The long run

In the long run, if price is below the firm’s ATC, they’re making a loss in the long run, and they exit, shifting the supply curve in, and the price up.

> ~~DO SOMETHING~~

<!--
|   |   |
| --- | --- |
| {++ 3.f.exit ++} | {++ Exit shifts supply inward; price rises from 50 to about 63.25. ++} |
-->

And if the price is above the firm’s ATC, they’re making a profit, and new firms enter, shifting the supply curve out, and the price down.

> ~~SHIFT SUPPLY IN AND OUT~~

<!--
|   |   |
| --- | --- |
|  | {++ Hold the equilibrium picture; entry was shown earlier. No further supply cycle is built here. ++} |
-->

Combined, the only long-run stable position is when price is equal to ATC and MC, which also corresponds with zero profit. This gives us the zero profit condition: In the long run, firms earn zero profit.

<!--
|   |   |
| --- | --- |
| {++ 3.f ++} | {++ Emphasize the minimum of ATC where P = MC = ATC and profit is zero. ++} |
-->

### Whiteboard Q2b–c after 3.f

{++ Exercise Q2b–c: entry or exit, and the effect on price. ++}

~~Q2b–c: if the price of 40 persists, exit once future fixed costs can be avoided. If instead the market has the profitable price of 90 from Q1, firms enter, supply increases, and price falls. In the standard identical-firm model, adjustment ends at zero economic profit, $P = MC = \min ATC$.~~

~~Say: “We now have both decisions: how much to produce while operating, and whether to remain in the market. Let’s use them together.” Stay at the board for Q3. Do not return to an animated solution.~~

## Final board problem

{++ Exercise Q3: start at zero profit, raise fixed cost, and draw the immediate and long-run responses. ++}

~~Q3 resets the market to long-run equilibrium, not the price of 40 or 90. The recurring fixed expense raises fixed cost from 1000 to 1600. This period’s payment is unavoidable; future payments can be avoided by exiting. Demand and input prices stay fixed; firms are identical and entry and exit are free.~~

~~Students attempt both graphs before discussion. Build the answer in three stages:~~

1. ~~**Before the shock.** Price meets MC at the minimum of ATC. Label $P_0$, $q_0$, and $Q_0$.~~
2. ~~**Immediately after.** Raise ATC by $600/q$, a smaller gap at larger output, not a parallel shift. Leave MC and AVC fixed. Market supply, price, firm output, and total output initially stay fixed. Shade the loss between the old price and new ATC at $q_0$. Profit falls from zero to $-600$.~~
3. ~~**After exit.** Shift market supply inward. Price rises; survivors move up unchanged MC and produce more. The market moves up demand and total output falls. Stop at the minimum of new ATC: zero economic profit, with fewer firms.~~

~~Ask someone to reconcile higher firm output with lower market output. Write $Q = Nq$: the decline in the number of firms more than offsets the increase in output per survivor. The market price rises through exit; individual price-taking firms do not choose to raise it.~~

~~Instructor check: initially $q_0 \approx 31.62$ and $P_0 \approx 63.25$; finally $q_1 = 40$ and $P_1 = 80$. Immediately after the expense, $TR = 2000$ and $TC = 2600$. Students need not calculate the minima.~~

## Resolve the episode question

{++ Return to the opener: why do some firms leave while the survivors produce more? ++}

~~Point to the opening question. Give students 30 seconds alone to finish:~~

> ~~A higher recurring fixed cost leaves the next unit’s cost unchanged, so initially \_\_\_\_. It reduces \_\_\_\_, so over time \_\_\_\_. That raises \_\_\_\_, which leads the surviving firms to \_\_\_\_.~~

~~Expected: output is unchanged; profit falls; firms exit; market price rises; survivors produce more. Close with:~~

~~**Optional transfer:** “Would a one-time payment already made, with no future payment required, create the same ongoing incentive to exit?” No: exiting cannot recover a sunk payment, and future operating costs have not changed.~~

> A recurring cost can make staying in the industry less attractive without making the next unit more expensive. Exit changes the market price, and that changes the remaining firms’ production decisions. This is one mechanism that can matter when businesses face new compliance costs.

## Next time

Resume to `4.a`: “What happens to marginal revenue when demand slopes down?”

<!--
|   |   |
| --- | --- |
| {++ 4.a ++} | {++ Remove the market and replace the firm’s flat price line with downward-sloping demand. ++} |
-->

[^1]: Source: [UC Small Farms Network](https://ucanr.edu/program/uc-small-farms-network/growers-report-food-safety-costs).
