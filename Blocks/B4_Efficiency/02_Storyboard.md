# Episode B4 | First Welfare Theorem | Storyboard

B3-based animation implementation · 2026-09-22.

Latest direction: interrupt the recap with Exercise B3 Q2 **before** resolving
equilibrium. Establish the people and willingness counts at an off-equilibrium
price, let the class reason about incentives, then show one deliberation and
one compressed common-price adjustment in each direction. Never reveal $4 as
the answer before that exercise. The seven stages remain independently runnable.

The live B4 notes now specify exact crowd welfare totals. Use those totals for
any crowd implementation; the continuous exercise market remains separate.
The standalone later scenes retain Taylor’s confirmed planner → theorem → policy order; their order can change without rebuilding the recap.
Lecture notes, exercise files, and the older Typst storyboard are author-owned.

## Runnable scenes

Each file is independent. Run its header command with `maniml` from this folder.
All use 15 fps and flat, sequential `construct()` choreography. Existing B3
geometry/model code is copied where indicated below; no shared assets changed.

| File | Class | Teaching stops |
|---|---|---|
| `03_01_Exchange.py` | `B4Exchange` | `0.a`, `1.a` |
| `03_02_Bidding.py` | `B4Bidding` | `1.b`, `1.b.settled` |
| `03_03_TwoTrades.py` | `B4TwoTrades` | `1.b.two_trades`, `1.b.equal_prices` |
| `03_04_Buyers.py` | `B4Buyers` | `1.c.buyers`, `1.c.buyers.low` |
| `03_05_Sellers.py` | `B4Sellers` | `1.c.sellers` |
| `03_06_Equilibrium.py` | `B4Equilibrium` | `1.d`, `1.e`, **`1.j`**, `1.f`–`1.i.stable` |
| `03_07_Graph.py` | `B4Graph` | `1.i.graph`, `1.i.algebra` |
| `03_08_Welfare.py` | `B4Welfare` | `2.a`–`5.d` |
| `03_09_Controls.py` | `B4Controls` | `6.a`–`7.a`, including both B4 exercises |

`03_Code.py` remains the older notebook export. The numbered scene files above
are this build's entry points.

## Direction and sources

Taylor's current direction is to make the simulation carry the welfare argument.
CS and PS are familiar from B1/B2. Price-control arithmetic and graphs build on
B3. The central new work is showing why an allocation maximizes total gains,
then showing that the market selects that allocation.

Confirmed in the September 22 storyboard interview:

- The newly written source is [B3's conversation outline](../B3_Equilibrium/00_Outline.md).
- Give the opening 5–10 minutes, excluding Exercise Q2, to teach all seven stages
  of that outline in their simplest form. This is B4's complete explanation of
  the equilibrium ideas that did not land clearly in class; it must stand on
  its own without returning to a separate B3 animation.
- Retain the small exchange, bidding, and two-trade stages, then build buyers,
  sellers, equilibrium, and the graph/algebra bridge. Give the largest share of
  the time to explaining why the equilibrium price holds.
- Let the social planner establish the best allocation before connecting it to
  competitive equilibrium.
- Edit only animation files and `02_Storyboard.md`; lecture prose stays with
  Taylor/Fable. This pass implements the animation scenes and keeps this storyboard current.

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

## Reuse B3's finished staging

Taylor's live review rejected the initial flat prototype. The implementation
now uses B3's actual `ThreeDScene`, sphere/shadow people, upright `Rectangle3D`
bars, ground circles, floor/rim, fixed graph overlays, and camera choreography.
The prototype is superseded; it is not an alternative design to preserve.

- Exchange and bidding copy B3 `2.a`–`2.c`, including the plaza-to-head-on
  move, bar width 1.10, gap 0.12, dollar height 0.55, base 0.75, and the
  camera centered at `[0, 0, 2.05]`, height 7.2, phi 90°.
- Two trades copies B3's `3.a` plaza and uses the familiar head-on view for
  Amanda-Grace's alternatives. It returns to the plaza for the recorded trace.
- Crowd scenes reuse B3's radius-4.8 floor and rim, and its plaza-left camera:
  phi 48°, theta 0°, focal distance 50, center `[4, 0, 0.65]`, height 11.
  More participants require smaller people/bars and folded sorted rows inside
  that same floor. No new camera orbit or replacement illustration is added.
- Buyer/seller introductions face the actual 3D rows. A projected copy of their
  bar tops moves into the graph using B3's `screen_point` technique, while the
  camera pulls back to the existing plaza view. The rows do not merely appear
  beside unrelated curves.
- Crowd deliberations enlarge the actual selected people/bars into B3's
  head-on view. The graphs temporarily clear for that comparison, then return
  with the original plaza camera. One illustrated switch precedes the common
  price adjustment; this is not a replay of every person's decision.
- Welfare comparisons retain B3's dollar-to-height scale. Pair 20, the buyer/
  seller substitutions, and proposed pair 21 need the taller head-on frame:
  center `[0, 0, 3.4]`, height 10.2, phi 90°. The later marginal pairs return to
  B3's center `[0, 0, 2.05]`, height 7.2. This keeps the $8–$10 bars below the title.
- `fixed`, `add_market_objects`, and the original text billboard adapter are
  reused from B3. They handle renderer/label behavior, not teaching choreography.
  No shared asset or engine code is changed.

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
  Individual comparisons enlarge the relevant bars into a head-on view while
  hiding the other people; their allocation stays unchanged. A full-width head-on row is reserved
  for the quantity sweep; it is not squeezed beside two small graphs.
- Read each compact row left to right, then continue on the next row. Preserve
  rank order across folds. Every row has the same local zero and dollar scale;
  repeat a local price segment at the appropriate height in each row, all driven
  by the same price. These are copies of one common price, not separate asks.
- Build the demand graph from its buyers and the supply graph from its sellers
  during the recap; stack them when both sides share the stage. At
  `1.i.graph`, slide those same axes into a single overlaid graph while retaining
  the crowd. That graph carries directly into the welfare argument at `2.a`.
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
  The exact crowd's read guides land on staircase boundaries. Smooth lines remain
  faint fitted references; policy totals use the exact crowd's rectangles.
- The scene files use flat, sequential `construct()` choreography, visible
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

The exact crowd is the implemented welfare model: $195,000 is its benchmark.
The smooth column is a numerical comparison for review, not an animated change
of model. Exercise B3/B4 cards explicitly switch to their separate pasty market.

## 0.a · Open B4

1. Use the shared bumper, “Part B | Episode 4,” and the notes' thesis:
   “Under some conditions, nothing can do better than markets.”
2. Hold, then clear the bumper for the exchange reminder.

## The seven-stage opening — teaching and pacing contract

These are the seven stages from B3's outline, taught here as one short sequence.
Each stage contributes one claim. Simplification means fewer examples and
stops within each stage, not skipping the link between individual choices,
quantities, and equilibrium. These timings include animation, explanation, and
short responses from the room; they are not timed waits in the scene.

| B3 stage | B4 beats | The claim to leave visible | Speaking + motion budget |
|---|---|---|---|
| 1. Exchange | `1.a` | A price between cost and value makes both sides gain. | 30–45 s |
| 2. Bidding | `1.b`, `1.b.settled` | A buyer left out can offer more; the seller gains from switching. | 40–60 s |
| 3. Two trades | `1.b.two_trades`, `1.b.equal_prices` | A better alternative gives someone a reason to switch; competition brings these prices together. | 45–60 s |
| 4. Buyers | `1.c.buyers` | At a common price, count the buyers whose MB reaches it: Qd. | 35–50 s |
| 5. Sellers | `1.c.sellers` | At that same price, count the sellers whose MC is covered: Qs. | 35–50 s |
| 6. Equilibrium | `1.c`–`1.i`, then `1.i.stability` | Unequal counts leave willing people without trades; their incentives move price. At $4 the counts match and the pressure disappears. | 150–220 s |
| 7. Graph and algebra | `1.i.graph`, `1.i.algebra` | The crossing and Qd=Qs express the same market condition. | 45–75 s |

The working allocation totals **6 minutes 20 seconds to 9 minutes 20 seconds**,
within Taylor's 5–10 minute request. Keep the equilibrium explanation spacious
and the earlier examples brief. Exercise Q2 interrupts stage 6 after the
shortage count, before the adjustment to equilibrium, and has its own classroom
time. The bumper is outside this recap budget.

## 1.a · Recall one exchange

1. Restore B3's approved Gary/Molly head-on close-up: MB $6, MC $2, price $4,
   “One pound.” Title: “Which prices work?”
2. Reveal the already familiar CS $2 and PS $2 together. Retain the green
   expenditure/revenue boundary and orange cost. Do not replay the five-step
   accounting construction or introduce either surplus definition again.
3. Mark the open $2–$6 interval between the two thresholds and show “MC < P < MB.”
   Keep $4 inside it. At an endpoint one person is indifferent; the interval
   marks strictly positive gains for both. Hold this one example rather than
   cycling through several accepted and rejected prices.

## 1.b · Recall why a deal changes

1. Remove the accounting labels; retain Gary's solid $4 deal. Admit Amanda-Grace
   with MB $7 using B3's existing three-person head-on layout.
2. Show her dashed $4.25 proposal and the question “Would Molly switch?” Hold
   before acceptance.
3. On advance, move Molly's MC comparison to Amanda-Grace's side, solidify $4.25,
   and release Gary's old connection. Carry forward B3's accepted-line grammar.
   Show Gary's $4.50 response, then compress the remaining quarter-dollar bids
   into one uninterrupted sequence with no extra teaching stops.

## 1.b.settled · Explain why the bidding stops

1. Park with Amanda-Grace buying from Molly at $6.25. Keep Gary's MB $6 and
   Amanda-Grace's MB $7 visible; show “Gary's next bid: $6.50 > MB $6.”
2. Show the small count “At $6.25: 1 willing buyer, 1 seller.” Hold “Who still
   wants to bid?” The point is that the buyer-side outbidding has stopped.
3. Do not claim Molly cannot ask more, or use this one-seller case as the full
   competitive-equilibrium argument. The whole-market claim comes in stage 6.

## 1.b.two_trades · Give the buyer another option

1. Admit Andrew with MC $4 and an entry ask of $4.25 in B3's original plaza.
   Use B3's head-on comparison geometry to face Amanda-Grace, Molly, and Andrew
   during the decision. Gary remains the unserved buyer in the underlying market.
2. Retain Amanda-Grace's solid $6.25 deal with Molly. Show her two alternatives:
   “Molly: $6.25; gain $0.75” / “Andrew: $4.25; gain $2.75.” Title: “Stay or switch?” Hold.
3. On advance, return to the same plaza and let Amanda-Grace take Andrew's $4.25 offer, then let Gary outbid
   at $4.50. Keep Molly at $6.25 with no buyer. Continue the recorded seed-54
   events without per-event pauses: Amanda-Grace $4.75, Gary $5, Molly cuts to
   $6; Amanda-Grace $5.25, Molly $5.75; Gary $5.50, Molly $5.50; Amanda-Grace
   takes Molly's open $5.50 offer. Show each changed price; do not invent or
   duplicate a seller cut. This is the same trace as B3's outline.

## 1.b.equal_prices · Park on two trades

1. Return to B3’s original plaza. Keep Gary with Andrew and Amanda-Grace with Molly. Both prices are $5.50.
   Show “2 willing buyers; 2 sellers” and “Both trades: $5.50.”
2. Ask “Would either buyer switch?” Hold with the alternative prices visible.
   The new seller has given buyers an alternative and made Molly respond.
3. This path demonstrates prices coming together. Do not claim the finite
   quarter-dollar model rules out a one-tick difference or that $5.50 is the
   unique possible small-market price. Omit the extra scripted price-rise test;
   the full crowd receives the stability test below.

## 1.c.buyers · Build quantity demanded from the people

1. Reconstruct all 59 buyers as a sorted 3D head-on row. This independent scene does not replay the small-market story. Caption “One person = 1,000 pounds”; keep bar heights in
   dollars per pound. This explicitly changes the unit from the one-pound trades.
2. Lift a copy of the sorted profile onto the demand graph at upper right;
   retain the people and their bars. Label the fitted line (P=12-Q_d/5).
   Title: “How many would buy at this price?”
3. Place the price at $6 and reveal 30 checks, with Gary exactly on the line.
   Show Qd=30 and “MB ≥ P.” Only Gary and the nearest excluded buyer need tags:
   $6 and MB $5.80. Hold; touching the line counts as willing.

## 1.c.buyers.low · Willingness is not a trade count

1. Lower the price from $6 to $3 in one play, revealing 45 checks and Qd=45.
2. Park on “At $3, 45 buyers are willing. We have not counted trades.”
   No trading circles or Qx appear; sellers have not entered this comparison.
3. Gary's preceding caption gives his MB $6 and the next buyer's $5.80 offer;
   individual tags are kept sparse rather than printed over every person.

## 1.c.sellers · Build quantity supplied the same way

1. Keep demand parked at $3 and Qd=45 on the upper graph. Reveal all 100 sellers
   as their own sorted head-on row; retain the 1,000-lb-lot convention.
2. Lift a copy of their profile to the supply graph directly below demand,
   with the same quantity scale. Label the fitted line (P=2+Q_s/20).
   Title: “How many would sell at this price?”
3. At the same $3, reveal 20 checks and Qs=20. Show “MC ≤ P.” Tag the boundary
   seller at $3 and the next seller at MC $3.05. Hold. Supply counts willingness;
   it is not a tally of completed sales. Keep circles and Qx absent until `1.c`.

## 1.c · One price, many decisions

1. Reconstruct the sorted buyer and seller rows together, with demand above
   supply at right. The independent scene begins at $3, as the seller scene ends.
2. Keep the unit convention visible: one person is 1,000 lb; price is dollars/lb.
   No equilibrium answer, crossing, or starred pair is visible yet.
3. Introduce the distinction between a willingness check and a trading circle.
   This is a transition into `1.d`, not an additional teaching hold.

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

## 1.j · Exercise B3 Q2 — before resolving equilibrium

1. After the $3 shortage has been counted at `1.e`, replace the market with the
   existing Exercise B3 Q2 card. Preserve the problem's pasty equations:
   (P=12-Q_d/2), (P=2+Q_s/2), price 5 galleons; quantities are pasties.
2. Use the sheet's exact four prompts: “What is the quantity demanded?”, “What
   is the quantity supplied?”, “Is this a shortage or an excess, and how large?”,
   and “Which way will the price move?” No answers appear before this pause.
3. Below the four prompts ask “What would buyers and sellers want to do?”
   This discussion cue supplements the existing sheet; it does not edit it.
4. On advance restore the spinach market at $3, still 45/20/20. The next beat
   enacts the incentives students just discussed. The pasty problem never
   substitutes its data into the spinach simulation.

## 1.f · Recall the incentive to raise price

1. Highlight Amanda-Grace in the original 3D plaza, then bring her and a served seller into B3’s head-on view. Clear the fixed graphs during that comparison. Replace the bottom text with two concise options:
   “Wait: no trade” / “Offer $3.25: gain $3.75/lb.” Draw the proposed bid dashed.
   Show that the served seller receives more if the bid is accepted. The two options stay in the bottom band; a dashed connector identifies the proposed switch, not an extra trade.
2. Ask “Which way does price move?” Hold with the answer still withheld.
3. On advance, accept the proposed price in the close-up, return to B3’s plaza camera, and show Amanda-Grace moving to the seller. Then clear the individual proposal and show “Other unserved buyers have the same incentive.” Follow with “Shortage → price rises.”
   Raise the common price to $4 in one continuous play. A faint price ladder retains the starting and ending prices; intermediate quarter-dollar steps are not extra pauses. Keep counts and marks
   synchronized; do not narrate every threshold crossing or stop at each tick.
4. Keep 40/40/40 visible as the next question enters; no navigation-only stop.

## 1.g · Predict the high-price result

1. Hide numerical counts, willingness checks, trading circles, and quantity
   read guides before moving the common price to $6. Ask “At $6, who is left
   out?” Hold with those answers still hidden.

## 1.h · Count the excess and recall undercutting

1. Reveal Qd=30, Qs=80, Qx=30: 30 buyer checks, 80 seller checks, 30 circles on
   each side. Mark the quantity gap 30–80; show “Excess: 50,000 pounds.”
2. Highlight Andrew among the unserved sellers and Gary among the served buyers. Show the same B3 head-on inspection view, with Andrew’s MC $4 and Gary’s MB $6. The actual plaza returns before Gary moves to Andrew.
   Replace the bottom content with “Keep $6: no buyer” / “Ask $5.75: gain $1.75/lb.”
   Gary would also gain by paying less. Ask “Which way does price move?” Hold.
3. On advance, briefly accept the proposed switch, then clear it and show “Other unserved sellers have the same incentive.” Follow with “Excess → price falls.” Move the
   common price to $4 in one play, retaining the counts throughout.

## 1.i · State the two parts of equilibrium together

1. Park on 40 checks and circles on each side and Qd=Qs=Qx=40. Keep unwilling
   people visible and dim, with their bars on the wrong side of the price.
2. Replace the adjustment caption with “Equilibrium: Qd=Qs=40” and
   “No willing buyer or seller is left without a trade.”
3. Point to both parts on this same frame: the matching counts,
   the absence of willing people left without trades, and the dim people whose
   MB/MC keeps them out at $4. Hold before testing the pressure at nearby prices.

## 1.i.stability · Test why the price holds

1. Keep $4 and the 40 trades as the faint reference. Show a dashed proposed
   $4.25 line without its count answers. Ask “Would a higher price hold?” Hold.
2. On advance, test $4.25: Qd=38, Qs=45, Qx=38. Show seven willing sellers
   without circles. Sellers 39–40 lose trades; sellers 41–45 become newly
   willing but unserved. Caption “Seven willing sellers have no buyer. They
   can undercut.” Restore $4.
3. Test $3.75 in the same short sequence: Qd=41, Qs=35, Qx=35. Show six willing
   buyers without circles. Buyers 36–40 lose trades; buyer 41 is newly willing.
   Caption “Six willing buyers have no seller. They can offer more.” Restore
   $4 and the 40 trades.
4. Park at `1.i.stable` on “Above $4: excess. Below $4: shortage.” before the
   graph transition. Use staircase count guides for these tests: the exact
   whole-lot counts differ from smooth-curve intersections at quarter dollars.
   Keep the cause visible as willing people left out, not just the marginal
   pair refusing an unaffordable price.

## 1.i.stable · Keep the conclusion visible

1. End the two deviation tests back at $4 and 40 trades.
2. Hold “Above $4: excess. Below $4: shortage.” This is the stable endpoint
   from which the independent graph scene begins.

## 1.i.graph · Recognize the same condition at the crossing

1. Retain the settled crowd and $4 line. Slide the two stacked graphs onto the
   same axes. Their continuous lines cross at Q=40, P=$4, matching the crowd's
   counts exactly at this price.
2. Title: “Why does the crossing give equilibrium?” Highlight Qd=Qs=40 below
   the graph and their shared point. Keep the people visible so this is another
   representation of the same result, not a second definition. Hold.

## 1.i.algebra · Make the equality explicit

1. Temporarily fade the crowd and slide the same merged graph to the left,
   opening B3's established right-hand math area. Carry copies of the displayed
   equations there, retaining their subscripts: (P=12-Q_d/5) and (P=2+Q_s/20).
2. Show (Q_d=Q_s=Q) before setting their right-hand sides equal. Then reveal
   (12-Q/5=2+Q/20), (10=Q/4), and (Q^*=40) in that order, with no extra
   arithmetic pauses. Substitute into supply to show (P^*=2+40/20=4).
3. Carry the starred pair to the crossing. Hold “Same price; equal quantities.”
   This is a short explanation of what the algebra means; leave Exercise Q1
   completed. This independent file ends on the solved frame. The welfare file reconstructs
   the same unchanged crowd and merged graph at $4; it does not replay the algebra.

## 2.a · Ask whether the market's answer is good

1. Title: “Could we do better?” Keep the 40 trades in the crowd.
2. Retain the already-merged graph from `1.i.graph`, its units, colors, selected
   quantity, and $4 price. Clear any remaining recap labels without rebuilding
   the graph or replaying its overlay move.
3. Briefly light the familiar CS and PS portions of traded bars together. Hold
   the notes' welfare question without re-teaching how those regions are defined.

## 2.b · Separate the size of the gain from its division

1. Enlarge the two bars for ranked pair 20: buyer MB $8, seller MC $3. Hide the
   other people while keeping their allocation fixed. Caption “One 1,000-lb lot.”
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
2. Compare the selected prefixes by rank using their circles. Do not imply
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

1. Return pair 39 to its row and enlarge only pair 40: MB $4 and MC $4. Its
   potential gain has zero height. Ask “What does this trade add?” Hold before
   the answer.

## 4.d · Account for indifference

1. Reveal “$0.” Circle rank 40 on each side using the existing convention that
   indifferent people are willing to trade. Move Q from 39 to 40 without
   increasing the total-surplus region.
2. Hold “The last trade adds zero.” Keep a small caption “39 or 40: same total
   gain” for this exact finite market. This is the endpoint, not a numerical bug.

## 4.e · Test a trade beyond the boundary

1. Keep the 40 chosen trades intact. Enlarge rank 41: MB $3.80, MC $4.05.
   Its connection stays dashed and its people stay uncircled.
2. Label the buyer's acceptable prices P≤$3.80 and the seller's P≥$4.05 beside
   the enlarged bars. Their values leave no mutually acceptable price.
3. Ask “Would this trade help?” Hold. On advance, reveal “−$250” and “MC > MB.”
   Do not paint negative private gains as realized CS/PS or execute a voluntary
   trade that neither common price can support.

## 4.f · Read the planner's complete rule

1. Return the enlarged pair to the full-width head-on comparison; the graph
   remains parked off screen. Begin with 40 chosen pairs; outline the
   positive gains through pair 39 and the zero-height boundary at pair 40.
2. Sweep a quantity marker back to 30. Remove circles and gain fills from
   pairs 31–40 as they leave the allocation, leaving the forgone positive gains
   from pairs 31–39 as empty outlines. Return to 40, restoring the circles
   and gain fills as each pair rejoins; pair 40 still adds no gain.
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
2. Recall the boundary with two threshold captions on the plaza: buyer 40 is
   indifferent, buyer 41 will not pay $4; seller 40 is indifferent, seller 41
   will not sell at $4. The enlarged comparison has already established why.
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

## 6.a · The same market's welfare benchmark

1. Reconstruct B3's 3D plaza beside the merged market graph at $4, 40 trades.
2. Shade one rectangle per traded lot: teal MB minus price and orange price
   minus MC. These are the exact people from the recap, not smooth triangles.
3. Hold on CS $156,000, PS $39,000, total surplus $195,000. State the policy
   comparison's allocation assumption: highest-value buyers and lowest-cost
   sellers trade. This keeps rationing explicit rather than asserting that any
   real-world control necessarily achieves that allocation.

## 6.b · A nonbinding ceiling

1. Introduce a maximum legal price of $5, with the legal interval below it.
2. Actual price stays $4 and Qx stays 40. Hold “Nonbinding.” The policy line
   and the actual market price are distinct.

## 6.c · Predict a binding ceiling

1. Hide counts, willingness checks, trade circles, and welfare fills before
   lowering the ceiling from $5 to $3.
2. Actual price stays $4 until the ceiling crosses it, then follows it to $3.
3. Ask how much actually trades. Hold before the answer appears.

## 6.c.blocked · The incentive remains; the bid is prohibited

1. Reveal Qd=45, Qs=20, Qx=20. The first 20 people on each side trade.
2. Recall Amanda-Grace's proposed $3.25 bid and mark it “Not allowed.” The
   ceiling prevents the earlier rise play; it does not remove her incentive.
3. Hold on the shortage and the blocked bid.

## 6.d · The lost beneficial trades

1. Outline the forgone gains from pairs 21–39 in grey. Pair 40 adds zero.
2. Keep the 20 actual trades filled; proposed/missing trades acquire no circles.
3. Define deadweight loss as the lost total surplus. Hold before the total is
   revealed, retaining the exact per-lot geometry.

## 6.e · Measure the ceiling

1. Reveal CS $138,000, PS $9,500, TS $147,500, and DWL $47,500.
2. Continuing buyers pay less, but buyers as a group lose surplus in this
   example. Compare with the original $156,000 rather than claiming that a
   lower controlled price always raises aggregate CS.

## 6.exercise_ceiling · Exercise B4 Q1

1. Clear the simulation for the original pasty equations and 5-galleon ceiling.
2. Copy the sheet's prompts: quantity exchanged, CS, PS, DWL, and plotting the
   demand/supply/ceiling with shaded areas. Show no answers.
3. Hold, then restore the spinach market. The exercise's continuous pasty areas
   are not the crowd's exact spinach totals.

## 6.f.nonbinding · Remove the ceiling; introduce a floor

1. Restore the $4 market, its 40 trades, and its original welfare.
2. Introduce a minimum legal price of $3. Actual price stays $4. Hold on this
   nonbinding case before moving the floor.

## 6.f · Predict a binding floor

1. Hide counts, checks, circles, and welfare fills before raising the floor.
2. Actual price stays $4 until the floor reaches it, then follows it to $6.
3. Ask how much actually trades. Hold with answers hidden.

## 6.g · The undercut is prohibited

1. Reveal Qd=30, Qs=80, Qx=30: 50 willing sellers have no buyer.
2. Recall Andrew's proposed $5.75 offer and mark it “Below the floor.”
3. Circle only the first 30 on each side. There are no government purchases;
   80 willing sellers do not mean 80 sales or 80 units of realized PS.

## 6.h · Measure the floor

1. Shade gains only on the 30 actual trades. Outline missing positive gains
   from 31–39; pair 40 contributes zero.
2. Reveal CS $87,000, PS $96,750, TS $183,750, and DWL $11,250.
3. Producers gain in aggregate in this example; the visible excluded sellers
   prevent that group result from implying that every seller gains.

## 6.exercise_floor · Exercise B4 Q2

1. Show the sheet's 9-galleon floor and original prompts: quantity exchanged,
   producer surplus, deadweight loss, and whether a floor of 6 changes the market.
2. Show no answers. Hold, then return to the spinach market.

## 7.a · Return to the result and its limits

1. Remove the floor and restore $4, 40 trades, and exact TS $195,000.
2. Keep “Does efficiency settle the policy question?” as the final question.
   Preserve the distinction between maximal gains and other policy objectives.
3. Retain the theorem's conditions: competition and all relevant benefits and
   costs counted. The exercise is not a claim that every policy objective is
   captured by CS plus PS.

## Review and implementation checks

- There are **51 literal named holds** across the nine files. The opening seven
  scenes contain 20: the bumper, Exercise Q2, and 18 teaching holds. Target
  5–10 minutes of recap excluding the exercise, around 7–8 minutes in rehearsal.
  Keep the equilibrium explanation; shorten spoken bidding repetition first.
- Exercise Q2 comes after the shortage is counted, before any $4 equilibrium
  answer appears in the full market. The pasty exercise remains a separate model.
- The exact quarter-dollar counts, inclusive willingness, and 39/40 welfare tie
  are retained. Circle interiors stay empty: visibility updates change stroke
  opacity, never fill opacity. Check marks likewise remain open strokes.
- Source execution and checkpoint restoration have been checked in ManimL.
  B3's copied small-market trace retains its final matching/price assertions.
  Each policy/planner state is checked against exact participant counts and gains.
- Visual review uses the development viewer and selected full-resolution native
  frames for this build. Native frame caches can display stale glyphs after
  unrelated checkpoint captures; suspected failures are checked with an isolated
  direct run before changing correct scene geometry.
- The recap, welfare, and control views have been reviewed. Direct native
  captures verify the welfare close-up labels, payment line, one enlarged pair
  at a time, and complete restoration of the ranked row at `4.f`.
- Only these animation files and this storyboard belong to the update. Notes,
  exercises, shared assets, and B3 files remain outside the animator's edits.

## Notes reconciliation for Taylor/Fable

- B4 now includes the seven-stage equilibrium explanation requested by Taylor.
  It needs to work as the class's clear account of these ideas, without requiring
  a separate return to B3. Use B3's conversation outline as its source; keep the
  literal lesson notes and the separate B3 storyboard untouched in this pass.
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
  specified $3 ceiling aggregate CS falls, from $156,000 to $138,000 in the implemented exact crowd. The floor’s
  producer surplus rises from $39,000 to $96,750. These agree with the live notes; retain the fixed-quantity qualification for the general sentence.
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
