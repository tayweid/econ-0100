---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

# Episode D3 | Public Goods

*People can benefit from a public good without contributing to its provision.*

<!--
NPR donation-game script and storyboard moved from D2 on 2026-10-21 at Taylor's request. Original D2 sections 6 and 7 are now D3 sections 1 and 2; the substantive examples and payoff values are unchanged. First runnable draft built October 27, 2026: D3_Animation.py, scene EpisodeD3. The original NPR narration below is retained; 02_Storyboard.md is the current animation choreography and 30-minute teaching plan. D2_Animation.py contains common resources only.
Source: ../D2_The_Commons/Class_On_Oct_30.pdf. Keep the two-player NPR matrix and three-player benefit formula from the October 30 notes. Use D1's diamond matrix, player-colored best-response boxes, single fixed-choice band, and separate question/answer pauses. Use the shared Graphite typography, 2:1 frame, and 15 fps conventions in ../../_Style_Guide.md. The legacy 01_Notes.md and code stubs remain preserved. The new animation continues through Dobby, majority voting, a brief Condorcet cycle, and Arrow; see sections 3–5 below and 02_Storyboard.md.
-->

## 1 | The NPR donation game

<!--
1.a · Title “Public Goods”; return to D1's taxonomy and move from Common Resources to Public Goods; bottom “Listening does not use up the broadcast.”
1.b · Title “The Contribution Game”; show two endowments of 15 and choices C = 15 or DC = 0; bottom “Do I contribute, or keep my money?”
1.c · Move one contribution of 15 into the fund; reveal a benefit of 10 to each player; bottom “A contribution costs me 15 and benefits each of us by 10.”
1.d · Fill the NPR matrix from retained money plus broadcast benefits; bottom “Payoff = money kept + benefit from the broadcast.”
1.e · Hold the other player at C; bottom “If the other player contributes, what is my best response?”
1.f · Box 25 rather than 20; bottom “Do not contribute: 25 > 20.”
1.g · Hold the other player at DC; bottom “If the other player does not contribute, what is my best response?”
1.h · Box 15 rather than 10; bottom “Do not contribute: 15 > 10.”
1.i · Mirror the comparisons for Player 2; outline DC,DC red and C,C green; bottom “Each prefers not to contribute; both would benefit from contributing.”
1.j · Side-by-side taxonomy cells and conclusions; bottom “The commons is overused; the public good is underprovided.”
-->

> **1.a.** Open D3 with the NPR donation example. Reuse D1′s taxonomy again and move the category outline from Common Resources to Public Goods. Retain Non-Excludable; change Rival to Non-Rival. Use the words “Radio broadcast” as the concrete example, without a decorative radio illustration.

In D2 we studied a shared fishery. Now change the resource. If I listen to a radio broadcast, that does not leave less broadcast for you. And, in our example, people can listen whether or not they help pay for it. The broadcast is **non-rival** and **non-excludable**: a **public good**.

The station still needs resources to produce the program. So instead of asking how much we take, ask how much we contribute.

> **1.b.** Show Player 1 and Player 2 in D1′s pink and teal, each with 15 money units. Put an empty shared “Broadcast fund” between them. Define C as contributing all 15 and DC as contributing zero. Pause before revealing a benefit rule.

Each player has 15 and can contribute all of it or none. Every 15 contributed produces a broadcast benefit worth 10 to **each** player. The benefit is available to contributors and non-contributors alike.

> **1.c.** Move Player 1′s 15 into the fund. Show “Money kept: 0” under Player 1 and “Money kept: 15” under Player 2. Reveal a benefit of 10 to each, then totals 10 and 25. Two benefit labels are valuations of the same broadcast, not cash distributed out of the fund. Pause on the private cost 15 versus own benefit 10 before revealing combined benefit 20.

For each player, the payoff is money kept plus the value of the broadcast:

$$
u_i=15-c_i+\frac{2}{3}(c_1+c_2),\qquad c_i\in\{0,15\}.
$$

> **1.d.** Transfer the completed C,DC pair into D1′s diamond matrix. Then fill DC,DC from 15 + 0 for each; C,C from 0 + 20 for each; and DC,C by symmetry. Complete both players’ payoffs at each step. Use C/DC on the matrix, with the full choices visible once above it.

| Player 1 / Player 2 | Contribute | Do not contribute |
| --- | --- | --- |
| Contribute | 20, 20 | 10, 25 |
| Do not contribute | 25, 10 | 15, 15 |

> **1.e–1.h.** Keep separate question and answer pauses. Use D1′s fixed-choice shading and player-colored payoff boxes. First compare 25 with 20, then 15 with 10. Do not outline a Nash cell before the comparisons.

If the other player contributes, I prefer 25 to 20: I enjoy the broadcast and keep my money. If the other player does not contribute, I prefer 15 to 10: making the contribution costs me more than the benefit I receive myself.

> **1.i.** Repeat the comparisons for Player 2 with brief pauses, then remove strategy shading. Mark DC,DC red and C,C green, retaining both. Show combined payoffs 30 and 40 beside those two cells.

Not contributing is a strictly dominant strategy for each player. Neither contributes in equilibrium, even though both would be better off if both contributed.

This is the **free rider problem**: people can benefit without contributing, so individual incentives can leave a public good underprovided. At the all-DC equilibrium there is no broadcast to enjoy; the incentive to free ride helps explain why it is not funded.

> **1.j.** Replace the matrices with the two relevant taxonomy cells. Under Common Resources show “Take too much”; under Public Goods show “Contribute too little”. Retain the shared Non-Excludable label and distinguish Rival from Non-Rival. End on the quoted teaching line.

In the pond, taking more leaves less for others. In the broadcast, contributing more benefits others. In both cases, the private decision leaves out part of its effect on other people. D1 gives us the same way to analyze both: find best responses, find the equilibrium, then compare it with what is best for the group.

## 2 | The three-player game

<!--
2.a · Title “Three Contributors”; add a third player and c_3 to the benefit sum; bottom “The private return stays below the contribution.”
2.b · Compare all-DC payoffs 15 each with all-C payoffs 30 each; bottom “The shared benefit can exceed the private cost.”
-->

> **2.a.** Clear the two-player matrix before adding Player 3. Preserve endowment 15 and benefit factor 2/3. Reveal the source notes’ formula u_i = 15 − c_i + (2/3)(c_1 + c_2 + c_3). Show one contributor: that player gets 10; each non-contributor gets 25. Do not reuse the two-player matrix for three players.

The October 30 example also uses three players. A contribution of 15 still gives its contributor a benefit of 10. The contributor’s own payoff falls by 5. But now three people each receive a benefit of 10, so the total benefit is 30.

> **2.b.** Compare two complete outcome strips: nobody contributes, payoffs (15,15,15), total 45; everybody contributes, payoffs (30,30,30), total 90. Keep the same contribution units. End with the spoken question about institutions; do not begin the voting example here.

Each person still has an incentive not to contribute. Yet all three would benefit if all contributed. Next we can ask how a group might arrange to fund the good, and what voting does or does not solve.

## 3 | Memorial to Dobby

The October 30 PDF’s second page turns to a memorial. Its five residents are Harry, Ron, Hermione, Ginny, and Neville, with annual benefits of 34, 29, 24, 19, and 14 ~~galleons~~{++coins++}. The annual cost is 100. The vignette uses different names with the same benefits; the animation follows the PDF.

Everyone can enjoy the memorial whether or not they help pay for it. All five would visit if it were freely available. An equal tax of 20 is different from a voluntary contribution: if the referendum passes, everyone pays. Three people value the memorial above 20 and two below 20, so it passes 3–2. The tax raises exactly 100.

Is the project efficient? Add the five benefits from the same memorial, rather than treating them as separate quantities of memorials. The marginal social benefit is 120, greater than the marginal social cost of 100. Building it creates a net gain of 20. That does not mean everyone benefits under the equal tax: Ginny and Neville lose 1 and 6 respectively.

The vignette also asks about a tax of 25. Only two residents favor that proposal. It fails 2–3. The project still costs 100; the hypothetical tax would raise 125 if passed, so it is not the same budget-balanced financing plan.

Now suppose a private operator could restrict access and charge a single annual admission fee. This changes the exclusion assumption. At a fee of 20, three people buy and revenue is 60. At 24, three buy and revenue is 72. At 19, four buy and revenue is 76. These calculations assume buyers purchase at equality. To verify the maximum, the other candidate prices are 34, 29, and 14, generating revenues 34, 58, and 70. No uniform fee covers 100 even though total willingness to pay is 120. Private revenue and social benefit are different objects.

The older outline mentions Lindahl and preference elicitation. A short bridge is enough here: payments of 30, 25, 20, 15, and 10 raise exactly 100 and leave every resident a net benefit of 4. Different payments can make all five favor funding the project. The hard part is learning their true willingness to pay when each has a reason to understate it. This is a simple feasible cost split, not a formal derivation of Lindahl equilibrium.

## 4 | Majority voting and efficiency

Dobby’s equal-tax vote happens to choose the efficient outcome. It need not always work that way. The Dumbledore exercise provides the counterexample: Aurelius, Aberforth, and Ariana have benefits 75, 10, and 20. The project costs 90, financed by a tax of 30 each. Only Aurelius votes Yes, so the proposal fails. Yet benefits total 105, exceeding cost by 15.

Majority voting counts the number of people who gain or lose under a proposal. It does not count how large those gains and losses are. Keep the decision to build a project distinct from the question of how its cost is shared. The Yule Ball homework supplies another application for practice.

## 5 | Brief limits of voting

The old schedule lists contributions and a referendum before a later class on three-ballot voting, Condorcet cycles, and Arrow. The dated entries are from 2023 with Fall 2024 episode annotations, so they do not establish the exact Fall 2024 class order. The October 30, 2024 PDF itself covers tuna, NPR, then Dobby; it does not contain a voting-cycle example.

Use a new, short illustration: voter 1 ranks A above B above C, voter 2 ranks B above C above A, and voter 3 ranks C above A above B. A beats B 2–1; B beats C 2–1; C beats A 2–1. Individual rankings are consistent, but the majority relation cycles. No alternative beats every other one. Voting on A against B, then the winner against C, selects C. Voting on B against C, then the winner against A, selects A, assuming sincere votes in each contest.

Arrow’s theorem extends the warning beyond this particular majority rule. With three or more alternatives, no rule can accept every profile of individual rankings, respect unanimity, make each pairwise social comparison depend only on individual rankings of that pair, avoid a dictator, and always produce a complete, transitive social ranking. Here a dictator means one individual’s strict preferences always determine the social ranking, not a claim about a political regime. See [Geanakoplos’s statement and proofs](https://cowles.yale.edu/sites/default/files/2022-08/d1123-r4.pdf). Keep this to the statement and its meaning; there is no proof in the draft.

Close by connecting the institutions to the incentives. Common resources can be overused; public goods can be underprovided. Voting can help fund a public good, but voting and efficient choice are not the same thing.
