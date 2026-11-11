---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

## Oligopoly | Episode E4

*When sellers play games with each other*

*The game theory of thin markets*

| Minutes | Animation or board work | Purpose |
| --- | --- | --- |
| Warmup | Exercise E4 Warmup on the board | Retrieve the monopolist’s problem on today’s market. |
| 0–5 | Bumper (`0.a`), then `1.a.last` and `1.a` | From one seller to a few. |
| 5–10 | Play `2.a` through `3.d` | The firm’s problem; the monopoly answer to the warmup. |
| 10–16 | Resume through `4.b` | A second seller: price and marginal revenue depend on the other firm. |
| 16–20 | Hide projection; Q1 on board | Choose firm A’s quantity for a given quantity from firm B. |
| 20–29 | Resume through `5.c` | The best-response rule, its graph, and firm B’s by symmetry. |
| 29–33 | Hide projection; Q2 on board | Use a best response; test whether a pair is an equilibrium. |
| 33–42 | Resume through `6.c` | Nash equilibrium, then the price beside the monopoly’s. |
| 42–47 | Hide projection; Q3 on board | Is the duopoly outcome efficient? |
| 47–50 | Resume to `7.a` | Preview more sellers. |

{++ This table is a proposal. It has not been timed against a run-through. ++}

<!--
E4 consolidation, 2026-11-11. This file now follows E2_Notes.md and E3_Notes.md: a timing table, then Taylor's paragraphs in their original order, each followed by a two-column table of the holds it cues, as built in E4_Animation.py (scene EpisodeE4, 26 holds; rendered without errors on 2026-11-11 after the change of market described below). Every paragraph of Taylor's is still here, word for word, with no strikes. Everything Claude added is inside addition marks, except the section headings (the animation's own titles) and the timing table. The animation keeps its 26 holds and their order; its market changed.

Where the earlier material went. The October 30 build log, its review correction, its "Choices left for Taylor", its "Not built" list and the old per-section beat lists are in _archive/2026-11-11_consolidation/E4_Notes_before_consolidation.md. The same folder holds 01_Notes.md (the same prose without comments) and the two empty stubs, 02_Storyboard.md and 03_Code.py. The old _Unplaced.md held two fragments of the Spring 2023 Wandmaker's Dilemma that exist nowhere else in the live course, among them a bonus question with a tax of 60 galleons; it is now E_Practice_Bank/Unplaced_E4_wandmakers-dilemma_S23.md, beside the other Wandmaker's Dilemma versions. 04_Handwritten.pdf, the source of this episode, stays where it was.

Model of record, changed 2026-11-11 to E2 and E3's market: demand P = 120 − Q; every firm MC = 2q (the fixed cost of 1,000 and ATC = q + 1000/q are not used on screen). The steps are still the handwritten sheet's; its own market (P = 200 − ½Q, MC = 20 + q: monopoly 90 at 155, then 72 each at 128) is in the archive as E4_Animation_handwritten_sheet_market.py. Monopoly: MR_A = 120 − 2q_A; 2q_A = 120 − 2q_A, q\* = 30; P\* = 120 − 30 = 90, E3's answer. Duopoly: Q = q_A + q_B, P = 120 − (q_A + q_B), MR_A = 120 − 2q_A − q_B. Firm A's demand and MR_A both start at 120 − q_B on the price axis: q_B = 0 gives q_A\* = 30; q_B = 24 gives 96 and q_A\* = 24; q_B = 48 gives 72 and q_A\* = 18; q_B = 120 gives 0 and q_A\* = 0. Best response: 120 − 2q_A − q_B = 2q_A, 120 − q_B = 4q_A, BR_A: q_A = 30 − ¼q_B; BR_B: q_B = 30 − ¼q_A by symmetry. Nash: q_A\* = 30 − ¼q_A\*, q_A\* = 24 = q_B\*, Q = 48, P = 120 − 48 = 72. These were read off the rendered holds on 2026-11-11 and match. Graphs: the market graph, 0 to 120 units by 0 to 140 \$/unit, the same axes as E3; the best-response graph, 0 to 140 by 0 to 140 with q_A across and q_B up.

STUCK. These need Taylor; nothing here was decided for him.
1. The prose stops halfway. The last paragraph is "What we want to do is find a way to decide our best response". The 10 holds from 5.b.trace to 7.a (the best-response graph, firm B by symmetry, the Nash equilibrium, the price comparison, Next Time) have no paragraphs of Taylor's; they were built from the sheet. One marked sentence stands in for each stretch.
2. Prices against quantities. The third and fourth paragraphs describe sellers setting high or low prices and undercutting each other. The animation's firms choose quantities (its subtitle says "The strategies are quantities."), as on the sheet.
3. One market for E2 to E4, decided 2026-11-11: this episode now uses E3's demand and E2's costs, so its monopoly recap is E3's answer, 30 units at 90. Two things follow. It no longer matches the numbers on the handwritten sheet, 04_Handwritten.pdf, which is still the source of its steps. E5 Wrap-Up moved to this market the same day. The hold 4.b.seventy_two keeps its name, though firm B's quantity there is now 24.
4. Naming. The title here is Oligopoly, the folder and the animation's main sections say Duopoly. There are two thesis lines; the bumper shows the first and the second is not on screen.
5. "To get a handle on … lets set up" has a gap where the ellipsis is, and "liked" in "payoff is liked" reads as "linked". Both are left as written.
6. No opener story, no warmup hold and no exercise cards exist in the animation. The warmup and Q1 to Q3 below exist only in these notes. New Homework and Vignette folders appeared in E4_Duopoly during this session; Claude did not write them. They use their own demand curves (P = 200 − Q and P = 100 − Q), and these exercises were not matched to them.
7. Time. The timing table is a proposal.
8. E2's conventions have not been applied: this episode keeps one gold line at the bottom, the side panel of algebra, and the taxonomy opening.
9. Still open from the October 30 build: the lines written for the build (the subtitles "One seller, many buyers." and "The strategies are quantities.", "The more the other firm sells, the less you want to sell.", "Two sellers: more output, lower price.", "What happens with more sellers?"); q\* and P\* against Part C's hats; the firm's card here colors its curve names while E5's is all white; the sweep ends at q_B = 120; duopoly profits are not shown, though this market's fixed cost now allows it (about 152 each, against the monopolist's 800); a quantity-choice payoff matrix tying back to Part D is an idea only.
10. Plass's round-trip check was not run on this file. The syntax copies E2_Notes.md.

ADDITIONS, all Claude's and all marked: the warmup; Whiteboard Q1, Q2 and Q3; one stand-in sentence each under Best Responses, Nash Equilibrium and Next Time. Each is a suggestion to cut or rewrite.
-->

## {++ Exercise E4 | Warmup ++}

{++ One seller faces demand $P = 120 - Q$, so $MR = 120 - 2Q$. Marginal cost is $MC = 2q$. ++}

{++ a\) What quantity does the monopolist choose? ++}

{++ b\) What price does it charge? ++}

<!--
Not built: the animation has no warmup hold. This is E3’s problem, and holds 3.c and 3.d work it again, so the animation answers the warmup.

Answers: a) 2q = 120 − 2q, so q = 30; b) P = 120 − 30 = 90.
-->

## Oligopoly

While markets can be great at organizing production and exchange, we’ve just shown that markets can start to break down when sellers have some influence on prices. We showed that competitive firms cannot benefit by moving their prices from market equilibrium prices, but that firms that do not have competitors actually can.

But neither the competitive seller nor the monopolist are all that common in our world. Most exchanges we make are with sellers who have some but not much influence on their prices.

<!--
|   |   |
| --- | --- |
| 0.a | Play the E4 bumper: Part E ∣ Episode 4, with the italic thesis in grey beneath it: “When sellers play games with each other”, the first italic line above, without a period. |
| 1.a.last | Title: Monopoly. Subtitle: “One seller, many buyers.” Center the market-structures taxonomy: columns Homogeneous and Differentiated; rows Many Sellers (Perfect Competition, Monopolistic Competition), Few Sellers (Oligopoly, the differentiated cell blank), One Seller (Monopoly, across both columns). A red box sits on Monopoly, last episode’s cell. No bottom line. |
-->

One type of situation like this, where the seller has some but not complete market power, is what we call oligopoly. A seller cannot charge a price too high because buyers will simply switch to the seller down the road. They also don’t want to sell too low, because even though they would bring in buyers from their competitor down the road, they also don’t want to miss out on selling at nice high prices.

But each seller in this environment is thinking this way. And each seller knows the other sellers are thinking this way. If the seller down the road sets a high price, then I should set a high price. And if they set a low price, I better not set a high price, or they will undercut me.

This type of strategic interaction we call oligopoly, where there are a few sellers with some but not complete control of the price responding to the prices of other sellers nearby.

<!--
|   |   |
| --- | --- |
| 1.a | Move the red box to Oligopoly and change the title to Oligopoly, with no subtitle. Gold line: “Oligopoly: a few sellers with some but not complete control of the price.” |
-->

## The Firm’s Problem and Monopoly

To get a handle on … lets set up the profits for the oligopolist. Like in every environment for the seller, we want to try to get a sense of the firm’s marginal costs and their marginal revenue. Their MC is similar to what we’ve done before. Since costs come from the production function and not the structure of the market, there’s nothing fundamentally different with the MC because we’re in a different environment.

<!--
These five holds play during this one paragraph. 2.a is cued by its first sentence and 3.a by “Their MC is similar to what we’ve done before.” 3.b to 3.d are the sheet’s monopoly half, spoken as a recap of E3; the paragraph has no words for them.

|   |   |
| --- | --- |
| 2.a | Title: The Firm’s Problem, with no subtitle. Center the card from the sheet, one row per fade: max over q of π = TR − TC; 1. MC = MR → q\*; 2. q\* → D → P\*; 3. q\* → ATC → ATC\*; 4. π\* = (P\* − ATC\*) · q\*; 5. If π\* ≥ 0 stay/enter, with If π\* < 0 exit beneath it. MC is orange, MR pink, D teal and ATC purple. Pause on the full card. No bottom line. |
| 3.a | Title: Monopoly. Subtitle: “All firms are similar.”, the sheet’s header. Draw the market graph, 0 to 120 units by 0 to 140 \$/unit, E3’s axes: demand in teal with its 120 on the price axis, named D at its foot, and MC in orange from the origin, named at its top end. Add the grey divider and the rows D: P = 120 − Q and MC = 2q. Gold line: “Costs come from the production function, not the structure of the market.” |
| 3.b | Draw MR_A in pink from 120 on the price axis down to 60 units, half of demand’s quantity, named MR_A at its foot. Add the rows MR_A = 120 − 2q_A and Q = q_A. Clear the gold line. |
| 3.c | Put a red dot where MR_A meets MC. Show the rows 2q_A = 120 − 2q_A, then 4q_A = 120, then q_A = 30 = q\*, one per play. Draw the dashed drop from the dot to the axis and carry the red 30 from the algebra down to the axis, with q\* under it. Gold line: “1. MC = MR → q\*”. |
| 3.d | Raise the drop to demand at (30, 90) with a second dot. Show the row P\* = 120 − 30 = 90, draw the dashed guide across to the price axis, and carry the 90 to it as P\* = 90. Gold line: “2. q\* → D → P\*”. |
-->

## Duopoly

Since revenue is the product of price and quantity, however, it is very different in this environment. As always, prices are set by the demand curve and everyone can see the price. So as a seller, like both the monopolist and the competitive firm, you as the oligopolist will choose to set prices so that nothing you make goes unsold. But unlike the monopolist, you’re not the only seller. So the quantity that’s sold to buyers isn’t just what you make, but also includes what the other seller makes. Both of you are trying to sell into the same market. So if the other seller lowers their price, everyone will go to them until you lower your price as well. So just like in competitive markets, you don’t have any reason to switch prices from the price that sells everything for everyone.

<!--
|   |   |
| --- | --- |
| 4.a | Title: Duopoly. The subtitle “All firms are similar.” stays. The monopoly graph keeps D, MR_A, MC, the red MR = MC dot, its drop and 30 over q\*; the price guide, the dot on D and P\* = 90 fade. In the panel the monopoly rows give way to Q = q_A + q_B and P = 120 − (q_A + q_B) under the two model rows. Gold line: “Both of you are trying to sell into the same market.” |
-->

But because the *price* depends on how much the other firm sells, your *revenue* depends on how much the other firm sells, which means your *marginal revenue* *also* depends on how much the other firm sells.

<!--
|   |   |
| --- | --- |
| 4.b.zero | The graph becomes firm A’s: the axis word Q becomes q_A, D becomes D_A, the demand firm A faces, and q\* becomes q_A\*. The teal 120 on the price axis becomes D_A’s intercept, a number that rolls with q_B, and a thin grey copy of the market demand stays behind. Add the row MR_A = 120 − 2q_A − q_B and a live red row q_B = 0. Gold line: “The price depends on how much the other firm sells.” |
| 4.b.seventy_two | Roll q_B from 0 to 24. D_A and MR_A slide down together and their teal intercept rolls 120 → 96; the grey market demand, its D and its 120 show behind them. The red dot slides down MC and q_A\* rolls 30 → 24. Gold line: “Your marginal revenue also depends on how much the other firm sells.” |
| 4.b | Roll q_B from 24 to 48: the intercept rolls to 72 and q_A\* rolls 24 → 18. Gold line: “The more the other firm sells, the less you want to sell.” |
-->

### {++ Whiteboard | Exercise Q1 ++}

{++ > Firm B sells 40 units, so firm A’s marginal revenue is $MR_A = 80 - 2q_A$. What quantity does firm A choose? ++}

<!--
Not built: no exercise card in the animation.

Answer: 80 − 2q_A = 2q_A, so q_A = 20. The best-response rule gives the same: 30 − ¼ · 40 = 20.
-->

## Best Responses

When our payoff is liked with the decisions of others like this, we call this strategic interaction, which is the domain of game theory.

What we want to do is find a way to decide our best response to every decision the other seller might make.

<!--
|   |   |
| --- | --- |
| 5.a.rule | Roll q_B back from 48 to 0, so firm A’s graph returns to the monopoly picture with its intercept at 120; the duopoly rows and the live q_B row leave. Title: Best Responses. Subtitle: “The strategies are quantities.” Under the model rows: MR_A = MC_A. Gold line: “Decide our best response to every decision the other seller might make.” |
| 5.a.substitute | Row: 120 − 2q_A − q_B = 2q_A, the MR side pink and the MC side orange. |
| 5.a.simplify | Row: 120 − q_B = 4q_A. |
| 5.a | Row: BR_A: q_A = 30 − ¼q_B, in pink. |
-->

{++ The rule gives firm A’s best quantity for every quantity firm B might choose, so we can draw it. Firm B has the same costs and faces the same market, so its rule is the mirror image. ++}

<!--
No paragraph of Taylor’s cues these three holds; they are the sheet’s BR_A, BR_B and best-response picture.

|   |   |
| --- | --- |
| 5.b.trace | The model rows, the first three algebra rows, the divider and the gold line leave, and the BR_A row shrinks into the upper right of a new best-response graph: q_A across, with “firm A” in pink under it, and q_B up, with “firm B” in teal beside it. Start a pink point at (30, 0) with red guides to both axes, q_B = 0 on the vertical axis and 30 over q_A\* under the horizontal. One four-second sweep takes q_B from 0 to 120. On the market graph D_A and MR_A slide down to nothing and the red dot runs down MC to the origin. On the best-response graph the point climbs to (0, 120) and leaves the pink BR_A line behind it. Then label the line BR_A at its top. The point, its guides, q_B = 120 and the 0 over q_A\* stay through the hold. No bottom line. |
| 5.b | Fade the market graph and the tracing marks. The best-response graph slides left while a grey divider grows beside it, and the definition from D1 fades in, its term in gold: “Best Response: The strategy that gives a player the highest payoff, given the strategies chosen by the other players in the game.” |
| 5.c | Symmetry, as on the sheet: draw a grey dashed 45° line from the origin with the grey word symmetry at its top. A copy of BR_A turns into BR_B in teal, from (0, 30) to (120, 0), named BR_B at its foot, and BR_B: q_B = 30 − ¼q_A joins under the BR_A equation. The definition stays. No bottom line. |
-->

### {++ Whiteboard | Exercise Q2 ++}

{++ > Suppose firm B sells 40 units. What is firm A’s best response? If firm A sells that quantity, what is firm B’s best response? Is this pair a Nash equilibrium? ++}

<!--
Not built: no exercise card in the animation.

Answer: firm A’s best response to 40 is 30 − ¼ · 40 = 20. Firm B’s best response to 20 is 30 − ¼ · 20 = 25, not 40, so firm B would change its quantity: (20, 40) is not a Nash equilibrium.
-->

## Nash Equilibrium

{++ Where the two best responses cross, each firm is choosing its best quantity given what the other is choosing, so neither wants to change. ++}

<!--
No paragraph of Taylor’s cues these six holds; they follow the sheet’s crossing, boxed answers and price, here q_A\* = q_B\* = 24, Q = 48 and P\* = 72.

|   |   |
| --- | --- |
| 6.a | Title: Nash Equilibrium. The subtitle “The strategies are quantities.” stays. The Best Response definition and the symmetry line leave, and the definition from D1 fades in: “Nash Equilibrium: A set of strategies such that no player can improve their payoff by unilaterally changing strategy.” On the graph, put a red dot where BR_A meets BR_B with red dashed guides to both axes, a question mark over q_A\* under the horizontal, q_B\* = ? on the vertical, and Nash Equilibrium in red beside the dot. No bottom line. |
| 6.b.substitute | The definition leaves. Panel rows: symmetric → q_A\* = q_B\*, then q_A\* = 30 − ¼q_A\*. |
| 6.b.solve | Rows: (5/4) q_A\* = 30, then q_A\* = 30 · (4/5) = 24 = q_B\*, the 24 in red. |
| 6.b | Carry the red 24 to both axes in place of the question marks. Row: Q = q_A\* + q_B\* = 48, the 48 in red. |
| 6.c.price | Title: Duopoly. Subtitle: “All firms are similar.” The panel and divider leave, the best-response graph slides back to the right, and the market graph returns with the monopoly outcome as a grey reference: a grey dot at (30, 90), grey dashed guides, 90 and 30 in grey, and the word Monopoly beside the dot. Then put 48 over Q in red under the axis, draw the red guide up to demand at (48, 72) with its dot, and show the gold formula P = 120 − (24 + 24) = 120 − 48 = 72. Then draw the guide across and P\* = 72 on the price axis. |
| 6.c | Gold line: “Two sellers: more output, lower price.” |
-->

### {++ Whiteboard | Exercise Q3 ++}

{++ > With two sellers the price is \$72 and each firm’s marginal cost at 24 units is \$48. Is this outcome efficient? Which way would a third seller move it? ++}

<!--
Not built: no exercise card in the animation.

Answer: no. Buyers value the next unit at about \$72 and it costs about \$48 to make, so units worth more than their cost go unmade: there is still deadweight loss, less than under monopoly. A third seller adds output and lowers the price further, toward marginal cost.
-->

## {++ Next time ++}

{++ Next time: what happens with more sellers? ++}

<!--
|   |   |
| --- | --- |
| 7.a | Title: Next Time, with no subtitle. The final picture stays, the market graph on the left and the best-response graph on the right, and a grey arrow points on down the demand curve from the duopoly dot. Gold line: “What happens with more sellers?” |
-->
