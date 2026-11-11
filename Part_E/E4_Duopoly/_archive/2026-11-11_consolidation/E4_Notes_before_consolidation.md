---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

## Oligopoly | Episode E4

*When sellers play games with each other*

*The game theory of thin markets*

<!--
Review correction, 2026-10-30 (fresh-eyes review): in 4.b the intercept of firm A's demand is now a teal number on the price axis that rolls with q_B (200 → 164 → 128) and fades near MC's 20 at the end of the 5.b sweep; the market's 200 stays in grey with the ghost demand and shows once D_A moves off it. This supersedes “the 200 intercept turns grey”. 5.b.trace now holds with the tracing point, its guides, q_B = 360 and the 0 over q_A* still up, so the collapsed market graph has its reason on screen; they leave at 5.b with the market graph. 7.a's bottom line is now “What happens with more sellers?” (it read “Next time: …” under the title Next Time). The best-response graph's origin moved from x = 2.6 to 2.45 so its words firm A and BR_B sit inside the 0.6 safe margin; beside a definition it is still at x = −5.6. The card's ATC color is now the ATC_COLOR constant from shared_E.md. Every on-screen number was re-derived independently (53 checks, all pass).
Animation storyboard for E4_Animation.py, scene EpisodeE4. Built 2026-10-30. There was never animation code for E4: the source is Taylor's handwritten sheet 04_Handwritten.pdf ("Example: Three Market Structures", 2 pages; the posted E4 episode works through it) and these notes. The episode animates the sheet's monopoly recap and its duopoly half; E5 animates the whole sheet and extends it to more sellers. Taylor writes the spoken notes; these comments list the beats in playback order, with every on-screen line quoted as built.
Playback order: 0 bumper; 1 Oligopoly (paragraphs 1 to 5); 2 The Firm's Problem and 3 Monopoly (sheet, during paragraph 6); 4 Duopoly (paragraphs 7 and 8); 5 Best Responses (paragraphs 9 and 10, then the sheet); 6 Nash Equilibrium (sheet); 7 Next Time. Sections 2, 3, 5, 6 and 7 are built from the sheet; their beats are in the comments after the notes.
References: D1_Animation.py (the Best Response and Nash Equilibrium definitions verbatim, its divider at x = 0.3 with the definition beside the model, the Table look reused for the taxonomy), D3_Animation.py (taxonomy hold, then the red box moves; bumper), C2_Animations.py (side solve right of a grey divider at x = 2.45, rows of colored math, numbers carried from the algebra to the axis, two-row quantity readouts), C3_Animations.py and B5_Animation.py (one ValueTracker drives a moving curve, its dot, guides and rolling numbers).
Model (the sheet): market demand P = 200 − ½Q; every firm MC = 20 + q ("all firms are similar"). Monopoly: MR_A = 200 − q_A, Q = q_A; 20 + q_A = 200 − q_A, 2q_A = 180, q_A = 90 = q* (MC there 110); P* = 200 − ½·90 = 155. Duopoly: Q = q_A + q_B, P = 200 − ½(q_A + q_B), MR_A = 200 − q_A − ½q_B. Firm A's demand and MR_A both start at 200 − ½q_B on the price axis (D_A reaches zero at q_A = 400 − q_B, MR_A at 200 − ½q_B): q_B = 0 gives q_A* = 90; q_B = 72 gives intercept 164 and q_A* = 72 (MC 92); q_B = 144 gives 128 and q_A* = 54 (MC 74); q_B = 360 gives 20 and q_A* = 0. Best response: 200 − q_A − ½q_B = 20 + q_A, 180 − ½q_B = 2q_A, BR_A: q_A = 90 − ¼q_B, from (90, 0) to (0, 360) with q_A across and q_B up; BR_B: q_B = 90 − ¼q_A by symmetry, from (0, 90) to (360, 0). Nash: q_A* = 90 − ¼q_A*, (5/4)q_A* = 90, q_A* = 90·(4/5) = 72 = q_B*, Q = 144, P = 200 − ½(72 + 72) = 200 − 72 = 128. Every number on screen was checked against these formulas (57 checks, all pass).
Graphs: the market graph 0–400 units by 0–220 $/unit, 5.6 by 4.6 units, origin (−5.4, −2.225); D teal from (0, 200) to (400, 0), MC orange from (0, 20) to (200, 220), MR_A pink from (0, 200) to (200, 0), half of demand's quantity. The best-response graph 0–400 by 0–400 (q_A across, q_B up), 4.6 by 4.6, origin (2.45, −2.225) beside the market graph, or (−5.6, −2.225) beside a definition. The algebra panel is centered at x = 5.2 right of a grey divider at x = 2.45 (C2); the definition panel starts at x = 0.85 right of a divider at x = 0.3 (D1).
Conventions (E_conventions.md, shared_E.md): plain Scene at 15 fps; the topic title in azure with every word capitalized; a grey CMU Sans subtitle only for context; one gold line in the bottom strip (scale 0.7443, centered, 0.05 from the bottom) or none; price readouts on the vertical axis, quantities as two rows under the horizontal (number, then symbol); red guides, dots and readouts; firm A pink and firm B teal as in Part D's games, demand teal, MC orange, MR pink; one tracker (q_B) drives every moving piece in sections 4 and 5; text replaced by removing the old line before the new one fades in. File header in shared_E.md's order: the maniml line and comments, then the PEP 723 block (D2/D3 form), imports of style.py only.
Not built: 1.b, the two earlier models as small icons (optional in the outline; the boxed taxonomy carries the comparison). Profits for the duopolists and the card's steps 3 to 5 in this episode: they need ATC and a fixed cost, and the sheet stops the duopoly at P* = 128. The sheet's MR_B = 200 − q_B − ½q_A row: firm B comes in by symmetry at 5.c, as on the sheet's page 2. The notes' second italic line, The game theory of thin markets, is not on screen. A quantity-choice payoff matrix tying the duopoly back to Part D (60 or 72 units each makes a prisoner's dilemma once a fixed cost of 450 is assumed: 4,950 each at 60, 4,734 each at 72, 5,166 against 4,590 when one deviates): an idea, not on the sheet.
Choices left for Taylor: (1) Lines written for this build, his to replace: the subtitle “One seller, many buyers.” (from E1's notes), “The more the other firm sells, the less you want to sell.” (4.b), the subtitle “The strategies are quantities.” (5.a), “Two sellers: more output, lower price.” (6.c), “What happens with more sellers?” (7.a). Trimmed from his paragraphs: 1.a, 3.a, 4.b.zero, 4.b.seventy_two (his second person kept: “Your marginal revenue…”), 5.a.rule; 4.a is his sentence verbatim; 3.c and 3.d show the card's steps 1 and 2 as the bottom line. (2) Notation from the sheet, q*, P*, q_A*, q_B*, P* = 128, where Part C would put hats on an inefficient market outcome. (3) The taxonomy's shape: three seller rows by two goods columns, Monopoly across both columns, the few-sellers differentiated cell blank because E1's notes give oligopoly homogeneous goods; built here before E1's version exists, so the two should be made one object. (4) The card colors its curve names (MC orange, MR pink, D teal, ATC purple) and sets them upright; E5_Animation.py, built in parallel, draws the same card all white in math italic with the sheet's punctuation (stay/enter; exit.). One of the two should win. (5) Firm A's MR is labeled MR_A from 3.b (the sheet's monopoly writes MR_A); MC stays MC, since every firm has the same one. (6) The sweep ends at q_B = 360, where q_A* = 0 and firm A's demand and MR shrink into the price axis at 20 (the hold keeps q_B = 360 on screen to say why); it could stop at 144 or roll back to 72 instead. (7) The red label beside the Nash dot and the gold definition both read Nash Equilibrium, as the sheet labels the dot. (8) The thesis keeps the notes' wording without a period.
-->

<!--
0 · Bumper and 1 · Oligopoly. Beats, as built.
0.a · The shared bumper: raster MICROECONOMICS, flicker, Part E | Episode 4 beneath it, and the italic thesis in grey under it: “When sellers play games with each other” (the notes' first italic line, without a period, as written). Pause, then clear.
1.a.last · Title: Monopoly. Subtitle: “One seller, many buyers.” The market-structures taxonomy centered in the body in D1's Table look (grey rules, red row and column words, white cells): columns Homogeneous and Differentiated; rows Many Sellers (Perfect Competition, Monopolistic Competition), Few Sellers (Oligopoly, the differentiated cell blank), One Seller (Monopoly, across both columns). A red box around Monopoly, last episode's cell. No bottom text.
1.a · The box moves to Oligopoly (0.8 s); title Oligopoly, no subtitle; then the bottom line: “Oligopoly: a few sellers with some but not complete control of the price.”
Cues. 1.a.last → “While markets can be great…” and “But neither the competitive seller nor the monopolist…”. 1.a → “One type of situation like this…” through “This type of strategic interaction we call oligopoly…”.
Not built: 1.b (see the top comment).
-->

While markets can be great at organizing production and exchange, we’ve just shown that markets can start to break down when sellers have some influence on prices. We showed that competitive firms cannot benefit by moving their prices from market equilibrium prices, but that firms that do not have competitors actually can.

But neither the competitive seller nor the monopolist are all that common in our world. Most exchanges we make are with sellers who have some but not much influence on their prices.

One type of situation like this, where the seller has some but not complete market power, is what we call oligopoly. A seller cannot charge a price too high because buyers will simply switch to the seller down the road. They also don’t want to sell too low, because even though they would bring in buyers from their competitor down the road, they also don’t want to miss out on selling at nice high prices.

But each seller in this environment is thinking this way. And each seller knows the other sellers are thinking this way. If the seller down the road sets a high price, then I should set a high price. And if they set a low price, I better not set a high price, or they will undercut me.

This type of strategic interaction we call oligopoly, where there are a few sellers with some but not complete control of the price responding to the prices of other sellers nearby.

<!-- 2.a and 3.a to 3.d play during this paragraph: the Firm’s Problem card and the monopoly recap from the sheet. Their beats are in the comments after the notes. -->

To get a handle on … lets set up the profits for the oligopolist. Like in every environment for the seller, we want to try to get a sense of the firm’s marginal costs and their marginal revenue. Their MC is similar to what we’ve done before. Since costs come from the production function and not the structure of the market, there’s nothing fundamentally different with the MC because we’re in a different environment.

<!--
4 · Duopoly. Beats, as built. Source: these two paragraphs, with the sheet's duopoly model (p. 1 header and p. 2).
4.a · Title: Duopoly. Subtitle stays: “All firms are similar.” The monopoly graph keeps D, MR_A, MC, the red MR = MC dot, its drop and 90 over q*; the price guides, the dot on D and P* = 155 fade. In the panel the monopoly rows give way to “Q = q_A + q_B” and “P = 200 − ½(q_A + q_B)” (teal) under the two model rows. Bottom: “Both of you are trying to sell into the same market.”
4.b.zero · The graph becomes firm A's: the axis word Q becomes q_A, D becomes D_A (the demand firm A faces), q* becomes q_A*, the teal 200 on the price axis becomes D_A's intercept (a number that rolls with q_B), and a thin grey copy of the market demand stays behind (its grey label D and grey 200 appear once D_A moves off it). MR_A and MC keep their labels. Panel adds “MR_A = 200 − q_A − ½q_B” (pink) and a live row “q_B = 0” (red). Bottom: “The price depends on how much the other firm sells.”
4.b.seventy_two · The q_B tracker rolls 0 → 72 (2.4 s): D_A and MR_A slide down together and their teal intercept rolls 200 → 164, the dot slides down MC, q_A* rolls 90 → 72 and q_B rolls in the panel. Bottom: “Your marginal revenue also depends on how much the other firm sells.”
4.b · q_B rolls 72 → 144: the intercept rolls to 128, q_A* 72 → 54. Bottom: “The more the other firm sells, the less you want to sell.”
Cues. 4.a → “Since revenue is the product of price and quantity…”. 4.b.zero → “But because the price depends on how much the other firm sells…”; 4.b.seventy_two and 4.b → the rest of that paragraph.
-->

Since revenue is the product of price and quantity, however, it is very different in this environment. As always, prices are set by the demand curve and everyone can see the price. So as a seller, like both the monopolist and the competitive firm, you as the oligopolist will choose to set prices so that nothing you make goes unsold. But unlike the monopolist, you’re not the only seller. So the quantity that’s sold to buyers isn’t just what you make, but also includes what the other seller makes. Both of you are trying to sell into the same market. So if the other seller lowers their price, everyone will go to them until you lower your price as well. So just like in competitive markets, you don’t have any reason to switch prices from the price that sells everything for everyone.

But because the *price* depends on how much the other firm sells, your *revenue* depends on how much the other firm sells, which means your *marginal revenue* *also* depends on how much the other firm sells.

<!-- 5.a.rule to 5.a play during these two paragraphs; section 5 is built from the sheet, and its beats are in the comments after the notes. -->

When our payoff is liked with the decisions of others like this, we call this strategic interaction, which is the domain of game theory.

What we want to do is find a way to decide our best response to every decision the other seller might make.

<!--
2 · The Firm's Problem. Source: the handwritten sheet, p. 2 top left (FIRM'S PROBLEM), verbatim. Beats, as built.
2.a · Title: The Firm’s Problem. No subtitle. The card centered in the body, rows left-aligned, one row per fade: “max over q: π = TR − TC”, then “1. MC = MR → q*” (MC orange, MR pink), “2. q* → D → P*” (D teal), “3. q* → ATC → ATC*” (the first ATC purple), “4. π* = (P* − ATC*)·q*”, “5. If π* ≥ 0 stay/enter” with “If π* < 0 exit” under its If. Pause on the full card. No bottom text. Curve names upright, as on the graphs.
Cues. 2.a → “To get a handle on … lets set up the profits for the oligopolist.”
-->

<!--
3 · Monopoly. Source: the handwritten sheet, p. 1 (header, MONOPOLY steps 1 and 2). Beats, as built.
3.a · Title: Monopoly. Subtitle: “All firms are similar.” (the sheet's header). The market graph: P and $/unit at the top of the price axis, Q and units at the end of the quantity axis, D (teal) with its 200 intercept, MC (orange) with its 20 intercept, labels D at demand's foot and MC at its top end. The grey divider at x = 2.45 and the two model rows: “D: P = 200 − ½Q” (teal), “MC = 20 + q” (orange). Bottom: “Costs come from the production function, not the structure of the market.”
3.b · MR_A (pink) from 200 down to 200 units, labeled MR_A at its foot. Panel: “MR_A = 200 − q_A” (pink) and “Q = q_A”. Bottom text cleared.
3.c · The red dot where MR_A meets MC; the rows “20 + q_A = 200 − q_A” (MC side orange, MR side pink), “2q_A = 180”, “q_A = 90 = q*” (90 and q* red), one per play; then the dashed drop from the dot to the axis and the red 90 carried from the algebra down to the axis with q* under it. Bottom: “1. MC = MR → q*”.
3.d · The drop rises on to D at (90, 155) with a second dot; the row “P* = 200 − ½·90 = 155” (P* and 155 red, the demand part teal); the dashed guide across to the price axis and the 155 carried to it as “P* = 155”. Bottom: “2. q* → D → P*”.
Cues. 3.a → “Their MC is similar to what we’ve done before. Since costs come from the production function…”. 3.b to 3.d are the sheet's monopoly half, spoken as a recap of E3.
-->

<!--
5 · Best Responses. Source: the handwritten sheet, p. 2 (DUOPOLY step 1 and the BR picture), with the notes' last two paragraphs. Beats, as built.
5.a.rule · The q_B tracker rolls back 144 → 0 (firm A's graph returns to the monopoly picture, its intercept back to 200), then the duopoly rows and the live q_B row leave. Title: Best Responses. Subtitle: “The strategies are quantities.” Panel, under the model rows: “MR_A = MC_A” (pink, orange). Bottom: “Decide our best response to every decision the other seller might make.”
5.a.substitute · “200 − q_A − ½q_B = 20 + q_A” (pink side, orange side).
5.a.simplify · “180 − ½q_B = 2q_A”.
5.a · “BR_A: q_A = 90 − ¼q_B” (pink).
5.b.trace · The model rows, the first three algebra rows, the divider and the bottom line leave; the BR_A row shrinks into the open upper right of the new best-response graph (q_A across with “firm A” in pink under it, q_B up with “firm B” in teal beside it). A pink point at (90, 0) with red guides to both axes, “q_B = 0” on the vertical axis and 90 over q_A* under the horizontal. One sweep (4 s, smooth): q_B 0 → 360 on the same tracker; on the market graph D_A and MR_A slide down to 20 (their teal intercept fades as it nears MC's 20, as do the names D_A and MR_A) and the dot runs down MC to (0, 20) with 0 over q_A*, while on the best-response graph the point climbs to (0, 360) and leaves the pink BR_A line behind it. Then the label BR_A arrives beside the point at the line's top; the point, its guides, “q_B = 360” and the 0 over q_A* stay through the hold. No bottom text.
5.b · The market graph and the tracing marks fade; the best-response graph slides left to (−5.6, −2.225) while a grey divider grows at x = 0.3; D1's definition fades in beside it, gold term and white lines: “Best Response” / “The strategy that gives a player” / “the highest payoff, given the strategies” / “chosen by the other players in the game.”
5.c · Symmetry, as on the sheet: a grey dashed 45° line from the origin with the grey word symmetry at its top; a copy of BR_A turns into BR_B (teal) from (0, 90) to (360, 0), labeled BR_B at its foot, and “BR_B: q_B = 90 − ¼q_A” (teal) joins under the BR_A equation. The definition stays; no bottom text.
Cues. 5.a.rule → “When our payoff is liked with the decisions of others…” and “What we want to do is find a way to decide our best response…”. 5.b.trace to 5.c are the sheet's BR_A, BR_B and the BR picture.
-->

<!--
6 · Nash Equilibrium. Source: the handwritten sheet, p. 2 (the BR picture's crossing, “NASH EQUILIBRIUM”, the boxed q_A* = q_B* = 72, Q = 144, and step 2's P* = 128). Beats, as built.
6.a · Title: Nash Equilibrium. Subtitle stays: “The strategies are quantities.” The Best Response definition and the symmetry line leave; D1's definition fades in: “Nash Equilibrium” / “A set of strategies such that no player” / “can improve their payoff by unilaterally” / “changing strategy.” On the graph: a red dot where BR_A meets BR_B, red dashed guides to both axes, “?” over q_A* under the horizontal, “q_B* = ?” on the vertical, and “Nash Equilibrium” in red beside the dot. No bottom text.
6.b.substitute · The definition leaves; the panel: “symmetric → q_A* = q_B*” (symmetric grey), “q_A* = 90 − ¼q_A*”. No bottom text.
6.b.solve · “(5/4) q_A* = 90”, “q_A* = 90·(4/5) = 72 = q_B*” (72 red).
6.b · The red 72 is carried to both axes in place of the question marks; “Q = q_A* + q_B* = 144” (144 red).
6.c.price · Title: Duopoly. Subtitle: “All firms are similar.” The panel and divider leave, the best-response graph slides back right, and the market graph returns with the market's axis word Q, D (teal, 200 intercept teal again) and the monopoly outcome as a grey reference: grey dot at (90, 155), grey dashed guides, 155 and 90 in grey, the word Monopoly up and right of the dot, above demand. Then 144 over Q in red under the axis, the red guide up to D at (144, 128) and its dot, and the bottom formula: “P = 200 − ½(72 + 72) = 200 − 72 = 128”; then the guide across and “P* = 128” on the price axis.
6.c · Bottom: “Two sellers: more output, lower price.”
-->

<!--
7 · Next Time. Source: the outline's restrained cue toward E5 (not on the sheet or in these notes). Beats, as built.
7.a · Title: Next Time; no subtitle. The final picture stays (market graph left, best-response graph right) and a grey arrow points on down the demand curve from the duopoly dot. Bottom: “What happens with more sellers?”
-->
