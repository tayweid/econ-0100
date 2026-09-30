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

= ECON 0100 | Exercise B1 | Demand

In the British wizarding world, the demand for enchanted broomsticks has always been high. Enchanted broomsticks sell along the demand curve #mi(`P = 16 - Q/4`), in galleons and broomsticks.

== Q1 | Quantity Demanded

a) What is the quantity demanded at 12 galleons? \_\_\_\_\_\_\_\_\_\_

b) What is the marginal benefit at a quantity of 16? \_\_\_\_\_\_\_\_\_\_

== Q2 | Consumer Surplus

Enchanted broomsticks again, #mi(`P = 16 - Q/4`).

a) What is the quantity demanded at 8 galleons? \_\_\_\_\_\_\_\_\_\_

b) Find and label the consumer surplus at that price.

// plass:comment
// | Editor. Broomstick version for a future semester, mirroring this fall's pasty Exercise. Text is Exercise B1's; the opening sentence is Classwork C1's. Pasties became enchanted broomsticks and the numbers follow the broomstick curves from Classwork C1 24F (16 − Q/4, 4 + Q/4; equilibrium 24 at 10); anything else I wrote is in {++ ++}.
// | Answers: Q1 a) 16, b) 12 galleons. Q2 a) 32, b) CS = ½ · 32 · (16 − 8) = 128 galleons.
// /plass:comment
