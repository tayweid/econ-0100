// Exported from Plass
#set page(paper: "us-letter", margin: 0.6in, numbering: "1", number-align: center)
#set par(justify: true, leading: 8.172pt, spacing: 17.172pt)
#set list(spacing: 10.672pt)
#set enum(spacing: 10.672pt)
#set grid.cell(breakable: false)
#show heading.where(level: 1): set text(size: 19.000pt)
#show heading.where(level: 1): set block(above: 21.113pt, below: 20.084pt)
#show heading.where(level: 1): set par(leading: 10.777pt)
#show heading.where(level: 2): set text(size: 14.000pt)
#show heading.where(level: 2): set block(above: 35.720pt, below: 15.950pt)
#show heading.where(level: 2): set par(leading: 7.941pt)
#show heading.where(level: 3): set text(size: 11.500pt)
#show heading.where(level: 3): set block(above: 30.728pt, below: 14.778pt)
#show heading.where(level: 3): set par(leading: 6.523pt)
#show heading.where(level: 4): set text(size: 11.500pt)
#show heading.where(level: 4): set block(above: 30.728pt, below: 14.778pt)
#show heading.where(level: 4): set par(leading: 6.523pt)
#show heading.where(level: 5): set text(size: 11.500pt)
#show heading.where(level: 5): set block(above: 30.728pt, below: 14.778pt)
#show heading.where(level: 5): set par(leading: 6.523pt)
#show heading.where(level: 6): set text(size: 11.500pt)
#show heading.where(level: 6): set block(above: 30.728pt, below: 14.778pt)
#show heading.where(level: 6): set par(leading: 6.523pt)
#show raw.where(block: false): set text(font: "DejaVu Sans Mono", size: 8.000pt)
#show math.equation.where(block: true): set block(above: 17.192pt, below: 18.962pt)
#set text(size: 10pt, font: "New Computer Modern", hyphenate: true)
#import "@preview/mitex:0.2.5": mi, mitex

= ECON 0100 | Demo B

Demos are similar to Checkpoints, often taken directly from past semesters. Work through the problems and check your work against mine. Practice answering clearly and completely. You are encouraged to work in small groups. Find a study room, grab some classmates, and work together on a whiteboard.

== Dragontear

Dragontear is a rare and powerful substance used in potions, spells, and fire-breathing, harvested from dragons while they laugh uncontrollably. Prices are in coins and quantity is in vials. The supply and demand equations for dragontear are known to be the following:

#mitex(`
P = 60 - \frac{1}{10} Q_D \qquad\textit{and}\qquad P = \frac{1}{5} Q_S
`)

== Q1 | Demand and Consumer Surplus (B1.1, B1.2)

Use a graph to plot this demand curve. Find and label the consumer surplus at a price of 30. On the same graph, show what happens to consumer surplus when the price increases to 40.

#grid(
  columns: (3.2fr, 1fr),
  gutter: 1em,
  [
    a) Quantity demanded at a price of 20 \_\_\_\_\_, at 30 \_\_\_\_\_, at 40 \_\_\_\_\_ (B1.1)

    b) What is the marginal benefit of the 300th vial? \_\_\_\_\_\_ (B1.1)

    c) CS at 30 \_\_\_\_\_\_ CS at 40 \_\_\_\_\_\_ Expenditure at 30 \_\_\_\_\_\_ (B1.2)
  ],
  [
    #image("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNTAiIGhlaWdodD0iMTY1IiB2aWV3Qm94PSIwIDAgMjUwIDE2NSI+PHBhdGggZD0iTTE4IDhWMTQ3SDI0MiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjOTk5IiBzdHJva2Utd2lkdGg9IjEiLz48L3N2Zz4=")
  ],
)

== Q2 | Supply and Producer Surplus (B2.1, B2.2)

Use a graph to plot this supply curve. Find and label the producer surplus at a price of 30. On the same graph, show what happens to producer surplus when the price increases to 40.

#grid(
  columns: (3.2fr, 1fr),
  gutter: 1em,
  [
    a) Quantity supplied at 20 \_\_\_\_\_, at 30 \_\_\_\_\_, at 40 \_\_\_\_\_ (B2.1)

    b) What is the marginal cost of the 100th vial? \_\_\_\_\_\_ (B2.1)

    c) PS at 30 \_\_\_\_\_\_ PS at 40 \_\_\_\_\_\_ Revenue at 30 \_\_\_\_\_\_ (B2.2)
  ],
  [
    #image("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNTAiIGhlaWdodD0iMTY1IiB2aWV3Qm94PSIwIDAgMjUwIDE2NSI+PHBhdGggZD0iTTE4IDhWMTQ3SDI0MiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjOTk5IiBzdHJva2Utd2lkdGg9IjEiLz48L3N2Zz4=")
  ],
)

== Q3 | Price Elasticity (B5.2)

a) Find the elasticity of demand when the price changes from 10 to 20. \_\_\_\_\_\_\_\_\_\_ 

Is this:~_elastic, unit elastic, _or_ inelastic_?

b) Find the elasticity of supply when the price changes from 20 to 40. \_\_\_\_\_\_\_\_\_\_~

Is this:~_elastic, unit elastic, _or_ inelastic_?

== Q4 | Equilibrium for Dragontear (B3.1, B4.1)

Use a graph to describe the market for Dragontear:

#grid(
  columns: (3.2fr, 1fr),
  gutter: 1em,
  [
    a) Calculate equilibrium price: \_\_\_\_\_\_ Find equilibrium quantity: \_\_\_\_\_\_ (B3.1)

    b) At 30 coins: _shortage, excess_ of size \_\_\_\_\_\_, and the price will: _rise, fall_ (B3.1)

    c) Calculate total surplus at equilibrium: \_\_\_\_\_\_ (B4.1)

    d) What is the deadweight loss if only 100 vials are exchanged? \_\_\_\_\_\_ (B4.1)
  ],
  [
    #image("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNTAiIGhlaWdodD0iMTY1IiB2aWV3Qm94PSIwIDAgMjUwIDE2NSI+PHBhdGggZD0iTTE4IDhWMTQ3SDI0MiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjOTk5IiBzdHJva2Utd2lkdGg9IjEiLz48cGF0aCBkPSJNNDAgMjRMMjEwIDEzNiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjMzMzIiBzdHJva2Utd2lkdGg9IjEuNSIvPjxwYXRoIGQ9Ik00MCAxMjJMMjEwIDI4IiBmaWxsPSJub25lIiBzdHJva2U9IiMzMzMiIHN0cm9rZS13aWR0aD0iMS41Ii8+PHRleHQgeD0iMjE0IiB5PSIxNDMiIGZvbnQtZmFtaWx5PSJzZXJpZiIgZm9udC1zaXplPSIxMyIgZmlsbD0iIzMzMyI+RDwvdGV4dD48dGV4dCB4PSIyMTQiIHk9IjMwIiBmb250LWZhbWlseT0ic2VyaWYiIGZvbnQtc2l6ZT0iMTMiIGZpbGw9IiMzMzMiPlM8L3RleHQ+PC9zdmc+")
  ],
)

== Q5 | Price Floor (B4.2)

Use a graph of the demand curve and the supply curve to evaluate the welfare effects of a price floor of 45.

#grid(
  columns: (3.2fr, 1fr),
  gutter: 1em,
  [
    a) CS \_\_\_\_\_\_ Change in CS from Equilibrium \_\_\_\_\_\_

    b) PS \_\_\_\_\_\_ Change in PS from Equilibrium \_\_\_\_\_\_

    c) DWL \_\_\_\_\_\_ Shortage/Excess \_\_\_\_\_\_
  ],
  [
    #image("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNTAiIGhlaWdodD0iMTY1IiB2aWV3Qm94PSIwIDAgMjUwIDE2NSI+PHBhdGggZD0iTTE4IDhWMTQ3SDI0MiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjOTk5IiBzdHJva2Utd2lkdGg9IjEiLz48cGF0aCBkPSJNNDAgMjRMMjEwIDEzNiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjMzMzIiBzdHJva2Utd2lkdGg9IjEuNSIvPjxwYXRoIGQ9Ik00MCAxMjJMMjEwIDI4IiBmaWxsPSJub25lIiBzdHJva2U9IiMzMzMiIHN0cm9rZS13aWR0aD0iMS41Ii8+PHRleHQgeD0iMjE0IiB5PSIxNDMiIGZvbnQtZmFtaWx5PSJzZXJpZiIgZm9udC1zaXplPSIxMyIgZmlsbD0iIzMzMyI+RDwvdGV4dD48dGV4dCB4PSIyMTQiIHk9IjMwIiBmb250LWZhbWlseT0ic2VyaWYiIGZvbnQtc2l6ZT0iMTMiIGZpbGw9IiMzMzMiPlM8L3RleHQ+PC9zdmc+")
  ],
)

== Q6 | Second Wizarding War (B5.1, B5.3)

The second wizarding war limited the population of dragons. Use a graph to aid your discussion of the impact the war had on the market for dragontear.

#grid(
  columns: (3.2fr, 1fr),
  gutter: 1em,
  [
    a) The demand curve: _shifted up, stayed the same, shifted down_ (B5.1)

    b) The supply curve: _shifted up, stayed the same, shifted down_~(B5.1)

    In the years after the war, many more in the wizarding world required dragontear as part of a widespread rise in the popularity of spells. On its own (not including the change in the population of dragons), how has this change in popularity of spells changed the market for dragontear?

    e) The demand curve: _shifted up, stayed the same, shifted down_ (B5.1)

    f) The supply curve: _shifted up, stayed the same, shifted down_ (B5.1)
  ],
  [
    #image("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNTAiIGhlaWdodD0iMTY1IiB2aWV3Qm94PSIwIDAgMjUwIDE2NSI+PHBhdGggZD0iTTE4IDhWMTQ3SDI0MiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjOTk5IiBzdHJva2Utd2lkdGg9IjEiLz48cGF0aCBkPSJNNDAgMjRMMjEwIDEzNiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjMzMzIiBzdHJva2Utd2lkdGg9IjEuNSIvPjxwYXRoIGQ9Ik00MCAxMjJMMjEwIDI4IiBmaWxsPSJub25lIiBzdHJva2U9IiMzMzMiIHN0cm9rZS13aWR0aD0iMS41Ii8+PHRleHQgeD0iMjE0IiB5PSIxNDMiIGZvbnQtZmFtaWx5PSJzZXJpZiIgZm9udC1zaXplPSIxMyIgZmlsbD0iIzMzMyI+RDwvdGV4dD48dGV4dCB4PSIyMTQiIHk9IjMwIiBmb250LWZhbWlseT0ic2VyaWYiIGZvbnQtc2l6ZT0iMTMiIGZpbGw9IiMzMzMiPlM8L3RleHQ+PC9zdmc+")
  ],
)

Without using numbers, how have these two changes together impacted the dragontear market equilibrium?

g) Equilibrium price has: _increased, stayed the same, decreased, indeterminate_ (B5.3)

h) Equilibrium quantity has: _increased, stayed the same, decreased, indeterminate_ (B5.3)
