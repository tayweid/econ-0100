# Episode B4 | First Welfare Theorem | Storyboard

B3-based animation implementation · 2026-09-22.

Latest authorized order: **market benefits (CS/PS → total surplus) → binding
floor → binding ceiling → permit a blocked trade → all beneficial trades →
force one harmful trade → undo it and state the conditional welfare result**.
This explicitly supersedes the earlier planner-first draft, the ceiling-first
notes, and the animator note's frozen-order instruction. Keep the entire opening
through `1.i.algebra` unchanged.

The review before Exercise B3 Q2 remains **under ten minutes, targeting eight**.
The exercise interrupts the $3 recap before equilibrium is resolved. The later
welfare argument uses the exact crowd; exercise markets remain separate.
Lecture notes, exercise files, and the older Typst storyboard are author-owned.

## Runnable animation and holds

Run **`maniml 03_B4.py B4`** for the canonical complete lesson. The code stays
flat and sequential at 15 fps. The first seven code sections retain their
**22 named holds**; the new continuous section 8 has **16 named holds**, for
**38 total** with the exercise placement below. The back half reuses the same
curved plaza and merged graph from the opening, including their actual objects.

| Code section | Content | Named holds |
|---|---|---|
| 1–7 | Existing exchange, bidding, two trades, demand, supply, equilibrium, graph/algebra | `0.a` through `1.i.algebra` (22 unchanged) |
| 8 | Market benefits | `2.a`, `2.b` |
| 8 | Binding floor, lost gains, blocked pair | `3.a`, `3.b`, `3.c` |
| 8 | Binding ceiling, lost gains, blocked pair | `4.a`, `4.b`, `4.c` |
| 8 | Permit trades, reach the boundary, force/undo harmful trade | `5.a`–`5.e` |
| 8 | B4 exercises, floor then ceiling | `6.exercise_floor`, `6.exercise_ceiling` |
| 8 | Scope and close | `7.a` |

The two B4 exercise holds follow the completed argument, floor before ceiling,
using Taylor's delegated placement decision. Their content and IDs remain intact.

`03_01_Exchange.py` through `03_09_Controls.py` are **stale development snapshots**,
not imported or executed by the canonical file. Their old back-half order and
staging do not represent this build. `03_Code.py` is the older notebook export.
Do not synchronize those snapshots for this change.

## Direction and sources

Use [B3's conversation outline](../B3_Equilibrium/00_Outline.md) for the opening
and [B4's notes](01_Notes.md) for the economic content. The notes and
[older storyboard](B4_Welfare_Storyboard.typ) supply context, while Taylor's
latest directive above determines the animation order. Do not edit those files.

CS/PS are familiar from B1/B2, so begin with their benefits in this market and
sum them. Use the floor and ceiling to make lost mutually beneficial trades
visible. Then permit one missing trade, allow the remaining beneficial trades,
and demonstrate why forcing the next pair lowers total surplus. The simulation
carries the argument; the final theorem names the result and its conditions.

Keep the approved opening and visual decisions: B3's camera/framing, buyers and
sellers on opposite arcs, short bars, actual partners meeting at the center,
world-space text/marks, and the independent merged graph with its lot bars.
The graph has its own price axis; the totem remains a separate plaza indicator.
Use attached labels, plain choice text, and simple fades throughout the back
half. Do not restore old bottom boxes, straight crowd rows, or detached counters.

## Reuse B3's finished staging

Taylor's live review rejected the initial flat prototype. The implementation
now uses B3's actual `ThreeDScene`, sphere/shadow people, upright `Rectangle3D`
bars, ground circles, floor/rim, fixed graph overlays, and camera choreography.
The prototype is superseded; it is not an alternative design to preserve.

- Exchange and bidding copy B3 `2.a`–`2.c`, including the plaza-to-head-on
  move, bar width 1.10, gap 0.12, dollar height 0.55, base 0.75, and the
  camera centered at `[0, 0, 2.05]`, height 7.2, phi 90°.
- Two trades first holds B3's `3.a` oblique plaza with both buyers and both
  sellers visible. Andrew's arrival animates into this frame. Only then does
  the familiar head-on view show Amanda-Grace's alternatives; the recorded
  trade sequence and settled hold return to that same plaza.
- All crowd scenes reuse B3's radius-4.8 floor and rim, and its plaza-left camera:
  phi 48°, theta 0°, focal distance 50, center `[4, 0, -0.4]`, height 11.
  This lifts the full-market plaza about 0.55 screen units, leaving the bottom
  caption strip clear. Use the same framing for all returns from close-ups.
  The merged graph has a fixed right-side origin independent of totem projection.
  The entire back half reuses the recap's same curved plaza, short bars,
  world-space checks/Xs, central partners, totem, and quantity lines. Do not
  reconstruct the older straight-row welfare/control staging. Restore these
  same objects after the algebra and retain them through the closing argument.
- Buyer/seller price comparisons remain in Taylor's approved full-width front
  view: phi 90°, center `[0, 0, 1.9]`, height 8. Keep every person in one row.
  The straight equation line passes through bar-top centers, with rank n at
  Q=n thousand pounds. Both rows use base 0.75 and dollar-height 0.28. The
  price guide ends at the equation line; checks and counts show exact willing
  people. Keep its price readout just left of the dashed guide, tracking its
  height. A bare quantity number tracks the corresponding horizontal position
  below the row, teal for buyers and orange for sellers. Ease in and out of every price move in these comparisons, including
  the sellers' return to $3. Keep the current episode order and teaching holds.
  Bring the plaza and separate market graphs back only when both sides enter
  the equilibrium argument.
- Crowd deliberations enlarge the actual selected people/bars into B3's
  head-on view. The graphs temporarily clear for that comparison, then return
  with the original plaza camera. One illustrated switch precedes the common
  price adjustment; this is not a replay of every person's decision.
- Selected blocked-trade close-ups enlarge the actual pair using B3's
  head-on comparison grammar, then return those same participants to the
  curved plaza. Keep choice/gain labels attached to their bars or price lines.
  Hide the remaining plaza and graph during inspection; restore them on return.
- `fixed`, `add_market_objects`, and the original text billboard adapter are
  reused from B3. They handle renderer/label behavior, not teaching choreography.
  No shared asset or engine code is changed.

## Curved-plaza review convention

Throughout the full-market recap and back half, short floating bars are value cues; the graphs retain
the detailed scale. Buyers occupy the upper/back arc (positive y), sellers the
lower/front arc (negative y), each still ordered by value/cost. A muted dashed
ground diameter at y=0 runs horizontally through the plaza and separates their
halves. Matched partners share an x station on opposite sides of this line:
buyer at y=+0.4, seller at y=−0.4. Center the occupied stations on the diameter.

Plant a vertical price totem at the diameter's right rim endpoint, x=4.8, y=0.
Its grey 0–12 number line carries a red moving price tick and an adjacent dollar
readout. This replaces the large floating price above the plaza; the same price
source drives the totem, graph guides, willingness, and counts. The ground
divider represents the meeting place, not a horizontal price-height guide.

Attach the plaza's buyer/seller labels, totem numbers, price heading, and current
price readout to their actual positions in the 3D scene. Use B3's `face_camera`
convention for genuine world-space, camera-facing text; these labels travel and
scale with the plaza as the camera changes. Do not turn them into fixed-screen
HUD overlays. Main lesson titles and graph text retain their existing conventions.

A green check means willing; a small red X means unwilling. Unwilling people
stay at the rim, willing unmatched people stand on an inner arc in their own
half, and partners meet across the center line. Pair adjacency carries the
trading meaning; the old circle objects remain invisible code anchors only.

Keep the market's price-derived graph quantities visible at both
prediction and revealed states: vertical guides drop from each price/curve
intersection to the Q axis, with bare teal demand and orange supply numbers
attached to their quantity positions. These guides/numbers follow price and
are independent of the plaza reveal. Keep the teal/orange plaza quantity lines
visible once willingness is revealed. Draw the central matched run and remaining
waiting arc separately; never join them with a diagonal across the plaza. Graph
baselines run from 0 to each side's actual Q.
Mark the unmatched willing arc on the longer side in yellow and the corresponding
min(Qd,Qs)–max(Qd,Qs) graph span in yellow. Attach a yellow “Shortage 25” or
“Excess 50” readout beside each span; the existing units are thousands of pounds.
Update these lines and counts with price, fading the yellow span/readout when
the gap reaches zero. Hide these marks with the plaza/graphs during example
close-ups and restore them on return. Prediction holds keep plaza willingness
marks, trades, and yellow gaps hidden; graph quantity guides and numbers remain
visible. Reveal yellow shortage/excess marks only with matching.
Apply this same convention to the floor, ceiling, and welfare argument. Camera
movement is available for deliberate example close-ups; the overview remains
stable during price changes and the sequence of added trades.

## Shared stage and meaning

- Use the existing 2:1 graphite stage, 2160 × 1080, 15 fps, CMU serif teaching
  text, azure question titles, gold definition terms, and existing style tokens.
  Demand/CS is teal; supply/PS is orange; price guides and price readouts are red.
  Quantity numbers follow their demand/supply colors. Payment/expenditure
  **areas** are green; total surplus is
  `TOTAL`; DWL is grey. The small exchange retains B3's orange cost and PS outline.
- Reserve one bottom band for the current question, definition, or two-option
  comparison. Remove its previous content before replacing it. Do not stack a
  definition, caption, and deliberation card there simultaneously. Use one
  question per beat rather than repeating a title question at the bottom;
  numerical/explanatory captions may use the clear bottom strip.
- Keep the market at left and its graph at right during market-wide beats.
  Keep the same 59 buyers and 100 sellers on their ranked curved arcs.
  Actual partners meet across the central diameter; willing unmatched people
  stay on the inner arcs and unwilling people at the rim. Mark every person,
  but label only selected people.
  Individual comparisons enlarge the relevant bars into a head-on view while
  hiding the other people; their allocation stays unchanged. Full-width head-on
  rows carry the individual demand/supply comparisons. For the later quantity
  argument, keep the B3 plaza and merged graph fixed: select participants and
  fill their gain strips without rearranging the scene.
- Decision close-ups use plain text, without bottom boxes or card backgrounds.
  Keep participant names through the two-by-two scene only. After that scene,
  omit names from players, headings, and captions, and omit individual role
  labels beneath close-up spheres. Retain MB/MC labels beside the bars. Names
  used later in this storyboard identify internal participants, not displayed
  text. In the two-seller comparison, place each payment/gain label beneath its
  seller. In the full-market bidding examples, place each choice beside its red
  current/proposed price line and point to that line with a short arrow. These
  are world-space, camera-facing labels, using B3's `face_camera` convention;
  remove detached footer choices. Emphasize acceptance by coloring the offer text.
- Full-width demand/supply rows retain their common local zero and dollar
  scale. On the plaza, keep short individual bars and show the common price
  on the totem and dashed graph guides. Central adjacency means actual trade;
  a check means willingness. Ranked pairing is visual bookkeeping, not a claim
  of unique partners. Prediction holds keep buyers waiting until matching is
  revealed.
- Build the demand graph from its buyers and the supply graph from its sellers,
  with narrow per-lot bars behind each straight equation line. Give both separate
  plots the same ordinary price-axis height, 2.0, independent of totem projection.
  At `1.i.graph`, translate each complete plot, including its bars, to the fixed
  right-side origin `[1.90, -0.90, 0]`. Do not morph or resize axes or curves.
  Keep the graph's own vertical axis, price ticks 4/8/12 (4 in red), and
  “Price ($/lb)” heading; remove only the duplicate second plot's axes/ticks.
  The plaza retains its own totem and $4 readout. Keep the complete graph and
  its bars unchanged through the algebra and later welfare transition.
- Quantity readouts are bare numbers at their corresponding horizontal graph
  positions: teal for demand and orange for supply. Apply this to the full-width
  rows, separate recap graphs, and merged welfare/control graph. Keep the number
  below its row or quantity axis, moving with its guide; omit detached `Qd =`
  and `Qs =` labels and the separate `Qx` counter. When quantities coincide on
  the merged graph, show one number. Actual matching or the current caption
  communicates trades. Keep quantity symbols in equations and teaching math.
- Green checks mean willing and red Xs unwilling. Central partner adjacency
  means an actual trade; do not restore the old trading circles. Use a temporary
  outline or short leader to identify a selected comparison.
- All willingness checks and red Xs are genuine world-space marks anchored above
  their own person/bar, using B3's `face_camera` convention. They follow their
  participants and scale with camera zoom/rotation, rather than staying in a
  fixed-screen overlay. Apply this to the full-width rows, curved plaza, welfare,
  and controls; retain each scene's existing willingness logic, counts, and order.
- In the uncontrolled and policy cases, (Q_x=\min(Q_d,Q_s)), with highest-MB
  buyers and lowest-MC sellers trading. This is an explicit rationing assumption
  under controls. After removing the ceiling, distinguish a permitted trade
  from completion of all willing matches. In the forced-pair experiment, mark
  the extra trade as forced: willingness checks still describe the posted
  price, and the resulting 41 trades are not a market-clearing outcome.
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
  Horizontal graph price guides are dashed, from the price axis to the curve,
  with no extension past the intersection. Separate graphs stop at their own
  willingness quantity; overlaid graphs stop at the first curve encountered.
  Reference prices and proposed policy prices follow the same convention.
  When a dashed guide changes length, keep dash lengths and gaps fixed, with
  the pattern anchored at the price axis or the guide's starting endpoint.
  Reveal or clip dashes at the moving endpoint instead of stretching the pattern.
  Apply this to the demand/supply comparisons, recap graphs, welfare quantity
  guides, and price-control guides; it changes no episode order or teaching hold.
  Keep straight equation lines and exact per-lot bars. Quarter-dollar count
  guides use exact whole-lot boundaries; policy totals sum the crowd's rectangles.
- The scene files use flat, sequential `construct()` choreography, visible
  constants, simple loops for repeated objects, and literal `self.pause('id')`
  boundaries. No per-beat helper framework. After `1.i.algebra`, section 8
  continues with the same market objects; no reset to an older scene layout.
  Use simple text fades, never paragraph or glyph morphs.

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

The pre-exercise review has a **hard ceiling of ten minutes**, with an eight-minute
working budget including the bumper, animation, explanation, and brief responses.
These are rehearsal allocations, not automatic waits. The viewer's internal play
steps are not invitations to explain every movement. The authored animation
before Q2 totals about **81 seconds**, leaving the rest of the eight-minute
budget for explanation and brief responses.

| Before Exercise Q2 | B4 beats | Budget |
|---|---|---|
| Bumper and one exchange | `0.a`, `1.a` | 1:00 |
| One bidding incentive | `1.b`, `1.b.settled` | 1:15 |
| Two sellers and switching | `1.b.two_trades.plaza`, `1.b.two_trades`, `1.b.equal_prices` | 1:15 |
| Buyers at two prices | `1.c.buyers`, `1.c.buyers.low` | 1:00 |
| Sellers at two prices | `1.c.sellers`, `1.c.sellers.high` | 1:00 |
| Both sides at $3; willingness versus trades | `1.d`, `1.e` | 1:30 |
| Transition to the exercise | `1.j` | 0:30 |
| Flex for brief responses/transitions | — | 0:30 |
| **Total before students begin Q2** | | **8:00** |

Show Amanda-Grace's explicit switching decision once, then compress the remaining
small-market bids into one smooth 1.8-second settlement of prices and partners.
Gary has no second deliberation. No repeated deliberation for each increment. Keep
CS/PS as familiar labels. If discussion runs long, shorten the exchange/bidding
commentary before cutting the willingness-versus-trades distinction.

After Q2, stages 6 and 7 finish the recap: one full-market buyer deliberation,
one seller deliberation, compressed adjustment to equilibrium, then the crossing
and algebra. Those explanations and the exercise's working time are outside the
pre-exercise eight-minute budget. Do not reveal the full market's $4 answer early.

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
   before acceptance. Keep only the plain caption “Molly receives $0.25 more”
   below the comparison; the existing and proposed prices remain on the bars.
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

## 1.b.two_trades.plaza · Establish the two-by-two market

1. Begin in B3's actual oblique plaza: phi 48°, center `[0, 0, 0.65]`, height
   10.4. Preserve the floor, people, bars, and side graphs from B3's `3.a`.
2. Animate Andrew's arrival and hold with all four people visible, Molly's
   $6.25 ask and Andrew's $4.25 ask. The plaza entrance is not skipped.

## 1.b.two_trades · Give the buyer another option

1. From the four-person plaza, use B3's head-on comparison geometry to face
   Amanda-Grace, Molly, and Andrew
   during the decision. Gary remains the unserved buyer in the underlying market.
2. Retain Amanda-Grace's solid $6.25 deal with Molly. Show her two alternatives:
   “Pay $6.25; gain $0.75” below Molly and “Pay $4.25; gain $2.75” below Andrew,
   as plain text. Title: “Stay or switch?” Hold.
3. On advance, return to the same plaza and let Amanda-Grace take Andrew's
   $4.25 offer. Then both asks and the actual partners settle in one continuous
   1.8-second move. No Gary deliberation and no per-bid replay. Caption:
   “The same incentives bring both prices together.”
4. The compressed transition uses a verified seed-34 simulation from asks
   ($6.25, $4.25), with Gary unmatched and Amanda-Grace at Andrew. Its final
   state has Gary at Andrew, Amanda-Grace at Molly, both asks $5.50. Internal
   bids determine the endpoint; they are not separate teaching beats.

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

1. Show all 59 buyers in the approved full-width head-on row. Keep the caption
   “One person = 1,000 lb. Bar height = dollars per pound.” This changes the
   unit from the preceding one-pound trades.
2. Draw the straight equation line P=12−Qd/5 through the bar-top centers; no
   stepped outline. Put its equation above the row. Keep this camera throughout
   the demand comparison, without pulling back to a separate graph.
3. At $6, end the dashed price guide at Qd=30 on that line. Show 30 checks,
   dim excluded people/bars, and highlight the marginal buyer (MB=$6). Put the
   price readout just left of the guide and a teal “30” below the row at Q=30;
   quantities are thousands of pounds. Caption: “The marginal buyer is
   indifferent at $6.” Hold “MB ≥ P”; equality is willing.

## 1.c.buyers.low · Willingness is not a trade count

1. Lower price from $6 to $3 in this same view with ease-in/ease-out motion.
   The dashed guide and its price readout descend together; the quantity label
   tracks horizontally to Q=45 as the actual willingness count reaches 45.
2. Hold “At $3, 45 buyers are willing. We have not counted trades.”
   Do not show trading circles or Qx.

## 1.c.sellers · Build quantity supplied the same way

1. Replace the buyers with all 100 sellers in their own full-width head-on row.
   Use the same camera, dollar-height, and 1,000-lb-lot convention.
2. Draw P=2+Qs/20 as a straight line through the cost-bar centers and display
   its equation. Keep the whole supply comparison in this view.
3. At $3, end the dashed price guide at Qs=20. Keep its price readout just left
   of the guide and an orange “20” below the row at Q=20. Show 20 checks, dim unwilling
   sellers, and hold “MC ≤ P.” Counts show willingness, not completed sales.

## 1.c.sellers.high · A higher price brings more sellers

1. Raise price from $3 to $6 without moving the camera, easing in and out.
   The price readout follows the guide upward and the quantity label moves
   horizontally to Q=80. Exact checks identify 80 willing sellers. Hold at Qs=80.
2. On advance, clear that caption and ease back to $3 and 20 willing sellers,
   with both labels tracking their positions, before bringing both market sides
   together. Do not stop at or label $4 as equilibrium during the sweep.

## 1.c · One price, many decisions

1. Bring buyers onto the upper/back curved edge of B3's plaza and sellers onto
   its lower/front edge, sorted by value/cost. Add the muted dashed horizontal
   ground diameter between them. Demand remains above supply at right. Begin at $3.
2. Show $3 on the vertical 0–12 price totem at the diameter's right rim endpoint:
   a red tick with an adjacent dollar readout. Keep one person = 1,000 lb; the
   short plaza bars preserve relative values, while graphs carry full scales.
3. Keep graph price guides dashed and ending at their straight equation lines.
   This is the entrance to `1.d`, not an extra teaching pause.

## 1.d · Predict the low-price result

1. Keep everyone at the outer rim, withholding plaza willingness marks and
   trades. Keep vertical graph guides from the $3 curve intersections to the
   Q axes, with teal “45” and orange “20” attached there. Hide yellow gap marks.
2. Use the existing title “At $3, who can trade?” as the single prompt. Omit
   the repeated bottom question “How much would each side trade?” Hold before
   revealing willingness.

## 1.e · Count the shortage and the actual trades

1. Willing people step to the inner arcs and receive green checks. Unwilling
   people stay at the rim with small red Xs. Retain the already-visible teal
   “45” and orange “20” at their graph quantity positions.
2. Reveal persistent teal quantity lines for the 45 willing buyers and demand's
   horizontal 0–45 span, and orange lines for the 20 sellers and supply's 0–20 span.
3. Keep those quantity lines, then move the first 20 buyers and sellers
   to matching x stations along the dashed diameter. Buyers stop just above it
   at y=+0.4 and sellers just below it at y=−0.4, forming 20 adjacent pairs.
   Center the occupied stations on the plaza. The matching and next caption
   communicate the 20 trades; add no separate Qx counter.
4. Hold “20 pairs trade. 25 willing buyers are still waiting.” The checked
   unmatched buyers, including Amanda-Grace and Gary, remain on the inner arc.
   Mark their waiting arc and demand's 20–45 graph gap in yellow, with adjacent
   “Shortage 25” readouts. Keep central matched runs separate from waiting arcs;
   the spatial difference distinguishes willingness from actual exchange.

## 1.j · Exercise B3 Q2 — before resolving equilibrium

1. After the $3 shortage has been counted at `1.e`, replace the market with an
   Exercise B3 Q2 card following [the style guide, §3](../_Style_Guide.md) and
   B2/B3: muted rounded panel, width 13, padding 0.65, gold serif heading
   “Exercise B3 | Q2,” and white body text indented 0.35. Center the equations.
2. Keep the displayed content concise and legible: pumpkin pasties at 5 galleons,
   with (P=12-Q_d/2) and (P=2+Q_s/2). Retain all four question meanings:
   quantity demanded, quantity supplied, shortage/excess and its amount, and
   the direction of price movement. Quantities are pasties. Show no answers.
3. Omit the extra incentive-question footer and oversized azure heading. Keep
   the existing `1.j` teaching hold and episode order; no exercise-file edits.
4. On advance restore the spinach market at $3, still 45/20/20. The next beat
   enacts the price incentives. The pasty problem never substitutes its data
   into the spinach simulation.

## 1.f · Recall the incentive to raise price

1. Highlight Amanda-Grace in the original 3D plaza, then bring her and served
   seller 20 (MC $3) into B3's head-on view. Title: “What would this buyer do?”
   Display MB/MC without names or individual role labels beneath the spheres.
   Clear the fixed graphs during that comparison. Place “Wait at $3: gain $0”
   beside the current red $3 line and
   “Offer $3.25: gain $3.75/lb” beside the proposed dashed red $3.25 line. Use
   world-space, camera-facing text with a short arrow from each choice to its
   price line; remove detached footer choices. Show that the served seller
   receives more if the bid is accepted. A dashed connector identifies the
   proposed switch, not an extra trade.
2. Ask “Which way does price move?” Hold with the answer still withheld.
3. On advance, accept the proposed price in the close-up: fade the waiting
   choice and its arrow, color the offer green, then clear the remaining callout
   as the camera returns to B3's
   plaza camera. Amanda-Grace joins seller 20; displaced buyer 20 returns to
   the willing inner arc. Then clear the individual proposal, restore the ranked
   snapshot, and show “Other unserved buyers have the same incentive.” Follow
   with “Shortage → price rises.”
   Raise the common price to $4 in one continuous play, moving the totem's red
   tick and readout upward. Intermediate quarter-dollar steps are not extra
   pauses. Keep counts and marks synchronized; do not narrate every threshold
   crossing or stop at each tick.
4. Keep 40/40/40 visible as the next question enters; no navigation-only stop.

## 1.g · Predict the high-price result

1. Return both sides to the outer rim and hide plaza checks, Xs, trades, and
   yellow gap marks before moving the common price to $6. Keep graph quantity
   guides and attached numbers visible throughout: verticals drop from the
   price/curve intersections to the Q axes, ending at teal “30” and orange “80.”
   Keep “At $6, who is left out?” as the single title prompt; omit the repeated
   bottom “Who would buy? Who would sell? Who actually trades?” Hold before
   revealing the plaza response and actual matching.

## 1.h · Count the excess and recall undercutting

1. Retain teal “30” and orange “80” at their graph quantity positions. Reveal
   30 buyer checks, 80 seller checks, and 30 central pairs. Keep the teal/orange plaza
   quantity lines and graph baselines visible. Fifty checked sellers remain on
   the inner arc: mark that arc and supply's 30–80 graph gap in yellow, with
   adjacent “Excess 50” readouts.
2. Highlight Andrew among the unserved sellers and Gary among the served buyers.
   Show the same B3 head-on inspection view, titled “What would this seller do?”
   Display only “MC $4” and “MB $6” beside the bars, without names or individual
   role labels beneath the spheres. The actual plaza returns before Andrew
   replaces seller 30 beside Gary.
   Keep Gary in the same central slot; seller 30 returns to the willing inner arc.
   Place “Keep $6: gain $0” beside the current red $6 line and
   “Ask $5.75: gain $1.75/lb” beside the proposed dashed red $5.75 line. Use
   world-space, camera-facing choice labels and short arrows to their respective
   price lines; remove detached footer choices. Gary would also gain by paying
   less. Ask “Which way does price move?” Hold.
3. On advance, fade the keep-price choice and its arrow, color the accepted
   offer green, and clear the remaining callout as the camera returns to the
   plaza. Briefly accept the proposed switch, then clear it and show “Other unserved sellers have the same incentive.” Follow with “Excess → price falls.” Move the
   common price to $4 in one play, lowering the totem's red tick and readout
   while retaining the counts throughout.

## 1.i · State the two parts of equilibrium together

1. Park on 40 buyer–seller pairs meeting across the dashed diameter, with buyers
   above and sellers below. Keep green checks and the totem at $4. Show “40” at
   the quantity position on each separate graph; matching communicates 40 trades.
   Unwilling people remain at the rim with red Xs; no willing
   person remains unmatched on the inner arcs. Teal/orange quantity lines
   remain visible; the yellow gap marks and readouts fade at zero.
2. Fade in the title “Equilibrium” and one line at the standard bottom definition
   position: “Equilibrium: no willing buyer or seller is left without a trade.
   Q_s = Q_d.” Color only “Equilibrium” gold; body and formula remain white.
   Omit “=40” from this definition; the graph's quantity numbers remain.
   Use simple fades for the title and definition, without glyph transforms.
3. Point to both parts on this same frame: the matching counts,
   the absence of willing people left without trades, and the dim people whose
   MB/MC keeps them out at $4. Hold before testing the pressure at nearby prices.

## 1.i.stability · Test why the price holds

1. Keep $4 and the 40 trades as the faint reference. Show a dashed proposed
   $4.25 line on each graph, with a red “$4.25” label just left of each line.
   Temporarily hide each nearby $4 axis tick so the labels do not overlap.
   Omit the repeated bottom price-hold question. Hold without proposed-price
   count answers.
2. On advance, fade the proposed labels and lines as price moves to $4.25:
   Qd=38, Qs=45, Qx=38. Fade in the existing excess caption. Show seven willing sellers
   without circles. Sellers 39–40 lose trades; sellers 41–45 become newly
   willing but unserved. Keep the quantity lines and mark the waiting sellers'
   arc and supply's 38–45 graph span in yellow, labeled “Excess 7.” Caption:
   “Seven willing sellers have no buyer. They can undercut.” Restore $4 and
   fade the yellow gap marks/readouts at zero.
3. Test $3.75 in the same short sequence: Qd=41, Qs=35, Qx=35. Show six willing
   buyers without circles. Buyers 36–40 lose trades; buyer 41 is newly willing.
   Keep the quantity lines and mark the waiting buyers' arc and demand's 35–41
   graph span in yellow, labeled “Shortage 6.” Caption: “Six willing buyers have
   no seller. They can offer more.” Restore $4 and the 40 trades, fading the
   yellow gap marks/readouts at zero.
4. Park at `1.i.stable` on “Above $4: excess. Below $4: shortage.” before the
   graph transition. Use staircase count guides for these tests: the exact
   whole-lot counts differ from smooth-curve intersections at quarter dollars.
   Keep the cause visible as willing people left out, not just the marginal
   pair refusing an unaffordable price. Use plain fades for all caption changes
   in this beat—excess, shortage, and stable conclusion—with no paragraph morphs.
   Keep their existing wording and the teaching holds unchanged.

## 1.i.stable · Keep the conclusion visible

1. End the two deviation tests back at $4 and 40 trades.
2. Hold “Above $4: excess. Below $4: shortage.” This is the stable endpoint
   from which the graph stage begins.

## 1.i.graph · Recognize the same condition at the crossing

1. Retain the settled crowd, horizontal meeting line, and price totem with its
   own $4 readout. Simply translate the two complete graphs, carrying their
   narrow lot bars and straight curves, to the fixed right-side origin
   `[1.90, -0.90, 0]`. Both already use price-axis height 2.0; no axes or curve
   morphing/resizing. Keep one ordinary graph price axis with ticks 4/8/12
   (4 in red), the “Price ($/lb)” heading, and the dashed $4 graph guide. Remove
   only the second plot's duplicate axes/ticks. The lines cross at Q=40, P=$4,
   matching the crowd's counts without sharing the totem's position.
2. Title: “Why does the crossing give equilibrium?” Highlight one shared “40”
   at the graph's quantity position and the crossing. Keep the people visible so this is another
   representation of the same result, not a second definition. Hold.

## 1.i.algebra · Make the equality explicit

1. Fade the plaza and totem while leaving the already-complete merged graph,
   its price axis, and lot bars unchanged at right. Add no replacement axis.
   Use the vacated left half for the arithmetic. Show the two equations with
   their subscripts: (P=12-Q_d/5) and (P=2+Q_s/20).
2. Show (Q_d=Q_s=Q) before setting their right-hand sides equal. Then reveal
   (12-Q/5=2+Q/20), (10=Q/4), and (Q^*=40) in that order, with no extra
   arithmetic pauses. Substitute into supply to show (P^*=2+40/20=4).
3. Carry the starred pair to the crossing. Hold “Same price; equal quantities.”
   This is a short explanation of what the algebra means; leave Exercise Q1
   completed. Hold on the solved frame. The welfare stage restores the same
   actual crowd and merged-graph objects at $4; it does not replay the algebra.

## 2.a · Show the market's benefits

1. After the algebra, fade its text and restore the same curved plaza, totem,
   partners, and independent merged graph at $4 and 40 trades. Reuse these
   objects; do not clear and rebuild the earlier welfare layout.
2. Show CS directly in teal benefit-minus-price regions and PS in orange
   price-minus-cost regions, retaining the graph's narrow lot bars and curves.
   Label the familiar benefits close to their regions: **CS $156,000** and
   **PS $39,000**. Keep the market-wide frame stable.
3. Hold `2.a` on the benefits generated by the actual participants. This is a
   callback to B1/B2, not a new surplus construction or a planner problem.

## 2.b · Sum the gains

1. Keep the same allocation and regions. Show **Total surplus = PS + CS**,
   with PS orange, CS teal, and the words/equality white, then **$195,000**.
2. Use simple fades and attached region labels; omit extra component formulas,
   cancellation arithmetic, named players, and a separate pair-20 payment story.
3. Hold `2.b` with the full market's total gain visible. This benchmark remains
   the comparison for each policy and for the final harmful-trade experiment.

## 3.a · Impose a binding price floor first

1. Move the posted price from $4 to a binding floor of **$6**, with the same
   totem, graph, and participant objects. Identify the legal minimum beside its
   red price guide. Do not introduce government purchases.
2. Show teal **30** and orange **80** at the graph quantities; only 30 pairs
   meet in the center. Keep the persistent teal/orange quantity lines on the
   plaza and graph. Fifty willing sellers wait on the inner arc.
3. Mark that waiting arc and the graph gap 30–80 in yellow with attached
   **Excess 50** labels. Hold `3.a`; the quantity labels are thousands of pounds.

## 3.b · See the floor's lost gains

1. Keep the same 30 actual trades and their filled surplus rectangles. Expose
   the forgone positive gains of pairs 31–39 in grey; pair 40 has zero gain.
2. Show **TS $183,750** and **DWL $11,250** beside the relevant gain/loss regions.
   CS is $87,000 and PS $96,750 if needed in the existing benefits display;
   avoid a detached row of redundant totals.
3. Hold `3.b` on the missing trades. The loss is the benefit that those trades
   could add above their costs, not the yellow count of all excess sellers.

## 3.c · Inspect one beneficial trade blocked by the floor

1. Select ranked pair **35**: buyer MB **$5**, seller MC **$3.75**. Bring these
   actual participants into a B3-style head-on close-up, hiding the rest of the
   plaza and graph during inspection. Keep world-space labels beside the bars.
2. The buyer cannot pay the legal $6 minimum. Show the potential gain between
   MB and MC: **$1.25/lb × 1,000 lb = $1,250**. A price between $3.75 and $5
   could benefit both, but it lies below the floor.
3. Attach the blocked-price indication to the proposed price/region; no detached
   question paragraph. Hold `3.c`, then return the same untraded pair to the
   waiting arcs. No surplus is realized by this blocked proposal.

## 4.a · Replace the floor with a binding ceiling

1. Remove the floor and replace it with a **$3 ceiling**. Pass through the
   existing $4 market without adding a teaching hold, then show the ceiling's
   legal maximum beside its red price guide.
2. The same graph shows teal **45** and orange **20**. Twenty pairs trade;
   25 willing buyers remain on the inner arc. Keep the colored quantity lines,
   marking the waiting buyers and graph gap 20–45 in yellow: **Shortage 25**.
3. Hold `4.a`. Preserve the established price, matching, and graph vocabulary.

## 4.b · See the ceiling's lost gains

1. Keep the 20 traded lots filled and expose missing positive gains from pairs
   21–39 in grey. Pair 40 again contributes zero.
2. Show **TS $147,500** and **DWL $47,500** next to the regions. The underlying
   components are CS $138,000 and PS $9,500; this is the same exact crowd.
3. Hold `4.b` on the missing mutually beneficial trades, with the curved plaza
   and merged graph stable. A lower price does not establish that buyers as a
   group gain when the set of trades also changes.

## 4.c · Inspect one beneficial trade blocked by the ceiling

1. Inspect ranked pair **25**: buyer MB **$7**, seller MC **$3.25**. Enlarge
   those same bars in the familiar head-on view. Hide the rest of the scene;
   use MB/MC labels without names and keep labels attached.
2. The seller will not supply at the legal $3 maximum. The pair could create
   **$3.75/lb × 1,000 lb = $3,750** of gain at a mutually acceptable price,
   including $4, but the ceiling prevents it.
3. Hold `4.c` with the blocked pair and its potential gain visible. Keep this
   close-up for the next step, when the ceiling is lifted and the pair trades.

## 5.a · Permit that missing trade

1. Lift the ceiling and post **$4** while still in pair 25's close-up. Visibly
   accept the proposed trade there, then return the same participants to the
   plaza's center line. The other already-realized trades stay selected. This
   is the first permitted addition, not yet the full matching.
2. Fill that pair's formerly missing gain. Its **$3,750** raises total surplus
   from $147,500 to **$151,250**; there are now 21 actual trades, specifically
   pairs 1–20 plus pair 25, rather than the first 21 ranked pairs.
3. Hold `5.a` in the restored overview with 21 central pairs and TS $151,250.
   Price-derived graph quantities reflect willingness at $4; central matching
   shows which trades have actually occurred so far.

## 5.b · Allow the remaining beneficial trades

1. In one smooth sequence, admit the remaining positive-gain pairs through
   pair 39 and include indifferent pair 40 under the inclusive convention.
   Do not replay every exchange or create extra teaching stops.
2. Fill each added lot's gain and shrink the missing-gain region. Finish at
   **40 pairs**, price **$4**, and **TS $195,000**. The willingness quantities
   coincide at 40; no willing participant is left unmatched.
3. Hold `5.b` on the same stable plaza and graph. The highest-value buyers and
   lowest-cost sellers participate; the actual partner identities need not be
   unique for the aggregate gains to be maximal.

## 5.c · Inspect the zero-gain boundary

1. Identify pair **40**, with MB **$4** and MC **$4**, in the existing model.
   Keep the quantity and total unchanged.
2. Show that this pair contributes **$0**. Hold `5.c`: 39 and 40 trades have
   the same maximum total surplus; the inclusive willingness convention uses 40.
3. Do not claim that every change in quantity or pairing must lower welfare.

## 5.d · Force one trade beyond the boundary

1. Title: “Force one trade too many.” Force pair **41** to trade: buyer MB
   **$3.80**, seller MC **$4.05**. Clearly identify this as forced, preserving
   the posted-price willingness marks and quantities. In the overview, show
   41 central pairs and total surplus falling from $195,000 to **$194,750**.
2. Bring that same pair into the selected head-on close-up. Show cost exceeding
   benefit by **$0.25/lb**, with a red loss bracket and attached **Loss $250**
   label. Hide the rest of the plaza and graph during this inspection.
3. Hold `5.d` in the forced pair's close-up. Return to the overview on advance,
   before undoing the harmful trade. This shows why simply increasing trade
   cannot improve welfare indefinitely.

## 5.e · Undo the harmful trade and name the result

1. Remove forced pair 41 and its negative realized gain. Restore the original
   40-pair market and **TS $195,000**, with no remaining positive-gain trade
   left out and no negative-gain trade included.
2. Name the **First Welfare Theorem** using the course's conditional statement:
   competitive markets with no externalities maximize welfare when all relevant
   benefits and opportunity costs are counted. Keep the conditions beside the
   model, with one concise conclusion and simple text fades.
3. Hold `5.e`. The demonstrated result is maximal total gains in this specified
   competitive market; it does not select unique partners, resolve distribution,
   or establish that every market satisfies the stated conditions.

## 6.exercise_floor · Exercise B4 Q2

1. Place the floor exercise after the completed argument, before the ceiling
   exercise. Use the sheet's 9-galleon floor and original prompts: quantity
   exchanged, producer surplus, deadweight loss, and a floor of 6.
2. Use the approved muted rounded panel, gold serif exercise heading, white
   concise body, and centered equations. Show no answers. Hold
   `6.exercise_floor`, then restore the same spinach scene.

## 6.exercise_ceiling · Exercise B4 Q1

1. Use the original pasty equations and 5-galleon ceiling with its prompts:
   quantity exchanged, CS, PS, DWL, and the graph with shaded regions.
2. Use the same exercise-card styling, without extra repeated questions or
   answers. Hold `6.exercise_ceiling`, then restore the spinach scene.
3. The pasty model's continuous areas never replace the exact spinach crowd's
   welfare totals.

## 7.a · Close with the result and its scope

1. Retain the $4, 40-pair market with total surplus $195,000.
2. Briefly distinguish maximal gains from distribution and other policy aims,
   while retaining the competitive/no-externality conditions already stated.
3. Hold `7.a` without introducing another policy or replaying the argument.

## Implementation and review boundaries

- Preserve all **22 opening holds** and the entire sequence through
  `1.i.algebra`, including the eight-minute pre-Q2 budget. The reordered section
  8 adds the 16 listed holds for a total of **38**.
- Keep the exact $3/$4/$6 willingness counts 45/20, 40/40, and 30/80; actual
  trade counts are 20/40/30 in the settled policy/market states. During permitted
  additions and the forced trade, distinguish the selected allocation from
  willingness at the posted price.
- Use the same crowd, short bars, checks/Xs, central matching, price totem,
  independent merged graph/lot bars, and persistent quantity/gap marks throughout
  the back half. World text follows the camera. Labels sit beside the things
  they describe, and text changes use fades.
- Preserve the 39/40 maximum-surplus tie and the exact blocked-pair gains.
  No government purchases, unique-matching claim, or extra planner-sorting
  episode is included in this sequence.
- Tests and renders for this rebuild are deferred at Taylor's request. Earlier
  validation of the superseded back half is not validation of this new order.
- Only the canonical animation and this storyboard belong to the update. Notes,
  exercises, shared assets, B3 files, and stale snapshots remain unchanged.

## Notes reconciliation for Taylor/Fable

- Taylor's latest explicit order above supersedes both the earlier planner-first
  animation and ceiling-first notes for this build. Author-owned notes remain
  untouched; this storyboard records the animation decision.
- CS/PS stay familiar callbacks. The first theorem argument now runs through
  blocked mutually beneficial trades and the harmful extra trade, rather than
  a separate planner-first allocation exercise or payment-cancellation proof.
- Exact policy arithmetic is unchanged: floor TS $183,750 / DWL $11,250;
  ceiling TS $147,500 / DWL $47,500. Lost gains concern unrealized beneficial
  lots, not all unmatched people.
- The theorem concerns maximal total gains under its stated conditions. A
  zero-gain boundary trade and alternative partner pairings can leave gains
  unchanged; efficiency alone does not settle every policy question.
