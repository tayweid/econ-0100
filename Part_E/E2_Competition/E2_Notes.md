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

## Opening question

Before starting the animation, say:

> In 2006, an E. coli outbreak was linked to spinach. California introduced a leafy-greens food-safety program the following year, and growers surveyed afterward reported higher food-safety costs. That gives us a question about competition: how can a higher cost push some firms out of a market while the firms that stay eventually produce more?

> We’ll isolate one kind of cost: a recurring expense that doesn’t depend on how much a firm produces. We’ll come back to that question once we have the pieces.

Write **Higher fixed cost: fewer firms, but more output per surviving firm?** in a corner of the board. Leave it there. Use “the firm” and “the market” through the rest of the lesson; no agricultural detail is needed in the exercise.

Source: [UC Small Farms Network](https://ucanr.edu/program/uc-small-farms-network/growers-report-food-safety-costs). The report documents higher seasonal food-safety costs. The pure recurring fixed expense and resulting exit are the classroom model, not claims about measured spinach-industry outcomes.

## Competitive markets

<!--
Current animation holds. Repeated bottom text remains visible across successive holds.
0.a · Introductory animation hold; no bottom teaching line.
1.a · Introductory animation hold; no bottom teaching line.
1.b.buyers · Introductory animation hold; no bottom teaching line.
1.b.sellers · Introductory animation hold; no bottom teaching line.
1.b.good · Introductory animation hold; no bottom teaching line.
1.b.externalities · Introductory animation hold; no bottom teaching line.
1.b · Introductory animation hold; no bottom teaching line.
1.c · Introductory animation hold; no bottom teaching line.
1.d · Bottom: “Competitive firms are what we call price takers.”
1.e · Bottom: “This firm changing quantity has no real effect on the price.”
1.e.mr · Bottom: “One more unit sells for the price: marginal revenue is the price.”
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

### Whiteboard Q1a after 1.e.mr

Say: “Now close the picture. At a price of 90, what does one more sale add to revenue?”

Q1a: write $TR(20) = 1800$, $TR(21) = 1890$, so $MR = 90$. Ask why the earlier units still sell for 90. The explanation is price taking, not just the multiplication. Then resume: “Knowing what one more unit brings in lets us compare it with what that unit costs.”

## Profit and output

<!--
Current animation holds. Repeated bottom text remains visible across successive holds.
2.a · Bottom: “Profit is everything left over after we’ve paid our costs.”
2.b.revenue · Bottom: “Each unit sells for the market price.”
2.b.atc.point · Bottom: “Plug the quantity into average total cost.”
2.b.atc · Bottom: “On average, each unit costs \$70.”
2.b.cost · Bottom: “Profit is the difference between these two areas.”
2.c.area · Bottom: “So we usually just look at the difference on the graph.”
2.c · Bottom: “Which is mathematically equivalent to $q(P - \mathrm{ATC})$.”
2.d.mc · Bottom: “What does the next unit cost to make?”
2.d.unit · Bottom: “Should we increase our quantity by 1?”
2.d.ten · Bottom: “Should we increase our quantity by 1?”
2.d.equal · Bottom: “Profit will continue to rise until MR = MC.”
2.d.past · Bottom: “Then it will fall.”
2.d · Bottom: “How much should the firm choose to produce? At MC = MR!”
2.e · Bottom: “How much should the firm choose to produce? At MC = MR!”
-->

At this price, what quantity maximizes the firm’s profits? Profit is everything left over after we’ve paid our costs, which is TR - TC.

*SHOW THE TWO AREAS ON THE COST GRAPH, THEN HAVE THEM TRANSITION TO A TWO VERTICAL LINES TO THE RIGHT OF THE GRAPH*

Profit is the difference between these two areas, so we usually just look at the difference on the graph.

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

### Whiteboard Q1b–c after 2.e

Q1b–c: write $P = 90$, $MC = 2q$, and $TC = 1000 + q^2$. Students choose $q = 45$. At $q = 40$, $MC = 80 < MR$; at $q = 50$, $MC = 100 > MR$. Increase from 40; decrease from 50. At 45, revenue is 4050, cost is 3025, and economic profit is 1025.

Draw a small firm graph with MC, ATC, and the price line, locating output first and profit second. Ask: “Why don’t we choose the bottom of ATC?” Quantity maximizes the difference between revenue and cost; minimum ATC is not the general output rule. Use $MC = MR$ on rising MC, subject to the shutdown decision.

Resume: “What does a profit like this invite other firms to do?” Use the animation to introduce the market adjustment.

## Market entry and short-run operation

<!--
Current animation holds. Repeated bottom text remains visible across successive holds.
3.a · Bottom: “The price comes from the market.”
3.d.entry · Bottom: “With profit, more firms enter, shifting the supply curve.”
3.d.zero · Bottom: “With profit, more firms enter, shifting the supply curve.”
3.d · Bottom: “A negative profit is a loss.”
3.e.avc · Bottom: “Firms earning a loss will exit the market if price is below their AVC.”
3.e.fc · Bottom: “Is operating with a loss better than exiting and paying the fixed cost?”
3.e · Bottom: “Price is above AVC, so the loss is smaller than the fixed cost.”
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

But profit is nice for everyone, so new firms open up to get in on some of that profit. New firms means the supply curve shifts out.

*SHIFT THE SUPPLY CURVE OUT*

This lowers the price, which lowers profit for the firm. Firms will continue to enter until there is no profit left.

*SHIFT THE SUPPLY CURVE TOWARD ZERO PROFIT*

When price is low, firms are making a negative profit, or what we sometimes call a loss.

*SHIFT SUPPLY OUT, SHIFTING PRICE DOWN*

Firms earning a loss will shut down in the short run if price is below their AVC at the best positive output.

*ADD A FC LINE NEXT TO THE TC, TR LINES*

The firm needs to decide whether operating with a loss is better than shutting down and still paying this period’s fixed cost.

*SHOW THE LOSS IS SMALLER THAN FIXED COST WHEN P > AVC*

### Spoken wording corrections

At `3.e.avc`, the screen says firms “exit” below AVC. Say **shut down in the short run**. The usual shutdown threshold is minimum AVC; at equality the firm is indifferent. At `3.e.fc`, replace “exiting and paying the fixed cost” aloud with **shutting down and still paying this period’s fixed cost**. Long-run exit avoids future fixed costs. The animation is unchanged.

This firm’s $AVC = q$ has a minimum of zero. The positive-price loss example demonstrates continued operation, not a positive shutdown-price threshold.

### Whiteboard Q2a after 3.e

Q2a: write $P = 40$, $q = 20$, $TR = 800$, $VC = 400$, and $FC = 1000$. Students compare operating profit of $-600$ with shutdown profit of $-1000$. Operating contributes 400 toward an unavoidable expense. Ask for both losses before accepting “keep operating.”

Resume: “That tells us what to do this period. It doesn’t tell us whether to stay in this industry indefinitely.”

## The long run

<!--
Current animation holds. Repeated bottom text remains visible across successive holds.
3.f.exit · Bottom: “With a loss, firms exit, shifting the supply curve.”
3.f · Bottom: “The only place with no change is where there is no profit.”
-->

In the long run, if price is below the firm’s ATC, they’re making a loss in the long run, and they exit, shifting the supply curve in, and the price up.

*DO SOMETHING*

And if the price is above the firm’s ATC, they’re making a profit, and new firms enter, shifting the supply curve out, and the price down.

*SHIFT SUPPLY IN AND OUT*

Combined, the only long-run stable position is when price is equal to ATC and MC, which also corresponds with zero profit. This gives us the zero profit condition: In the long run, firms earn zero profit.

### Whiteboard Q2b–c after 3.f

Q2b–c: if the price of 40 persists, exit once future fixed costs can be avoided. If instead the market has the profitable price of 90 from Q1, firms enter, supply increases, and price falls. In the standard identical-firm model, adjustment ends at zero economic profit, $P = MC = \min ATC$.

Say: “We now have both decisions: how much to produce while operating, and whether to remain in the market. Let’s use them together.” Stay at the board for Q3. Do not return to an animated solution.

## Final board problem

Q3 resets the market to long-run equilibrium, not the price of 40 or 90. The recurring fixed expense raises fixed cost from 1000 to 1600. This period’s payment is unavoidable; future payments can be avoided by exiting. Demand and input prices stay fixed; firms are identical and entry and exit are free.

Students attempt both graphs before discussion. Build the answer in three stages:

1. **Before the shock.** Price meets MC at the minimum of ATC. Label $P_0$, $q_0$, and $Q_0$.
2. **Immediately after.** Raise ATC by $600/q$, a smaller gap at larger output, not a parallel shift. Leave MC and AVC fixed. Market supply, price, firm output, and total output initially stay fixed. Shade the loss between the old price and new ATC at $q_0$. Profit falls from zero to $-600$.
3. **After exit.** Shift market supply inward. Price rises; survivors move up unchanged MC and produce more. The market moves up demand and total output falls. Stop at the minimum of new ATC: zero economic profit, with fewer firms.

Ask someone to reconcile higher firm output with lower market output. Write $Q = Nq$: the decline in the number of firms more than offsets the increase in output per survivor. The market price rises through exit; individual price-taking firms do not choose to raise it.

Instructor check: initially $q_0 \approx 31.62$ and $P_0 \approx 63.25$; finally $q_1 = 40$ and $P_1 = 80$. Immediately after the expense, $TR = 2000$ and $TC = 2600$. Students need not calculate the minima.

## Resolve the episode question

Point to the opening question. Give students 30 seconds alone to finish:

> A higher recurring fixed cost leaves the next unit’s cost unchanged, so initially \_\_\_\_. It reduces \_\_\_\_, so over time \_\_\_\_. That raises \_\_\_\_, which leads the surviving firms to \_\_\_\_.

Expected: output is unchanged; profit falls; firms exit; market price rises; survivors produce more. Close with:

> A recurring cost can make staying in the industry less attractive without making the next unit more expensive. Exit changes the market price, and that changes the remaining firms’ production decisions. This is one mechanism that can matter when businesses face new compliance costs.

**Optional transfer:** “Would a one-time payment already made, with no future payment required, create the same ongoing incentive to exit?” No: exiting cannot recover a sunk payment, and future operating costs have not changed.

## Next time

<!--
Current animation holds. Repeated bottom text remains visible across successive holds.
4.a · Bottom: “What happens to marginal revenue when demand slopes down?”
-->

Resume to `4.a`: “What happens to marginal revenue when demand slopes down?”
