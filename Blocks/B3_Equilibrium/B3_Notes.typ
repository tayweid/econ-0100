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
// | Editor. September 29. This is a new working file; the existing notes, outline, archive, exercises, and animations are unchanged. The seven scenes follow B3_Outline.typ. Your latest request adds a brief view of the market growing after Multiple Trades, within scene 3, before we turn to the full buyer and seller views.
// | Editor. Unmarked prose and directions come from your existing notes or your recorded planning remarks, with light punctuation cleanup. New wording, new headings, and inherited passages still marked as drafts in the source are enclosed in {++ ++}. An inherited draft is not treated as approved merely because it appeared in B3_Notes_new.typ. Comments beginning Editor. explain placement, provenance, and unresolved choices; they do not appear in the PDF.
// | Editor. Main references: B3_Outline.typ; B3_Notes_new.typ; 01_Notes_scenes_2026-09-22.md; _archive/Planning_Chat.typ; _archive/01_Notes_pre_edit_2026-09-16.md; _archive/01_Notes_Original.md; _archive/01_Notes_pre_scenes_2026-09-22.md; _archive/Lecture 08 (B4)_pre_edit_2026-09-16.md; _archive/Lecture 11 (B7).md. The archived critiques informed the proposed clarifications, but are not sources of your wording.
// | Editor. Your September 26 distinction governs the scope: B3 introduces incentives, with individual PS and CS as measures of incentives; B4 develops market welfare through price controls. These are preparation notes, not a script. No detailed storyboard or beat IDs are included here.
// | Editor. Reference numbers retained from the current outline and notes: small cast Gary MB $6, Amanda-Grace MB $7, Molly MC $2, Andrew MC $4. Large market P = 12 - Qd/5 and P = 2 + Qs/20; Q in thousands of pounds, P in dollars per pound. At $3: Qd 45, Qs 20; at $4: 40 and 40; at $6: 30 and 80. Earlier dictation uses superseded numbers. The large-market unit change is proposed explicitly in scene 4.
// /plass:comment

=== Opener

{++Last week we started with buyers:++} we found that individuals’ preferences about how much spinach to buy obey the law of demand giving us an individual demand curve. Then we took many buyers and found the spinach demand curve. Representing this with algebra allowed us to find the quantity demanded at a whole range of prices.

{++Then we turned to the other side of the market, sellers: we allowed++} Molly to make her decision about where to live on the frontier which gave us her individual supply curve, which obeys the law of supply. Then we took all the many farmers growing spinach and found the spinach supply curve. Representing this with algebra allowed us to find the quantity supplied at a whole range of prices.

This answered part of the question about where on the frontier to live but introduced another free variable left to float around: Price. {++In some sense we simply pushed the question of where to live on the PPF one level deeper into prices. Now we put the two together and ask whether there’s a price at which those quantities agree.++} So this brings us to the question. What happens to prices when we have supply and demand in a market for spinach?

To do this, let’s set up a farmer’s market for spinach and use two graphs. One for supply and one for demand.

// plass:comment
// | Editor. The opener's marked transitions were proposals in 01_Notes_Original.md. The demand-then-supply order matches the present course. The rest is your existing recap. This leaves the question of the price open before the first exchange.
// /plass:comment

=== {++1 | The Basic Exchange++}

{++Let’s start with just two people. Gary would pay up to \$6 for a pound of spinach. Growing that pound costs Molly \$2. Now suppose a price of \$4 comes up between them. Would they both say yes? Gary pays less than the spinach is worth to him. Molly receives more than it cost her. So the trade happens.++}

{++Let’s zoom way in on this one exchange. Gary hands over \$4 — his expenditure. Against his marginal benefit of \$6, that leaves him \$2 of consumer surplus. Molly receives the same \$4 as revenue. Above her cost of \$2, that leaves her \$2 of producer surplus. The price is doing the splitting: it divides the gains from this trade between the two of them.++}

// plass:comment
// | Editor. Those two paragraphs are inherited drafts, retained as proposals. They supply the specific example for your September 22 basic-exchange direction. Keep this as the incentive calculation for one exchange; the market-wide areas belong in B4.
// /plass:comment

There is a price that can facilitate this trade if it can be between MC and MB: #mi(`MC < P < MB`).

_*Show a few other prices that don’t work and some that do.*_

#quote(block: true)[
  _{++Board and paper: At prices of \$5, \$7, and \$1, would Gary buy? Would Molly sell? At \$5, how much does each gain?++}_

]

{++Any price strictly between \$2 and \$6 makes both better off. At \$2 Molly is indifferent; at \$6 Gary is indifferent. We’ll count an indifferent person as willing when we count quantities.++}

{++When Gary and Molly trade, one pound is sold and the same pound is bought. We’ll call the amount that actually changes hands the quantity exchanged.++}

_*And then ask “What price should they choose?”*_

// plass:comment
// | Editor. Quantity exchanged is proposed here as a name for the familiar transaction, without a formula yet. Scene 2 distinguishes wanting to buy from actually buying; scene 5 returns to the term when both market quantities are available. Practice check: $5 works for both, with gains of $1 and $3; $7 is too high for Gary, $1 too low for Molly.
// /plass:comment

=== {++2 | The Bidding War++}

{++Now let’s add another buyer. Two buyers want spinach and Molly only has one pound to sell. Amanda-Grace would pay up to \$7. At \$4, both buyers are willing, but only one can buy.++}

Who should get the spinach? Gary is able to pay Molly and had a nice deal if Amanda-Grace weren’t there.

{++Amanda-Grace could stay out and gain nothing. Or she could offer Molly \$4.75 and gain \$2.25. Molly would receive \$0.75 more than she gets from Gary. Would they both prefer that trade?++}

{++Gary can answer with \$5 and still gain \$1. But how far will he go?++}

_*{++Ask who will get the spinach, then let the rest of the bidding run quickly.++}*_

{++At \$6.25, Amanda-Grace gains \$0.75. Gary would have to pay more than the spinach is worth to him to outbid her. He still likes spinach, but staying out is better than taking a loss.++}

A price is not stable unless no one has an incentive to switch.

This stability is equilibrium. No one wants to switch.

#quote(block: true)[
  _*Equilibrium*_: _No one wants to switch._

]

// plass:comment
// | Editor. Your definition and the question about Gary are from Planning_Chat.typ, September 22. The proposed arithmetic gives both sides of one bid, using the current cast. This introduces the idea of equilibrium on the small stage; it does not establish a unique competitive price or show that Molly could never change her ask. Scene 6 supplies the full market-clearing and stability argument.
// /plass:comment

=== {++3 | Multiple Trades++}

{++Now add Andrew, whose marginal cost is \$4. Suppose Gary buys from him at \$4.25, while Amanda-Grace is still buying from Molly at \$6.25. Each trade works for the two people involved. But would anyone rather switch?++}

_*Show a more focused deliberation phase, where one buyer is highlighted and given two options for who to trade with, maybe two hypotheticals in two boxes.*_

{++Amanda-Grace could stay with Molly at \$6.25 and gain \$0.75. Or she could offer Andrew \$4.50 and gain \$2.50. Andrew would gain \$0.50 instead of \$0.25. Again, the new offer works for both of them.++}

{++But that leaves Gary without spinach and Molly without a buyer. The other people in the market have options too.++}

If the pairings’ prices weren’t equal, someone could switch and do better.

Prices must be equal for prices to be stable.

{++Two trades at \$5.50 give us an example of a common price. The small example tells us why different prices create an incentive to switch. It doesn’t yet tell us which common price the whole market will settle on.++}

// plass:comment
// | Editor. The direction and the two equal-price sentences are yours. The worked comparison is proposed to fill the gap you identified in scene 3. It assumes identical spinach and people able to find and switch to better offers. There is no need to narrate every subsequent bid or cut.
// /plass:comment

==== {++The Market Builds Up++}

_*Show the details of the market buildup, showing its complexity on screen, the messiness of the market, but not really dwelling on it or taking real class time.*_

_*Here’s the small things with an exchange, bidding war, multiple options, then let’s quickly add more and more people until we get really big.*_

Each buyer and seller will accept a better offer if it’s available. This process continues, until no one wants to change.

{++There are a lot of decisions going on at once now. We don’t need to follow every one of them. They’re the same kinds of decisions we just looked at with a few people.++}

// plass:comment
// | Editor. The two directions use your September 29 request, with punctuation cleanup. The two sentences about accepting a better offer come from Planning_Chat.typ, September 16. This is a brief transition within scene 3, so the seven-scene structure remains intact. Your current direction supersedes the older no-growth decision for this new file. Keep the visual complexity, without returning to a stop for each entrant.
// | Editor. The population grows during this transition. Once we reach scenes 4–6, hold the population fixed while testing prices; otherwise changes in who is present and adjustment within one market are easily conflated. The later market-changes block can develop entry as a shifter.
// /plass:comment

=== {++4 | Buyers++}

_*Arrange buyers in order and ask who would buy at a range of prices. Put a green check over them, and a green circle under them to indicate a trade. Then show the graph of the demand curve like we already do and an equation for demand.*_

We just have one person per bar, and if someone wants more than one, we just have them show up twice.

_*This should be a large enough number that the equation makes sense as a good approximation.*_

{++In the large market, we’re measuring quantity in thousands of pounds. Each displayed unit now represents a 1,000-pound lot, and prices, marginal benefits, and marginal costs are still in dollars per pound.++}

Prices must be equal for everyone. At this price, this is how many people would buy.

_*Then show that some aren’t happy or willing to pay that much, but still want it. Show the offers, which are at the price for those who would pay, and the MB for those who wouldn’t.*_

{++A buyer is willing to buy when their marginal benefit is at least the price. Their marginal benefit is the most they would offer. But being willing doesn’t yet mean they get spinach. We still need to count the sellers.++}

// plass:comment
// | Editor. The directions, common-price lines, and one-person-per-bar sentence are yours, recorded in Planning_Chat.typ. The unit transition is proposed wording for the chosen large-market scale. Keep the check/circle distinction from your direction: a check means willing; a circle means an actual exchange. This buyer-only count cannot yet guarantee circles for everyone who is willing.
// /plass:comment

{++The demand curve for this market is++} #mi(`P = 12 - Q_d/5`).

#quote(block: true)[
  _{++Board and paper: Draw the demand curve, with price on the vertical axis and quantity on the horizontal axis. Label the units and intercepts. At \$6, find the quantity demanded and mark it on the graph. Then do the same at \$3.++}_

]

// plass:comment
// | Editor. Practice check: price intercept $12; quantity intercept 60 thousand pounds. At $6, Qd = 30; at $3, Qd = 45. These are readings along the same demand curve. Keep this graph for the comparison with sellers and the eventual combined graph.
// /plass:comment

=== {++5 | Sellers++}

On the seller side, in a separate plaza, it’s a similar setup. The single price, it works for most, but some sellers can’t price that low. Their asks are their MC.

{++A seller is willing to sell when the price is at least their marginal cost. Their marginal cost is the lowest price they would accept. And being willing to sell doesn’t yet mean they have a buyer.++}

{++The supply curve for this market is++} #mi(`P = 2 + Q_s/20`).

#quote(block: true)[
  _{++Board and paper: Draw supply on a separate graph, using the same axis scales as demand. At \$3, find the quantity supplied and mark it on the graph. Repeat at \$6.++}_

]

// plass:comment
// | Editor. Practice check: price intercept $2; at $3, Qs = 20 thousand pounds; at $6, Qs = 80. The line describes nonnegative supply from $2 upward; below $2, supply is zero. The separate graphs follow your requested order and keep attention on counting each side at the same price.
// /plass:comment

#quote(block: true)[
  _{++Pause for Exercise B3 | Q2(a)(b): At 5 galleons on the pumpkin-pasty curves, find the quantity demanded and the quantity supplied. Sketch the two curves separately and mark the quantities.++}_

]

==== {++Quantity Exchanged++}

{++Now we have both sides. At 5 galleons, buyers want 14 pasties and sellers are willing to sell 6.++}

Q. In this situation, how much is sold? A. #mi(`Q_s`).

Q. How much is bought? A. #mi(`Q_s`), since that’s all that’s available, meaning many buyers who would want to buy will go without.

{++Six pasties are sold, and the same six are bought. The quantity exchanged is 6, even though the quantity demanded is 14.++}

{++In this market, when willing buyers and sellers can find each other, quantity exchanged is the smaller of quantity demanded and quantity supplied.++}

// plass:comment
// | Editor. The two Q/A lines are moved from your old Lecture 08 (B4), where they concern a low price. They apply to the pasty exercise here without changing the reasoning. The framing and general rule are proposed. This develops quantity exchanged before scene 6, as you suggested, and gives the Q2 calculations an immediate meaning. Let students answer before the answers above are discussed. Leave the name and size of the shortage for Q2(c)(d) after the next scene's explanation.
// /plass:comment

=== {++6 | Finding Equilibrium++}

_*Supply and demand separate to start. Stack them vertically to show the quantities are equal.*_

==== {++A Low Price: \$3++}

Let’s say spinach sellers, of which Molly and Andrew are included, decide to sell spinach at a price of \$3. We can find the quantity supplied at this price. Which comes out to be 20,000 pounds. But is this how much buyers are willing to buy at this price? The quantity demanded is 45,000 pounds and we find this by plugging in price into the demand curve.

{++How much is exchanged? There are only 20,000 pounds offered for sale, so 20,000 pounds are bought and sold. Buyers want another 25,000 pounds at this price.++}

So it turns out people want more than is available which we call a shortage.

#quote(block: true)[
  _{++__*Shortage*__: Quantity demanded is greater than quantity supplied.++}_

]

But let’s say in this situation Amanda-Grace, an entrepreneurial buyer, decides to offer Molly a higher price. Let’s say three dollars and twenty-five cents. This is good for Molly since she’s making more and it’s good for Amanda-Grace who is more than willing to pay the higher price if she can receive what she wants.

But it turns out the buyer who was buying from Molly now can’t get any spinach. So, what should they do? They should raise the price.

In this way, whenever there’s a shortage both buyers and sellers have an incentive to raise their prices.

{++As the price rises, quantity demanded falls and quantity supplied rises. The gap closes. At \$4, buyers want 40,000 pounds and sellers are willing to sell 40,000 pounds.++}

// plass:comment
// | Editor. This restores your original sellers-offer-a-price setup from 01_Notes_Original.md. The later buyers-get-together and break-ranks passages were editor additions, so they are not assumed here. Names and $3/$4/$6 figures follow the current notes. For one concrete deliberation, an unserved Amanda-Grace compares zero with $7 - $3.25 = $3.75 per pound, while Molly compares receipts of $3 and $3.25. The existing narration already counts both participants' incentives.
// /plass:comment

==== {++A High Price: \$6++}

Let’s say instead spinach sellers sell at a price of \$6. At this price the quantity supplied is 80,000 pounds. And the quantity demanded is 30,000. So people want less than is available. Which we’ll call an excess.

#quote(block: true)[
  _{++__*Excess*__: Quantity supplied is greater than quantity demanded.++}_

]

{++How much is exchanged this time? Buyers only want 30,000 pounds, so 30,000 pounds are bought and sold. Sellers are willing to sell another 50,000 pounds at this price, but they don’t have buyers.++}

I want to offer a little side note here: most textbooks call this a surplus but for reasons we’ll get into later, I think this naming convention is less than ideal and can be confusing. So instead of surplus we use excess to describe quantity supplied being greater than quantity demanded. But I just want you to be aware that it’s often called surplus.

So Andrew is sitting around with excess spinach. He can’t sell at 6 per pound. So Andrew, being the entrepreneur farmer, decides to offer a price of \$5.75 to Gary.

Gary was buying spinach from another farmer but is more than willing to buy spinach from Andrew at the lower price. And would even buy a little extra. You can think of the law of demand here. That farmer isn’t happy about losing Gary’s business. So they decide to lower their prices too.

In this way, whenever there’s excess both buyers and sellers have an incentive to lower their prices.

{++As the price falls, quantity supplied falls and quantity demanded rises. Again, the gap closes at \$4.++}

// plass:comment
// | Editor. The excess story is your prose as carried forward in the current notes. Andrew's $5.75 offer gives him $1.75 per pound above MC instead of no sale; Gary pays $0.25 less. Keep one such comparison, then return to the whole market. “Would even buy a little extra” expresses the quantity response; with one unit per bar, an extra unit is another decision/bar, not a second unit hidden inside Gary's bar.
// /plass:comment

#quote(block: true)[
  _{++Board and paper: At \$3 and at \$6, mark quantity demanded, quantity supplied, and quantity exchanged on your spinach graphs. Find the size of the gap and draw an arrow showing which way the price moves.++}_

  _{++Return to Exercise B3 | Q2(c)(d): At 5 galleons, name the situation, say how large it is, and predict which way the price moves. Who has an incentive to make a different offer?++}_

]

// plass:comment
// | Editor. Exercise check: Qd = 14, Qs = 6, quantity exchanged = 6; shortage = 8 pasties; upward price pressure. This finishes the question begun in scene 5. The existing exercise sheet is unchanged; graphing and the quantity-exchanged question are proposed class prompts in these notes.
// /plass:comment

==== {++The Price That Doesn’t Change++}

So prices will rise with a shortage and lower with an excess.

Can there ever be a price that doesn’t change? Yes. What if quantity demanded was equal to quantity supplied? Here no one has an incentive to change their prices or quantities. If a seller raised their price, they would lose all their business.

If they lower their price, they would make less than they could. If a buyer raised their price, they would be paying more than they needed to. And if the buyer lowered their price no seller would sell to them. In this way incentives push the price to the point where quantity supplied is equal to quantity demanded.

#quote(block: true)[
  _{++__*Equilibrium*__: The price and quantity at which quantity supplied equals quantity demanded — where no one wants to change.++}_

]

{++At \$4, quantity demanded, quantity supplied, and quantity exchanged are all 40,000 pounds.++}

{++This doesn’t mean everyone buys or sells. The buyers who are left out aren’t willing to pay \$4, and the sellers who are left out aren’t willing to sell for \$4. There is no willing buyer left without a seller, or willing seller left without a buyer.++}

_*{++Ask what would happen a little above \$4, then a little below it. Use the graphs to show which side is left out and why the price moves back.++}*_

Okay, so we’ve found where prices come from. And we’ve found an equilibrium concept that’s stable.

At this equilibrium price and quantity no buyer and no seller wants to change the price they’re offering and the quantity they’re either supplying or demanding from the market. So we call this equilibrium stable.

// plass:comment
// | Editor. Your original shortage → excess → “Can there ever be a price that doesn’t change?” sequence is restored here. The formal definition was a marked proposal in the older scene draft, so its wording remains proposed. The graph tests make “stable” visible rather than only announcing it. The no-better-offer argument assumes the competitive setting where alternative trading partners are available; it is stronger than what scene 2's lone seller establishes.
// /plass:comment

=== {++7 | The Graph and the Algebra++}

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

// plass:comment
// | Editor. The PPF tieback and pit-market material below are retained from B3_Notes_new.typ and the archived Lecture 11 (B7). They remain outside the seven-scene class sequence. Your archived predict-the-equilibrium-before-running-the-market idea may be useful for later practice, but it need not lengthen this lesson.
// /plass:comment

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
