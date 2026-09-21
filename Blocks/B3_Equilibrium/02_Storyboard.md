# B3 · Build equilibrium, then test deviations

Current animation storyboard · September 21, 2026

## Entry point and ownership

Run `maniml Blocks/B3_Equilibrium/03_Equilibrium.py EpisodeB3` from the project
root. This is the fresh, flat episode: one sequential `construct()`, literal
pause IDs, the shared B1/B2 bumper, 15 fps, 2160×1080. The pure posted-price
rules (sampled visits and full surveys) live in `Blocks/Sim/discovery.py`;
they contain no choreography.

[01_Notes.md](01_Notes.md) is Taylor/Fable's read-only script source. The animator
edits the storyboard and code. Taylor's original animation directions remain
[verbatim in the detailed storyboard](02_Companion_Storyboard.md#taylors-animation-directions-verbatim).
`Animate.py`, `Animate_A.py`, and their detailed storyboards are references and
history. Their old episode/companion division and pause IDs do not govern this
new single episode. The map below supersedes earlier proposals.

**Review cadence:** edit in the connected ManimLive development viewer,
which hot-reloads this scene from a safe checkpoint. Inspect the live frame
and nearby motion after saving. Use targeted stills/clips as a fallback; reserve
full exports for deliverables or larger milestones. The static movie viewer
does not hot-reload. The scene reloads its pure discovery module too, so
changes to search rules are picked up by the same live session. See the
animator workflow in `Blocks/_Style_Guide.md` §8.

**Order:** first pair → side-view deliberation → payment and gains → Amanda-Grace’s
incentive and buyer bidding → gradual arrivals → crowd discovers a price → name equilibrium → introduce the graph/recap →
algebra → deviations. Taylor's latest review adds separate MB/MC curves during
the buildup; their combination and the algebra still follow discovery. The
approved first Gary/Molly staging is retained, with MC and its cost area staying orange.
The accounting follow-up carries expenditure’s green boundary to Molly as
revenue and draws an inset orange PS outline.

**Text in the plaza:** names, marginal values, offers, posted dollar tags, and
the close-up accounting labels are world-space text. Reuse `Animate.py`'s
`face_camera` updater: turn the glyphs toward the camera while retaining their
3D anchors and world scale. Names sit just in front of their people at z=0.13;
Gary/Molly's first labels sit 0.75 units outward to clear the orbs in side view.
Values sit 0.28 units above their bars; dollar tags stay beside the seller/trade.
They follow movement, camera zooms, and backward seeks. Rebuild a rolling
number's flat glyph geometry when its value changes before facing it again.
Titles, bottom questions, and labels belonging to the two side graphs retain
their screen layout. The new episode keeps this one small orientation helper;
choreography remains sequential inside `construct()`.

**Price visibility in the 3D market:** use a 4.5-pixel red stroke for
accepted prices and world-space offers throughout the plaza buildup and
deviations. The pullback brings the original accepted price to that same
width. Ground shadows use a 2.4-pixel stroke at the existing 0.3 opacity,
keeping the elevated price prominent. Close-up bids and graph guides retain
their existing widths.

## First pair and deliberate decisions

| Pause | Script / action | Stopped frame |
|---|---|---|
| `0.a` | Shared MICROECONOMICS bumper, Part B / Episode 3 | Notes' thesis, “Equilibrium: when no one wants to change.” |
| `2.a` | Notes 1.a/2.a: the question and the first exchange | Gary and Molly start nearby (x=±1.65), with no offered price yet. Teal MB $6, orange MC $2 above their orbs. Question title: “Would they exchange?” |
| `2.a.i` | Taylor's first-deliberation direction | Camera faces the pair from the side. Buyer left, seller right at x=±1.45; their original bars move inward between them, broaden to 1.10 units with a 0.12 gap. Molly’s MC bar, label, and orb remain orange throughout. Dashed red offer at $4, matching faint floor shadow. Only the bottom question, “Would they both accept this price?”, enters after the camera settles. No payoff labels yet. |
| `2.b` | Accept on advance | Remove question; fill the gaps in the stationary red price and shadow over 0.45 seconds. The existing dashes and price label remain fixed as the offer becomes solid. |
| `2.b.i` | Recall B1 expenditure | Green area 0–4 on the buyer's bar, then “Expenditure $4.” |
| `2.b.ii` | Recall B1 CS | Teal area 4–6, then “CS $2.” |
| `2.b.iii` | Carry the payment from buyer to seller | Trace a green, unfilled copy of Gary’s expenditure boundary, then slide it horizontally by 1.22 units onto Molly’s side without changing its size or dollar height (0–4). Gary’s expenditure fill stays in place. After the outline arrives, reveal green “Revenue $4.” Keep the revenue boundary through Cost and PS. |
| `2.b.iv` | Move the marginal-cost label | Keep the orange area 0–2. Slide the existing orange “MC $2” label from above its bar to the right of that lower area in 1.2 seconds, as the area settles into the accounting view. Do not replace it with “Cost.” Restore its above-bar tracking position before Amanda-Grace's first offer. |
| `2.b.v` | Producer surplus | Outline the upper region between MC $2 and price $4 in orange, with no orange fill; inset the border 0.045 world units on all four sides so it fits visibly inside the green revenue boundary. This inset is a highlight margin, not a change to the $2 surplus. Then reveal “PS $2.” Expenditure equals revenue; total gain $4 = 6−2. |
| `2.b.vi` | Make the single-unit interpretation explicit | “One unit” bottom caption. Bars have widened visually; quantities have not changed. |
| `2.c` | Center the three-person close-up on the plaza | Keep the first pair's head-on camera at center (0, 0, 2.05), height 7.2, and original world scale. Slide Gary and Molly 1.45 units left: Gary at x=−2.9, Molly at x=0. Amanda-Grace enters at x=2.9, all y=0, balanced around the plaza center. Move the existing bars, names, and $4 line with the pair. All three people then stay still throughout bidding; only Molly's MC switches between the two MBs. No side curves yet. |
| `2.c.i` | Compare a new offer with the standing deal | Show Amanda-Grace’s dashed $4.25 line and label in the right-hand comparison, while Gary’s solid $4 line and label remain on the left. Hold “Would Amanda-Grace gain by offering $4.25?” Both MBs stay fully visible. On advance, slide only Molly’s MC bar and attached MC label to Amanda-Grace’s side. After the slide, fill the new offer's gaps in place over 0.45 seconds while fading Gary’s former line/price. The new dashes, endpoints, and price number never shift during acceptance; its floor shadow fills in the same way. |
| `2.c.accepted` | Make her incentive explicit | Hold “Amanda-Grace gains $7−$4.25=$2.75.” Her $4.25 line is now solid; MC $2 is beside MB $7. All people and both MB bars remain at their original positions. |
| `2.c.ii` | Gary responds without walking | Show Gary’s dashed $4.50 offer alongside Amanda-Grace’s standing solid $4.25. Pause before Molly’s MC moves back to Gary; then solidify his offer and remove the old deal. Continue the same offer → MC slide → acceptance sequence for the remaining quarter-dollar bids. |
| `2.c.iii` | Finish the bidding before pulling back | Amanda-Grace wins at $6.25. Keep Gary’s MB $6 and her MB $7 fully visible with “Gary: next bid $6.50 > MB $6.” Only after this hold does the camera pull out to the plaza. The two sorted marginal curves enter with the two existing buyers and Molly’s posted $6.25; Andrew then arrives. |

The old `2.d`–`2.d.ii` Andrew comparison is removed from this teaching scene.
Andrew enters deliberately during the growing market: an MC-$4 bar followed
by an ask of $4.25 just above it. Both existing buyers return to the lookout
and compare visible options. No transition moves Molly to the buyer side.

All dollar heights share `z = baseline + scale × dollars`; the ground connection
is the projection of those exact endpoints. In the plaza, dashed connections
mean contemplated; solid means accepted but still revisable. On the supply
graph, dashed red markers record standing posted prices; solid red highlights
show a buyer's contemplated offer. No cancelled deal is counted as completed
trade or accumulated surplus. Payment/cost colors and reveal order begin from
B1/B2; Taylor’s latest correction replaces B2’s white revenue boundary with a
green boundary transferred from expenditure, and its PS fill with an outline.

## Crowd and stopping state

| Pause | Action | Stopped frame |
|---|---|---|
| `3.a.plaza` | Keep the bidding outcome through one pullback | Clear the question and marginal/name labels, retaining the accepted $6.25 line, its shadow, and price number. Keep the approved 2.2-second pullback, final 48° tilt, height 10.4, and final market positions. From the centered close-up, Molly reaches (3.5, 1.2) on the seller arc, Amanda-Grace reaches (4.1, 0.85) beside her, and Gary reaches his buyer-arc place, approximately (−3.53, 1.12). Keep the center empty. Bring the same people, bars, and price line to their normal plaza sizes and compact paired positions. Hold before adding graphs. |
| `3.a.overview` | Add the two marginal curves together | Both side panels and their sorted columns fade in together where they belong: MB $7/$6 on the left, MC $2 on the right. No copies fly across the plaza. Carry the $6.25 number to Molly's compact price tag, add her dashed graph price, and retain the original solid world-price line. Hold before Andrew enters. |
| `3.a.entry` | Andrew enters deliberately | Keep the settled camera, Molly’s station, and Amanda-Grace’s $6.25 deal. Andrew enters at another fixed seller station; show MC $4 first, then his price $4.25 just above it in the world and supply graph. The price caption reads only “$4.25,” without “Ask.” Retain the four names for these decisions. Gary is still unmatched. |
| `3.a.switch.options` | Amanda-Grace reconsiders | She returns to the hub. Highlight her MB-$7 bar and compare Molly $6.25 with Andrew $4.25 on the supply graph. Hold “Would Amanda-Grace keep paying $6.25?” |
| `3.a.switch.accepted` | Choose the lower price | She walks to Andrew at $4.25. Molly stays put, now without a buyer. |
| `3.a.counter.options` | Gary reconsiders | Gary enters the hub. Highlight MB $6; show Molly’s open $6.25 ask versus the $4.50 needed to outbid Amanda-Grace at Andrew. Hold “Could Gary gain by offering $4.50?” |
| `3.a.counter.accepted` | Gary makes the affordable bid | Gary walks to Andrew at $4.50; Amanda-Grace returns to her waiting place on the buyer arc. Both sellers stay in place. Continue bargaining with these four people before admitting anyone else. |
| `3.a.seller.cut` | Molly responds to losing her buyer | Buyers bid Andrew through $4.75 and $5. Show Molly still at $6.25 without a buyer; ask whether she would lower her price. Then her price falls to $6. Subsequent bids and cuts bring both sellers to $5.50. Each buyer visits the center with their demand column highlighted, compares a dashed MB guide against red required-price lines over every present MC column, then selects a seller. |
| `3.a.two_pairs` | Complete the two-by-two | Gary trades with Andrew; Amanda-Grace trades with Molly. Both prices are $5.50. MBs remain $6/$7 and MCs $2/$4, so all four gain. Hold “Both trades: $5.50. Gary's gain: $0.50.” This is a demonstrated path to equal prices, not a claim that every quarter-dollar path gives equality. |
| `3.a.third_buyer` | Add only a buyer | A new buyer with MB $8 enters; supply remains exactly two units. Retain Gary, Amanda-Grace, Molly, and Andrew's names, and label the entrant “New buyer.” |
| `3.a.third.lookout` | Stop when the third buyer reaches the circle | Buyer stationary in the center, demand column highlighted, dashed MB $8 guide on supply. Advance to reveal the sellers' offers and the existing price-choice question. |
| `3.a.third.options` | A third bidder wants a unit | The new buyer enters the center, compares the two sellers, and considers $5.75 at Molly. MB $8 makes this strictly beneficial. Ask “Would the new buyer offer $5.75?” before acceptance. |
| `3.a.excluded` | Three buyers, two units | Continue permitted outbids to two prices of $6.25. The new buyer trades with Molly; Amanda-Grace trades with Andrew. Gary returns to his buyer-arc place. Keep his MB $6 visible in the demand curve and ask “Why is Gary left out?” |
| `3.a.excluded.reason` | Compare Gary's two situations | Hold “Gary traded at $5.50. Now $6.25 > MB $6.” Gary's benefit and both sellers' costs have not changed. His earlier positive gain demonstrates that he was willing and able to trade in the two-by-two; the higher-value third buyer changes the allocation. |
| `3.a` | A third seller restores an option | With three buyers still present, add an MC-$4 seller posting $4.50. Insert its MC bar and dashed price in the supply curve. Fade out plaza price labels now that there are three sellers. Gary is still waiting; the new buyer and Amanda-Grace hold the other two units at $6.25. |
| `3.a.lookout` | Gary reconsiders | Gary returns to the center. Highlight his unchanged MB-$6 bar, dim the other two buyers and their standing connections, and keep all three sellers visible. |
| `3.a.options` | Read the three options | Highlight each world seller and its supply column together. Needed prices are $6.50 to outbid at Molly, $4.50 at the new seller, and $6.50 to outbid at Andrew. Add the teal MB-$6 guide. Hold “Would Gary trade with the new seller?” Only the new seller is affordable. |
| `3.a.chosen` | Gary trades again | Gary walks from the hub to the new seller at $4.50. Show the short accepted-price connection and floor shadow. Hold before restoring the other buyers and fading the small-cast names. Then continue one-person-at-a-time growth. |
| `3.a.i` | Grow from six to eight | Add the next buyer and seller separately. After each arrival, let the present market respond before admitting anyone else. Pause with four of each after those responses. |
| `3.a.growth.B{i}.lookout` | Stop at each new buyer in the circle | Buyers B2, B3, B5, B6, B7, B8, and B9 each get a distinct arrival pause immediately after reaching the hub with their demand column highlighted. This also applies when none of the sellers is affordable. Advancing reveals the full MB/price comparison. |
| `3.a.growth.*` / `3.a.ii` | Continue one person at a time to ten of each | Each newcomer first joins the sorted curve. A new buyer enters the hub and stops at `.lookout`, then compares all current sellers, including when every offer exceeds MB. Existing buyers reconsider and unsold sellers lower asks before the next arrival. Carry every match and price forward. Retain `.options` for each visible decision, `.accepted` or `.declined` for its result, and `.settled` after each arrival. Keep plaza price labels absent; red dashed posted prices remain on all supply columns. |
| `3.b` | Inspect the market already reached | Ten buyers and ten sellers are present, with six trades at $4. There is no deferred full-market trading batch. Every visible deliberation during growth uses the demand highlight, dashed MB guide across supply, and red required-price lines over **all** present MC columns. Highlight the selected seller after the comparison; displaced buyers return to waiting. Seller cuts move their persistent red dashed markers downward. |
| `4.a` | Name the stopping state | Six accepted trades at $4 in the presentation run. Keep nontraders visible. Bottom definition: “Equilibrium is where no one wants to change.” Gold arrow points to a settled price. |

Fixture, updated for the unequal-MB bidding scene:

- MB: `[6, 8, 4, 3, 7, 5, 4, 3, 2, 2]`.
- MC: `[2, 4, 3, 5, 4, 2, 6, 3, 5, 6]`.
- Gary B0; Amanda-Grace B4; new buyer B1 (MB $8); Molly S0; Andrew S4.
- Growth begins from the worked three-by-three: B0→S1 at $4.50, B1→S0
  and B4→S4 at $6.25. The next arrival inherits these prices and matches.
- Thereafter add B2, S2, B3, S3, B5, S5, B6, S6, B7, S7, B8, S8,
  B9, S9. Carry active prices/matches into each new run; never include absent
  buyers or sellers. Each incoming buyer compares first, even if no option is
  affordable. Later sellers retain the existing $6 starting asks.
- Survey mode compares every seller and chooses the cheapest worthwhile offer,
  with seeded ties (seed 6). Buyers keep their current reservation on a tie.
  Each arrival's responses settle before the next person enters. This chosen
  trace has 37 successful visits and finishes with six trades at $4, total
  gains $16. The earlier sampled-search fixture remains a regression test.
- The three-person bidding trace is the existing model with values [6, 7],
  cost [2], initial ask [4], Gary initially matched, seed 0.
- Andrew’s new entry trace is $4.25 at MC $4; Amanda-Grace switches from Molly’s
  $6.25; Gary then outbids her at Andrew for $4.50. Seed 54 continues this
  two-by-two to $5.50 at both sellers in four rounds. Seed 6 then adds the
  MB-$8 buyer and reaches two $6.25 prices in five rounds, excluding Gary.
  Both paths are actual model traces, with every bid/cut checked.
  The former two-$6-deal fixture
  remains only as a model regression test. The $0.25 process can
  settle at unequal nearby prices on other paths; the common $4 is shown
  through actual permitted actions in the chosen trace.

Stopping is an exhaustive audit of permitted improvements, not a quiet random
round. The tick-based search rule is not a proof of general convergence or of
stability against every possible strategy. At the uniform $4 benchmark,
Qd = Qs = 6, counting indifferent participants. Sorted marginal units have four
strictly positive gains and two zero gains; this is not a claim that each
observed pair has the same surplus split as that sorted pairing.

## Graph bridge and algebra (implemented after discovery)

| Pause | Action | Values / reveal order |
|---|---|---|
| `4.b` | Bring the two curves together in the center | Fade the plaza, people, marginal bars, world-price lines, and hub over 0.8 seconds while the two side graph panels stay intact. Reset the camera only after the world is hidden. Move both already-sorted sets of bars together onto centered axes (center x=0, y=0.1; x 0–10, y 0–8) in one 1.8-second play as the side axes and posted prices fade. Keep all units in their original rank order. Reduce the bar fill to 0.06 and remove their box borders as they move. Reveal continuous three-pixel staircases tracing the tops, with vertical connectors only where marginal values change; no full-height dividers. Keep the faint area beneath each curve. Then reveal the red price/quantity guides with “P=$4” beside the price axis and “Qd=Qs=6” below the quantity axis, both at scale 0.7. The price label replaces the grey 4 tick during this hold; restore that tick while the graph is hidden before its later reuse. No camera slide or plaza beneath the merging bars. |
| `4.c` | Move to the aggregate example | Fade the centered unit graph. While hidden, shift its complete axis, bars, and step outlines four units right to preserve the later plaza-and-graph deviation layout. Explicit caption “Q in thousands of pounds.” New aggregate axes x 0–90, y 0–13; D: P=12−Q/5, S: P=2+Q/20. These curves represent a larger market, not a rescaling of six people. Leave numerical equilibrium answers off the graph. |
| `4.c.i` | Carry the equations into the working | Copies of the orange supply and teal demand equations travel from their graph labels to two rows in the right-hand math area over 1.5 seconds. Leave the graph labels intact; recolor only P and Q in the copies red. Hold before equating their right-hand sides. |
| `4.d.collect`, `4.d.simplify`, `4.d` | Solve quantity by moving its terms | Move the two right-hand sides into 2+Q/20=12−Q/5. Keep completed lines above the active row. Move a copy of the demand fraction left and the orange 2 right, changing their signs to give Q/20+Q/5=12−2; hold, then combine 12−2 into a neutral 10. Factor the two red Qs into Q(1/20+1/5)=10, retaining orange 1/20 and teal 1/5. Combine the coefficients into Q/4=10 and hold. Move the denominator 4 across the equality to form Q=10×4, then combine the product into red Q*=40. Equality signs and newly combined constants are neutral; source terms and their signs retain their curve colors until combined. Math remains scale 0.8, with equals signs aligned at x=4.4 and completed rows at y=2.15, 1.20, 0.25, −0.70. |
| `4.d.i` | Substitute the calculated quantity | Copy the orange supply equation from its graph label into a new row at y=−1.65, with P and Q red. Move a copy of the red 40 from Q*=40 into its numerator as Q disappears and P gains its star. Keep P*=2+40/20 visible above a final row at y=−2.60; reduce the fraction to 2, then combine 2+2 into red P*=$4. |
| `4.e` | Read the combined graph | Red point and guides at (40,4); starred quantity and price. This fresh scene uses one combined graph from the bridge rather than introducing duplicate graphs just before combining them. |

Use B1/B2's grey divider, question titles, 0.7 minimum type, graph-to-math number
transfers, and unknown-before-answer convention. The six units in the toy world
are never labeled 40,000 pounds. Keep the representation change visible.

## Exercise pauses and deviations (refinement pass)

The exercise cards follow the editor-owned `Exercise/Exercise_B3.typ`, read on
September 21. They are a separate pumpkin-pasties market, measured in galleons
and pasties: demand P=12−Qd/2, supply P=2+Qs/2. Do not carry the spinach
example's numerical answers into these cards, and do not reveal exercise answers.
Use B2's serif gold heading, slightly indented white prompts, opaque rounded
panel, and dimmed stage. Literal pauses remain available in the live viewer.

| Pause | Action | Arithmetic / staging |
|---|---|---|
| `4.exercise` | Exercise B3 Q1, after the worked equilibrium graph | Show the sheet's two curves and units. Ask for equilibrium quantity, equilibrium price, and the graph with the starred pair. |
| `5.a.s.question`, `5.a.d.question`, `5.a` | $3 below equilibrium; supply then demand | Copy each colored graph equation into the math area; P and Qs/Qd become red. Copy the red price into P, move terms across the equality, move the denominator to multiply, and collect the result. Leave the original equation and completed algebra visible. Carry red Qs=20 and Qd=45 back to their unknown graph readouts. Highlight the gap at the selected price. |
| `5.b` | Return to the one-unit plaza and name shortage | Discrete Qs=4, Qd=8, with separate red drops/readouts and P=$3 on the unit graph. Matched marginals dock at width 0.18, gap 0.035; accepted price lines span only the compact pair and sit 0.015 units toward the camera to prevent coplanar occlusion. Unmatched buyers wait on their own arc, with blue rings identifying the willing buyers left out. Sellers remain fixed. |
| `5.b.lookout`, `5.b.options`, `5.b.i` | Amanda-Grace bids $3.25 for Molly | Show Gary, Molly, and Amanda-Grace with their existing camera-facing world names. Amanda-Grace enters the dashed center circle with a blue floor ring. Highlight her demand column, extend her MB as a dashed guide across the combined graph, and show required red offers over every seller's MC, including the outbid increment. Seller highlights use unfilled outlines, preserving the faint staircase shading. Highlight Molly's offer, return Gary to his buyer slot, move Amanda-Grace to Molly, dock the marginals, then show the solid accepted price. |
| `5.c.round…`, `5.c` | Continuous upward adjustment | Retain unchanged pairs and links. Show only changed buyers moving and changed sellers' price markers/arrows. Undock before switching, dock after arrival, and keep prices attached to the compact pair. Each changed round has a skip pause. At settlement restore P=$4 and Qd=Qs=6. |
| `5.d.s.question`, `5.d.d.question`, `5.d` | $6 above equilibrium | Same colored, term-by-term arithmetic: aggregate Qs=80, Qd=30. Discrete Qs=10, Qd=3. Show leftover units beside their stationary sellers. |
| `5.d.i`, `5.e` | Name excess; distinguish the textbook term | Bottom definition points to unsold units. The brief crossed-out “Surplus” and replacement “Excess” sit in the screen's bottom caption band, outside the plaza action. |
| `5.f.lookout`, `5.f.options`, `5.f` | Molly cuts $6→$5; Gary reconsiders | Gary starts with Andrew, the new buyer with S1, Amanda-Grace with S5. Molly's price falls on the supply column. Gary's blue ring follows him to the lookout; compare his MB and every required seller price before he chooses Molly. Names remain attached to Gary, Andrew, and Molly. |
| `5.g.round…`, `5.g` | Continuous downward adjustment | Same compact pairs and selective movement as the shortage return. Unsold sellers cut; buyers move to strictly better prices. End with six $4 trades. |
| `5.h`, `5.h.i.offer`, `5.h.i`, `5.h.ii`, `5.h.iii` | Test actual marginal participants | Keep the allocation from the just-completed excess adjustment. Do not reshuffle people to another equally valid equilibrium. For each actual marginal participant, fade unrelated people and zoom the real pair to a side-on view at the left of the fixed unit graph. Camera height 3.4 makes the quarter-dollar proposal legible; camera-facing MB/MC labels stay attached to the bars. Highlight an MB-$4 buyer and partner, show a dashed $4.25 proposal, pause to consider it, then show refusal with a short step back. Restore the same $4 match and explicitly re-establish its visible solid stroke at each close-up handoff. Highlight an MC-$4 seller for a dashed $3.75 bid, pause, then reject it and retain the accepted $4 trade. Return smoothly to the plaza after each test. Use the same world rings, graph column/MB/MC highlights, red proposals, and compact bars as the first half. |
| `5.exercise` | Exercise B3 Q2, after stability | Show the same pasty curves and units. At 5 galleons, ask for Qd, Qs, shortage/excess and its size, and the direction of price movement. No solution on the card. |

The aggregate calculations use the full graph and side calculation, then return
to the plaza beside its own **Units** graph. The two representations share price,
not quantity. At $3 the four initially matched buyers are B0–B3, leaving
Amanda-Grace unserved. At $6 Gary starts with Andrew, the new buyer with S1,
and Amanda-Grace with S5. These staged allocations illustrate the deviations;
they are not described as the random discovery outcome.
After the named offer, seeded random search resumes (upward seed 473;
downward seed 361). Both traces must pass the stopping audit and end with six
$4 trades. During individual price changes, remove the common-price readout;
keep every seller's posted price on the supply columns. The final stability
tests use actual, potentially different pairs from the final excess-adjustment state.

## Reconciliation with the live notes

Taylor's latest review preserves the first Gary/Molly scene and replaces
simultaneous entrances with sequential arrivals. Amanda-Grace's MB is now $7
in animation code; the notes' cast comment still says $6 and belongs to the
editor. The newer `2.c` prose already describes buyer first, seller second,
then one-at-a-time expansion. Taylor’s latest staging finishes the two-by-two
at $5.50 before adding the MB-$8 buyer. Gary’s unchanged MB $6 makes the
three-by-two exclusion at $6.25 explicit. The third seller then offers him a
trade again. These extensions run ahead of the editor’s prose; notes stay untouched.

Taylor's latest direction supersedes the earlier “no graph before discovery”
restriction for the two separate marginal curves. They now begin after the
entire close-up bidding war, at `3.a.overview`, and stay on opposite sides of
the plaza. The shared unit graph still
appears at `4.b`, and aggregate algebra at `4.c`. No notes edits are needed to
implement this staging correction.

The original `Animate.py` provides the dashed radius-0.35, twelve-dash lookout
ring and the buyer → center → seller movement. The current scene uses those
visuals with its existing posted-price/outbid rules, not the historical
midpoint-bargaining prices. Left and right panels each retain a dollar axis
0–8. Their horizontal scale expands from the current participant count to ten;
bar widths shrink as people join, so all present people remain legible. Neither
side imports absent participants. MB sorts descending; MC sorts ascending,
with stable participant IDs resolving ties.

The side panels are centered at x=−5.9 and +5.9, with 3×3.5 axes and a fixed
0–8 dollar range. Red dashed posted-price markers begin with Molly, then follow
every seller's sorted MC column. Plaza prices remain through Andrew's entry
and both buyer decisions; the third seller triggers their removal. Solid red
highlights show the price needed for a particular choice, including the extra
$0.25 for an occupied seller. After the separate curves combine, per-seller
markers return on the unit graph during deviations; plaza price labels stay off.
The crowd camera height is 10.4. Buyers and sellers occupy centered radius-3.7
arcs on their respective sides. Gary waits at approximately (−3.53, 1.12),
and Amanda-Grace at (−3.68, 0.37) whenever unmatched. Gary's slot is swapped
with the original fourth slot so all ten waiting places remain distinct.
The center is reserved for a buyer actively comparing options. During the initial
pullback she stays to Molly's right, with MC left and MB right; after she leaves
that first match, subsequent paired bars resume the usual MB-left/MC-right order.
Both side graphs enter together only after the camera has settled. Molly's carried
price tag sits 0.65 units right of her MC bar, 0.25 above the current price
height, clear of the compact red line. The initial $6.25 readout changes to its
tracked tag in the same position. Andrew's entry price retains its position
beside his body. Amanda-Grace's name sits 0.55 units toward the front and up
to 0.65 units toward the plaza center, blending its modest side offset as she
crosses the hub. This keeps the name close to her orb, clear of Andrew, and
inside the plaza when she returns to the buyer arc.
After the centered close-up resolves into the market, Molly keeps her
(3.5, 1.2) station, Andrew stays
at (3.5, −1.2), and further sellers fill the right arc. Only buyers walk between
stations and the center. The worked survey highlights the three world sellers
and their corresponding supply columns in the same order before the question
pause. Every later deliberation retains that full comparison: demand-column
highlight first, then a dashed teal MB line spanning supply, then solid red
required prices over every MC. After the worked three-by-three, show one
legible selected price below the graph instead of packing numerals into each
narrow column. Seller highlights are outlines; redraw the MB guide and price
lines above them so every option stays visible, including prices equal to MC.
The needed price includes a quarter-dollar outbid at another buyer's reserved
seller; one's own price remains the comparison baseline. An unaffordable
newcomer returns to waiting after “Every offer exceeds this buyer’s MB.”
Unchanged background checks are omitted; visible decisions are never reduced
to a single unexplained seller highlight.

Whenever a buyer's demand column is highlighted, add a matching buyer-blue
(`DEMAND`) floor ring around that person: radius 0.29, stroke width 3, z=0.045,
the same geometry as the small-market seller rings. The ring moves in the same plays as the buyer, with explicit floor positions
and no body-tracking updater. It follows the buyer into the lookout and onward to a chosen seller or back to waiting. Keep it
through the arrival, options, and decision holds; fade it with the demand
highlight. Apply this to Andrew's entry, the two-by-two/three-by-two decisions,
the worked three-by-three survey, and every growth deliberation. Gary also
gets the ring at his waiting place during “Why is Gary left out?”

Each newly added buyer has a named `.lookout` stop immediately after entering
the deliberation circle, followed by the existing `.options` stop. The current
ManimLive development viewer builds an enclosing loop in one continuous first
execution; additional pause calls do not interrupt that initial build. Prepare
the growth checkpoints by jumping to `3.b`, then return to the buildup to use
forward/back between its authored stops. This is a live checkpoint preparation,
not a movie export. A later edit inside the loop requires preparing it again.

Matched plaza marginals are 0.18 wide, with a 0.035 gap, centered between the
neighboring buyer and seller (buyer left, seller right, common depth). They
slide together after acceptance and separate when a buyer reconsiders or is
displaced. The red price segment and floor shadow span only this compact pair
(0.395 units). Seller bodies stay at their stations. This staging applies to
the growth sequence, both deviation runs, and the final stability tests.

Taylor explicitly deferred the PPF tieback on September 21. Leave its stage
treatment and the following B4 closing for that later pass; this pass ends at
the second exercise card after the stability tests.

## Remaining writing-dependent material

The final PPF tieback needs a carrot price or permission to reuse A3's explicitly
illustrative exchange ratio. Do not derive a carrot price from the spinach
market. The exercise files now supply the prompts used above. Do not invent
lecture prose or add unsupported numerical markets for the PPF tieback.
B4 is the next block, not B5.

## Validation record

- September 21 back-half refinement: added the two exercise holds from the
  current editor-owned pasty handout, with its own curves and units and no
  answers. Rebuilt both price calculations using colored graph-equation
  copies, red selected values, explicit term movement, and answers carried
  back to the graph. Live-reviewed the exercise cards, calculation layouts,
  named decisions, compact plaza pairs, and both side-on stability tests.
  Market adjustment preserves unchanged pairs and pauses at changed rounds;
  the stability tests retain the final allocation. The discovery model's 20
  tests pass, as do source compilation and whitespace checks. Corrected
  unintentional filled highlights and coplanar price-line occlusion during
  visual review. Used live checkpoints throughout; no video or checkpoint
  image export. Notes and exercise files remain editor-owned; the PPF tieback
  and B4 closing remain deferred at Taylor's request.

- September 21 Amanda-Grace name spacing: reduced her maximum inward offset
  from 1.8 to 0.65 world units, retaining the existing front offset and camera
  facing. Checked the reported “Why is Gary left out?” hold, her deliberation
  in the hub, and her waiting position after being outbid. The name stays
  close and clears Andrew and the side graphs. All other choreography is
  unchanged; syntax/whitespace checks pass. Refreshed the live market
  checkpoints and left the viewer on the reported hold.

- September 21 staircase refinement: reduced the combined graph's bar fills
  from 0.20 to 0.06 and removed box borders. Each curve is now one continuous
  top boundary with vertical joins at value changes. Live-reviewed the final
  graph: the faint areas remain visible, equal-height units form plateaus,
  and the red price/quantity guides and readouts remain clear. Syntax and
  whitespace checks pass; no export. The reused deviation graph shares this
  same lighter styling.

- September 21 price readout: added red “P=$4” at the left end of the centered
  graph's price guide, matching the quantity readout. It replaces the grey 4
  tick for this hold; the tick returns while hidden for later reuse. Checked
  its alignment and spacing in the live viewer; syntax/whitespace checks pass.

- September 21 graph transition: faded the entire plaza before combining the
  side curves. Both sorted bar sets now move together onto centered unit axes,
  followed by the step outlines and $4 / six-unit guides. Live-reviewed the
  cleared plaza, centered result, algebra handoff, and backward return. The
  hidden graph shifts right four units before reuse in deviations, restoring
  its previous coordinates. Earlier discovery and later algebra/deviation
  choreography are unchanged. Syntax and whitespace checks pass; no export.

- September 21 buyer rings: added the buyer-colored floor highlight to each
  deliberation and to Gary's exclusion explanation. Rings use explicit
  movements alongside the buyer, with no tracking updater or body reference.
  Rebuilt only the B3 live preview after mixed playback states displaced
  objects during review. Verified Amanda-Grace's comparison and acceptance,
  backward restoration, and Gary's third-seller trade with compact marginals
  and correctly placed prices. Prepared the full growth checkpoints. An AST
  comparison confirms that removing the ring additions leaves all existing
  choreography unchanged. Syntax and whitespace checks pass.

- September 21 price visibility: increased all elevated 3D market price and
  offer strokes to 4.5, and their ground shadows to 2.4 at 0.3 opacity.
  Live-reviewed the first plaza pair, market growth, and the settled ten-by-ten
  market. Refreshed the growth checkpoints for arrow navigation; syntax and
  whitespace checks pass. No movie or checkpoint-image export was needed.

- September 21 centered-close-up correction: retained the first Gary/Molly
  scene and its camera framing. The pair shifts left 1.45 units to admit
  Amanda-Grace, producing a centered −2.9/0/+2.9 lineup on y=0. Live-reviewed
  the three-person entrance, final $6.25 comparison, and subsequent pullback.
  The plaza is balanced behind the close-up; the approved final market
  positions, 2.2-second pullback timing, and final camera are unchanged.
  Syntax/whitespace checks pass. No movie or checkpoint-image export needed.

- September 21 buyer navigation: added eight circle-arrival pauses, one for
  the third buyer and seven during subsequent growth. Checked the simulation
  trace for exactly one first comparison per entrant, including unaffordable
  entrants. Prepared the live growth history through `3.b` without an export;
  the viewer now has eight additional checkpoints. Verified the tenth buyer
  remains in the circle with its demand column highlighted, forward stops at
  the price comparison, and back returns to the arrival hold. Syntax and
  whitespace checks pass. First execution of an uncached enclosing loop still
  runs continuously; the preview preparation described above is required.

- September 21 plaza placement correction: centered both market arcs at radius
  3.7 and fitted the head-on bidding tableau around Molly's actual station.
  Verified from the source geometry that every bidding body and shadow fits
  inside the plaza, Molly's station is identical before/after the pullback,
  and each arc has ten distinct places. Live-reviewed the preserved close-up,
  moving pullback, Gary on the buyer arc, Amanda-Grace beside Molly, side-graph
  reveal, and Andrew's entrance. The carried price stays legible while scaling;
  Amanda-Grace's name clears Andrew's MC and faces into the plaza. The revised
  arcs also complete the ten-by-ten buildup at six trades/$4 with the existing
  per-round assertions. All 20 discovery tests and syntax/whitespace checks
  pass. No video or checkpoint-image export was rebuilt.

- September 21 acceptance polish: replaced the dashed-to-solid morph with a
  0.45-second fade into the gaps for the first trade and every face-on bid,
  including the floor shadows. Live-reviewed the initial offer/acceptance,
  intermediate acceptance frames for Amanda-Grace's $4.25 and Gary's $4.50,
  and the final $6.25 hold. Dashes and price labels stay fixed while the old
  deal fades. Syntax/whitespace checks and the existing two-buyer bidding test
  pass. Used the hot-reloaded viewer without exporting video or checkpoints.

- September 21 transition polish: live-reviewed the bidding-to-plaza pullback,
  preserved $6.25 line/shadow, fixed Gary/Molly stations, Amanda-Grace staying
  on Molly's right, and simultaneous in-place side graphs. The bars' following
  updaters start after the resize, preventing a competing positional snap.
  Replayed the market through the six-trade $4 result with the existing
  per-round assertions. All 20 discovery tests and syntax checks pass; no video
  or checkpoint-image export was needed.

- September 21 growth revision: 20 discovery tests pass, including full-survey
  choices, keeping one's own reservation on a tie, a newcomer's unaffordable
  comparison, and the complete 14-arrival carry-forward trace. Existing small
  market and deviation fixtures still pass. Syntax and whitespace checks pass.
  Live execution reaches ten-by-ten and six trades at $4, with per-round
  model/visual-state assertions intact. Reviewed the compact matched marginals,
  growing curves, all-seller comparison, and late-buyer refusal in ManimLive.
  Seller focus now changes stroke opacity only; guides and offered prices draw
  above the highlights. No movie or checkpoint-image export was rebuilt.

- September 21 bidding revision: live-checked the stationary head-on setup,
  simultaneous solid $4 / dashed $4.25 comparison, MC's slide to Amanda-Grace
  and solidification at $4.25, the final $6.25 hold at the same zoom, and the
  subsequent plaza/side-curve reveal. MB $6/$7 remain fully visible throughout.
  Syntax checks and the existing quarter-dollar bidding regression test pass.
  Reviewed through ManimLive; no full export was rebuilt.
- World-text update: inspected the first pair, side-on accounting view,
  Amanda-Grace's entrance, rolling prices through $6.25, and the small-market
  buyers returning to the circle in the live viewer. Glyphs face the camera
  while their position and apparent size follow the 3D scene. Syntax checks
  pass; no full movie or checkpoint export was needed.
  Viewer follow-up: seeking backward from the growing market to `2.b.vi`
  restored an oblique camera pose instead of the authored side view, allowing
  bars to occlude portions of world text. Forward playback through the next
  camera move restored the intended pose. The text remains camera-facing;
  the backward-seek camera behavior needs separate investigation.
- Current incremental pass extends the two-by-two through equal prices and
  the three-by-two through Gary’s exclusion, then lets the third seller restore
  his trade. Verified automatic reload in the connected ManimLive development
  viewer, then inspected the equal-$5.50 hold, third-buyer entrance and first
  offer, Gary’s exclusion question/explanation, and third-seller reconsideration.
  Continuing through crowd discovery reached the six-trade $4 state and the
  equilibrium definition without assertion failures. The static movie awaits
  the next larger export; the full-render record below precedes this extension.

- Pure rule suite: 41 tests pass in the shared checkout, including 16
  discovery tests. These check every auction bid, both buyers' permitted
  improvements after Andrew enters, and the lookout buyer’s choice of the
  only affordable option after the third seller enters, including the cost
  of an outbid. Separate checks verify positive gains at $5.50 in the
  two-by-two and Gary’s lost trade at $6.25 in the three-by-two.
  The three presentation traces have
  six $4 matches, total gains $16, unique reservations, no losses, and no
  remaining permitted moves.
- Prior full GPU render (before this extension) passes at 2160×1080 and 15 fps: 604 checkpoints,
  46 named teaching holds, and 283.40 seconds of motion. Reviewed the separate
  curves at three, four, six, and twenty people; Andrew's MC-$4/ask-$4.25 entry;
  both original buyers' return to the circle; the third-seller price-label
  removal; all sellers' persistent red dashed prices; the survey and choice;
  the settlement; the combined graph; and the final stability frame. The
  animated state is checked against the model after every discovery round.
  Old price lines and shadows finish fading before a buyer moves; new lines
  enter after the marginals meet.
- The first deliberation keeps its camera, geometry, and question while MC and
  its cost area stay orange. The accounting review transfers expenditure’s green
  boundary to revenue, slides the existing MC label into the lower-right position,
  and uses an inset orange PS outline; its motion and stopped frames are checked
  in the preview.
- Reviewed actual stopped frames: first deliberation, all five accounting
  regions, switching, crowd settlement, graph sorting, algebra, both deviation
  calculations, shortage/excess, named switches, and stability.
- Twenty-four backward/forward restores across 3D and 2D scenes reproduce their
  original rendered frames exactly (maximum channel error 0). The browser player
  also passed forward/reverse buyer-choice playback and the accounting label
  move. Sampled movie frames show the highlighted buyer in the hub, then walking
  along the single selected route; the green payment boundary in transit; and
  the same MC label moving into its accounting position.
- Preview: `media/EpisodeB3_present/index.html`, generated locally; it is not
  a published course artifact. Rebuild with `--export-present`. The application
  supplies the standard ManimL forward/reverse controls.
- Teaching text fades out on advance rather than being removed instantaneously.
  The movie player parks on the first frame after a pause boundary; a fade
  preserves the question/definition in that frame. Native checkpoint images
  alone do not catch this distinction. Twelve exported-movie pause frames
  were checked for their question, caption, or definition, including both
  Andrew-entry decisions and the three-seller comparison.

## Review correction · compact pairs and distinct cost color

The first-pair marginals move inward before the price appears, with the existing
1.10-wide bars and 0.12 gap. The latest bidding revision keeps both MBs in place
and slides Molly's one MC bar between those same close comparison positions.
The old solid price remains visible alongside the new dashed offer until the
MC slide completes. Lines span the bar edges, and their ground shadows use the
same endpoints. The crowd uses neighboring trading positions and keeps its
faster pacing after the bidding close-up ends.

Taylor’s latest correction supersedes the temporary green MC/cost treatment:
Molly’s MC bar, label, and cost fill all stay orange through the close-up and
pullback. The existing MC label slides to the lower-right accounting position;
it retains “MC $2” rather than disappearing and being replaced by “Cost $2.”
The green expenditure boundary visibly travels from
Gary to Molly and is relabeled Revenue: the same $4 payment viewed from either
side. The upper $2 region receives an orange outline and PS label, with its
interior unfilled. The PS border is inset by 0.045 world units on every side,
leaving the full green revenue boundary visible around it. This replaces the
earlier white revenue outline and orange PS fill without changing any dollars.

All posted prices remain red dashed markers on their supply columns, including
unsold offers. Plaza price numbers disappear with the third seller. Price-change
arrows repeat beside the graph markers in discovery and the deviation runs.
Removing a match removes both its elevated line and its floor shadow.
