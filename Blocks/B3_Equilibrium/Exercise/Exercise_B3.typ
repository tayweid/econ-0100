// ECON 0100 handout. This file is the source; export the PDF from Plass.
// ED: CURVES (2026-09-21) — demand is B1's sheet curve verbatim. B2's sheet supply (P = 2 + Q_s/10) crosses it at Q = 50/3, so this sheet's market supply uses slope 1/2 for clean integers: equilibrium (10 pasties, 7 galleons). Swap freely; the Gradescope sheet and the notes' pause lines carry these numbers.
#set page(paper: "us-letter", margin: 1in, numbering: "1", number-align: center)
#set par(justify: true, leading: 10.215pt, spacing: 21.465pt)
#set text(size: 12.5pt, font: "New Computer Modern", hyphenate: true)
#show heading.where(level: 1): set text(size: 23.750pt)
#show heading.where(level: 1): set block(above: 26.391pt, below: 25.105pt)
#show heading.where(level: 2): set text(size: 14.375pt)
#show heading.where(level: 2): set block(above: 38.410pt, below: 18.473pt)
#show math.equation.where(block: true): set block(above: 21.490pt, below: 23.702pt)
#set math.equation(numbering: "(1)")
#import "@preview/mitex:0.2.5": mi, mitex

= ECON 0100 | Exercise B3 | Equilibrium

Pumpkin pasties are bought and sold in a market with the following demand and supply curves:

#mitex(`
P = 12 - \frac{Q_d}{2} \qquad\qquad P = 2 + \frac{Q_s}{2}
`)

Prices are in galleons and quantity is in pasties.

== Q1 | Equilibrium

a) Solve for the equilibrium quantity. \_\_\_\_\_\_\_\_\_\_

b) Solve for the equilibrium price. \_\_\_\_\_\_\_\_\_\_

c) Plot the demand curve, the supply curve, and the starred equilibrium pair.

== Q2 | A Price Away from Equilibrium

Pumpkin pasties again. Suppose the price is 5 galleons.

a) What is the quantity demanded? \_\_\_\_\_\_\_\_\_\_

b) What is the quantity supplied? \_\_\_\_\_\_\_\_\_\_

c) Is this a shortage or an excess, and how large? \_\_\_\_\_\_\_\_\_\_

d) Which way will the price move? \_\_\_\_\_\_\_\_\_\_
