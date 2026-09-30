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

= ECON 0100 | Exercise C4 | Corrective Taxes

{++Smoked toffee again, with the same curves and 10 Galleon smoke cost as Q2 of Exercise C3:++}

#mitex(`
D: P_b = 100 - Q_d \qquad\qquad S: P_s = 10 + Q_s
`)

== Q1 | Policy Proposal

What type and size of policy would you propose to eliminate the DWL you identified in {++Q2 of Exercise C3++} #strike[Question 1]?

~

~

~

~

Policy Type: \_\_\_\_\_\_\_\_\_\_ Policy Size: \_\_\_\_\_\_\_\_\_\_

Buyer Price: \_\_\_\_\_\_ Seller Price: \_\_\_\_\_\_ Post-Policy Quantity: \_\_\_\_\_\_

~

== Q2 | Deadweight Loss Intuition

If the marginal cost of a gallon of gas is \$4.00, the negative externality is \$1.00, and the marginal benefit is \$4.50, what is the deadweight loss?

Deadweight Loss: \_\_\_\_\_\_\_\_\_\_

// plass:comment
// | Editor. Built 2026-09-29. Series story: Smoked Toffee (Exercises). Taylor’s text, verbatim; the opening line and the "Q2 of Exercise C3" cross-reference are mine.
// | Sources. Q1: Checkpoints/C/_Archive/MiniExam_C_v3.md Question 2 (23F Version 1; the same exam as 24F MiniExam_C_v5.md). Q2: MiniExam_C_v3.md Question 3. The other number set is 23F/24F Version 2, MiniExam_C_v4.md and MiniExam_C_v6.md: curves 90 − Q_d and 20 + Q_s, and in Q2 a negative externality of $1.50.
// | Answer key (checked against the ink key Checkpoints/C/_Archive/ME_C_v1_sols.pdf). Q1: a tax of 10 galleons; the buyers’ price equals the sellers’ price plus 10, so 100 − Q = 10 + Q + 10, Q = 40, buyer price 60, seller price 50, post-policy quantity 40, and the DWL is gone. Q2: MSC = 4.00 + 1.00 = 5.00 is more than MB = 4.50, so this exchange’s DWL is 0.50. Version 2 numbers: tax 10, buyer price 60, seller price 50, quantity 30; Q2 DWL 1.00.
// | Gaps: none for C4.1. The corrective subsidy (a positive externality) has no smoked toffee material.
// | Flag: Q2 is a single-exchange question about gas, not smoked toffee. The skillsheet lists this skill under C3.1 (decision (4) there), so it could move to Exercise C3.
// /plass:comment
