---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

# Episode D3 | Public Goods And Voting

Classroom draft, revised October 28, 2026 (first runnable draft October 27). Run `maniml D3_Animation.py EpisodeD3` from this directory. The animation is click-paced; the time budget includes discussion, not just motion. All 52 teaching stops are explicit top-level `self.pause()` calls, listed below under their ids. Layout and rhythm mirror D2: the arithmetic on the left, a graph on the right that keeps every outcome, a thin divider, then the graph shrinks left while the matrix fades in right and the numbers move into their cells, and separate question and answer holds.

## Sources and scope

- `_archive/Class_On_Oct_30.pdf`, pages 1–2: NPR two-player matrix, three-player payoff formula, Dobby’s benefits, the equal-tax vote with its checks and crosses, social efficiency, and admission fees. The PDF was created October 30, 2024. D2 already covers its tuna material.
- `D3_Notes.md`: NPR narration and incentives. Its embedded 1.a–1.j storyboard comments (the taxonomy move, “Do I contribute, or keep my money?”, the contribution beat, “Payoff = money kept + benefit from the broadcast.”, and the two-cell taxonomy contrast) are what section 1 builds.
- `Vignette/Vignette_D3.md`: adds the 25-galleon tax question and the uniform-fee question. The PDF names the residents Harry, Ron, Hermione, Ginny, and Neville; the vignette uses different names with the same five numbers. The animation follows the PDF names.
- `Exercise/Exercise_D3.md`: the Dumbledore memorial, benefits 75, 10, 20; cost 90; proposed tax 30. Its setup with parts a) and b) is the warmup at the top of class, and parts c)–e) return on the exercise card after Dobby; the animation does not solve it. Practice files remain unchanged.
- `_Schedule.md`: October 25, 2023 lists contributions, a voting example, and limits of voting; October 30, 2023 lists a three-ballot example, Condorcet cycles, and Arrow. Nearby Fall 2024 annotations renumber the episodes but do not establish an exact Fall 2024 teaching sequence. The October 30 PDF itself establishes NPR before Dobby.
- The old D3 code is mostly stubs, including an unfinished memorial with different numbers. It remains preserved. Its Lindahl topic is represented by a short personalized-payment illustration; this discrete example is not presented as a formal Lindahl equilibrium.
- The cyclic three-voter rankings are a new illustration of the schedule’s topic, not recovered historical ballots. Arrow’s scope was checked against John Geanakoplos, [Three Brief Proofs of Arrow’s Impossibility Theorem](https://cowles.yale.edu/sites/default/files/2022-08/d1123-r4.pdf). The result concerns complete, transitive social rankings on an unrestricted domain with at least three alternatives, unanimity, independence of irrelevant alternatives, and no dictator. No proof is attempted.

The Yule Ball homework is a parallel application left for practice. The broad Part D outline also names Tiebout and club goods as separate tutorials; those are not added to this half-hour lesson. All public-goods material in the October 30 PDF is included. Tuna is deliberately left in D2.

## Classroom budget

| Section | Minutes | Focus |
| --- | ---: | --- |
| Opening | 6 | Bumper; Exercise D3 Q1’s setup with parts a) and b), in small groups, then discussed together |
| NPR, two players | 9 | Taxonomy, one contribution, matrix, best responses, free rider problem, taxonomy contrast |
| NPR, three players | 2 | Same private incentive; larger shared benefit |
| Dobby | 11 | Visits, tax vote, social benefit, higher tax, admission, personalized payments |
| Exercise D3 card | 2 | Dumbledore memorial, questions only |
| Voting limits | 4 | One cycle, agenda order, brief Arrow statement |
| Close | 1 | Connect back to D2 |

If discussion runs long, cover the three pairwise results briskly and spend only 30–45 seconds on Arrow. Retain NPR, the Dobby calculations, and the 25-tax vote at 3.h, which is the lecture’s own case of a majority rejecting an efficient project.

## Visual contract

Use D2′s 2:1 Graphite frame, 15 fps, serif model text, azure topic titles, grey context subtitles, pink Player 1, teal Player 2, purple Player 3, a grey divider, and sparse gold teaching lines. The body is centered between 2.5 and −2.8. A teaching line is 0.7443 scale, centered at the bottom with a 0.05 margin. Short questions and answers occupy different holds. Keep existing objects when their values or role change. No decorative radio or memorial art.

NPR follows D2’s turn from a model to a graph to a matrix. The board’s payoff rule, Payoff_i = (15 − c_i) + (c_1 + c_2) · 2/3 with its two underbraces “the money I keep” and “funding NPR”, sits at the top of the left panel; under it, one worked line per player in that player’s color gives the current profile’s arithmetic, with the result as its own glyph. The right panel is a graph of Player 1’s payoff against Player 2’s contribution, with only 0 and 15 marked under the axis and payoffs read beside the points. Each profile is run on the worked lines and then Player 1’s result flies to its point as a pink dot, with the strategy pair beside it in grey and the pair of payoffs as a row (Player 1 pink, Player 2 teal), left of the point at 0 and right of it at 15. The two contributing points complete the C line and the two non-contributing points the DC line, parallel and 5 apart, so the dominant strategy is visible before the matrix. Then the rule panel fades, the graph shrinks into the left panel, the matrix fades in on the right, and the number pairs move from the points into their cells while the pair labels stay on the graph, exactly as D2 moved its totals. Best responses shade Player 2’s column on the matrix and the same contribution on the graph as a vertical band. There is no fund-and-boxes model: the rule, its worked lines, and the graph carry the game from the start.

Dobby has five persistent teal benefit bars on the left (values above, names below, no tick numerals) and a results panel on the right of the divider. The tax, and later the fee, is one red dashed line on a tracker: it rolls between 20, 25, 20, 24, and 19 rather than being redrawn, with a red readout left of the vertical axis like a price and a small “tax” or “fee” word at its right end. Votes are green checks and red crosses in a row below the names, as on the board; personalized payments use the same row. Efficiency stacks copies of the five bars vertically into one MSB bar on the right against an orange dashed MSC line; these are five benefits from one memorial, not five units of the good. Non-buyers turn grey rather than disappearing, and earlier revenue results are stored below in grey. The exercise card dims the stage to 5% behind a rounded panel, as in D1. The closing comparison uses aligned term and explanation columns.

## 0 | Opening — 6 minutes

| Hold | Action and teaching point |
| --- | --- |
| 0.a | The bumper, as D1 opens: the raster wordmark fades in and flickers, then “Part D \| Public Goods” joins beneath it, Part D in azure. |
| 0.b | Everything clears. Title “Warmup”, subtitle “Exercise D3, Q1, in groups, five minutes.” Below it, an exercise card in D1’s style: gold heading “Exercise D3 \| Q1: The Dumbledore Memorial”, the setup in three lines, “Three Dumbledores are considering a memorial to their brother Albus, just outside their town. Anyone can enjoy it, whether or not they helped pay. It costs 90 coins a year.”, then the handout’s first two parts, a) “If it were built, how many of the three would visit?” and b) “An endowment covers the first year. After that, each must put in 30 coins a year. Would it get funded?” At right on the card, the handout’s table as three teal bars, Aurelius 75, Aberforth 10, Ariana 20, under “Annual benefit”, with “Annual cost: 90” beneath. No teaching line. Answers: a) all three, since no one can be kept out; b) no: only Aurelius, with a benefit of 75, would pay 30, while Aberforth (10) and Ariana (20) would not, and each can enjoy it whether or not they pay. In discussion, ask whether it is worth it to the three together: yes, 105 against 90. That is the free-rider problem found in groups before the lecture names it. Groups work for about five minutes, then the class compares answers. Parts c)–e) return, with the same letters as the handout, on the card at 3.exercise. |

## 1 | The NPR Game — 9 minutes

| Hold | Action and teaching point |
| --- | --- |
| 1.a.commons | Title “Common Resources”, subtitle “Goods that are rival and non-excludable.” D1′s taxonomy with the red box on Common Resources: last time’s topic. No teaching line. |
| 1.a | The box slides to Public Goods while the title becomes “Public Goods” and the subtitle “Goods that are non-rival and non-excludable.” No teaching line. |
| 1.b.rule | Title becomes “The NPR Game”; subtitle “Everyone can listen, whether or not they contribute.” The rule alone, large and centered: Payoff_i = (15 − c_i) + (c_1 + c_2) · 2/3. No teaching line. |
| 1.b.kept | The first underbrace fades in under (15 − c_i): “the money I keep”. |
| 1.b.fund | The second underbrace fades in under (c_1 + c_2) · 2/3: “funding NPR”. |
| 1.b | Everything moves into place in one play: the rule shrinks to the top of the left panel, “Two Strategies: Contribute (C): 15 / Do not contribute (DC): 0” fades in beneath it, and on the right the divider and the empty graph, “Player 1′s payoff” against “Player 2′s contribution” with 0 and 15 marked. Teaching line: “Do I contribute, or keep my money?” |
| 1.d.payoffs | The strategies fade and the first profile’s worked lines appear under the rule: “Player 1: (15 − 15) + (15 + 0) · 2/3 = 10” and “Player 2: (15 − 0) + (15 + 0) · 2/3 = 25”. Teaching line: “A contribution costs me 15 and benefits each of us by 10.” |
| 1.e.graph | The two results fly from the worked lines to the first point: pink dot at (0, 10), “C,DC” and “10 \| 25” to its left. Teaching line: “Each run is a point: Player 1′s payoff against Player 2′s contribution.” |
| 1.f.payoffs | The worked lines become DC,DC: “(15 − 0) + (0 + 0) · 2/3 = 15” for both. Teaching line: “Nobody contributes: each keeps 15.” |
| 1.f.graph | Dot at (0, 15), “DC,DC 15 \| 15” to its left. |
| 1.g.payoffs | The worked lines become C,C: “(15 − 15) + (15 + 15) · 2/3 = 20” for both. Teaching line: “Both contribute: each receives 20.” |
| 1.g.graph | Dot at (15, 20), “C,C 20 \| 20” to its right; then the C line draws from (0, 10) to (15, 20), labelled “C” above its middle. |
| 1.h.payoffs | The worked lines become DC,C: “Player 1: (15 − 0) + (0 + 15) · 2/3 = 25”, “Player 2: (15 − 15) + (0 + 15) · 2/3 = 10”. Teaching line: “Switch the contributor; switch the payoffs.” |
| 1.h.graph | Dot at (15, 25), “DC,C 25 \| 10” to its right; the DC line draws from (0, 15) to (15, 25), labelled “DC”, parallel to C and 5 above it. Teaching line: “Whatever Player 2 does, not contributing pays 5 more.” |
| 1.i.matrix | The rule and worked lines fade. One play: the graph shrinks into the left panel, the diamond matrix with C/DC labels and “Player 1”/“Player 2” fades in on the right, and the four number pairs move from the points into their cells. The pair labels stay on the graph. Teaching line: “Player 1′s payoff first; Player 2′s payoff second.” |
| 1.j.response-c | Teal shade and underline on Player 2′s C column, and a teal band on the graph at contribution 15. Teaching line: “If Player 2 contributes, what is Player 1′s best response?” |
| 1.k.answer-c | Pink box on Player 1′s 25. Teaching line: “Do not contribute: 25 > 20.” |
| 1.l.response-dc | Shade and band move to the DC column and contribution 0. Teaching line: “If Player 2 does not contribute, what is Player 1′s best response?” |
| 1.m.answer-dc | Pink box on Player 1′s 15. Teaching line: “Do not contribute: 15 > 10.” |
| 1.n.symmetry | Shade and band out; teal boxes on Player 2′s 25 and 15. Teaching line: “The same comparisons hold for Player 2. Neither contributes.” |
| 1.n.nash | Red square on DC,DC. Teaching line: “Neither player gains by changing alone.” |
| 1.o.free-rider | Green square on C,C, with “20 > 15 for each player.” above the matrix. Bottom: gold “Free rider problem” over two white lines, “Individual incentives lead to the underprovision of a public good:” and “each contributor pays the full cost but receives only part of the total benefit.” |
| 1.p.contrast | Everything clears. Title “Common Resources And Public Goods”, subtitle “Both are non-excludable. One is rival; the other is not.” The taxonomy returns with both bottom cells boxed red, “Take too much” under Common Resources and “Contribute too little” under Public Goods. Teaching line: “The commons is overused; the public good is underprovided.” |

The payoff matrix is exactly the source matrix, with Player 1 first:

| Player 1 / Player 2 | C | DC |
| --- | --- | --- |
| C | 20,20 | 10,25 |
| DC | 25,10 | 15,15 |

## 2 | Three Contributors — 2 minutes

Title “Three Contributors”; subtitle “The same rule, with one more contribution in the fund.” The same layout as the NPR runs: the rule with three contributions and its braces at the top of the left panel, three worked lines beneath (pink, teal, purple), and on the right a graph of Player 1’s payoff against the others’ contributions, 0, 15 and 30 marked under the axis, with the C and DC lines already drawn out to 30. Only Player 1’s payoff is plotted; the others’ payoffs are on the worked lines.

| Hold | Action and teaching point |
| --- | --- |
| 2.a.one | Worked lines “Player 1: (15 − 15) + (15 + 0 + 0) · 2/3 = 10”, “Player 2: (15 − 0) + (15 + 0 + 0) · 2/3 = 25”, “Player 3: … = 25”. Player 1′s 10 flies to a dot at (0, 10), “C,DC,DC 10” to its left. Teaching line: “One contributor: 10 for them, 25 for each of the others.” |
| 2.b.none | Worked lines become “(15 − 0) + (0 + 0 + 0) · 2/3 = 15” for all three; dot at (0, 15), “DC,DC,DC 15”. Teaching line: “Nobody contributes: 15 each.” |
| 2.c.all | Worked lines become “(15 − 15) + (15 + 15 + 15) · 2/3 = 30”; dot at (30, 30) at the far end of the C line, “C,C,C 30” to its right. Teaching line: “Everybody contributes: 30 each. Could a group arrange that?” |

$$
\text{Payoff}_i=(15-c_i)+(c_1+c_2+c_3)\cdot\tfrac{2}{3},\qquad c_i\in\{0,15\}.
$$

## 3 | A Memorial To Dobby — 11 minutes

Title “A Memorial To Dobby”; subtitle “Annual benefits and costs, in galleons. Everyone can enjoy the memorial.”

| Hold | Action and teaching point |
| --- | --- |
| 3.a.visits | Left: “Marginal benefit” heading over five teal bars, Harry 34, Ron 29, Hermione 24, Ginny 19, Neville 14, values above and names below. Divider. Right: “Annual cost: 100” in orange. Teaching line: “If it is built, how many people will visit?” |
| 3.b.all-five | Right: “Visitors: 5”. Teaching line: “All five: each gets a benefit, and no one can be kept out.” |
| 3.c.vote | Visitors out. A red dashed line at 20 crosses the bars, with a red “20” left of the axis and a small “tax” at its right end. Teaching line: “Would a tax of 20 each pass a majority vote?” Assume votes follow each person’s financial interest. |
| 3.d.passes | Checks appear under Harry, Ron, and Hermione and crosses under Ginny and Neville, in sequence. Right: “3 Yes, 2 No”, then “5 × 20 = 100” in green. Teaching line: “It passes, and the tax pays for the memorial.” |
| 3.d.outvoted | Teaching line: “Ginny and Neville pay 20 for benefits of 19 and 14.” |
| 3.e.efficiency | Votes, result, and total out; the bars and the tax line stay. Teaching line: “Is building the memorial socially efficient?” |
| 3.f.efficient | Copies of the five bars stack vertically into one bar on the right, labeled “MSB” below and “120” above, then an orange dashed line at 100 with “MSC 100”, the 100 copied from the cost label. Teaching line: “MSB = 120 > MSC = 100: building it is efficient.” |
| 3.g.tax25 | Stack and cost line out. The tax line rolls up to 25 with its readout. Teaching line: “What if the proposed tax were 25 each?” |
| 3.h.fails | Checks under Harry and Ron, crosses under the other three. Right: “2 Yes, 3 No”. Teaching line: “It fails, even though the memorial is still efficient.” Do not treat this proposal as the budget-balanced 20-each proposal. |
| 3.i.admission | Votes out. Subtitle becomes “Now suppose a private company can keep non-payers out, for a fee.”; the line’s word becomes “fee” and the line rolls back to 20; right heading “Admission revenue”. Teaching line: “Can one fee cover the annual cost of 100?” The model assumes a person buys at equality. |
| 3.j.fee20 | Ginny’s and Neville’s bars and values go grey. Right: “3 × 20 = 60”. |
| 3.k.fee24 | The line rolls to 24; the 60 result shrinks to grey below; “3 × 24 = 72”. |
| 3.l.fee19 | The line rolls to 19 and Ginny’s bar returns to teal; 72 shrinks to grey with 60 below it; “4 × 19 = 76”. Teaching line: “Even the best single fee raises only 76 < 100.” The other candidate maxima, 1 × 34 = 34, 2 × 29 = 58, and 5 × 14 = 70, stay in narration. |
| 3.m.personalized-question | Line, readout, “fee”, results, and heading out; Neville’s bar returns to teal. Subtitle “What if each person paid a different amount?” Teaching line: “Could different payments make everyone willing to fund it?” |
| 3.n.personalized | Red marks across the bars at 30, 25, 20, 15, 10 with red amounts below the names, in sequence. Right: “30 + 25 + 20 + 15 + 10 = 100” in green. Teaching line: “Each pays 4 less than their benefit: all five say yes.” |
| 3.n.elicitation | Teaching line: “The difficulty: learning how much each person really values it.” |
| 3.exercise | The stage dims to 5% behind a rounded card. Gold heading “Exercise D3 \| Q1, continued: The Dumbledore Memorial”, grey note “The memorial from the warmup, now with the tools.”, and parts c)–e) at left: “Does a referendum for a tax of 30 each pass?”, “What is the marginal social benefit?”, “If it passed, would the outcome be efficient?” At right, the same three teal bars, Aurelius 75, Aberforth 10, Ariana 20, over “Annual cost: 90”. Nothing is solved on screen; parts a) and b) were the warmup. |

The personalized allocation is a new, deliberately simple illustration motivated by the old Lindahl topic. It is one feasible cost-sharing arrangement for a binary project, not a derivation of continuous Lindahl prices or a claim that voluntary honest reports implement it. A full Lindahl model is outside this half-hour draft.

The Dumbledore counterexample is the in-class exercise, so the animation poses it and stops; the earlier draft’s section 4, which solved it on screen, is gone. The lecture’s own majority-versus-efficiency case is the 25-tax vote at 3.h, where a majority rejects a project with MSB 120 > MSC 100. The voting holds keep their 5.* ids.

## 5 | Brief limits of voting — 4 minutes

Title “Three Voters, Three Alternatives”; subtitle “Each voter ranks A, B, and C. Rankings read from least to most preferred.” Rankings on the left, results on the right of a divider.

| Hold | Action and teaching point |
| --- | --- |
| 5.a.rankings | Voter 1: C ≺ B ≺ A; Voter 2: A ≺ C ≺ B; Voter 3: B ≺ A ≺ C. Teaching line: “Which alternative wins a majority against each of the others?” |
| 5.b.ab | “A beats B, 2 to 1” (voters 1 and 3). |
| 5.c.bc | “B beats C, 2 to 1” (voters 1 and 2). |
| 5.d.cycle | “C beats A, 2 to 1” (voters 2 and 3). Teaching line: “A Condorcet cycle: no alternative beats every other one.” |
| 5.e.agenda | Two grey lines below the results: “A vs. B first, then the winner vs. C: C wins” and “B vs. C first, then the winner vs. A: A wins”. Teaching line: “The order of the votes can change the winner.” |
| 5.f.arrow | New slide. Title “Arrow’s Impossibility Theorem”; subtitle “With three or more alternatives, no voting rule can do all of the following.” Four lines: “Accept any individual rankings”, “Respect unanimous preferences”, “Compare two alternatives using only how people rank those two”, “Let no single voter always decide”. Then “No rule does all four and always produces a consistent social ranking.” Teaching line: “A limit on ranking rules, not a reason to abandon voting.” Explain the independence condition in plain language; no proof and no claim that democratic decisions are impossible. |

## 6 | Close — 1 minute

`6.a.recap`: Title “Public Goods And Voting”; subtitle “Both common resources and public goods are non-excludable.” Three gold terms with white descriptions in aligned columns: Common resources, “Rival: individual incentives lead to overuse.”; Public goods, “Non-rival: individual incentives lead to underprovision.”; Voting, “Can fund a public good, but a majority need not choose efficiently.” Ask students to distinguish the incentive problem from the choice of institution.
