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

= ECON 0100 | Homework C2 | Taxes

_Due: TBD_

Homework is designed to both test your knowledge and challenge you to apply familiar concepts in new applications. Answer clearly and completely, and show your work so you can later understand your thought process. You are welcomed and encouraged to work in groups as long as your work is your own. Submit your answers on Gradescope when you’re finished: each answer there is a selection.

== Q1 | The Butterbeer Tax

The Ministry of Magic was in some financial trouble after their considerable expenditures during the war. They decided to impose a tax of 2 galleons on the sale of butterbeer as a source of funding. Use a graph to evaluate the welfare effects the policy had on the market. The supply and demand curves for butterbeer can be represented by the following equations.

#mitex(`
P_b = 20 - \frac{1}{2} Q_b
`)

#mitex(`
P_s = 2 + \frac{1}{2} Q_s
`)

Use a graph and algebra to calculate equilibrium before and after the tax. Start with the pre-tax equilibrium. Then use the tax equation (#mi(`P_b = \tau + P_s`)) to solve for equilibrium quantity and the two prices. Conclude with the remaining relevant components. _Note: _#strike[_Like Q1, _]_I’m looking for a complete description of the impacts on the market._

// plass:comment
// | Editor. Sources. Q1 base: Homework C 24F Q2 (C_Practice_Bank/Homework_C_F24.md, +pdf; ink key ECON_0100/Checkpoints/C/HW_C_sols.pdf), verbatim, the most complete version. Carried in: "Use a graph to evaluate the welfare effects the policy had on the market." from the three vignettes (C_Practice_Bank/_archive/Vignette_2_butterbeer-tax_F21.md, Vignette_C1_butterbeer-tax_F23.md, Vignette_B5_butterbeer-tax_F24.md), placed where they have it, after the tax sentence. Struck: "Like Q1," (24F's Q1 is the lemon tarts tariff, kept for the reattempts). Other versions: Homework C 23F Q1 (C_Practice_Bank/Homework_C_butterbeer-tax-floo_F23.md, ink key _sols_F23.pdf) is the same question with "price equation" for "tax equation," "Galleons," Q_d for Q_b, and no closing sentence or note; its "on the sale of as a source" is missing "butterbeer," which 24F has. No typo fixes needed.
// | Number sets. Used: 20 − Q/2 and 2 + Q/2 with a 2-galleon tax (Homework C 23F Q1, Homework C 24F Q2, Vignette C1 23F). Not used: 23 − Q/6 and 2 + Q/2 with no tax amount given (Vignette 2 21F, Vignette B5 24F); 21F and 24F name the curves "P" and "D:/S:" respectively.
// | Answers. Pre-tax: Q 18, P 11, CS 81, PS 81. After the tax: Q 16, Pb 12, Ps 10, CS 64, PS 64, government revenue 32, DWL 2. The tax lowered quantity, raised the buyers' price by 1, lowered the sellers' price by 1, raised revenue, and produced DWL; incidence split evenly (equal slopes). Matches both ink keys (23F: Q 18 → 16, Pb 12, Ps 10; 24F: CS 64, PS 64, Gov 32, DWL 2).
// | Gaps and flags. Gap: C2.2 Subsidies (no butterbeer subsidy material). Flag: these curves (20 − Q/2, 2 + Q/2) differ from Part B's and old Homework C1 Q1–Q3's butterbeer (100 − Q/2, 20 + Q/2). No graph grid and no Gradescope selection blanks placed.
// /plass:comment
