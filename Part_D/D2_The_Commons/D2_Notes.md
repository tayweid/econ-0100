---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

# Episode D2 | The Commons

*What makes sense for each of us can leave less for all of us.*

<!--
Draft script and storyboard, 2026-10-20. Not built: all beats below. Intended animation: D2_Animation.py, scene EpisodeD2; no implementation is included in this pass. This is a proposed new script, not a transcription of the 2024 class. The numbered legacy files remain untouched pending review.
Sources and teaching choices: D2_Planning.md. Primary source: Class_On_Oct_30.pdf, pp. 1–2, created October 30, 2024. Preserve its tuna → NPR progression. The new pond model below generates its own payoff numbers; the original tuna matrix is retained in the planning notes and must not be represented as a calculation from this model.
Style references: ../../_Style_Guide.md, ../D1_Games/D1_Notes.md and D1_Animation.py, ../../Part_C/C1_Externalities/C1_Notes.md, ../../Part_C/C3_Corrective_Policy/C3_Notes.md, ../../Part_C/C4_Wrap_Up/C4_Notes.md. Use the current Notes-file convention: section comments index beats; quote blocks give detailed directions; ordinary paragraphs are proposed narration. No student beat links are introduced.
Stage: Graphite 2:1, 15 fps, CMU Serif teaching content, azure topic titles, optional grey CMU Sans subtitle, fixed 0.7443-scale gold teaching line centered 0.05 from the bottom. Body band y = −2.8 to 2.5, centered at −0.15. Import shared style tokens when built. No illustrated fishermen or decorative scenery: one INK pond outline, neutral fish tokens, and named catch trays. Firm 1 is ROW_PLAYER pink; Firm 2 is COL_PLAYER teal. Fish acquire a firm's color only when caught. A fish token represents 1,000 fish; fractional tokens represent fractional thousands, with exact numeric readouts. Keep the pond boundary fixed: fewer fish do not mean less water or a smaller carrying capacity.
Pacing follows C1/C3: quantities first, question and pause, calculation, answer and pause. Carry the same fish into catch trays and the same totals into matrix cells. D1's best-response boxes precede Nash and efficiency conclusions. Each dotted ID is a stopped beat unless its direction explicitly describes a continuous transition.
Suggested core: sections 1–6, about 30–35 minutes with discussion. Optional live simulation goes after beat 3.a, before revealing the outcomes; see D2_Simulation.md. Section 7 is an optional extension, about 5 minutes, or a D3 opener.
-->

## 1 | A shared pond

<!--
1.a · Title “Common Resources”; reuse D1's taxonomy and isolate Common Resources; bottom “What changes when we cannot exclude other users?”
1.b · Carry the category into the pond; one fish moves into Firm 1's tray; bottom “A fish I catch is no longer available for you to catch.”
1.c · Reveal 20 fish tokens and K = 20; bottom “Carrying capacity is a stock, not a monthly catch.”
-->

> **1.a.** Start with D1′s existing taxonomy geometry. Highlight Common Resources, preserving the Rival and Non-Excludable labels, then fade the other categories. Pause before introducing the pond. Do not rerun the A/B/C tour or the deadline activity.

In D1, we learned how to ask what each player would choose, given what the other player does. Today we will build the payoffs from something we can see: two fishing firms using the same pond.

The fish are **rival**: catching one leaves one fewer for someone else. Access is **non-excludable in our setup**: neither firm can keep the other from fishing. These are the characteristics of a **common resource**.

> **1.b.** Center an INK pond outline on the left, with two labeled catch trays below it. Place Firm 1′s pink name over its tray and Firm 2′s teal name over the other. Move one neutral fish token into Firm 1′s tray and recolor it pink. Firm 2′s tray remains empty. Return that fish before the next beat; this was an illustration, not month 1.

The catch belongs to the firm that takes it. The remaining fish, and the fish they can produce, are shared. The private benefit is easy to see. The cost imposed on the other firm is less immediate.

> **1.c.** Show 20 neutral tokens inside the fixed pond. Label it “Stock: 20” and put “Thousands of fish” in a small grey unit caption. Add “Carrying capacity: K = 20” beside the boundary. Keep the right half empty for the next calculation.

The pond can support 20,000 fish. That is its **carrying capacity**. It does not mean we can catch 20,000 fish every month. A stock is measured at a point in time; a harvest is a flow over a period of time.

## 2 | Catch, then reproduce

<!--
2.a · Title “Population And Harvest”; 20 → 10 after a harvest of 10; bottom “How many fish remain to reproduce?”
2.b · Survivors double: 10 → 20; bottom “Ten thousand fish caught; twenty thousand next month.”
2.c · Reset: 20 → 8 → 16 after a harvest of 12; bottom “The same pond now starts next month with fewer fish.”
2.d · Reset: 20 → 16 → 20 after a harvest of 4; bottom “Reproduction is limited by carrying capacity.”
2.e · Reveal S_t = N_t − h_1t − h_2t, then N_(t+1) = min{20, 2S_t}; bottom “Next month's stock depends on what survives this month's catch.”
2.f · Compare recovery from 8 survivors with no further harvest: 8 → 16 → 20; then 0 → 0; bottom “Depletion can be reversed; an empty pond cannot reproduce.”
-->

> **2.a.** Keep the pond left and a calculation area right, separated by the thin vertical divider used in Part C. From a fresh stock of 20, move 5 tokens to each firm’s tray. On the right reveal “Start 20”, then “Catch 10”, then the subtraction “20 − 10 = ?”. Pause before revealing 10 survivors. Keep the month fixed during harvest.

We will use the simple rule from the old classroom game: after the firms fish, the survivors double, up to the pond’s capacity. These are model fish, not a biological estimate for tuna.

> **2.b.** Reveal 10 survivors. Each survivor produces one new token. Fill back to 20, then advance the month once. Reveal “2 × 10 = 20” on the right. Catch trays stay outside the pond: caught fish do not reproduce. Pause at the restored stock.

If we catch 10,000 fish from a full pond, 10,000 remain. They reproduce, and next month we have 20,000 again. We can repeat this harvest without reducing the starting stock.

> **2.c.** Reset stock, clock, and catch trays. Move 6 tokens to each tray. Pause at “20 − 12 = 8”, then reproduce to 16 and advance the month. Show the three numbers 20 → 8 → 16 with “Start”, “Survivors”, and “Next month” above them. Remove the previous example’s arithmetic first.

If we catch 12,000, only 8,000 remain. Next month there are 16,000 fish. Reproduction helps, but it does not replace everything we took.

> **2.d.** Reset again. Catch 2 per firm. Reveal 16 survivors, then “min{20, 2 × 16} = 20”. Add only 4 new tokens; do not draw 32 fish and quietly delete 12. The capacity label briefly receives a FOCUS outline, which leaves before the next beat.

If we leave 16,000 fish, the pond does not grow to 32,000. The carrying capacity limits the population. Leaving more fish does not always produce more fish next month.

Let $N_t$ be the stock at the start of month $t$, and let $h_{1t}$ and $h_{2t}$ be the firms’ catches during that month. All quantities are in thousands of fish. Survivors are

$$
S_t = N_t-h_{1t}-h_{2t}.
$$

The next month’s stock is

$$
N_{t+1}=\min\{20,\;2S_t\}.
$$

> **2.e.** Replace the example arithmetic with the two general equations, one at a time. Point each quantity to the existing stock or catch tray before adding its symbol. Keep “Harvest → Reproduction → Next month” over the calculation area. Require total catch to be no larger than the stock; there are no negative fish.

> **2.f.** Show 8 survivors from the earlier example. With no further fishing, reproduce to 16 and then to 20 over two month advances. Reset to zero survivors and advance once: zero remains. Keep the capacity label at 20 in both cases. Clear the recovery example before section 3.

Overharvesting need not mean immediate extinction. A depleted population can recover if enough fish remain and fishing falls. But zero stays zero in this model: we have assumed no restocking or migration.

## 3 | Two strategies, three months

<!--
3.a · Title “The Fishing Game”; show L = catch 1/4 of current stock and H = catch 1/2; bottom “Choose a fishing strategy for all three months.”
3.b · L,L: three harvests of 5 each; bottom “Low harvests maintain the stock.”
3.c · H,L: Firm 1 catches 10, 5, 2.5; Firm 2 catches 5, 2.5, 1.25; bottom “A larger share today can mean a smaller pond tomorrow.”
3.d · H,H: each catches 10, 0, 0; bottom “Both firms take more at first, then there are no fish left.”
3.e · Hold three Firm 1 harvest paths on the same axes; bottom “The payoff counts all three months.”
-->

We need to specify the game before solving it. Each firm chooses a fishing strategy at the beginning and keeps it for three months:

- **Low, L:** catch one-quarter of the stock each month.
- **High, H:** catch one-half of the stock each month.

Both firms fish simultaneously from that month’s starting stock. The percentages are not applied one after the other. Even two High choices take no more than the available fish.

The payoff is the firm’s **total catch over three months**, in thousands of fish. Every unit of catch has the same value, and we leave fishing costs out of this first model. We score only these three months; fish left at the end are not added to the score. We are comparing two committed strategies, not allowing a new decision each month.

> **3.a.** Reset the pond to 20 and the clock to month 1. Put the L/H rules at right with a three-month timeline below. Reveal “Payoff = catch in month 1 + month 2 + month 3”. Pause before any strategy profile or payoff is shown. Keep this equation as quiet context during the runs.

> **3.b.** Select L for both firms. Run the same harvest-then-reproduction choreography three times: each catches 5; 10 survive; stock returns to 20. Stop after the first cycle for a prediction, then after the third. Keep each month’s catch in a separate tray compartment. Reveal each total only after its three catches are present: 5 + 5 + 5 = 15. Retain “L,L: 15 | 15” as a small result card, then clear trays before the next run.

With two Low strategies, each firm catches 5,000 fish per month. Each collects 15,000 over three months, and the pond keeps returning to capacity.

> **3.c.** Reset to 20. Select H for Firm 1 and L for Firm 2. Run month 1 slowly: catches 10 and 5, survivors 5, next stock 10. Pause before asking for month 2′s catches. Continue with catches 5 and 2.5, next stock 5; then 2.5 and 1.25, next stock 2.5. Fractional tokens and numeric labels must agree. Reveal totals 17.5 and 8.75. Retain “H,L: 17.5 | 8.75”. State that exchanging the firms exchanges the two payoffs; a fourth full pond run is unnecessary.

If Firm 1 switches to High while Firm 2 stays Low, Firm 1 catches more. But the combined catch leaves too few survivors to restore the pond. The starting stock halves each month: 20, then 10, then 5. Firm 1 gets 17,500 fish in total. Firm 2 gets 8,750.

> **3.d.** Reset to 20. Select H for both firms. Move 10 tokens to each tray simultaneously, leaving zero. Advance through the remaining months with empty catches. Reveal 10 + 0 + 0 = 10 for each firm. Retain “H,H: 10 | 10”. Do not animate spontaneous recovery.

If both choose High, they empty the pond in the first month. Each gets 10,000 fish, and nothing in months 2 and 3.

> **3.e.** Replace the pond with a full-width plot, horizontal axis “Month” at 1, 2, 3; vertical axis “Firm 1′s catch” from 0 to 10, with “Thousands of fish per month” in grey. Reveal the sequences (5,5,5), (10,5,2.5), (10,0,0) in run order. Use ROW_PLAYER for all three, distinguished by solid/dashed/dotted lines and direct L,L / H,L / H,H labels; temporarily dim earlier paths while revealing another. Join observations with straight segments, not a smooth biological curve. The catch totals remain beside their paths. Do not relabel this harvest plot as population.

The first month’s biggest catch is not necessarily the best three-month outcome. Now we can put the whole consequence of each pair of strategies into a matrix.

## 4 | The pond becomes a payoff matrix

<!--
4.a · Title “The Fishing Game”; transfer calculated totals into D1's diamond matrix; bottom “Firm 1's payoff first; Firm 2's payoff second.”
4.b · Hold Firm 2 at L; bottom “If Firm 2 chooses Low, what is Firm 1's best response?”
4.c · Box 17.5 in pink; bottom “High: 17.5 > 15.”
4.d · Hold Firm 2 at H; bottom “If Firm 2 chooses High, what is Firm 1's best response?”
4.e · Box 10 in pink; bottom “High: 10 > 8.75.”
4.f · Hold Firm 1 at L; bottom “If Firm 1 chooses Low, what is Firm 2's best response?”
4.g · Box 17.5 in teal; bottom “High: 17.5 > 15.”
4.h · Hold Firm 1 at H; bottom “If Firm 1 chooses High, what is Firm 2's best response?”
4.i · Box 10 in teal; bottom “High: 10 > 8.75.”
4.j · Remove choice shading; outline H,H in NASH red; bottom “Neither firm gains by changing its strategy alone.”
4.k · Add totals 30, 26.25, 26.25, 20; outline L,L in EFFICIENT green; bottom “Both firms would catch more if both chose Low.”
-->

> **4.a.** Fade the plot while carrying its three result cards into D1′s matrix layout. Use 1.5-unit square cells rotated clockwise 45 degrees; board center (0, −0.5); keep text horizontal and player names at y = 2.0. Firm 1 is the row player, Firm 2 the column player. Original upper-left L,L is the top diamond cell; L,H right; H,L left; H,H bottom. Fill L,L, H,L, its reflected L,H, then H,H, completing each payoff pair before the next. Strategy labels are grey CMU Sans; payoffs use player colors. No best-response, Nash, or efficiency boxes yet.

| Firm 1 / Firm 2 | Low | High |
| --- | --- | --- |
| Low | 15, 15 | 8.75, 17.5 |
| High | 17.5, 8.75 | 10, 10 |

> **4.b–4.i.** Follow the eight separate question/answer pauses indexed above. For Firm 1, shade only Firm 2′s fixed column teal at 12% opacity and underline its fixed strategy. On each answer add the pink box around Firm 1′s best-response payoff. Then switch perspective: remove the teal band and underline, shade only Firm 1′s fixed row pink, and add teal boxes around Firm 2′s answers. Keep earlier payoff boxes. Never show both background bands at once. Use the existing D1 geometry rather than a new matrix treatment.

If Firm 2 chooses Low, Firm 1 compares 15 with 17.5 and chooses High. If Firm 2 chooses High, Firm 1 compares 8.75 with 10 and again chooses High. High is a **strictly dominant strategy** for Firm 1. The same comparisons apply to Firm 2.

> **4.j.** Remove fixed-choice underlines and background bands. Retain payoff boxes and add D1′s equal-size red Nash outline around H,H. Pause on the unilateral-deviation test before saying “Nash equilibrium.”

The **Nash equilibrium** is High, High. Given the other firm’s strategy, neither firm can improve its payoff by changing alone.

> **4.k.** Reveal the sum of the two payoffs for each outcome outside its cell, then a green efficiency outline around L,L, equal in size to the red outline. Retain both outcomes for comparison. Do not confuse an outcome’s total with either player’s individual payoff.

But both firms would get 15 instead of 10 if they both chose Low. Low, Low also produces the largest combined catch among the four strategy pairs: 30,000 fish. The equilibrium and the jointly best outcome differ.

This is the **tragedy of the commons**: individual incentives can lead to overuse of a shared resource. The problem is not that the fish cannot reproduce. It is that neither firm has an incentive to choose the strategy that works best when both follow it.

## 5 | The incentive we are missing

<!--
5.a · Title “Private And Shared Consequences”; reopen L,L → H,L; bottom “The extra catch benefits one firm and reduces the other's catch.”
5.b · Title “Changing The Game”; return to the unmarked matrix; bottom “What would make Low a best response?”
-->

> **5.a.** Carry the L,L and H,L payoff pairs out of the matrix into two side-by-side comparisons. Reveal Firm 1′s change, 17.5 − 15 = +2.5, then pause. Reveal Firm 2′s change, 8.75 − 15 = −6.25, then the combined change, −3.75. Keep the comparison on one common baseline, using the firms’ colors and TOTAL purple for the combined result. Reveal only one calculation at a time; clear each question before its answer.

Return to the question from Part C: what does the decision maker count, and what happens to everyone affected? When Firm 1 switches to High against Low, it gains 2,500 fish. Firm 2 loses 6,250. The combined catch falls by 3,750.

This is an external cost. Firm 1 bears some of the effect of reducing the stock, but it does not bear Firm 2′s loss. Knowing that cooperation would help both firms is not enough to make cooperation a best response.

> **5.b.** Restore the original calculated matrix without Nash/efficiency outlines. Hold on the question. After discussion, reveal three short grey labels beside it, one at a time: “Harvest rules”, “Monitoring”, “Consequences for violations”. Do not display an altered numerical matrix without specifying an actual enforcement rule.

An agreement can work if the rules and incentives support it. We could limit harvests, observe catches, and enforce the limits. We could also ask how communication and future dealings affect behavior. Shared use does not guarantee failure; this particular game explains why cooperation needs support.

## 6 | From taking fish to funding a broadcast

<!--
6.a · Title “Public Goods”; return to D1's taxonomy and move from Common Resources to Public Goods; bottom “Listening does not use up the broadcast.”
6.b · Title “The Contribution Game”; show two endowments of 15 and choices C = 15 or DC = 0; bottom “Do I contribute, or keep my money?”
6.c · Move one contribution of 15 into the fund; reveal a benefit of 10 to each player; bottom “A contribution costs me 15 and benefits each of us by 10.”
6.d · Fill the NPR matrix from retained money plus broadcast benefits; bottom “Payoff = money kept + benefit from the broadcast.”
6.e · Hold the other player at C; bottom “If the other player contributes, what is my best response?”
6.f · Box 25 rather than 20; bottom “Do not contribute: 25 > 20.”
6.g · Hold the other player at DC; bottom “If the other player does not contribute, what is my best response?”
6.h · Box 15 rather than 10; bottom “Do not contribute: 15 > 10.”
6.i · Mirror the comparisons for Player 2; outline DC,DC red and C,C green; bottom “Each prefers not to contribute; both would benefit from contributing.”
6.j · Side-by-side taxonomy cells and conclusions; bottom “The commons is overused; the public good is underprovided.”
-->

> **6.a.** Clear the fish and matrix. Reuse D1′s taxonomy again and move the category outline from Common Resources to Public Goods. Retain Non-Excludable; change Rival to Non-Rival. Use the words “Radio broadcast” as the concrete example, without a decorative radio illustration.

Now change the resource. If I listen to a radio broadcast, that does not leave less broadcast for you. And, in our example, people can listen whether or not they help pay for it. The broadcast is **non-rival** and **non-excludable**: a **public good**.

The station still needs resources to produce the program. So instead of asking how much we take, ask how much we contribute.

> **6.b.** Show Player 1 and Player 2 in D1′s pink and teal, each with 15 money units. Put an empty shared “Broadcast fund” between them. Define C as contributing all 15 and DC as contributing zero. Pause before revealing a benefit rule.

Each player has 15 and can contribute all of it or none. Every 15 contributed produces a broadcast benefit worth 10 to **each** player. The benefit is available to contributors and non-contributors alike.

> **6.c.** Move Player 1′s 15 into the fund. Show “Money kept: 0” under Player 1 and “Money kept: 15” under Player 2. Reveal a benefit of 10 to each, then totals 10 and 25. Two benefit labels are valuations of the same broadcast, not cash distributed out of the fund. Pause on the private cost 15 versus own benefit 10 before revealing combined benefit 20.

For each player, the payoff is money kept plus the value of the broadcast:

$$
u_i=15-c_i+\frac{2}{3}(c_1+c_2),\qquad c_i\in\{0,15\}.
$$

> **6.d.** Transfer the completed C,DC pair into D1′s diamond matrix. Then fill DC,DC from 15 + 0 for each; C,C from 0 + 20 for each; and DC,C by symmetry. Complete both players’ payoffs at each step. Use C/DC on the matrix, with the full choices visible once above it.

| Player 1 / Player 2 | Contribute | Do not contribute |
| --- | --- | --- |
| Contribute | 20, 20 | 10, 25 |
| Do not contribute | 25, 10 | 15, 15 |

> **6.e–6.h.** Keep separate question and answer pauses. Use D1′s fixed-choice shading and player-colored payoff boxes. First compare 25 with 20, then 15 with 10. Do not outline a Nash cell before the comparisons.

If the other player contributes, I prefer 25 to 20: I enjoy the broadcast and keep my money. If the other player does not contribute, I prefer 15 to 10: making the contribution costs me more than the benefit I receive myself.

> **6.i.** Repeat the comparisons for Player 2 with brief pauses, then remove strategy shading. Mark DC,DC red and C,C green, retaining both. Show combined payoffs 30 and 40 beside those two cells.

Not contributing is a strictly dominant strategy for each player. Neither contributes in equilibrium, even though both would be better off if both contributed.

This is the **free rider problem**: people can benefit without contributing, so individual incentives can leave a public good underprovided. At the all-DC equilibrium there is no broadcast to enjoy; the incentive to free ride helps explain why it is not funded.

> **6.j.** Replace the matrices with the two relevant taxonomy cells. Under Common Resources show “Take too much”; under Public Goods show “Contribute too little”. Retain the shared Non-Excludable label and distinguish Rival from Non-Rival. End on the quoted teaching line.

In the pond, taking more leaves less for others. In the broadcast, contributing more benefits others. In both cases, the private decision leaves out part of its effect on other people. D1 gives us the same way to analyze both: find best responses, find the equilibrium, then compare it with what is best for the group.

## 7 | Optional bridge to the three-player game

<!--
7.a · Title “Three Contributors”; add a third player and c_3 to the benefit sum; bottom “The private return stays below the contribution.”
7.b · Compare all-DC payoffs 15 each with all-C payoffs 30 each; bottom “The shared benefit can exceed the private cost.”
-->

> **7.a.** Clear the two-player matrix before adding Player 3. Preserve endowment 15 and benefit factor 2/3. Reveal the source notes’ formula u_i = 15 − c_i + (2/3)(c_1 + c_2 + c_3). Show one contributor: that player gets 10; each non-contributor gets 25. Do not reuse the two-player matrix for three players.

The October 30 example also uses three players. A contribution of 15 still gives its contributor a benefit of 10. The contributor’s own payoff falls by 5. But now three people each receive a benefit of 10, so the total benefit is 30.

> **7.b.** Compare two complete outcome strips: nobody contributes, payoffs (15,15,15), total 45; everybody contributes, payoffs (30,30,30), total 90. Keep the same contribution units. End with the spoken question about institutions; do not begin the voting example here.

Each person still has an incentive not to contribute. Yet all three would benefit if all contributed. Next we can ask how a group might arrange to fund the good, and what voting does or does not solve.
