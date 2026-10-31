---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

## Episode E5 | Wrap-Up

<!--
Review correction, 2026-10-30 (fresh-eyes review of the first build): the best-response graph in section 4 now runs to 400 on both axes, as in E4, so BR_A and BR_B each run from axis to axis as on the sheet (supersedes 0 to 240, where both lines stopped at the graph's edge); ATC is drawn from q = 6 (ATC 98) instead of q = 3, so it no longer runs up the price axis on either graph; the side solve sits closer under the card, so 4.b.symmetry's five lines clear the bottom line; the competitive market graph sits 0.25 further right, so the firm's MR name and the market's P* = 50 no longer read as one phrase; section 1 sits 0.25 lower; the rolling P = and n = readouts have a wider gap after the equals sign. Added to Choices left for Taylor: 4.c's bottom line and the side line "Many sellers: MR ≈ P". Added to Not built: the E2 cue at the limit.
Animation storyboard for E5_Animation.py, scene EpisodeE5. Drafted and built 2026-10-30 from Taylor's request: "B5 is a wrapup, covering the three models and how they relate, through n, so basically cournot." There are no spoken notes for E5 yet; Taylor writes them. The quote blocks below are animation directions in playback order, not replacement prose. On-screen lines in quotes are what the build shows; every line not taken from Taylor's own words is listed under Choices left for Taylor.
Source: his handwritten sheet "Example: Three Market Structures" (Part_E/E4_Duopoly/04_Handwritten.pdf, two pages): the header (D: P = 200 - Q/2; MC = 20 + q, "all firms are similar"), the three columns (monopoly, duopoly, competitive), the firm's problem card, the monopoly solution and graph, the duopoly best responses and Nash equilibrium, and the competitive firm and market graphs. Section 6 extends the sheet's duopoly MR to n sellers (Cournot), and section 7 puts the three outcomes on one market.
References: C4_Animations.py for the wrap-up shape and the step card beside the graph (current step gold, the rest grey, all white at the close); C2/C3 for the market graph, red readouts, the side solve right of a grey divider and one-unit strips; B5 for tracker-driven readouts; D3 for the flat Scene and the bumper with no thesis.
Model (one market for the whole episode): demand P = 200 - Q/2; every firm MC = 20 + q; fixed cost FC = 450, so ATC = 450/q + 20 + q/2 (FC is not on the sheet: inferred so the competitive firm's long run sits at the bottom of ATC, q = 30 and ATC = 50, as the sheet draws and states). Monopoly: MR = 200 - q; MR = MC at q* = 90; P* = 155; MC there 110; ATC* = 70; profit (155 - 70)(90) = 7,650. Socially efficient quantity where MC meets demand: Q_sp = 120 at P = 140; DWL = (1/2)(155 - 110)(120 - 90) = 675 (not shown as a number). Duopoly: BR_A: q_A = 90 - q_B/4; BR_B: q_B = 90 - q_A/4; Nash q_A* = q_B* = 72, Q = 144, P* = 128 (the sheet stops there; ATC(72) = 62.25 and profit 4,734 each are not shown). Competitive (the sheet's S: P = 20 + Q/10 is ten such firms): Q* = 300, P* = 50 = MR; q* = 30; ATC* = 50; profit 0. n sellers: MR_i = 200 - q_i - (1/2)(others' output) = P - q_i/2; with MR_i = MC, q = 360/(n + 3), Q = 360n/(n + 3), P = 200 - Q/2, P - MC = q/2. Stops: n = 1: q 90, Q 90, P 155, P - MC 45; n = 2: 72, 144, 128, 36; n = 3: 60, 180, 110, 30; n = 6: 40, 240, 80, 20; n = 15: 20, 300, 50, 10.
Note on n = 15: fifteen Cournot sellers land on the same market outcome (Q = 300, P = 50) as the sheet's ten price takers. That is a coincidence of these numbers, not a rule: the fifteen still price above marginal cost (P - MC = 10, each at q = 20 with MC = 40), where the price takers have none (q = 30, MC = 50). With FC = 450 those fifteen would also lose 50 each. n = 12 (q 24, Q 288, P 56, P - MC 12) is a stop that avoids the coincidence.
Conventions: the market graph's axes are the sheet's (Q to 400, P to 200, drawn to 220 so P sits above the 200 intercept); MC orange, ATC purple, demand and the price a firm takes teal, MR pink; firm A pink and firm B teal on the best-response graph (Part D's player colors), Nash red. Dots and drops at a crossing (MR = MC, the Nash point, supply meets demand, each outcome of n sellers) are red; a value read off one curve at q* is dashed in that curve's color (P* teal off demand, ATC* purple off ATC), the style guide's monopoly rule; the efficient quantity is yellow, as on the sheet. Results in the side solve are red and boxed, as on the sheet. Areas are one-unit strips: profit orange at 0.35, DWL grey at 0.8; at 400 units across the strips read nearly solid. Quantity readouts are two rows under the axis (number, then symbol); prices sit on the vertical axis. Titles name the topic; one yellow bottom line at a time.
Not built: duopoly ATC and profit (the sheet stops at P*); grey DWL for each structure in the summary (each structure has its own industry MC, 20 + Q, 20 + Q/2 and 20 + Q/10, so a shrinking DWL needs three MC curves or three panels: monopoly 675, duopoly 648, competitive 0); a firm-level picture of MR_i shrinking toward P as n grows (section 6 shows it as the P - MC bracket and the table; the outline's pink MR_i line under a teal price line, named P - MR, is the same gap, since MR_i = MC at each stop); the E2 cue at the limit (the competitive firm's flat teal MR = P line; 6.c says it in words only, "Many sellers: MR ≈ P"); the market-structures taxonomy (E1's object) at the top; a thesis line.
Choices left for Taylor: the bumper has no thesis line (C4's precedent; the lead's outline suggested the sheet's words "Three market structures." as a placeholder); the bottom lines written for this build, all replaceable: 1.b "What happens to price and quantity as sellers are added?", 2.a "Every seller solves the same problem.", 3.a "The monopolist faces the market's downward-sloping demand.", 3.b and 5.c "Every unit up to q* adds more to revenue than to cost.", 3.c "The price is what buyers will pay for q* units.", 3.d "Average total cost: the cost per unit of making q* units.", 3.e "Profit: the price minus the cost per unit, on each of the q* units.", 3.g "DWL: every unit between q* and Q_sp, from MC up to demand." (C4's pattern), 4.b.symmetry "Firm B's problem is the same, with A and B swapped.", 4.b "Neither firm can do better by changing its output alone.", 4.c "Two sellers: more output, lower price." (the lead's plain line from the E4 outline, which E4 also shows), 5.b "Step 0: supply and demand set the market price.", 5.d "A price taker sells every unit at the market price.", 5.e "Average total cost is at its lowest, right at the price.", 6.a "Each seller's MR is the price minus half its own output.", 6.b "More sellers: more output, a lower price, a price closer to marginal cost." (the outline's "... a smaller markup." reworded to match the table's P - MC); the side line at 6.c "Many sellers: MR ≈ P"; lines adapted from his words: 3.g.efficient "Q_sp: the socially efficient quantity, where marginal cost meets demand." (E3 notes), 4.a "Firm A's marginal revenue depends on how much firm B sells." (E4 notes), 5.a "Competitive firms are what we call price takers." (E2 notes), 6.c "A firm changing its quantity has no real effect on the price." (E2 notes, "This firm changing quantity..."); his own lines: 3.f "No entry, because it's a monopoly.", 5.f "π = 0. Long run equilibrium.", 5.g "No entry or exit." (the sheet) and 7.a "Market power leads to inefficient markets." (Part E's tagline on the course page). Also: the titles "Perfect Competition" (the sheet says Competitive) and "More Sellers"; the subtitles "One seller: Q = q_A.", "Two sellers: Q = q_A + q_B.", "Many sellers.", "n similar sellers." and "One market, three outcomes."; FC = 450; the n stops 1, 2, 3, 6, 15; the summary shows outcomes, not DWL.
-->

### 0 | Bumper

> **0.a.** Shared bumper, Part E | Episode 5. Thesis line left for Taylor.

### 1 | One Market

> **1.a.** Title “Three Market Structures”; subtitle “All firms are similar.” The sheet’s header, centered: D: P = 200 − ½Q in teal over MC = 20 + q in orange. No bottom line.

> **1.b.** The sheet’s three columns fade in left to right under the header with grey arrows between their names: Monopoly (MR_A = 200 − q_A in pink, Q = q_A) → Duopoly (MR_A = 200 − q_A − ½q_B in pink, MR_B = 200 − q_B − ½q_A in teal) → Competitive (S: P = 20 + (1/10)Q in orange). Bottom: “What happens to price and quantity as sellers are added?”

### 2 | The Firm’s Problem

> **2.a.** Title “The Firm’s Problem”. The sheet’s card, centered, in white: max over q of π = TR − TC, then its five steps one at a time: 1. MC = MR → q\*; 2. q\* → D → P\*; 3. q\* → ATC → ATC\*; 4. π\* = (P\* − ATC\*)·q\*; 5. If π\* ≥ 0 stay/enter; If π\* < 0 exit. Bottom: “Every seller solves the same problem.”

### 3 | Monopoly

> **3.a.** Title “Monopoly”; subtitle “One seller: Q = q_A.” The card shrinks into the right panel under a small azure “The Firm’s Problem” head, its steps grey, behind a grey divider. The market graph fades in: D (teal, 200 to 400), MR (pink, ending at 200, half of D’s extent), MC (orange, from 20), ATC (purple, U-shaped, drawn from q = 6), names at the curve ends, intercepts 200 and 20 on the price axis. Bottom: “The monopolist faces the market’s downward-sloping demand.”

> **3.b.** Step 1 turns gold. Side solve, one line at a time: 20 + q = 200 − q; 2q = 180; q\* = 90 (red, boxed). A red dot where MR meets MC; its dashed drop draws down to the axis, 90 over q\*. Bottom: “Every unit up to q\* adds more to revenue than to cost.”

> **3.c.** Step 2. The red guide continues up from the dot to demand; a teal dot there and a teal dashed guide to the axis, P\* = 155 in teal. Side solve: P = 200 − ½·90; P\* = 155 (boxed). Bottom: “The price is what buyers will pay for q\* units.”

> **3.d.** Step 3. A purple dot where q\* meets ATC, a purple dashed guide to the axis, ATC\* = 70 in purple. Side solve: ATC\* = 70 (boxed). Bottom: “Average total cost: the cost per unit of making q\* units.”

> **3.e.** Step 4. Side solve: π\* = (155 − 70)·90, then π\* = 7,650 (boxed). Orange one-unit strips fill the profit box from 0 to 90 between 70 and 155, left to right, named “Profit.” Bottom: “Profit: the price minus the cost per unit, on each of the q\* units.”

> **3.f.** Step 5. Bottom, from the sheet: “No entry, because it’s a monopoly.”

> **3.g.efficient.** The card returns to grey. Side solve: 20 + Q = 200 − ½Q; (3/2)Q = 180; Q_sp = 120 in yellow. A yellow dot where MC meets demand, its yellow drop to the axis, 120 over Q_sp. Bottom: “Q_sp: the socially efficient quantity, where marginal cost meets demand.”

> **3.g.** Grey one-unit strips fill the triangle between MC and demand from 90 to 120, named “DWL” just above its top edge. Bottom: “DWL: every unit between q\* and Q_sp, from MC up to demand.”

### 4 | Duopoly

> **4.a.** The monopoly graph leaves; the card stays. Title “Duopoly”; subtitle “Two sellers: Q = q_A + q_B.” The best-response graph, as in E4 (q_A across, q_B up, 0 to 400). Step 1 gold. Side solve from the sheet: MR_A = MC_A; 200 − q_A − ½q_B = 20 + q_A; 180 − ½q_B = 2q_A; then BR_A: q_A = 90 − ¼q_B in pink as the pink BR_A line appears (from 90 on the q_A axis up to 360 on the q_B axis, steep), named at its top. Bottom: “Firm A’s marginal revenue depends on how much firm B sells.”

> **4.b.symmetry.** BR_B: q_B = 90 − ¼q_A in teal with a grey “symmetry” beside it, as on the sheet; the teal BR_B line appears (from 90 on the q_B axis out to 360 on the q_A axis, flat), named at its foot. Bottom: “Firm B’s problem is the same, with A and B swapped.”

> **4.b.** A red dot where the lines cross, labeled “Nash Equilibrium” in red; its dashed guides draw to both axes, 72 over q_A\* under the axis and q_B\* = 72 on the vertical axis. Side solve replaced: q_A\* = 90 − ¼q_A\*; (5/4)q_A\* = 90; q_A\* = q_B\* = 72 (boxed); Q = 144. Bottom: “Neither firm can do better by changing its output alone.”

> **4.c.** The best-response graph leaves; the market graph returns with demand alone. The monopoly outcome stays as a grey reference (dot at 90 and 155, grey guides, 155 on the axis, 90 over q\* under it). Step 2 gold. A red drop up from 144 (over Q) to demand, a teal dot and teal guide to P\* = 128. Side solve: P = 200 − ½(72 + 72); P = 200 − 72; P\* = 128 (boxed). Bottom: “Two sellers: more output, lower price.”

### 5 | Competitive

> **5.a.** The market leaves; the card stays, all grey. Title “Perfect Competition”; subtitle “Many sellers.” The sheet’s two graphs on one price scale: the firm (q to 80; MC orange, ATC purple with its bottom at 30 and 50), headed “Firm,” and the market (Q to 400; D teal, S orange), headed “Market.” Bottom: “Competitive firms are what we call price takers.”

> **5.b.** Step 0 of the sheet. Side solve: 200 − ½Q = 20 + (1/10)Q; 180 = (3/5)Q; Q\* = 300 (boxed), as the red market dot and its drop to 300 over Q\* appear; P\* = 20 + 30 = 50 = MR (boxed), as the red guide runs to P\* = 50 on the market’s axis. Then the price carries across: the firm’s teal MR line draws from the right at 50, named MR. Bottom: “Step 0: supply and demand set the market price.”

> **5.c.** Step 1. A red dot where MC meets MR on the firm graph, its drop to 30 over q\*. Side solve: 20 + q = 50; q\* = 30 (boxed). Bottom: “Every unit up to q\* adds more to revenue than to cost.”

> **5.d.** Step 2. P\* = 50 in teal on the firm’s price axis. Side solve: P\* = 50 (boxed). Bottom: “A price taker sells every unit at the market price.”

> **5.e.** Step 3, “on the graph”: a purple ring at the bottom of ATC, under the red dot. Side solve: ATC\* = 50 (boxed). Bottom: “Average total cost is at its lowest, right at the price.”

> **5.f.** Step 4. Side solve: π\* = (50 − 50)·30, then π\* = 0 (boxed). Bottom, from the sheet: “π = 0. Long run equilibrium.”

> **5.g.** Step 5. Bottom, from the sheet: “No entry or exit.”

### 6 | More Sellers

> **6.a.** The two graphs and the card leave; the divider stays. Title “More Sellers”; subtitle “n similar sellers.” The market graph with demand alone. Right panel: the sheet’s duopoly MR in pink, MR_A = 200 − q_A − ½q_B, rewritten under it as = P − ½q_A; then MR = MC, so P − MC = ½q. One tracker, n, drives the outcome: a red dot on demand with red dashed guides, P = 155 on the price axis, 90 over Q under it, an orange dot at MC below the red dot and a white bracket between them named P − MC, and “n = 1” in the graph’s upper right. A table under the MR lines with headings n, q, Q, P, P − MC (grey) and its first row: 1, 90, 90, 155, 45. Bottom: “Each seller’s MR is the price minus half its own output.”

> **6.b.two → 6.b.three → 6.b.six → 6.b.** n rolls to 2, 3, 6 and 15; at each stop the dot has ridden down demand, the readouts and n have rolled, the bracket has shrunk, and the table adds its row (2, 72, 144, 128, 36; 3, 60, 180, 110, 30; 6, 40, 240, 80, 20; 15, 20, 300, 50, 10). At 6.b, bottom: “More sellers: more output, a lower price, a price closer to marginal cost.”

> **6.c.** Under the table, in pink: “Many sellers: MR ≈ P.” Bottom: “A firm changing its quantity has no real effect on the price.”

### 7 | Summary

> **7.a.** The tracker’s marks, the MR lines and the table leave. Title “Three Market Structures”; subtitle “One market, three outcomes.” The card returns beside the graph with every step in white. On demand, one at a time, three red outcomes with their guides, prices on the axis and quantities under it, each named: Monopoly (90, 155), Duopoly (144, 128), Competitive (300, 50). Bottom: “Market power leads to inefficient markets.”
