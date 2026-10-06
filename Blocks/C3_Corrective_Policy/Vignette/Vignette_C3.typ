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

= ECON 0100 | Vignette C3 | Corrective Taxes

_Due in Recitation. Vignettes are a certificate of the work done together in Recitation._

Residents of Hogsmeade enjoy pumpkin pasties year round. The Demand (marginal benefit) curve and Supply (marginal cost) curve for pumpkin pasties can be represented using the following relationships.

#mitex(`
D: P_b = 100 - Q_b
`)

#mitex(`
S: P_s = 10 + Q_s
`)

However, a recent report conducted by the Daily Profit conclusively established a link between the consumption of pumpkin pasties and accidental magical spells, with a cost to society of 10 galleons.

== Q1 | Policy Proposal

What type and size of policy would you propose to eliminate the DWL you identified in {++Vignette C1++} #strike[Q1]?

~

~

a) Policy Type: \_\_\_\_\_\_\_\_\_\_ Policy Size: \_\_\_\_\_\_\_\_\_\_

b) Buyer Price: \_\_\_\_\_\_ Seller Price: \_\_\_\_\_\_ Post-Policy Quantity: \_\_\_\_\_\_

== Q2 | Deadweight Loss Intuition

If the marginal cost of a gallon of gas is \$4.00, the negative externality is \$1.00, and the marginal benefit is \$4.50, what is the deadweight loss of this gallon of gas?

a) Deadweight Loss: \_\_\_\_\_\_\_\_\_\_

// plass:comment
// | Editor. Source. The story (repeated from Vignette C1) and Q1–Q2 are 24F Demo C1, "Somethin’s Up With Pumpkins", Q2 (of 3) "Policy Proposal" and Q3 (of 3) "Deadweight Loss Intuition" (ECON_0100/Checkpoints/C/_Archive/24F_Demo_C.md, +pdf), verbatim except "in Q1" → "in Vignette C1", marked. Q2 keeps the source's dollars.
// | Answers. Q1: a tax of 10 galleons (the external cost); buyer price 100 − 40 = 60, seller price 10 + 40 = 50, quantity 40; buyers' price up 5 from 55, sellers' down 5. Revenue 10 · 40 = 400. Q2: MSC = 4.00 + 1.00 = 5.00 > MB 4.50, so DWL = 0.50. Matches the ink key Demo_C_sols.pdf (tax, 10, 60, 50, 40; 0.50).
// | Flags. (1) Q1 refers back to the DWL found in Vignette C1 (25 galleons); the story is repeated here so C3 stands alone. Cut it if C1 and C3 run in one recitation. (2) Q2 is a gas example in dollars, not pasties; source kept. It is the single-exchange bullet that Skillsheet C lists under C1.1 (decision 4 on the Skillsheet).
// | Gaps: none for C3.1's tax side. The subsidy side of C3.1 (a corrective subsidy for a positive externality) and the WTP/WTS price-setting bullet have no pasty source.
// /plass:comment
