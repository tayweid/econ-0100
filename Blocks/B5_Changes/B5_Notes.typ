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

= Episode B5 | Market Changes

_How markets respond to internal and external changes._

=== Outline

+ What markets are doing. Recap of equilibrium and total surplus.
+ When the price goes up. Spinach and chocolate, side by side.
+ It’s not the slope. The same line, two places on it.
+ Measuring elasticity. The midpoint method, elastic and inelastic.
+ The extremes. Gary’s EpiPen and Andrew’s spinach.
+ Sellers. The elasticity of supply.
+ Sometimes things change. The spinach study, then the demand shifters.
+ Shifters: supply.
+ Comparative statics. One shift, then the math.
+ Both curves shift. Price is indeterminate.
+ How much price, how much quantity. The same shift against elastic and inelastic supply.

== Act 1 | Elasticity

Curves hold still and the price changes.

=== 1 | What Markets Are Doing

// plass:comment
// | Beats, as built.
// | 1.a · Title: Equilibrium. Subtitle: No one has a reason to change. The spinach market at 40 and $4. Bottom: Equilibrium: quantity demanded equals quantity supplied.
// | 1.b · The title gains Welfare. Subtitle: Equilibrium in competitive markets maximizes total surplus. CS and PS as vertical slices, recolored into total surplus. Bottom: Total Surplus is the sum of the gains for buyers and sellers.
// | 1.c · The buyers’ and sellers’ bars at $4, the frame the hook starts from. Not built: 1.b cuts straight to 2.a.
// | Cut Oct 2, at your request: “Combining the supply and demand relationships on the same graph makes this abundantly clear.” and “This pins down how much of each quantity we would want.” They were B3 frame cues with no beat.
// | Cues. 1.a → “In Episode B3 we showed…”. 1.b → “We also wanted to know who benefits…” and “Last time we used a government policy…”.
// /plass:comment

In Episode B3 we showed that there was only one price where neither buyer nor seller would want to change their price: #mi(`Q_S = Q_D`). This is what we call equilibrium: no one wants to change.

We also wanted to know who benefits from the exchanges in the market. So we developed producer surplus and consumer surplus.

Last time we used~a government policy to show that markets maximize *Total Surplus Value*, the sum of PS and CS.

=== 2 | When the Price Goes Up

// plass:comment
// | Beats, as built.
// | 2.a · Title: Responsiveness to Price. Subtitle: Which buyers are hit harder? Spinach on the left, P = 12 − Q/5, axes to $12 and 60 thousand lb; chocolate on the right, P = 6 − Q/20, axes to $6 and 120 thousand bars. Both lines run corner to corner, both markets at 40 and $4, the buyers’ bars up to the price line. The axis numbers are shown from the start.
// | 2.c · The price rises to $5 in both markets together. Bars whose tops fall below $5 gray out; the $4 choice stays as a gray ghost.
// | 2.d · A span under each axis measures the quantity forgone, 5 on the left and 20 on the right. No count is printed.
// | 2.g · Under spinach: Inelastic: a relatively small change in quantity. Under chocolate: Elastic: a relatively large change in quantity.
// | Not built from the Sep 27 plan: the hold for a class vote (2.b), Gary’s bar staying lit with his name (2.e), and the axis numbers fading in only after the move (2.f). “Gary would pay up to $6, so he’s still buying” has no mark on screen.
// | Cues. 2.a → “We found the price of spinach…” and “Which buyers do you think are hit harder?”; hold on the question. 2.c → the price moves; no line, or the first words of the next paragraph. 2.d → “In the spinach market, 5 lots drop out…” and “Why? Spinach is the base…”. 2.g → “We call chocolate buyers elastic…”.
// /plass:comment

We found the price of spinach: \$4. Now suppose it goes up to \$5. What happens to the buyers? Let’s ask that question for two goods at the same time: spinach, and chocolate bars from the stand next to it.

Which buyers do you think are hit harder?

In the spinach market, 5 lots drop out. Gary would pay up to \$6, so he’s still buying. In the chocolate market, 20 lots drop out. Half the buyers are gone.

Why? Spinach is the base of Gary’s salads. Most of the people buying it at \$4 would pay a lot more. Chocolate is a treat. Plenty of people buy a bar at \$4, but only just. Raise the price a dollar and they walk away.

We call chocolate buyers elastic: they respond a lot to a change in price. Spinach buyers are inelastic: they don’t respond much.

=== 3 | It’s Not the Slope

_How should we measure the responsiveness of the demand curve?_

// plass:comment
// | Beats, as built.
// | 3.a · Between the two graphs: Is this related to the slope? Then the hook clears.
// | 3.b · Title: Elasticity. Subtitle: Responsiveness to change. The spinach line twice, labeled Spinach, P = 12 − Q/5, with a $10 to $11 interval on the left copy and a $1 to $2 interval on the right. Note: Price goes up by $1 in both scenarios.
// | 3.c · The starting coordinates stay in gray; both changes are measured on both copies: +1 in price, −5 in quantity.
// | 3.d · Bottom: Elasticity measures responsiveness in percentage terms.
// | Direction. Show the two models side by side, animating the changes and fading out the supply curve, so all we see is the demand curve and the price and quantity changes.
// | Direction. Use the B3 demand curve P = 12 - Q/5, where Q is in thousands of pounds of spinach. Then use the prices of 11 and 10 for the first example, with quantities of 5 and 10, and prices of 2 and 1 for the second example with quantities of 50 and 55.
// | Direction. Let’s do two examples, one where we decrease the price by y but quantity is very low, and one where we decrease the price by y but the quantity is very high.
// | Editor. The last two directions describe price cuts; the animation raises the price instead, and the script matches. Cut Oct 2, at your request: “The animation I have in mind follows this basic outline.”
// | Cues. 3.a → “The two lines looked the same… So what are we measuring?”, with the slope question on screen; the hook clears at “Let’s stay on one line”. 3.b → “…change the price in two different places.” and “Which change in quantity is larger?”. 3.c → “Well in one way…” and “But the first example halved…”. 3.d → “So if we’re interested…” and “Probably not…”.
// | Editor. The two intervals were only on screen; the {++ ++} sentence in the first paragraph is a proposal to say them.
// /plass:comment

The two lines looked the same, and the buyers responded very differently. So what are we measuring? Let’s stay on one line, the spinach line, and change the price in two different places. Say the price goes from \$10 to \$11, and then, on the same line, from \$1 to \$2.

Which change in quantity is larger?

Well in one way, the quantities have changed by exactly the same amount. We’ve shifted the price by the same amount, and because the slope is the same, the absolute change in the quantity is exactly equal.

But the first example halved~the quantity. Has the second? No! It has gone down, but by well less than half.

So if we’re interested in measuring how buyers respond to changes in the market, how might we measure changes? Do you think it’s appropriate to use the absolute changes?

Probably not. These two examples show that absolute changes don’t tell the full story. We would say the first example is _*very responsive*_ while the second example is _*not very responsive*_. The word we use for this idea is _*elasticity*_. The first example is _*elastic*_ and the second example is _*inelastic*_.

=== 4 | Measuring Elasticity

// plass:comment
// | Beats, as built.
// | 4 · Title: Price Elasticity of Demand. The formula, ΔQ over Q-bar divided by ΔP over P-bar, beside the $10 to $11 interval.
// | 4.b · Action, the lower row: ΔP = 1 and P-bar = (10 + 11)/2 = 10.5. Bottom: Midpoint method divides each change by the average of its two values. The screen teaches price before quantity.
// | 4.a · Response, the upper row: ΔQ = −5 and Q-bar = (10 + 5)/2 = 7.5.
// | 4.c · Both ratios become percentage bars on one scale: −5/7.5 and 1/10.5.
// | 4.d · The division gives −7. Label: Elastic, |ε| > 1. Bottom: The sign gives direction; the magnitude measures responsiveness.
// | 4.e · The interval slides down the line while the bars update; a bracket marks the elastic region, |ε| > 1.
// | 4.f · It stops at $6. Label: Unit elastic, |ε| = 1, then a marked dot at 30 and $6.
// | 4.g · It continues to $1 to $2. Label: Inelastic, |ε| = 1/7 < 1; a bracket marks the inelastic region.
// | 4.h · The calculation clears and the three regions are listed: Elastic |ε| > 1, Unit elastic |ε| = 1, Inelastic |ε| < 1. Bottom: Different elasticities with the same slope: −1/5. The dot at 40 and $4 is not built.
// | 4.i · Back to the two copies of the line from step 3. Under each: Slope = −1/5. Then Elastic: ε = −7 and Inelastic: ε = −1/7. Top: Same slope, different elasticities.
// | Direction. Elasticity visualization: use a horizontal line composed of two parts, the change part and the base part. This could show the idea that elasticity is a way of measuring the responsiveness and not just the slope. I’m thinking about a visual like grant’s bayes video. Then visualize the horizontal axis with a horizontal line in the elasticity fraction and the vertical in the elasticity fraction. Then have both up and down different colors and the changes part be a more vibrant color and the base be a muted color. Then move the base around moving the lines in the fraction. Then fade in the numbers, adding the number beside the bars in the SD graph and in the elasticity equation. Then show the elasticity number itself by the fraction. Then move it around. Then color the regions where it’s elastic, and inelastic and fade in a bracket labeling each region.
// | Editor. The direction above is built, as 4.a to 4.h.
// | Editor. Not built: the return to spinach and chocolate with −0.6 and −3, planned as the hook’s answer. The paragraphs “Now back to the two goods” and “That’s what happened with our two goods” have no beat, so they are moved to the end of the step, where one would go, after 4.i. I’d build it: the hook raised the question, and these two paragraphs are the only place it is answered. The other option is to cut both paragraphs.
// | Cues. 4 → “We have a way of calculating…”, the formula, and “We use the quantity on top…”. 4.b (.bars, .change, .midpoint) → “This is called the midpoint method…” and the price sentences of the first example. 4.a (.bars, .change, .midpoint) → the quantity sentences. 4.c → the two percentages. 4.d (.divide) → “The elasticity is −67% divided by 9.5%, which is −7.” and “Demand elasticity is negative… We call that elastic.” 4.e to 4.g → “In the second example…” and “When it’s smaller than 1… unit elastic.”; the screen does not step the second example, the bars update as the interval slides, 4.f stops at $6 and 4.g at $1 to $2. 4.h → “Notice something about our two examples…”. 4.i → the end of that paragraph, with Same slope, different elasticities on screen. No beat: “Now back to the two goods…” and “That’s what happened with our two goods…”.
// | Editor. The screen takes price before quantity (4.b, then 4.a). The two worked examples now say price first; the sentences were swapped Oct 2, no words changed.
// /plass:comment

We have a way of calculating these things with the _*elasticity of demand*_.

#mitex(`
\epsilon_D = \frac{\%\Delta Q_b}{\%\Delta P} = \frac{\frac{Q_b' - Q_b}{\bar{Q_b}}}{\frac{P' - P}{\bar{P}}}
`)

We use the quantity on top because we’re essentially asking how the quantity responds to a change in price. So a larger number is more responsive.

The bars over Q and P are the midpoints of the two values. This is called the midpoint method. We divide each change by the midpoint of the two values, halfway between where we started and where we ended. That way we get the same answer whether the price goes up or down.

Let’s try it on our first example. Price goes from \$10 to \$11, a change of 1. The midpoint is 10.5, so price changes by 1 divided by 10.5, about 9.5%. Quantity goes from 10 to 5, a change of −5. The midpoint is 7.5, so quantity changes by −5 divided by 7.5, about −67%. The elasticity is −67% divided by 9.5%, which is −7.

In the second example, price goes from \$1 to \$2, a change of 1 on a midpoint of 1.5, about 67%. Quantity goes from 55 to 50, a change of −5 on a midpoint of 52.5, about −9.5%. The elasticity is −9.5% divided by 67%, about −0.14.

Demand elasticity is negative, since price and quantity demanded move in opposite directions, so we look at its size. When the size is bigger than 1, quantity changes by more than price, in percentage terms. We call that elastic. When it’s smaller than 1, quantity changes by less than price. We call that inelastic. And when it’s exactly 1, we call it unit elastic.

Notice something about our two examples. They came from the same demand curve, with the same slope everywhere. But the first was elastic and the second was inelastic. Along a straight-line demand curve, the slope stays the same while the elasticity changes. Near the top, where the price is high and the quantity is small, demand is elastic. Near the bottom, it’s inelastic. And in the middle, at \$6, it’s unit elastic.

Now back to the two goods. For spinach, quantity falls from 40 to 35, about −13% on a midpoint of 37.5. Price rises from \$4 to \$5, about 22% on a midpoint of 4.5. The elasticity is −0.6. For chocolate, quantity falls from 40 to 20, about −67% on a midpoint of 30. The price change is the same 22%, so the elasticity is −3.

That’s what happened with our two goods. Spinach at \$4 sits in the bottom third of its line, where demand is inelastic. Chocolate at \$4 sits in the top third of its line, where demand is elastic.

=== 5 | The Extremes

// plass:comment
// | Beats, as built.
// | 5.a · Title: Elasticity: Two Extremes. Subtitle: Buyers who are perfectly responsive and perfectly non-responsive to changes in price. Left: a vertical demand curve labeled Gary’s EpiPen; the price moves and the quantity stays. Bottom: Price changes; quantity stays fixed.
// | 5.b · Right: a horizontal demand curve at $4 labeled Andrew’s spinach. His ask rises to $4.25 and the quantity drops to 0, then returns. Bottom: The buyer will buy all or none if the price isn’t $4.
// | Direction. Show a vertical demand curve, then a horizontal one, each labeled.
// | Cues. 5.a → the first paragraph. 5.b → the second.
// /plass:comment

There are two extreme cases. If buyers would buy exactly the same amount no matter the price, the demand curve is vertical. Quantity doesn’t respond at all, so the elasticity is 0. We call this perfectly inelastic.~Think of Gary’s EpiPen. He’s allergic to peanuts, and he buys one two-pack a year, whatever it costs.

At the other extreme, if buyers would buy any amount at one price but nothing at all if the price rose even a little, the demand curve is horizontal. We call this perfectly elastic.~Think of Andrew’s spinach. Every other stand sells the same spinach at \$4. If Andrew asks \$4.25, nobody buys from him.

=== 6 | Sellers

// plass:comment
// | Beats, as built.
// | 6.a · Title: Elasticity. Subtitle: Responsiveness to change. The spinach supply curve at 40 and $4. Bottom: Price Elasticity of Supply measures how quantity supplied responds to price.
// | 6.b · The price rises to $5; the $4 choice stays in gray. Changes: ΔP = 1, ΔQs = 20.
// | 6.c · The same calculation as step 4, price first: P-bar 4.5, Q-bar 50, the two percentage bars, then the division. Result 1.8, positive. Bottom: The sign gives direction; the magnitude measures responsiveness.
// | 6.d · The same $1 interval slides up the curve: supply stays elastic.
// | 6.e · At higher prices the two percentages approach each other. Bottom: This supply curve stays elastic; elasticity approaches 1 as price rises.
// | Editor. The seller bars from the Sep 27 plan (bars at 6.a, “20 more sellers” at 6.b) are not built; the screen shows the curve and the two points. “Molly and Andrew grow more, and a few new farmers bring their spinach to market” has no mark on screen. 6.d and 6.e have no line in the script; they can play under the last sentence, or come out of the animation.
// | Cues. 6.a → “Everything we just did for buyers…”. 6.b → “Go back to spinach… bring their spinach to market.” 6.c (.price, .quantity, .ratios, .result) → “The price rises 22%… The elasticity of supply is 1.8.”, price sentence first to match, swapped Oct 2. 6.d and 6.e → no line.
// /plass:comment

Everything we just did for buyers works for sellers too. The elasticity of supply measures how much the quantity supplied responds to a change in price. Since price and quantity supplied move together, it’s positive. When sellers can easily expand production, like a farmer with spare land, supply is elastic. When they can’t, like beachfront property, supply is inelastic.

Go back to spinach at \$4 and raise the price to \$5. Molly and Andrew grow more, and a few new farmers bring their spinach to market. The price rises 22%. The quantity supplied goes from 40 to 60, a change of 20 on a midpoint of 50, or 40%. The elasticity of supply is 1.8.

== Act 2 | Shifters

_The curves move without thinking about changes prices._

=== 7 | Demand

// plass:comment
// | Beats, as built.
// | 7.a · Title: Equilibrium. The spinach market at 40 and $4. Center: What if the curves move instead?
// | 7.b · Title: Shifters: Demand. Supply fades; the price moves along the fixed demand curve with the buyers’ bars in view. Bottom: A change in quantity demanded moves along the curve.
// | 7.c · The bars hold still. Gary’s bar comes forward at $6, MB in $/lb, with a check mark while the price is below it.
// | 7.d · The price crosses $6 and the check becomes a cross. He stops buying.
// | 7.e · Subtitle: Buyers place a higher value on spinach. The price holds; Gary’s MB rises from 6 to 11, on his bar and on the graph. Bottom: A change in preferences moves the curve itself.
// | 7.f · Every other buyer’s bar rises by the same amount, and the whole curve moves with them.
// | Direction. But the world is not always the same. Sometimes things change. Let’s say a new study comes out linking spinach to longer lives. Gary liked spinach before. But like nearly everyone, this new piece of information means he’s even more interested in buying spinach.
// | Direction. Show a dot sliding along the demand curve as the price moves, labeled “change in quantity demanded.” Then hold the price still and move the whole curve, labeled “change in demand.”
// | Editor. The first direction reads as script; your Oct 2 rewrite of the Gary paragraph covers it.
// | Editor. Steps 7 and 8 merged Oct 2, your rewrite. The step keeps number 7 so the beat IDs 7.x and 8.x stay readable against the animation. Seam: the second paragraph, “To understand how prices would change…”, plays under 7.c and 7.d, where Gary buys below $6 and stops above it; the words do not mention him until the next paragraph.
// | Cues. 7.a → “These examples have moved price while the curves have held still.”, with What if the curves move instead? on screen. 7.b → “When the price of spinach went from $4 to $5… We moved along the curve.” 7.c and 7.d → “To understand how prices would change…”. 7.e (.predict first) → “For example, what would happen to Gary’s demand curve…”. 7.f → “If this is a larger pattern for the whole market…”.
// /plass:comment

// plass:comment
// | Beats, as built.
// | 8.a · The shared change is named a, on the equation P = 12 + a − Q/5 and as a gold bar from the old intercept 12; the Scenarios list opens.
// | 8.b · Subtitle: A new study finds spinach is healthier than we had thought. List: More Preference, a > 0. The curve shifts up by 5, the original left in gray. Bottom: A change in demand shifts the whole curve. Every scenario pauses for a prediction before its shift.
// | 8.c · Bottom: More at the same price; a higher willingness to pay for the same quantity. The same change is read on each buyer’s bar and on Gary.
// | 8.d · Subtitle: Buyers become less interested in spinach. a < 0; the curve shifts down by 3. Bottom: Less demand: less is wanted at every price.
// | 8.e · Subtitle: Incomes rise; spinach is a normal good. List: More Income: Normal, a > 0. Bottom: Normal goods: higher income increases demand.
// | 8.f · Subtitle: Incomes rise; instant noodles are an inferior good. The schematic reused for noodles, a < 0. Bottom: Inferior goods: higher income decreases demand.
// | 8.g · Subtitle: The price of romaine rises. List: Pricier Substitutes, a > 0. Bottom: Substitutes can take each other’s place.
// | 8.h · Subtitle: The price of salad dressing rises. a < 0. Bottom: Complements are used together.
// | 8.i · Subtitle: The number of identical buyers increases by 25%. List: More Buyers, c down. The quantities scale and the intercept stays. Bottom: More buyers increase quantity demanded at each price.
// | Direction. What does this do to the model? Well, nothing has changed about costs or the number of sellers, so the supply curve is exactly the same. But because spinach is now known to be healthier than we thought, buyers want spinach more. This means buyers are more willing to buy spinach. Buyers are willing to pay more for the same quantity and are willing to buy more at the same price. This means the demand curve shifts up.
// | Editor. The direction reads as script and is 8.c’s caption in your words. This frame moved up under the 7.x frame on Oct 2 so the prose runs from Gary’s paragraph into “The reverse is also true”.
// | Editor. The buyers and sellers cases flatten the curve on screen rather than shifting it, so neither in/out nor up/down matches that picture.
// | Cues. 8.a to 8.c → no line: the screen names a, shifts by 5 for the health study, and reads the change on the bars; the last sentence of the Gary paragraph can stretch here. 8.d → “The reverse is also true…”. 8.e → “Preferences aren’t the only thing…”. 8.f → “Not every good works this way…”. 8.g → “Demand also depends on the prices of other goods…”. 8.h → “Other goods are used together…”. 8.i → “And just like adding sellers…”. Each of 8.b and 8.d to 8.i has a .predict pause: the subtitle is up and the curve has not moved, a place to ask before answering.
// /plass:comment

These examples have moved price while the curves have held still. When the price of spinach went from \$4 to \$5, buyers didn’t get a new demand curve. We moved along the same demand curve to a new quantity demanded. 

To understand how prices would change we first have to look at why the curve would shift. A~shift in the demand curve happens when something other than the price of spinach influences how much Gary is willing to pay for spinach. If people change their willingness to pay, the whole curve moves, what we call a shift in Demand.~

For example, what would happen to Gary’s demand curve if he learns that spinach has more health benefits than he had thought? It’s better for his health, which is one of the reasons he likes spinach, so he’s willing to pay more for it. If he was willing to pay \$4 for a pound of spinach, he’s now willing to pay more than \$4. If this is a larger pattern for the whole market of buyers, all their marginal benefits shift up, shifting up the demand curve.~

The reverse is also true. If buyers begin to prefer spinach less, the demand curve will shift down.

Preferences aren’t the only thing that shifts demand. What if Gary gets a raise? For most goods, and spinach is probably one of them, more income means he’s willing to buy more at every price. The demand curve shifts up. We call these normal goods.

Not every good works this way. When Gary’s income goes up, he might buy fewer packs of instant noodles, since he can now afford something he likes better. For these goods, more income shifts demand down. We call these inferior goods.

Demand also depends on the prices of other goods. Romaine lettuce and spinach can both make a salad. If the price of romaine goes up, some buyers switch to spinach, and the demand for spinach shifts up. Goods like these, where one can stand in for the other, are substitutes.

Other goods are used together. If the price of salad dressing goes up, buyers make fewer salads, and they want less spinach at every price. The demand for spinach shifts down. Goods like these are complements.

And just like adding sellers shifts supply down, adding buyers shifts demand up. Every new buyer in the market adds to the quantity demanded at every price.

=== 9 | Supply

// plass:comment
// | Beats, as built.
// | 9.a · Title: Shifters: Supply. Subtitle: The price of spinach rises from $4 to $5. The price moves along the fixed supply curve with the sellers’ bars in view. Bottom: A change in quantity supplied moves along the curve.
// | 9.a1 · Subtitle: At a price of $4, Molly is willing to supply her next unit. Her bar comes forward at a cost of 3, MC in $/lb.
// | 9.b · Subtitle: Farmland becomes more expensive. b is named on P = 2 + b + Q/20 with its gold bar, and the Scenarios list opens: Higher Input Costs, b > 0. Her cost rises on her bar and on the curve; at $4 fewer lots pay. Bottom: A change in supply shifts the whole curve. Every scenario pauses for a prediction before its shift.
// | 9.c · Subtitle: Fertilizer becomes cheaper. b < 0; each marginal cost falls.
// | 9.d · Subtitle: The price of carrots rises. List: Better Alternatives, b > 0.
// | 9.e · Subtitle: Better technology lowers the cost of growing spinach. b < 0. Bottom: Lower costs increase supply at every price.
// | 9.f · Subtitle: The number of identical sellers increases by 25%. List: More Sellers, d down. Bottom: More sellers increase quantity supplied at each price.
// | Editor. The technology paragraph moves ahead of the sellers paragraph to match 9.e and 9.f, and the bridge sentence “The changes in the costs of production…” now sits between them, closing the cost cases and opening the sellers case. The rest of that paragraph, a repeat of the farmland case, was cut Oct 2.
// | Cues. 9.a → “The same ideas hold for sellers…”. 9.a1 → “Molly’s Individual Supply Curve depends on the costs of producing spinach.” 9.b (.predict first) → the rest of that paragraph, farmland. 9.c → fertilizer. 9.d → carrots. 9.e → technology. Between 9.e and 9.f → “The changes in the costs of production…”. 9.f → “The market supply curve is also impacted by the number of sellers…”. Each of 9.b to 9.f has a .predict pause before its shift.
// | Editor. Heading changed Oct 2 from “Shifters: Supply” to “Supply”, matching “Demand” in step 7.
// /plass:comment

The same ideas hold for sellers. When the price of spinach rose to \$5, Molly moved along her supply curve. That’s a change in the quantity supplied. Anything else that changes her costs shifts the whole curve. That’s a change in supply.

Molly’s _*Individual Supply Curve*_ depends on the costs of producing spinach. For example, what would happen if the price of renting farmland increased? Her supply curve would also shift up! The cost of each additional unit of spinach becomes more expensive since the input, land, has also become more expensive. This means that, for example, she wouldn’t be willing to produce as much spinach as before at a price of \$4 or any price.

What would happen if she had to pay less for her organic fertilizer? Each additional unit of spinach would become less costly to produce. Molly would be willing to make _more_ spinach than before at a price of \$4 or any price.

What would happen if the price of carrots were to increase? Molly would have a higher opportunity cost of switching her farmland away from carrots to spinach, so the cost of production would also go up!

Technology works like a cheaper input. If a new harvesting machine lets Molly pick her spinach in fewer hours, each additional unit costs her less to produce. She’s willing to sell more at every price, and her supply curve shifts down.

The changes in the costs of production shift the farmers’ individual supply curves, which in turn shifts the market supply curve.

The market supply curve is also impacted by the number of sellers. Like when we added Andrew’s supply to Molly’s to get the market supply curve, every time another seller opens their doors the supply curve shifts down, and when a seller drops out of the market the supply curve shifts up.

== Act 3 | Comparative Statics

_Curves move equilibrium._~

=== 10 | Comparative Statics

// plass:comment
// | Beats, as built. The screen is qualitative here: no equations, no a or b, no algebra. The Sep 27 beats 10.g and 10.h, solving for equilibrium as a function of a, came out of the animation on Sep 28.
// | 10.a · Title: Comparative Statics. Subtitle: How does the market respond to a change? The demand curve alone; the Scenarios list is empty.
// | 10.b · Demand shifts up, the original in gray.
// | 10.c · Demand shifts down, then returns.
// | 10.d · Supply appears. P* = 4, Q* = 40. Bottom: Baseline equilibrium.
// | 10.e · Subtitle: Buyers place a higher value on spinach. List: Demand increases. Demand shifts up at the fixed price: Qs = 40, Qd = 65, a bracket labeled Shortage. Bottom: Demand rises; price fixed.
// | 10.f · Bottom: Price adjusts; curves stay fixed. The price rises along both curves to P*′ = 5, Q*′ = 60. Recorded: Price rises; quantity rises.
// | 10.i · Subtitle: Income falls; spinach is a normal good. List: Demand decreases. The market resets.
// | 10.j · Demand shifts down at $4: Qs = 40, Qd = 15, Excess supply. Bottom: Demand falls; price fixed.
// | 10.k · The price falls to P*′ = 3, Q*′ = 20. Recorded: Price falls; quantity falls.
// | 10.l · Subtitle: Fertilizer becomes more expensive. List: Supply decreases. A fresh market at 40 and $4.
// | 10.m · Supply shifts up at $4: Qs = 15, Qd = 40, Shortage. Bottom: Supply falls; price fixed.
// | 10.n · The price rises to P*′ = 5, Q*′ = 35. Recorded: Price rises; quantity falls.
// | 10.o · Subtitle: Fertilizer becomes cheaper. List: Supply increases. Reset.
// | 10.p · Supply shifts down at $4: Qs = 65, Qd = 40, Excess supply. Bottom: Supply rises; price fixed.
// | 10.q · The price falls to P*′ = 3, Q*′ = 45. Recorded: Price falls; quantity rises. Bottom: Comparative statics compares equilibrium before and after a change.
// | Direction. Introduce a shock parameter a into the equations. Show what happens to the demand curve when a shifts up and shifts down. Then fade in the supply curve and show the shifts on the market without changing price. The parameter is not built here; it was named in steps 8 and 9.
// | Moved into the body Oct 2: the shortage direction, your words, as the narration for 10.e and 10.f.
// | Direction. Do the math for this. Show the change in price and change in quantity. Not built.
// | Direction. Then do a supply shifter with a parameter b on a separate graph with a different price and quantity from the first example. Built on its own graph, but the same market at 40 and $4.
// | Editor. This is the act that ran short in class. The first scenario is now narrated by your shortage paragraph, with a one-sentence {++ ++} lead-in naming the study. The three {++ ++} paragraphs after the questions are proposals, written to the screen captions, so each scenario has an answer; the last one covers the fourth scenario and the definition at 10.q.
// | Editor. What the screen shows with no line to say it: the definition at 10.q; the four results in the list; excess supply and the falling price at 10.j and 10.k; and the fourth scenario, cheaper fertilizer, at 10.o to 10.q.
// | Cut Oct 2, at your request: “Let’s say Income goes up. What happens to equilibrium Price and Quantity?” The screen does income falling only.
// | Cues. 10.a to 10.c → “We just talked about shifters…”. 10.d → “And on the other side of the market…” and “These changes impact the equilibrium…”. 10.e.setup, 10.e, 10.f → “Start with the spinach study… This will raise P* and raise Q*.” 10.i to 10.k → “What happens to equilibrium when Income goes down?” and the proposed answer. 10.l to 10.n → “What about with an increase in the cost of fertilizer…” and the proposed answer. 10.o to 10.q → the proposed “And if fertilizer gets cheaper instead…”.
// /plass:comment

We just talked about shifters. When forces that impact Buyers’ preferences for spinach change, so does the Demand curve.

And on the other side of the market, when sellers’ opportunity costs change, so does the supply curve.

These changes impact the equilibrium through change in Supply and Demand.

{++Start with the spinach study. Buyers place a higher value on spinach, so demand shifts up.++} At the initial equilibrium price, we now have a shortage because buyers now want more. Sellers are all sold out since buyers want more and both buyers and sellers have incentives to raise the price. This takes us back to equilibrium analysis. Because there’s a shortage, prices will rise until there is no shortage. This might not happen over night. But it’s the direction that the market will go. This will raise #mi(`P^\ast`) and raise #mi(`Q^\ast`).

What happens to equilibrium when Income goes down?

{++Spinach is a normal good, so demand shifts down. At \$4 there is now excess supply, so the price falls, and the quantity falls with it.++}

What about with an increase in the cost of fertilizer, an input to producing spinach?

{++Supply shifts up. At \$4 there is a shortage, so the price rises, and this time the quantity falls.++}

{++And if fertilizer gets cheaper instead, supply shifts down, there is excess supply at \$4, and the price falls while the quantity rises. Comparative statics is this comparison: the equilibrium before a change against the equilibrium after it.++}

=== 11 | Both Curves Shift

// plass:comment
// | Beats, as built.
// | 11.a · Title: Comparative Statics. Subtitle: Demand and supply both increase. The market at 40 and $4, with the causes beside it: Romaine costs more; Harvesting costs less. A record with columns Price and Quantity. Note: Same starting market; three possible outcomes. Bottom: What if demand and supply both increase?
// | 11.b · Demand shifts up by 5 and supply shifts down a little. Recorded: price Rises, quantity Rises.
// | 11.c · The same demand shift with a larger supply shift. Recorded: price Unchanged, quantity Rises.
// | 11.d · A still larger supply shift. Recorded: price Falls, quantity Rises. Bottom: Indeterminate: the direction depends on the relative sizes of the shifts.
// | Cues. 11.a → “Now what about when the price of romaine…”. 11.b to 11.d → “This leads to an increase…” and “Prices are indeterminate…”.
// /plass:comment

Now what about when the price of romaine lettuce goes up while the price of spinach harvesting technology goes down at the same time?

This leads to an _increase_ in the equilibrium quantity and an _indeterminate_ change in price.

Prices are _indeterminate_ because the shift in demand raises prices, while the shift in supply lowers prices, and we don’t know the magnitude of the shifts.

=== 12 | How Much Price, How Much Quantity

// plass:comment
// | Beats, as built.
// | 12.a · Title: Comparative Statics. Subtitle: The same demand increase meets different supply responses. Two identical graphs through 40 and $4: More elastic supply on the left, Less elastic supply on the right. Bottom: How much changes in price, and how much in quantity?
// | 12.b · Demand shifts up by the same amount on both and the equilibria move. Left: Small price rise; large quantity rise. Right: Large price rise; small quantity rise. Bottom: Elasticity helps explain how a shift changes price and quantity.
// | Direction. Ok, but will prices always respond like this? No. It turns out if the slopes were different, the response would be different. Pivot the S&D curves around equilibrium.
// | Direction. The slope is related to how the S or D curves respond to a change in price. But simply looking at the slope itself gives us the wrong picture.
// | Direction. Show two graphs side by side. Left: the B3 supply curve. Right: a steep supply curve through the same equilibrium, 40 and $4. Shift demand up by the same amount on both.
// | Editor. The first two directions were the old bridge into elasticity, from when elasticity came last. The first reads as script and could open the step. The second is answered in step 3 now.
// | Editor. The numbers in the script, $1 and 20 against $4 and 5, are not printed on screen; the captions are the two sentences quoted at 12.b.
// | Cues. 12.a → “Let’s put the two ideas together…”. 12.b → “On the left… On the right…” and “Same shift, very different outcomes…”. 12.c → the last sentence, with Elasticity helps explain how a shift changes price and quantity on screen.
// /plass:comment

Let’s put the two ideas together. Here’s the same spinach study, and the same shift in demand, against two different supply curves.

On the left, sellers can respond easily. The price rises only \$1, to \$5, and the quantity rises by 20, to 60. On the right, sellers can’t easily respond. The price rises \$4, to \$8, and the quantity rises by only 5, to 45.

Same shift, very different outcomes. When supply is elastic, a shift in demand mostly changes the quantity. When supply is inelastic, it mostly changes the price.

=== Closing

// plass:comment
// | Beats, as built.
// | 13.a · Title: Comparative Statics. Subtitle: How markets respond to change. Bottom: How do markets respond to change?
// | 13.b · Bottom: Next time: international trade.
// | Cues. 13.a → the paragraph. 13.b → “Next time we take these tools across the border…”.
// /plass:comment

Markets respond to change. Elasticity tells us how much buyers and sellers respond when the price moves. When preferences, incomes, or costs change, the curves shift, and the equilibrium moves to a new price and quantity. And elasticity tells us how that change splits between price and quantity. Next time we take these tools across the border, to international trade.

// plass:comment
// | Editor. Numbers, checked Sep 27 and updated Oct 2 to the built animation. Spinach is the B3 market throughout: demand P = 12 - Q/5 (Q = 60 - 5P), supply P = 2 + Q/20 (Q = 20P - 40), equilibrium 40 at $4. Q is in thousands of pounds.
// | 
// | Step 2, the hook. Chocolate demand P = 6 - Q/20 (Q = 120 - 20P), Q in thousands of bars. Spinach axes: P to 12, Q to 60. Chocolate axes: P to 6, Q to 120. Both lines run corner to corner.
// | Both at 40 and $4, price to $5, midpoint method. %ΔP = 1/4.5 = 22.2% in both.
// | Spinach: Q 40 to 35, 5 lots out. %ΔQ = -5/37.5 = -13.3%. Elasticity -0.6. Inelastic.
// | Chocolate: Q 40 to 20, 20 lots out. %ΔQ = -20/30 = -66.7%. Elasticity -3. Elastic.
// | The spinach dot is at 1/3 of the line’s height ($4 of $12); the chocolate dot at 2/3 ($4 of $6). On the spinach line, 2/3 of the height is $8, and $8 to $10 there also gives -3, the chocolate number.
// | Gary’s MB $6 (B3) stays in at $5.
// | 
// | Steps 3 and 4, elasticity of spinach demand, midpoint method, price up $1 in both:
// | Example 1: $10 to $11, Q from 10 to 5. %ΔQ = -5/7.5 = -66.7%, %ΔP = 1/10.5 = 9.5%, elasticity -7. Elastic.
// | Example 2: $1 to $2, Q from 55 to 50. %ΔQ = -5/52.5 = -9.5%, %ΔP = 1/1.5 = 66.7%, elasticity -1/7, about -0.14. Inelastic. Reciprocal of example 1.
// | Example 3, cut Sep 27: $2 to $3, Q from 50 to 45, elasticity -5/19, about -0.26.
// | Unit elastic at $6 and 30, the middle of the line. Elastic above $6, inelastic below.
// | 
// | Step 6, spinach supply, $4 to $5: Q from 40 to 60. %ΔQ = 20/50 = 40%, %ΔP = 22.2%, elasticity 1.8.
// | 
// | Demand shift a: demand P = 12 + a - Q/5. New equilibrium P = 4 + a/5, Q = 40 + 4a.
// | Spinach study, a = 5: demand P = 17 - Q/5, equilibrium 60 at $5. At the old $4, quantity demanded 65 and quantity supplied 40, a shortage of 25.
// | Income goes down, a = -5: demand P = 7 - Q/5, equilibrium 20 at $3. At the old $4, quantity demanded 15 and quantity supplied 40, an excess of 25.
// | 
// | Supply shift b: supply P = 2 + b + Q/20. New equilibrium P = 4 + 4b/5, Q = 40 - 4b.
// | Fertilizer costs more, b = 1.25: supply P = 3.25 + Q/20, equilibrium 35 at $5. At the old $4, quantity supplied 15 and quantity demanded 40, a shortage of 25.
// | Fertilizer costs less, b = -1.25: supply P = 0.75 + Q/20, equilibrium 45 at $3. At the old $4, quantity supplied 65 and quantity demanded 40, an excess of 25.
// | 
// | Both shift: P = 4 + a/5 + 4b/5, Q = 40 + 4a - 4b. Romaine up, a = 5, with better technology, b negative:
// | b = -0.625: 62.5 at $4.50. b = -1.25: 65 at $4, price unchanged. b = -2.5: 70 at $3. Quantity rises in all three; price can go either way.
// | 
// | Step 12, the same a = 5 against two supply curves through 40 and $4:
// | B3 supply P = 2 + Q/20: new equilibrium 60 at $5. Price up 1, quantity up 20. Supply elasticity between the two points (midpoint) 1.8.
// | Steep supply P = 0.8Q - 28: new equilibrium 45 at $8. Price up 4, quantity up 5. Supply elasticity between the two points (midpoint) 0.18.
// /plass:comment
