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

The supply and demand curves for food before the pandemic are given in _*Vignette B3*_:

#mitex(`
S: P_s = 2 + \frac{1}{2} Q_s \qquad\qquad D: P_d = 20 - Q_d
`)

== Q1 | Price Elasticity

a) {++Use the midpoint method to find the elasticity of demand for food when the price changes from 8 to 12 dollars.++} \_\_\_\_\_\_\_\_\_\_

b) {++Is demand elastic, unit elastic, or inelastic in a)?++} \_\_\_\_\_\_\_\_\_\_

c) {++Use the midpoint method to find the elasticity of demand when the price changes from 2 to 6 dollars.++} \_\_\_\_\_\_\_\_\_\_

d) {++Use the midpoint method to find the elasticity of supply when the price changes from 4 to 8 dollars.++} \_\_\_\_\_\_\_\_\_\_

== Q2 | Pandemic Impact

The pandemic had two primary impacts on the food market. First, the supply chain experienced major disruptions. Second, consumers were willing to spend more on food as government programs like unemployment benefits and employee protections supported incomes and uncertainty about the future led to stockpiling.

a) {++After the supply chain disruptions, the supply curve:++} _shifted in, stayed the same, shifted out_

b) {++After the support for incomes and the stockpiling, the demand curve:++} _shifted in, stayed the same, shifted out_

== Q3 | Both Shocks

If in addition to the supply chain disruptions, consumers were willing to spend more on food as government programs like unemployment benefits and employee protections supported incomes. Use a graph to discuss what happened to the market price and quantity after both shocks and in the absence of price controls.

#mitex(`
S: P = 5 + \frac{1}{2} Q_s \qquad\qquad D: P = 23 - Q_d
`)

a) {++Without using numbers, the price has:++} _increased, stayed the same, decreased, indeterminate_ {++and the quantity has:++} _increased, stayed the same, decreased, indeterminate_

b) {++With the curves above, the new equilibrium price is++} \_\_\_\_\_\_\_\_\_\_ {++and quantity is++} \_\_\_\_\_\_\_\_\_\_

c) {++What phenomenon is this?++} \_\_\_\_\_\_\_\_\_\_

// plass:comment
// | Editor. Alternate Vignette for a future semester, from the pandemic food-market story. Q2 is 24F Classwork B2 Q2 (with the stockpiling line); Q3 is 24F Vignette B3 Q4, with 23F Vignette C4 Q2's closing question "What phenomenon is this?". Q1 is mine, in Exercise B5's elasticity wording. The "cents" 24F variant (B_Practice_Bank/_archive/Vignette_B3_pandemic-cents_F24.md) is the same story with prices in cents. Numbers are new (the 23F ban left zero food supplied and the 24F shock gave 1.5 servings); wording in {++ ++} is mine.
// | Answers: Q1 a) Q 12 → 8: (−4/10) ÷ (4/10) = −1; b) unit elastic; c) Q 18 → 14: (−4/16) ÷ (4/4) = −1/4; d) Q 4 → 12: (8/8) ÷ (4/6) = 3/2. Q2 a) shifted in, b) shifted out. Q3 a) price increased, quantity indeterminate; b) 23 − Q = 5 + Q/2 gives 12 servings at 11 dollars (the quantity is back at 12, the price is up 3); c) inflation: the price level rises with no change in how much is eaten.
// /plass:comment
