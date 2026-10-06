#set page(paper: "us-letter", margin: 0.65in, numbering: "1")
#set text(font: "New Computer Modern", size: 11pt)
#set par(leading: 0.6em)
#set heading(numbering: none)
#show heading.where(level: 1): set text(size: 18pt)
#show heading.where(level: 2): set text(size: 13pt)
#let blank = underline[ #h(1.1in) ]
#let axes = box(width: 100%, height: 1.55in, inset: 8pt, stroke: 0.4pt + gray)[P #h(1fr)
#v(1fr) Q]
= Checkpoint C | Version 1 | Key and pass criteria

== Q1 | C1.1 Trade

$Q_d = 40$, $Q_s = 8$, imports $=32$. Buyers gain, sellers lose, domestic total surplus rises.

*Pass:* Calculates domestic quantities and the gap as imports, and correctly identifies the welfare directions. No before/after surplus arithmetic is required. The given no-trade price is 10.

== Q2 | C1.2 Tariffs

Domestic price $=6+2=8$; $Q_d=32$, $Q_s=16$, imports $=16$; revenue $=2 times 16=32$. Relative to free trade, buyers lose and sellers gain.

*Graph:* Free-trade price 6 and tariff price 8. Production DWL lies between supply and the world price from $Q=8$ to $16$; consumption DWL lies between demand and the world price from $Q=32$ to $40$. The revenue rectangle is not DWL.

*Pass:* Uses world price plus tariff, computes imports and tariff revenue, identifies welfare directions, and locates both DWL regions. Do not require numerical area or surplus-change calculations. The two areas would each be 8, but that is not assessed.
