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
#import "@preview/mitex:0.2.5": mi, mitex

= ECON 0100 | Exercise B5 | Market Changes

Enchanted broomsticks again, with the same demand and supply curves as Exercise B3:

#mitex(`
P = 16 - \frac{Q_d}{4} \qquad\qquad P = 4 + \frac{Q_s}{4}
`)

Prices are in galleons and quantity is in broomsticks. The equilibrium you found is 24 broomsticks at 10 galleons.

== Q1 | Price Elasticity

a) Use the midpoint method to find the elasticity of demand when the price changes from 10 to 14 galleons. \_\_\_\_\_\_\_\_\_\_

b) Is demand elastic, unit elastic, or inelastic in a)?~

c) Use the midpoint method to find the elasticity of demand when the price changes from 2 to 6 galleons. \_\_\_\_\_\_\_\_\_\_

d) Use the midpoint method to find the elasticity of supply when the price changes from 6 to 10 galleons. \_\_\_\_\_\_\_\_\_\_

~

#pagebreak()

== Q2 | Supply & Demand Shifters

{++The Floo Network opened a fireplace connection in every wizarding village, and many witches and wizards stopped flying to work.++}

a) The demand curve: _shifted in, stayed the same, shifted out_

b) The supply curve: _shifted in, stayed the same, shifted out_

~

~

~

~

== Q3 | Comparative Statics

{++Broom makers suddenly discover an enchantment that lets each workshop finish twice as many broomsticks in a day.++} On its own, how did this discovery impact the market?

a) The equilibrium price: _increased, stayed the same, decreased_

b) The equilibrium quantity: _increased, stayed the same, decreased_

Without using numbers, how have these two changes together (the {++Floo Network++} and the {++enchantment++}) impacted the broomstick market equilibrium?

c) Equilibrium price has: _increased, stayed the same, decreased, indeterminate_

d) Equilibrium quantity has: _increased, stayed the same, decreased, indeterminate_

~

// plass:comment
// | Editor. Broomstick version for a future semester, mirroring this fall's pasty Exercise. Text is Exercise B5's; the two events are mine (a substitute for demand, a technology for supply) standing in for the Daily Profit study and the fertilizer. Pasties became enchanted broomsticks and the numbers follow the broomstick curves from Classwork C1 24F (16 − Q/4, 4 + Q/4; equilibrium 24 at 10); anything else I wrote is in {++ ++}.
// | Answers: Q1 a) Q 24 → 8: (−16/16) ÷ (4/12) = −3; b) elastic; c) Q 56 → 40: (−16/48) ÷ (4/4) = −1/3; d) Q 8 → 24: (16/16) ÷ (4/8) = 2. Q2 a) shifted in (a better substitute), b) stayed the same. Q3 a) decreased, b) increased; c) decreased, d) indeterminate. With numbers, if demand falls to P = 14 − Q/4 and supply to P = 2 + Q/4, the new equilibrium is 24 at 8: price down, quantity unchanged.
// /plass:comment
