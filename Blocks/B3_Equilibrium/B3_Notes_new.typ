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

== Episode B3 | Equilibrium

_Equilibrium: when no one wants to change_

=== Teaching Plan

These are preparation notes for the seven scenes in #link("B3_Outline.typ")[B3 Outline]. They combine the current notes with the useful teaching points in #link("01_Notes_scenes_2026-09-22.md")[the September 22 scene draft]. The older draft retains the detailed staging history; this version organizes the economics and the work students do in class.

*The question for B3:* Where do prices come from? Buyers and sellers respond to prices; their incentives push a competitive market toward a price at which their quantities agree. Individual consumer and producer surplus help explain those incentives. Adding up welfare and evaluating price controls belong in B4.

*Pacing:* Keep scenes 1–3 to roughly the opening ten minutes. Use one exchange, one bidding example, and one example of switching between sellers. Move directly to the full set of buyers and sellers. If using existing animation, run repeated bids or market entry quickly; do not pause over each arrival or each switch. Protect at least half the class for scenes 6–7, including students drawing, calculating, and explaining.

*Board and paper:* Students begin working in scene 1, draw demand in scene 4, add a separate supply graph in scene 5, mark gaps in scene 6, and combine the curves in scene 7. Keep these graphs available throughout. Use the existing Exercise B3 in pieces: Q2(a)(b), then Q2(c)(d), then Q1. The teaching order differs from the printed order.

*Opener:* Demand tells us how much buyers want at each price. Supply tells us how much sellers want at each price. We have left the price floating. What happens when the two sides meet in a market for spinach?

=== Scene 1 | The Basic Exchange

*Claim:* A price between a seller’s marginal cost and a buyer’s marginal benefit can make both willing to trade, but this alone does not select a price.

Gary would pay up to \$6 for a pound of spinach. Growing that pound costs Molly \$2. At a price of \$4, would both say yes? Gary pays less than the spinach is worth to him. Molly receives more than it costs her.

Gary’s \$4 expenditure is Molly’s \$4 revenue. Gary gains \$2, measured by consumer surplus, $"MB"-P$. Molly gains \$2, measured by producer surplus, $P-"MC"$. Use these amounts to explain why each accepts. Leave aggregate surplus areas for B4.

#quote(block: true)[
  *Paper pause:* Try prices of \$5, \$7, and \$1. At each price, would Gary buy and would Molly sell? At \$5, calculate each person’s gain.
]

*Check:* At \$5 both accept: Gary gains \$1 and Molly gains \$3. At \$7 Gary declines; at \$1 Molly declines. For both to gain strictly, $"MC" < P < "MB"$. At either endpoint one person is indifferent; count an indifferent person as willing for the quantity exercises that follow.

Any price strictly between \$2 and \$6 benefits both. This is like the range of exchange rates that could support trade in Part A. End with the unresolved question: *What price should they choose?*

=== Scene 2 | The Bidding War

*Claim:* A buyer who is left out can have an incentive to offer more, and a seller can have an incentive to accept.

Amanda-Grace values the pound at \$7. Gary is buying it from Molly for \$4. Compare Amanda-Grace’s two options: stay out and gain nothing, or offer \$4.75 and gain \$2.25. Molly receives \$0.75 more by switching. Count both sides of the proposed trade.

Gary can answer with \$5 and still gain \$1. Ask who will get the spinach, then compress the remaining bidding. At \$6.25 Amanda-Grace gains \$0.75; Gary cannot profitably outbid her because his MB is only \$6.

#quote(block: true)[
  *Ask:* Why does Gary stop? He still likes spinach. What makes another bid unattractive?
]

The answer is his next-best option: not buying gives him zero, while buying above \$6 gives him a loss. Being left out does not always create an incentive to bid more.

Introduce the idea of *equilibrium*: no one wants to switch. Here we have shown why the bidding stops. One seller and this particular bidding path do not establish a unique competitive market price. The full market will let us connect the stability idea to supply and demand.

=== Scene 3 | Multiple Trades

*Claim:* For the same good in a market where people can switch freely, different transaction prices create an opportunity to do better.

Add Andrew, whose MC is \$4. Suppose Gary buys from Andrew at \$4.25 while Amanda-Grace buys from Molly at \$6.25. Both trades are individually acceptable. Can these two prices last?

Amanda-Grace would prefer the cheaper spinach. She could offer Andrew \$4.50: she gains \$2.50 instead of \$0.75, and Andrew receives \$0.25 more. This can displace Gary and leave Molly looking for a buyer. The same incentives that raise a low offer can push a high asking price down.

#quote(block: true)[
  *Quick comparison:* Write Amanda-Grace’s gain and Andrew’s gain before and after the proposed switch. Why is it not enough to say that Amanda-Grace would like a lower price?
]

*Check:* Amanda-Grace’s gain rises from \$0.75 to \$2.50; Andrew’s rises from \$0.25 to \$0.50. The alternative must also be acceptable to the trading partner.

Use two trades at \$5.50 as an example of a common price. Do not walk through every intervening switch. With these four people, multiple common prices can support two trades; we have explained pressure toward *one price across trades*, not yet pinned down *which price*. Assume identical spinach, visible prices, and no costs of switching.

=== Scene 4 | Buyers

*Claim:* At a given price, the demand curve counts the quantity buyers are willing to buy; it does not tell us how many trades actually happen.

Move directly to the full set of buyers, ordered from highest MB to lowest. Each bar represents one unit decision. Someone who wants several units contributes several such decisions. For the large spinach market, measure quantity in *thousands of pounds* and price in *dollars per pound*. A displayed unit now represents a 1,000-pound lot; MB and MC remain per-pound amounts.

Buy if $"MB" >= P$. A buyer below the price line will not pay that price; their MB is the most they would offer. A buyer above it is willing to buy, but still needs a seller. Keep willingness separate from receiving spinach.

$ P = 12 - frac(Q_d, 5) quad <==> quad Q_d = 60 - 5P $

#quote(block: true)[
  *Board and paper:* Draw demand with price on the vertical axis and quantity on the horizontal axis. Label the intercepts. At \$6, read the quantity horizontally to the curve and then down to the quantity axis. Repeat at \$3. Predict the direction before calculating.
]

*Check:* The intercepts are \$12 and 60 thousand pounds. At \$6, $Q_d=30$; at \$3, $Q_d=45$. These are movements along the same demand curve. Use a few prices, not a slow count of individual buyers.

=== Scene 5 | Sellers

*Claim:* At the same price, supply counts the quantity sellers are willing to sell.

Use a separate graph for sellers, ordered from lowest MC to highest. Sell if $"MC" <= P$. A seller whose cost exceeds the price declines; their MC is the lowest price they would accept. Willingness to sell does not guarantee a buyer.

$ P = 2 + frac(Q_s, 20) quad <==> quad Q_s = 20P - 40 $

#quote(block: true)[
  *Board and paper:* Draw supply beside or below demand using matching axis scales. Mark its price intercept and find the quantities supplied at \$3 and \$6. Use the same price on both graphs.
]

*Check:* Supply begins at \$2 when $Q_s=0$. At \$3, $Q_s=20$; at \$6, $Q_s=80$. The stated supply equation applies at prices of at least \$2; below that, quantity supplied is zero.

#quote(block: true)[
  *Exercise B3 | Q2(a)(b):* At 5 galleons in the pumpkin-pasty market, find quantity demanded and quantity supplied. Add separate demand and supply sketches on paper and mark the two quantities. Save the interpretation for scene 6.
]

*Instructor check:* $Q_d=14$ pasties and $Q_s=6$ pasties. Neither number by itself is “the market quantity.”

=== Scene 6 | Finding Equilibrium

*Claim:* Count both sides at one price. The side left without trades explains the pressure on price.

Before revealing the result at each price, have students predict the quantities and who will be left out. In this simple market, with willing buyers and sellers matched, the amount exchanged is the smaller of quantity demanded and quantity supplied.

==== A low price: \$3

At \$3, buyers want 45,000 pounds and sellers offer 20,000 pounds. Only 20,000 pounds can change hands. The remaining 25,000 pounds of demand are unfilled.

#quote(block: true)[
  *Shortage:* Quantity demanded exceeds quantity supplied. Its size is $Q_d-Q_s$.
]

An unserved Amanda-Grace can gain by offering \$3.25 instead of remaining without spinach: her gain is \$3.75 per pound. A seller gains by accepting the higher offer. Other unserved buyers have the same kind of incentive. As price rises, quantity demanded falls and quantity supplied rises, closing the gap.

Use one buyer’s comparison, then move directly to \$4. At that price, 40,000 pounds are demanded and 40,000 pounds are supplied. There is no longer a group of willing buyers unable to find sellers.

==== A high price: \$6

At \$6, buyers want 30,000 pounds and sellers offer 80,000 pounds. Only 30,000 pounds change hands. Sellers are willing to sell 50,000 pounds more than buyers want.

#quote(block: true)[
  *Excess:* Quantity supplied exceeds quantity demanded. Its size is $Q_s-Q_d$. Textbooks often call this a “surplus”; use “excess” here to distinguish it from consumer and producer surplus.
]

Suppose Andrew, whose MC is \$4, has no buyer. Offering \$5.75 gives him a gain of \$1.75 per pound instead of zero. Gary gains by switching from a seller charging \$6. Other unserved sellers have a reason to undercut too. As price falls, quantity supplied falls and quantity demanded rises, closing the gap.

Again, use one comparison and move directly to \$4. There is no longer a group of willing sellers unable to find buyers.

#quote(block: true)[
  *Board and paper:* On the separate spinach graphs, mark the same horizontal price at \$3, then at \$6. Label both quantities, the amount exchanged, and the size of the gap. Add an arrow showing the predicted price movement.

  *Exercise B3 | Q2(c)(d):* Return to the two quantities at 5 galleons. Name and measure the gap, then explain which side has an incentive to move the price and in which direction.
]

*Instructor check:* The pasty market has a shortage of 8 pasties; 6 can trade at that price. Unserved buyers can offer more, putting upward pressure on price.

==== The price that holds: \$4

#quote(block: true)[
  *Equilibrium:* The price and quantity at which $Q_d=Q_s$. Buyers and sellers are choosing their preferred quantities at the prevailing price, and those choices are compatible.
]

At \$4, 40,000 pounds are demanded, supplied, and exchanged. “No one wants to change” means no one can improve their outcome through an available trade or switch at the going market opportunities. It does not mean everyone likes the price or everyone buys. Buyers with MB below \$4 and sellers with MC above \$4 choose to stay out.

*Stability check:* Ask what happens a little above \$4 and a little below it. Above: excess and downward pressure. Below: shortage and upward pressure. Have students explain this from the slopes on their graphs; another long sequence of price changes is unnecessary. Price adjustment here is an incentive story, not a claim that every real market clears instantly.

=== Scene 7 | The Graph and the Algebra

*Claim:* The intersection identifies the same compatible choices we found by counting both sides.

#quote(block: true)[
  *Board and paper:* Combine the spinach curves on one set of axes. Label demand, supply, and the axes with units. Predict the intersection from scene 6. Draw guides from it to the price and quantity axes. Re-mark the shortage at \$3 and the excess at \$6 as horizontal distances between the curves.
]

Now solve for the intersection. At equilibrium, $Q_d=Q_s=Q$, and both curves give the same price:

$ 12 - frac(Q, 5) = 2 + frac(Q, 20) quad ==> quad 10 = frac(Q, 4) quad ==> quad Q^star = 40. $

Substitute into supply, then check with demand:

$ P^star = 2 + frac(40, 20) = 4 quad "and" quad P^star = 12 - frac(40, 5) = 4. $

The starred pair is *40,000 pounds at \$4 per pound*. Label $Q^star$ and $P^star$ on the graph. Away from equilibrium, $Q_d$ and $Q_s$ generally differ; setting them equal is the equilibrium condition, not an identity at every price.

#quote(block: true)[
  *Exercise B3 | Q1:* Solve for the equilibrium quantity and price in the pumpkin-pasty market. Combine the curves on one graph and label the starred pair. Transfer the 5-galleon line from Q2 to this graph and check that its location agrees with the predicted price movement.
]

*Instructor check:* $12-Q/2=2+Q/2$ gives $Q^star=10$ pasties and $P^star=7$ galleons. The 5-galleon line is below equilibrium, consistent with a shortage and upward price pressure.

*Exit check:* At a price above equilibrium, identify quantity demanded, quantity supplied, and quantity exchanged. Who is left out, and what offer could improve their outcome? Require both a graph and one sentence about incentives.

=== Closing | From Equilibrium to B4

We have found how a market price coordinates buyers’ and sellers’ choices. Does that outcome make the most of the possible gains from trade? In B4, use price ceilings and price floors to investigate that question and develop the first welfare theorem: under the competitive model’s assumptions, including no externalities, equilibrium exhausts the gains from trade and maximizes total surplus in this market. Keep the distinction between efficiency and fairness visible.

For the next B4 pass, intersperse graphing and welfare exercises with the price-control intuition. Plaza simulations of price controls are a separate future project.

=== Parked | Outside the Core Sequence

The following material is retained for later preparation. It is not additional required material after scene 7. If class time is tight, keep the graphing and exercise pauses; leave these extensions parked.

==== PPF Tieback

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
