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

= ECON 0100 | Exercise C2 | Taxes

In recent years Hogsmeade has seen a proliferation of candy shops selling smoked toffees. The Demand (marginal benefit) curve and Supply (marginal cost) curve for smoked toffee can be represented by the following relationships.

#mitex(`
D: P_b = 20 - \frac{1}{2} Q_d \qquad\qquad S: P_s = Q_s
`)

Due to the metabolic issues among the younger generation of wizards in the community resulting from the consumption of these high glycemic index treats, the Ministry of Magic imposed a 2 Galleon tax on the sale of smoked toffee.

== Q1 | Tax Equilibrium

Use a graph and algebra to discuss the impact of the tax on the market. No need to include welfare measures here.

~

~

~

~

~

~

#pagebreak()

== Q2 | Post-Tax Welfare

Identify the post-tax welfare on the graph. Be sure to include how the welfare areas changed after the policy. No need to do any calculation here: I’m looking for a graphical and intuitive description of what happened to welfare after the policy. Be as clear as possible.

~

// plass:comment
// | Editor. Built 2026-09-29. Series story: Smoked Toffee (Exercises). Taylor’s text, verbatim apart from the typo fixes listed below.
// | Sources. Stem, Q1 and Q2: Checkpoints/C/_Archive/MiniExam_2_v3.md (22F MiniExam 2, Parts 1–2), with the stem’s "Due to" from Checkpoints/C/_Archive/24F_Demo_C2.md. Every version has the same numbers (20 − Q/2, Q, 2-galleon tax), so there is no other number set: MiniExam_2_v1.md (21F notebook), MiniExam_2_v2.md (21F), MiniExam_2_v4.md (22F unused), 24F_Demo_C2.md parts A–B, MiniExam_C_demo_v1.md and MiniExam_C_demo_v2.md parts A–B (22F demo). C_Practice_Bank/Vignette_C1_smoked-toffee_F24.md Q1 is the same question with Q1 and Q2 folded into one prompt ("Include but do not calculate welfare measures and discuss what changed after the policy").
// | Typo fixes: "Due the" to "Due to" (Taylor’s own 24F fix); "glicemic" to "glycemic".
// | Answer key (checked against the ink keys Checkpoints/C/_Archive/miniexam_2_sols.pdf and C_Practice_Bank/Vignette_C1_smoked-toffee_sols_F24.pdf; both agree). Before the tax: Q = P = 40/3 ≈ 13.33. Q1: the buyers’ price equals the sellers’ price plus 2, so 20 − Q/2 = Q + 2, Q = 12, buyers’ price 14, sellers’ price 12. Quantity falls, the buyers’ price rises by 2/3 and the sellers’ price falls by 4/3, so sellers bear more of the tax. Q2 (areas; no calculation asked): CS 400/9 ≈ 44.44 to 36, PS 800/9 ≈ 88.89 to 72, government revenue 24, DWL 4/3 ≈ 1.33. In the ink key’s labels, Gov = A + B, DWL = C + D, ΔCS = −A − C, ΔPS = −B − D.
// | Gap: C2.2 Subsidies. No smoked toffee subsidy material.
// | Flag: the vignette gives the tax a different motive: "To raise government funds the Ministry of Magic imposed a 2 Galleon tax on the sale of smoked toffee." It is not placed, since the stem already has the metabolic motive; swap it in if you prefer it. The vignette also writes demand in Q_b rather than Q_d.
// | Flag: the vignette’s Q2 (the 2-galleon smoke externality) is placed in Exercise C3 Q1 b).
// /plass:comment
