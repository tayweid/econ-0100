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

= ECON 0100 | Vignette C1 | Tariffs

_Due in Recitation. Vignettes are a certificate of the work done together in Recitation._

Members of the wizarding world have preferences for pumpkin pasties according to the following demand curve:

#mitex(`
P_d = 14 - \frac{1}{2} Q_d
`)

Pumpkin pasties are produced by many sellers according to the following supply curve:

#mitex(`
P = 2 + \frac{1}{2} Q_s
`)

Prices are in galleons and quantity is in pasties.

== Q1 | {++The UK’s Pumpkin Pasties++}

Economic historians remember a time before the Ministry lifted barriers to exports and imports of {++pumpkin pasties++} #strike[lemon tarts]. The global price was 6 galleons. However, due to the trade barriers the UK did not #strike[did not] have access to this market for {++pasties++} #strike[tarts]. {++The UK’s domestic supply and demand curves are the ones above.++}

Use a graph and algebra to illustrate what happened to the market after the trade barrier was lifted.

a) Imports or exports? _imports, exports_

b) Quantity demanded: \_\_\_\_\_\_ Quantity supplied: \_\_\_\_\_\_ Imports: \_\_\_\_\_\_

c) Consumer surplus before: \_\_\_\_\_\_ after: \_\_\_\_\_\_

d) Producer surplus before: \_\_\_\_\_\_ after: \_\_\_\_\_\_

e) Change in total surplus: \_\_\_\_\_\_\_\_\_\_

f) Buyers: _gain, lose_ Sellers: _gain, lose_

== Q2 | {++Egypt’s Pumpkin Pasties++}

While the supply curve is very similar to that of the UK, demand for {++pumpkin pasties++} #strike[lemon tarts] is much lower in Egypt’s wizarding community, leading to a domestic price below the global price. Use a graph (_but no algebra_) to illustrate what happened to the market after Egypt lifted their ban on international trade of {++pumpkin pasties++} #strike[lemon tarts].

a) Egypt _imports, exports_

b) Buyers: _gain, lose_ Sellers: _gain, lose_

c) Total surplus: _rises, stays the same, falls_

~

~

== Q3 | {++A Rising World Price++}

{++Back in the UK, suppose the global price rises from 6 to 7 galleons.++}

a) Quantity demanded: \_\_\_\_\_\_ Quantity supplied: \_\_\_\_\_\_ Imports: \_\_\_\_\_\_

b) Imports have: _risen, stayed the same, fallen_

#pagebreak()

== Q4 | International Pumpkin Pasties

Economic historians in the wizarding world remember a time before the Ministry had begun meddling with the domestic market. In those earlier days, trade barriers had been lifted for exports of pumpkin pasties to international magical markets with a world price of 12 galleons. At the time, the Ministry of Magic used this opportunity to pad its coffers without facing the political backlash associated with a domestic tax, instead imposing an import tariff of 1 {++galleon++} #strike[galleons]. The supply and demand curves:

#mitex(`
P = 17 - \frac{1}{6} Q_D
`)

#mitex(`
P = 2 + \frac{2}{3} Q_S
`)

Use a graph to illustrate what happened to the market after the tariff was imposed.

~

~

What is the area of the deadweight loss from the tariff? \_\_\_\_\_\_\_\_\_\_

#pagebreak()

== Q5 | International Pumpkin Pasties

Economic historians in the wizarding world remember a time before the Ministry had begun meddling with the domestic market. In those earlier days, trade barriers had been lifted for exports of pumpkin pasties to international magical markets with a world price of 16 galleons. The Ministry of Magic imposed an export subsidy of 1 galleon. The supply and demand curves:

#mitex(`
P = 17 - \frac{1}{6} Q_D
`)

#mitex(`
P = 2 + \frac{2}{3} Q_S
`)

Use a graph to illustrate what happened to the market after the export subsidy was imposed.

~

~

What is the area of the deadweight loss from the {++subsidy++} #strike[tariff]? \_\_\_\_\_\_\_\_\_\_

// plass:comment
// | Editor. Sources. Q1–Q3 are copied verbatim from B6_Trade/Vignette/Vignette_B6.typ (Fall 2026 draft; B6 did not run), with its {++ ++} and #strike markup unchanged; that draft took Q1–Q2 from 24F Vignette B4 ("UK’s Lemon Tarts", "Egypt’s Lemon Tarts", C1_Tariffs/Practice_Bank/Vignette_B4_v2.md) with lemon tarts swapped for pasties, and "did not did not" is the source's typo. The B6 file is left in place. Q4 is 24F Demo X1 (ECON_0100/Checkpoints/C/_Archive/24F_Demo_X1.md; stem C2.1_intl-pumpkin-pasties-tariff.md is the same text). Q5 is 24Fb Demo X3 (Checkpoints/C/_Archive/24Fb_Demo_X3.md; 24F_Demo_X3.md and stem C2.1_intl-pumpkin-pasties-export-subsidy.md are the same text).
// | Other number sets. Q4 uses Demo X1's 1-galleon tariff. 24F Demo D4 (Checkpoints/C/_Archive/24F_Demo_D4.md) is the same question with a 2-galleon tariff, and "Use a graph…" placed before the curves. The 21F original is Homework 3 Part 5 (C_Practice_Bank/Homework_3_pasties-tax_F21.md): "In recent years, trade barriers were lifted for exports… The Ministry of Magic used this opportunity to pad its coffers by imposing an export tariff of 2 galleons", same curves, world price 12. Q5 has one number set.
// | Typo fixes, each marked in the text: Q4 "1 galleons" → "1 galleon"; Q5 "deadweight loss from the tariff" → "from the subsidy" (the stem already made this fix).
// | Answers. Q1 imports; Qd 16, Qs 8, imports 8; CS 36 → 64; PS 36 → 16; TS +8; buyers gain, sellers lose. Q2 exports; buyers lose, sellers gain; TS rises. Q3 Qd 14, Qs 10, imports 4 (fallen). (Q1–Q3 as B6's draft key; rechecked.)
// | Q4: no trade Q 18, P 14; free trade at 12: Qd 30, Qs 15, imports 15, CS 75, PS 75; tariff price 13: Qd 24, Qs 16.5, imports 7.5, CS 48, PS 90.75, tariff revenue 7.5; DWL = ½·1·1.5 + ½·1·6 = 3.75. Matches the ink keys Demo_X1_sols.pdf and Demo_X1_repo.pdf (3.75, 15/4). With D4's 2-galleon tariff (and HW3 Part 5), the price rises to 14 = the no-trade price, imports fall to 0, revenue 0, DWL = ½·2·3 + ½·2·12 = 15.
// | Q5: world 16 is above the no-trade price 14, so exports. Free trade: Qd 6, Qs 21, exports 15, CS 3, PS 147. With the subsidy the domestic price is 17: Qd 0, Qs 22.5, exports 22.5, CS 0, PS 168.75, subsidy cost 22.5; DWL = ½·1·6 + ½·1·1.5 = 3.75. No ink key for these numbers: Demo_X3_sols.pdf prints world price 12 with "an export subsidy of 1 galleon" (and X1's "pad its coffers" sentence), and its ink works an import tariff (price 13, DWL 15/4), i.e. Demo X1.
// | Flags. (1) Two curve sets: Q1–Q3 use the Vignette B-series curves (14 − Q/2, 2 + Q/2, world price 6); Q4–Q5 use the Demo X curves (17 − Q/6, 2 + 2Q/3). Both kept as written. (2) Q3 is not Taylor's: B6's editor note says the previous editor wrote it for the B6.1 world-price bullet; its stem is marked but its blanks are not. Cut it if unwanted. (3) Q4's story says barriers were lifted "for exports" but the case is an import tariff (world 12 < 14); source wording kept. (4) Q5's 1-galleon subsidy lifts the domestic price to 17, the demand intercept, so domestic consumption is zero. (5) Q4 and Q5 share the source title "International Pumpkin Pasties".
// | Gaps: none for C1.1 or C1.2. Q2 is graph-only (no algebra), as in the source.
// /plass:comment
