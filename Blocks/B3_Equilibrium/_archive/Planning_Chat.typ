// Exported from Plass
#set page(paper: "us-letter", margin: 1.25in, numbering: "1", number-align: center)
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

= Planning Chat

Taylor’s words from the B3 and B4 planning chats, as typed.

== Sep 16 | Companion Spec

lets start by setting up the buyers on one side of the platform with the demand curve locked to the screen, then the opposite side for the sellers, then start with one buyer walking from one seller to the next, leaving a connection visualized somehow with the one it prefers, the one with the lowest price. i want bars over each of their heads representing their MB and MC. then afterward, the buyer goes back to the seller they match with. then a second buyer goes through, including the one that's already selling to the first buyer. each buyer and seller will accept a better offer if it's available. this process continues, until no one wants to change. when an unmatched buyer and a seller match, they pick a price that's halfway between their values. when one is already matched, they pick a price that's halfway between the previous match and the unmatched MB or MC. if someone becomes unmatched, they then start over. i think it's worth having the bars up on the graphs glued to the screen, since that's the easiest way to think about buyers and sellers. and we'll animate these as being matched or not, maybe with a highlight or by showing their ps and cs and the price or something.

then to scale and data. i think we start with one buyer and one seller to get the idea, then we go to two of each to get the mechanics of switching and things. then we go up to maybe 10 each, then maybe more. but lets stop at 10 for now.

== Sep 20 | Animation Directions

players need a price. larger groups will randomly check sellers prices. sellers set a starting proce and lower it if noone buys and buyers can outbid an existing match by some amount. line on the ground is a shadow of the price, which is a line between the buyer and seller's marginals. then we can zoomin for marginal analysis. we move the marginals together so they're basically touching, and then use the price line in red to show what's going to the seller and the buyer, and expenditure, and cs and ps, all while we're zoomed way in on two players.

i think for larger scenes, we can't have the deliberation step. but i want it for smaller numbers of people.

but for you as we do that, lets plan to start with the small number of players first, building up equilibrium, then do the deviations ansimations on the back end.

oh and the picture i have in my mind about the marginal analysis for the two players with their marginals is to face them from the side, with the buyer on the left and the seller on the right, their marginals sitting between them, almost touching, and then a price somewhere on the vertical, and we pause to consider (nothing major in the animations besides a question bottom text) whether they would accept or not. and maybe we do this for the first deliberation, so show what's actually being done at the deliberation stage.

== Sep 21 | After Class

hey i just got back from class, covering B3 with the 3d animations i just wrote up. but i don't know that it landed well. maybe i didn't talk it through well enough. but i feel like it doesn't hit the fundamentals clearly in the way I aim for. and id love your perspective on it. truely get into the weeds from a petagogical perspective. i think what it's trying to do is right, but something is slightly off. and i'm having trouble putting a finger on it. any thoughts?

i stayed somewhat close to the notes, but i never stick to them fully. they're basically prep material before class, not a script i read form.

yeah maybe a lot of the issue is there was too much. i keep running up against the end of the class with the exercises. and id much rather have at least one part of an exercise upfront. that's part of what felt missing today.

== Sep 22 | Core Scenes

ok i've spent the day thinking about this, and getting to B4, which is very closely related to what we're doing in B3. so they dovetail nicely. I do want to go back and clean up B3 before doing B4. i'll do a small review at the top of class before getting into B4. i've been writing out the storyboard on paper.

i think it's maybe worth breaking it into core scenes, instead of just a long animation. there are a list of things i want to convey in the simulation:

+ the basic exchange. i think the animation nails this one. "There is a price that can facilitate this trade if it can be between MC and MB: MC < P < MB." "Show a few other prices that don't work and some that do." And then ask "What price should they choose?"
+ the bidding war. that switching drives the price around. "A price is not stable unless no one has an incentive to switch." "This stability is equilibrium. No one wants to switch." "Who should get the spinach? Gary is able to pay Molly and had a nice deal if AG weren't there."
+ multiple trades. i think we don't quite nail this yet. i think it might be better to stay in the head on view for it instead of having it on the plaza. "Prices must be equal for prices to be stable." "If the pairings prices weren't equal, someone could switch and do better." show a more focussed deliberation phase, where one buyer is highlighted and given two options for who to trade with, maybe two hypotheticals in two boxes, or some other setup for it.
+ buyers. this is where we start to deviate a bit more from the flow in the current animations. i want to jump from 2 by 2 in head on view to a plaza with 100 buyers and a demand curve. "Arange buyers in order and ask who would buy at a range of prices. Put a green check over them, and a green circle under them to indicate a trade. Then show the graph of the demand curve like we already do and an equation for demand." This should be a large enough number that the equation makes sense as a good approximation. Prices must be equal for everyone. At this price, this is how many people would buy. Then show that some aren't happy or willing to pay that much, but still want it. show the offers, which are at the price for those who would pay, and the MB for those who wouldn't.
+ sellers. on the seller side, in a separate plaza, it's a similar setup. The single price, it works for most, but some sellers can't price that low. Their asks are their MC.
+ then the harder one to setup, finding equilibrium.
  - I want a deliberation stage, where the buyer looks at everything available. maybe do this like the hypotheticals done in the boxes in the 2 by 2, checking which ones the buyer would be willing to pay for, and then the one they ultimately choose.
  - should have supply and demand separate to start.
  - Primer does a good job at this stage, and they stack supply and demand vertically on the right of the screen after moving price around for awhile, which allows them to show that quantities are equal. They also showed buyers and sellers on the same graph eventually, which worked because they didn't use the supply and demand graphs to pair the buyers and sellers on the graph.

anyway, that's some progress. i'm still not totally sure how to include deliberation in the finding equilibrium stage while keeping it snappy. i think you're right that the core problem is connected to the long animation and the inability to see the prices for the buyers as the market grows. i don't think we need the growing of the market, and i think having a few stages as it grows to highlight the core ideas of bidding and switching and the single price and deliberation before jumping to those mechanics for one or two players in the very large system is probably the right way to go. i really want to get this right and get it right in a way that lets us simulatate all the things that depend on understanding markets, like taxes, international trade, and externalities.

can you help me write down a detailed plan to hand off to my editor and animator? and interview me about anything that isn't yet clear.

== Sep 22 | Answers

=== Timing

we only got through to the first exercise question, so the whole back half of B3 we didn't even get to. it's a natural place to start in B4 as well, since we're doing price controls at the beginning. i think the jump from 2 by 2 to the full demand curve in the plaza view can basically start with a single price for everyone who's willing and an offer from those who aren't. and then we talk about the incentives to quantity supplied equalling quantity demanded as the core mechanism. this then sets us up nicely for B4. where we do this but while also focussing on welfare and introducing DWL. so i think it's worth doing the whole thing now.

=== Numbers | Chosen from options

Same market, one person = 1,000 lb

=== Price line | Chosen from options

One price line you step, plus boxed deliberations

=== Big plaza | Chosen from options

Sorted row, head-on

i think with the big buyer scenes we can nicely show the full demand curve on the side and somehow visually connect it to the buyers on the plaza, maybe starting in a head on view and then zooming out to the plaza, but with the demand curve made up of those MB lines then moved to the demand curve on the side. sorry i missed your questions, ask again

=== Units

right. i think we just have one person per bar, and we just say if someone want's more than one, we just have them show up twice

=== Window | Chosen from options

Only in scene 1

=== Wed flow

i think i want just a quick review in B4, none of the complexity, just basically getting through the core ideas, beelining straight for Q2 of the exercise. i don't feel like we truely did a good job getting the ideas with equilibrium on the graph, and i want to make sure to spend plenty of time there. then we use that as a jump off for the rest of B4. not sure that answers your question though.

and while you're at it, can you add all the context from this conversation to that file to make the handoffs as easy as possible? i want all the text i gave you recorded somewhere in the dir so the editor can use it in the notes, which needs to be in my words, not theirs, and that would let them use it as reference material. but the most important thing is getting the animation details right that we layed out.

== Sep 22 | B4 Back Half

ok when i go into the back half of the animations, thinking about trying to do better than the market, the decisions we’ve made up front don’t seem to continue on. outline should be: 1. how much does the market benefit buyers and sellers, talk about total surplus, then ask whether we can increase it by raising the price, introduce DWL as the ts that we could have had, zooming into a buyer and seller pair that don’t trade because of the price control, then by lowering the prices, show the DWL again with a specific pair, then give them the trade, showing how TS is maximized by allowing all these people to trade with each other, and showing that we don’t actually want anything more, that if we forced the next pair to trade, they would lose benefit, nevative TS. that’s the outline.

so could you:

+ reorder and reanimate what’s needed to get that to work
+ then update all that animation with the styling choices of the front half?

== Sep 26 | The Structure I Want

the problem right now is that the organization i want and what I did in class aren't the same. B3 in class didn't get far enough, so we're a little behind. the layout i want is B3 introduces the incentives of buyers and sellers in markets, directly after introducing supply and demand, only indirectly touching individual PS and CS welfare as a way to measure incentives. then B4 does welfare at the market level, starting by showing one exchange, setting the price very low with a price control, thinking through quantity exchanged, and so on. then thinking about incentives in the price control, and then a move to equilibrium, and how welfare changed. then more quickly show a high price, doing it with TS maybe here. then force a few more people to exchange and see what happens to TS. then do first welfare theorem. rigiht now B4 doesn't compare welfare changes in price control to equilibrium. but maybe that lives better in B5 anyway. but overall, that's the structure i WANT even though we spent too long on the specifics of the market dynamics in B3 last week.

i think it's basically right. we use price controls to motivate the question of what's best. i think starting at equilibrium makes sense, since we just showed that setting in B3, but maybe there are better ways.

== Fall 2024 | Comments in the Old Code

- Last time we ... ppf ... but we're left the question where to live on the PPF. How do we choose between a and b? That's the question we turn to: how to pick where on the PPF to live?
- If there's no deal, lower price. If there's a deal, raise price.
- If there's no deal, raise price. If there's a deal, lower price and break deal.
- Find the area of producer surplus on a supply curve for different prices.

~
