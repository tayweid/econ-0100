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

== B5 Outline

// plass:comment
// | Editor, Sep 27, evening. This is a new file. B5_Notes.typ and B5_Outline.typ are untouched, so nothing you haven't reviewed is lost. The outline sits at the top and the notes follow it.
// | Your lines are moved, not rewritten. Anything in {++ ++} is mine and is a proposal. Cuts are struck. Each step opens with a Beats comment, and an Editor comment explains each move and flags each place where the words are mine.
// | The new order is yours from chat today: elasticity, then shifters, then comparative statics. Your chat lines are placed below as body text and as direction lines, word for word.
// /plass:comment

elasticity: curves hold still and the price changes. shifters: the curves move, sorta price stays the same. comparative statics: price and curves move.

// plass:comment
// | Editor. Your Sep 27 arc, word for word from chat. It replaces the Sep 13 arc below, which put shifters first.
// /plass:comment

we want to start by asking what happens when things change in the market, and that requires thinking about changes in the supply and demand curve. then we get into elasticity, when it’s not the curve itself changing but the price, then we bring it all together with comparative statics.

// plass:comment
// | Editor. Your Sep 13 arc, kept for the record. Superseded by the line above.
// /plass:comment

=== {++Steps++}

+ {++What markets are doing. Recap of equilibrium and total surplus.++}
+ {++When the price goes up. Spinach and chocolate, side by side.++}
+ {++It’s not the slope. The same line, two places on it.++}
+ {++Measuring elasticity. The midpoint method, elastic and inelastic.++}
+ {++The extremes. Gary’s EpiPen and Andrew’s spinach.++}
+ {++Sellers. The elasticity of supply.++}
+ {++Sometimes things change. The spinach study.++}
+ {++Shifters: demand.++}
+ {++Shifters: supply.++}
+ {++Comparative statics. One shift, then the math.++}
+ {++Both curves shift. Price is indeterminate.++}
+ {++How much price, how much quantity. The same shift against elastic and inelastic supply.++}

// plass:comment
// | Editor. Why this order works, in short. Each step adds one moving part: the price moves along fixed curves (2 to 6), the curves move at a fixed price (7 to 9), then both (10 to 12).
// | Two handoffs make it hold together. The hook’s side-by-side figure raises the slope question that step 3 answers. And the shifters end with a shortage or surplus at the old price, which is the first frame of comparative statics, so nothing sits between them.
// /plass:comment

=== Part B Outline | Episode B5

Comparative statics analyzes how equilibrium changes when supply or demand conditions shift. Elasticity measures how responsive quantity is to changes in price, income, or other factors.

=== Tutorial 2.4 | Comparative Statics

- Supply curve shifters
- Demand curve shifters
- Changes to price and quantity
- Both supply and demand shifting

=== Tutorial 2.5 | Elasticity

- Intuition with rubber bands
- Elasticity equation
- Complements/Substitutes
- Inferior/Normal/Lux
- Applied to supply
- Applied to demand
- Cross price
- Income elasticity of demand, but we won’t use it in this class

// plass:comment
// | Editor. Copied from B5_Outline.typ, which copied them from B_Outline.typ.
// | Decided: the midpoint method, no chapter labels, and today: elasticity first, spinach inelastic and chocolate elastic, seller bars for spinach only, a named example for the extremes. Still open: the episode title, and every {++ ++} passage.
// /plass:comment

== Episode B5 | Comparative Statics and Elasticity

_Markets will adapt to change in costs and preferences according to the responsiveness of supply and demand._

_How prices change._

// plass:comment
// | Beats for B5_Animation_new.py, scene B5. Topic titles orient each section; questions serve as prompts. Gold bars measure shifts; side lists retain the scenarios.
// | 0.a · Bumper: How prices change.
// | These comments outline the screen action. The animation code holds the choreography.
// /plass:comment

// plass:comment
// | Editor. The subtitle "Markets will adapt..." names change first and responsiveness second; the episode now teaches them the other way around. It still reads true, so no edit is proposed.
// | B5_Animation.py still follows the old order. The beats below are renumbered for the new order, so the code will need to follow once you approve.
// /plass:comment

// plass:comment
// | For the animator, Sep 27 night. Taylor hasn't reviewed this file yet. Build from it tonight on these terms, and he reviews the animation, not the text.
// | 
// | File. Copy B5_Animation.py to B5_Animation_new.py and work only in the copy. B5_Animation.py stays as it is so the class on Sep 28 has a working version. Taylor chooses which one to present.
// | 
// | Status of the text. Treat every {++ ++} passage and every struck cut as approved for animation, provisionally. On-screen text comes only from the beat lines, which quote titles, questions, and bottom lines exactly. Where a beat gives no text, add none. Don't write new definitions.
// | 
// | Provisional defaults for the open questions:
// | · On screen, count buyers, not bars ("5 buyers drop out"), as in B3, where one person is one 1,000-unit lot. "Bars" would clash with chocolate bars.
// | · Perfectly inelastic: Gary's EpiPen. Perfectly elastic: Andrew at $4.25.
// | · The −5/19 example is cut: drop old beat 5.i.
// | · Chocolate is in thousands of bars; its axis unit label reads "thousand bars".
// | 
// | Most of the episode is built. Each beat line below ends with its old ID in brackets, e.g. [old 5.d]. Those are reorders: move the code, renumber the pause, and fix the entry and exit so each beat starts from the state the one before it leaves. Beats marked [new] are the build list:
// | · 1.c, the bars at $4 at the end of the recap. Reuse the B4 lot bars (B4_Animation.py, beat 2.a: one bar per lot).
// | · 2.a to 2.g, the side-by-side hook. All numbers are in the last Editor comment of this file.
// | · 3.a, the slope question on the hook figure.
// | · 4.f and 4.h additions, the returns to the hook.
// | · 6.a and 6.b, the seller bars on spinach.
// | · 7.a, the turn from price moving to curves moving.
// | The largest reorder: old steps 3 and 4 (shifters) now come after old step 5 (elasticity). Old 3.a starts from the old 2.b state, which now arrives after the seller bars. Check every changed boundary in the viewer.
// | 
// | Ask Taylor only about something these notes don't settle. Anything settled here that turns out wrong on screen is his to change in review.
// /plass:comment

In this video we’ll consider what happens to equilibrium price and quantity when preferences change and shift the demand curve or when costs change and shift the supply curve.

// plass:comment
// | Editor. This opening line describes only the shifters half. Proposed addition below so it names the first half too. Wording is mine.
// /plass:comment

{++But first, we’ll ask what happens to buyers and sellers when the price itself changes.++}

=== {++1 | What Markets Are Doing++}

// plass:comment
// | Beats
// | 1.a · The familiar market at 40 and $4. [old 1.a]
// | 1.b · CS and PS become total surplus. [old 1.b]
// | 1.c · Hold the price at $4, with every buyer’s bar and every seller’s bar in view. This is the frame the next step starts from. No new text. [new]
// /plass:comment

_*Start by talking about what markets are doing, that we get equilibrium price because of buyers and sellers incentives, and that under some conditions, this is very good for buyers and sellers, although not everyone.*_

// plass:comment
// | Editor. Unchanged from B5_Notes.typ. The struck frame cues are the 2024 storyboard cues, proposed for removal there too.
// | New beat 1.c: ending the recap on the bars at $4 lets the hook start with the price line moving, not with a new picture.
// /plass:comment

==== #strike[STORYBOARD: B1 | B2 | B3 | B4]

{++Back in B3,++} #strike[Last time] we showed that there was only one price where neither buyer nor seller would want to change their price: #mi(`Q_S = Q_D`). This is what we call equilibrium: no one wants to change.

Combining the supply and demand relationships on the same graph makes this abundantly clear.

==== #strike[B3]

This pins down how much of each quantity we would want.

==== #strike[B4]

We also wanted to know who benefits from the exchanges in the market. So we developed producer surplus and consumer surplus.

==== #strike[B3]

{++Last time we used++} #strike[Later, we’re going to use] a government policy to show that markets maximize *Total Surplus Value*, the sum of PS and CS.

=== {++2 | When the Price Goes Up++}

// plass:comment
// | Beats
// | 2.a · Title: When the price goes up. Fade out supply. Spinach demand on the left, labeled Spinach; chocolate demand on the right, labeled Chocolate. The two lines are drawn identical, with the axis numbers hidden. Both markets at 40 and $4, with the buyers’ bars up to the price line. [new]
// | 2.b · Question: Which buyers are hit harder? Hold for a class vote. [new]
// | 2.c · Raise the price line from $4 to $5 in both markets together. Bars whose tops fall below $5 gray out. [new]
// | 2.d · Readouts under each graph: 5 buyers drop out; 20 buyers drop out. [new]
// | 2.e · Gary’s spinach bar at $6 stays lit, labeled Gary. [new]
// | 2.f · Fade in the axis numbers: spinach to $12 and 60 thousand lb, chocolate to $6 and 120 thousand bars. The $4 dots now read at different heights on the same-looking line. [new]
// | 2.g · Labels: Elastic under chocolate, Inelastic under spinach. No bottom line and no formula yet. [new]
// /plass:comment

_*we found price in B4. what happens to buyers when the price of spinach goes up? but do it for two different goods. start with an inelastic good and an elastic good and ask which one is most impacted by an increase in price.*_

_*spinach inelastic and chocolate bars elastic, with the figure of both side by side showing the same shapes on the graph, done by scaling the axes.*_

// plass:comment
// | Editor. Both direction lines are your words from chat today, word for word. The price was found in B3; B4 added surplus. "we found price in B4" may want to read B3.
// | The numbers. Spinach is the B3 demand, P = 12 − Q/5, drawn with price to $12 and quantity to 60. Chocolate is P = 6 − Q/20, in thousands of bars, drawn with price to $6 and quantity to 120. Each line runs corner to corner, so the two lines look identical on screen. Both pass through 40 at $4.
// | Why the dots can’t sit in the same place. Elasticity has no units, so scaling the axes can’t change it. If the lines look the same and the dots sit in the same spot, the two elasticities are equal. With these numbers the spinach dot sits a third of the way up its line and the chocolate dot two thirds of the way up. That difference is the whole lesson of step 3, so the figure sets it up for free.
// | One cost of the scaling: $1 on the chocolate axis is twice as tall as $1 on the spinach axis. The price line jumps farther on the right. Worth saying aloud, or students may think chocolate got the bigger price increase.
// | A word clash: "bars" means both the buyers’ bars and chocolate bars. You may want a different word on screen for one of them, such as lots.
// | Amanda-Grace is left out on purpose. In B1 her chocolate demand tops out at $2.50, so at $4 she wouldn’t be in this market.
// /plass:comment

{++We found the price of spinach: \$4. Now suppose it goes up to \$5. What happens to the buyers? Let’s ask that question for two goods at the same time: spinach, and chocolate bars from the stand next to it.++}

{++Which buyers do you think are hit harder?++}

// plass:comment
// | Editor. Both lines above are mine. The question asks who cuts back more, not who pays more. The second reading leads to revenue, which you’re leaving out.
// /plass:comment

{++In the spinach market, 5 lots drop out. Gary would pay up to \$6, so he’s still buying. In the chocolate market, 20 lots drop out. Half the buyers are gone.++}

{++Why? Spinach is the base of Gary’s salads. Most of the people buying it at \$4 would pay a lot more. Chocolate is a treat. Plenty of people buy a bar at \$4, but only just. Raise the price a dollar and they walk away.++}

// plass:comment
// | Editor. Mine, both paragraphs. The story only has to be believable; B5.2 doesn’t ask students why a good is elastic. The bars carry the point: spinach bars run from $12 down to $4, and chocolate bars are squeezed between $6 and $4.
// /plass:comment

{++We call chocolate buyers elastic: they respond a lot to a change in price. Spinach buyers are inelastic: they don’t respond much.++}

// plass:comment
// | Editor. Mine. This names the idea before the formula, so step 4 measures something students have already seen. Your own line in step 3 ("We would say the first example is very responsive...") names it again, formally.
// /plass:comment

=== {++3 | It’s Not the Slope++}

// plass:comment
// | Beats
// | 3.a · Question: Is it the slope? Hold the two identical lines from 2.f, then clear them. [new]
// | 3.b · Title: Price elasticity of demand. Show the same spinach demand curve twice, selecting a high-price and a low-price interval. [old 5.a]
// | 3.c · Cut each price by $1; both quantities rise by 5, but only the first doubles. [old 5.b]
// | 3.d · Introduce elasticity as responsiveness in percentage terms. [old 5.c]
// /plass:comment

_How should we measure the responsiveness of the demand curve?_

// plass:comment
// | Editor. Your lines from step 5 of B5_Notes.typ, in their order. They were written to open elasticity cold; here they answer the question the hook leaves. The two goods looked the same on screen and responded very differently, so the slope can’t be what we’re measuring.
// | Proposed bridge below, mine.
// /plass:comment

{++The two lines looked the same, and the buyers responded very differently. So what are we measuring? Let’s stay on one line, the spinach line, and change the price in two different places.++}

The animation I have in mind follows this basic outline.

Let’s do two examples#strike[ of comparative statics], one where we decrease the price by y but quantity is very low, and one where we decrease the price by y but the quantity is very high.

_*Show the two models side by side, animating the changes and fading out the supply curve, so all we see is the demand curve and the price and quantity changes.*_

_*Use the B3 demand curve P = 12 - Q/5, where Q is in thousands of pounds of spinach. Then use the prices of 11 and 10 for the first example, with quantities of 5 and 10, and prices of 2 and 1 for the second example with quantities of 50 and 55.*_ #strike[_*Maybe do a third example to show that they aren’t always reciprocal, using prices of 3 and 2, with quantities of 45 and 50.*_]

// plass:comment
// | Editor. Proposed cut: your third example ($3 to $2, elasticity −5/19). It was there to show the two sides of the line aren’t always reciprocal. The hook already shows that: spinach at $4 to $5 is −0.6, which is no reciprocal of anything here. It saves a beat in a full session.
// | Your examples decrease the price and the hook increased it. I’d leave them as decreases. Your midpoint line in step 4 says the answer is the same either way, and this gives it something to point back to.
// /plass:comment

Which change in quantity is larger?

Well in one way, the quantities have changed by exactly the same amount. We’ve shifted the price by the same amount, and because the slope is the same, the absolute change in the quantity is exactly equal.

But the first example doubled the quantity. Has the second? No! It has gone up, but by well less than half.

So if we’re interested in measuring how buyers respond to changes in the market, how might we measure changes? Do you think it’s appropriate to use the absolute changes?

Probably not. These two examples show that absolute changes don’t tell the full story. We would say the first example is _*very responsive*_ while the second example is _*not very responsive*_. The word we use for this idea is _*elasticity*_. The first example is _*elastic*_ and the second example is _*inelastic*_.

// plass:comment
// | Editor. Counting lots worked in the hook because both markets started at 40. Here the starting points differ, so the same 5 lots mean different things. That is the reason for percentages, and your lines above make it.
// /plass:comment

=== {++4 | Measuring Elasticity++}

// plass:comment
// | Beats
// | 4.a · On the $11 to $10 example, measure the quantity change and its midpoint base. [old 5.d]
// | 4.b · Measure the price change and its midpoint base in the same way. [old 5.e]
// | 4.c · Turn the measurements into percentage bars on a shared scale. [old 5.f]
// | 4.d · Find elasticity of −7; distinguish its sign from its responsiveness. [old 5.g]
// | 4.e · Move to the second interval; the same changes give elasticity of −1/7. [old 5.h]
// | 4.f · Return to the hook figure, axis numbers shown. Readouts under each graph: ε = −0.6 under spinach, ε = −3 under chocolate. [new]
// | 4.g · Stop at the unit-elastic midpoint of the spinach line, $6: equal percentage changes in magnitude. [old 5.j]
// | 4.h · Label the elastic and inelastic regions while the slope stays constant. [old 5.k] Addition: a dot at 40 and $4 on the spinach line, sitting in the inelastic region. [new]
// /plass:comment

We have a way of calculating these things with the _*elasticity of demand*_.

#mitex(`
\epsilon_D = \frac{\%\Delta Q_b}{\%\Delta P} = \frac{\frac{Q_b' - Q_b}{\bar{Q_b}}}{\frac{P' - P}{\bar{P}}}
`)

We use the quantity on top because we’re essentially asking how the quantity responds to a change in price. So a larger number is more responsive.

{++This is called the midpoint method. We divide each change by the midpoint of the two values, halfway between where we started and where we ended. That way we get the same answer whether the price goes up or down.++}

{++Let’s try it on our first example. Quantity goes from 5 to 10, a change of 5. The midpoint is 7.5, so quantity changes by 5 divided by 7.5, about 67%. Price goes from \$11 to \$10, a change of −1. The midpoint is 10.5, so price changes by −1 divided by 10.5, about −9.5%. The elasticity is 67% divided by −9.5%, which is −7.++}

{++In the second example, quantity goes from 50 to 55, a change of 5 on a midpoint of 52.5, about 9.5%. Price goes from \$2 to \$1, a change of −1 on a midpoint of 1.5, about −67%. The elasticity is 9.5% divided by −67%, about −0.14.++}

// plass:comment
// | Editor. The three passages above are the ones proposed in B5_Notes.typ, unchanged. The next one is new and mine: it brings the formula back to the hook, so the numbers confirm what students saw.
// /plass:comment

{++Now back to the two goods. For spinach, quantity falls from 40 to 35, about −13% on a midpoint of 37.5. Price rises from \$4 to \$5, about 22% on a midpoint of 4.5. The elasticity is −0.6. For chocolate, quantity falls from 40 to 20, about −67% on a midpoint of 30. The price change is the same 22%, so the elasticity is −3.++}

_*Elasticity visualization: use a horizontal line composed of two parts, the change part and the base part. This could show the idea that elasticity is a way of measuring the responsiveness and not just the slope. I’m thinking about a visual like grant’s bayes video. *_#strike[_*The elasticity measure could be slighly different than the midpoint method, using the smaller of the two values instead of the middle of the two values.*_]_* Then visualize the horizontal axis with a horizontal line in the elasticity fraction and the vertical in the elasticity fraction. Then have both up and down different colors and the changes part be a more vibrant color and the base be a muted color. Then move the base around moving the lines in the fraction. Then fade in the numbers, adding the number beside the bars in the SD graph and in the elasticity equation. Then show the elasticity number itself by the fraction. Then move it around. Then color the regions where it’s elastic, and inelastic and fade in a bracket labeling each region.*_

// plass:comment
// | Editor. Your visualization direction, unchanged, with the smaller-base sentence still proposed as a cut. "elasticty" is corrected to "elasticity"; that is the only change.
// /plass:comment

{++Demand elasticity is negative, since price and quantity demanded move in opposite directions, so we look at its size. When the size is bigger than 1, quantity changes by more than price, in percentage terms. We call that elastic. When it’s smaller than 1, quantity changes by less than price. We call that inelastic. And when it’s exactly 1, we call it unit elastic.++}

{++Notice something about our two examples. They came from the same demand curve, with the same slope everywhere. But the first was elastic and the second was inelastic. Along a straight-line demand curve, the slope stays the same while the elasticity changes. Near the top, where the price is high and the quantity is small, demand is elastic. Near the bottom, it’s inelastic. And in the middle, at \$6, it’s unit elastic.++}

{++That’s what happened with our two goods. Spinach at \$4 sits in the bottom third of its line, where demand is inelastic. Chocolate at \$4 sits in the top third of its line, where demand is elastic.++}

// plass:comment
// | Editor. The first two passages are from B5_Notes.typ, unchanged. The third is new and mine. It closes the loop on the hook’s figure: same line on screen, different place on it.
// /plass:comment

=== {++5 | The Extremes++}

// plass:comment
// | Beats
// | 5.a · Move price along a vertical demand curve; quantity does not respond. Label: Gary’s EpiPen. [old 5.l, label new]
// | 5.b · On perfectly elastic demand, quantity can change at the same price. Label: Andrew’s spinach. [old 5.m, label new]
// /plass:comment

// plass:comment
// | Editor. Both passages were proposed in B5_Notes.typ with generic examples. At your request they now each have a specific, named example. The wording is mine.
// | Gary’s EpiPen is the standard real case: its list price for a two-pack went from about $100 in 2007 to about $600 in 2016, and people who need one kept buying. Nothing at a farmers market is truly perfectly inelastic, so the example steps outside the market on purpose. An alternative inside it: a restaurant that has printed tonight’s menu and needs exactly 20 pounds of spinach, whatever the price. That’s nearly vertical, but only for one night.
// | Andrew’s stand calls back to B3, where he priced at $4.25 near his cost.
// /plass:comment

{++There are two extreme cases. If buyers would buy exactly the same amount no matter the price, the demand curve is vertical. Quantity doesn’t respond at all, so the elasticity is 0. We call this perfectly inelastic.++} #strike[Think of a life-saving medicine with no substitute.] {++Think of Gary’s EpiPen. He’s allergic to peanuts, and he buys one two-pack a year, whatever it costs.++}

{++At the other extreme, if buyers would buy any amount at one price but nothing at all if the price rose even a little, the demand curve is horizontal. We call this perfectly elastic.++} #strike[Think of one farmer’s spinach at a market full of identical spinach.] {++Think of Andrew’s spinach. Every other stand sells the same spinach at \$4. If Andrew asks \$4.25, nobody buys from him.++}

_*{++Show a vertical demand curve, then a horizontal one, each labeled.++}*_

=== {++6 | Sellers++}

// plass:comment
// | Beats
// | 6.a · Title: Price elasticity of supply. The spinach market at 40 and $4, with the sellers’ bars and the supply curve. [old 5.n, bars new]
// | 6.b · Raise the price to $5. New sellers’ bars light up, from 40 to 60. Readout: 20 more sellers. [new]
// | 6.c · Use the same percentage ratio to calculate positive supply elasticity, 1.8. [old 5.o; check its numbers match $4 to $5, 40 to 60]
// /plass:comment

// plass:comment
// | Editor. Seller bars for spinach only. If the chocolate price rose alongside spinach, Molly and Andrew could switch crops, and that’s a PPF question this step doesn’t need.
// | The supply elasticity of 1.8 is the same number that comes back in step 12, where the same shift meets elastic and inelastic supply.
// | The first passage below was proposed in B5_Notes.typ. The second is new and mine.
// /plass:comment

{++Everything we just did for buyers works for sellers too. The elasticity of supply measures how much the quantity supplied responds to a change in price. Since price and quantity supplied move together, it’s positive. When sellers can easily expand production, like a farmer with spare land, supply is elastic. When they can’t, like beachfront property, supply is inelastic.++}

{++Go back to spinach at \$4 and raise the price to \$5. Molly and Andrew grow more, and a few new farmers bring their spinach to market. The quantity supplied goes from 40 to 60, a change of 20 on a midpoint of 50, or 40%. The price rises 22%. The elasticity of supply is 1.8.++}

=== {++7 | Sometimes Things Change++}

// plass:comment
// | Beats
// | 7.a · Question: What if the curves move instead? Clear the elasticity work back to the spinach market at 40 and $4. [new]
// | 7.b · Title: A change in preferences. Pick out the willingness-to-pay bar for Gary’s next unit. [old 2.a]
// | 7.c · Bring his bar forward. The spinach study raises his valuation. [old 2.b]
// /plass:comment

// plass:comment
// | Editor. Your step 2 from B5_Notes.typ, moved down whole. Its lines were written to open the episode, and they still work as the turn from the first half to the second.
// | Proposed bridge first, mine. It uses your arc’s own terms from chat.
// /plass:comment

{++So far, the curves have held still and the price has moved. Now let’s hold the price still and move the curves.++}

_*But the world is not always the same. Sometimes things change. Let’s say a new study comes out linking spinach to longer lives. Gary liked spinach before. But like nearly everyone, this new piece of information means he’s even more interested in buying spinach.*_

First, we’re going to show how prices and quantities, our coordination device, are impacted by forces outside the model. We’ll do this by #strike[building on] {++introducing++} the idea of *Shifters*.

=== {++8 | Shifters: Demand++}

// plass:comment
// | Beats
// | 8.a · Introduce a at zero, then change price along the unchanged demand curve. This is now a callback to steps 2 to 4. [old 3.a]
// | 8.b · The spinach study raises a. Measure the shift in gold and begin the scenario list. [old 3.b]
// | 8.c · Read the same shift as greater willingness to pay. [old 3.c]
// | 8.d · Less preference lowers a; retain each case in the list. [old 3.d]
// | 8.e · Higher income increases demand for a normal good. [old 3.e]
// | 8.f · Higher income decreases demand for an inferior good. [old 3.f]
// | 8.g · More expensive romaine increases demand for spinach. [old 3.g]
// | 8.h · More expensive dressing decreases demand for spinach. [old 3.h]
// | 8.i · More identical buyers flatten market demand; show the changing slope coefficient. [old 3.i]
// /plass:comment

// plass:comment
// | Editor. The first two passages were proposed in B5_Notes.typ to introduce the difference between moving along a curve and shifting it. Now students have already spent four steps moving along the curve, so the first passage is revised to point back at that instead of introducing it. The revision is mine.
// /plass:comment

{++Before we look at what changes the demand curve, let’s remember what doesn’t. When the price of spinach went from \$4 to \$5, the buyers didn’t get a new demand curve. They moved along the one they already had. We call this a change in the quantity demanded.++}

{++A shift is different. Something other than the price of spinach changes, and now Gary wants a different amount at every price. We call this a change in demand. The whole curve moves.++}

_*{++Show a dot sliding along the demand curve as the price moves, labeled “change in quantity demanded.” Then hold the price still and move the whole curve, labeled “change in demand.”++}*_

_*What does this do to the model? Well, nothing has changed about costs or the number of sellers, so the supply curve is exactly the same. But because spinach is now known to be healthier than we thought, buyers want spinach more. This means buyers are more willing to buy spinach. Buyers are willing to pay more for the same quantity and are willing to buy more at the same price. This means the demand curve shifts up.*_

What would happen to Gary’s demand curve if he learns that spinach has more health benefits than he had thought. He’d be more willing to pay for spinach at every quantity or alternatively, he would be willing to buy more spinach at every price. Either way you think of it, his demand curve shifts out.

Gary isn’t the only one who realizes spinach has more health benefits than previously thought. It turns out everyone in the market now prefers spinach more than they had. This shifts the demand curve out.

Everyone is willing to buy more spinach at every price or alternatively everyone is willing to pay more for spinach at every quantity. The reverse is also true. If buyers begin to prefer spinach less, the demand curve will shift in.

// plass:comment
// | Editor. The passages below were proposed in B5_Notes.typ for income, substitutes and complements, and the number of buyers. Unchanged.
// /plass:comment

{++Preferences aren’t the only thing that shifts demand. What if Gary gets a raise? For most goods, and spinach is probably one of them, more income means he’s willing to buy more at every price. The demand curve shifts out. We call these normal goods.++}

{++Not every good works this way. When Gary’s income goes up, he might buy fewer packs of instant noodles, since he can now afford something he likes better. For these goods, more income shifts demand in. We call these inferior goods.++}

{++Demand also depends on the prices of other goods. Romaine lettuce and spinach can both make a salad. If the price of romaine goes up, some buyers switch to spinach, and the demand for spinach shifts out. Goods like these, where one can stand in for the other, are substitutes.++}

{++Other goods are used together. If the price of salad dressing goes up, buyers make fewer salads, and they want less spinach at every price. The demand for spinach shifts in. Goods like these are complements.++}

{++And just like adding sellers shifts supply out, adding buyers shifts demand out. Every new buyer in the market adds to the quantity demanded at every price.++}

=== {++9 | Shifters: Supply++}

// plass:comment
// | Beats
// | 9.a · Introduce b at zero, then change price along the unchanged supply curve, as in step 6. [old 4.a]
// | 9.b · Molly’s costs raise b. Measure the shift in gold and begin the supply list. [old 4.b]
// | 9.c · Cheaper fertilizer lowers costs and increases supply. [old 4.c]
// | 9.d · More valuable carrots raise the opportunity cost of spinach. [old 4.d]
// | 9.e · More identical sellers flatten market supply; show the changing slope coefficient. [old 4.e]
// | 9.f · Better harvesting technology lowers costs and increases supply. [old 4.f]
// /plass:comment

// plass:comment
// | Editor. Step 4 of B5_Notes.typ, moved whole. The one change is in the first proposed passage, which now points back to step 6 instead of introducing the idea. The change is mine.
// /plass:comment

{++The same distinction holds for sellers. When the price of spinach rose to \$5, Molly moved along her supply curve. That’s a change in the quantity supplied. Anything else that changes her costs shifts the whole curve. That’s a change in supply.++}

Molly’s _*Individual Supply Curve*_ depends on the costs of producing spinach. For example, what would happen if the price of renting farmland increased? Her supply curve would also #strike[increase] {++shift up++}! The cost of each additional unit of spinach becomes more expensive since the input, land, has also become more expensive. This means that, for example, she wouldn’t be willing to produce as much spinach as before at a price of \$4 or any price.

// plass:comment
// | Editor. The rest of the paragraph describes a shift up and in, so "increase" reads as the opposite. The market paragraph below says "shift up".
// /plass:comment

What would happen if she had to pay less for her organic fertilizer? Each additional unit of spinach would become less costly to produce. Molly would be willing to make _more_ spinach than before at a price of \$4 or any price.

What would happen if the price of carrots were to increase? Molly would have a higher opportunity cost of switching her farmland away from carrots to spinach, so the cost of production would also go up!

The changes in the costs of production shift the farmers’ individual supply curves, which in turn shifts the market supply curve. We’ll come back to think about how shifters impact producer surplus#strike[, but we don’t yet have all the tools]. If the cost of inputs like farmland or fertilizer were to increase, production would become more costly for farmers, meaning the supply curve would shift up. Each quantity supplied is now more expensive and farmers are willing to sell less at any given price.

// plass:comment
// | Editor. "We don't yet have all the tools" was written for B2. B4 has now given students CS, PS, and DWL. This episode doesn't return to producer surplus, so the whole sentence may be stale.
// /plass:comment

The market supply curve is also impacted by the number of sellers. Like when we added Andrew’s supply to Molly’s to get the market supply curve, every time another seller opens their doors the supply curve shifts out, and when a seller drops out of the market the supply curve shifts in.

// plass:comment
// | Editor. Proposed passage for B5.1's third standard: technology. Step 11 uses harvesting technology. Unchanged from B5_Notes.typ.
// /plass:comment

{++Technology works like a cheaper input. If a new harvesting machine lets Molly pick her spinach in fewer hours, each additional unit costs her less to produce. She’s willing to sell more at every price, and her supply curve shifts down and out.++}

=== {++10 |++} Comparative Statics

// plass:comment
// | Beats
// | 10.a · Revisit a and its gold shift measure beside the market. [old 6.a]
// | 10.b · Raise demand while keeping the original curve visible. [old 6.b]
// | 10.c · Lower demand, then restore the original curve. [old 6.c]
// | 10.d · Add supply at 40 and $4; begin the comparative-statics case list. [old 6.d]
// | 10.e · Raise demand at the old price and show the shortage of 25. [old 6.e]
// | 10.f · Raise price along the fixed curves; record the new equilibrium. [old 6.f]
// | 10.g · Solve for equilibrium as a function of the demand shift. [old 6.g]
// | 10.h · Substitute the demand increase and recover 60 at $5. [old 6.h]
// | 10.i · Restore the original market before considering falling income. [old 6.i]
// | 10.j · Lower demand at the old price and show excess supply of 25. [old 6.j]
// | 10.k · Lower price; record 20 at $3 in the case list. [old 6.k]
// | 10.l · Restore the baseline and revisit b while keeping the case list. [old 6.l]
// | 10.m · Raise fertilizer costs at the old price and show the shortage. [old 6.m]
// | 10.n · Raise price; record 35 at $5 with all three outcomes in view. [old 6.n]
// /plass:comment

// plass:comment
// | Editor. Step 6 of B5_Notes.typ, moved whole and unchanged. It now follows the shifters directly, as your arc asks: the shift leaves a shortage at the old price, and the price has to move.
// | One thing to notice when you record it: in 10.f the price rises along the fixed supply curve, the same kind of move students measured in steps 2 to 6. A one-line callback could fit there; none is proposed.
// /plass:comment

{++We just talked about shifters.++} #strike[You’ll remember, we talked shifters in Demand.] When forces that impact Buyers’ preferences for spinach change, so does the Demand curve.

==== #strike[B2]

And on the other side of the market, when sellers’ opportunity costs change, so does the supply curve.

==== #strike[B1]

These changes impact the equilibrium through change in Supply and Demand.

_*Introduce a shock parameter #mi(`a`) into the equations. Show what happens to the demand curve when #mi(`a`) shifts up and shifts down. Then fade in the supply curve and show the shifts on the market without changing price.*_

_*At the initial equilibrium price, we now have a shortage because buyers now want more. Sellers are all sold out since buyers want more and both buyers and sellers have incentives to raise the price. This takes us back to equilibrium analysis. Because there’s a shortage, prices will rise until there is no shortage. This might not happen over night. But it’s the direction that the market will go. This will raise #mi(`P^\ast`) and raise #mi(`Q^\ast`).*_

_*Do the math for this. Show the change in price and change in quantity.*_

Let’s say Income goes up. What happens to equilibrium Price and Quantity?

==== #strike[B3]

What happens to equilibrium when Income goes down?

==== #strike[B3]

_*Then do a supply shifter with a parameter #mi(`b`) on a separate graph with a different price and quantity from the first example.*_

What about with an increase in the cost of fertilizer, an input to producing spinach?

==== #strike[B3]

=== {++11 | Both Curves Shift++}

// plass:comment
// | Beats
// | 11.a · Set up both changes; compare three possible outcomes with one baseline. [old 7.a]
// | 11.b · Increase demand and supply; record rising quantity and price. [old 7.b]
// | 11.c · Increase supply further; add rising quantity with unchanged price. [old 7.c]
// | 11.d · Increase supply again; add rising quantity with falling price. [old 7.d]
// /plass:comment

Now what about when the price of romaine lettuce goes up while the price of spinach harvesting technology goes down at the same time?

==== #strike[B3]

This leads to an _increase_ in the equilibrium quantity and an _indeterminate_ change in price.

Prices are _indeterminate_ because the shift in demand raises prices, while the shift in supply lowers prices, and we don’t know the magnitude of the shifts.

==== #strike[B3]

=== {++12 | How Much Price, How Much Quantity++}

// plass:comment
// | Beats
// | 12.a · Compare supply responses on identical graphs through the same equilibrium. [old 8.a]
// | 12.b · Shift demand equally in both markets and follow the equilibria. [old 8.b]
// | 12.c · Compare the resulting price and quantity changes. [old 8.c]
// /plass:comment

_*Ok, but will prices always respond like this? No. It turns out if the slopes were different, the response would be different. Pivot the S&D curves around equilibrium.*_

_*The slope is related to how the S or D curves respond to a change in price. But simply looking at the slope itself gives us the wrong picture.*_

// plass:comment
// | Editor. These were the last two Outline bullets, your old bridge into elasticity. With elasticity first, the second one is now a callback: step 3 is where students learned that the slope gives the wrong picture.
// | The passages below were proposed in B5_Notes.typ for the last B5.3 standard. Unchanged. The left graph’s supply elasticity, 1.8, is the one students calculated in step 6.
// /plass:comment

{++Let’s put the two ideas together. Here’s the same spinach study, and the same shift in demand, against two different supply curves.++}

_*{++Show two graphs side by side. Left: the B3 supply curve. Right: a steep supply curve through the same equilibrium, 40 and \$4. Shift demand up by the same amount on both.++}*_

{++On the left, sellers can respond easily. The price rises only \$1, to \$5, and the quantity rises by 20, to 60. On the right, sellers can’t easily respond. The price rises \$4, to \$8, and the quantity rises by only 5, to 45.++}

{++Same shift, very different outcomes. When supply is elastic, a shift in demand mostly changes the quantity. When supply is inelastic, it mostly changes the price.++}

=== {++Closing++}

// plass:comment
// | Beats
// | 13.a · Hold the paired markets to recap how they respond to change. [old 9.a]
// | 13.b · Introduce the next block: international trade. [old 9.b]
// /plass:comment

// plass:comment
// | Editor. The closing proposed in B5_Notes.typ, reordered to follow the new order: responsiveness first, then shifts. Mine.
// /plass:comment

{++Markets respond to change. Elasticity tells us how much buyers and sellers respond when the price moves. When preferences, incomes, or costs change, the curves shift, and the equilibrium moves to a new price and quantity. And elasticity tells us how that change splits between price and quantity. Next time we take these tools across the border, to international trade.++}

=== {++Parked++}

==== {++Exercise candidate: Toffees++}

// plass:comment
// | Editor. Moved into the B5 notes from B3_Equilibrium/_Unplaced.md on Sep 16. It turns on a subsidy, which Part B doesn't teach (C2 does). It works here if the shifter becomes "production got cheaper"; otherwise hold it for Part C.
// /plass:comment

Due to longstanding tradition, all toffees are made the same way, anyone could easily start making them, and the number of toffee makers had been constant over the past couple of years. This changed when the Ministry imposed a subsidy on all toffee sales. Using a couple of graphs to illustrate your answer, explain what happened in the market because of this subsidy.

// plass:comment
// | Editor. Numbers, checked Sep 27. Spinach is the B3 market throughout: demand P = 12 - Q/5 (Q = 60 - 5P), supply P = 2 + Q/20 (Q = 20P - 40), equilibrium 40 at $4. Q is in thousands of pounds.
// | 
// | Step 2, the hook. Chocolate demand P = 6 - Q/20 (Q = 120 - 20P), Q in thousands of bars. Spinach axes: P to 12, Q to 60. Chocolate axes: P to 6, Q to 120. Both lines run corner to corner.
// | Both at 40 and $4, price to $5, midpoint method. %ΔP = 1/4.5 = 22.2% in both.
// | Spinach: Q 40 to 35, 5 lots out. %ΔQ = -5/37.5 = -13.3%. Elasticity -0.6. Inelastic.
// | Chocolate: Q 40 to 20, 20 lots out. %ΔQ = -20/30 = -66.7%. Elasticity -3. Elastic.
// | The spinach dot is at 1/3 of the line’s height ($4 of $12); the chocolate dot at 2/3 ($4 of $6). On the spinach line, 2/3 of the height is $8, and $8 to $10 there also gives -3, the chocolate number.
// | Gary’s MB $6 (B3) stays in at $5.
// | 
// | Steps 3 and 4, elasticity of spinach demand, midpoint method:
// | Example 1: $11 to $10, Q from 5 to 10. %ΔQ = 5/7.5 = 66.7%, %ΔP = -1/10.5 = -9.5%, elasticity -7. Elastic.
// | Example 2: $2 to $1, Q from 50 to 55. %ΔQ = 5/52.5 = 9.5%, %ΔP = -1/1.5 = -66.7%, elasticity -1/7, about -0.14. Inelastic. Reciprocal of example 1.
// | Example 3, proposed as a cut: $3 to $2, Q from 45 to 50, elasticity -5/19, about -0.26.
// | Unit elastic at $6 and 30, the middle of the line. Elastic above $6, inelastic below.
// | 
// | Step 6, spinach supply, $4 to $5: Q from 40 to 60. %ΔQ = 20/50 = 40%, %ΔP = 22.2%, elasticity 1.8.
// | 
// | Demand shift a: demand P = 12 + a - Q/5. New equilibrium P = 4 + a/5, Q = 40 + 4a.
// | Spinach study, a = 5: demand P = 17 - Q/5, equilibrium 60 at $5. At the old $4, quantity demanded 65 and quantity supplied 40, a shortage of 25.
// | Income goes down, a = -5: demand P = 7 - Q/5, equilibrium 20 at $3. At the old $4, quantity demanded 15 and quantity supplied 40, an excess of 25.
// | 
// | Supply shift b: supply P = 2 + b + Q/20. New equilibrium P = 4 + 4b/5, Q = 40 - 4b.
// | Fertilizer, b = 1.25: supply P = 3.25 + Q/20, equilibrium 35 at $5. At the old $4, quantity supplied 15 and quantity demanded 40, a shortage of 25.
// | 
// | Both shift: P = 4 + a/5 + 4b/5, Q = 40 + 4a - 4b. Romaine up, a = 5, with better technology, b negative:
// | b = -0.625: 62.5 at $4.50. b = -1.25: 65 at $4, price unchanged. b = -2.5: 70 at $3. Quantity rises in all three; price can go either way.
// | 
// | Step 12, the same a = 5 against two supply curves through 40 and $4:
// | B3 supply P = 2 + Q/20: new equilibrium 60 at $5. Price up 1, quantity up 20. Supply elasticity between the two points (midpoint) 1.8.
// | Steep supply P = 0.8Q - 28: new equilibrium 45 at $8. Price up 4, quantity up 5. Supply elasticity between the two points (midpoint) 0.18.
// /plass:comment
