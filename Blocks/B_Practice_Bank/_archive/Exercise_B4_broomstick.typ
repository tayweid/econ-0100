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

= ECON 0100 | Exercise B4 | Price Controls

Enchanted broomsticks again, with the same demand and supply curves as Exercise B3:

#mitex(`
P = 16 - \frac{Q_d}{4} \qquad\qquad P = 4 + \frac{Q_s}{4}
`)

Prices are in galleons and quantity is in broomsticks. The equilibrium you found is 24 broomsticks at 10 galleons.

== Q1 | A Price Ceiling

The government sets a maximum legal price of 8 galleons. From Exercise B3, at 8 galleons the quantity demanded is 32 and the quantity supplied is 16.

Start by plotting the demand curve, the supply curve, and the price ceiling, and shade consumer surplus, producer surplus, and deadweight loss.

a) How many broomsticks are exchanged? \_\_\_\_\_\_\_\_\_\_

b) What is consumer surplus? \_\_\_\_\_\_\_\_\_\_

c) What is producer surplus? \_\_\_\_\_\_\_\_\_\_

d) What is deadweight loss? \_\_\_\_\_\_\_\_\_\_

~

~

~

~

~

== Q2 | A Price Floor

Suppose instead the government sets a minimum legal price of 12 galleons. Now the quantity demanded is 16 and the quantity supplied is 32.

Start by plotting the demand curve, the supply curve, and the price floor, and shade consumer surplus, producer surplus, and deadweight loss.

a) How many broomsticks are exchanged? \_\_\_\_\_\_\_\_\_\_

b) What is producer surplus? \_\_\_\_\_\_\_\_\_\_

c) What is deadweight loss? \_\_\_\_\_\_\_\_\_\_

d) Would a floor of 9 galleons change the market? \_\_\_\_\_\_\_\_\_\_

// plass:comment
// | Editor. Broomstick version for a future semester, mirroring this fall's pasty Exercise. Text is Exercise B4's. Pasties became enchanted broomsticks and the numbers follow the broomstick curves from Classwork C1 24F (16 − Q/4, 4 + Q/4; equilibrium 24 at 10); anything else I wrote is in {++ ++}.
// | Answers: Q1 a) 16; b) CS = ½ · (8 + 4) · 16 = 96 (MB of the 16th is 12); c) PS = ½ · 16 · 4 = 32; d) DWL = ½ · (12 − 8) · (24 − 16) = 16 (check: 144 − 96 − 32). Q2 a) 16; b) PS = ½ · (8 + 4) · 16 = 96 (MC of the 16th is 8); c) DWL = 16; d) no, 9 is below the equilibrium price of 10, so the floor doesn't bind.
// /plass:comment
