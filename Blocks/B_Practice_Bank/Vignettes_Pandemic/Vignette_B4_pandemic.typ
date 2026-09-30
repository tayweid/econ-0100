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

= ECON 0100 | Vignette B4 | Efficiency

_Due in Recitation. Vignettes are a certificate of the work done together in Recitation._

The supply and demand curves for food before the pandemic are given in _*Vignette B3*_:

#mitex(`
S: P_s = 2 + \frac{1}{2} Q_s \qquad\qquad D: P_d = 20 - Q_d
`)

The equilibrium was 12 daily servings at 8 dollars.

== Q1 | Supply Chain Shock

The pandemic substantially disrupted the supply chain, leading to difficulty bringing food to market with a new supply curve below.

#mitex(`
P = 5 + \frac{1}{2} Q_s
`)

Use the graph (_above_) to discuss the impact of supply chain disruptions on the market. Be sure to include how welfare measures have changed.

a) New equilibrium price: \_\_\_\_\_\_\_\_\_\_ quantity: \_\_\_\_\_\_\_\_\_\_

b) Consumer surplus: \_\_\_\_\_\_\_\_\_\_ Producer surplus: \_\_\_\_\_\_\_\_\_\_

c) Change in total surplus: \_\_\_\_\_\_\_\_\_\_

~

== Q2 | A Ban on Price Gouging

In response to worries about price-gouging a basic necessity during a time {++of++} #strike[to] difficulty, the government imposes a ban on price hikes from pre-pandemic levels. Use a graph to discuss the impact on food availability were this policy to be implemented. Show welfare measures and calculate the new consumer surplus.

a) Quantity supplied: \_\_\_\_\_\_\_\_\_\_ Quantity demanded: \_\_\_\_\_\_\_\_\_\_ Shortage: \_\_\_\_\_\_\_\_\_\_

b) Consumer surplus: \_\_\_\_\_\_\_\_\_\_ Producer surplus: \_\_\_\_\_\_\_\_\_\_ Deadweight loss: \_\_\_\_\_\_\_\_\_\_

c) {++Compared with the market after the shock, buyers:++} _gain, lose_ {++and sellers:++} _gain, lose_

// plass:comment
// | Editor. Alternate Vignette for a future semester, from the pandemic food-market story. Q1 is 24F Vignette B3 Q2; Q2 is 23F Vignette C4 Q3 with 24F Q3's last sentence ("Show welfare measures and calculate the new consumer surplus"). The 24F Classwork B2 Q3 and 24F Vignette B3 Q3 ask the same ban with slightly different wording ("affordability of basic necessities", "good availability"). Numbers are new (the 23F ban left zero food supplied and the 24F shock gave 1.5 servings); wording in {++ ++} is mine.
// | Answers: Q1 a) 10 dollars, 10 servings; b) CS = ½ · 10 · 10 = 50, PS = ½ · 10 · 5 = 25; c) 75 − 108 = −33. Q2 the ban holds the price at 8: a) Qs 6, Qd 12, shortage 6; b) CS = ½ · (12 + 6) · 6 = 54 (MB of the 6th serving is 14), PS = ½ · 6 · 3 = 9, DWL = ½ · (14 − 8) · (10 − 6) = 12; c) buyers gain (50 → 54), sellers lose (25 → 9). Food availability falls from 10 to 6 servings.
// /plass:comment
