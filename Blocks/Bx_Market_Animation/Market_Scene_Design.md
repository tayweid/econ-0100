# A reusable market scene for Parts B and C

Design proposal · September 9, 2026

A first ManimL proof of concept now lives in [Blocks/Sim](../Sim/README.md).
That README describes the four runnable scenes and their current limits; the
proposal below remains the broader plan.

Build one market world whose participants, rules, and analytical views can change between lessons. Begin with the existing ManimL lecture workflow. Keep the economic model independent of ManimL so a later student-controlled version can use the same rules and examples.

The first deliverable should be small: one buyer on a plane, a value indicator above the buyer, and a flat model beside the scene. Add one seller and complete one exchange before expanding to a market.

## What the existing work gives us

- [The earlier simulation outline](Bx_Equilibrium_Video.typ) is the strongest design source. Lines 24–104 already describe marginal-unit bars, ordering people into curves, visiting posted prices, switching sellers, multiple units, and links to the standard market graph. Preserve that progression.
- [The main Maxine experiment](Bx_Equilibrium_Video_Maxine_3D.py) contains the useful visual ingredients: a plane, a participant represented by a disk, and a floating bar. Its bar is an illustration, not yet a quantity bound to an economic model.
- [The 2D prototype](Bx_Equilibrium_Video_Market_2D_Prototype.py) contains useful distinctions between reservation values and offers, but it does not parse as written: the first indentation error is at line 28. Its bargaining loop at lines 96–121 reads economic prices from mobject coordinates. Moving or scaling the drawing can therefore change the supposed economics. Extract ideas rather than adopting this as the shared engine.
- The Simple/Experiments files explore text visibility but are not a reusable label system. In the currently installed ManimL source, ordinary `Text` inherits a `StringMobject.apply_depth_test(recurse=True)` override. The experiments' `anti_alias_width=0` keyword is incompatible with that override. This is a source-level finding; these scenes were not rendered during this review.
- [The current B0 scene](../B0_Markets/03_Code.py), [shared style](../_Assets/style.py), and [style guide](../_Style_Guide.md) establish the production workflow: a 2:1 frame, semantic colors, Tex labels, flat episode choreography, and explicit pause checkpoints.
- [The equilibrium notes](../B2_Equilibrium_and_Welfare/01_Notes_pt1.md) already imagine Maryville's weekly market. [C4's code comments](../C4_Corrective_Policy/03_Code.py) anticipate explaining a tax on one exchange before moving to the market model.

The installed `maniml` command points to the local ManimLive checkout. Its CLI aliases `manim` to ManimL, and its exports include `Square3D` and `Disk3D`. Those names are available in this runtime even though generic Manim Community examples use different APIs. Plain Python importing `manim` is not an equivalent compatibility check.

## The scene has three visual layers

**The world:** a shallow, tilted plane with buyers on the left, sellers on the right, and room to meet between them. Sellers have stable positions; buyers travel to them. Use simple disks or short columns with names/IDs, consistent with the existing course's preference for minimal glyphs. Begin with a fixed camera. Move the camera only when changing teaching views, then stop it while students read.

**Labels attached to people:** an anchor above each participant carries a short, camera-facing label. It follows the participant but stays upright and legible. These labels are annotations, not physical signs that should disappear behind the floor. Start with `WTP $10` or `Cost $4`. Show detailed information only for the selected participant or pair. At market scale, retain a small ID and reveal values selectively.

**The on-screen model:** a flat, screen-fixed graph, equation, or individual decision panel. Reserve a portion of the frame for it instead of placing opaque text across active participants. The first panel can be a vertical value/price/cost comparison; later it becomes a P–Q graph. Expand it when it becomes the focus of the lesson. Do not keep every graph, ledger, and explanation visible at once; the existing notes-panel experiment was retired for clutter.

These are three coordinate systems: world positions, world anchors projected onto the screen, and fixed screen positions. Give each an explicit API. A fixed label alone will not follow a walking buyer. Conversely, ordinary world text will rotate and shrink with the world.

ManimL already has `mobject.fix_in_frame()`. Put overlay creation, depth behavior, and conversion from world anchors to screen coordinates behind a small renderer adapter. Match projection to the local camera/shader implementation and verify it visually. Do not assume Manim Community's `add_fixed_orientation_mobjects` helper exists locally: its [official documentation](https://docs.manim.community/en/stable/reference/manim.scene.three_d_scene.ThreeDScene.html) describes the useful distinction, but it is a different API.

Use the course tokens consistently: `DEMAND` for buyers and CS, `SUPPLY` for sellers and PS, `GOV` for the government balance, `EXT` for spillovers, and `DWL` for deadweight loss. Labels and shapes reinforce color. Keep the spatial plane economically neutral: location and travel distance have no effect unless a later lesson explicitly introduces search or transport costs.

## What floats above an agent

Separate the participant's identity from the quantity being displayed. One label/bar component should support several explicitly named modes:

- **Value or cost:** the next unit's WTP or marginal cost.
- **Offer:** a seller's ask or a buyer's bid, visibly distinct from value/cost.
- **Potential gain:** the gain if the current offer were accepted.
- **Realized surplus:** the gain from a completed exchange, or a clearly labeled round total.

Never silently turn a WTP bar into a surplus bar. Introduce the price marker, show the difference, then name that difference. Before an exchange, the difference is potential surplus. After the exchange, it can enter the realized total.

For the first example, WTP is $10, cost is $4, and price is $6. A completed exchange creates CS of $4 and PS of $2. Animate the selected agents' quantities into the flat model using copies or connectors, preserving their identity. The change of representation is itself a teaching beat.

If world-space bar height represents dollars, use one dollar scale. Perspective makes distant bars look smaller, so quantitative comparisons should happen in the flat panel or in a deliberate aligned view. A numeric head label is a safer first implementation than a forest of perspective-distorted bars.

## A progression that reuses the same objects

1. **One buyer, one unit.** Reveal WTP, introduce price, and vary price while WTP remains fixed. Show buy/not-buy and potential CS.
2. **One buyer, several units.** Reveal declining marginal values. Keep one person with a schedule of units; do not imply that every extra unit is a different person. Repeat for one seller's increasing marginal costs.
3. **Many buyers or sellers.** Initially give each one unit. Copy their values/costs into ordered steps on the flat graph. Preserve IDs through the sorting so students see where demand and supply come from. Add multiple units per person later; smooth curves are a further approximation.
4. **One buyer, one seller.** Compare WTP, ask, and cost; approach; accept or reject; settle; reveal gains. This establishes the exchange grammar.
5. **One buyer, several sellers.** Compare posted asks, identify the best available acceptable offer, and travel to it. Keep cost and ask distinct. An unattractive or unavailable seller remains visible.
6. **Many buyers and sellers.** Start with roughly six to eight of each and one unit per person. Demonstrate one decision slowly, then compress the remaining visits. Keep nontraders in view. Show intended demand, intended supply, and completed trades as different quantities.
7. **Policy comparisons.** Replay the same population under a ceiling, floor, tax, or externality. Change one rule at a time. Show who trades as well as how much is traded.

Treat the one-buyer/many-seller lesson as explaining choices among quotes, not as proof of competitive price formation. Build intuition about marginal decisions and exchange before adding a decentralized price-adjustment mechanism.

## Decide what a round means

A market period follows: **arrive → post offers → visit/compare → match → settle → summarize → begin the next period**.

Within a period, each one-unit participant can complete at most one trade. Matching reserves capacity so two buyers cannot purchase the same unit. Buyers can move at different animation speeds without changing the allocation.

The old outline includes a buyer making a higher offer and displacing another buyer. Support this later as an explicit **provisional matching** phase: tentative partners can change before settlement, and their gains are labeled provisional. Do not reverse completed consumption merely because a later buyer appears. A simpler first version completes trades immediately and lets price adjustment happen between periods.

Distinguish these operations internally:

- **Replay:** same initial state, random seed, events, and outcome.
- **Next period:** replenish unit availability and reset round gains; optionally retain offers learned in previous periods. Keep cumulative totals separate.
- **Policy comparison:** restore the same initial population and comparable seeded priorities, then apply a different rule.

Keep walking time separate from economic time. Pause, backward seek, playback speed, and export must not generate new economic decisions or duplicate a trade. Use recorded events and state snapshots at teaching checkpoints; verify that ManimL's replay restores non-mobject state too. The local ManimLive simulation notes describe attaching state to a checkpointed mobject and writing updaters against their restored mobject argument. For this market, keep the model independent of rendering, but let a checkpointed view own the current event cursor/state snapshot; do not close over stale mutable state after a seek.

## Two economic modes, with a common visual language

**A competitive benchmark** computes the allocation from values and costs and displays a supporting uniform price. It is useful for teaching demand, supply, welfare, and policy wedges. For a small discrete market, the supporting price may be an interval. Use an explicit rule for ties and zero-gain trades; do not force a unique price just to draw one dot. If the instructor chooses a price below or above that interval, compute willingness separately and apply an explicit rationing rule.

**A decentralized process** gives sellers offers, gives buyers an information/search rule, and specifies when quotes can change. It generates an event sequence that the same scene plays. Start with a transparent posted-offer rule and a bounded number of periods. Keep its observed trades/prices separate from the benchmark. Stability under one rule is not automatically competitive equilibrium; label maximum-round termination as such, and do not guarantee convergence without checking it.

In both modes, outcomes come from model state. The scene illustrates those outcomes. Random walking alone is not a price-discovery mechanism, and scripting movement toward a known equilibrium is an illustration rather than evidence that the mechanism discovers it.

## Policy extensions

| Lesson | Economic change | Visual consequence |
|---|---|---|
| Competitive market | No policy wedge; explicit information and allocation assumptions | Participants trade, nontraders remain, individual units become D/S and surplus |
| Price ceiling | Constrain the specified legal transaction price; ration scarce supply | More willing buyers than completed purchases; expose queue/lottery/priority |
| Price floor | Constrain price; ration among willing sellers | Unsold units remain; show excess supply |
| Government purchases | Government buys specified units under its own rule | A distinct purchasing participant/account; acquired inventory and fiscal cost |
| Per-unit tax | Buyer payment exceeds seller receipt by tax | Split the price marker and route the difference to government |
| Subsidy | Government funds the gap between receipt and payment | Same accounting with negative government net revenue |
| Externality | A trade imposes damage or creates benefit outside the trading pair | Bystanders outside the two market sides receive an effect; add MSC/MSB |
| Corrective policy | Combine the wedge with the spillover model | Compare private outcome, policy outcome, and social benchmark |

For a ceiling or floor, traded quantity alone does not determine welfare. Highest-value buyers receiving the available units is an assumption in the existing B2 welfare notes. A lottery can produce the same quantity and less surplus. Compute welfare from the identities that actually traded. Under decentralized search, actual trade may also be below the short side of the market.

Government purchases are a separate extension from a price floor alone, matching the course's government-cheese plan. Record public inventory and specify its use/value before asserting a social-welfare result. Tax incidence also requires prices to respond; assigning the remittance obligation to one side is not the same as determining the burden. Combined controls/taxes should identify exactly which price the legal bound constrains.

For externalities, a transaction can be privately beneficial and socially harmful. In the $10/$4 example, external damage of $8 makes the social gain −$2 although the two parties gain $6. A corrective tax changes incentives; tax revenue does not cancel physical damage. Keep monetary surplus distinct from claims about need, fairness, or subjective well-being, as the B1 notes already do.

## A small implementation structure

Keep one shared package under `Blocks/_Assets/market/`, created incrementally:

- `model.py`: participants, marginal units, scenario rules, state transitions, immutable events, and the transaction ledger. No Manim imports.
- `benchmark.py`: competitive and social allocations, supporting price ranges, and welfare comparisons.
- `views.py`: `MarketStage`, `AgentView`, attached labels, individual/market panels, and the renderer adapter.
- `scenarios.py`: small named teaching examples and reproducible populations; keep price discovery here or in a separate mechanism module once needed.

Initially, these boundaries can be a few dataclasses and functions. Avoid a general simulation framework or a deep hierarchy of episode subclasses.

An economic participant stores an ID, role, marginal values or costs, unit availability, and any offers needed by the chosen mechanism. Display position belongs to the view. A trade records buyer/seller IDs, marginal-unit IDs, quantity, value, cost, buyer payment, seller receipt, government balance change, and external effect. For nonlinear spillovers, record the actual marginal effect at the relevant aggregate state.

Suggested events are `OfferPosted`, `VisitPlanned`, `OfferRejected`, `MatchReserved`, `TradeSettled`, and `PeriodEnded`; add `MatchReleased` only when provisional matching is introduced. A pure state transition produces the next state and events. The animation builds movement, labels, graph marks, and readouts from that same event sequence. No updater may settle trades or consume random numbers.

Keep `self.play(...)` and literal `self.pause('…')` calls in the episode's flat `construct()`, respecting the current stepper contract. Shared helpers should create geometry, state, and animation objects; do not hide the entire lesson inside `market.run(scene)` or per-beat methods. Numeric trackers interpolate between model states for display, while the ledger remains the authoritative record of completed exchanges.

For each settled unit, verify:

`CS = value − buyer_payment`

`PS = seller_receipt − cost`

`GOV = buyer_payment − seller_receipt`

`social_surplus = CS + PS + GOV + external_benefit − external_cost`

The first three terms sum to value minus cost. This prevents counting tax transfers twice. Subsidies make GOV negative. Deadweight loss compares actual social surplus with the efficient feasible allocation under the same primitives; it is not every empty patch on a graph.

## First build and acceptance criteria

**First scene:** one buyer, one plane, one attached WTP label, one flat decision panel. Move the buyer; briefly change the camera; change price. The label follows, the panel stays fixed, and WTP stays unchanged. Check live playback and export, plus backward seek. This isolates the hardest rendering interaction early.

**Second scene:** add one seller and one accepted or rejected offer. Animate the visit, settle exactly once, and show correct CS/PS. Replaying produces the same state.

**Third scene:** reuse the views for a small one-unit market with a uniform displayed price and explicit allocation. Form discrete demand/supply from the same unit data. Compare high/low prices and the competitive benchmark.

**Fourth scene:** run that same example with a binding ceiling, a tax, and an external cost. Verify actual identities and ledger sums. Add decentralized repricing after these basic representations and accounting rules work together.

Meaningful model checks are: no duplicated units; voluntary trades satisfy the relevant value/cost bounds; policy price bounds hold; tax accounting balances; rationing changes participants correctly; discrete ties and no-trade cases work; replay does not change state. A useful fixed example is values `[12, 10, 8, 6]` and costs `[2, 4, 7, 9]`: three positive-gain trades yield total private surplus 17. A ceiling of 5 makes four buyers willing and two sellers willing; allocating those units to values 12 and 10 yields surplus 16, while allocating them to values 8 and 6 yields surplus 8. The same traded quantity must not produce the same welfare display.

The original review produced this proposal and a conceptual sketch. The subsequent proof of concept is documented in [Blocks/Sim/README.md](../Sim/README.md); the legacy experiments and current B0 work remain separate.
