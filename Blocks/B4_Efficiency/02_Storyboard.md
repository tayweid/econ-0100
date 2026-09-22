# Episode B4 | First Welfare Theorem | Storyboard

Draft for Taylor's review · 2026-09-22 · No animation implementation yet.

## Direction and sources

Taylor's current direction is to make the simulation carry the welfare argument.
CS and PS are familiar from B1/B2. Price-control arithmetic and graphs build on
B3. The central new work is showing why an allocation maximizes total gains,
then showing that the market selects that allocation.

Confirmed in the September 22 storyboard interview:

- The newly written source is [B3's conversation outline](../B3_Equilibrium/00_Outline.md).
- Begin with one quick exchange/switching reminder, then the full market.
- Let the social planner establish the best allocation before connecting it to
  competitive equilibrium.
- Edit only animation files and `02_Storyboard.md`; lecture prose stays with
  Taylor/Fable. This pass creates only this storyboard.

Read [B4's notes](01_Notes.md), especially Welfare Analysis, Efficiency, and Price
Controls, alongside that outline. The older [welfare storyboard](B4_Welfare_Storyboard.typ)
supplies the affordable-spinach motivation and blocked-bid example. The current
interview puts the planner argument before the policy applications. The B3
outline's ceiling-first class suggestion therefore does not fix this draft's
whole teaching order.

The staged buyer/seller replacements below are animator proposals for making
the notes' social-planner argument visible. Their mathematics is checked; their
wording and pacing remain reviewable. All quoted display text below is proposed
on-screen text, not new lecture prose. No note sentences have been rewritten.

## Shared stage and meaning

- Use the existing 2:1 graphite stage, 2160 × 1080, 15 fps, CMU serif teaching
  text, azure question titles, gold definition terms, and existing style tokens.
  Demand/CS is teal; supply/PS is orange; payment is green; total surplus is
  `TOTAL`; DWL is grey. The small exchange retains B3's orange cost and PS outline.
- Reserve one bottom band for the current question, definition, or two-option
  comparison. Remove its previous content before replacing it. Do not stack a
  definition, caption, and deliberation card there simultaneously.
- Keep the market at left and its graph at right during market-wide beats.
  Use the B3 sorted buyer/seller rows, with buyers above sellers. Keep each side
  in compact rows of at most 20; mark every person but label only selected people.
  Individual comparisons enlarge the relevant bars into a head-on inset while
  the unchanged crowd remains dimly visible. A full-width head-on row is reserved
  for the quantity sweep; it is not squeezed beside two small graphs.
- Read each compact row left to right, then continue on the next row. Preserve
  rank order across folds. Every row has the same local zero and dollar scale;
  repeat a local price segment at the appropriate height in each row, all driven
  by the same price. These are copies of one common price, not separate asks.
- The recap begins its full-market portion with the two stacked B3 graphs. At
  `2.a`, slide those same axes into a single overlaid graph while retaining the
  crowd. The overlaid graph remains the common reference for welfare.
- One check means willing at the displayed market price. One ground circle means
  actually trading. Keep marks distinguishable by shape; default to side-colored
  checks and green circles, as proposed in the B3 outline. A selected comparison
  uses a temporary outline/leader, not an extra trading circle.
- In the uncontrolled and policy cases, (Q_x=\min(Q_d,Q_s)), with highest-MB
  buyers and lowest-MC sellers trading. This is an explicit rationing assumption
  under controls. During planner experiments, chosen (Q) replaces this rule;
  hide market-willingness checks and Qd/Qs readouts so they do not masquerade as
  the planner's allocation rule. Circles still identify the selected trades.
- Distinguish actual allocations from proposals. Dashed trade connections and
  unfilled gain outlines are hypothetical; solid connections and filled gain
  regions belong to the current allocation. Reset each experiment rather than
  accumulating trades or surplus across examples.
- Bidding/undercutting sketches in the recap explain the pressure on the going
  price. A dashed individual offer does not instantly reprice every trade or
  count as an extra sale. The full-crowd price move follows the sketch.
- Use one source for the market price, willingness tests, counts, and graph
  guides. Count predicates include indifference. During motion, integer counts
  follow the actual bar thresholds; never interpolate an independent count.
  The exact crowd's read guides land on staircase boundaries. Smooth lines are
  faint fitted references until the explicit approximation at `6.a`.
- New files eventually use flat, sequential `construct()` choreography, visible
  constants, simple loops for repeated objects, and literal `self.pause('id')`
  boundaries. No per-beat helper framework. Each independent scene reconstructs
  its opening state without replaying earlier teaching stops.

## Numerical reference — checked, not an on-screen table

Keep B3's market: (P_D=12-Q_d/5), (P_S=2+Q_s/20), with price in dollars per
pound and Q in thousands of pounds. Buyers have (MB_n=12-n/5), n=1…59;
sellers have (MC_n=2+n/20), n=1…100. Each crowd token represents one
1,000-lb lot. The opening Gary/Molly reminder is one pound; announce the unit
change when the full crowd enters. Never label a lot's $2-per-pound gain as $2
of total surplus: it is $2,000.

Use Q axes 0–100 and P axes 0–13 throughout. Demand ends at (60,0); supply
ends at (100,7). The $2 supply intercept is not an extra crowd seller. Gary is
buyer 30 (MB $6), Amanda-Grace buyer 25 (MB $7), Andrew seller 40 (MC $4).

| Price | Qd | Qs | Qx | Unserved willing side |
|---|---:|---:|---:|---|
| $3 | 45 | 20 | 20 | 25 buyers |
| $4 | 40 | 40 | 40 | None |
| $6 | 30 | 80 | 30 | 50 sellers |

For the exact crowd, ranked pair n adds (1,000(10-n/4)) dollars of surplus.
Pairs 1–39 add positive gains, pair 40 adds zero, and pair 41 adds −$250.
Thus **39 and 40 trades tie for maximum discrete surplus**. The inclusive
willingness convention selects 40. Do not claim every change from 40 lowers
surplus, or that counterpart pairings are uniquely efficient.

The smooth model has (TS(Q)=10Q-Q^2/8), in thousands of dollars, and its
unique maximizing quantity is Q=40. Exact discrete totals are

\[TS_{\mathrm{crowd}}(Q)=10Q-Q(Q+1)/8.\]

| Case | Exact crowd CS / PS / TS / loss ($000) | Smooth model CS / PS / TS / DWL ($000) |
|---|---|---|
| P=$4, Q=40 | 156 / 39 / 195 / 0 | 160 / 40 / 200 / 0 |
| P=$3, Q=20 | 138 / 9.5 / 147.5 / 47.5 | 140 / 10 / 150 / 50 |
| P=$6, Q=30 | 87 / 96.75 / 183.75 / 11.25 | 90 / 97.5 / 187.5 / 12.5 |

Use each model's own optimum as its loss benchmark. `6.a` explicitly introduces
the smooth approximation; a copy of the bars may refine into areas, but the
crowd's original MB/MC values never change. Before that transition, show exact
per-lot differences without a running aggregate numerical tally.

## 0.a · Open B4

1. Use the shared bumper, “Part B | Episode 4,” and the notes' thesis:
   “Under some conditions, nothing can do better than markets.”
2. Hold, then clear the bumper for the exchange reminder.

## 1.a · Recall one exchange

1. Restore B3's approved Gary/Molly head-on close-up: MB $6, MC $2, price $4,
   “One pound.” Title: “Why trade?”
2. Reveal the already familiar CS $2 and PS $2 together. Retain the green
   expenditure/revenue boundary and orange cost. Do not replay the five-step
   accounting construction or introduce either surplus definition again.
3. Hold the two gains and their shared price line.

## 1.b · Recall why a deal changes

1. Remove the accounting labels; retain Gary's solid $4 deal. Admit Amanda-Grace
   with MB $7 using B3's existing three-person head-on layout.
2. Show her dashed $4.25 proposal and the question “Would Molly switch?” Hold
   before acceptance.
3. On advance, move Molly's MC comparison to Amanda-Grace's side, solidify $4.25,
   and release Gary's old connection. Carry forward B3's accepted-line grammar.
   Do not run the remaining bidding war or make an equilibrium claim here.

## 1.c · One price, many decisions

1. Clear the small-cast scene in one transition and reveal the entire fixed
   crowd, already sorted. Do not animate entrants one at a time.
2. Caption “One person = 1,000 pounds”; axis caption “Dollars per pound.” Title:
   “Who would trade at this price?”
3. Restore the stacked demand/supply graphs and the common price $4. Show checks
   on ranks 1–40 on each side, circles on those same people, and Qd=Qs=Qx=40.
4. Hold. This is the full market's known benchmark, not the conclusion of the
   preceding one-seller negotiation. Keep its identity through the entire lesson.

## 1.d · Predict the low-price result

1. Hide numerical counts, willingness checks, trading circles, and quantity
   read guides before moving the common price to $3. Keep them hidden during
   the prediction hold; retain bars and the price on both graphs.
2. Ask “At $3, how much would each side trade?” Hold before revealing the counts.

## 1.e · Count the shortage and the actual trades

1. Reveal 45 buyer checks and 20 seller checks. Circle the first 20 on each side.
   Print Qd=45, Qs=20, Qx=20, with a quantity gap from 20 to 45.
2. Show “Shortage: 25,000 pounds” beside that gap; point once to the 25 willing
   buyers without circles. Amanda-Grace and Gary are among them.
3. Hold. Keep the distinction between willingness and actual exchange visible.

## 1.f · Recall the incentive to raise price

1. Highlight Amanda-Grace. Replace the bottom text with two concise options:
   “Wait: no trade” / “Offer $3.25: gain $3.75/lb.” Draw the proposed bid dashed.
   Show that the served seller receives more if the bid is accepted.
2. Ask “Which way does price move?” Hold with the answer still withheld.
3. On advance, clear the individual proposal and show “Shortage → price rises.”
   Raise the common price to $4 in one continuous play. Keep counts and marks
   synchronized; do not narrate every threshold crossing or stop at each tick.
4. Keep 40/40/40 visible as the next question enters; no navigation-only stop.

## 1.g · Predict the high-price result

1. Hide numerical counts, willingness checks, trading circles, and quantity
   read guides before moving the common price to $6. Ask “At $6, who is left
   out?” Hold with those answers still hidden.

## 1.h · Count the excess and recall undercutting

1. Reveal Qd=30, Qs=80, Qx=30: 30 buyer checks, 80 seller checks, 30 circles on
   each side. Mark the quantity gap 30–80; show “Excess: 50,000 pounds.”
2. Highlight Andrew among the unserved sellers and Gary among the served buyers.
   Replace the bottom content with “Keep $6: no buyer” / “Ask $5.75: gain $1.75/lb.”
   Gary would also gain by paying less. Ask “Which way does price move?” Hold.
3. On advance, clear the proposed deal and show “Excess → price falls.” Move the
   common price to $4 in one play, retaining the counts throughout.

## 1.i · State the two parts of equilibrium together

1. Park on 40 checks and circles on each side and Qd=Qs=Qx=40. Keep unwilling
   people visible and dim, with their bars on the wrong side of the price.
2. Replace the adjustment caption with the B3 definition:
   “Equilibrium: the price and quantity at which quantity supplied equals
   quantity demanded — where no one wants to change.” Reflow at the usual size.
3. Hold. Do not solve the equilibrium algebra again.

## 1.j · Exercise B3 Q2

1. Dim the market. Show the existing Exercise B3 Q2 card with its original
   numbering and pasty equations: (P=12-Q_d/2), (P=2+Q_s/2).
2. State the units, galleons and pasties, and the price of 5 galleons. Ask parts
   (a) Qd, (b) Qs, (c) shortage/excess and its size, (d) direction of price change,
   using the exercise sheet's exact wording. Show no answers on this card.
3. Hold for the exercise. On advance, remove the card and restore the same
   spinach market at $4. The exercise is a separate problem, not a new dataset
   for the subsequent simulation.

## 2.a · Ask whether the market's answer is good

1. Title: “Could we do better?” Keep the 40 trades in the crowd.
2. Slide the two stacked graphs onto common axes. Retain their objects, units,
   colors, selected quantity, and $4 price. Do not replace the market.
3. Briefly light the familiar CS and PS portions of traded bars together. Hold
   the notes' welfare question without re-teaching how those regions are defined.

## 2.b · Separate the size of the gain from its division

1. Enlarge the two bars for ranked pair 20: buyer MB $8, seller MC $3. Keep the
   rest of the current allocation fixed and dim. Caption “One 1,000-lb lot.”
2. Show (CS=MB-P), (PS=P-MC), and then ((MB-P)+(P-MC)=MB-MC), with matching
   colored terms. Cancel only the payment terms; show the total gap of $5/lb.
3. Move this pair's payment from $4 to $5 while both people and the traded lot
   remain fixed. CS shrinks and PS grows by the same amount. Keep the outer
   MB–MC gain bracket stationary and label the total gain $5,000.
4. Hold “The price divides the gain.” This is a fixed-trade accounting
   comparison, not a new common market price or a renegotiation prediction.
   Restore the $4 payment and return the bars to their places on advance.

## 2.c · Give the planner the two choices

1. Remove the market-price line, checks, Qd/Qs readouts, and all CS/PS division
   lines. Retain each person's MB/MC and the 40 trading circles.
2. Title: “Which trades should happen?” Show only two short prompts beside the
   model: “Who trades?” and “How many trades?”
3. Highlight the selected participants, then the Q marker. Hold. From here the
   planner chooses an allocation; no automatic price adjustment runs.

## 3.a · Hold quantity fixed and test the buyers

1. Set the planner's allocation to 20 trades. For this explicit counterfactual,
   select buyers 1–20 except buyer 10, with Gary (buyer 30) in that slot; select
   sellers 1–20. Mark “20 trades” and retain all unselected people.
2. Show Gary's MB $6 beside unserved buyer 10's MB $10. Keep their potential
   counterpart, seller 10 (MC $2.50), fixed. Use an empty outline for buyer 10's
   proposed connection; the other 19 trades stay unchanged.
3. Ask “Who should get this lot?” Hold before revealing the replacement.

## 3.b · Improve the allocation without adding a trade

1. Move that one trading circle and connection from Gary to buyer 10. Gary
   remains in the market, now unselected. Keep seller 10 and Q=20 unchanged.
2. Reveal “Same cost; $4,000 more benefit.” Extend the highlighted total-gain
   segment by exactly the MB difference. Do not count a twenty-first trade.
3. Mark the first 20 buyers as the selected set. Hold “Highest-value buyers.”

## 3.c · Hold quantity fixed and test the sellers

1. Retain the efficient first 20 buyers. For a separate, explicitly hypothetical
   allocation, replace selected seller 10 with Andrew (seller 40). Keep Q=20.
2. Fix buyer 10 (MB $10). Compare Andrew's MC $4 with unselected seller 10's
   MC $2.50. Ask “Who should produce this lot?” Hold before switching.

## 3.d · Keep the benefit and reduce the cost

1. Move the affected trading circle and connection from Andrew to seller 10.
   Keep the buyer and total number of trades fixed.
2. Reveal “Same benefit; $1,500 less cost.” Extend the total-gain segment by
   that amount. Restore the first 20 sellers as the selected set.
3. Hold “Lowest-cost sellers.” These substitutions establish the sorting rule;
   they are not a claim that the original market spontaneously chose badly.

## 3.e · Fix the best participants for each quantity

1. Show the two sorted selected prefixes with “Highest-value buyers” above and
   “Lowest-cost sellers” below. Fade out the individual arithmetic.
2. Keep one-to-one connections by rank for visual bookkeeping. Do not imply
   that this particular pairing is uniquely efficient: total benefit and cost
   depend on who participates, not which selected buyer meets which seller.
3. Hold “Now choose how many.” Keep Q=20 for the next question.

## 4.a · Consider the next trade

1. Move from the compact plaza to a full-width head-on comparison. Park the
   overlaid graph off screen, preserving its state. Unfold the participants into
   ranked buyer/seller bar pairs along a common quantity axis; use a shared
   dollar baseline so the gap between each MB and MC is directly comparable.
   Keep all labels except the selected pair's hidden. Do not change values or
   allocations as the geometry moves.
2. Keep the first 20 selected on both sides. Enlarge the next two bars, rank 21:
   MB $7.80 and MC $3.05. Leave their circles empty and connection dashed.
3. Show a potential gain outline between these heights. Ask “Should we add this
   trade?” Hold before adding it.

## 4.b · Add positive gains

1. Select the rank-21 pair; solidify its connection. Reveal its gain of $4,750
   and move Q from 20 to 21. The prior twenty trades stay selected.
2. Continue in one short sweep through Q=39. At each integer boundary, select
   the next pair and add only its gain strip. The strips get smaller.
3. Park with pair 39's MB $4.20 and MC $3.95 enlarged and its gain $250. Hold
   “Another trade helps while MB > MC.” No running dollar tally is needed.

## 4.c · Inspect the boundary

1. Show rank 40 beside rank 39: MB $4 and MC $4. Its potential gain has zero
   height. Ask “What does this trade add?” Hold before the answer.

## 4.d · Account for indifference

1. Reveal “$0.” Circle rank 40 on each side using the existing convention that
   indifferent people are willing to trade. Move Q from 39 to 40 without
   increasing the total-surplus region.
2. Hold “The last trade adds zero.” Keep a small caption “39 or 40: same total
   gain” for this exact finite market. This is the endpoint, not a numerical bug.

## 4.e · Test a trade beyond the boundary

1. Keep the 40 chosen trades intact. Enlarge rank 41: MB $3.80, MC $4.05.
   Its connection stays dashed and its people stay uncircled.
2. Show the buyer's acceptable price interval ending at $3.80 and the seller's
   starting at $4.05. Leave their non-overlap clearly visible.
3. Ask “Would this trade help?” Hold. On advance, reveal “−$250” and “MC > MB.”
   Do not paint negative private gains as realized CS/PS or execute a voluntary
   trade that neither common price can support.

## 4.f · Read the planner's complete rule

1. Return the enlarged pair to the full-width head-on comparison; the graph
   remains parked off screen. Begin with 40 chosen pairs; outline the
   positive gains through pair 39 and the zero-height boundary at pair 40.
2. Sweep a quantity marker back to 30. Remove circles and solid connections from
   pairs 31–40 as they leave the allocation, leaving the forgone positive gains
   from pairs 31–39 as empty outlines. Return to 40, restoring the circles,
   connections, and gain fills as each pair rejoins; pair 40 still adds no gain.
   Price is still absent: this is the notes' quantity-controlled planner.
3. Show “Take the gains; stop when additional cost exceeds benefit.” Hold on
   the maximum, with the previously demonstrated zero-gain boundary retained.

## 5.a · Return control to buyers and sellers

1. Fold the rows back into the compact plaza and restore the saved overlaid
   graph beside them. Preserve every participant's rank and value. Store the
   planner's selected prefixes as faint outlines. Remove the planner selection
   circles, quantity control, and hypothetical comparison marks.
2. Restore the market price of $4. Title: “Does the market choose these trades?”
   Hold before revealing willingness or the resulting allocation.

## 5.b · Let the common price select participants

1. Reveal checks on the 40 buyers with MB≥$4 and 40 sellers with MC≤$4. Circle
   those participants and print Qd=Qs=Qx=40. The actual selection coincides
   with the saved planner outlines.
2. Enlarge the boundary and first excluded bars briefly: buyer 40 is indifferent,
   buyer 41 will not pay $4; seller 40 is indifferent, seller 41 will not sell
   at $4. Keep their thresholds and quantities consistent.
3. Hold “The same people; the same gains.” Fade the comparison outlines on advance.

## 5.c · Close the argument on the simulation

1. Restore the full allocation. In succession, highlight the highest-value
   selected buyers, lowest-cost selected sellers, and boundary between beneficial
   and harmful additional trades. Use the existing outlines; add no new diagram.
2. Show “Total surplus = total benefit − total cost.” Then replace it with
   “Equilibrium maximizes total gains from trade.” Hold on the actual participants
   and their gain strips, not on an isolated theorem slide.
3. Preserve the qualification already demonstrated: every positive-gain addition
   in the ranked allocation occurs, the marginal trade adds zero, and exact
   partner identities need not be unique. Do not say the only efficient
   allocation is this exact matching.

## 5.d · Name the theorem and its conditions

1. Use the notes' gold term “First Welfare Theorem” with the on-model line
   “Competitive markets with no externalities maximize welfare.”
2. Keep “Competitive market” and “All costs and benefits counted” as two short
   condition labels beside the unchanged model. Hold.
3. The animation establishes the claim for this partial-equilibrium, dollar-gain
   model with fixed values/costs, identical tradable units, and no outside effects.
   It is not a general-equilibrium proof or a claim that maximum dollar surplus
   settles distributional questions. This is an implementation boundary, not
   extra text to place on screen.

## 6.a · Move from exact lots to the familiar smooth areas

1. Return the $4 market to the compact plaza-left/graph-right layout. Title:
   “What do price controls change?” Retain the selected 40 lots.
2. Lift a copy of the traded CS/PS strips onto the overlaid graph. Keep the
   original crowd bars fixed. Caption the graph “Smooth-market approximation.”
3. Refine the graph copy into narrow strips and then the familiar continuous
   CS/PS regions. Do not morph the literal crowd's aggregate dollar total into
   the continuous total or claim exact equality of the two measurements.
4. Use the known triangle geometry briefly: CS $160,000, PS $40,000, TS $200,000.
   Hold this smooth-market benchmark. Subsequent area totals use these curves;
   crowd counts at $3/$4/$6 still coincide exactly with graph quantities.

## 6.b · A ceiling that does not bind

1. Keep the market at $4. Introduce a maximum legal price of $5, with a distinct
   labeled cap and a bracket for the legal prices below it. Do not move the
   actual market-price line to the cap.
2. Ask “Does this ceiling change the outcome?” Hold. On advance, show
   “Nonbinding”; retain the same 40 trades and welfare areas.

## 6.c · Pin the price below equilibrium

1. Lower the ceiling to $3. The market stays at $4 until the cap reaches it,
   then follows the cap down to $3. Keep the faint
   equilibrium reference at $4. Show “Maximum legal price.”
2. Reveal the familiar 45/20/20 counts and shortage of 25,000 pounds. Circle the
   highest-value 20 buyers and lowest-cost 20 sellers. Beside the rows, briefly
   show “Assume highest-value buyers and lowest-cost sellers trade.” This is the
   best allocation of the available trades, not something a ceiling guarantees.
3. Revisit Amanda-Grace's outbid from `1.f`. Strike the $3.25 option with “Above
   the ceiling.” Hold “The incentive remains; the higher price is prohibited.”
   The shortage persists; do not run the recap's return-to-equilibrium play.

## 6.d · Show the beneficial trades that are missing

1. Keep the cap, actual price, and 20 trades visible. In the unselected rows,
   outline the beneficial pairs 21–39 and the zero-gain boundary pair 40.
2. Enlarge pair 21 once: MB $7.80 > MC $3.05, but the seller cannot cover cost
   at a legal price ≤$3. This is an available social gain blocked in this
   price-controlled market, not welfare already received by an unserved buyer.
3. Copy the outlines to the graph's Q=20…40 interval. Shade the smooth-model
   lost-gains region grey. Hold “Deadweight loss: gains from trade left unrealized.”

## 6.e · Measure the ceiling's welfare effects

1. Shade CS only under demand, above $3, through Qx=20; PS only above supply,
   below $3, through Qx=20. Shade DWL between the curves from 20 to 40.
2. Carry the known measurements to brief area arithmetic. Reveal CS $140,000,
   PS $10,000, total surplus $150,000, and DWL $50,000; keep the $200,000
   benchmark faintly visible for the comparison.
3. Hold “Lower price; fewer trades.” Make visible that continuing buyers pay
   less but buyers as a group lose surplus in this example. Do not animate the
   notes' current claim that aggregate CS rises for these numbers.

## 6.f · Restore equilibrium and introduce a floor

1. Remove the ceiling and let the market return to $4 and 40 trades. Restore
   the same benchmark areas before introducing the new policy.
2. Introduce a minimum legal price of $3 with legal prices above it. Keep the
   actual price at $4; show “Nonbinding” without a separate prediction stop.
3. Hide counts, checks, circles, quantity read guides, and filled welfare areas
   before raising the floor. The actual price stays at $4 until the floor
   reaches it, then follows the floor up to $6. Ask “How much actually trades?”
   Hold before revealing the answer; no stale 40-trade marks remain.

## 6.g · A floor leaves sellers without buyers

1. Reveal Qd=30, Qs=80, Qx=30, and excess 50,000 pounds. Circle only the
   lowest-cost 30 sellers and highest-value 30 buyers.
2. Revisit Andrew's $5.75 undercut from `1.h`; strike it with “Below the floor.”
   Keep his MC $4 visible: wanting to sell is not the same as finding a buyer.
3. Outline missing beneficial trades 31–39, and the zero-gain pair 40. Hold
   “The lower price is prohibited.” There are no government purchases in this
   example; 80 willing sellers do not produce 80 realized sales or PS areas.

## 6.h · Measure the floor's welfare effects

1. Shade the smooth-model areas only through Qx=30. Reveal CS $90,000,
   PS $97,500, total surplus $187,500, and DWL $12,500.
2. Hold the comparison with the original $160,000 CS and $40,000 PS: buyers
   lose, producers in aggregate gain in this particular example, and total
   gains fall. Keep the unserved sellers visible so a group gain is not read as
   every seller gaining.
3. Do not generalize the sign of CS or PS changes to every possible control.

## 7.a · Return to the result and its limits

1. Remove the floor and restore the $4 market, 40 trades, and maximum smooth
   surplus. Show the theorem line again on the same stage.
2. Highlight its two conditions in turn. Keep the notes' externality examples
   and Adam Smith discussion as spoken material; introduce no new market or
   externality simulation in this episode.
3. Hold “Does efficiency settle the policy question?” Keep CS/PS separately
   colored within total surplus. This supports the notes' final distinction
   between welfare analysis and society's other policy objectives.

## Review and implementation checks

- The opening has nine teaching holds (`1.a`–`1.i`) before Exercise Q2. Confirm
  the time budget with Taylor; the initial proposal is roughly five minutes,
  excluding the exercise. Keep the one switch; remove extra arithmetic or
  intermediate price stops first if the recap runs long.
- The draft has 38 named holds including the bumper and exercise. Beat actions
  explicitly marked “on advance” belong after that beat's pause. Recount after
  review; do not add hidden per-person or navigation-only pauses in code.
- Review whether the buyer and seller substitution beats make the planner's
  problem clear without feeling like a new lecture on rationing. These are the
  principal new staging proposals; keep them separate from the already-approved
  B3 recap mechanics.
- Preserve the integer-lot/continuous distinction, the zero-gain boundary, and
  units in every label. At held market prices, circles per side equal Qx and
  check totals equal Qd/Qs. Planner quantities are explicitly chosen allocations.
- Confirm the $4↔$5 price movement in `2.b` leaves total gain and quantity fixed.
  Confirm the swaps change only the intended participant, and that pending or
  rejected trades contribute no realized surplus.
- Check proposed full-crowd and head-on stopped frames at actual projection size
  before implementing all motion. Keep label size; simplify the visible detail
  if needed. Verify overlays, forward/backward seeks, and retained states in the
  ManimLive development viewer. No visual validation has been done for this draft.
- B4's existing `03_Code.py` is a legacy notebook export using a different
  market. Reuse useful choreography from B3/B1/B2 without importing its old
  equilibrium price or welfare geometry. Shared assets, model files, notes,
  exercises, and other blocks are outside this storyboard edit.

## Notes reconciliation for Taylor/Fable

- Condense the long CS and PS sections to familiar-tool callbacks, per Taylor's
  latest instruction. Keep the gain-cancellation argument because it explains
  what the planner is maximizing.
- The current notes alternate between controlling quantity and controlling
  price. This draft establishes the best people/quantity first, reconnects to
  decentralized equilibrium, then uses price controls as applications.
- “For every unit above the quantity exchanged” should be checked against the
  intended area: realized total surplus is summed over the units exchanged.
- “When price decreases, CS increases” applies to an unchanged set of trades
  in `2.b`; it is not a general result after quantity/rationing changes. At the
  specified $3 ceiling aggregate CS falls, from $160,000 to $140,000 in the
  smooth model. The notes' ceiling claim and low-price offset sentence need
  reconciliation. The $6 floor raises PS substantially, not merely “slightly.”
- “Any deviation from this outcome reduces welfare” is too strong for the exact
  crowd: dropping its zero-gain final trade changes no welfare, and swapping
  counterparties among the same selected people changes no aggregate benefit
  or cost. The theorem concerns maximal gains, not a unique matching.
- Theorem wording follows the notes' course-level formulation. The animation's
  demonstrated result is total-surplus maximization in this specified competitive
  market, with all relevant benefits and opportunity costs in the bars.
- Government purchases appear as a future capability in B3's outline, but are
  absent from this first B4 sequence, consistent with B4.2's skillsheet. Adding
  them would require a separate allocation and government-accounting beat.
