---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

# Episode D3 | Public Goods

*People can benefit from a public good without contributing to its provision.*

| Section | Minutes | Focus |
| --- | --- | --- |
| Opening | 6 | Bumper; Exercise D3 Q1’s setup with parts a) and b), in small groups, then discussed together |
| NPR, two players | 9 | Taxonomy, one contribution, matrix, best responses, free rider problem, taxonomy contrast |
| NPR, three players | 2 | Same private incentive; larger shared benefit |
| Dobby | 11 | Visits, tax vote, social benefit, higher tax, admission, personalized payments |
| Exercise D3 card | 2 | Dumbledore memorial, questions only |
| Voting limits | 4 | One cycle, agenda order, brief Arrow statement |
| Close | 1 | Connect back to D2 |

<!--
|   |   |
| --- | --- |
| Animation | D3_Animation.py, scene EpisodeD3, 58 holds. The timing table above is the classroom budget from the October 28 storyboard. |
| Model | NPR game: each player has 15 and contributes all or none; Payoff_i = (15 − c_i) + (c_1 + c_2) · 2/3. Dobby: benefits 34, 29, 24, 19, 14 against an annual cost of 100. Dumbledore exercise: benefits 75, 10, 20 against a cost of 90. |
| Open | The opening paragraph of “Brief limits of voting” is a research note about the old schedule, not lecture prose. |
| Open | The names follow the October 30, 2024 handwritten notes (../D_Class_On_Oct_30_Dobby_plus_Tuna.pdf); the vignette uses different names with the same numbers. |
| Marked | Everything inside addition marks is Claude’s: the warmup line and two bridges in the NPR game. |
| Archive | The October 28 storyboard, the earlier notes, the code stubs and the direction blocks that used to sit in this file are in _archive/2026-11-12_consolidation/. |
-->

## {++ Warmup ++}

{++ Start in groups with Exercise D3, Q1: the Dumbledore memorial, parts a) and b). We come back to it after Dobby. ++}

<!--
|   |   |
| --- | --- |
| 0.a | Bumper: Part D | Episode 3. |
| 0.b | Title “Warmup”. The Exercise D3 Q1 card, with the memorial’s setup and parts a) and b). |
-->

## 1 | The NPR donation game

In D2 we studied a shared fishery. Now change the resource. If I listen to a radio broadcast, that does not leave less broadcast for you. And, in our example, people can listen whether or not they help pay for it. The broadcast is **non-rival** and **non-excludable**: a **public good**.

<!--
|   |   |
| --- | --- |
| 1.a.commons | Title “Common Resources”. D1’s taxonomy with the box on Common Resources, last time’s topic. |
| 1.a | The box slides to Public Goods. Subtitle: “Goods that are non-rival and non-excludable.” |
-->

The station still needs resources to produce the program. So instead of asking how much we take, ask how much we contribute.

Each player has 15 and can contribute all of it or none. Every 15 contributed produces a broadcast benefit worth 10 to **each** player. The benefit is available to contributors and non-contributors alike.

<!--
|   |   |
| --- | --- |
| 1.b.rule | Title “The NPR Game”; subtitle “Everyone can listen, whether or not they contribute.” The payoff rule alone: Payoff_i = (15 − c_i) + (c_1 + c_2) · 2/3. |
| 1.b.kept | A brace under the first term: “the money I keep”. |
| 1.b.fund | A brace under the second: “funding NPR”. |
| 1.b | The rule moves up; the two strategies, Contribute (C): 15 and Do not contribute (DC): 0; an empty graph of Player 1’s payoff against Player 2’s contribution. “Do I contribute, or keep my money?” |
-->

For each player, the payoff is money kept plus the value of the broadcast:

$$
u_i=15-c_i+\frac{2}{3}(c_1+c_2),\qquad c_i\in\{0,15\}.
$$

<!--
|   |   |
| --- | --- |
| 1.d.rule | Player 1’s row under the rule. “Player 1’s payoff: the rule, with i = 1.” |
| 1.d.c1 | “Player 1 contributes: c_1 = 15.” |
| 1.d.c2 | “Player 2 does not: c_2 = 0.” |
| 1.d.p1 | The row resolves to 10. “Player 1 keeps nothing and gets two thirds of 15.” |
| 1.d.rule2 | “Player 2’s payoff: the same rule, with i = 2.” |
| 1.d.choices2 | “Player 2 keeps 15: c_2 = 0. Player 1 put in c_1 = 15.” |
| 1.d.payoffs | The row resolves to 25. “A contribution costs me 15 and benefits each of us by 10.” |
| 1.e.graph | The two results become the first point on the graph, C,DC 10 and 25. “Each run is a point: Player 1′s payoff against Player 2′s contribution.” |
-->

{++ Run the other three cases the same way. If nobody contributes, each keeps 15. If both contribute, each gets 20. And if only Player 2 contributes, Player 1 keeps 15 and still gets 10, for 25. ++}

<!--
|   |   |
| --- | --- |
| 1.f.payoffs | “Nobody contributes: each keeps 15.” |
| 1.f.graph | The point DC,DC 15 and 15. |
| 1.g.payoffs | “Both contribute: each receives 20.” |
| 1.g.graph | The point C,C 20 and 20, and the C line through the two contributing points. |
| 1.h.payoffs | “Switch the contributor; switch the payoffs.” |
| 1.h.graph | The point DC,C 25 and 10, and the DC line, 5 above C. “Whatever Player 2 does, not contributing pays 5 more.” |
-->

{++ Now put the four results in a matrix, Player 1’s payoff first. ++}

| Player 1 / Player 2 | Contribute | Do not contribute |
| --- | --- | --- |
| Contribute | 20, 20 | 10, 25 |
| Do not contribute | 25, 10 | 15, 15 |

<!--
|   |   |
| --- | --- |
| 1.i.matrix | The graph shrinks to the left; the diamond matrix appears and the four pairs move into its cells. “Player 1's payoff first; Player 2's payoff second.” |
-->

If the other player contributes, I prefer 25 to 20: I enjoy the broadcast and keep my money. If the other player does not contribute, I prefer 15 to 10: making the contribution costs me more than the benefit I receive myself.

<!--
|   |   |
| --- | --- |
| 1.j.response-c | Player 2 held at Contribute. “If Player 2 contributes, what is Player 1′s best response?” |
| 1.k.answer-c | 25 is boxed. “Do not contribute: 25 > 20.” |
| 1.l.response-dc | Player 2 held at Do not contribute. “If Player 2 does not contribute, what is Player 1′s best response?” |
| 1.m.answer-dc | 15 is boxed. “Do not contribute: 15 > 10.” |
-->

Not contributing is a strictly dominant strategy for each player. Neither contributes in equilibrium, even though both would be better off if both contributed.

<!--
|   |   |
| --- | --- |
| 1.n.symmetry | Player 2’s boxes, by symmetry. “The same comparisons hold for Player 2. Neither contributes.” |
| 1.n.nash | A red square on DC, DC. “Neither player gains by changing alone.” |
-->

This is the **free rider problem**: people can benefit without contributing, so individual incentives can leave a public good underprovided. At the all-DC equilibrium there is no broadcast to enjoy; the incentive to free ride helps explain why it is not funded.

<!--
|   |   |
| --- | --- |
| 1.o.free-rider | A green square on C, C, with “20 > 15 for each player.” “Free rider problem” in gold, with its definition. |
-->

In the pond, taking more leaves less for others. In the broadcast, contributing more benefits others. In both cases, the private decision leaves out part of its effect on other people. D1 gives us the same way to analyze both: find best responses, find the equilibrium, then compare it with what is best for the group.

<!--
|   |   |
| --- | --- |
| 1.p.contrast | Title “Common Resources And Public Goods”. The taxonomy with both bottom cells boxed: “Take too much” and “Contribute too little”. “The commons is overused; the public good is underprovided.” |
-->

## 2 | The three-player game

The October 30 example also uses three players. A contribution of 15 still gives its contributor a benefit of 10. The contributor’s own payoff falls by 5. But now three people each receive a benefit of 10, so the total benefit is 30.

<!--
|   |   |
| --- | --- |
| 2.a.one | Title “Three Contributors”. The same rule with a third contribution, and a third player in purple. “One contributor: 10 for them, 25 for each of the others.” |
-->

Each person still has an incentive not to contribute. Yet all three would benefit if all contributed. Next we can ask how a group might arrange to fund the good, and what voting does or does not solve.

<!--
|   |   |
| --- | --- |
| 2.b.none | “Nobody contributes: 15 each.” |
| 2.c.all | “Everybody contributes: 30 each. Could a group arrange that?” |
-->

## 3 | Memorial to Dobby

The October 30 PDF’s second page turns to a memorial. Its five residents are Harry, Ron, Hermione, Ginny, and Neville, with annual benefits of 34, 29, 24, 19, and 14 ~~galleons~~{++coins++}. The annual cost is 100. The vignette uses different names with the same benefits; the animation follows the PDF.

<!--
|   |   |
| --- | --- |
| 3.a.visits | Title “A Memorial To Dobby”. Five benefit bars, Harry 34, Ron 29, Hermione 24, Ginny 19, Neville 14, and “Annual cost: 100”. “If it is built, how many people will visit?” |
-->

Everyone can enjoy the memorial whether or not they help pay for it. All five would visit if it were freely available. An equal tax of 20 is different from a voluntary contribution: if the referendum passes, everyone pays. Three people value the memorial above 20 and two below 20, so it passes 3–2. The tax raises exactly 100.

<!--
|   |   |
| --- | --- |
| 3.b.all-five | “Visitors: 5”. “All five: each gets a benefit, and no one can be kept out.” |
| 3.c.vote | A red line at 20 crosses the bars, read like a price. “Would a tax of 20 each pass a majority vote?” |
| 3.d.passes | Checks under Harry, Ron and Hermione, crosses under Ginny and Neville: 3 Yes, 2 No, and 5 × 20 = 100. “It passes, and the tax pays for the memorial.” |
-->

Is the project efficient? Add the five benefits from the same memorial, rather than treating them as separate quantities of memorials. The marginal social benefit is 120, greater than the marginal social cost of 100. Building it creates a net gain of 20. That does not mean everyone benefits under the equal tax: Ginny and Neville lose 1 and 6 respectively.

<!--
|   |   |
| --- | --- |
| 3.d.outvoted | “Ginny and Neville pay 20 for benefits of 19 and 14.” |
| 3.e.efficiency | The vote clears; the bars and the tax line stay. “Is building the memorial socially efficient?” |
| 3.f.efficient | The five bars stack into one, MSB 120, against a line at MSC 100. “MSB = 120 > MSC = 100: building it is efficient.” |
-->

The vignette also asks about a tax of 25. Only two residents favor that proposal. It fails 2–3. The project still costs 100; the hypothetical tax would raise 125 if passed, so it is not the same budget-balanced financing plan.

<!--
|   |   |
| --- | --- |
| 3.g.tax25 | The tax line rolls up to 25. “What if the proposed tax were 25 each?” |
| 3.h.fails | 2 Yes, 3 No. “It fails, even though the memorial is still efficient.” |
-->

Now suppose a private operator could restrict access and charge a single annual admission fee. This changes the exclusion assumption. At a fee of 20, three people buy and revenue is 60. At 24, three buy and revenue is 72. At 19, four buy and revenue is 76. These calculations assume buyers purchase at equality. To verify the maximum, the other candidate prices are 34, 29, and 14, generating revenues 34, 58, and 70. No uniform fee covers 100 even though total willingness to pay is 120. Private revenue and social benefit are different objects.

<!--
|   |   |
| --- | --- |
| 3.i.admission | Subtitle: “Now suppose a private company can keep non-payers out, for a fee.” The line becomes a fee, back at 20. “Can one fee cover the annual cost of 100?” |
| 3.j.fee20 | At 20, Ginny and Neville go grey: 3 × 20 = 60. |
| 3.k.fee24 | At 24: 3 × 24 = 72. |
| 3.l.fee19 | At 19, Ginny returns: 4 × 19 = 76. “Even the best single fee raises only 76 < 100.” |
-->

The older outline mentions Lindahl and preference elicitation. A short bridge is enough here: payments of 30, 25, 20, 15, and 10 raise exactly 100 and leave every resident a net benefit of 4. Different payments can make all five favor funding the project. The hard part is learning their true willingness to pay when each has a reason to understate it. This is a simple feasible cost split, not a formal derivation of Lindahl equilibrium.

<!--
|   |   |
| --- | --- |
| 3.m.personalized-question | Subtitle: “What if each person paid a different amount?” “Could different payments make everyone willing to fund it?” |
| 3.n.personalized | Payments of 30, 25, 20, 15 and 10 marked on the bars; they sum to 100. “Each pays 4 less than their benefit: all five say yes.” |
| 3.n.elicitation | “The difficulty: learning how much each person really values it.” |
-->

## 4 | Majority voting and efficiency

Dobby’s equal-tax vote happens to choose the efficient outcome. It need not always work that way. The Dumbledore exercise provides the counterexample: Aurelius, Aberforth, and Ariana have benefits 75, 10, and 20. The project costs 90, financed by a tax of 30 each. Only Aurelius votes Yes, so the proposal fails. Yet benefits total 105, exceeding cost by 15.

<!--
|   |   |
| --- | --- |
| 3.exercise | The Exercise D3 Q1 card again, “continued”: parts c) to e) on the Dumbledore memorial, questions only. The animation does not solve it. |
-->

Majority voting counts the number of people who gain or lose under a proposal. It does not count how large those gains and losses are. Keep the decision to build a project distinct from the question of how its cost is shared. The Yule Ball homework supplies another application for practice.

## 5 | Brief limits of voting

The old schedule lists contributions and a referendum before a later class on three-ballot voting, Condorcet cycles, and Arrow. The dated entries are from 2023 with Fall 2024 episode annotations, so they do not establish the exact Fall 2024 class order. The October 30, 2024 PDF itself covers tuna, NPR, then Dobby; it does not contain a voting-cycle example.

Use a new, short illustration: voter 1 ranks A above B above C, voter 2 ranks B above C above A, and voter 3 ranks C above A above B. A beats B 2–1; B beats C 2–1; C beats A 2–1. Individual rankings are consistent, but the majority relation cycles. No alternative beats every other one. Voting on A against B, then the winner against C, selects C. Voting on B against C, then the winner against A, selects A, assuming sincere votes in each contest.

<!--
|   |   |
| --- | --- |
| 5.a.rankings | Title “Three Voters, Three Alternatives”. The three rankings. “Which alternative wins a majority against each of the others?” |
| 5.b.ab | “A beats B, 2 to 1” |
| 5.c.bc | “B beats C, 2 to 1” |
| 5.d.cycle | “C beats A, 2 to 1”. “A Condorcet cycle: no alternative beats every other one.” |
| 5.e.agenda | Two agendas, two winners: A against B first gives C; B against C first gives A. “The order of the votes can change the winner.” |
-->

Arrow’s theorem extends the warning beyond this particular majority rule. With three or more alternatives, no rule can accept every profile of individual rankings, respect unanimity, make each pairwise social comparison depend only on individual rankings of that pair, avoid a dictator, and always produce a complete, transitive social ranking. Here a dictator means one individual’s strict preferences always determine the social ranking, not a claim about a political regime. See [Geanakoplos’s statement and proofs](https://cowles.yale.edu/sites/default/files/2022-08/d1123-r4.pdf). Keep this to the statement and its meaning; there is no proof in the draft.

<!--
|   |   |
| --- | --- |
| 5.f.arrow | Title “Arrow’s Impossibility Theorem”. Four conditions, then “No rule does all four and always produces a consistent social ranking.” |
-->

Close by connecting the institutions to the incentives. Common resources can be overused; public goods can be underprovided. Voting can help fund a public good, but voting and efficient choice are not the same thing.

<!--
|   |   |
| --- | --- |
| 6.a.recap | Title “Public Goods And Voting”. Three gold terms with one line each: common resources are overused, public goods are underprovided, and voting can fund a public good but need not choose efficiently. |
-->
