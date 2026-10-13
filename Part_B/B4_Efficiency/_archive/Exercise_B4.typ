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

= ECON 0100 | Exercise B4 | Price Controls

Pumpkin pasties again, with the same demand and supply curves as Exercise B3:

#mitex(`
P = 12 - \frac{Q_d}{2} \qquad\qquad P = 2 + \frac{Q_s}{2}
`)

Prices are in galleons and quantity is in pasties. The equilibrium you found is 10 pasties at 7 galleons.

== Q1 | A Price Ceiling

The government sets a maximum legal price of 5 galleons. From Exercise B3, at 5 galleons the quantity demanded is 14 and the quantity supplied is 6.

Start by plotting the demand curve, the supply curve, and the price ceiling, and shade consumer surplus, producer surplus, and deadweight loss.

a) How many pasties are exchanged? \_\_\_\_\_\_\_\_\_\_

b) What is consumer surplus? \_\_\_\_\_\_\_\_\_\_

c) What is producer surplus? \_\_\_\_\_\_\_\_\_\_

d) What is deadweight loss? \_\_\_\_\_\_\_\_\_\_

~

~

~

~

~

== Q2 | A Price Floor

Suppose instead the government sets a minimum legal price of 9 galleons. Now the quantity demanded is 6 and the quantity supplied is 14.

Start by plotting the demand curve, the supply curve, and the price floor, and shade consumer surplus, producer surplus, and deadweight loss.

a) How many pasties are exchanged? \_\_\_\_\_\_\_\_\_\_

b) What is producer surplus? \_\_\_\_\_\_\_\_\_\_

c) What is deadweight loss? \_\_\_\_\_\_\_\_\_\_

d) Would a floor of 6 galleons change the market? \_\_\_\_\_\_\_\_\_\_
