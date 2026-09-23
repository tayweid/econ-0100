# Episode B4 | First Welfare Theorem | Storyboard

B3-based animation implementation · 2026-09-22.

Latest authorized order: **market benefits (CS/PS → total surplus) → binding
floor → binding ceiling → permit a blocked trade → all beneficial trades →
force one harmful trade → undo it and state the conditional welfare result**.
This explicitly supersedes the earlier planner-first draft, the ceiling-first
notes, and the animator note's frozen-order instruction. Keep the entire opening
through `1.i.algebra` in its existing order, with the latest decision-close-up
and moving ground-segment refinements below. The latest visual direction supersedes the
back-half plaza-reuse requirement: after the algebra, use **one large graph**
as the overview. Selected MB/MC bars expand directly from that graph into the
preferred two-person comparison, without restoring the plaza or totem. Keep
the economic order above.

The review before Exercise B3 Q2 remains **under ten minutes, targeting eight**.
The exercise interrupts the $3 recap before equilibrium is resolved. The later
welfare argument uses the exact crowd; exercise markets remain separate.
Lecture notes, exercise files, and the older Typst storyboard are author-owned.

## Runnable animation and holds

Run **`maniml 03_B4.py B4`** for the canonical complete lesson. The code stays
flat and sequential at 15 fps. The first seven code sections retain their
**22 named holds**; section 8 now has **18 named holds**, including the two
selected-lot holds before expansion, for **40 total** with the exercise placement below. Section 8 presents the welfare
argument on one large, stable graph. Discrete lot economics stay the same,
while the screen omits aggregate dollar totals and the recap's crowd displays.

| Code section | Content | Named holds |
|---|---|---|
| 1–7 | Existing exchange, bidding, two trades, demand, supply, equilibrium, graph/algebra | `0.a` through `1.i.algebra` (22 unchanged) |
| 8 | Market benefits | `2.a`, `2.b` |
| 8 | Binding floor, lost gains, select/inspect blocked pair | `3.a`, `3.b`, `3.c.select`, `3.c` |
| 8 | Binding ceiling, lost gains, select/inspect blocked pair | `4.a`, `4.b`, `4.c.select`, `4.c` |
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
and demonstrate why forcing the next lot lowers total surplus. The graph's
realized and missing gain areas carry the argument; the final theorem names
the result and its conditions.

Keep the approved opening intact. Its 3D plaza and recap graph conventions
below apply through the algebra. The welfare sequence instead uses a single
large graph: teal CS and orange PS labels inside their own areas, then a unified
purple total-surplus region. Grey marks lost gains and red marks a harmful lot.
Use attached labels and simple fades, without arrows, dashboards, aggregate
dollar totals, or repeated questions. First select the two MB/MC bars for a
missing lot on the graph, then expand those bars into a clear two-person figure.
Legal and mutually beneficial price intervals make the blocking restriction
visible. Return to the same graph overview; do not restore the crowd plaza.

## Opening staging — same sequence through the algebra

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
  These plaza conventions apply to the recap only. Do not restore the plaza,
  people, or totem after the algebra; the back half uses one large graph.
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
- `fixed`, `add_market_objects`, and the original text billboard adapter are
  reused from B3. They handle renderer/label behavior, not teaching choreography.
  No shared asset or engine code is changed.

## Curved-plaza convention — recap only

Throughout the full-market recap, short floating bars are value cues; the graphs retain
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
are independent of the plaza reveal. Once willingness is revealed, show a
short teal/orange ground segment attached to each willing person's position.
Every segment travels with its person between rim, inner arc, and center; do
not connect players into a continuous span or draw a diagonal across the plaza.
Graph baselines remain unchanged, running from 0 to each side's actual Q.
Mark each unmatched willing person with a short yellow ground segment that
also moves with them; retain the corresponding min(Qd,Qs)–max(Qd,Qs) graph span
in yellow. Keep the nearby yellow “Shortage 25” or “Excess 50” readouts; units
remain thousands of pounds. Update the segments and counts with price, fading
the yellow segments, graph span, and readout when
the gap reaches zero. Hide these marks with the plaza/graphs during example
close-ups and restore them on return. Prediction holds keep plaza willingness
marks, trades, and yellow gaps hidden; graph quantity guides and numbers remain
visible. Reveal yellow shortage/excess marks only with matching.
These willingness, matching, and yellow-gap displays stop with the recap.
The welfare graph uses a single actual-quantity marker during the policy beats,
without shortage/excess labels, gap brackets, or a second willingness display.
From `5.a`, its active price/quantity guides stay hidden.

## Visual conventions and economic meaning

- Use the existing 2:1 graphite stage, 2160 × 1080, 15 fps, CMU serif teaching
  text, azure question titles, gold definition terms, and existing style tokens.
  Demand/CS is teal; supply/PS is orange; price guides and price readouts are red.
  Quantity numbers follow their demand/supply colors. Payment/expenditure
  **areas** are green; total surplus is
  `TOTAL`; DWL is grey. The small exchange retains B3's orange cost and PS outline.
- Put narration, principle, and definition footers at the centered bottom,
  with margin **0.05** and text scale **0.7443**, following the style guide.
  Use this baseline for all standalone bottom captions, including the seller's
  gain narration in `1.f` and excess narration in `1.h`; do not lay them over
  the plaza. Replace the previous footer before showing the next. For an
  intentional multiline footer, such as theorem plus conditions, preserve the
  vertical stack and anchor the whole group at the bottom so lines do not overlap.
  Keep model values, price/choice labels, and quantity-gap labels attached to
  their visual features. Use one question per beat, without repeating the title.
  In `1.d`–`1.h`, titles give context: “A low price: $3” or “A high price: $6.”
  Put each question in yellow at the same bottom margin/scale, replacing any
  narration there. Remove the question on acceptance. Before the common price
  changes, replace the fixed-price context title with “Price adjustment.”
- During the recap, keep the market at left and its graph at right.
  Keep the same 59 buyers and 100 sellers on their ranked curved arcs.
  Actual partners meet across the central diameter; willing unmatched people
  stay on the inner arcs and unwilling people at the rim. Mark every person,
  but label only selected people.
  Individual comparisons enlarge the relevant bars into a head-on view while
  hiding the other people; their allocation stays unchanged. Full-width head-on
  rows carry the individual demand/supply comparisons. After the algebra,
  remove the crowd presentation and keep one large welfare graph fixed.
- Decision close-ups use plain text, without bottom boxes or card backgrounds.
  Keep participant names through the two-by-two scene only. After that scene,
  omit names from players, headings, and captions, and omit individual role
  labels beneath close-up spheres. Retain MB/MC labels beside the bars. Names
  used later in this storyboard identify internal participants, not displayed
  text. In the two-seller comparison, place each payment/gain label beneath its
  seller. In the full-market bidding examples, place each choice beside its red
  current/proposed price line and point to it with a short arrow. Keep both
  alternatives visible, with arrow paths clear of the bars. These
  are world-space, camera-facing labels, using B3's `face_camera` convention;
  remove detached footer choices. Emphasize acceptance by coloring the offer text.
  In the full-market buyer/seller deliberations, put a yellow world-space ring
  around the deciding person's orb and include the incumbent trading partner.
  Keep the actual red price floating at its dollar height over the existing
  pair; add no ground match connector or ground price. The counterparty's bar
  and MB/MC label sit with that pair. A dashed proposed price spans the deciding
  actor and counterparty. Acceptance moves the counterparty's bar/label and
  solid price to the new pair as the incumbent steps aside. Perform this switch
  only in the close-up, then
  return to the untouched full crowd for one smooth common-price change to $4.
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
  The plaza retains its own totem and $4 readout through this recap bridge.
  Keep the graph stable during the algebra; the next section establishes the
  large graph used for the entire welfare argument.
- Quantity readouts are bare numbers at their corresponding horizontal graph
  positions: teal for demand and orange for supply. Apply this to the full-width
  rows and recap graphs. Keep the number
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
  fixed-screen overlay. Apply this to the opening's full-width rows and curved
  plaza; no willingness marks appear in the graph-only welfare sequence.
- In the uncontrolled and policy cases, (Q_x=\min(Q_d,Q_s)), with highest-MB
  buyers and lowest-MC sellers trading. This is an explicit rationing assumption
  under controls. After removing the ceiling, distinguish a permitted trade
  from completion of all willing matches. In the forced-pair experiment, mark
  the extra lot as forced. The resulting 41 trades are not a market-clearing
  outcome. Policy quantity markers denote actual selected trades; the later
  additions are shown directly in the realized-gain area without counters.
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
  boundaries. No per-beat helper framework. Section 8 uses one stable large
  graph overview with selected MB/MC bars expanding into a two-person figure;
  no plaza restoration or unrelated inset diagram.
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
2. Title: “A low price: $3.” Put “Who can trade?” in yellow at the standard
   bottom footer position (scale 0.7443, margin 0.05). Hold before revealing
   willingness; show no other footer simultaneously.

## 1.e · Count the shortage and the actual trades

1. Willing people step to the inner arcs and receive green checks. Unwilling
   people stay at the rim with small red Xs. Retain the already-visible teal
   “45” and orange “20” at their graph quantity positions.
2. Reveal short teal ground segments under the 45 willing buyers and orange
   segments under the 20 willing sellers. Keep demand's horizontal 0–45 and
   supply's 0–20 graph baselines unchanged.
3. Let each ground segment follow its person as the first 20 buyers and sellers move
   to matching x stations along the dashed diameter. Buyers stop just above it
   at y=+0.4 and sellers just below it at y=−0.4, forming 20 adjacent pairs.
   Center the occupied stations on the plaza. The matching and next caption
   communicate the 20 trades; add no separate Qx counter.
4. Keep the title “A low price: $3.” Replace “Who can trade?” with the existing
   narration “20 pairs trade. 25 willing buyers are still waiting.” Hold with
   the checked unmatched buyers, including Amanda-Grace and Gary, on the inner arc.
   Give each unmatched willing buyer a short yellow ground segment following
   that person, and keep demand's 20–45 graph gap yellow with nearby “Shortage 25”
   readouts. The marks stay local to people rather than connecting their positions.

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

1. Highlight the deciding buyer (internally buyer 25) and seller 20 (MC $3),
   then bring them into B3's head-on view. Keep the context title “A low price: $3.”
   Put a yellow world-space circular ring around the deciding buyer's orb.
   Arrange a compact three-person figure: deciding buyer left, seller center,
   incumbent buyer 20 right. Include the incumbent's **MB $8** bar and label.
   Seller 20 already trades with that buyer. Put the seller's MC bar and label
   with this right-hand pair, and keep the solid red **$3** price floating at
   dollar height over them.
   Add no ground match connector or ground price. Display no names or individual
   role labels.
2. Clear the fixed graphs during inspection. Keep MB/MC labels beside the bars.
   Use two world-space camera-facing choices: “Wait at $3: gain $0” with a
   short arrow to the current solid price, and “Offer $3.25: gain $3.75/lb” with
   a short arrow to the proposed dashed price spanning buyer and seller. Keep
   both arrows visible and route them clear of the three bars. Any seller-gain
   narration uses the bottom footer first; replace it with the yellow question
   “What would this buyer do?” at the existing `1.f` decision hold. Keep one
   footer at a time, at scale 0.7443 and bottom margin 0.05.
3. On advance, remove the yellow question and accept in the close-up: move
   the seller's MC bar/label to the
   deciding buyer's new pair and solidify their floating **$3.25** price at its
   dollar height. Let the incumbent buyer step aside with their MB bar/label.
   Fade the waiting choice and its arrow, clear the proposal arrow as its price
   is accepted, and color the offer green.
   Clear the close-up callouts and return to the untouched full-crowd snapshot.
   Do not replay the switch on the plaza or animate a rollback there.
4. Change the title to “Price adjustment.” Show “Other unserved buyers have
   the same incentive,” followed by “Shortage → price rises.” Raise the common
   price to **$4** in one smooth
   play, with the totem, counts, willingness marks, and per-person ground segments
   synchronized. Finish at 40/40/40; no extra teaching or navigation stop.

## 1.g · Predict the high-price result

1. Return both sides to the outer rim and hide plaza checks, Xs, trades, and
   yellow gap marks before moving the common price to $6. Keep graph quantity
   guides and attached numbers visible throughout: verticals drop from the
   price/curve intersections to the Q axes, ending at teal “30” and orange “80.”
   Title: “A high price: $6.” Put “Who is left out?” in yellow at the standard
   bottom footer position. Hold before revealing the plaza response and actual
   matching; do not show another footer or repeat the question in the title.

## 1.h · Count the excess and recall undercutting

1. Retain teal “30” and orange “80” at their graph quantity positions. Reveal
   30 buyer checks, 80 seller checks, and 30 central pairs. Short teal/orange
   ground segments move with each willing person. Fifty unserved sellers keep
   local yellow segments; supply's 30–80 graph gap and “Excess 50” remain yellow.
   Keep the title “A high price: $6.” Replace “Who is left out?” with the
   existing excess narration at the standard bottom footer position, clear
   of the plaza; the quantity-gap labels stay attached.
2. Inspect the deciding seller (internally seller 40) with buyer 30 in the
   familiar head-on view, retaining “A high price: $6” as the context title.
   Ring the deciding seller's orb in yellow. Mirror the compact figure: incumbent seller 30 left,
   buyer center, deciding seller right. Include the incumbent's **MC $3.50**
   bar and label. Buyer 30 already trades with that seller. Move the buyer's MB
   bar/label to this left-hand pair and keep the solid red **$6** price floating
   at dollar height over them. Add no ground match connector or ground price.
   Show MB/MC labels without names or individual role labels beneath the spheres.
3. Use two world-space choices: “Keep $6: gain $0” with a short arrow to the
   current solid price, and “Ask $5.75: gain $1.75/lb” with a short arrow to
   the proposed dashed price spanning seller and buyer. Keep both arrows
   visible and clear of all three bars. Replace the excess narration with the
   yellow footer “What would this seller do?” at the existing `1.h` decision
   stop, using scale 0.7443 and bottom margin 0.05. On advance, remove that
   question, move the buyer's MB bar/label to the new pair, and solidify the
   floating **$5.75** price at dollar height, and let the incumbent seller step
   aside with their MC bar/label. Fade the keep-price choice and its arrow,
   clear the proposal arrow as its price is accepted, and color the offer green.
4. Clear the close-up and return to the untouched full crowd, without a second
   plaza switch or rollback. Change the title to “Price adjustment.” Show
   “Other unserved sellers have the same incentive,” followed by “Excess → price falls.” Move the common price to
   **$4** in one smooth play, retaining synchronized counts and moving ground
   segments. No new hold is introduced.

## 1.i · State the two parts of equilibrium together

1. Park on 40 buyer–seller pairs meeting across the dashed diameter, with buyers
   above and sellers below. Keep green checks and the totem at $4. Show “40” at
   the quantity position on each separate graph; matching communicates 40 trades.
   Unwilling people remain at the rim with red Xs; no willing
   person remains unmatched on the inner arcs. Teal/orange per-person ground
   segments and graph baselines remain visible; the yellow gap marks and readouts fade at zero.
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
   willing but unserved. Keep the local quantity segments and mark each waiting
   seller's ground segment and supply's 38–45 graph span yellow, with “Excess 7.” Caption:
   “Seven willing sellers have no buyer. They can undercut.” Restore $4 and
   fade the yellow gap marks/readouts at zero.
3. Test $3.75 in the same short sequence: Qd=41, Qs=35, Qx=35. Show six willing
   buyers without circles. Buyers 36–40 lose trades; buyer 41 is newly willing.
   Keep the local quantity segments and mark each waiting buyer's ground segment
   and demand's 35–41 graph span yellow, with “Shortage 6.” Caption: “Six willing buyers have
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
2. Keep the title **Equilibrium**. Highlight one shared “40” at the graph's
   quantity position and the crossing, with the people still visible. Restore
   the same bottom definition used at `1.i`: “Equilibrium: no willing buyer or
   seller is left without a trade. Q_s = Q_d.” Color the term gold and the rest
   white. Hold with this definition, without a “Same price, same quantity” caption.

## 1.i.algebra · Make the equality explicit

1. Keep the title **Equilibrium**. Fade the plaza, totem, and bottom definition
   while leaving the already-complete merged graph, its price axis, and lot bars
   unchanged at right. Add no replacement axis.
   Use the vacated left half for the arithmetic. Show the two equations with
   their subscripts: (P=12-Q_d/5) and (P=2+Q_s/20).
2. Show (Q_d=Q_s=Q) before setting their right-hand sides equal. Then reveal
   (12-Q/5=2+Q/20), (10=Q/4), and (Q^*=40) in that order, with no extra
   arithmetic pauses. Substitute into supply to show (P^*=2+40/20=4).
3. Carry the starred pair to the crossing. Keep the existing numeric result
   footer: “40,000 pounds at $4 per pound.”
   This is a short explanation of what the algebra means; leave Exercise Q1
   completed. Hold on the solved frame. The welfare stage restores the same
   actual crowd and merged-graph objects at $4; it does not replay the algebra.

## Back-half graph convention

After `1.i.algebra`, establish one large graph for the rest of the economic
argument. This supersedes any earlier forward-looking instruction to restore
plaza objects at the welfare transition. Keep all earlier behavior unchanged.

- Keep demand and supply curves and a clear price/quantity scale. Exact
  adjacent lot cells form a visually continuous filled area; do not display
  narrow lot bars, except the selected-lot outlines. CS is teal and PS orange,
  with labels **inside** their colored regions.
  Do not attach dollar totals, arrows, or extra readout rows to those labels.
- Combine CS and PS into **one purple total-surplus area**, labeled inside the
  area. Keep realized gains purple, forgone positive gains grey, and a forced
  negative-gain lot red. Do not continue displaying CS/PS splits after combining.
- During the floor/ceiling beats, use **one price guide**, stopping at the
  short-side curve, and **one actual quantity tick/drop**. From `5.a` onward,
  keep both active guides hidden; the ordinary 40 axis tick remains visible.
  Omit willingness counters, yellow shortage/excess spans, dashboard totals,
  and all aggregate dollar amounts from the welfare visuals.
- Keep the overview graph stable, with **P*=4** at the crossing and a drop to the ordinary
  **40** quantity tick as equilibrium references. Identify lost trades from actual Q to Q*=40, not the entire
  shortage/excess range. Select two MB/MC bars inside that lost-trade range
  before expanding those same bars into a two-person close-up. Give the two
  people teal/orange materials without names; do not restore a crowd or plaza.
- In the policy close-up, put the red floor/ceiling beside a vertical price
  axis. Show the legal price interval in green: floor 6 upward with continuation,
  or ceiling 0–3. Put the mutually beneficial interval MC–MB in purple beside
  the axis and mark the mutually acceptable **$4**. The disjoint intervals show
  that the restriction blocks a still-beneficial trade. Caption: **Both gain
  at $4; that price is illegal.**
- The forced negative lot remains an exact red strip on the overview with small
  teal/orange endpoint dots and an adjacent “MC > MB” label. Never exaggerate
  its area or add individual gain/loss dollars.
- Aggregate welfare arithmetic and allocations remain internal. The selected
  pair retains the preferred figure's lost-surplus bracket ($1,250 or $3,750). Maintain all 40 holds
  and the accepted economic order. Use simple text fades and one concise prompt.

## 2.a · Show the market's benefits

1. At price $4 and quantity 40, show the familiar teal CS and orange PS regions
   on the large graph. Put only **CS** and **PS** inside their respective areas.
2. Hold `2.a` on this simple callback to B1/B2. Do not show aggregate dollar
   totals, arrows, a separate table, or a detailed surplus construction.

## 2.b · Sum the gains

1. Unite the realized CS/PS fills into a single **purple total-surplus region**
   between benefit and cost for the traded lots. Place **Total surplus** inside.
2. Show only the simple bottom definition **Total surplus = PS + CS**, without
   expanding either component. Hold `2.b` on the unified purple area, then fade
   the definition before the floor. No payment demonstration, numerical total,
   or detached legend is needed.

## 3.a · Impose a binding price floor first

1. Move to a binding floor of **$6** on the same graph. Identify the floor beside
   its red price guide, which ends at the demand curve at **30**.
2. Move the single actual-quantity tick/drop to 30 and retain purple gains only
   on those traded lots. Hold `3.a`. Do not show excess-supply brackets or the
   separate willingness quantity 80; no government purchases occur.

## 3.b · See the floor's lost gains

1. Keep the first 30 lots' realized gains purple. Show the missing positive-gain
   lots 31–39 in grey; lot 40 has zero gain.
2. Retain the **P*=4** marker and drop to quantity **40**. Mark **Q=30 to Q=40** on the
   quantity axis, labeled **Lost trades**. This is not the
   entire excess-supply range; positive missing gains are lots 31–39 and 40 is zero.
3. Label the grey area **DWL** nearby and hold `3.b`, without dollar-total rows.

## 3.c.select · Select a trade lost from equilibrium

1. Select lot **35** within the graph's marked 30–40 lost-trade range. Highlight
   its **two** MB/MC bars, with heights **$5** and **$3.75**.
   Add the numerical MB/MC labels in the close-up.
2. Hold `3.c.select` so the class can locate this specific missing trade before
   the bars expand. Keep the equilibrium reference and lost-trade range readable.

## 3.c · Inspect one beneficial lot blocked by the floor

1. Expand those same two graph bars into the preferred two-person comparison,
   with teal/orange people and no names. Keep MB/MC labels beside the bars;
   no crowd plaza or totem returns.
2. Show the red **$6 floor** on the vertical price axis. Its green legal interval
   runs from 6 upward with continuation. Beside it, show the purple mutually
   beneficial interval **$3.75–$5** and the mutually acceptable **$4** marker.
3. Hold `3.c` with the two intervals visibly disjoint and one caption:
   **Both gain at $4; that price is illegal.** The proposed trade stays unrealized.
   Return to the same graph overview before the ceiling transition.

## 4.a · Replace the floor with a binding ceiling

1. Remove the floor and move to a **$3 ceiling**, passing through the $4 market
   without adding a hold. Restore the graph overview and clear the floor's
   selected-bar figure, legal interval, labels, and caption.
2. End the single red price guide at the short-side supply curve and put the
   actual-quantity tick/drop at **20**. Retain purple gains for those lots.
3. Hold `4.a`. Do not add shortage labels, brackets, or a separate demand count.

## 4.b · See the ceiling's lost gains

1. Keep the first 20 lots' realized gains purple and show missing positive gains
   from lots 21–39 in grey. The zero-gain fortieth lot adds no area.
2. Retain the **P*=4** marker and drop to quantity **40**. Mark **Q=20 to Q=40** on the
   quantity axis, labeled **Lost trades**. This differs from
   the whole shortage range; positive missing gains are lots 21–39 and 40 is zero.
3. Hold `4.b` with **DWL** attached to the grey region and no dollar-total rows.

## 4.c.select · Select a trade lost from equilibrium

1. Select lot **25** inside the graph's marked 20–40 lost-trade range. Highlight
   its **two** MB/MC bars, with heights **$7** and **$3.25**.
   Add the numerical MB/MC labels in the close-up.
2. Hold `4.c.select` before expanding those bars, keeping the equilibrium
   reference and the subset of missing trades clear.

## 4.c · Inspect one beneficial lot blocked by the ceiling

1. Expand the selected graph bars into the same two-person figure, with
   teal/orange materials and MB/MC labels, without names or a restored plaza.
2. Show the red **$3 ceiling** on the vertical price axis. Its green legal
   interval runs from **0 to 3**; the purple mutually beneficial interval beside
   it is **$3.25–$7**. Mark **$4** inside the beneficial interval.
3. Hold `4.c` on the disjoint intervals and caption **Both gain at $4; that
   price is illegal.** Keep this figure for the next permission step.

## 5.a · Permit that missing trade

1. Lift the ceiling while still in the selected two-person figure. Remove its
   legal restriction and complete the trade at **$4**, showing the agreed price
   inside the mutually beneficial interval.
2. Change the close-up's lost-surplus bracket to **purple surplus gained
   ($3,750)**. Hold `5.a` on this completed trade in the two-person figure.
   Do not return to a held partial-allocation graph or isolated purple lot strip.
3. Internally the allocation is lots 1–20 plus 25, with total surplus $151,250.
   Keep that aggregate total and any quantity-21 readout off screen. Remove the
   policy price/quantity guides before returning to the graph on the next advance.

## 5.b · Allow the remaining beneficial trades

1. On advance from `5.a`, return the selected bars to the graph while filling
   all remaining positive-gain lots through 39 in one continuous transition;
   include indifferent lot 40 under the inclusive convention. Do not pause
   on the intermediate gap or isolated lot-25 strip, or add per-trade stops.
2. Hold `5.b` only after the purple total-surplus region is **contiguous through
   40**. Keep the ordinary 40 axis tick visible and active price/quantity guides
   hidden; no positive-gain strip remains grey.

## 5.c · Inspect the zero-gain boundary

1. Highlight lot **40** directly at the curves' boundary, where MB and MC are
   both **$4**. Mark the coincident endpoints on the same stationary graph.
2. Hold `5.c` on the zero gap. The exact crowd's 39 and 40 trades tie for maximum
   gains; do not claim that removing this lot would lower welfare.

## 5.d · Force one trade beyond the boundary

1. Title: **Force one trade too many.** Add lot **41** as an explicitly forced
   trade immediately past the ordinary 40 axis tick. Color its exact negative
   gain strip red; do not widen it, add a 41 counter, or restore active guides.
2. Add small teal/orange dots at the MB/MC endpoints and one nearby **MC > MB**
   label. Internally MB is $3.80 and MC $4.05; display no individual loss dollars.
3. Hold `5.d` on the unchanged graph with one bottom caption: **The next unit
   costs more than it is worth.** No inset, extra diagram, or camera move.

## 5.e · Undo the harmful trade and name the result

1. Remove forced lot 41 and its red strip, then clear its endpoint dots/label.
   Retain the full purple maximum-gain area and ordinary 40 axis tick; active
   price/quantity guides remain hidden.
2. Name the **First Welfare Theorem** with a concise conditional statement:
   competitive markets with no externalities maximize welfare when all relevant
   benefits and opportunity costs are counted.
3. Hold `5.e` on the graph and stated conditions. This does not establish unique
   partners, resolve distribution, or assert that every market satisfies them.

## 6.exercise_floor · Exercise B4 Q2

1. Place the floor exercise after the completed argument, before the ceiling
   exercise. Use the sheet's 9-galleon floor and original prompts: quantity
   exchanged, producer surplus, deadweight loss, and a floor of 6.
2. Use the approved muted rounded panel, gold serif exercise heading, white
   concise body, and centered equations. Show no answers. Hold
   `6.exercise_floor`, then restore the same spinach graph.

## 6.exercise_ceiling · Exercise B4 Q1

1. Use the original pasty equations and 5-galleon ceiling with its prompts:
   quantity exchanged, CS, PS, DWL, and the graph with shaded regions.
2. Use the same exercise-card styling, without extra repeated questions or
   answers. Hold `6.exercise_ceiling`, then restore the spinach graph.
3. The pasty model's continuous areas never replace the exact spinach lots.

## 7.a · Close with the result and its scope

1. Retain the $4, quantity-40 graph and purple total-surplus area.
2. Briefly distinguish maximal gains from distribution and other policy aims,
   keeping the competitive/no-externality conditions already stated.
3. Hold `7.a` without a new policy, crowd scene, or repeated argument.

## Implementation and review boundaries

- Preserve all **22 opening holds** through `1.i.algebra`, including the
  eight-minute pre-Q2 budget. Section 8 has 18 holds, for **40 total**, including
  `3.c.select` and `4.c.select` before the selected graph bars expand.
- The graph overview and graph-derived two-person comparisons supersede the
  old back-half crowd/plaza staging. Recap episode order and holds are unchanged;
  the September 23 close-up and per-person ground-segment refinements apply.
- The welfare display has inside-area CS/PS labels, unified purple total surplus,
  grey DWL, and red negative gain. Policy beats have one price guide and one
  actual-quantity tick/drop; both stay hidden after `5.a`. No aggregate dollar
  totals or shortage/excess dashboard appears.
- Keep exact arithmetic internally: equilibrium TS $195,000; floor TS $183,750
  and DWL $11,250; ceiling TS $147,500 and DWL $47,500; permitting lot 25 gives
  TS $151,250; forcing lot 41 gives TS $194,750. These are not displayed totals.
- Preserve the 39/40 tie, ranked lot identities, and the distinction between
  willingness at a price and actual selected trades. No government purchases
  or extra planner-sorting episode is introduced.
- The revised 40-hold scene passed its end-of-pass construction and exact
  allocation/arithmetic checks. Captured selection, close-up, and return frames
  were inspected. All 22 opening holds remain in the same order. The latest
  front-half pass checks the decision figures, original crowd membership, and
  fixed-length ground segments through both plaza returns.
- Only the canonical animation and this storyboard belong to the update. Notes,
  exercises, shared assets, B3 files, and stale snapshots remain unchanged.

## Notes reconciliation for Taylor/Fable

- Keep the accepted floor-first economic order; only its presentation changes
  to a graph overview and selected MB/MC bars expanding into two-person
  comparisons after the equilibrium/algebra recap. Legal and mutually
  beneficial price intervals explain why the controls block gains.
- CS/PS are familiar callbacks, then become one purple measure of total gain.
  Blocked positive-gain lots and the forced negative-gain lot carry the theorem
  argument without a separate planner episode or payment-cancellation proof.
- The exact discrete totals remain unchanged in the model. Lost gains concern
  unrealized beneficial lots; maximum gains can have a zero-gain final lot.
- Author-owned notes remain untouched. Efficiency is conditional and does not
  by itself settle distribution or every policy question.
