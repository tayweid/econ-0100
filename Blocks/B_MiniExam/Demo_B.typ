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

Demos are similar to Checkpoints, often taken directly from past semesters. Work through the problems and check your work against mine. Practice answering clearly and completely. Show your work so someone else can understand your thought process. You are encouraged to work in small groups. Find a study room, grab some classmates, and work together on a whiteboard.

== Dragontear

Dragontear is a rare and powerful substance used in potions, spells, and fire-breathing, harvested from dragons while they laugh uncontrollably. The supply and demand equations for dragontear are known to be the following:

#mitex(`
P_d = 60 - \frac{1}{10} Q_d \qquad\qquad P_s = \frac{1}{5} Q_s
`)

Prices are in {++coins++} #strike[galleons] and quantity is in {++vials++} #strike[thousands of units]. Use {++a graph++} #strike[the graph below] to guide your work.

== Q1 | Demand and Consumer Surplus (B1.1, B1.2)

Use a graph to plot this demand curve, and find the quantity demanded at a price of 20, 30, and 40.

a) Quantity demanded at a price of 20 \_\_\_\_\_\_\_\_\_\_, at 30 \_\_\_\_\_\_\_\_\_\_, at 40 \_\_\_\_\_\_\_\_\_\_

b) {++What is the marginal benefit of the 300th vial?++} \_\_\_\_\_\_\_\_\_\_

Find and label the consumer surplus at a price of 30. On the same graph, show what happens to consumer surplus when the price increases to 40.

c) CS at 30 \_\_\_\_\_\_\_\_\_\_ CS at 40 \_\_\_\_\_\_\_\_\_\_

== Q2 | Supply and Producer Surplus (B2.1, B2.2)

Use a graph to plot this supply curve, and find the quantity supplied at a price of 20, 30, and 40.

a) Quantity supplied at 20 \_\_\_\_\_\_\_\_\_\_, at 30 \_\_\_\_\_\_\_\_\_\_, at 40 \_\_\_\_\_\_\_\_\_\_

b) {++What is the marginal cost of the 100th vial?++} \_\_\_\_\_\_\_\_\_\_

Find and label the producer surplus at a price of 30. On the same graph, show what happens to producer surplus when the price increases to 40.

c) PS at 30 \_\_\_\_\_\_\_\_\_\_ PS at 40 \_\_\_\_\_\_\_\_\_\_

== Q3 | Equilibrium for Dragontear (B3.1, B4.1)

Use {++a graph++} #strike[the graph above] to describe the market for Dragontear:

a) Calculate equilibrium price: \_\_\_\_\_\_\_\_\_\_ Find equilibrium quantity: \_\_\_\_\_\_\_\_\_\_

b) Calculate consumer surplus: \_\_\_\_\_\_\_\_\_\_ Calculate producer surplus: \_\_\_\_\_\_\_\_\_\_

c) {++At a price of 30, is there a shortage or an excess, and how large?++} \_\_\_\_\_\_\_\_\_\_

d) {++What is the deadweight loss if only 100 vials are exchanged?++} \_\_\_\_\_\_\_\_\_\_

== Q4 | Price Floor (B4.2)

Use a graph of the demand curve and the supply curve to evaluate the welfare effects of a price floor of 45.

a) CS \_\_\_\_\_\_\_\_\_\_ Change in CS from Equilibrium \_\_\_\_\_\_\_\_\_\_

b) PS \_\_\_\_\_\_\_\_\_\_ Change in PS from Equilibrium \_\_\_\_\_\_\_\_\_\_

c) DWL \_\_\_\_\_\_\_\_\_\_ Shortage/Excess \_\_\_\_\_\_\_\_\_\_

== Q5 | Second Wizarding War (B5.1, B5.3)

The second wizarding war limited the population of dragons. Use {++a graph++} #strike[the graph above] to aid your discussion of the impact the war had on the market for dragontear.

a) The demand curve: _shifted in, stayed the same, shifted out_ #h(1fr) b) The supply curve: _shifted in, stayed the same, shifted out_

c) The equilibrium price: _increased, stayed the same, decreased_ #h(1fr) d) The equilibrium quantity: _increased, stayed the same, decreased_

In the years after the war, many more in the wizarding world required dragontear as part of a widespread rise in the popularity of spells. On {++its++} #strike[it’s] own (not including the change in the population of dragons), how has this change in popularity of spells {++changed++} #strike[change] the market for {++dragontear++} #strike[dragonstear]?

e) The demand curve: _shifted in, stayed the same, shifted out_ #h(1fr) f) The supply curve: _shifted in, stayed the same, shifted out_

Without using numbers, how have these two changes together impacted the dragontear market equilibrium?

g) Equilibrium price has: _increased, stayed the same, decreased, indeterminate_

h) Equilibrium quantity has: _increased, stayed the same, decreased, indeterminate_

The supply and demand equations for dragontear after the post-war changes {++above++} #strike[in Q2 and Q3] are known to be the following:

#mitex(`
P_d = 69 - \frac{1}{10} Q_d \qquad\qquad P_s = 15 + \frac{1}{5} Q_s
`)

Use a graph to discuss how consumer surplus and producer surplus changed after the war.

i) Consumer surplus after the war: \_\_\_\_\_\_\_\_\_\_ Change in consumer surplus after the war: \_\_\_\_\_\_\_\_\_\_

j) Producer surplus after the war: \_\_\_\_\_\_\_\_\_\_ Change in producer surplus after the war: \_\_\_\_\_\_\_\_\_\_

== Q6 | Price Elasticity (B5.2)

a) Use the midpoint method to find the elasticity of demand when the price changes from 10 to 20. \_\_\_\_\_\_\_\_\_\_

b) Use the midpoint method to find the elasticity of demand when the price changes from 40 to 50. \_\_\_\_\_\_\_\_\_\_

c) Use the midpoint method to find the elasticity of supply when the price changes from 20 to 40. \_\_\_\_\_\_\_\_\_\_

d) {++Which of a)–c) is elastic, unit elastic, or inelastic?++} \_\_\_\_\_\_\_\_\_\_

// plass:comment
// | Editor. Demo B is the 24F Dragontear homework (B_Practice_Bank/Homework_B1_dragontear_F24.md and _archive/Homework_2_dragontear_F24.md), laid out in the Checkpoint's six-question skill order. Every Dragontear piece is here: the laughing dragons, Q1 equilibrium with CS and PS (now Q3), the war, the rise in spells, "these two changes together," and Post-War Welfare Changes (Q5 i–j). The gaps are filled with your wording from two older demos: the carrots Homework 2 demo (quantity demanded and supplied "at a price of …", the midpoint elasticity questions) and the generic Homework 3 demo (consumer and producer surplus when "the price increases," the price floor with its CS / change / PS / change / DWL / shortage lines). New numbers (60 − Q/10 and Q/5) keep it apart from Reattempt B's Dragon's Blood curves. Wording in {++ ++} is mine.
// | Answers: Q1 a) 400, 300, 200; b) 30; c) 4500, 2000. Q2 a) 100, 150, 200; b) 20; c) 2250, 4000. Q3 a) 40, 200; b) 2000, 4000; c) shortage of 150; d) ½ · (50 − 20) · (200 − 100) = 1500. Q4 floor 45: Qd 150, Qs 225; a) 1125, −875; b) 4500 (price 45 minus MC from 0 to 30 over 150 vials), +500; c) 375, excess of 75. Q5 a) same, b) in, c) increased, d) decreased; e) out, f) same; g) increased, h) indeterminate; post-war equilibrium 180 at 51, i) 1620, −380, j) 3240, −760. Q6 a) −1/3, b) −3, c) 1 (supply through the origin is unit elastic everywhere), d) a) inelastic, b) elastic, c) unit elastic.
// /plass:comment
