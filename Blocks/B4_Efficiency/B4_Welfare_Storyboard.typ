// Exported from Plass
#set page(paper: "us-letter", margin: 1.25in, numbering: "1", number-align: center)
#set par(justify: true, leading: 10.215pt, spacing: 21.465pt)
#set list(spacing: 13.340pt)
#set enum(spacing: 13.340pt)
#show heading.where(level: 1): set text(size: 23.750pt)
#show heading.where(level: 1): set block(above: 26.391pt, below: 25.105pt)
#show heading.where(level: 1): set par(leading: 13.471pt)
#show heading.where(level: 2): set text(size: 17.500pt)
#show heading.where(level: 2): set block(above: 44.650pt, below: 19.937pt)
#show heading.where(level: 2): set par(leading: 9.926pt)
#show heading.where(level: 3): set text(size: 14.375pt)
#show heading.where(level: 3): set block(above: 38.410pt, below: 18.473pt)
#show heading.where(level: 3): set par(leading: 8.153pt)
#show raw.where(block: false): set text(font: "DejaVu Sans Mono", size: 10.000pt)
#show math.equation.where(block: true): set block(above: 21.490pt, below: 23.702pt)
#set text(size: 12.5pt, font: "New Computer Modern", hyphenate: true)
#set math.equation(numbering: "(1)")
#import "@preview/mitex:0.2.5": mi, mitex

=== Welfare Analysis

=== STORYBOARD: B1 | B2 | B3 | B4

But at this point you might be wondering: Ok, this is nice. Markets pick a price, which gives us a quantity, and a point on the PPF. But is the market even good? Like, do markets give us a coordination devise that makes us as well off as possible?

The answer is complicated as we'll see. But what I'm going to show you is a simple answer to a simpler question.

To show this, I'm going to ask you a simple question, related to the previous class.

What would happen to our market if the government decided the price should be low?

Maybe there's a health equity concern with spinach. We'd like people to not have to pay too much to get healthy food.

=== B2

At this price, Buyers want to buy a great deal and Sellers wish to sell only a little. This is a shortage. Typically in shortages, Buyers would be able to jump the line with a slightly higher price, paying a little more, but being happy to at least get their spinach. Sellers would obviously accept the higher prices. However, here with the legal price being low, Buyers cannot jump the line with a higher price, meaning the shortage will persist despite the incentives to raise the price.

Q. In this situation, how much is sold? A. #mi(`Q_S`).

Q. How much is bought? A. #mi(`Q_S`), since that's all that's available, meaning many Buyers who would want to buy will go without.

What's the welfare in this market?

=== B2

Have we lost welfare? Yes! This loss in welfare is what we call *Deadweight Loss*. For now, we're going to define *DWL* as the loss in *Welfare* compared to it's maximum.

Q. Now what if the goverment want to protect sellers, and mandated a high price?

=== B1

Is this good for those exchanging in the market?

Well its kind of good for sellers. But its very bad for Buyers, which means TS goes down.

This type of logic applies to any price that's not equilibrium, which leaves us with a big result.

_*First Welfare Theorem*_. Competitive markets with no externalities maximize welfare.

This is the thing you often hear free market economists talk about on TV. Let the market do it's thing because it will maximize welfare. But remember two things about this result.

First, markets must be competitive. That means there must be many Buyer's buying identical goods from many Sellers. In Part E, we're going to look at what happens when markets are not competitive.

Second, markets must not have externalities. This means that the things we're buying and selling do not impact those not engaging in the exchanges. When I drive my Prius, even though it's an efficient vehicle, it's releasing carbon dioxide, which contributes to climate change. This is a negative externality: a cost that's not carried by the person driving the car. I also plant flowers in my front garden. As my neighbors walk by, they get a little moment of happiness because of my actions. This is a positive externality: a benefit that's going to someone not involved with the planting of the flowers. In Part C we're going to look at what happens when markets have externalities.

Keeping these caviats in mind, I want to focus for a second on the remarkable result that is the First Welfare Theorem. What this theorem tells us, is that in competitive markets with no externalities, the best thing for society as whole happens when we let Buyers follow their individual incentives, sometimes jumping the line, and when we let Sellers follow their individual incentives, sometimes trying to undercut other sellers. In this kind of environment, it turnout out that everyone following their individual incentives, in a distributed way coordinates those involved toward something that can be thought of as socially optimal! It's remarkable that no one need plan it out.

This is the idea that made Adam Smith famous. By the end of this class, you're going to be able to recognize when markets like this are good way to organize society and when they are not. It's important to both recognize the power of this idea of markets while also recognizing the limited scope.

=== Surplus Value Intuition

But lets say I walk into the store to buy a chocolate bar, I'm willing to pay \$\$2\$ but the seller is selling for \$\$1\$. This is good for me right? I don't need to pay what I would be willing to, so I've saved a dollar. This dollar, the difference between what I would be willing to pay and what I actually have to pay, is what we call Consumer Surplus. And we represent it on the graph as:

+ The area under the demand curve
+ Above the price
+ And at every quantity that's exchanged

And for sellers we have a similar notion, called Producer Surplus. This is just the difference between what a seller is willing to sell for and what they actually sell for. And we represent it on the graph in a similar way:

+ The area above the supply curve
+ Below the price
+ And at every quantity that's exchanged
