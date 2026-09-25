// ECON 0100 handout. This file is the source; export the PDF from Plass.
#set page(paper: "us-letter", margin: (top: 1in, right: 0.5in, bottom: 1in, left: 0.5in), numbering: "1", number-align: center)
#set par(justify: true, leading: 10.215pt, spacing: 21.465pt)
#set text(size: 12.5pt, font: "New Computer Modern", hyphenate: true)
#show heading.where(level: 1): set text(size: 23.750pt)
#show heading.where(level: 1): set block(above: 26.391pt, below: 25.105pt)
#show heading.where(level: 2): set text(size: 14.375pt)
#show heading.where(level: 2): set block(above: 38.410pt, below: 18.473pt)
#show math.equation.where(block: true): set block(above: 21.490pt, below: 23.702pt)
#set math.equation(numbering: "(1)")
#import "@preview/mitex:0.2.5": mi, mitex

= ECON 0100 | Exercise B1 | Demand

Pumpkin pasties sell along the demand curve $P = 12 - Q/2$, in galleons and #strike[thousands of] pasties.

// ED: UNITS (2026-09-15, per chat) — quantities are now in individual pasties; the equation stays the same. Remove the struck words to accept. For the surplus triangle, explicitly carry B1's divisible-good assumption into this example in your own words: fractional pasties can be bought. "Individual pasties" specifies the scale, not a restriction to whole purchases. Under that continuous model, Q1(a) = 4 pasties, Q1(b) = 10 galleons per pasty, Q2(a) = 14 pasties, and Q2(b) = 49 galleons. If only whole pasties are allowed and each is valued at the line's right endpoint, the corresponding surplus would be 45.5 galleons. My pick is to keep the divisible model just taught. The existing PDF has not been re-exported from these review marks.

== Q1 | Quantity Demanded

a) What is the quantity demanded at 10 galleons? \_\_\_\_\_\_\_\_\_\_

b) What is the marginal benefit at a quantity of 4 #strike[thousand]? \_\_\_\_\_\_\_\_\_\_

== Q2 | Consumer Surplus

Pumpkin pasties again, $P = 12 - Q/2$.

a) What is the quantity demanded at 5 galleons? \_\_\_\_\_\_\_\_\_\_

b) Find and label the consumer surplus at that price.
