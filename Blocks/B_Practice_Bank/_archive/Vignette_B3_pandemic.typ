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

= ECON 0100 | Vignette B3 | Equilibrium

_Due in Recitation. Vignettes are a certificate of the work done together in Recitation._

== Modeling a Pandemic

In this Vignette we’re going to model a hypothetical scenario to illustrate the effect a global pandemic can have on the lives of buyers and sellers and the impact of one type of government policy. This is both hypothetical and illustrative.

Imagine a pandemic forces the world into a global lockdown and a subsequent slow reopening. This has many effects on the market for food. First, buyers have roughly the same income, due in part to unemployment benefits, government support, and employee protections. Second, there are major supply chain disruptions for nearly every good available. Third, many types of goods and services are no longer available, like movie theaters, cruises, and in-restaurant dining.

Imagine the market for food (as a bundle) is represented by the following supply and demand curves before the pandemic.

#mitex(`
S: P_s = 2 + \frac{1}{2} Q_s \qquad\qquad D: P_d = 20 - Q_d
`)

Units are in dollars and daily servings.

== Q1 | Initial Equilibrium

Use a graph and a sentence to discuss the food market prior to the pandemic. Be sure to calculate equilibrium price, quantity, consumer surplus, and producer surplus.

a) Equilibrium price: \_\_\_\_\_\_\_\_\_\_ Equilibrium quantity: \_\_\_\_\_\_\_\_\_\_

b) Consumer surplus: \_\_\_\_\_\_\_\_\_\_ Producer surplus: \_\_\_\_\_\_\_\_\_\_

~

~

== Q2 | {++Empty Shelves++}

{++In the first weeks of the lockdown, grocers kept the price at 6 dollars.++}

a) {++Quantity demanded:++} \_\_\_\_\_\_\_\_\_\_ {++Quantity supplied:++} \_\_\_\_\_\_\_\_\_\_

b) {++Is there a shortage or an excess, and how large?++} \_\_\_\_\_\_\_\_\_\_

c) {++Which way will the price move?++} \_\_\_\_\_\_\_\_\_\_

// plass:comment
// | Editor. Alternate Vignette for a future semester, from the pandemic food-market story. Intro and Q1 are 23F Vignette C4 and 24F Vignette B3 (B_Practice_Bank/_archive/Vignette_B3_pandemic_*); Q2 is mine, for the B3.1 shortage bullet. Numbers are new (the 23F ban left zero food supplied and the 24F shock gave 1.5 servings); wording in {++ ++} is mine.
// | Answers: Q1 a) 8 dollars, 12 servings; b) CS = ½ · 12 · 12 = 72, PS = ½ · 12 · 6 = 36. Q2 a) Qd 14, Qs 8; b) a shortage of 6; c) up.
// /plass:comment
