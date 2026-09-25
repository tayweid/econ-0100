// ECON 0100 handout. This file is the source; export the PDF from Plass.
#set page(paper: "us-letter", margin: (top: 1in, right: 0.5in, bottom: 1in, left: 0.5in), numbering: "1", number-align: center)
#set par(justify: true, leading: 10.215pt, spacing: 21.465pt)
#set text(size: 12.5pt, font: "New Computer Modern", hyphenate: true)
#show heading.where(level: 1): set text(size: 23.750pt)
#show heading.where(level: 1): set block(above: 26.391pt, below: 25.105pt)
#show heading.where(level: 2): set text(size: 14.375pt)
#show heading.where(level: 2): set block(above: 38.410pt, below: 18.473pt)
#show math.equation.where(block: true): set block(above: 21.490pt, below: 23.702pt)
#set math.equation(numbering: "(1)")
#import "@preview/mitex:0.2.5": mi, mitex

= ECON 0100 | Exercise B2 | Supply

Pumpkin pasties are produced by many sellers according to the following supply curve:

#mitex(`
P = 2 + \frac{Q_s}{10}
`)

Prices are in galleons and quantity is in pasties.

== Q1 | Quantity Supplied

a) What is quantity supplied at 10 galleons? \_\_\_\_\_\_\_\_\_\_

b) What is marginal cost at 9 pasties? \_\_\_\_\_\_\_\_\_\_

== Q2 | Producer Surplus

What is producer surplus at 10 galleons? \_\_\_\_\_\_\_\_\_\_
