// Exported from Plass
#set page(paper: "us-letter", margin: 0.6in, numbering: "1", number-align: center)
#set par(justify: true, leading: 8.172pt, spacing: 17.172pt)
#set list(spacing: 10.672pt)
#set enum(spacing: 10.672pt)
#set grid.cell(breakable: false)
#show heading.where(level: 1): set text(size: 19.000pt)
#show heading.where(level: 1): set block(above: 21.113pt, below: 20.084pt)
#show heading.where(level: 1): set par(leading: 10.777pt)
#show heading.where(level: 2): set text(size: 14.000pt)
#show heading.where(level: 2): set block(above: 35.720pt, below: 15.950pt)
#show heading.where(level: 2): set par(leading: 7.941pt)
#show heading.where(level: 3): set text(size: 11.500pt)
#show heading.where(level: 3): set block(above: 30.728pt, below: 14.778pt)
#show heading.where(level: 3): set par(leading: 6.523pt)
#show heading.where(level: 4): set text(size: 11.500pt)
#show heading.where(level: 4): set block(above: 30.728pt, below: 14.778pt)
#show heading.where(level: 4): set par(leading: 6.523pt)
#show heading.where(level: 5): set text(size: 11.500pt)
#show heading.where(level: 5): set block(above: 30.728pt, below: 14.778pt)
#show heading.where(level: 5): set par(leading: 6.523pt)
#show heading.where(level: 6): set text(size: 11.500pt)
#show heading.where(level: 6): set block(above: 30.728pt, below: 14.778pt)
#show heading.where(level: 6): set par(leading: 6.523pt)
#show raw.where(block: false): set text(font: "DejaVu Sans Mono", size: 8.000pt)
#show math.equation.where(block: true): set block(above: 17.192pt, below: 18.962pt)
#set text(size: 10pt, font: "New Computer Modern", hyphenate: true)
#import "@preview/mitex:0.2.5": mi, mitex

= ECON 0100 | Demo C

Demos are similar to Checkpoints, often taken directly from past semesters. Work through the problems and check your work against mine. Practice answering clearly and completely. Show your work so someone else can understand your thought process. You are encouraged to work in small groups. Find a study room, grab some classmates, and work together on a whiteboard.

== Glittering Gum

Hogsmeade has recently seen a surge in shops selling Glittering Gum, a magical candy that makes the consumer’s words sparkle and glisten as they speak. The Demand (marginal benefit) curve and Supply (marginal cost) curve for Glittering Gum can be represented using the following relationships:

#mitex(`
D: P_b = 60 - Q_d \qquad\qquad S: P_s = 10 + Q_s
`)

However, a magical externality has arisen: the widespread chewing of Glittering Gum has led to an increase in “Starlight Sneeze,” a condition where non-consumers start sneezing out harmless but bothersome glitter. This condition imposes an inconvenience cost of 10 {++coins++} #strike[Galleons] to both consumers and non-consumers in Hogsmeade.

== Q1 | Market Equilibrium (C3.1)

Use a graph and algebra to find equilibrium price, quantity, and DWL. Be sure to show your work. #strike[(continued below)]

a) Market Equilibrium Price: \_\_\_\_\_\_\_\_\_\_ Market Equilibrium Quantity: \_\_\_\_\_\_\_\_\_\_

b) Socially Efficient Quantity: \_\_\_\_\_\_\_\_\_\_ Deadweight Loss: \_\_\_\_\_\_\_\_\_\_

== Q2 | Policy Proposal (C4.1)

What type and size of policy would you propose to eliminate the DWL you identified in Question 1?

a) Policy Type: \_\_\_\_\_\_\_\_\_\_ Policy Size: \_\_\_\_\_\_\_\_\_\_

b) Buyer Price: \_\_\_\_\_\_\_\_\_\_ Seller Price: \_\_\_\_\_\_\_\_\_\_ Post-Policy Quantity: \_\_\_\_\_\_\_\_\_\_

== Q3 | Deadweight Loss Intuition (C3.1)

If the marginal cost of a gallon of gas is \$4.00, the negative externality is \$2.50, and the marginal benefit is \$4.50, what is the deadweight loss?

a) Deadweight Loss: \_\_\_\_\_\_\_\_\_\_

// plass:comment
// | Editor. Demo C is Glittering Gum and the Starlight Sneeze, the Fall 2023 MiniExam Z (your ink key is headed "FALL 2023"), laid out like Demo B: the Checkpoint's question order, each question tagged by skill, and coins for galleons. The story and all three questions are verbatim. The only changes: the two curves share one display line as in Demo B; the exam's answer blanks are lettered a) and b) as in Demo B; "(continued below)" is struck because it pointed across an exam page break; the exam's intro and academic conduct pledge are left out, as in Demo B. No typos needed fixing. No wording of mine besides {++coins++}.
// | Sources. Base text: Checkpoints/C/_Archive/MiniExam_Z_v1.md. The same exam, word for word, is in Checkpoints/C/_Archive/MiniExam_Z_v2.md (the "_arch" copy, blanks on separate lines), Checkpoints/C/_Archive/MiniExam_Z_v2.pdf (the typeset exam), and Checkpoints/Z/MiniExam_Z_v1.md (recomposed from the three banked stems). None has a sentence or sub-question the others lack. Ink key: Checkpoints/Z/MEZ_sols.pdf (Taylor's Version, Fall 2023). Grading notes: Checkpoints/Z/MiniExam_Z_Q1_rubric_email.pdf (Q1) and Checkpoints/Z/MEZ_Q2_Q3.pdf (Q2 and Q3), emails to the TAs from 12/15/2023.
// | Answers. Q1: MB = MC gives 60 − Q = 10 + Q, so Q = 25 and P = 35. MSC = 10 + Q + 10 = 20 + Q, and MSB = MSC gives Q = 20. DWL = ½ · 10 · 5 = 25 (the height is MSC − MB = 45 − 35 at Q = 25). a) 35, 25; b) 20, 25. Q2: a) tax, 10 per unit; b) buyers pay 60 − 20 = 40, sellers get 10 + 20 = 30, quantity 20. Q3: MSC = 4.00 + 2.50 = 6.50 is above MB = 4.50, so the gallon shouldn't be exchanged and a) DWL = \$2.00. All match the ink key (Q1 35, 25, 20, 25; Q2 tax, 10, 40, 30, 20; Q3 2).
// | Gaps: C1.1 International Trade, C1.2 Tariffs, C2.1 Taxes & Incidence, C2.2 Subsidies. MiniExam Z has nothing for C1 or C2 (Q2's corrective tax touches C2.1's buyer and seller prices but not incidence, revenue, or DWL from a tax). C3.2 Positive Externalities is also untested here.
// | Flags. (1) Q3 is tagged C3.1, where Skillsheet C now puts the single-exchange "Deadweight Loss Intuition"; if decision (4) moves it into C4.1, retag it C4.1. It stays third, as on the exam. (2) Q3 keeps its dollars: it's a real-world gallon of gas, not galleons; say if you want coins there too. (3) Checkpoints/C/_Archive/MiniExam_Z_v1.md is headed "Fall 2024", but the ink key says Fall 2023 and the 24F MiniExam Z is the Wandmakers exam (Checkpoints/Z/ME_Z_sols.pdf); Glittering Gum is 23F. (4) The ink key's Q3 working reads "4.50 − 4.00 − 2.20 = −2", a slip for 2.50; its answer, 2, is right.
// /plass:comment
