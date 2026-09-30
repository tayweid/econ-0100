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

= ECON 0100 | Exercise B3 | Equilibrium

Enchanted broomsticks are bought and sold in a market with the following demand and supply curves:

#mitex(`
P = 16 - \frac{Q_d}{4} \qquad\qquad P = 4 + \frac{Q_s}{4}
`)

Prices are in galleons and quantity is in broomsticks.

== Q1 | Equilibrium

a) What is the equilibrium quantity? \_\_\_\_\_\_\_\_\_\_

b) What is the equilibrium price? \_\_\_\_\_\_\_\_\_\_

c) Plot the demand curve, the supply curve, and the starred equilibrium pair.

~

~

~

~

== Q2 | A Price Away from Equilibrium

Enchanted broomsticks again. Suppose the price is 8 galleons.

a) What is the quantity demanded? \_\_\_\_\_\_\_\_\_\_

b) What is the quantity supplied? \_\_\_\_\_\_\_\_\_\_

c) Is this a shortage or an excess, and how large? \_\_\_\_\_\_\_\_\_\_

d) Which way will the price move? \_\_\_\_\_\_\_\_\_\_

// plass:comment
// | Editor. Broomstick version for a future semester, mirroring this fall's pasty Exercise. Text is Exercise B3's. Pasties became enchanted broomsticks and the numbers follow the broomstick curves from Classwork C1 24F (16 − Q/4, 4 + Q/4; equilibrium 24 at 10); anything else I wrote is in {++ ++}.
// | Answers: Q1 a) 24, b) 10 galleons. Q2 a) 32, b) 16, c) a shortage of 16, d) up.
// /plass:comment
