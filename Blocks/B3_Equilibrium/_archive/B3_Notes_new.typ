// Exported from Plass
#set page(paper: "us-letter", margin: (top: 1in, right: 0.5in, bottom: 1in, left: 0.5in), numbering: "1", number-align: center)
#set par(justify: true, leading: 10.215pt, spacing: 21.465pt)
#set list(spacing: 13.340pt)
#set enum(spacing: 13.340pt)
#set grid.cell(breakable: false)
#show heading.where(level: 1): set text(size: 23.750pt)
#show heading.where(level: 1): set block(above: 26.391pt, below: 25.105pt)
#show heading.where(level: 1): set par(leading: 13.471pt)
#show heading.where(level: 2): set text(size: 17.500pt)
#show heading.where(level: 2): set block(above: 44.650pt, below: 19.937pt)
#show heading.where(level: 2): set par(leading: 9.926pt)
#show heading.where(level: 3): set text(size: 14.375pt)
#show heading.where(level: 3): set block(above: 38.410pt, below: 18.473pt)
#show heading.where(level: 3): set par(leading: 8.153pt)
#show heading.where(level: 4): set text(size: 14.375pt)
#show heading.where(level: 4): set block(above: 38.410pt, below: 18.473pt)
#show heading.where(level: 4): set par(leading: 8.153pt)
#show heading.where(level: 5): set text(size: 14.375pt)
#show heading.where(level: 5): set block(above: 38.410pt, below: 18.473pt)
#show heading.where(level: 5): set par(leading: 8.153pt)
#show heading.where(level: 6): set text(size: 14.375pt)
#show heading.where(level: 6): set block(above: 38.410pt, below: 18.473pt)
#show heading.where(level: 6): set par(leading: 8.153pt)
#show raw.where(block: false): set text(font: "DejaVu Sans Mono", size: 10.000pt)
#show math.equation.where(block: true): set block(above: 21.490pt, below: 23.702pt)
#set text(size: 12.5pt, font: "New Computer Modern", hyphenate: true)
#set math.equation(numbering: "(1)")
#import "@preview/mitex:0.2.5": mi, mitex

== Episode B3 | Equilibrium

_Equilibrium: when no one wants to change_

// plass:comment
// | Storyboard. Each section opens with its beats, one line each, as built on Sep 23 in the opening of B4_Animation.py. That opening follows the seven scenes and is the version to carry forward.
// | B3_Animation.py is the Sep 21 build, used in class that day. Its beats run 2.a to 5.exercise.
// | Camera, layout, and color detail: B4_Efficiency/_archive/B4_Storyboard_2026-09-23.md.
// /plass:comment

=== Opener

// plass:comment
// | 0.a · Bumper with the part, the episode number, and the thesis.
// | Not built: the recap of demand and supply on twin graphs, and the price line that detaches and drifts with a question mark.
// /plass:comment

Last week we started with buyers: we found that individuals preferences about how much spinach to buy obey the law of demand giving us an individual demand curve. Then we took many buyers and found the spinach demand curve. Representing this with algebra allowed us to find the quantity demanded at a whole range of prices.

Then we turned to the other side of the market, sellers: we allowed Molly to make her decision about where to live on the frontier which gave us her individual supply curve, which obeys the law of supply. Then we took all the many farmers growing spinach and found the spinach supply curve. Representing this with algebra allowed us to find the quantity supplied at a whole range of prices.

This answered part of the question about where on the frontier to live but introduced another free variable left to float around Price. In some sense we simply pushed the question of where to live on the PPF one level deeper into prices. Now we put the two together and ask whether there’s a price at which those quantities agree. So this brings us to the question. What happens to prices when we have supply and demand in a market for spinach? Let’s run a little fun simulation to build up some intuition for markets.

To do this, let’s set up a farmer’s market for spinach and use two graphs. One for supply and one for demand.

=== The Basic Exchange

// plass:comment
// | 1.a.price_question · Gary and Molly, head on. MB $6 and MC $2. Title: Which prices work?
// | 1.a.surplus · Price $4. CS $2 and PS $2 appear together, with the green expenditure and revenue boundary and the orange cost.
// | 1.a · The interval from $2 to $6 is marked between the two bars. Bottom: MC < P < MB.
// | Sep 21 build, beats 2.a to 2.b.vi: the same exchange built step by step. Side view, would they both accept, expenditure, CS, revenue, cost, PS, one unit.
// /plass:comment

*\[draft\]* Let’s start with just two people. Gary would pay up to \$6 for a pound of spinach. Growing that pound costs Molly \$2. Now suppose a price of \$4 comes up between them. Would they both say yes? Gary pays less than the spinach is worth to him. Molly receives more than it cost her. So the trade happens.

*\[draft\]* Let’s zoom way in on this one exchange. Gary hands over \$4 — his expenditure. Against his marginal benefit of \$6, that leaves him \$2 of consumer surplus. Molly receives the same \$4 as revenue. Above her cost of \$2, that leaves her \$2 of producer surplus. The price is doing the splitting: it divides the gains from this trade between the two of them.

There is a price that can facilitate this trade if it can be between MC and MB: #mi(`MC < P < MB`).

_*Show a few other prices that don’t work and some that do.*_

*\[draft\]* And notice that any price between \$2 and \$6 would have worked — the same window we saw in Part A, when our two farmers settled on an exchange rate.

_*And then ask “What price should they choose?”*_

=== The Bidding War

// plass:comment
// | 1.b · Amanda-Grace arrives with MB $7 and offers $4.75. Title: Would Molly switch? Bottom: Molly receives $0.75 more.
// | 1.b.competition · Title: Who gets the spinach? Molly switches, Gary answers at $5, and the bids alternate by a quarter up to $6.25 in one play.
// | 1.b.settled · Amanda-Grace buys at $6.25. Bottom: We stop when no one wants to bid.
// /plass:comment

*\[draft\]* Now let’s add another buyer. Two buyers want spinach and Molly only has so much. Whoever would go home empty-handed has a reason to offer a little more, so the price creeps up.

Who should get the spinach? Gary is able to pay Molly and had a nice deal if Amanda-Grace weren’t there.

A price is not stable unless no one has an incentive to switch.

This stability is equilibrium. No one wants to switch.

#quote(block: true)[
  _*Equilibrium*_: _No one wants to switch._

]

=== Multiple Trades

// plass:comment
// | 1.b.before_entry · The plaza with the side graphs. Title: Would any player switch?
// | 1.b.two_trades.plaza · Andrew arrives with MC $4 and asks $4.25. Amanda-Grace and Molly stay paired at $6.25.
// | 1.b.two_trades.center · Gary walks to the circle at the center.
// | 1.b.two_trades · Close-up, title: Gary and Andrew. Bottom: Would Gary buy at $4.25?
// | 1.b.two_trades.accepted · Bottom: Gary gains $1.75. The camera flies back and Gary joins Andrew.
// | 1.b.convergence · Bottom: The same incentives bring both prices together. Both prices move to $5.50 in one play.
// | 1.b.equal_prices · Two trades at $5.50, marked on both side graphs.
// /plass:comment

*\[draft\]* Add another seller and the pressure runs the other way: sellers competing for buyers cut their prices. Andrew is new, so he prices near his cost to get a customer.

If the pairings’ prices weren’t equal, someone could switch and do better.

Prices must be equal for prices to be stable.

=== Buyers

// plass:comment
// | 1.c.buyers.rule · 59 buyers in one row, head on, sorted by MB. Bottom: Buy if MB ≥ P.
// | 1.c.buyers.curve · The line P = 12 − Qd/5 through the tops of the bars.
// | 1.c.buyers · Price $6. 30 green checks, the rest dimmed, and 30 thousand lb under the row.
// | 1.c.buyers.low · The price falls to $3. 45 checks.
// /plass:comment

_*Arrange buyers in order and ask who would buy at a range of prices. Put a green check over them, and a green circle under them to indicate a trade. Then show the graph of the demand curve like we already do and an equation for demand.*_

*\[draft\]* We just have one person per bar, and if someone wants more than one, we just have them show up twice.

_*This should be a large enough number that the equation makes sense as a good approximation.*_

Prices must be equal for everyone. At this price, this is how many people would buy.

_*Then show that some aren’t happy or willing to pay that much, but still want it. Show the offers, which are at the price for those who would pay, and the MB for those who wouldn’t.*_

=== Sellers

// plass:comment
// | 1.c.sellers.units · 100 sellers in one row, head on, sorted by MC.
// | 1.c.sellers.curve · The line P = 2 + Qs/20.
// | 1.c.sellers · Price $3. 20 green checks. Bottom: Sell if MC ≤ P.
// | 1.c.sellers.high · The price rises to $6. 80 checks. Then back to $3.
// /plass:comment

On the seller side, in a separate plaza, it’s a similar setup. The single price, it works for most, but some sellers can’t price that low. Their asks are their MC.

#quote(block: true)[
  _Pause for Exercise B3 | Q2 (a)(b): at 5 galleons on the pumpkin-pasty curves, find the quantity demanded and the quantity supplied._

]

=== Finding Equilibrium

// plass:comment
// | 1.d · Buyers and sellers on the plaza, demand above supply at the right. Title: A low price: $3. Bottom: Who trades?
// | 1.e.willing · The willing step forward with green checks: 45 buyers and 20 sellers. The rest stay at the rim with a red X.
// | 1.e · 20 pairs meet along the center line. 25 willing buyers are left, marked yellow. Shortage 25.
// | 1.e.exchanged · 20 exchanged, labeled on the plaza and on the graph.
// | 1.j · Exercise B3 Q2 card.
// | 1.f.offer · One buyer who is left out is ringed in yellow. Bottom: A buyer who's left out offers a seller more than $3.
// | 1.f.match, 1.f.wait, 1.f · Close-up of three people. Wait at $3: gain $0. Offer $3.25: gain $3.75/lb.
// | 1.f.accepted · The offer is accepted at $3.25, and the three fly back to the plaza.
// | 1.f.incentive · Title: Price adjustment. Bottom: Other unserved buyers have the same incentive.
// | 1.f.adjusted · The price rises to $4 in one play, to 40 willing buyers, 40 willing sellers, and 40 trades. Bottom: Shortages lead to an increase in the price.
// | 1.g · Title: A high price: $6. Bottom: Who trades? 30 and 80 on the graphs.
// | 1.h.offer · 30 pairs, 50 willing sellers left. Excess 50. Bottom: A seller who's left out offers a buyer less than $6.
// | 1.h.match, 1.h.wait, 1.h · Close-up of three people. Keep $6: gain $0. Ask $5.75: gain $1.75/lb.
// | 1.h.accepted · The offer is accepted at $5.75.
// | 1.h.incentive · Bottom: Other unserved sellers have the same incentive. The price falls to $4 in one play.
// | 1.i · Title: Equilibrium. 40 pairs. Bottom: Equilibrium: no willing buyer or seller is left without a trade. Qs = Qd.
// | 1.i.stability · Bottom: What happens to this system if we raise the price a little?
// | 1.i.excess · $4.25 gives 38 and 45. Bottom: Seven willing sellers have no buyer. They can undercut.
// | 1.i.shortage · $3.75 gives 41 and 35. Bottom: Six willing buyers have no seller. They can offer more.
// | 1.i.stable · Back at $4. Bottom: Above $4: excess. Below $4: shortage.
// | Not built here: the word surplus crossed out and replaced by excess. The Sep 21 build has it at beat 5.e.
// /plass:comment

*\[draft\]* But suppose the buyers aren’t happy paying \$4. A bunch of them get together and insist on a lower price: \$3 a pound.

We can find the quantity supplied at this price. Which comes out to be 20,000 pounds. But is this how much buyers are willing to buy at this price? The quantity demanded is 45,000 pounds and we find this by plugging in price into the demand curve.

So it turns out people want more than is available which we call a shortage.

#quote(block: true)[
  _*Shortage*_: _Quantity demanded is greater than quantity supplied._

]

But let’s say in the situation. Amanda-Grace an entrepreneurial buyer decides to offer Molly a higher price. Let’s say three dollars and twenty-five cents. This is good for Molly since she’s making more and it’s good for Amanda-Grace who is more than willing to pay for the higher price if she can receive what she wants.

But it turns out the buyer who was buying from Molly now can’t get any spinach. So, what should they do? They should raise the price.

In this way, whenever there’s a shortage both buyers and sellers have an incentive to raise their prices.

*\[draft\]* Of course, the sellers can play the same game in the other direction.

Let’s say instead spinach sellers sell at a price of \$6. At this price the quantity supplied is 80,000 pounds. And the quantity demanded is 30,000. So people want less than is available. Which we’ll call an excess.

#quote(block: true)[
  _*Excess*_: _Quantity supplied is greater than quantity demanded._

]

I want to offer a little side note here most textbooks call this a surplus but for reasons we’ll get into later. I think this naming convention is less than ideal and can be confusing. So instead of surplus we use excess to describe quantity supplied being greater than quantity demanded. But I just want you to be aware that it’s often called surplus.

So Andrew is sitting around with excess spinach. He can’t sell at 6 per pound. So Andrew being the entrepreneur farmer, decides to offer a price of \$5.75 to Gary.

Gary was buying spinach from another farmer but is more than willing to buy spinach from Andrew at the lower price. And would even buy a little extra. You can think of the law of demand here. That farmer isn’t happy about losing Gary’s business. So they decide to lower their prices too.

In this way, whenever there’s excess both buyers and sellers have an incentive to lower their prices.

#quote(block: true)[
  _Pause for Exercise B3 | Q2 (c)(d): name the situation at 5 galleons, say how large it is, and predict which way the price moves._

]

So prices will rise with a shortage and lower with an excess.

Can there ever be a price that doesn’t change? Yes. What if quantity demanded was equal to quantity supplied? Here no one has an incentive to change their prices or quantities. If a seller raised their price, they would lose all their business.

If they lower their price, they would make less than they could. If a buyer raised their price, they would be paying more than they needed to. And if the buyer lowered their price no seller would sell to them. In this way incentives push the price to the point where quantity supplied is equal to quantity demanded.

#quote(block: true)[
  _*Equilibrium*_: _The price and quantity at which quantity supplied equals quantity demanded — where no one wants to change._

]

Okay, so we’ve found where prices come from. And we’ve found an equilibrium concept that’s stable.

At this equilibrium price and quantity no buyer and no seller wants to change the price they’re offering and the quantity they’re either supplying or demanding from the market. So we call this equilibrium stable.

*\[draft\]* Notice what happened both times: a whole side of the market teamed up to move the price, and it still didn’t hold. Someone always found it worthwhile to break ranks.

=== The Graph and the Algebra

// plass:comment
// | 1.i.graph · The two graphs slide together into one. The lines cross at 40 and $4, and the definition returns.
// | 1.i.algebra.equal · Both equations, with Qd = Qs = Q.
// | 1.i.algebra.equate · 12 − Q/5 = 2 + Q/20.
// | 1.i.algebra.simplify · 10 = Q/4.
// | 1.i.algebra.solve · Q* = 40, then P* = 2 + 40/20 = 4.
// | 1.i.algebra · The starred pair lands on the crossing. Bottom: 40,000 pounds at $4 per pound.
// | Not built here: the Exercise B3 Q1 card. The Sep 21 build has it at beat 4.exercise.
// /plass:comment

We typically combine supply and demand on one graph, so let’s do that here.

Here we’re going to use algebra to build a model using both supply and demand to arrive at the prices that coordinate sellers choices of quantity supplied and buyers choices of quantity demanded.

The supply curve for spinach was price is equal to two plus one over twenty quantity and the demand curve for spinach was price is equal to twelve minus one over five quantity. There’s one price that allows quantity supplied to equal quantity demanded. And that’s where they intersect.

Let’s first solve for the equilibrium quantity then solve for equilibrium price. We set the supply curve equal to the demand curve. Then we solve for quantity which gives us 40. We then take this and plug it into the supply curve.

And solve for price which comes out to be \$4. It would be equivalent if you plugged the quantity into the demand curve and solved for price that way but plugging it into the supply curve is usually easier.

We denote the equilibrium price and quantity with a star.

Plot it on the graph.

#quote(block: true)[
  _Pause for Exercise B3 | Q1: solve for Q\* and P\* in the pumpkin-pasty market on the exercise sheet, then plot the starred pair._

]

=== Closing

*\[draft\]* We’ve found where prices come from. Next time we keep the same setup and ask how good the market’s answer is: we’ll add up the gains from every exchange, and see what happens when a government moves the price.

=== Parked

==== PPF Tieback

// plass:comment
// | The only animated tieback is beat 5.b of _archive/Animate_A.py: the market graph moves to a corner, the two-farmer PPF returns, and the two prices form the exchange-rate line.
// /plass:comment

We’ve spent time talking about markets, the preferences of buyers and sellers, and the incentives that push markets toward equilibrium. And we found that this equilibrium gave us two things: a price and a quantity.

At the beginning of the semester we began by framing the class in the context of the PPF. We had our two farmers who found that if they specialized and traded with each other, they could do better than they could on their own (in autarky).

But we were left with the question of where on the PPF to live. If we fully specialized, we knew what the point on the PPF would be. But we wouldn’t necessarily always fully specialize. We could partially specialize, and still be outside the autarky PPF. So that was a question.

And we proposed markets as a way of picking the point, the pair of quantities. So we built up the intuition for the demand curve, which tells us how much buyers will demand at all possible prices, which satisfies the law of demand. And we built the supply curve, which satisfies the law of supply.

Then we developed our intuition for the market equilibrium. Buyers and sellers have incentive to move the prices and quantities toward market clearing: the point where everything that’s produced by a seller is sold to a buyer. And this equilibrium idea is what gave us a price and quantity.

We’ve only ever looked at a single market. But in the background we know there must be markets for all the goods and services we’re considering. So going back to the farmers, we can apply our notion of markets to tell us something about prices and quantities for spinach and carrots.

Remember we found an exchange rate for trading between the two farmers? We said the exchange rate allowed the farmers to not just co-op, but exchange with each other as separate entities while still benefitting from specialization and trade. We said this exchange rate must live between their own internal exchange rates, represented by their PPFs. We didn’t decide which one was best, but said that there were a range of prices that would make the trade benefit both farmers.

What we’re doing now with markets pins this exchange rate down. Using a market for spinach and a separate market for carrots, we have buyers and sellers making up the demand and supply curves, all facing the incentives that push the market toward equilibrium. The equilibrium generates prices in both markets. And these prices coordinate the decisions of the farmers by forming an exchange rate that allows the farmer to specialize accordingly.

This is some of what’s happening in the background for the farmer, who makes up part of the supply curve. If the farmer is going to produce a crop (and we’ll come back to exactly how the farmer would think about it), their decision about WHICH crop comes from their own production functions and the prices in the markets. When prices are relatively high in the carrot market, both farmers will grow carrots. And the same goes for spinach. But when the prices live somewhere in the middle, between the two farmer’s opportunity costs, then one will grow one crop and the other the other.

And since there are many farmers in the market with different PPFs (and hence different production functions), when working effectively, the market will arrive at a pair of prices that supply the appropriate quantities to the market once every farmer has decided their crop choices.

==== Pit Market

Continue from Part A to model Molly’s preferences. She makes some money from her farm and wants to think about what to spend her income on.

Imagine Molly lives in the town Maryville.

Market simulation. Maryville has buyers who have a maximum price and sellers who have a minimum price. We haven’t talked about where these prices come from yet. We’re going to say these buyers and sellers walk into the marketplace for \#commodity that molly doesn’t grow. Every week buyers and sellers arrive and exchange and leave.

And lets say buyers have a distribution of WTB and sellers have a distribution of WTS.

The idea is to give enough information to predict the equilibrium price before the simulation even starts. I created a spreadsheet with the cards in the deck.

Have some students do the pit market and others use the information to predict the market equilibrium. Red is supply and black is demand.

Follow `en.m.wikiversity.org/wiki/Economic_Classroom_Experiments/Pit_Market`

Run it twice.

Plot of histogram of prices.

Then do the math.

plan 0100 simulation: equilibrium sim by using math to predict the price before. start with the card game version. run it. find the price. then change the cards, use some math, find the price, set the price, and see if anyone switches. it might take a bit more work to get right, but I think it could make the point that equilibrium is predictable and about deviation. maybe don’t even show them the math at first.

==== Decisions

Taylor, Sep 22. Do not re-litigate these in the notes pass or the storyboard.

+ *Seven short scenes, not one long animation.* Each carries one claim and can be rendered, exported, and presented on its own.
+ *No one-at-a-time growth.* Stages are 1×1 → 2×1 → 2×2 → the full market. Bidding, switching, one price, and deliberation are taught on the small stages, then shown for one or two people inside the big one.
+ *Equilibrium is named at scene 2* on the smallest case, as “no one wants to switch,” and re-earned at scene 6 where the counts match.
+ *The price window (\$2–\$6) appears only in scene 1.*
+ *One person per bar.* A buyer who wants more than one stands twice.
+ *The big market is the algebra market.* Demand P = 12 − Q/5, supply P = 2 + Q/20, Q in thousands of pounds. One person = one 1,000-lb lot at the per-pound price. Counts in the plaza equal the algebra’s Qd and Qs at \$3, \$4, \$5, \$6 (see §4 for the quarter-dollar caveat).
+ *One market price line, stepped by Taylor, plus one boxed deliberation per direction.* Not decentralized per-seller price discovery in the big market.
+ *Sorted head-on rows build each curve;* the curve lifts to a side graph; the camera then pulls out to the plaza, where checks and circles happen.
+ *Build the whole thing now.* Scenes 4–6 first: they carry the mechanism and are the assets B4′s price controls reuse.
+ *Class 09 (Wed Sep 23) does not depend on this.* Quick graph-centred review of the current export, straight to Exercise Q2, then B4 (§11).

==== Numbers

- Market: demand P = 12 − Q/5, supply P = 2 + Q/20, equilibrium at 40 and \$4. Q is in thousands of pounds, and one person is one 1,000 pound lot.
- Small cast: Gary MB \$6, Amanda-Grace MB \$7, Molly MC \$2, Andrew MC \$4. First offer \$4. Bids and cuts move in \$0.25 steps.
- At \$3, quantity demanded is 45 and quantity supplied is 20. At \$6, quantity demanded is 30 and quantity supplied is 80.
- Exercise, pumpkin pasties: P = 12 − Qd/2 and P = 2 + Qs/2, equilibrium at 10 and 7. At 5 galleons, Qd is 14 and Qs is 6.
