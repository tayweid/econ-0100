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

= Episode B3 | Equilibrium

_Equilibrium: when no one wants to change_

Last week we started with buyers, and asked how much each was willing to buy at a range of prices. This gave us a relationship between prices and quantity demanded on the price quantity graph, a relationship we call demand. We found it to be downward sloping, which is what we call the Law of Demand: people buy more when the price is lower. These ideas work for individuals and for large groups. The only difference is that in large groups we ask many people at each price. In general Demand is not linear but for this class we’ll represent preferences like this with a linear function. Working with a function like this, whether it’s linear or not, makes it very easy for us to ask questions about people’s preferences for things over a whole range of prices, which turns out to~be very convenient.~

Then we asked the same kinds of questions of sellers. Molly has to decide how much spinach to sell.~As price goes up, shes willing to switch her resources away from other uses toward growing spinach, and maybe even expand her farm or factory to produce more. This gave us a positive relationship between price and quantity supplied, Individual Supply, which obeys the Law of Supply: sellers will~sell more when prices go up. Again here we can ask the same questions of any number of sellers and represent the relationship between prices and quantities with a mathematical function. And again while it’s generally not linear in reality, it doesn’t change any core results if we work with linear~supply to keep the math simple.~

But while this is convenient and allows us to answer questions about how much buyers want and sellers will provide, it introduced another question: where do prices come from?

While it may seem like we’ve simply pushed the question of where to live on the PPF one level deeper, having preferences alongside production with prices in between actually allows us to answer~the question.

Here’s a farmer’s market for spinach. We have many buyers with preferences represented by the demand curve and many sellers with costs represented by the supply curve. Before looking at this messy market lets zoom in on two people.~

=== Act 1 | The Basic Exchange

Gary loves fresh spinach for salads and sometimes even in smoothies and would pay up to \$6 for a pound of spinach. Growing that pound costs Molly \$2 who runs a pretty tight operation on her farm. Lets say the price \$4 comes up between them. Would both Gary and Molly agree to exchange at this price?

On Gary’s side, he would hand over \$4, his expenditure, and goes home with the pound of spinach~he~values at \$6, leaving him \$2 of consumer surplus.

On Molly’s side, she receives the \$4 Gary gave her, which covers the \$2 marginal costs it took her to grow the spinach and bring it to the farmers market, leaving her \$2 of producer surplus.~

The price splits the gains from the exchange between the two of them. Both would accept this exchange at \$4.~

#quote(block: true)[
  Exercise to Rewrite:~_At prices of \$5, \$7, and \$1, would Gary buy? Would Molly sell? At \$5, how much does each gain?_

]

More generally, if the price is too high, the the buyer will not accept the exchange. If the price is~too~low the seller will not accept the exchange. A price can facilitate a trade if it calls between the seller’s MC and the buyer’s MB: #mi(`MC < P < MB`).

Between Gary and Molly, any price strictly between \$2 and \$6 makes both better off. At \$2 Molly is indifferent; at \$6 Gary is indifferent. It doesn’t matter much, but to make our job a little easier we’ll count an indifferent person as willing when we count quantities.

When Gary and Molly trade, one pound is sold and the same pound is bought. We’ll call the amount that actually changes hands the quantity exchanged. What price should they choose?

=== Act 2 | The Bidding War

Here we all probably agree that in isolation they should exchange with each other at some price between \$2 and \$6. But they’re not in isolation. Amanda-Grace is another buyer who’s willing to pay up to \$7 for the one pound of spinach Molly has to sell.~At \$4, both buyers are willing to buy from her. Who should get the spinach?

As it stands, Gary has a nice deal with Molly. Amanda-Grace faces a decision. If she accepts that \$4 is the price she’ll have to walk away since Gary has the deal. She pays nothing but also gains nothing: her consumer surplus is \$0. If she instead offers Molly a price higher than what she’s getting from Gary, say \$4.25, Molly would accept this better price and Amanda-Grace would have a \$2.75 consumer surplus.

Amanda-Grace offers the \$4.25, collecting a consumer surplus of \$2.75. Molly accepts, with a producer surplus of \$2.25. Both are happier because Amanda-Grace out-bid Gary. But Gary loses the deal and his \$2 consumer surplus. Overall this is a net win for the trio. Total surplus, the sum of consumer and producer surplus, has gone up by \$1 after the change in price.

But this isn’t the end of the story. Gary, after walking away from his lost deal, realizes he faces a decision. If he simply walks away, he’s gained nothing from this farmers market. If he instead organizes a counter~offer slightly higher than Amanda-Graces offer, say \$4.50, Molly would switch _back_~to selling _him_~spinach, and he would walk out with a consumer surplus of \$1.50. So that’s exactly what he does.

Amanda-Grace counter’s Gary’s counter, and the bidding war begins. As this pattern continues, how~far will they go? Who gets the spinach?

#quote(block: true)[
  _*Let the rest of the bidding run quickly.*_

]

Let’s pause at Amanda-Grace’s offer of \$6.25 for Molly’s pound of spinach. At this price Amanda-Grace gains \$0.75 and Molly gains \$4.25. Gary is willing to pay up to \$6 but no more, so he’s not willing to pay enough to outbid Amanda-Grace. While he likes spinach quite a bit, at this price staying out is better than taking a loss.

With these three people, the price is stable. No one wants to switch. This idea of stability is how we think about equilibrium.~

#quote(block: true)[
  _*Equilibrium*_: _No one wants to switch._

]

=== Act 3 | Multiple Trades

With multiple sellers of spinach a new phenomenon shows up. Andrew is another seller of spinach who isn’t quite as efficient as Molly and is willing to sell a pound of spinach for no less than \$4. Lets keep our lives simple and pretend that the sellers cannot make up the prices they charge, they simply take the prices that the buyers offer, and choose to accept or reject. This doesn’t change our results but does make our lives easier. While Amanda-Grace is over buying spinach from Molly, Gary realizes his two options are to walk away or try to buy from Andrew. Gary is a generous buy and splits their difference with an offer of \$5. Andrew accepts this offer since it’s the best available option for him. Both Gary and Andrew gain \$1 in surplus value from this exchange.

Our quantity exchanged is now up to 2.

Is this stable? Would anyone rather switch?

#quote(block: true)[
  _*Show a more focused deliberation phase, where one buyer is highlighted and given two options for who to trade with, maybe two hypotheticals in two boxes.*_

]

If Amanda-Grace stays with Molly at \$6.25, she would gain \$0.75. If instead she offers Andrew \$5.25, she would gain \$1.75 and Andrew would gain \$0.25 more than his \$1 surplus value with Gary. Here Amanda-Grace has an incentive to switch to this new offer that Andrew would accept.

Just like before, this leaves poor Gary without spinach. But now unlike before, Molly is without a buyer. Gary realizes he can offer Molly the \$5.25 Amanda-Grace offered Andrew. If he sets the price~any lower, Amanda-Grace would try to swoop in again and out-bid him. If he sets it any higher,~he’s missing out.~

So the prices end up being the same. Interestingly, if the pairings’ prices weren’t equal, someone could switch and do better. Stability only happens when prices are equal for everyone.

With two pairings it’s easy to see that there will be incentives to switch whenever prices aren’t equal. But it doesn’t yet tell us which price the larger market will settle on.~

=== Act 4 | Buyers and Sellers

Our four are part of many in the larger farmers market. I’ve put the other buyers on one side and the other sellers on the other. There are many buyers here who want more~than one pound of spinach. We’ve just included them muliple times, once for each of the pounds~of spinach they’d like. And the~sellers who want to sell more than a pound of spinach are also shown multiple times. The number of buyers and sellers isn’t necessarily equal.~

This is all pretty complicated looking. The value of models like we’re developing is to give us a better view of complicated things. To keep things organized, lets keep track of all the buyers in order on the side, forming a demand curve like we’re familiar with, along with an equation for the line through their marginal benefits. Like before, we can use price to ask how much this group wants.~

At a price of … , buyers want ….~

#quote(block: true)[
  _Find a few price and quantity pairs, showing the buyers who would buy with green checks, and~those who wouldn’t with red xs.~_

]

Like we did for buyers, lets keep track of the sellers on the side, forming the supply curve like we’re familiar with, along with the equation for their marginal costs.~

#quote(block: true)[
  _Find a few price and quantity pairs, showing the sellers who would sell with green checks, and~those who wouldn’t with red xs.~_

]

Q. How much is bought? A. #mi(`Q_s`), since that’s all that’s available, meaning many buyers who would want to buy will go without.

{++Six pasties are sold, and the same six are bought. The quantity exchanged is 6, even though the quantity demanded is 14.++}

{++In this market, when willing buyers and sellers can find each other, quantity exchanged is the smaller of quantity demanded and quantity supplied.++}

_Exercise B3 | Q2(a)(b): At 5 galleons on the pumpkin-pasty curves, find the quantity demanded and the quantity supplied. Sketch the two curves separately and mark the quantities._

=== Act 5 | Low and High Prices

// plass:comment
// | Editor. These low- and high-price cases now establish the counts and incentives before the market run. The two passages that name $4 as the place where the gap closes have moved to Act 6; they can explain the observed result after it appears. Keep the curves separate and ask for predictions here.
// /plass:comment

==== A Low Price: \$3

Let’s say spinach sellers, of which Molly and Andrew are included, decide to sell spinach at a price of \$3. We can find the quantity supplied at this price. Which comes out to be 20,000 pounds. But is this how much buyers are willing to buy at this price? The quantity demanded is 45,000 pounds and we find this by plugging in price into the demand curve.

{++How much is exchanged? There are only 20,000 pounds offered for sale, so 20,000 pounds are bought and sold. Buyers want another 25,000 pounds at this price.++}

So it turns out people want more than is available which we call a shortage.

#quote(block: true)[
  ___*Shortage*__: Quantity demanded is greater than quantity supplied._

]

But let’s say in this situation Amanda-Grace, an entrepreneurial buyer, decides to offer Molly a higher price. Let’s say three dollars and twenty-five cents. This is good for Molly since she’s making more and it’s good for Amanda-Grace who is more than willing to pay the higher price if she can receive what she wants.

But it turns out the buyer who was buying from Molly now can’t get any spinach. So, what should they do? They should raise the price.

In this way, whenever there’s a shortage both buyers and sellers have an incentive to raise their prices.

// plass:comment
// | Editor. This restores your original sellers-offer-a-price setup from 01_Notes_Original.md. The later buyers-get-together and break-ranks passages were editor additions, so they are not assumed here. Names and $3/$4/$6 figures follow the current notes. For one concrete deliberation, an unserved Amanda-Grace compares zero with $7 - $3.25 = $3.75 per pound, while Molly compares receipts of $3 and $3.25. The existing narration already counts both participants' incentives.
// /plass:comment

==== A High Price: \$6

Let’s say instead spinach sellers sell at a price of \$6. At this price the quantity supplied is 80,000 pounds. And the quantity demanded is 30,000. So people want less than is available. Which we’ll call an excess.

#quote(block: true)[
  ___*Excess*__: Quantity supplied is greater than quantity demanded._

]

{++How much is exchanged this time? Buyers only want 30,000 pounds, so 30,000 pounds are bought and sold. Sellers are willing to sell another 50,000 pounds at this price, but they don’t have buyers.++}

I want to offer a little side note here: most textbooks call this a surplus but for reasons we’ll get into later, I think this naming convention is less than ideal and can be confusing. So instead of surplus we use excess to describe quantity supplied being greater than quantity demanded. But I just want you to be aware that it’s often called surplus.

So Andrew is sitting around with excess spinach. He can’t sell at 6 per pound. So Andrew, being the entrepreneur farmer, decides to offer a price of \$5.75 to Gary.

Gary was buying spinach from another farmer but is more than willing to buy spinach from Andrew at the lower price. And would even buy a little extra. You can think of the law of demand here. That farmer isn’t happy about losing Gary’s business. So they decide to lower their prices too.

In this way, whenever there’s excess both buyers and sellers have an incentive to lower their prices.

// plass:comment
// | Editor. The excess story is your prose as carried forward in the current notes. Andrew's $5.75 offer gives him $1.75 per pound above MC instead of no sale; Gary pays $0.25 less. Keep one such comparison, then return to the whole market. “Would even buy a little extra” expresses the quantity response; with one unit per bar, an extra unit is another decision/bar, not a second unit hidden inside Gary's bar.
// /plass:comment

#quote(block: true)[
  _Exercise: At \$3 and at \$6, mark quantity demanded, quantity supplied, and quantity exchanged on your spinach graphs. Find the size of the gap and draw an arrow showing which way the price moves._

  _Return to Exercise B3 | Q2(c)(d): At 5 galleons, name the situation, say how large it is, and predict which way the price moves. Who has an incentive to make a different offer?_

]

So prices will rise with a shortage and lower with an excess.

Can there ever be a price that doesn’t change?

=== Act 6 | The Messy Market

Starting with a small set of exchanges, we can continue to expand the number of buyers and sellers making exchanges through the same kinds of undercutting and out-bidding as in the smaller settings. Let’s quickly add more and more people until the market gets much bigger.

#quote(block: true)[
  Show the details of the market buildup. Start with the original four in the middle with the others on the sides, have a new person come in~from the side. A buyer enters by outbiding for an existing seller. A buyer undercuts to a new seller to bring them into the middle. This slowly~expands the market, leaving some on the edges without matches. Do this slowly at first~to~show the decisions, then speeding up so it doesn’t take much time.~

]

There are a lot of decisions going on at once now. We don’t need to follow every one of them. They’re the same kinds of decisions we just looked at with a few people.~Each buyer and seller will accept a better offer if it’s available. This process continues, until no one wants to change, leaving us with a~price for all the exchanges.~

==== The Price That Doesn’t Change

{++Now let’s read the price and quantity where the market settled from the two curves on the side.++}

_*Supply and demand separate to start. Stack them vertically to show the quantities are equal.*_

Yes. What if quantity demanded was equal to quantity supplied? Here no one has an incentive to change their prices or quantities. If a seller raised their price, they would lose all their business.

If they lower their price, they would make less than they could. If a buyer raised their price, they would be paying more than they needed to. And if the buyer lowered their price no seller would sell to them. In this way incentives push the price to the point where quantity supplied is equal to quantity demanded.

#quote(block: true)[
  ___*Equilibrium*__: The price and quantity at which quantity supplied equals quantity demanded — where no one wants to change._

]

{++At \$4, quantity demanded, quantity supplied, and quantity exchanged are all 40,000 pounds.++}

{++We can now look back at our two trial prices and see where the adjustment leads.++}

{++As the price rises, quantity demanded falls and quantity supplied rises. The gap closes. At \$4, buyers want 40,000 pounds and sellers are willing to sell 40,000 pounds.++}

{++As the price falls, quantity supplied falls and quantity demanded rises. Again, the gap closes at \$4.++}

The exact pairings between the buyers and sellers isn’t particularly important here. We could swap~any two pairs and no one would be any less well off. So lets arrange all the buyers in order.~

This makes it easier for us to see the demand curve and that no more buyers are interested in buying at this price. Buyers are on the sidelines not because they couldn’t find a seller to buy from, but because they have other better uses of their money at this price.

We can also arrange sellers in order, making it clear that the sellers on the sidelines aren’t there for lack of buyers. They simply aren’t willing to divert their resources away from their other uses to growing spinach at this price.~

{++This doesn’t mean everyone buys or sells. The buyers who are left out aren’t willing to pay \$4, and the sellers who are left out aren’t willing to sell for \$4. There is no willing buyer left without a seller, or willing seller left without a buyer.++}

_*{++Ask what would happen a little above \$4, then a little below it. Use the graphs to show which side is left out and why the price moves back.++}*_

Okay, so we’ve found where prices come from. And we’ve found an equilibrium concept that’s stable.

At this equilibrium price and quantity no buyer and no seller wants to change the price they’re offering and the quantity they’re either supplying or demanding from the market. So we call this equilibrium stable.

// plass:comment
// | Editor. The shortage and excess cases now lead to the open question before the market runs. This section answers it afterward, using the observed price and the separate curves. The existing headings and definitions are unmarked; moving your words or renumbering sections is not new writing. The remaining {++ ++} spans identify wording added by the editor. The graph tests make “stable” visible rather than only announcing it. The no-better-offer argument assumes the competitive setting where alternative trading partners are available; it is stronger than what scene 2's lone seller establishes.
// /plass:comment

=== Act 7 | The Graph and the Algebra

We typically combine supply and demand on one graph, so let’s do that here.

#quote(block: true)[
  _{++Board and paper: Put the spinach demand and supply curves on the same axes. Label the intersection using what we found at \$4. Mark the horizontal gap at \$3 and at \$6. How does each gap compare with the one on your separate graphs?++}_

]

Here we’re going to use algebra to build a model using both supply and demand to arrive at the prices that coordinate sellers’ choices of quantity supplied and buyers’ choices of quantity demanded.

The supply curve for spinach was price is equal to two plus one over twenty quantity and the demand curve for spinach was price is equal to twelve minus one over five quantity. There’s one price that allows quantity supplied to equal quantity demanded. And that’s where they intersect.

{++At equilibrium, quantity demanded equals quantity supplied, so we can call both of them Q. Away from equilibrium they can be different quantities, even though buyers and sellers face the same price.++}

Let’s first solve for the equilibrium quantity then solve for equilibrium price. We set the supply curve equal to the demand curve. Then we solve for quantity which gives us 40. We then take this and plug it into the supply curve.

And solve for price which comes out to be \$4. It would be equivalent if you plugged the quantity into the demand curve and solved for price that way but plugging it into the supply curve is usually easier.

We denote the equilibrium price and quantity with a star.

Plot it on the graph.

// plass:comment
// | Editor. Proposed clarification above supplies the reason Qd and Qs become one Q. Board working: Qd = Qs = Q; 12 - Q/5 = 2 + Q/20; 10 = Q/4; Q* = 40; P* = 2 + 40/20 = 4. Check with demand: 12 - 40/5 = 4. Label the result 40,000 pounds at $4 per pound. These reference calculations are in the comment rather than a separate answer section.
// /plass:comment

#quote(block: true)[
  _{++Pause for Exercise B3 | Q1: Solve for the equilibrium quantity and price in the pumpkin-pasty market. Plot both curves and the starred pair. Add the 5-galleon line from Q2 and check that the graph agrees with your earlier answers.++}_

]

// plass:comment
// | Editor. Exercise check: 12 - Q/2 = 2 + Q/2 gives Q* = 10 pasties and P* = 7 galleons. At 5 galleons the graph gives Qs = 6, Qd = 14, and the shortage of 8. The teaching order is Q2(a)(b), Q2(c)(d), then Q1; the printed sheet remains as it is. Students first read each curve, then compare the two quantities, then solve for the common quantity.
// /plass:comment

=== Closing

But at this point you might be wondering: Ok, this is nice. Markets pick a price, which gives us a quantity, and a point on the PPF. But is the market even good? Like, do markets give us a coordination device that makes us as well off as possible?

The answer is complicated as we’ll see. But what I’m going to show you is a simple answer to a simpler question.

What would happen to our market if the government decided the price should be low?

// plass:comment
// | Editor. These are your opening lines from Lecture 08 (B4), moved here as a candidate closing question. They connect the incentives in B3 to the price-control route into welfare that you described on September 26. For the eventual B4 notes, retain the next paragraph's distinction: buyers would normally offer more, but the legal restriction prevents it, so the shortage persists. Market-wide welfare, DWL, and the first welfare theorem stay with B4.
// /plass:comment

=== Parked

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
