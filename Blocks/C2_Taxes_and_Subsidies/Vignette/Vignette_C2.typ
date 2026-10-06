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

= ECON 0100 | Vignette C2 | Taxes

_Due in Recitation. Vignettes are a certificate of the work done together in Recitation._

{++The demand curve for pumpkin pasties can be represented by:++}

#mitex(`
P = 17 - \frac{1}{6} Q
`)

The supply curve for pumpkin pasties can be represented by the equation:

#mitex(`
P = 2 + \frac{2}{3} Q
`)

== Q1 | Somethin’s Up With Pumpkins

After years of careful epidemiological analysis, a subcommittee of the Ministry tasked with improving the health and wellbeing of the wizarding community published a story in the Daily Profit establishing a link between the consumption of pumpkin pasties and accidental magical spell casting by wizards and witches in public areas, with many cases of innocent muggles being nearly injured. To address these obvious public health concerns, the fiscal arm of the Ministry imposed a 2 galleon tax on the sale of pumpkin pasties, and reinvested the revenues into researching a magical remedy for this diet-driven ailment.\* Use a graph to illustrate the impact this tax had on the market and suggest a value to the tax.

~

~

a) Eq. Price (pre-tax): \_\_\_\_\_\_ Eq. Price (post-tax): \_\_\_\_\_\_

b) Eq. Quant (pre-tax): \_\_\_\_\_\_ Eq. Quantity (post-tax): \_\_\_\_\_\_

c) CS (post-tax): \_\_\_\_\_\_ ΔCS: \_\_\_\_\_\_

d) PS (post-tax): \_\_\_\_\_\_ ΔPS: \_\_\_\_\_\_

e) DWL: \_\_\_\_\_\_

_\*Note: assume there are no externalities, which we’ll cover next week; pumpkin pasties are a private good; the market is competitive._

// plass:comment
// | Editor. Sources. The curves are 21F Homework 3 Parts 1–2 (C_Practice_Bank/Homework_3_pasties-tax_F21.md); the supply sentence is Part 2's, the demand sentence is mine (Part 1's reads "Last homework we looked at the demand curve…"). Q1 is Homework 3 Part 4 (the 2-galleon tax, blanks, and footnote), with the closing "and suggest a value to the tax" carried in from 24F Demo C4 Q2 (stem Checkpoints/C/_Archive/C1.1_pumpkin-tax.md, same text as 24F_Demo_C4.md Q2), whose title "Somethin’s Up With Pumpkins" is the heading. The blanks are the source's nine, paired two per line in the source's two columns. The Demo version differs only in "nearly being injured", "imposed a tax … while reinvesting the revenues", and no stated tax size.
// | Answers. Pre-tax: P 14, Q 18, CS 27, PS 108. Post-tax (17 − Q/6 − 2 = 2 + 2Q/3): Q 15.6, buyers pay 14.4, sellers get 12.4; CS 20.28 (ΔCS −6.72), PS 81.12 (ΔPS −26.88), revenue 31.2, DWL ½·2·2.4 = 2.4. "Eq. Price (post-tax)" has two answers, 14.4 for buyers and 12.4 for sellers. "Suggest a value" has no single number (the Demo gave no externality size). No ink key: the stem names Demo_C_sols.pdf, but that file is 24F Demo C1 (the accidental-spells market, now Vignette C1–C3), not this tax question, and no Homework 3 key was found.
// | Flags. (1) "Suggest a value to the tax" sits after a stated 2-galleon tax and against the footnote's "assume there are no externalities"; keep one or the other (the Demo version had no number and no footnote). (2) These curves (17 − Q/6, 2 + 2Q/3) match old Vignette C1 Q4–Q5 but not Vignettes C1 and C3 (100 − Q, 10 + Q) or old Vignette C1 Q1–Q3. (3) The footnote's "which we’ll cover next week" no longer fits: since 2026-10-06 externalities (C1) come before taxes (C2), and all three C Vignettes share the Oct 15/16 recitation.
// | Gap: C2.2 Subsidies. The export subsidy (old Vignette C1 Q5) is the only pasty subsidy.
// /plass:comment
