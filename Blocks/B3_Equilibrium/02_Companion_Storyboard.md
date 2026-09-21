# B3 · Building Equilibrium in 3D

Revision storyboard · September 20, 2026 · **Organize and storyboard first.**

The existing scene is [Animate.py · PriceDiscovery](Animate.py). Its current
behavior is recorded below. The new beats are a plan for the next implementation
pass, not a claim that the animation already does these things. Start at the
[B3 materials map](README.md) for existing files. The
[overall storyboard](02_Storyboard.md) governs the shared arc: build equilibrium
from a small cast first, then test deviations on the back end. This file details
the first branch; its legacy “Companion” filename does not prescribe a video split.

Taylor's latest directions are quoted verbatim in
[01_Notes.md](01_Notes.md#animation-direction--2026-09-20). They supersede the
old midpoint-only mechanism, the crowd's exhaustive deliberation, and the
restriction against explaining CS/PS in the companion. The earlier brief is
preserved in the collapsed history at the end. Taylor and Fable own the prose;
this document owns the animation plan and records where writing may need to
catch up.

## The visual idea

One exchange should be readable at three distances. Across the plaza, people
find and change partners. Above a pair, a red line marks their price between
the buyer's MB and the seller's MC. Up close, those same marginals and that
same price reveal payment, receipts, and gains. The ground connection is the
price line's shadow, so the wide shot and the close-up describe the same deal.

Keep the small-cast deliberation: students need time to see a choice. At ten
buyers and ten sellers, show short random price checks and the resulting
actions continuously. The change in pacing should make the market legible
without turning twenty people into twenty repeated explanations.

## What is built now

This is a source/model inventory, not a fresh visual review.

| Component | Current `Animate.py` behavior | Revision |
|---|---|---|
| World | Round plaza, seller crescent, jittered buyer crescent, floating orbs and MB/MC bars; people sort with graph twins | Preserve this foundation |
| Price | Fresh pairs split MB and MC; a challenger splits their MB and the standing price | Use explicit posted asks and an explicit outbid increment |
| Connection | Pink ground thread and a nearby dollar tag; red tick on the fixed graph | Price-height red connection with a ground projection |
| Small decisions | Survey, chosen dashed connection, spotlight, a three-person decision close-up at `2.b.i`, then displacement | Preserve the readable compare → choose → switch sequence |
| Surplus | CS/PS fills already appear on the fixed graph | Teach their meaning on the nearly adjacent marginals in the two-player close-up |
| Crowd | Every buyer sees every effective ask; each survey has a `3.a.N` or `3.b.N` pause | Seeded random seller checks; no per-visit deliberation pauses |
| Ending | One entrant/displacement pass, then an equilibrium caption and a band drawn from observed prices | Verify remaining incentives and compare with an independently computed benchmark |

The current crowd uses MB `[12, 7, 11, 5, 10, 6, 8, 9, 4, 3]` and
MC `[3, 6, 9, 8, 7, 2, 5, 10, 11, 4]`. Its inline trace produces **14 events,
four displacements, and six matches**, with prices `[7, 7, 7, 7.5, 7.5, 7.5]`.
The older header's five-displacement description is stale. Finishing that
trace is not a test that every remaining improvement has been exhausted.

The lecture prototype [Animate_A.py · PostedPrice](Animate_A.py) already has
seller tags and price-adjustment rules in [posted_price.py](../Sim/posted_price.py).
Those rules and tests are useful references, but their ID-order, full-information
process is not the requested random-search mechanism. Reuse its deviation
material after this branch establishes equilibrium, following the overall
storyboard rather than treating the two files as unrelated lesson openings.

## Price and marginal geometry

- **MB, MC, and price are distinct.** Keep each agent's marginal bar fixed at
  its value/cost. Give each seller an ask and a buyer making an offer a bid.
  An unmatched buyer has no transaction price; do not relabel MB as their price.
- **One dollar scale per view.** Both head-bars start at the same dollar-zero
  elevation. With baseline `z0` and scale `k`, draw price at `z0 + k * p`.
  Connect the buyer's and seller's horizontal positions at that height. A price
  between MC and MB is a horizontal crossbar, not a sloped line joining their
  bar tops. A faint neutral guide can extend above the seller's MC; it must not
  look like additional cost.
- **The shadow follows the line.** Project the same endpoints vertically onto
  the floor. Introduce this once with faint drop-lines, then remove those guides.
  Shadow length shows who is connected, not how many dollars they pay. The red
  line's height and label carry the price. Updating a price moves the elevated
  line; walking changes both its span and its floor projection.
- **State is visible.** A contemplated connection is dashed; an accepted match
  is solid. A switch replaces the incumbent connection and its shadow together.
  The match remains provisional while displacement is allowed. Complete trades
  once at the end of the period; cancelled matches never accumulate realized gains.
- **The close-up keeps the objects.** Move the two players and their attached
  marginals near one another, with a narrow horizontal gap and aligned dollar
  baselines. Do not move the tops together or alter their values. Orient the
  camera so their common height scale is readable, then hold it during analysis.
  Fade the market panel during this close-up; restore it when returning wide.
- **Graphite meanings persist.** Price/bid/ask: `GUIDE` red. MB and CS:
  `DEMAND`. MC and PS: `SUPPLY`. Expenditure/cost when explicitly taught:
  `GOV` green, with labels distinguishing their roles. Use faint grey for these
  supporting regions when only surplus is the focus. All labels use Tex and
  shared style tokens; 2:1 frame, 15 fps, sparse on-model text.

## Mechanics to implement next

Taylor specified posted starting prices, cuts when no one buys, outbidding,
random checks in larger groups, and deliberation for smaller groups. The rules
below make those directions implementable. Details marked **proposed** are
animator defaults for the first build, not additional quoted instructions.

1. **State:** one unit per buyer and seller, fixed MB/MC, each seller's ask,
   each current match and price, and time spent unmatched. Initial asks are
   inputs distinct from costs and must be at least MC.
2. **Small cast:** show the buyer checking the available prices and holding
   their preferred feasible connection. Keep the incumbent visible until a
   better offer is actually accepted. Stage all alternatives explicitly here.
3. **Crowd search — proposed:** each buyer checks one randomly selected seller
   per round, including already matched sellers. Randomize buyer order too.
   Use a local saved seed and precompute the event sequence, so replay is exact.
   A buyer responds only to checked offers; the fixed graph is information for
   the audience, not privileged information for the agents.
4. **Match and outbid:** an available seller accepts their posted ask when the
   buyer can afford it. To displace an incumbent, offer `standing price + bid_step`,
   never above the newcomer's MB. The seller must receive strictly more.
   **Proposed:** use the lecture's $0.25 tick for the first demonstration;
   make it an explicit editable constant rather than a midpoint formula.
5. **Better alternatives:** the Part B outline already has matched people
   continue searching for better contingent deals. In this rule set, buyers
   keep checking and
   can switch to a strictly cheaper feasible deal. A buyer never abandons a
   match without an accepted replacement. A displaced buyer searches again;
   a newly abandoned seller resumes waiting. Keep accepted price and posted
   ask consistent for a matched seller in this one-unit version.
6. **Unsold sellers — proposed:** after one complete round without a match,
   reduce the ask by an editable `ask_step`, bounded below by MC. Start with
   $0.25 to match the bid tick. Reset the waiting counter after a match or a
   cut. A matched seller does not lower an incumbent's price just because no
   new buyer arrived. Below-cost offers are never made.
7. **Stops:** distinguish a quiet round, a state with no allowed improvement,
   and a run stopped by its round limit. Check all feasible switches, overbids,
   unmatched matches, and remaining permitted price cuts in the model before
   calling the state settled. This diagnostic does not direct agents' choices.
   Do not promise convergence to the competitive benchmark from arbitrary
   asks/seeds; test the chosen scenario before writing its ending.

Economic events are computed independently of camera, position, animation
speed, and pause state. Use a small pure-Python mechanism alongside the existing
Sim models; keep the scene's plays and literal named pauses flat in `construct()`.
No random draws or economic decisions inside visual updaters.

## Revision beats

Existing top-level pause IDs stay stable. New close-up subpauses are identified
below; the crowd's old per-survey subpauses are explicitly retired in the revision.
On-screen labels below are staging proposals, not edits to Taylor's narration.

### 0.a · Open with the small cast

Retain the plaza and question title, “Where do prices come from?” Establish a
small space for the one-buyer/one-seller example; do not reveal the full crowd
first. Move the existing crescent assembly and world/panel sorting to `3.a`,
when the population actually expands. Pause at `0.a` on the simple setup.

### 1.a · One buyer, one seller, one price

Use the existing MB $10 / MC $4 pair. **Proposed initial ask: $7**, retaining
the current example's number but making it a posted input. Show the ask before
the buyer's approach. The buyer checks $7 against MB $10; the seller's MC stays
$4. The dashed connection at price height follows the approach, then becomes
solid when accepted. Reveal its floor shadow and the same $7 tick on the panel.
The small fixed panel uses Q = 0–2 one-unit slots and P = 0–12 dollars/unit,
enough for this pair and the next small-cast example.
Remove the old “split the difference” formula. Pause at `1.a` with one match,
one price, and no accounting labels yet.

### 1.b · Zoom into the same exchange

Fade the panel and background cast. Bring the two attached marginals almost
together, keeping a common zero and their original heights, and push the camera
in until the bars carry the frame. Keep enough of the players visible to preserve
identity. The red price crossbar stays at $7 throughout the transformation.

Ordered close-up holds:

1. **`1.b.i` · Read the marginals.** Label MB $10, MC $4, and Price $7 on the
   model, with a common zero baseline. The price is visibly between their tops.
   Reserve equal illustrative widths for the two views of the same one unit;
   bringing them together does not create a second unit.
2. **`1.b.ii` · The buyer.** Reveal the buyer's expenditure region from 0 to 7;
   then its label and $7. Reveal the region from 7 to 10; then name CS and show
   `10 − 7 = $3`. Keep the calculation beside the region, not in a sidebar.
3. **`1.b.iii` · The seller.** Trace the same payment as receipts of $7. Reveal
   cost from 0 to 4, then PS from 4 to 7; label `7 − 4 = $3`. Use a receipt
   brace covering 0–7 rather than filling the whole receipt and the PS twice.
4. **`1.b` · Hold the whole exchange.** Both sides remain legible: expenditure
   = receipts = $7; CS $3 + PS $3 = MB $10 − MC $4 = $6. Price divides the gain;
   the payment is a transfer between these same two people. While the match is
   provisional, these are gains at the displayed terms, not cumulative realized
   gains. The viable price range remains MC to MB, inclusive of zero gain.

Remove the arithmetic and receipt brace before pulling back. Restore the
original pair spacing, market camera, and fixed panel; the match remains $7.

### 2.a · A small market still deliberates

Bring in the existing second buyer/seller (MB $12, MC $2). Show the second
seller's posted ask before the buyer compares options. **Proposed ask: $6**
to make the available cheaper deal distinct from the incumbent $7 deal.
Hold the candidate connection while the buyer checks, then walk to the chosen
seller. Keep spotlight and camera focus on the current decision. Pause at `2.a`.
Cost bars never serve as substitute price tags.

### 2.b · Outbid, displace, search again

Keep the existing explicit rerun with newcomer MB $11 and second-seller MC $8.
**Proposed tags:** standing S1 deal $7; available S2 ask $9. The new buyer checks
both, then offers S1 $7.25 under the proposed tick rule. At `2.b.i`, hold the
challenger, incumbent, and seller: the seller compares $7.25 with $7; the
challenger compares $7.25 with MB $11. Preserve the three-person deliberation
and the circling displacement choreography. Replace the old $9 midpoint chips.

Once accepted, the price line rises to $7.25 and its connection transfers to
the challenger. The displaced MB-$10 buyer restarts and can accept S2's $9 ask.
Pause at `2.b` after that rematch. Show one displacement clearly; continued
search and price adjustment belong to the crowd beat, not an equilibrium
claim about this selected demonstration.

### 3.a · Ten buyers, ten sellers

Introduce the full cast here, retaining the existing crescent staging and
sorting choreography. **Proposed:** use the lecture prototype's marginal values
and named cast for this new crowd, as specified in the
[overall storyboard](02_Storyboard.md#bridge--the-market-we-will-test), so the
deviation branch can test the same people afterward. This replaces the old
companion's $7 benchmark population only in the planned revision. Starting asks
are a separate input list to tune; the old midpoint outcomes are not targets.
Use a fixed panel with Q = 0–10 units and P = 0–8 dollars/unit. Introduce each
seller's ask separately from MC, and do not imply sorting gives agents access
to every price.

Run the precomputed random visits continuously. A brief dashed check points to
one seller; acceptance, refusal, a raised bid, a cut ask, or displacement follows.
Use compact local emphasis and a broad market view. Omit the hub's fan of ten
comparison rays, individual comparison chips, per-visit camera orbits, and
`3.a.N` / `3.b.N` deliberation stops. Persistent matches remain visible while
other buyers act. Price tags and graph ticks update from the same event state.
Pause at `3.a` after a coherent run segment, not after every person's choice.

### 3.b · Inspect the stopping state

Show the final tableau with all participants visible, including nontraders.
If the mechanism's full improvement check passes, hold that state at `3.b`.
Save the state for the later deviation experiments before altering any prices.
If the run merely became quiet or hit its limit, describe that outcome accurately
and retain it as a tuning case. Do not reuse the current unconditional
“no one wants to change” caption before the check exists.

### 4.a · Compare the outcome with the graph

Fade the world and enlarge the fixed panel. Show the competitive benchmark
computed from the chosen MB/MC data separately from the observed match prices.
For the proposed shared crowd, four units have strictly positive gains and
two more have MB = MC = $4. With zero-gain participation, Q = 6 is supported
at $4. The original companion pools instead support six units at $7; their
current trace includes $7.50 matches. These are different scenarios, not a
price change in the same market. Likewise, distinguish the discrete crowd from
the lecture's smooth aggregate example of 40 thousand pounds at $4.

Explain agreement or a remaining gap based on the tested run. A band chosen
from minimum/maximum observed prices cannot itself prove that “the graph knew.”
Pause at `4.a` with benchmark and observed outcome clearly distinguished.
Then follow the overall storyboard's graph/algebra bridge and deviations;
the discovery branch is the front half of the developing arc.

### 5.a · Caveats, placement pending in the shared script

Keep nontraders visible. The existing caveats about who trades and willingness
to pay versus need remain writing candidates. Replace the old full-information
claim: in the new crowd, buyers checked sampled sellers, not every seller.
Final wording and placement remain with Taylor/Fable. Do not automatically
end the lesson here: the deviation animations follow discovery. These points
can be brief observations at the settled market or join the overall coda.

## Next implementation pass and review

Build the two-player line, shadow, and close-up first. Review `1.a` through
`1.b` before expanding the mechanism to the crowd. Preserve the original scene
until the revised sequence is ready to compare.

- **Model:** check the posted-price bounds, strict improvements, displacement,
  retry, seller waiting/cuts, one match per unit, and no double-counting at
  settlement. Test seed replay and quiet/limit termination separately from
  verified settlement. Keep the existing 25 model tests passing.
- **Accounting:** at 10/4/7, verify expenditure = receipts = 7, CS = PS = 3,
  and CS + PS = 6. Check zero-gain boundaries without negative fill heights.
- **Visuals:** inspect price-height alignment, floor projection, label legibility,
  near-touching bars with unchanged values, region-before-label reveals, and
  the restoration to the plaza. Review forward, backward, replay, and export.
- **Pacing:** hold the small-cast choices; watch the ten-per-side run continuously
  to confirm there are no inherited survey pauses or repetitive camera turns.
- **Writing handoff:** midpoint explanations and exhaustive-search claims are
  superseded; companion CS/PS is now requested. The lecture's Cindy/Amanda-Grace
  naming, pounds/kilograms, multi-unit Gary line, and carrot-market price remain
  writing questions already present in the materials. Do not silently resolve
  them through invented animation content.

Starting asks, random seed, search cadence, and bid/cut sizes are tuning choices
for that pass. The specific small-cast prices above are proposed review fixtures.
No random-search convergence or new rendered frames were validated in this
storyboard-only pass.

## Previous brief and reference notes

The following is the pre-revision working brief, retained verbatim as history.
Its midpoint rules, all-sellers survey, surplus restrictions, and planned engine
paths are superseded where they conflict with the current plan above. Its
reference-video review records an earlier review, not one performed in this pass.

<details>
<summary>Earlier companion brief · September 16–17, 2026</summary>

# B3 Companion | Price Discovery in 3D — Scene Setup

<!-- ED/ANIMATOR (2026-09-16) — separate setup from 01_Notes.md, per chat. The mechanics are your spec, transcribed verbatim in the block below; the formalization, beats, and engine mapping are animator work built on it. The scene follows B3's general arc (one exchange → incentives to switch → settling down is equilibrium → the graph knew it all along) without using the episode's script. Surplus overlays are soft-pedaled: CS/PS visuals belong to B4 (PolicyComparison in Sim/ is already that seed). Scene name placeholder: PriceDiscovery (in Blocks/Sim/, alongside OneAgent/OneTrade/MarketRound). -->

## Your spec (2026-09-16, verbatim from chat)

> lets start by setting up the buyers on one side of the platform with the demand curve locked to the screen, then the opposite side for the sellers, then start with one buyer walking from one seller to the next, leaving a connection visualized somehow with the one it prefers, the one with the lowest price. i want bars over each of their heads representing their MB and MC. then afterward, the buyer goes back to the seller they match with. then a second buyer goes through, including the one that's already selling to the first buyer. each buyer and seller will accept a better offer if it's available. this process continues, until no one wants to change. when an unmatched buyer and a seller match, they pick a price that's halfway between their values. when one is already matched, they pick a price that's halfway between the previous match and the unmatched MB or MC. if someone becomes unmatched, they then start over. i think it's worth having the bars up on the graphs glued to the screen, since that's the easiest way to think about buyers and sellers. and we'll animate these as being matched or not, maybe with a highlight or by showing their ps and cs and the price or something.
>
> then to scale and data. i think we start with one buyer and one seller to get the idea, then we go to two of each to get the mechanics of switching and things. then we go up to maybe 10 each, then maybe more. but lets stop at 10 for now.

## Staging

Three layers, as in Sim/ (world plane · attached info · screen-fixed model):

- **World**: the platform, buyers lined on the left edge, sellers on the right. Each agent carries a **vertical bar over their head** — height = MB for buyers (DEMAND color), MC for sellers (SUPPLY color). Bars are world objects that travel with their agent (extends `attached_label`; the bar is new visual vocabulary for Sim/).
- **Screen-glued model**: the (Q,P) panel `fixed(...)` to the screen. Every head-bar has a twin bar on the panel; the panel twins sort into the descending MB staircase (demand) and ascending MC staircase (supply). A match lights both twins and draws the **price tick** between them; unmatched twins stay dim. This is the "easiest way to think about buyers and sellers" — the panel is the truth the plane acts out.
- **Connection**: a lane/thread on the plane from a buyer to their current seller, carrying the match price as a small label. Tentative while walking (dashed), settled after matching (solid). A displaced thread snaps and the displaced agent's bar dims back to unmatched.

## Mechanics, formalized

State: each agent is unmatched, or matched at a price. One unit per agent (current engine rule; multi-unit buyers deferred).

1. **Walk**: an unmatched buyer walks the seller line. Each seller's *effective ask* is: their current match price if matched, else their MC. The buyer notes the lowest effective ask.
2. **Match, both unmatched**: price = (MB + MC) / 2.
3. **Displace, one side matched**: the newcomer must beat the standing deal — price = (standing match price + newcomer's MB or MC) / 2. The seller accepts a higher price; a buyer accepts a lower one. The displaced agent becomes unmatched and starts over (walks again).
4. **Participation**: nobody deals at a loss — a buyer never pays above their MB, a seller never sells below their MC. If the best available deal violates that, the agent stays unmatched (their panel twin stays dim: *not everyone trades*).
5. **Stopping**: rounds continue until no agent can improve their deal — nobody wants to change. Freeze frame; the settled price labels cluster; the panel shows every settled tick sitting in the band where the staircases cross. **This settling down where no one wants to move is equilibrium** — same sentence the episode earns algebraically.

Determinism for the build: agents act in ID order (no randomness, so checkpoints replay exactly). The model rules go in `market_model.py` as pure functions with unit tests (convergence, the displacement chain terminating, settled prices inside [max matched MC, min matched MB], the no-loss rule, ties by ID) before any animation runs.

## Beats (dotted IDs, PriceDiscovery scene)

- `0.a · Platform` — plane in, buyers left, sellers right, head-bars grow in; panel fades in screen-fixed, twins sort into the two staircases.
- `1.a · One buyer, one seller` — B1 (MB 10) and S1 (MC 4) alone. Walk, meet, match at 7. Thread solidifies; panel ticks at 7 between the two bars. *(Reuses OneTrade's 10/4 example so the scenes rhyme.)*
- `1.b · The window` — hold: any price between 4 and 10 would have worked; the midpoint is just their split. (Callback to A3's range of workable rates.)
- `2.a · Two and two` — B2 (MB 12) and S2 (MC 2) join. B2 walks past the matched S1 (effective ask 7) to unmatched S2 (ask 2): match at 7.
- `2.b · The switch` — rerun with data where displacement pays: the newcomer outbids a standing deal, the thread snaps, the displaced buyer starts over and settles elsewhere. The mechanics of "accept a better offer."
- `3.a · Ten and ten` — full cast walks in ID order. Threads form, snap, reform; panel ticks accumulate. Let it run visibly unnarrated for a beat.
- `3.b · Settling` — activity slows and stops: no one wants to change. Settled ticks cluster in one band.
- `4.a · The graph knew` — camera holds on the panel: the band the prices found is exactly where the staircases cross. (The episode's algebra will name this point; the class's pit-market histogram is this frame in real life.)
- `5.a · Caveats (optional, from the .typ)` — dim twins linger: not everyone trades; a high-MB buyer who never needed it most can outbid; the walk assumed everyone could see every ask (information matters).

## Scale and data

| Stage | Cast | Data |
|---|---|---|
| 1×1 | B1/S1 | MB 10, MC 4 (OneTrade's numbers) |
| 2×2 | +B2/S2 | MB 12, MC 2 (Sim's existing constants) |
| 10×10 | full | proposed default: MB = 12, 11, …, 3; MC = 2, 3, …, 11 — crossing band ≈ $7, about 5 matches; integer midpoints throughout |

Stop at 10 (per spec). The 10×10 lists are an animator default — swap freely; they live as constants at the top of the scene file. Note the companion's crowd is its own small world: the episode's market curves (S: 2 + Q/20, D: 12 − Q/5, in thousands of pounds) are the limit this staircase gestures at, not this cast's literal data.

## Engine work before animation

1. `market_model.py`: matching/displacement/stopping rules as pure functions + tests (the current `clear_market` is a benchmark at a posted price — this is the new piece).
2. `scene_layers.py`/scene: head-bars (world) with panel twins (fixed), thread objects with price labels, dim/lit match states.
3. Layout: ROWS to 10 per side; panel range fitting MB 12 → MC 2.
4. Open cosmetic decisions (yours, from the notes' Companion section): Marryville vs Maryville; the commodity (B_Outline says rice); whether the class's actual card deck becomes the 10×10 data in a later pass.

</details>
