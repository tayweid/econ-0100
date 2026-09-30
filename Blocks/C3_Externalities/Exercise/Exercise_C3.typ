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

= ECON 0100 | Exercise C3 | Externalities

{++Smoked toffee again, with the same curves and 2 Galleon tax as Exercise C2:++}

#mitex(`
D: P_b = 20 - \frac{1}{2} Q_d \qquad\qquad S: P_s = Q_s
`)

== Q1 | The Effects on Residents

a) This policy had an unintended consequence. The proliferation of smoked toffee makers meant the town saw a subsequent rise in _smoke_. Wood smoke is harmless at low levels, but can cause lung issues at the higher concentrations experienced in Hogsmeade. Use a graph to discuss the unintended effect the tax had on air quality. No need to discuss welfare.

~

~

~

~

b) Public health officials have estimated the externality to be equal to 2 Galleons per unit of smoked toffee produced. Use a graph to find the socially efficient quantity of smoked toffee and deadweight loss associated with the wood smoke. How does the socially efficient quantity compare to the tax equilibrium in Q1{++ of Exercise C2++}?

~

~

~

~

#pagebreak()

== Q2 | Market Equilibrium

Hogsmeade has seen a recent proliferation of candy shops selling smoked toffees. The Demand (marginal benefit) curve and Supply (marginal cost) curve for smoked toffee can be represented using the following relationships.

#mitex(`
D: P_b = 100 - Q_d \qquad\qquad S: P_s = 10 + Q_s
`)

The proliferation of smoked toffee makers has meant the town saw a subsequent rise in _smoke_. Wood smoke can cause lung issues and carries a cost of 10 Galleons to the health of Hogsmeade residents.

Use a graph and algebra to find equilibrium price, quantity, and DWL. Be sure to show your work.

~

~

~

~

Market Equilibrium Price: \_\_\_\_\_\_\_\_\_\_ Market Equilibrium Quantity: \_\_\_\_\_\_\_\_\_\_

Socially Efficient Quantity: \_\_\_\_\_\_\_\_\_\_ Deadweight Loss: \_\_\_\_\_\_\_\_\_\_

// plass:comment
// | Editor. Built 2026-09-29. Series story: Smoked Toffee (Exercises). Taylor’s text, verbatim apart from the typo fixes listed below; the opening line and "of Exercise C2" in Q1 b) are mine.
// | Sources. Q1 a): Checkpoints/C/_Archive/24F_Demo_C2.md part C "The Effects on Residents" (same text in MiniExam_C_demo_v1.md and MiniExam_C_demo_v2.md part C, and the bank stem Checkpoints/C/_Archive/C1.1_smoked-toffee-residents.md). Q1 b): C_Practice_Bank/Vignette_C1_smoked-toffee_F24.md Q2 (also titled "The Effects on Residents"; not in the stub’s plan, but it is this series’ story and the only numeric version of the smoke on these curves). Q2: Checkpoints/C/_Archive/MiniExam_C_v3.md Question 1 (23F Version 1; the same exam as 24F MiniExam_C_v5.md). The other number set is 23F/24F Version 2, MiniExam_C_v4.md and MiniExam_C_v6.md: D: P_b = 90 − Q_d, S: P_s = 20 + Q_s, same 10-galleon cost.
// | Typo fixes: "a unintended" to "an unintended" (the bank stem had kept it); "a cost of 10 Galleon" to "10 Galleons".
// | Answer key. Q1 a) (ink key Checkpoints/C/_Archive/Demo_C2_sols.pdf): smoke comes from production, so the tax’s cut in quantity (40/3 to 12) cut smoke and air quality improved; with an externality of 2 the tax quantity is the socially optimal one, as if toffee makers internalized the cost of wood smoke. Q1 b) (ink key C_Practice_Bank/Vignette_C1_smoked-toffee_sols_F24.pdf): MSC = Q + 2 = 20 − Q/2, so the socially efficient quantity is 12; DWL = ½ · 2 · (40/3 − 12) = 4/3 ≈ 1.33; the efficient quantity equals the tax equilibrium quantity. Q2 (ink key Checkpoints/C/_Archive/ME_C_v1_sols.pdf): market 100 − Q = 10 + Q, Q = 45, P = 55; efficient 100 − Q = 20 + Q, Q = 40; DWL = ½ · 10 · 5 = 25. Version 2 numbers: market Q = 35, P = 55; efficient Q = 30; DWL = 25.
// | Gap: C3.2 Positive Externalities. No smoked toffee material.
// | Flag: two curve sets in one series. Q1 and Exercise C2 use 20 − Q/2 and Q with a 2-galleon externality; Q2 (and Exercise C4) use 100 − Q and 10 + Q with a 10-galleon cost. Both kept as written.
// | Flag: Q1 a) and b) share one title in their sources, so they sit under one heading as a) and b).
// /plass:comment
