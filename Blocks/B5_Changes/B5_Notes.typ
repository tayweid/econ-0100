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

== Episode B5 | Comparative Statics and Elasticity

_Markets will adapt to change in costs and preferences according to the responsiveness of supply and demand._

_How prices change._

// plass:comment
// | Beats for B5_Animation.py, scene B5. Topic titles orient each section; questions serve as prompts. Gold bars measure shifts; side lists retain the scenarios.
// | 0.a · Bumper: How prices change.
// | These comments outline the screen action. The animation code holds the choreography.
// /plass:comment

// plass:comment
// | Editor, Sep 27. Every line in the steps is yours, moved from 01_Notes.md (now _archive/01_Notes_2026-09-16.md). The order follows your Sep 13 arc: shifters, then elasticity, then comparative statics.
// | Your animation Outline bullets are split up into the steps they direct, as direction lines.
// | Step headings, strikes, and anything in {++ ++} are proposals for you to approve.
// | Sep 27, second pass, at your request: proposed passages for each gap against the B5 skills, all in {++ ++}, plus a proposed Closing. Your approvals are applied: the new numbers, and the equal-slopes line is cut.
// | Third pass: the midpoint method throughout, and the chapter pointers are removed, both at your request.
// | The block and the course site call this episode Market Changes. You named "Changes" as a possible title earlier. Both subtitle lines are kept.
// | No Exercise B5 pause lines yet. B3 and B4 each had two.
// /plass:comment

In this video we’ll consider what happens to equilibrium price and quantity when preferences change and shift the demand curve or when costs change and shift the supply curve.

=== {++1 | What Markets Are Doing++}

// plass:comment
// | Beats
// | 1.a · The familiar market at 40 and $4.
// | 1.b · CS and PS become total surplus.
// /plass:comment

_*Start by talking about what markets are doing, that we get equilibrium price because of buyers and sellers incentives, and that under some conditions, this is very good for buyers and sellers, although not everyone.*_

// plass:comment
// | Editor. These lines opened your Comparative Statics section. They are the recap your first Outline bullet asks for, so they moved up here.
// | The struck headings are the 2024 storyboard frame cues. They point at frames that no longer exist, and it was never clear if each cue belonged to the line before it or the line after it. Proposed: drop them all, here and in step 6.
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

=== {++2 | Sometimes Things Change++}

// plass:comment
// | Beats
// | 2.a · Pick out the willingness-to-pay bar for Gary’s next unit.
// | 2.b · Bring his bar forward. The spinach study raises his valuation.
// /plass:comment

_*But the world is not always the same. Sometimes things change. Let’s say a new study comes out linking spinach to longer lives. Gary liked spinach before. But like nearly everyone, this new piece of information means he’s even more interested in buying spinach.*_

First, we’re going to show how prices and quantities, our coordination device, are impacted by forces outside the model. We’ll do this by #strike[building on] {++introducing++} the idea of *Shifters*.

// plass:comment
// | Editor. "Building on" assumed shifters were taught in B1 and B2. Under your Sep 13 arc they start here.
// /plass:comment

=== {++3 | Shifters: Demand++}

// plass:comment
// | Beats
// | 3.a · Introduce a at zero, then change price along the unchanged demand curve.
// | 3.b · The spinach study raises a. Measure the shift in gold and begin the scenario list.
// | 3.c · Read the same shift as greater willingness to pay.
// | 3.d · Less preference lowers a; retain each case in the list.
// | 3.e · Higher income increases demand for a normal good.
// | 3.f · Higher income decreases demand for an inferior good.
// | 3.g · More expensive romaine increases demand for spinach.
// | 3.h · More expensive dressing decreases demand for spinach.
// | 3.i · More identical buyers flatten market demand; show the changing slope coefficient.
// /plass:comment

// plass:comment
// | Editor. Proposed passage for B5.1's first standard: a movement along the curve versus a shift, and a change in quantity demanded versus a change in demand. No passage for this existed in B1, B2, or here.
// /plass:comment

{++Before we look at what changes the demand curve, let’s be careful about what doesn’t. When the price of spinach changes, Gary doesn’t get a new demand curve. He moves along the one he already has. At \$4 he buys a little, and at \$3 he buys a bit more. We call this a change in the quantity demanded.++}

{++A shift is different. Something other than the price of spinach changes, and now Gary wants a different amount at every price. We call this a change in demand. The whole curve moves.++}

_*{++Show a dot sliding along the demand curve as the price moves, labeled “change in quantity demanded.” Then hold the price still and move the whole curve, labeled “change in demand.”++}*_

_*What does this do to the model? Well, nothing has changed about costs or the number of sellers, so the supply curve is exactly the same. But because spinach is now known to be healthier than we thought, buyers want spinach more. This means buyers are more willing to buy spinach. Buyers are willing to pay more for the same quantity and are willing to buy more at the same price. This means the demand curve shifts up.*_

What would happen to Gary’s demand curve if he learns that spinach has more health benefits than he had thought. He’d be more willing to pay for spinach at every quantity or alternatively, he would be willing to buy more spinach at every price. Either way you think of it, his demand curve shifts out.

Gary isn’t the only one who realizes spinach has more health benefits than previously thought. It turns out everyone in the market now prefers spinach more than they had. This shifts the demand curve out.

Everyone is willing to buy more spinach at every price or alternatively everyone is willing to pay more for spinach at every quantity. The reverse is also true. If buyers begin to prefer spinach less, the demand curve will shift in.

// plass:comment
// | Editor. Proposed passages below for B5.1's second standard: income (normal and inferior goods), substitutes and complements, and the number of buyers. Step 6 asks about income and step 7 about romaine lettuce, so these set both up. Your Tutorial 2.5 bullets in B_Outline.typ list "Complements/Substitutes" and "Inferior/Normal/Lux".
// /plass:comment

{++Preferences aren’t the only thing that shifts demand. What if Gary gets a raise? For most goods, and spinach is probably one of them, more income means he’s willing to buy more at every price. The demand curve shifts out. We call these normal goods.++}

{++Not every good works this way. When Gary’s income goes up, he might buy fewer packs of instant noodles, since he can now afford something he likes better. For these goods, more income shifts demand in. We call these inferior goods.++}

{++Demand also depends on the prices of other goods. Romaine lettuce and spinach can both make a salad. If the price of romaine goes up, some buyers switch to spinach, and the demand for spinach shifts out. Goods like these, where one can stand in for the other, are substitutes.++}

{++Other goods are used together. If the price of salad dressing goes up, buyers make fewer salads, and they want less spinach at every price. The demand for spinach shifts in. Goods like these are complements.++}

{++And just like adding sellers shifts supply out, adding buyers shifts demand out. Every new buyer in the market adds to the quantity demanded at every price.++}

=== {++4 | Shifters: Supply++}

// plass:comment
// | Beats
// | 4.a · Introduce b at zero, then change price along the unchanged supply curve.
// | 4.b · Molly’s costs raise b. Measure the shift in gold and begin the supply list.
// | 4.c · Cheaper fertilizer lowers costs and increases supply.
// | 4.d · More valuable carrots raise the opportunity cost of spinach.
// | 4.e · More identical sellers flatten market supply; show the changing slope coefficient.
// | 4.f · Better harvesting technology lowers costs and increases supply.
// /plass:comment

{++The same distinction holds for sellers. A change in the price of spinach moves Molly along her supply curve. That’s a change in the quantity supplied. Anything else that changes her costs shifts the whole curve. That’s a change in supply.++}

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
// | Editor. Proposed passage for B5.1's third standard: technology. Step 7 uses harvesting technology.
// /plass:comment

{++Technology works like a cheaper input. If a new harvesting machine lets Molly pick her spinach in fewer hours, each additional unit costs her less to produce. She’s willing to sell more at every price, and her supply curve shifts down and out.++}

=== {++5 |++} Elasticity

// plass:comment
// | Beats
// | 5.a · Show the same demand curve twice, selecting a high-price and a low-price interval.
// | 5.b · Cut each price by $1; both quantities rise by 5, but only the first doubles.
// | 5.c · Introduce elasticity as responsiveness in percentage terms.
// | 5.d · On the first graph, measure the quantity change and its midpoint base.
// | 5.e · Measure the price change and its midpoint base in the same way.
// | 5.f · Turn the measurements into percentage bars on a shared scale.
// | 5.g · Find elasticity of −7; distinguish its sign from its responsiveness.
// | 5.h · Move to the second interval; the same changes give elasticity of −1/7.
// | 5.i · Try $3 to $2; elasticity is −5/19.
// | 5.j · Stop at the unit-elastic midpoint: equal percentage changes in magnitude.
// | 5.k · Label the elastic and inelastic regions while the slope stays constant.
// | 5.l · Move price along vertical demand: quantity does not respond.
// | 5.m · On perfectly elastic demand, quantity can change at the same price.
// | 5.n · Raise price along supply and follow the quantity supplied.
// | 5.o · Use the same percentage ratio to calculate positive supply elasticity.
// /plass:comment

_How should we measure the responsiveness of the demand curve?_

// plass:comment
// | Editor. Your arc puts elasticity here, where the curve stays put and only the price moves.
// /plass:comment

The animation I have in mind follows this basic outline.

Let’s do two examples#strike[ of comparative statics], one where we decrease the price by y but quantity is very low, and one where we decrease the price by y but the quantity is very high.

_*Show the two models side by side, animating the changes and fading out the supply curve, so all we see is the demand curve and the price and quantity changes.*_

_*Use the B3 demand curve P = 12 - Q/5, where Q is in thousands of pounds of spinach. Then use the prices of 11 and 10 for the first example, with quantities of 5 and 10, and prices of 2 and 1 for the second example with quantities of 50 and 55. Maybe do a third example to show that they aren’t always reciprocal, using prices of 3 and 2, with quantities of 45 and 50.*_

// plass:comment
// | Editor. New numbers, approved Sep 27. Your lines below still hold: both quantities change by 5, the first doubles, and the second rises 10 percent. With the midpoint method the first two examples are reciprocal (-7 and -1/7) and the third is not (-5/19). Full numbers are at the end.
// /plass:comment

Which change in quantity is larger?

Well in one way, the quantities have changed by exactly the same amount. We’ve shifted the price by the same amount, and because the slope is the same, the absolute change in the quantity is exactly equal.

But the first example doubled the quantity. Has the second? No! It has gone up, but by well less than half.

So if we’re interested in measuring how buyers respond to changes in the market, how might we measure changes? Do you think it’s appropriate to use the absolute changes?

Probably not. These two examples show that absolute changes don’t tell the full story. We would say the first example is _*very responsive*_ while the second example is _*not very responsive*_. The word we use for this idea is _*elasticity*_. The first example is _*elastic*_ and the second example is _*inelastic*_.

We have a way of calculating these things with the _*elasticity of demand*_.

#mitex(`
\epsilon_D = \frac{\%\Delta Q_b}{\%\Delta P} = \frac{\frac{Q_b' - Q_b}{\bar{Q_b}}}{\frac{P' - P}{\bar{P}}}
`)

// plass:comment
// | Editor. The Markdown version wrote the primes as backticks, which can't sit inside #mitex. They are primes here.
// | Your formula is the midpoint method, which you chose on Sep 27. The proposals after the next line name it and work your first two examples with it.
// /plass:comment

We use the quantity on top because we’re essentially asking how the quantity responds to a change in price. So a larger number is more responsive.

{++This is called the midpoint method. We divide each change by the midpoint of the two values, halfway between where we started and where we ended. That way we get the same answer whether the price goes up or down.++}

{++Let’s try it on our first example. Quantity goes from 5 to 10, a change of 5. The midpoint is 7.5, so quantity changes by 5 divided by 7.5, about 67%. Price goes from \$11 to \$10, a change of −1. The midpoint is 10.5, so price changes by −1 divided by 10.5, about −9.5%. The elasticity is 67% divided by −9.5%, which is −7.++}

{++In the second example, quantity goes from 50 to 55, a change of 5 on a midpoint of 52.5, about 9.5%. Price goes from \$2 to \$1, a change of −1 on a midpoint of 1.5, about −67%. The elasticity is 9.5% divided by −67%, about −0.14.++}

_*Elasticity visualization: use a horizontal line composed of two parts, the change part and the base part. This could show the idea that elasticity is a way of measuring the responsiveness and not just the slope. I’m thinking about a visual like grant’s bayes video. *_#strike[_*The elasticity measure could be slighly different than the midpoint method, using the smaller of the two values instead of the middle of the two values.*_]_* Then visualize the horizontal axis with a horizontal line in the elasticty fraction and the vertical in the elasticity fraction. Then have both up and down different colors and the changes part be a more vibrant color and the base be a muted color. Then move the base around moving the lines in the fraction. Then fade in the numbers, adding the number beside the bars in the SD graph and in the elasticity equation. Then show the elasticity number itself by the fraction. Then move it around. Then color the regions where it’s elastic, and inelastic and fade in a bracket labeling each region.*_

// plass:comment
// | Editor. Moved from Bx_Elasticity.typ, now archived at _archive/Bx_Elasticity.typ. The struck sentence is the smaller-base idea, proposed as a cut now that you've chosen the midpoint method. The base bar would then show the midpoint.
// | Proposed passages below for the rest of B5.2: elastic, inelastic, and unit elastic; elasticity changing along a straight line while the slope stays constant; perfectly elastic and perfectly inelastic; elasticity of supply.
// /plass:comment

{++Demand elasticity is negative, since price and quantity demanded move in opposite directions, so we look at its size. When the size is bigger than 1, quantity changes by more than price, in percentage terms. We call that elastic. When it’s smaller than 1, quantity changes by less than price. We call that inelastic. And when it’s exactly 1, we call it unit elastic.++}

{++Notice something about our two examples. They came from the same demand curve, with the same slope everywhere. But the first was elastic and the second was inelastic. Along a straight-line demand curve, the slope stays the same while the elasticity changes. Near the top, where the price is high and the quantity is small, demand is elastic. Near the bottom, it’s inelastic. And in the middle, at \$6, it’s unit elastic.++}

{++There are two extreme cases. If buyers would buy exactly the same amount no matter the price, the demand curve is vertical. Quantity doesn’t respond at all, so the elasticity is 0. We call this perfectly inelastic. Think of a life-saving medicine with no substitute.++}

{++At the other extreme, if buyers would buy any amount at one price but nothing at all if the price rose even a little, the demand curve is horizontal. We call this perfectly elastic. Think of one farmer’s spinach at a market full of identical spinach.++}

_*{++Show a vertical demand curve, then a horizontal one, each labeled.++}*_

{++Everything we just did for buyers works for sellers too. The elasticity of supply measures how much the quantity supplied responds to a change in price. Since price and quantity supplied move together, it’s positive. When sellers can easily expand production, like a farmer with spare land, supply is elastic. When they can’t, like beachfront property, supply is inelastic.++}

=== {++6 |++} Comparative Statics

// plass:comment
// | Beats
// | 6.a · Revisit a and its gold shift measure beside the market.
// | 6.b · Raise demand while keeping the original curve visible.
// | 6.c · Lower demand, then restore the original curve.
// | 6.d · Add supply at 40 and $4; begin the comparative-statics case list.
// | 6.e · Raise demand at the old price and show the shortage of 25.
// | 6.f · Raise price along the fixed curves; record the new equilibrium.
// | 6.g · Solve for equilibrium as a function of the demand shift.
// | 6.h · Substitute the demand increase and recover 60 at $5.
// | 6.i · Restore the original market before considering falling income.
// | 6.j · Lower demand at the old price and show excess supply of 25.
// | 6.k · Lower price; record 20 at $3 in the case list.
// | 6.l · Restore the baseline and revisit b while keeping the case list.
// | 6.m · Raise fertilizer costs at the old price and show the shortage.
// | 6.n · Raise price; record 35 at $5 with all three outcomes in view.
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

=== {++7 | Both Curves Shift++}

// plass:comment
// | Beats
// | 7.a · Set up both changes; compare three possible outcomes with one baseline.
// | 7.b · Increase demand and supply; record rising quantity and price.
// | 7.c · Increase supply further; add rising quantity with unchanged price.
// | 7.d · Increase supply again; add rising quantity with falling price.
// /plass:comment

Now what about when the price of romaine lettuce goes up while the price of spinach harvesting technology goes down at the same time?

==== #strike[B3]

This leads to an _increase_ in the equilibrium quantity and an _indeterminate_ change in price.

Prices are _indeterminate_ because the shift in demand raises prices, while the shift in supply lowers prices, and we don’t know the magnitude of the shifts.

==== #strike[B3]

=== {++8 | How Much Price, How Much Quantity++}

// plass:comment
// | Beats
// | 8.a · Compare supply responses on identical graphs through the same equilibrium.
// | 8.b · Shift demand equally in both markets and follow the equilibria.
// | 8.c · Compare the resulting price and quantity changes.
// /plass:comment

_*Ok, but will prices always respond like this? No. It turns out if the slopes were different, the response would be different. Pivot the S&D curves around equilibrium.*_

_*The slope is related to how the S or D curves respond to a change in price. But simply looking at the slope itself gives us the wrong picture.*_

// plass:comment
// | Editor. These were the last two Outline bullets, your old bridge into elasticity. Now that elasticity comes first, they fit here as the close. They could also open step 5 instead.
// | Proposed passage below for the last B5.3 standard: the same demand shift moves mostly price when supply is inelastic and mostly quantity when it is elastic.
// /plass:comment

{++Let’s put the two ideas together. Here’s the same spinach study, and the same shift in demand, against two different supply curves.++}

_*{++Show two graphs side by side. Left: the B3 supply curve. Right: a steep supply curve through the same equilibrium, 40 and \$4. Shift demand up by the same amount on both.++}*_

{++On the left, sellers can respond easily. The price rises only \$1, to \$5, and the quantity rises by 20, to 60. On the right, sellers can’t easily respond. The price rises \$4, to \$8, and the quantity rises by only 5, to 45.++}

{++Same shift, very different outcomes. When supply is elastic, a shift in demand mostly changes the quantity. When supply is inelastic, it mostly changes the price.++}

=== {++Closing++}

// plass:comment
// | Beats
// | 9.a · Hold the paired markets to recap how they respond to change.
// | 9.b · Introduce the next block: international trade.
// /plass:comment

{++Markets respond to change. When preferences, incomes, or costs change, the curves shift, and the equilibrium moves to a new price and quantity. Elasticity tells us how that change splits between price and quantity. Next time we take these tools across the border, to international trade.++}

=== {++Parked++}

==== {++Exercise candidate: Toffees++}

// plass:comment
// | Editor. Moved into the B5 notes from B3_Equilibrium/_Unplaced.md on Sep 16. It turns on a subsidy, which Part B doesn't teach (C2 does). It works here if the shifter becomes "production got cheaper"; otherwise hold it for Part C.
// /plass:comment

Due to longstanding tradition, all toffees are made the same way, anyone could easily start making them, and the number of toffee makers had been constant over the past couple of years. This changed when the Ministry imposed a subsidy on all toffee sales. Using a couple of graphs to illustrate your answer, explain what happened in the market because of this subsidy.

// plass:comment
// | Editor. Numbers, checked Sep 27. The B3 market throughout: demand P = 12 - Q/5 (Q = 60 - 5P), supply P = 2 + Q/20 (Q = 20P - 40), equilibrium 40 at $4. Q is in thousands of pounds.
// | 
// | Elasticity of demand, midpoint method:
// | Example 1: $11 to $10, Q from 5 to 10. %ΔQ = 5/7.5 = 66.7%, %ΔP = -1/10.5 = -9.5%, elasticity -7. Elastic.
// | Example 2: $2 to $1, Q from 50 to 55. %ΔQ = 5/52.5 = 9.5%, %ΔP = -1/1.5 = -66.7%, elasticity -1/7, about -0.14. Inelastic. Reciprocal of example 1.
// | Example 3: $3 to $2, Q from 45 to 50. %ΔQ = 5/47.5 = 10.5%, %ΔP = -1/2.5 = -40%, elasticity -5/19, about -0.26. Not the reciprocal of example 1.
// | Unit elastic at $6 and 30, the middle of the line. Elastic above $6, inelastic below.
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
// | Step 8, the same a = 5 against two supply curves through 40 and $4:
// | B3 supply P = 2 + Q/20: new equilibrium 60 at $5. Price up 1, quantity up 20. Supply elasticity between the two points (midpoint) 1.8.
// | Steep supply P = 0.8Q - 28: new equilibrium 45 at $8. Price up 4, quantity up 5. Supply elasticity between the two points (midpoint) 0.18.
// /plass:comment
