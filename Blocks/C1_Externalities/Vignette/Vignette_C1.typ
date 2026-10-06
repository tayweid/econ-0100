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

= ECON 0100 | Vignette C1 | Externalities

_Due in Recitation. Vignettes are a certificate of the work done together in Recitation._

Residents of Hogsmeade enjoy pumpkin pasties year round. The Demand (marginal benefit) curve and Supply (marginal cost) curve for pumpkin pasties can be represented using the following relationships.

#mitex(`
D: P_b = 100 - Q_b
`)

#mitex(`
S: P_s = 10 + Q_s
`)

However, a recent report conducted by the Daily Profit conclusively established a link between the consumption of pumpkin pasties and accidental magical spells, with a cost to society of 10 galleons.

== Q1 | Market Equilibrium

Find the market equilibrium price, quantity, and DWL. Use algebra and a graph to guide your answers.

~

~

a) Market Equilibrium Quantity: \_\_\_\_\_\_\_\_\_\_ Socially Efficient Quantity: \_\_\_\_\_\_\_\_\_\_

b) Market Equilibrium Price: \_\_\_\_\_\_\_\_\_\_ Deadweight Loss: \_\_\_\_\_\_\_\_\_\_

// plass:comment
// | Editor. Source. The story and Q1 are 24F Demo C1, "Somethin’s Up With Pumpkins", Q1 (of 3) "Market Equilibrium" (ECON_0100/Checkpoints/C/_Archive/24F_Demo_C.md, +pdf), verbatim. Left out: the MiniExam timing line and the Academic Conduct Code, the story title (the Part B Vignettes have none), and the "(of 3)". Q2–Q3 of that demo are Vignette C3.
// | Answers. MSC = 10 + Q + 10 = 20 + Q; MSB = MB = 100 − Q. Market: 100 − Q = 10 + Q, Q 45, P 55. Efficient: 100 − Q = 20 + Q, Q 40 (P 60). DWL = ½ · 10 · (45 − 40) = 25. Matches the ink key Demo_C_sols.pdf (45, 55, 40, 25).
// | Flags. These curves (100 − Q, 10 + Q) differ from Vignette C2's (17 − Q/6, 2 + 2Q/3) and old Vignette C1's; the stories are separate, so both are kept.
// | Gap: C1.2 Positive Externalities.
// /plass:comment
