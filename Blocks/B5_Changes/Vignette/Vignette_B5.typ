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

= ECON 0100 | Vignette B5 | Market Changes

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

== Q1 | Price Elasticity

a) Use the midpoint method to find the elasticity of demand when the price changes from 6 to 8 galleons. \_\_\_\_\_\_\_\_\_\_

b) Is demand elastic, unit elastic, or inelastic in a)? \_\_\_\_\_\_\_\_\_\_

c) Use the midpoint method to find the elasticity of demand when the price changes from 1 to 3 galleons. \_\_\_\_\_\_\_\_\_\_

d) Use the midpoint method to find the elasticity of supply when the price changes from 4 to 6 galleons. \_\_\_\_\_\_\_\_\_\_

#pagebreak()

== Q2 | Supply & Demand Shifters

Recent drier growing seasons has made growing pumpkins more difficult, with a new supply curve that can be represented by the following. At a price of 8 galleons, how has the quantity supplied and producer surplus changed with this change in climate?

#mitex(`
P = 4 + \frac{1}{2} Q_s
`)

a) Change in quantity supplied: \_\_\_\_\_\_\_\_\_\_

b) Change in producer surplus: \_\_\_\_\_\_\_\_\_\_

~

~

A popular channel on the wizarding social network FlueTube has been promoting pumpkin pasties, leading to {++an++} #strike[a] increase in the popularity of the snack.

c) The demand curve: _shifted in, stayed the same, shifted out_

d) The supply curve: _shifted in, stayed the same, shifted out_

#pagebreak()

== Q3 | Comparative Statics

{++Using the new supply curve from Q2 and the original demand curve,++} find and plot the equilibrium price and quantity for pumpkin pasties.

a) Equilibrium price: \_\_\_\_\_\_\_\_\_\_

b) Equilibrium quantity: \_\_\_\_\_\_\_\_\_\_

~

~

{++With both the drier growing seasons and the FlueTube promotion,++} without using numbers, use the graph above to discuss how the market has been impacted.

c) Equilibrium price has: _increased, stayed the same, decreased, indeterminate_

d) Equilibrium quantity has: _increased, stayed the same, decreased, indeterminate_

// plass:comment
// | Editor. Sources: the curves are Vignette B3's. Q1 is Exercise B5 Q1's wording with prices picked for clean answers (6 to 8 is exactly unit elastic). Q2 is 24F Vignette B2 (B_Practice_Bank/Vignette_B2_pasties_F24): Q3 drier growing seasons and Q6 FlueTube, verbatim except "an increase"; the drier-season supply moved from 4 + 2Q/3 to 4 + Q/2 to match this semester's curves, and the question asks at 8 galleons instead of 10. Q3's closing prompt is Vignette B2 Q6's "Without using numbers, use the graph above to discuss how the market has been impacted." Wording in {++ ++} is mine.
// | Answers: Q1 a) −1, b) unit elastic, c) −1/6, d) 5/3. Q2 a) −4 pasties (12 to 8), b) −20 galleons (36 to 16), c) shifted out, d) stayed the same. Q3 a) 9, b) 10, c) increased, d) indeterminate.
// /plass:comment
