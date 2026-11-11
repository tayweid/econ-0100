---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

## Episode E5 | Wrap-Up

<!--
Market switch, 2026-11-11. E5_Animation.py (scene EpisodeE5, 30 holds, rendered without errors) now uses the market E2, E3 and E4 share: demand P = 120 − Q and E1 and E2's firm, TC = 1000 + q^2, MC = 2q, ATC = q + 1000/q. It still follows the steps of the handwritten sheet (E5_Handwritten_Three_Markets.pdf). The October 30 storyboard, with its build log, Not built list and Choices left for Taylor, is _archive/2026-11-11_consolidation/E5_Notes_before_market_switch.md, and the sheet-market animation is beside it as E5_Animation_handwritten_sheet_market.py. There are still no spoken notes for E5; the quote blocks below are animation directions in playback order, as built.

Model. Monopoly: MR = 120 − 2q; q\* = 30; P\* = 90; ATC\* = 63.33; profit 800; Q_sp = 40. Duopoly: BR_A: q_A = 30 − ¼q_B; Nash 24 each, Q = 48, P\* = 72. Competitive, the same demand line read in thousands: supply S: P = 5Q, Q\* = 20 thousand, P\* = 100 = MR; q\* = 50; ATC\* = 70; profit 1,500 (E2's worked example); then entry to the long run, P = 63.25, q = 31.6, Q = 56.75 thousand, profit 0, shown as 63, 32 and 57. n sellers: MR_i = P − q_i; q = 120/(n + 3), P − MC = q. Stops: n = 1: q 30, Q 30, P 90, P − MC 30; n = 2: 24, 48, 72, 24; n = 3: 20, 60, 60, 20; n = 7: 12, 84, 36, 12; n = 17: 6, 102, 18, 6. Every number here was read off the rendered holds on 2026-11-11.

STUCK. These need Taylor.
1. Scale. One seller or two, with these costs, fit a market read in units; many price takers need the same line read in thousands. The competitive market graph is captioned "thousands", and in 7.a the competitive outcome is marked on the units graph by its price only, 63, with no quantity. The subtitle there now reads "One demand curve, three outcomes."
2. The competitive section was rebuilt, not just renumbered. The sheet solves the long run directly (zero profit, no entry or exit). On this market the long run is not whole, so the section solves E2's example at P = 100 with whole numbers (profit 1,500), and step 5 then rolls the price down to the long run. Holds 5.e, 5.f and 5.g changed meaning: ATC\* = 70, profit 1,500, then entry.
3. More Sellers ignores the fixed cost. On this market a third seller would lose money (each sells 20 at 60 with ATC 70), so the sweep to n = 17 shows the marginal-revenue mechanism, not sellers who would stay. Taylor has said the new E5 is an overview of one procedure across the models; whether section 6 stays is open. It is still built. The stops moved from 6 and 15 to 7 and 17 for whole numbers; the hold 6.b.six keeps its name.
4. In section 3 the ATC readout is the number 63.33 alone; "ATC\* = 63.33" ran off the left edge.
5. Still open from October 30: no thesis line on the bumper; every bottom line written for the build; the titles "Perfect Competition" and "More Sellers"; the summary shows outcomes, not deadweight loss.
6. Plass's round-trip check was not run on this file.
-->

### 0 | Bumper

> **0.a.** Shared bumper, Part E | Episode 5. Thesis line left for Taylor.

### 1 | One Market

> **1.a.** Title “Three Market Structures”; subtitle “All firms are similar.” The header, centered: D: P = 120 − Q in teal over MC = 2q in orange. No bottom line.

> **1.b.** Three columns fade in left to right under the header with grey arrows between their names: Monopoly (MR_A = 120 − 2q_A in pink, Q = q_A) → Duopoly (MR_A = 120 − 2q_A − q_B in pink, MR_B = 120 − 2q_B − q_A in teal) → Competitive (MR = P in teal). Bottom: “What happens to price and quantity as sellers are added?”

### 2 | The Firm’s Problem

> **2.a.** Title “The Firm’s Problem”. The sheet’s card, centered, in white: max over q of π = TR − TC, then its five steps one at a time: 1. MC = MR → q\*; 2. q\* → D → P\*; 3. q\* → ATC → ATC\*; 4. π\* = (P\* − ATC\*)·q\*; 5. If π\* ≥ 0 stay/enter; If π\* < 0 exit. Bottom: “Every seller solves the same problem.”

### 3 | Monopoly

> **3.a.** Title “Monopoly”; subtitle “One seller: Q = q_A.” The card shrinks into the right panel under a small azure “The Firm’s Problem” head, its steps grey, behind a grey divider. The market graph fades in, 0 to 120 units by 0 to 140 \$/unit, E3’s axes: D (teal, 120 to 120), MR (pink, ending at 60, half of D’s extent), MC (orange, from the origin), ATC (purple, U-shaped, drawn from q = 9.2), names at the curve ends, 120 on the price axis. Bottom: “The monopolist faces the market’s downward-sloping demand.”

> **3.b.** Step 1 turns gold. Side solve, one line at a time: 2q = 120 − 2q; 4q = 120; q\* = 30 (red, boxed). A red dot where MR meets MC; its dashed drop draws down to the axis, 30 over q\*. Bottom: “Every unit up to q\* adds more to revenue than to cost.”

> **3.c.** Step 2. The red guide continues up from the dot to demand; a teal dot there and a teal dashed guide to the axis, P\* = 90 in teal. Side solve: P = 120 − 30; P\* = 90 (boxed). Bottom: “The price is what buyers will pay for q\* units.”

> **3.d.** Step 3. A purple dot where q\* meets ATC, a purple dashed guide to the axis, 63.33 in purple. Side solve: ATC\* = 30 + 1000/30; ATC\* = 63.33 (boxed). Bottom: “Average total cost: the cost per unit of making q\* units.”

> **3.e.** Step 4. Side solve: π\* = (90 − 63.33)·30, then π\* = 800 (boxed). Orange one-unit strips fill the profit box from 0 to 30 between 63.33 and 90, left to right, named “Profit.” Bottom: “Profit: the price minus the cost per unit, on each of the q\* units.”

> **3.f.** Step 5. Bottom, from the sheet: “No entry, because it’s a monopoly.”

> **3.g.efficient.** The card returns to grey. Side solve: 2Q = 120 − Q; 3Q = 120; Q_sp = 40 in yellow. A yellow dot where MC meets demand, its yellow drop to the axis, 40 over Q_sp. Bottom: “Q_sp: the socially efficient quantity, where marginal cost meets demand.”

> **3.g.** Grey one-unit strips fill the triangle between MC and demand from 30 to 40, named “DWL” just above its top edge. Bottom: “DWL: every unit between q\* and Q_sp, from MC up to demand.”

### 4 | Duopoly

> **4.a.** The monopoly graph leaves; the card stays. Title “Duopoly”; subtitle “Two sellers: Q = q_A + q_B.” The best-response graph, as in E4 (q_A across, q_B up, 0 to 140). Step 1 gold. Side solve: MR_A = MC_A; 120 − 2q_A − q_B = 2q_A; 120 − q_B = 4q_A; then BR_A: q_A = 30 − ¼q_B in pink as the pink BR_A line appears (from 30 on the q_A axis up to 120 on the q_B axis, steep), named at its top. Bottom: “Firm A’s marginal revenue depends on how much firm B sells.”

> **4.b.symmetry.** BR_B: q_B = 30 − ¼q_A in teal with a grey “symmetry” beside it, as on the sheet; the teal BR_B line appears (from 30 on the q_B axis out to 120 on the q_A axis, flat), named at its foot. Bottom: “Firm B’s problem is the same, with A and B swapped.”

> **4.b.** A red dot where the lines cross, labeled “Nash Equilibrium” in red; its dashed guides draw to both axes, 24 over q_A\* under the axis and q_B\* = 24 on the vertical axis. Side solve replaced: q_A\* = 30 − ¼q_A\*; (5/4)q_A\* = 30; q_A\* = q_B\* = 24 (boxed); Q = 48. Bottom: “Neither firm can do better by changing its output alone.”

> **4.c.** The best-response graph leaves; the market graph returns with demand alone. The monopoly outcome stays as a grey reference (dot at 30 and 90, grey guides, 90 on the axis, 30 over q\* under it). Step 2 gold. A red drop up from 48 (over Q) to demand, a teal dot and teal guide to P\* = 72. Side solve: P = 120 − (24 + 24); P = 120 − 48; P\* = 72 (boxed). Bottom: “Two sellers: more output, lower price.”

### 5 | Competitive

> **5.a.** The market leaves; the card stays, all grey. Title “Perfect Competition”; subtitle “Many sellers.” Two graphs on one price scale: the firm (q to 70, in units; MC orange, ATC purple), headed “Firm,” and the market (Q to 120, captioned thousands; D teal, S orange and steep), headed “Market.” Bottom: “Competitive firms are what we call price takers.”

> **5.b.** Step 0. S: P = 5Q appears in orange beside the supply line. Side solve: 120 − Q = 5Q; 120 = 6Q; Q\* = 20 (boxed), as the red market dot and its drop to 20 over Q\* appear; P\* = 5·20 = 100 = MR (boxed), as the red guide runs to P\* = 100 on the market’s axis. Then the price carries across: the firm’s teal MR line draws from the right at 100, named MR. Bottom: “Step 0: supply and demand set the market price.”

> **5.c.** Step 1. A red dot where MC meets MR on the firm graph, its drop to 50 over q\*. Side solve: 2q = 100; q\* = 50 (boxed). Bottom: “Every unit up to q\* adds more to revenue than to cost.”

> **5.d.** Step 2. P\* = 100 in teal on the firm’s price axis. Side solve: P\* = 100 (boxed). Bottom: “A price taker sells every unit at the market price.”

> **5.e.** Step 3. A purple dot where q\* meets ATC, a purple dashed guide to the firm’s axis, 70 in purple. Side solve: ATC\* = 50 + 1000/50; ATC\* = 70 (boxed). Bottom: “Average total cost: the cost per unit of making q\* units.”

> **5.f.** Step 4. Side solve: π\* = (100 − 70)·50, then π\* = 1,500 (boxed). Orange one-unit strips fill the firm’s profit box from 0 to 50 between 70 and 100, named “Profit.” Bottom: “Profit: the price minus the cost per unit, on each of the q\* units.”

> **5.g.** Step 5. The supply equation leaves. Bottom: “With profit, more firms enter and the price falls.” One tracker, the market price, rolls from 100 to 63.25: supply pivots out through the origin, the market dot slides down demand (Q\* 20 → 57, P\* 100 → 63), the firm’s MR line and its dot slide down MC (q\* 50 → 32), the profit strips close to nothing and the purple 70 fades as ATC meets the price at the bottom of the curve. Side solve: Long run: P\* = ATC\*; π\* = 0 (boxed). Bottom, from the sheet: “π = 0. Long run equilibrium: no entry or exit.”

### 6 | More Sellers

> **6.a.** The two graphs and the card leave; the divider stays. Title “More Sellers”; subtitle “n similar sellers.” The market graph with demand alone. Right panel: the duopoly MR in pink, MR_A = 120 − 2q_A − q_B, rewritten under it as = P − q_A; then MR = MC, so P − MC = q. One tracker, n, drives the outcome: a red dot on demand with red dashed guides, P = 90 on the price axis, 30 over Q under it, an orange dot at MC below the red dot and a white bracket between them named P − MC, and “n = 1” in the graph’s upper right. A table under the MR lines with headings n, q, Q, P, P − MC (grey) and its first row: 1, 30, 30, 90, 30. Bottom: “Each seller’s MR is the price minus its own output.”

> **6.b.two → 6.b.three → 6.b.six → 6.b.** n rolls to 2, 3, 7 and 17; at each stop the dot has ridden down demand, the readouts and n have rolled, the bracket has shrunk, and the table adds its row (2, 24, 48, 72, 24; 3, 20, 60, 60, 20; 7, 12, 84, 36, 12; 17, 6, 102, 18, 6). At 6.b, bottom: “More sellers: more output, a lower price, a price closer to marginal cost.”

> **6.c.** Under the table, in pink: “Many sellers: MR ≈ P.” Bottom: “A firm changing its quantity has no real effect on the price.”

### 7 | Summary

> **7.a.** The tracker’s marks, the MR lines and the table leave. Title “Three Market Structures”; subtitle “One demand curve, three outcomes.” The card returns beside the graph with every step in white. On demand, one at a time, three red outcomes: Monopoly (30, 90) and Duopoly (48, 72), each with guides, its price on the axis and its quantity under it; then Competitive, marked at the long-run price 63 with its price on the axis and no quantity, since its market is the line read in thousands. Bottom: “Market power leads to inefficient markets.”
