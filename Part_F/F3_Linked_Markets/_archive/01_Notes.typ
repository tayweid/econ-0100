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

== Episode F2 | Demand

This video introduces the individual’s constrained optimization decision intuitively and how it gives us demand.

So we have a model for preferences and constraints. Demand is the two together.

== Animation | Income and Quantity

How would a change in income influence the individual demand curves?

When \$ Y = 120 \$, the optimal bundle has \$ q\_a^\* = 60 \$ and \$ q\_b^\* = 30 \$. Shifting income inward to \$ Y = 80 \$, our new optimal bundle shifts in to \$ q\_a^\* = 40 \$ and \$ q\_b^\* = 20 \$, placing us on a lower indifference curve. This makes sense with our intuition, that a lower income means we won’t be able to reach the original bundle.

Increasing income to \$ Y = 180 \$, our optimal bundles shift out to \$ q\_a^\* = 90 \$ and \$ q\_b^\* = 45 \$. Again, with an increase in income we are able to acheive a higher bundle and a higher indifference curve, matching our intuition.

We can look at a range of income levels, mapping out the relationship between \$ Y \$ and our optimal bundles. And a side note here. This isn’t the relationship between just any bundle and income. Its the relationship between income and the optimal bundle, after we’ve done our optimizing. This relationship is what we call the *Income-Consumption Path*, the path denoting the optimal bundles of goods as income increases, holding prices constant.

What does the income compensation path curve tell us? Both \$ q\_a \$ and \$ q\_b \$ increase in response to an increase in income. There’s another way to set this up as a relationship between income and quantity demanded, called the “Engle Curve”, the relationship between income and bundles.

There are probably flashes of intro topics going on in the back of your mind here. A positive relationship between income and quantity demanded means we’re looking at a normal good. And if the Engle curve bent backward, this would mean it would be an inferior good. If I were to ask you to use just the information we have available, could you calculate the income elasticity of demand for any point on the Engle curve?

== Animation | Demand: Price and Quantity

Doing the same thing but for prices gives us individual demand curves. Lets set \$ p\_a = 1 \$, \$ p\_b = 1 \$, and \$ Y = 180 \$.

When \$ p\_a = 1 \$ the budget constraint isn’t particularly steep or flat, and we choosing \$ q\_a = 90 \$, and \$ q\_b^\* = 90 \$.

When \$ p\_a = 1 \$ the budget constraint isn’t particularly steep or flat, and we choosing \$ q\_a = 90 \$, and \$ q\_b^\* = 90 \$.

And finally at \$ p\_a = 3 \$ we see a further 1) steepening of the MRT and MRS, 2) shrinking of \$ q\_a \$ to \$ q\_a = 30 \$, and 3) \$ q\_b \$ saying at \$ q\_b = 90 \$.

Lets just quickly animate a few other prices, tracing out the individual demand for \$ q\_a \$. This is the classic relationship between \$ p\_a \$ and \$ q\_a \$ we call individual demand for \$ q\_a \$.

We can do the same tracing for \$ q\_b \$ by varying \$ p\_b \$ in the consumer’s problem. Similar to \$ p\_a \$, moving \$ p\_b \$ maps out the individual demand for \$ q\_b \$.

And we could see these relationships with calculus. If we took the first derivative of \$ q\_a^\* \$ with repsect to \$ p\_a \$, we would get the negative relationship satisfying the law of demand.

If we did the same thing for \$ q\_b^\* \$, we would get no response, since it doesn’t depend on \$ p\_a \$. And vice versa.
