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

Pumpkin pasties again, with the same demand and supply curves as Exercise B3:

#mitex(`
P = 12 - \frac{Q_d}{2} \qquad\qquad P = 2 + \frac{Q_s}{2}
`)

Prices are in galleons and quantity is in pasties. The equilibrium you found is 10 pasties at 7 galleons.

== Q1 | Unlocking the Magic

For nearly all of recent history the Ministry of Magic required {++pumpkin pasties++} #strike[broomsticks] to be made and purchased locally. The ministry got wind of some economics ideas around opening the domestic market to international trade and has hired you to offer {++advice++} #strike[advise] on the impact this policy would have on the domestic {++pasty++} #strike[broomstick] market. The world price for {++pumpkin pasties++} #strike[enchanted broomsticks] is 5 galleons.

Use a market model to analyze the impact. Give special focus to the welfare impacts on buyers and sellers. {++Do calculate the welfare measures,++} #strike[No need to calculate welfare measures. Do calculate] {++and++} the impact to prices and quantities.

a) Imports or exports? _imports, exports_

b) Quantity demanded: \_\_\_\_\_\_ Quantity supplied: \_\_\_\_\_\_ Imports: \_\_\_\_\_\_

c) Consumer surplus before: \_\_\_\_\_\_ after: \_\_\_\_\_\_

d) Producer surplus before: \_\_\_\_\_\_ after: \_\_\_\_\_\_

e) Change in total surplus: \_\_\_\_\_\_\_\_\_\_

f) Buyers: _gain, lose_ Sellers: _gain, lose_

~

== Q2 | An Alternative World

If instead of a price of 5 galleons in Question 1 the global price had been 9 what would have been the distributional impact of opening the domestic market for trade? No need to do math here. Simply use a graph to show the impact on the market.

a) Imports or exports? _imports, exports_

b) Buyers: _gain, lose_ Sellers: _gain, lose_

c) Total surplus: _rises, stays the same, falls_

// plass:comment
// | Editor. Source: Classwork C1 24F, "From Local Markets to Global Skies" (C1_Tariffs/Practice_Bank/Classwork_C1_v2.md; also 23S MiniExam X and 24F Vignette B1), with broomsticks swapped for this semester's Exercise pasties and world prices of 5 and 9 to fit the curves. Q1 now asks for the welfare numbers (B6.1). Wording in {++ ++} is mine. The broomstick original, verbatim with its own curves (16 − Q/4, 4 + Q/4; world prices 6 and 12), would give Exercises a story of their own.
// | Answers: Q1 imports; Qd 14, Qs 6, imports 8; CS 25 → 49; PS 25 → 9; TS +8; buyers gain, sellers lose. Q2 exports (8); buyers lose, sellers gain; TS rises.
// /plass:comment
