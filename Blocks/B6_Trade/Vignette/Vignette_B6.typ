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

= ECON 0100 | Vignette B6 | International Trade

_Due in Recitation. Vignettes are a certificate of the work done together in Recitation._

Members of the wizarding world have preferences for pumpkin pasties according to the following demand curve:

#mitex(`
P_d = 14 - \frac{1}{2} Q_d
`)

Pumpkin pasties are produced by many sellers according to the following supply curve:

#mitex(`
P = 2 + \frac{1}{2} Q_s
`)

Prices are in galleons and quantity is in pasties.

== Q1 | {++The UK’s Pumpkin Pasties++}

Economic historians remember a time before the Ministry lifted barriers to exports and imports of {++pumpkin pasties++} #strike[lemon tarts]. The global price was 6 galleons. However, due to the trade barriers the UK did not #strike[did not] have access to this market for {++pasties++} #strike[tarts]. {++The UK’s domestic supply and demand curves are the ones above.++}

Use a graph and algebra to illustrate what happened to the market after the trade barrier was lifted.

a) Imports or exports? _imports, exports_

b) Quantity demanded: \_\_\_\_\_\_ Quantity supplied: \_\_\_\_\_\_ Imports: \_\_\_\_\_\_

c) Consumer surplus before: \_\_\_\_\_\_ after: \_\_\_\_\_\_

d) Producer surplus before: \_\_\_\_\_\_ after: \_\_\_\_\_\_

e) Change in total surplus: \_\_\_\_\_\_\_\_\_\_

f) Buyers: _gain, lose_ Sellers: _gain, lose_

== Q2 | {++Egypt’s Pumpkin Pasties++}

While the supply curve is very similar to that of the UK, demand for {++pumpkin pasties++} #strike[lemon tarts] is much lower in Egypt’s wizarding community, leading to a domestic price below the global price. Use a graph (_but no algebra_) to illustrate what happened to the market after Egypt lifted their ban on international trade of {++pumpkin pasties++} #strike[lemon tarts].

a) Egypt _imports, exports_

b) Buyers: _gain, lose_ Sellers: _gain, lose_

c) Total surplus: _rises, stays the same, falls_

~

~

== Q3 | {++A Rising World Price++}

{++Back in the UK, suppose the global price rises from 6 to 7 galleons.++}

a) Quantity demanded: \_\_\_\_\_\_ Quantity supplied: \_\_\_\_\_\_ Imports: \_\_\_\_\_\_

b) Imports have: _risen, stayed the same, fallen_

// plass:comment
// | Editor. Sources: Q1–Q2 are 24F Vignette B4, "UK’s Lemon Tarts" and "Egypt’s Lemon Tarts" (C1_Tariffs/Practice_Bank/Vignette_B4_v2.md), with lemon tarts swapped for this semester's Vignette pasties (the 24F Demo X1 "International Pumpkin Pasties" opens the same way) and the world price set to 6 to fit Vignette B3's curves. Q3 is mine, for the B6.1 bullet on a changing world price. Wording in {++ ++} is mine; "did not did not" is the source's typo.
// | Answers: Q1 imports; Qd 16, Qs 8, imports 8; CS 36 → 64; PS 36 → 16; TS +8; buyers gain, sellers lose. Q2 exports; buyers lose, sellers gain; TS rises. Q3 Qd 14, Qs 10, imports 4 (fallen).
// /plass:comment
