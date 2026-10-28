---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

# Episode D3 | Public Goods And Voting

First runnable classroom draft, October 27, 2026. Run `maniml D3_Animation.py EpisodeD3` from this directory. The animation is click-paced; the time budget includes discussion, not just motion. All 40 teaching stops are explicit top-level `self.pause()` calls.

## Sources and scope

- `_archive/Class_On_Oct_30.pdf`, pages 1–2: NPR two-player matrix, three-player payoff formula, Dobby’s benefits, equal-tax vote, social efficiency, and admission fees. The PDF was created October 30, 2024. D2 already covers its tuna material.
- `D3_Notes.md`: NPR narration and incentives. This storyboard supersedes its earlier unbuilt choreography while preserving its model and payoffs.
- `Vignette/Vignette_D3.md`: adds the 25-galleon tax question and the uniform-fee question. The PDF names the residents Harry, Ron, Hermione, Ginny, and Neville; the vignette uses different names with the same five numbers. The animation follows the PDF names.
- `Exercise/Exercise_D3.md`: Dumbledore memorial counterexample, benefits 75, 10, 20; cost 90. Practice files remain unchanged.
- `_Schedule.md`: October 25, 2023 lists contributions, a voting example, and limits of voting; October 30, 2023 lists a three-ballot example, Condorcet cycles, and Arrow. Nearby Fall 2024 annotations renumber the episodes but do not establish an exact Fall 2024 teaching sequence. The October 30 PDF itself establishes NPR before Dobby.
- The old D3 code is mostly stubs, including an unfinished memorial with different numbers. It remains preserved. Its Lindahl topic is represented by a short personalized-tax illustration; this discrete example is not presented as a formal Lindahl equilibrium.
- The cyclic three-voter rankings are a new illustration of the schedule’s topic, not recovered historical ballots. Arrow’s scope was checked against John Geanakoplos, [Three Brief Proofs of Arrow’s Impossibility Theorem](https://cowles.yale.edu/sites/default/files/2022-08/d1123-r4.pdf). The result concerns complete, transitive social rankings on an unrestricted domain with at least three alternatives, unanimity, independence of irrelevant alternatives, and no dictator. No proof is attempted.

The Yule Ball homework is a parallel application left for practice. The broad Part D outline also names Tiebout and club goods as separate tutorials; those are not added to this half-hour lesson. All public-goods material in the October 30 PDF is included. Tuna is deliberately left in D2.

## Classroom budget

| Section | Minutes | Focus |
| --- | ---: | --- |
| NPR, two players | 9 | One contribution, matrix, best responses, free rider problem |
| NPR, three players | 2 | Same private incentive; larger shared benefit |
| Dobby | 11 | Visits, tax vote, social benefit, higher tax, admission, personalized payments |
| Majority versus efficiency | 3 | Dumbledore counterexample |
| Voting limits | 4 | One cycle, agenda, brief Arrow statement |
| Close | 1 | Connect back to D2 |

If discussion runs long, cover the three pairwise results briskly and spend only 30–45 seconds on Arrow. Retain NPR, the Dobby calculations, and the majority/efficiency distinction.

## Visual contract

Use D2′s 2:1 Graphite frame, 15 fps, serif model text, azure topic titles, grey context subtitles, pink Player 1 and teal Player 2, a grey divider, and sparse gold teaching lines. The body is centered between 2.5 and −2.8. A teaching line is 0.7443 scale, centered at the bottom with a 0.05 margin. Short questions and answers occupy different holds. Keep existing objects when their values or role change. No decorative radio or memorial art.

NPR opens with two rounded money boxes on the left and two strategy choices on the right. A contribution moves into the fund. The benefit labels are values of the same broadcast, not cash distributed out of the fund. Payoffs move into the right-hand diamond matrix. Best responses use player-colored boxes; Nash is red and the efficient outcome green, matching D2.

Dobby has five persistent teal benefit bars on the left and a calculation/result panel on the right. A tax/fee line crosses the same bars. Benefits stack vertically to compare social benefit with cost. Names sit below the axis; Yes/No labels or personalized payment amounts use a separate row below the names. These are five benefits from one memorial, not five units of the good. The closing comparison uses aligned term and explanation columns.

## 1 | The NPR Game — 9 minutes

| Hold | Action and teaching point |
| --- | --- |
| 1.a.rules | Start with NPR, each player holding 15, empty broadcast fund, and C: 15 / DC: 0. Subtitle defines public goods as non-rival and non-excludable. Everyone may listen. Choose simultaneously; maximize own payoff. |
| 1.b.benefits | Move Player 1′s 15 into the fund; their money kept becomes 0. Reveal benefit 10 for both players. Private cost 15, private return 10, combined benefit 20. Benefits are valuations, not money paid from the fund. |
| 1.c.question | Ask what each player receives before revealing the payoff calculation. |
| 1.d.payoffs | Right panel: payoff equals money kept plus benefit. Show 0 + 10 = 10 and 15 + 10 = 25 in player colors. |
| 1.e.matrix | Fade in the right-hand diamond and divider. Move those results into C,DC. Retain the money/fund model on the left. |
| 1.f.neither | Set both money-kept values to 15, fund to 0, benefits to 0. Copy the kept money into DC,DC: 15,15. |
| 1.g.both | Set money kept to 0, fund to 30, benefits to 20. Copy benefits into C,C: 20,20. |
| 1.h.symmetry | Set money kept to 15,0, fund to 15, and benefits to 10 each. Copy the asymmetric result with player identities exchanged into DC,C: 25,10. |
| 1.i.response-c | Replace the fund model with its private/shared incentive comparison. Shade Player 2′s C column. Ask Player 1′s best response. |
| 1.j.answer-c | Box Player 1′s 25. DC beats C because 25 > 20. |
| 1.k.response-dc | Move the same shade to Player 2′s DC column. Ask again. |
| 1.l.answer-dc | Box Player 1′s 15. DC beats C because 15 > 10. |
| 1.m.nash | Add Player 2′s response boxes by symmetry. Remove shading and outline DC,DC red. DC strictly dominates for both; neither gains from a unilateral change. |
| 1.n.free-rider | Outline C,C green. Define the free rider problem: people can benefit without contributing, so individual incentives can leave a non-rival, non-excludable good underprovided. Each gets 20 rather than 15 at C,C; combined payoff is 40 rather than 30. At DC,DC there is no broadcast to enjoy; it is the incentive to free ride that prevents funding. |

The payoff matrix is exactly the source matrix, with Player 1 first:

| Player 1 / Player 2 | C | DC |
| --- | --- | --- |
| C | 20,20 | 10,25 |
| DC | 25,10 | 15,15 |

## 2 | Three Contributors — 2 minutes

| Hold | Action and teaching point |
| --- | --- |
| 2.a.one | Clear the two-player matrix. Show the source formula and three aligned player columns. C,DC,DC gives 10,25,25. Own return remains 10 for a contribution of 15; aggregate benefit is now 30. |
| 2.b.none | Same columns become DC,DC,DC: 15 each, total 45. Each player’s marginal private loss from contributing remains 5 regardless of others. |
| 2.c.all | Same columns become C,C,C: 30 each, total 90. Funding institutions may improve on voluntary contributions. |

$$
u_i=15-c_i+\frac{2}{3}(c_1+c_2+c_3),\qquad c_i\in\{0,15\}.
$$

## 3 | A Memorial To Dobby — 11 minutes

| Hold | Action and teaching point |
| --- | --- |
| 3.a.visits | Five bars: Harry 34, Ron 29, Hermione 24, Ginny 19, Neville 14. Annual cost 100. Ask who visits if the memorial is freely available. |
| 3.b.all-five | All five have positive benefits, so all visit. Valuations need not be equal. |
| 3.c.vote | Add a horizontal tax line at 20. Ask for the majority result before revealing votes. Assume votes follow each person’s financial interest. |
| 3.d.passes | Yes, Yes, Yes, No, No under the five names. Show 3 Yes, 2 No and 5 × 20 = 100. The equal tax funds the project; two residents lose relative to no project. |
| 3.e.efficiency | Remove votes and tax marks, preserving the benefit bars. Ask whether the project is efficient. |
| 3.f.efficient | Copy the five bar heights into one stacked social-benefit bar on the right. Reveal 120, then a cost line at 100. MSB > MSC, net gain 20. This binary project test adds willingness to pay over people. |
| 3.g.tax25 | Remove the social aggregate and add the higher tax line at 25. Ask how the vote changes. |
| 3.h.fails | Yes, Yes, No, No, No. It fails. Revenue would be 125 if passed, while the resource cost remains 100. Do not treat this higher-tax proposal as the budget-balanced 20-each proposal. |
| 3.i.admission | Explicitly change the assumption: the operator can now restrict access, with one annual fee. At a fee of 20, ask whether revenue covers 100. The model assumes a person buys at equality. |
| 3.j.fee20 | Dim the two non-buyers’ bars. Three buyers pay 20: revenue 60. |
| 3.k.fee24 | Move the fee line to 24. Still three buyers: revenue 72. Store the earlier result below in grey. |
| 3.l.fee19 | Move the line to 19 and restore the fourth buyer’s bar. Four buyers: revenue 76. Even the best single fee cannot cover 100. The only other candidate maxima are 1 × 34 = 34, 2 × 29 = 58, and 5 × 14 = 70; keep this exhaustive check in narration, not extra animated permutations. |
| 3.m.personalized-question | Restore all bars and clear the fee calculations. Ask if different payments could make everyone willing to fund the good. |
| 3.n.personalized | Add red payment marks at 30,25,20,15,10 and amounts below names. Sum is 100; each person’s benefit exceeds their tax by 4. This is the intuition behind personalized benefit taxation. Ask how one learns true valuations when people have incentives to understate them. |

The personalized allocation is a new, deliberately simple illustration motivated by the old Lindahl topic. It is one feasible cost-sharing arrangement for a binary project, not a derivation of continuous Lindahl prices or a claim that voluntary honest reports implement it. A full Lindahl model is outside this half-hour draft.

## 4 | Majority and efficiency — 3 minutes

| Hold | Action and teaching point |
| --- | --- |
| 4.a.counterexample | Dumbledore exercise: three new benefit bars 75,10,20, equal tax 30, cost 90. Ask separately whether the project passes and whether it is efficient. |
| 4.b.rejected | One Yes, two No; rejected. Benefits sum to 105 > 90. Majority counts people, not the magnitude of gains and losses. Contrast with Dobby, where the equal-cost vote happened to select the efficient outcome. |

Leave the remainder of the Dumbledore exercise and the Yule Ball application for student practice rather than turning them into additional lecture sequences.

## 5 | Brief limits of voting — 4 minutes

| Hold | Action and teaching point |
| --- | --- |
| 5.a.rankings | Three consistent rankings, least to most preferred: C ≺ B ≺ A; A ≺ C ≺ B; B ≺ A ≺ C. Ask for pairwise majorities. |
| 5.b.ab | A beats B, 2 to 1 (voters 1 and 3). |
| 5.c.bc | B beats C, 2 to 1 (voters 1 and 2). |
| 5.d.cycle | C beats A, 2 to 1 (voters 2 and 3). Define the Condorcet cycle. There is no alternative that beats every other alternative by majority. |
| 5.e.agenda | A vs. B, then C produces C. Orally contrast B vs. C, then A, which produces A. Agenda order can change the winner under sincere sequential pairwise voting. |
| 5.f.arrow | One brief slide names unrestricted individual rankings, unanimity, pairwise independence, and no dictator. No rule satisfies all four while always producing a complete, transitive social ranking with three or more alternatives. Explain the independence condition in plain language; no proof and no claim that democratic decisions are impossible. |

## 6 | Close — 1 minute

`6.a.recap`: Common resources are rival: incentives can lead to taking too much. Public goods are non-rival: incentives can lead to contributing too little. Both are non-excludable. Voting can help fund a public good, but its outcome need not be efficient. Ask students to distinguish the incentive problem from the choice of institution.
