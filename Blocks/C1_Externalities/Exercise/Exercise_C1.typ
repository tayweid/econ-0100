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

= ECON 0100 | Exercise C1 | Externalities

== Q1 | Market Equilibrium

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
// | Editor. Built 2026-09-29. Series story: Smoked Toffee (Exercises). Taylor’s text, verbatim apart from the typo fixes listed below. 2026-10-06: externalities now come before taxes, so "The Effects on Residents" (the old Q1 a–b, which needs Exercise C2’s tax) moved to Exercise C3; the old Q2 is now Q1.
// | Sources. Q1: Checkpoints/C/_Archive/MiniExam_C_v3.md Question 1 (23F Version 1; the same exam as 24F MiniExam_C_v5.md). The other number set is 23F/24F Version 2, MiniExam_C_v4.md and MiniExam_C_v6.md: D: P_b = 90 − Q_d, S: P_s = 20 + Q_s, same 10-galleon cost.
// | Typo fix: "a cost of 10 Galleon" to "10 Galleons".
// | Answer key. Q1 (ink key Checkpoints/C/_Archive/ME_C_v1_sols.pdf): market 100 − Q = 10 + Q, Q = 45, P = 55; efficient 100 − Q = 20 + Q, Q = 40; DWL = ½ · 10 · 5 = 25. Version 2 numbers: market Q = 35, P = 55; efficient Q = 30; DWL = 25.
// | Gap: C1.2 Positive Externalities. No smoked toffee material.
// /plass:comment
