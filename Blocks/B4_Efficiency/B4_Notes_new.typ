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

== Episode B4 | First Welfare Theorem

_Under some conditions, nothing can do better than markets._

// plass:comment
// | Storyboard. Each step opens with its beats, one line each, as built on Sep 23 in B4_Animation.py, scene B4.
// | The animation runs the floor before the ceiling. These notes run the ceiling first, so steps 2 and 3 are in the other order on screen.
// | The animation opens with the B3 review, beats 0.a to 1.i.algebra. Those are listed in the B3 notes.
// | Camera, layout, and color detail: _archive/B4_Storyboard_2026-09-23.md.
// /plass:comment

=== 1 | One Exchange, Then a Low Price

// plass:comment
// | 2.a · Title: The gains from trade. The large graph at $4 and 40. CS and PS labeled inside their regions, one bar per lot.
// | 2.b.parts · The first lot's bar comes forward, CS stacked on PS with the price between them.
// | 2.b.sum · A purple line spans both parts. Bottom: Total surplus = PS + CS.
// | 2.b · The bar returns and every lot turns purple. Label: Total surplus.
// | 4.a · Title: A price ceiling. The price guide at $3 ends at the supply curve. Quantity 20.
// | In the B3 review, beats 1.d to 1.e.exchanged show the same price with the counts: 45 willing buyers, 20 willing sellers, 20 exchanged.
// /plass:comment

But at this point you might be wondering: Ok, this is nice. Markets pick a price, which gives us a quantity, and a point on the PPF. But is the market even good? Like, do markets give us a coordination device that makes us as well off as possible?

The answer is complicated as we’ll see. But what I’m going to show you is a simple answer to a simpler question.

We’re now equipped with consumer and producer surplus to let us evaluate how good the market is for buyers and sellers.

_*Highlight consumer surplus and producer surplus.*_

Consumer surplus is the value buyers didn’t need to pay.

_*Highlight*_

Expenditure in green is how much buyers paid to sellers.

_*Highlight*_

And the seller’s producer surplus was the value sellers didn’t have to pay from buyers’ expenditure.

_*Highlight*_

Surplus Value is the sum of producer and consumer surplus, essentially measuring the goodness of the market by capturing the extras not needed to be paid.

_*Highlight*_

Here is where you can think back to our conversation on specialization and trade.

We’re benefitting both sides, and by the amount represented by surplus, sometimes called welfare.

What if I pay 5, but I’m willing to pay 7.

This is nice for me.

_*Do something like hearts floating up.*_

I would have been willing to pay 2 extra dollars, but instead, I don’t need to spend those dollars, and I can keep that money in my pocket.

What if I sell for #mi(`7`), but I’m willing to sell for #mi(`5`).

This is nice for me as a seller.

I would have been willing to charge #mi(`2`) less dollars, but instead, I can keep those extra dollars.

But lets say I walk into the store to buy a chocolate bar, I’m willing to pay \$2 but the seller is selling for \$1. This is good for me right? I don’t need to pay what I would be willing to, so I’ve saved a dollar. This dollar, the difference between what I would be willing to pay and what I actually have to pay, is what we call Consumer Surplus. And we represent it on the graph as:

+ The area under the demand curve
+ Above the price
+ And at every quantity that’s exchanged

And for sellers we have a similar notion, called Producer Surplus. This is just the difference between what a seller is willing to sell for and what they actually sell for. And we represent it on the graph in a similar way:

+ The area above the supply curve
+ Below the price
+ And at every quantity that’s exchanged

To show this, I’m going to ask you a simple question, related to the previous class.

What would happen to our market if the government decided the price should be low?

Maybe there’s a health equity concern with spinach. We’d like people to not have to pay too much to get healthy food.

When we impose a price control, who benefits and who loses?

And we’ll use our notions of consumer surplus, producer surplus, and deadweight loss to answer this question.

What about a binding price ceiling, a maximum legal price?

Here incentives push the price toward equilibrium, but are constrained, since the equilibrium doesn’t lie on the legal interval.

So prices get as close as possible: the price ceiling.

Q. In this situation, how much is sold? A. #mi(`Q_S`).

Q. How much is bought? A. #mi(`Q_S`), since that’s all that’s available, meaning many Buyers who would want to buy will go without.

We can start by finding the CS for the buyers with the highest willingness to pay.

This is a small assumption that those who are most willing will be the ones who make it happen.

What’s the welfare in this market?

=== 2 | Incentives in the Price Control, Then Equilibrium

// plass:comment
// | 4.b · Lots 21 to 39 turn grey. Lost trades marked from 20 to 40 on the quantity axis. Label: DWL.
// | 4.c.select · Lot 25 is picked out: MB $7, MC $3.25.
// | 4.c · Two people, with the $3 ceiling on a price axis. Legal prices 0 to 3 in green, prices both would accept $3.25 to $7 in purple, $4 marked. Bottom: Both gain at $4; that price is illegal.
// | 6.exercise_ceiling · Exercise B4 Q1 card.
// | 5.a · Title: The surplus from this trade. The same pair trades at $4. Surplus gained $3,750.
// | 5.b · Title: The market without controls allows all beneficial trades. Every lot through 40 is purple.
// | Not built: the price released from $3 back to $4 with the areas changing.
// /plass:comment

At this price, Buyers want to buy a great deal and Sellers wish to sell only a little. This is a shortage. Typically in shortages, Buyers would be able to jump the line with a slightly higher price, paying a little more, but being happy to at least get their spinach. Sellers would obviously accept the higher prices. However, here with the legal price being low, Buyers cannot jump the line with a higher price, meaning the shortage will persist despite the incentives to raise the price.

Consumer surplus is the area below the demand curve, above the price, and inside the quantity exchanged.

Producer surplus is the area below the price, above the supply curve, and inside the quantity exchanged.

*\[draft\]* Here you might expect consumer surplus to grow — the price is lower. But count what was lost. The quantity collapsed to 20, and the trades that disappeared took their surplus with them: consumer surplus falls from \$156,000 at equilibrium to \$138,000. The ceiling hurt even the buyers it was meant to help.

Producer surplus is smaller due to both the lower price and the smaller quantity exchanged.

Have we lost welfare? Yes! This loss in welfare is what we call *Deadweight Loss*. For now, we’re going to define *DWL* as the loss in *Welfare* compared to its maximum.

And deadweight loss is the area between the supply and demand curves above the lost quantity.

#quote(block: true)[
  _Pause for Exercise B4 | Q1: the pumpkin-pasty market gets a price ceiling of 5 galleons. You found Qd = 14 and Qs = 6 at that price on the B3 sheet — now find the quantity exchanged, consumer surplus, producer surplus, and deadweight loss, and shade all three on your plot._

]

=== 3 | A High Price

// plass:comment
// | 3.a · Title: A price floor. The price guide at $6 ends at the demand curve. Quantity 30.
// | 3.b · Lots 31 to 39 turn grey. Lost trades marked from 30 to 40. Label: DWL.
// | 3.c.select · Lot 35 is picked out: MB $5, MC $3.75.
// | 3.c · Two people, with the $6 floor. Legal prices from 6 up in green, prices both would accept $3.75 to $5 in purple. Bottom: Both gain at $4; that price is illegal.
// | 6.exercise_floor · Exercise B4 Q2 card, shown last in the animation.
// /plass:comment

Q. Now what if the government wants to protect sellers, and mandated a high price?

And let’s impose a price floor.

This is a legal minimum price.

If we impose the price floor below equilibrium the control is not binding.

If we impose it above equilibrium, the incentives pushing the market toward equilibrium are impeded, and the price gets as close as possible to equilibrium: the binding price floor.

Is this good for those exchanging in the market?

Well it’s kind of good for sellers. But it’s very bad for Buyers, which means TS goes down.

Here we can see that higher price and lower quantity exchanged both decrease the consumer surplus, while producer surplus goes up *\[draft\]* More than doubles, actually: from \$39,000 to \$96,750. The sellers still selling collect \$6 a pound on spinach that cost far less to grow.

This policy though cuts off a region of total surplus, since it raises the price, which causes an excess and a reduction in the quantity exchanged.

*\[draft\]* And here’s the reason I promised in the last episode: from now on, surplus means value created — consumer and producer surplus — which is why we say excess, not surplus, when quantity supplied outruns quantity demanded.

The interpretation here is not that price controls like the minimum wage and rent control are bad.

We have many policy agendas, and we can evaluate them based on our wants and needs as a society.

But when we evaluate how well a policy is doing, welfare analysis of this type gives us a toolset to effectively evaluate the welfare implications.

#quote(block: true)[
  _Pause for Exercise B4 | Q2: the pasty market gets a price floor of 9 galleons instead. Find the quantity exchanged, producer surplus, and deadweight loss — and decide whether a floor of 6 galleons would change anything._

]

=== 4 | Force a Few More Trades

// plass:comment
// | 5.c · Lot 40 sits at the crossing. MB and MC are both $4, so its gain is zero.
// | 5.d · Title: Trades beyond equilibrium. Lots 41 to 50 appear as ten red bars. Bottom: For these trades, MC exceeds MB.
// | 5.d.negative_ts · Lot 50 outlined in yellow. Label: Negative TS.
// | 5.d.detail · Lot 50 up close: MB $2 and MC $4.50 side by side, the gap labeled Negative TS. Quantity: 1,000 lb.
// /plass:comment

_*Then force a few more people to exchange and see what happens to TS.*_

Imagine you’re a benevolent overlord trying to maximize social welfare. And you get to decide how much is bought and sold. We do this sometimes with government policies by regulating which prices are legal.

_*Slide quantity back and forth.*_

In economics this imaginary person, called the social planner, can make thinking about problems more simple.

And we found that both buyers and sellers have incentives to move price toward equilibrium, where quantity demanded equals quantity supplied at the market price.

_*Start with price far from equilibrium, and let it oscillate toward equilibrium.*_

But we can see that PS and CS are in some sense at odds with each other.

When price decreases, CS increases, but PS decreases.

When price increases, CS decreases, but PS increases.

Visually it’s relatively easy here to see that surplus at any price is the difference between willingness to pay and willingness to sell for every unit above the quantity exchanged.

But how should the social planner maximize total surplus? Let’s give you the social planner control over price.

From here, you probably can see that our job as the social planner is to minimize deadweight loss.

So how should the social planner set prices?

Taken as a whole, you as the social planner can conclude that maximizing welfare involves setting the price at equilibrium, since any increase or decrease lowers surplus.

=== 5 | First Welfare Theorem

// plass:comment
// | 5.e · The ten extra lots leave. Title: The First Welfare Theorem, stated with its conditions.
// /plass:comment

This type of logic applies to any price that’s not equilibrium, which leaves us with a big result.

_*First Welfare Theorem*_. Competitive markets with no externalities maximize welfare.

This is the thing you often hear free market economists talk about on TV. Let the market do its thing because it will maximize welfare. But remember two things about this result.

First, markets must be competitive. That means there must be many Buyers buying identical goods from many Sellers. In Part E, we’re going to look at what happens when markets are not competitive.

Second, markets must not have externalities. This means that the things we’re buying and selling do not impact those not engaging in the exchanges. When I drive my Prius, even though it’s an efficient vehicle, it’s releasing carbon dioxide, which contributes to climate change. This is a negative externality: a cost that’s not carried by the person driving the car. I also plant flowers in my front garden. As my neighbors walk by, they get a little moment of happiness because of my actions. This is a positive externality: a benefit that’s going to someone not involved with the planting of the flowers. In Part C we’re going to look at what happens when markets have externalities.

Keeping these caveats in mind, I want to focus for a second on the remarkable result that is the First Welfare Theorem. What this theorem tells us, is that in competitive markets with no externalities, the best thing for society as a whole happens when we let Buyers follow their individual incentives, sometimes jumping the line, and when we let Sellers follow their individual incentives, sometimes trying to undercut other sellers. In this kind of environment, it turns out that everyone following their individual incentives, in a distributed way coordinates those involved toward something that can be thought of as socially optimal! It’s remarkable that no one need plan it out.

This is the idea that made Adam Smith famous. By the end of this class, you’re going to be able to recognize when markets like this are a good way to organize society and when they are not. It’s important to both recognize the power of this idea of markets while also recognizing the limited scope.

Maximized welfare is what we call efficiency: the property of a resource allocation of maximizing the total surplus received by all members of society

It’s always important to approach models with some scepticism, but it’s worth a moment to just recognize how surprising this might seem.

No one is trying to maximize welfare, it’s maximized by individuals following their incentives in competitive private goods markets.

Any deviation from this outcome reduces welfare.

DWL can be found by looking at where we are and comparing to where the social planner wants us.

In our model here, DWL is a triangle, but it doesn’t need to be triangular.

We’ll see an example or two in coming videos.

=== Closing

*\[draft\]* We asked how good the market’s answer is, and got the First Welfare Theorem: leave the price alone, and no one can do better. Next time we ask what happens to equilibrium when the world changes — when the curves themselves move.

=== Cut

==== Consumer Surplus Review

We built the intuition for demand as the relationship for an individual buyer between a price and their willingness and ability to pay at that price.

Then we added up all the individual buyers’ demand curves to find the market demand curve, which gives us a relationship between a price and quantity demanded.

Then for a given price, if we have the demand curve we can always find the quantity demanded by intersecting the price with the demand curve.

This essentially answers the question: “How much is the market willing and able to buy at this price?”

And when we change the price, from the Law of Demand, we know the quantity can change, and will move in the opposite direction as price.

That is for one buyer at one quantity. But we have many buyers, and even buyers buying multiple units.

To find the CS in the market we need to add up the consumer surplus for every unit bought.

Then we move out across the whole range of units sold, quantity demanded.

This gives us geometric objects that have area. We can find the area with some basic geometry.

Summary – Consumer Surplus is represented by the area

+ Below the buyer’s willingness to pay
+ Above the price buyers are paying
+ Inside the quantity bought

==== Producer Surplus Review

Buyers form one side of the market. Sellers form the other.

Here we’ll do a similar thing for sellers.

In a previous video we introduced a model to capture the relationship for an individual seller between a price and their willingness and ability to sell at that price.

_*Actually do a review here.*_

Then we added up all the sellers in the market to find the market supply curve.

_*Actually do a review here.*_

For a given price, if we know the supply curve we can always find the quantity supplied by intersecting the price with the supply curve.

This essentially answers the question: “How much is the market willing and able to sell at this price?”

And when we change the price, from the Law of Supply, we know the quantity can change, and will move in the same direction as price.

That is for one seller for one unit of quantity.

But we have many sellers, and sellers selling many units.

To find the PS in the market we need to add up the producer surplus for every unit sold.

We can start by finding the PS for the seller with the lowest willingness to sell.

Then we move out across the whole range of units sold, quantity supplied.

This gives us geometric objects that have area.

We can find the area with some basic geometry.

We’re going to focus mainly on PS here. But be aware of costs, as we’ll come back to them in a later section.

Summary – Producer Surplus is represented by the area

+ Below the price received by the seller
+ Above the supply curve
+ Inside quantity sold

=== Numbers

- Market: the B3 market throughout. Demand P = 12 − Q/5, supply P = 2 + Q/20, equilibrium at 40 and \$4. Q is in thousands of pounds, and one person is one 1,000 pound lot.
- Equilibrium: CS \$156,000, PS \$39,000, TS \$195,000.
- Ceiling at \$3: quantity demanded 45, quantity supplied 20, 20 exchanged. CS \$138,000, PS \$9,500, DWL \$47,500.
- Floor at \$6: quantity demanded 30, quantity supplied 80, 30 exchanged. CS \$87,000, PS \$96,750, DWL \$11,250.
- Exercise, pumpkin pasties: P = 12 − Qd/2 and P = 2 + Qs/2, equilibrium at 10 and 7. Ceiling of 5 galleons: 6 exchanged, CS 33, PS 9, DWL 8. Floor of 9 galleons: 6 exchanged, CS 9, PS 33, DWL 8.
