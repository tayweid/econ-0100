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

= ECON 0100 | Exercise B6 | International Trade

== Q1 | Unlocking the Magic

In the British wizarding world, the demand for enchanted broomsticks has always been high. For nearly all of recent history the Ministry of Magic required broomsticks to be made and purchased locally. The ministry got wind of some economics ideas around opening the domestic market to international trade and has hired you to offer {++advice++} #strike[advise] on the impact this policy would have on the domestic broomstick market. The world price for enchanted broomsticks is 6 galleons and the supply and demand curves for enchanted broomsticks are as follows:

#mitex(`
P = 16 - \frac{Q_d}{4} \qquad\qquad P = 4 + \frac{Q_s}{4}
`)

Use a market model to analyze the impact. Give special focus to the welfare impacts on buyers and sellers. No need to calculate welfare measures. Do calculate the impact to prices and quantities.

{++a) Imports or exports?++} _imports, exports_

{++b) Quantity demanded:++} \_\_\_\_\_\_\_\_\_\_ {++Quantity supplied:++} \_\_\_\_\_\_\_\_\_\_ {++Imports:++} \_\_\_\_\_\_\_\_\_\_

{++c) Buyers:++} _gain, lose_ {++Sellers:++} _gain, lose_

~

~

== Q2 | An Alternative World

If instead of a price of 6 galleons in Question 1 the global price had been 12 what would have been the distributional impact of opening the domestic market for trade? No need to do math here. Simply use a graph to show the impact on the market.

{++a) Imports or exports?++} _imports, exports_

{++b) Buyers:++} _gain, lose_ {++Sellers:++} _gain, lose_

// plass:comment
// | Editor. Broomstick version for a future semester, mirroring this fall's pasty Exercise. Text is Classwork C1 24F verbatim (C1_Tariffs/Practice_Bank/Classwork_C1_v2.md), with its own curves; only the answer lines are mine. Pasties became enchanted broomsticks and the numbers follow the broomstick curves from Classwork C1 24F (16 − Q/4, 4 + Q/4; equilibrium 24 at 10); anything else I wrote is in {++ ++}.
// | Answers: Q1 a) imports; b) Qd 40, Qs 8, imports 32; c) buyers gain (CS 72 → 200), sellers lose (PS 72 → 8); TS rises by 64. Q2 a) exports (Qd 16, Qs 32, exports 16); b) buyers lose, sellers gain.
// /plass:comment
