# Episode B4 | First Welfare Theorem | Storyboard

B3-based animation implementation · 2026-09-22.

Latest direction: interrupt the recap with Exercise B3 Q2 **before** resolving
equilibrium. The entire review before Q2, including the bumper, must finish
**under ten minutes; target eight minutes**. Establish the people and willingness counts at an off-equilibrium
price, let the class reason about incentives, then show one deliberation and
one compressed common-price adjustment in each direction. Never reveal $4 as
the answer before that exercise. The full lesson now runs as one animation.

The live B4 notes now specify exact crowd welfare totals. Use those totals for
any crowd implementation; the continuous exercise market remains separate.
The animation currently runs planner → theorem → policy. Taylor is deciding
between that order and the ceiling-first notes; keep the current episode order
and beat IDs unchanged until he decides.
Lecture notes, exercise files, and the older Typst storyboard are author-owned.

## Runnable scenes

Run **`maniml 03_B4.py B4`** from this folder to review the complete lesson in
one viewer. This is the primary animation file for subsequent edits. All nine
stages and all 53 named teaching stops share one forward/back navigation rail.
The code remains a flat, sequential `construct()` at 15 fps. Each section joins
the next by clearing the completed stage and resetting its camera; there are no
extra navigation-only pauses. Existing B3 geometry/model code is copied where
indicated below; no shared assets changed.

The curved-plaza prototype now covers the full-market recap and graph bridge
(`1.d`–`1.i.algebra`). Buyers occupy the upper/back rim arc and sellers the
lower/front arc. A muted dashed horizontal diameter divides their halves;
actual partners meet across it, and a vertical price totem stands at its right
end. Willingness moves people partway inward. Review
this representative market layout before propagating it into welfare/controls,
which still use their earlier crowd placement. Approved full-width demand/supply
rows and small-market scenes remain as reviewed. Selected examples may use a
B3-style close-up; the overview is steady while willingness and matching change.

The numbered files below are **stale development snapshots**, retained for
reference. They predate the latest combined-scene staging and must not be used
to review the current design. They are not imported or executed by `03_B4.py`.
The teaching-stop column lists the current combined scene's corresponding
stages; the snapshots may differ. No snapshot synchronization is included here.

| File | Class | Teaching stops |
|---|---|---|
| `03_01_Exchange.py` | `B4Exchange` | `0.a`, `1.a` |
| `03_02_Bidding.py` | `B4Bidding` | `1.b`, `1.b.settled` |
| `03_03_TwoTrades.py` | `B4TwoTrades` | `1.b.two_trades.plaza`, `1.b.two_trades`, `1.b.equal_prices` |
| `03_04_Buyers.py` | `B4Buyers` | `1.c.buyers`, `1.c.buyers.low` |
| `03_05_Sellers.py` | `B4Sellers` | `1.c.sellers`, `1.c.sellers.high` |
| `03_06_Equilibrium.py` | `B4Equilibrium` | `1.d`, `1.e`, **`1.j`**, `1.f`–`1.i.stable` |
| `03_07_Graph.py` | `B4Graph` | `1.i.graph`, `1.i.algebra` |
| `03_08_Welfare.py` | `B4Welfare` | `2.a`–`5.d` |
| `03_09_Controls.py` | `B4Controls` | `6.a`–`7.a`, including both B4 exercises |

`03_Code.py` remains the older notebook export.

## Direction and sources

Taylor's current direction is to make the simulation carry the welfare argument.
CS and PS are familiar from B1/B2. Price-control arithmetic and graphs build on
B3. The central new work is showing why an allocation maximizes total gains,
then showing that the market selects that allocation.

Recorded in the September 22 storyboard interview (the order decision below
is now pending):

- The newly written source is [B3's conversation outline](../B3_Equilibrium/00_Outline.md).
- Keep the review before Exercise Q2 under ten minutes, targeting eight minutes
  including animation and discussion. Teach the seven stages of that outline in
  their simplest form, with equilibrium adjustment and algebra after Q2. This is B4's complete explanation of
  the equilibrium ideas that did not land clearly in class; it must stand on
  its own without returning to a separate B3 animation.
- Retain the small exchange, bidding, and two-trade stages, then build buyers,
  sellers, equilibrium, and the graph/algebra bridge. Give the largest share of
  the time to explaining why the equilibrium price holds.
- The earlier interview placed the social planner's best allocation before
  competitive equilibrium. This remains the implemented order while Taylor
  considers the alternative in the animator note.
- Edit only animation files and `02_Storyboard.md`; lecture prose stays with
  Taylor/Fable. This pass implements the animation scenes and keeps this storyboard current.

Read [B4's notes](01_Notes.md), especially Welfare Analysis, Efficiency, and Price
Controls, alongside that outline. The older [welfare storyboard](B4_Welfare_Storyboard.typ)
supplies the affordable-spinach motivation and blocked-bid example. The current
animation puts the planner argument before the policy applications; the restaged
notes use ceiling-first. Neither this storyboard nor the animator should resolve
that fork before Taylor decides.

September 22 live-review confirmations and open points:

- **Confirmed: no price line spanning the plaza rows.** Taylor called that line
  confusing, then approved the short bars and separate price indicator. His
  later direction places price on a vertical totem at the right rim. The dashed
  ground diameter is the meeting line; dashed graph price guides still end at
  their curves.
- **Bottom boxes rejected; broader unboxed convention still open.** Taylor
  said the bottom boxes were throwing him off and identified the decision
  close-ups as the layout problem. The current implementation uses plain-text
  choices. Explicit confirmation that every deliberation, including blocked
  policy bids, should replace B3's boxed grammar has not been recorded. Keep
  the existing implementation pending that decision.
- **Order frozen.** Following Taylor's instruction about the
  [animator note](00_Note_to_Animator_2026-09-22.md), only its enumerated
  order-independent corrections are in scope for the next edits. The combined
  animation has 53 named holds, including `1.c.sellers.high`; the full order
  and existing section for that hold remain unchanged.

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
- Two trades first holds B3's `3.a` oblique plaza with both buyers and both
  sellers visible. Andrew's arrival animates into this frame. Only then does
  the familiar head-on view show Amanda-Grace's alternatives; the recorded
  trade sequence and settled hold return to that same plaza.
- All crowd scenes reuse B3's radius-4.8 floor and rim, and its plaza-left camera:
  phi 48°, theta 0°, focal distance 50, center `[4, 0, 0.65]`, height 11.
  The recap now uses the curved-plaza convention below. The later welfare/control
  stages retain this earlier placement pending review: buyers and sellers each
  occupy one uninterrupted line, at y=2 and
  y=−1.7. Both use the same rank spacing, 7.4/99, beginning at x=−3.7.
  Waiting spheres have radius 0.026, bars width 0.058, and circles radius 0.035.
  Bars retain the common base 0.18 and dollar-height 0.19.
  Actual trading partners stand beside one another at the seller's station,
  at x offsets −0.019/+0.019. Paired spheres have radius 0.014, bars width
  0.030, and circles radius 0.018, leaving space between neighboring pairs.
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
- Welfare comparisons retain B3's dollar-to-height scale. Pair 20, the buyer/
  seller substitutions, and proposed pair 21 need the taller head-on frame:
  center `[0, 0, 3.4]`, height 10.2, phi 90°. The later marginal pairs return to
  B3's center `[0, 0, 2.05]`, height 7.2. This keeps the $8–$10 bars below the title.
- `fixed`, `add_market_objects`, and the original text billboard adapter are
  reused from B3. They handle renderer/label behavior, not teaching choreography.
  No shared asset or engine code is changed.

## Curved-plaza review convention

For the full-market recap, short floating bars are value cues; the graphs retain
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

Briefly highlight each willing group's ground arc together with the same-colored
horizontal 0–Q span on its graph. Clear these correspondence marks before matching.
The older circle/row convention below continues only in the later stages awaiting
this layout review. Camera movement is available for deliberate example close-ups.

## Shared stage and meaning

- Use the existing 2:1 graphite stage, 2160 × 1080, 15 fps, CMU serif teaching
  text, azure question titles, gold definition terms, and existing style tokens.
  Demand/CS is teal; supply/PS is orange; price guides and price readouts are red.
  Quantity numbers follow their demand/supply colors. Payment/expenditure
  **areas** are green; total surplus is
  `TOTAL`; DWL is grey. The small exchange retains B3's orange cost and PS outline.
- Reserve one bottom band for the current question, definition, or two-option
  comparison. Remove its previous content before replacing it. Do not stack a
  definition, caption, and deliberation card there simultaneously.
- Keep the market at left and its graph at right during market-wide beats.
  Begin with 59 buyers and 100 sellers in separate ranked waiting lines.
  When actual trades are revealed, each trading buyer joins their seller.
  Those without trades stay at their waiting positions. Mark every person but
  label only selected people.
  Individual comparisons enlarge the relevant bars into a head-on view while
  hiding the other people; their allocation stays unchanged. Full-width head-on
  rows carry the individual demand/supply comparisons. For the later quantity
  argument, keep the B3 plaza and merged graph fixed: select participants and
  fill their gain strips without rearranging the scene.
- Decision close-ups use plain text, without bottom boxes or card backgrounds.
  Keep participant names beneath their spheres and MB/MC labels beside their
  bars. In the two-seller comparison, place each payment/gain label beneath its
  seller. In the full-market bidding examples, place each choice beside its red
  current/proposed price line and point to that line with a short arrow. These
  are world-space, camera-facing labels, using B3's `face_camera` convention;
  remove detached footer choices. Emphasize acceptance by coloring the offer text.
- Read each line left to right with no row breaks. Both have the same local
  zero and dollar scale. Show the common price in the readout and dashed graph
  guides; do not draw a price line through either row of people on the plaza.
  The common rank spacing keeps potential counterparts aligned; the seller-only
  tail continues past buyer 59. Adjacency represents an actual trade, not mere
  willingness. Prediction holds keep buyers waiting until trades are revealed.
  The ranked pairing is visual bookkeeping, not a claim of unique partners.
- Build the demand graph from its buyers and the supply graph from its sellers,
  with narrow per-lot bars behind each straight equation line. Give both separate
  graphs the same price scale from the start, matching the projected foot and
  top of the plaza's price totem. At `1.i.graph`, translate each complete graph,
  including its bars, to a shared origin at the projected totem foot. Do not
  morph or resize the axes or curves. Clear duplicate axis labels and use the
  actual 3D totem as the merged graph's visible price axis while the plaza stays
  visible. Retain the bars through the algebra and later welfare transition.
- Quantity readouts are bare numbers at their corresponding horizontal graph
  positions: teal for demand and orange for supply. Apply this to the full-width
  rows, separate recap graphs, and merged welfare/control graph. Keep the number
  below its row or quantity axis, moving with its guide; omit detached `Qd =`
  and `Qs =` labels and the separate `Qx` counter. When quantities coincide on
  the merged graph, show one number. Actual matching or the current caption
  communicates trades. Keep quantity symbols in equations and teaching math.
- One check means willing at the displayed market price. One ground circle means
  actually trading. Keep marks distinguishable by shape; default to side-colored
  checks and green circles, as proposed in the B3 outline. A selected comparison
  uses a temporary outline/leader, not an extra trading circle.
- All willingness checks and red Xs are genuine world-space marks anchored above
  their own person/bar, using B3's `face_camera` convention. They follow their
  participants and scale with camera zoom/rotation, rather than staying in a
  fixed-screen overlay. Apply this to the full-width rows, curved plaza, welfare,
  and controls; retain each scene's existing willingness logic, counts, and order.
- In the uncontrolled and policy cases, (Q_x=\min(Q_d,Q_s)), with highest-MB
  buyers and lowest-MC sellers trading. This is an explicit rationing assumption
  under controls. During planner experiments, chosen (Q) replaces this rule;
  hide market-willingness checks and demand/supply quantity numbers so they do not masquerade as
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
  Horizontal graph price guides are dashed, from the price axis to the curve,
  with no extension past the intersection. Separate graphs stop at their own
  willingness quantity; overlaid graphs stop at the first curve encountered.
  Reference prices and proposed policy prices follow the same convention.
  When a dashed guide changes length, keep dash lengths and gaps fixed, with
  the pattern anchored at the price axis or the guide's starting endpoint.
  Reveal or clip dashes at the moving endpoint instead of stretching the pattern.
  Apply this to the demand/supply comparisons, recap graphs, welfare quantity
  guides, and price-control guides; it changes no episode order or teaching hold.
  The exact crowd's read guides land on staircase boundaries. Smooth lines remain
  faint fitted references; policy totals use the exact crowd's rectangles.
- The scene files use flat, sequential `construct()` choreography, visible
  constants, simple loops for repeated objects, and literal `self.pause('id')`
  boundaries. No per-beat helper framework. Each stage reconstructs
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
   dim excluded people/bars, and highlight Gary, whose MB=$6. Put the price
   readout just left of the guide and a teal “30” below the row at Q=30;
   quantities are thousands of pounds. Hold “MB ≥ P”; equality is willing.

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

1. Keep everyone at the outer rim, with willingness marks and counts hidden.
2. Ask how much each side would trade at $3. Hold before revealing willingness.

## 1.e · Count the shortage and the actual trades

1. Willing people step to the inner arcs and receive green checks. Unwilling
   people stay at the rim with small red Xs. Reveal teal “45” at demand's
   quantity position and orange “20” at supply's quantity position.
2. Briefly highlight the 45 willing buyers' ground arc with demand's horizontal
   0–45 span. Repeat for the 20 willing sellers and supply's 0–20 span.
3. Clear the correspondence marks, then move the first 20 buyers and sellers
   to matching x stations along the dashed diameter. Buyers stop just above it
   at y=+0.4 and sellers just below it at y=−0.4, forming 20 adjacent pairs.
   Center the occupied stations on the plaza. The matching and next caption
   communicate the 20 trades; add no separate Qx counter.
4. Hold “20 pairs trade. 25 willing buyers are still waiting.” The checked
   unmatched buyers, including Amanda-Grace and Gary, remain on the inner arc.
   The spatial difference distinguishes willingness from actual exchange.

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
   seller 20 (MC $3) into B3's head-on view. Clear the fixed graphs during that
   comparison. Place “Wait at $3: gain $0” beside the current red $3 line and
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

1. Return both sides to the outer rim and hide numerical counts,
   checks, Xs, and quantity read guides before moving the common price to $6. Ask “At $6, who is left
   out?” Hold with those answers still hidden.

## 1.h · Count the excess and recall undercutting

1. Reveal teal “30” and orange “80” at their graph quantity positions, 30 buyer
   checks, 80 seller checks, and 30 central pairs. Fifty checked sellers remain on the inner arc. Mark the quantity gap 30–80; show “Excess: 50,000 pounds.”
2. Highlight Andrew among the unserved sellers and Gary among the served buyers.
   Show the same B3 head-on inspection view, with Andrew's MC $4 and Gary's MB $6.
   The actual plaza returns before Andrew replaces seller 30 beside Gary.
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
   person remains unmatched on the inner arcs.
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
   from which the graph stage begins.

## 1.i.graph · Recognize the same condition at the crossing

1. Retain the settled crowd, horizontal meeting line, $4 price totem, and dashed
   $4 graph guide. Simply translate the two complete graphs, carrying their
   narrow lot bars and straight curves, to a common origin at the projected
   totem foot. Their price scales already match the totem; no axes or curve
   morphing/resizing. Remove duplicate axis labels and let the actual 3D totem
   serve as the visible price axis. The lines cross at Q=40, P=$4, matching the
   crowd's counts exactly at this price.
2. Title: “Why does the crossing give equilibrium?” Highlight one shared “40”
   at the graph's quantity position and the crossing. Keep the people visible so this is another
   representation of the same result, not a second definition. Hold.

## 1.i.algebra · Make the equality explicit

1. Keep the merged graph and its lot bars fixed at right while fading the plaza.
   As the 3D totem fades, show an ordinary graph price axis in the same place.
   Use the vacated left half for the arithmetic. Show the two equations with
   their subscripts: (P=12-Q_d/5) and (P=2+Q_s/20).
2. Show (Q_d=Q_s=Q) before setting their right-hand sides equal. Then reveal
   (12-Q/5=2+Q/20), (10=Q/4), and (Q^*=40) in that order, with no extra
   arithmetic pauses. Substitute into supply to show (P^*=2+40/20=4).
3. Carry the starred pair to the crossing. Hold “Same price; equal quantities.”
   This is a short explanation of what the algebra means; leave Exercise Q1
   completed. Hold on the solved frame. The welfare stage reconstructs
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
4. Hold “The price divides the gain.” Hide the market graph during this one-lot
   calculation so no ghost graph sits behind the equation. This is a fixed-trade accounting
   comparison, not a new common market price or a renegotiation prediction.
   Restore the $4 payment and return the bars to their places on advance.

## 2.c · Give the planner the two choices

1. Remove the graph's market-price guide, checks, demand/supply quantity numbers, and all CS/PS division
   lines. Retain each person's MB/MC and the 40 trading circles.
2. Title: “Which trades should happen?” Show only two short prompts beside the
   model: “Who trades?” and “How many trades?”
3. Highlight the selected participants, then the Q marker. Hold. From here the
   planner chooses an allocation; no automatic price adjustment runs.

## 3.a · Hold quantity fixed and test the buyers

1. Set the planner's allocation to 20 trades. For this explicit counterfactual,
   select buyers 1–20 except buyer 10, with Gary (buyer 30) in that slot; select
   sellers 1–20. Gary joins seller 10; unselected buyers return to their waiting
   stations. Mark “20 trades” and retain all unselected people.
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
   allocation, replace selected seller 10 with Andrew (seller 40). Buyer 10
   joins Andrew at his station. Keep Q=20.
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

1. Keep the B3 plaza, camera, and merged graph in place. The first 20 trading
   partners remain beside each other. Highlight buyer and seller 21 in their
   actual locations; do not enlarge or rearrange them.
2. Mark their MB $7.80 and MC $3.05 on the same graph, with labels beside those
   points and a purple segment spanning the potential gain. Circles stay empty.
3. Ask “Trade 21: should we add this lot?” Hold before adding it.

## 4.b · Add positive gains

1. Add pair 21 to the allocation and its exact gain strip to the graph. Show
   $(7.80 − 3.05) × 1,000 = $4,750 in the current bottom caption.
2. In one short sweep, increase the quantity to 39. Newly trading buyers join
   their sellers; circles and filled gain strips follow the selected quantity.
3. Highlight pair 39 in place, with MB $4.20 and MC $3.95 beside the graph
   points. Hold “Trade 39 adds $250. Another trade helps while MB > MC.”

## 4.c · Inspect the boundary

1. Move only the selection to pair 40. Put “MB = MC = $4” beside the crossing.
   Keep the camera, axes, bars, and previous 39 trades fixed.
2. Ask “Trade 40: what does this lot add?” Hold before the answer.

## 4.d · Account for indifference

1. Select pair 40 using the inclusive willingness convention. Quantity reaches
   40, but no additional gain area appears.
2. Hold “Trade 40 adds $0. 39 or 40: the same total gain.” This exact finite
   market has an indifferent final pair; do not imply a unique optimum.

## 4.e · Test a trade beyond the boundary

1. Select pair 41 for inspection, retaining 40 actual trades. Label MB $3.80
   and MC $4.05 beside their graph points. Both people remain untraded.
2. Ask “Trade 41: would this lot help?” Hold. On advance, reveal that MC > MB
   and this trade would lose $250. Do not execute a voluntary trade unsupported
   by any mutually acceptable price.

## 4.f · Read the planner's complete rule

1. Clear the temporary point labels and selection marks. Reduce quantity to
   30 once, leaving the missing positive gains as unfilled purple outlines.
   The departing buyers return to their waiting places.
2. Restore 40 trades and their gain fills in one sweep. Pair 40 adds no area.
   Camera, plaza, and graph remain fixed throughout; price remains absent.
3. Hold “Take the gains; stop when additional cost exceeds benefit.”

## 5.a · Return control to buyers and sellers

1. Release the planner's chosen people to their waiting stations. Keep the
   camera and overlaid graph exactly where they are. Preserve every rank and
   value. Store the
   planner's selected prefixes as faint outlines. Remove the planner selection
   circles, quantity control, and hypothetical comparison marks.
2. Restore the market price of $4. Title: “Does the market choose these trades?”
   Hold before revealing willingness or the resulting allocation.

## 5.b · Let the common price select participants

1. Reveal checks on the 40 buyers with MB≥$4 and 40 sellers with MC≤$4. Move
   those buyers beside their sellers and circle both partners. Show one “40”
   at the merged graph's quantity position. The actual selection coincides
   with the saved planner outlines; add no separate trade counter.
2. Recall the boundary with two threshold captions on the plaza: buyer 40 is
   indifferent, buyer 41 will not pay $4; seller 40 is indifferent, seller 41
   will not sell at $4. The point comparison has already established why.
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

1. Retain B3's 3D plaza and the same merged graph dimensions at $4, 40 trades.
   Use one straight equation line per curve; the filled per-lot rectangles keep
   the exact discrete surplus arithmetic. Curve names sit beside their curves;
   price labels sit at their y-axis levels. Policy bounds use the red price-guide
   color; a binding bound replaces the duplicate actual-price label.
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

1. Hide complete count and welfare readouts (labels as well as numbers),
   willingness checks, trade circles, and welfare fills before
   lowering the ceiling from $5 to $3.
2. Actual price stays $4 until the ceiling crosses it, then follows it to $3.
3. Ask how much actually trades. Hold before the answer appears.

## 6.c.blocked · The incentive remains; the bid is prohibited

1. Reveal teal “45” and orange “20” at their quantity positions on the graph.
   The first 20 people on each side trade; matching conveys the trade count.
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

1. Hide complete count and welfare readouts, checks, circles, and welfare fills
   before raising the floor.
2. Actual price stays $4 until the floor reaches it, then follows it to $6.
3. Ask how much actually trades. Hold with answers hidden.

## 6.g · The undercut is prohibited

1. Reveal teal “30” and orange “80” at their quantity positions on the graph.
   Thirty pairs trade; the caption states that 50 willing sellers have no buyer.
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

- There are **53 literal named holds** in the combined animation. The opening seven
  stages contain 22: the bumper, Exercise Q2, and 20 teaching holds. Budget
  **eight minutes before Q2, always under ten**, including the bumper. Keep the
  post-exercise equilibrium explanation; cut bidding repetition first.
- Exercise Q2 comes after the shortage is counted, before any $4 equilibrium
  answer appears in the full market. The pasty exercise remains a separate model.
- The exact quarter-dollar counts, inclusive willingness, and 39/40 welfare tie
  are retained. Circle interiors stay empty: visibility updates change stroke
  opacity, never fill opacity. Check marks likewise remain open strokes.
- Source execution and checkpoint restoration have been checked in ManimL.
  B3's copied small-market trace retains its final matching/price assertions.
  Each policy/planner state is checked against exact participant counts and gains.
- Actual partner placement follows the selected allocation. The $3/$4/$6
  market states contain 20/40/30 adjacent pairs; the individual switches preserve
  trade counts. Prediction holds return people to their waiting stations.
- Visual review uses the development viewer and selected full-resolution native
  frames for this build. Native frame caches can display stale glyphs after
  unrelated checkpoint captures; suspected failures are checked with an isolated
  direct run before changing correct scene geometry.
- The recap, welfare, and control views have been reviewed. Direct native
  captures verify the welfare comparison labels and payment line. The quantity
  proof (`4.a`–`4.f`) uses a fixed camera/graph throughout, with exact selected
  counts and gains checked at each hold. No separate ranked-row layout remains.
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
