// Exported from Plass
#set page(paper: "us-letter", margin: 1.25in, numbering: "1", number-align: center)
#set par(justify: true, leading: 10.215pt, spacing: 21.465pt)
#set list(spacing: 13.340pt)
#set enum(spacing: 13.340pt)
#show heading.where(level: 1): set text(size: 23.750pt)
#show heading.where(level: 1): set block(above: 26.391pt, below: 25.105pt)
#show heading.where(level: 1): set par(leading: 13.471pt)
#show heading.where(level: 2): set text(size: 17.500pt)
#show heading.where(level: 2): set block(above: 44.650pt, below: 19.937pt)
#show heading.where(level: 2): set par(leading: 9.926pt)
#show heading.where(level: 3): set text(size: 14.375pt)
#show heading.where(level: 3): set block(above: 38.410pt, below: 18.473pt)
#show heading.where(level: 3): set par(leading: 8.153pt)
#show raw.where(block: false): set text(font: "DejaVu Sans Mono", size: 10.000pt)
#show math.equation.where(block: true): set block(above: 21.490pt, below: 23.702pt)
#set text(size: 12.5pt, font: "New Computer Modern", hyphenate: true)
#set math.equation(numbering: "(1)")
#import "@preview/mitex:0.2.5": mi, mitex

== ECON 0100 | Vignette B1 | Demand

=== Q1 | Individual Demand Simulation

For each price offered to the volunteer in recitation, plot your *Quantity Demanded*, how much you would be willing to buy at that price.

~

~

~

~

=== Q2 | Pumpkin Pasties

Members of the wizarding world have preferences for pumpkin pasties according to the following demand curve:

#mitex(`
P_d = 12 - \frac{1}{2} Q_d
`)

Prices are in galleons and quantity is in thousands of pasties. Plot this demand curve.

~

~

~

~

_Hint: Start by finding the vertical intercept: plug in a value of _#mi(`0`)~_for quantity. Then find the horizontal intercept: plug in a value of _#mi(`0`)_ for price._

=== Q3 | Quantity Demanded

a) Plot and find the quantity demanded at #mi(`10`) galleons.~\_\_\_\_\_\_\_\_\_

b) Plot and find the quantity demanded at #mi(`5`) galleons.~\_\_\_\_\_\_\_\_\_\_

c) How much did quantity demanded change as the price dropped from #mi(`10`) to #mi(`5`)?
