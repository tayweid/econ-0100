# B3 · Build equilibrium, then test deviations

Current animation storyboard · September 20, 2026

## Entry point and ownership

Run `maniml Blocks/B3_Equilibrium/03_Equilibrium.py EpisodeB3` from the project
root. This is the fresh, flat episode: one sequential `construct()`, literal
pause IDs, the shared B1/B2 bumper, 15 fps, 2160×1080. The pure random-search
rules live in `Blocks/Sim/discovery.py`; they contain no choreography.

[01_Notes.md](01_Notes.md) is Taylor/Fable's read-only script source. The animator
edits the storyboard and code. Taylor's original animation directions remain
[verbatim in the detailed storyboard](02_Companion_Storyboard.md#taylors-animation-directions-verbatim).
`Animate.py`, `Animate_A.py`, and their detailed storyboards are references and
history. Their old episode/companion division and pause IDs do not govern this
new single episode. The map below supersedes earlier proposals.

**Order:** first pair → side-view deliberation → payment and gains → switching
→ crowd discovers a price → name equilibrium → introduce the graph/recap →
algebra → deviations. No graph appears before the market has settled. This
implements Taylor's latest placement and retains the notes' 2–6 act IDs.

## First pair and deliberate decisions

| Pause | Script / action | Stopped frame |
|---|---|---|
| `0.a` | Shared MICROECONOMICS bumper, Part B / Episode 3 | Notes' thesis, “Equilibrium: when no one wants to change.” |
| `2.a` | Notes 1.a/2.a: the question and the first exchange | Gary and Molly start nearby (x=±1.65), with no offered price yet. Teal MB $6, orange MC $2 above their orbs. Question title: “Would they exchange?” |
| `2.a.i` | Taylor's first-deliberation direction | Camera faces the pair from the side. Buyer left, seller right at x=±1.45; their original bars move inward between them, broaden to 1.10 units with a 0.12 gap. Molly’s MC bar and label become green (the existing Cost color); her orb stays orange. Dashed red offer at $4, matching faint floor shadow. Only the bottom question, “Would they both accept this price?”, enters after the camera settles. No payoff labels yet. |
| `2.b` | Accept on advance | Remove question; the same price and shadow become solid. |
| `2.b.i` | Recall B1 expenditure | Green area 0–4 on the buyer's bar, then “Expenditure $4.” |
| `2.b.ii` | Recall B1 CS | Teal area 4–6, then “CS $2.” |
| `2.b.iii` | Recall B2 revenue | White revenue outline 0–4 on the seller's side, then “Revenue $4.” Keep the full outline visible through the next two fills. |
| `2.b.iv` | Cost before PS | Green area 0–2, then “Cost $2.” |
| `2.b.v` | Producer surplus | Orange area 2–4, then “PS $2.” Expenditure equals revenue; total gain $4 = 6−2. |
| `2.b.vi` | Make the single-unit interpretation explicit | “One unit” bottom caption. Bars have widened visually; quantities have not changed. |
| `2.c` | Notes switching | Pull back to Gary and Molly only 1.6 units apart. Their bars stay between them, width 0.38 with a 0.06 gap; the $4 line spans their combined 0.82-unit width. Restore the wide-market orange MC color. Amanda-Grace and Andrew join. |
| `2.c.i` | Small-cast deliberation | Amanda-Grace approaches Molly first. Their own bars then slide together at equal depth with a 0.06 gap; only afterward draw the short dashed $4.25 offer and its floor shadow. Dim Gary’s incumbent connection/bar and hide his name and price/MB labels during the question hold. Offset Amanda-Grace’s long name to keep the compact pair readable. |
| `2.c.ii` | Resolve the switch | Molly accepts $4.25 and keeps the compact bar arrangement with Amanda-Grace. Gary approaches Andrew; their bars move inward before the $5 line appears. Both accepted price lines are 0.82 units long. MB and MC never change. |

All dollar heights share `z = baseline + scale × dollars`; the ground connection
is the projection of those exact endpoints. Dashed means contemplated; solid
means accepted but still revisable. No cancelled deal is counted as completed
trade or accumulated surplus. Payment/cost colors and reveal order follow the
actual B1/B2 implementations; the B2 revenue/cost/PS frame was inspected.

## Crowd and stopping state

| Pause | Action | Stopped frame |
|---|---|---|
| `3.a` | Introduce the rest of the existing ten-buyer/ten-seller cast | Keep Gary/Andrew and Amanda-Grace/Molly as the two standing deals, including $5/$4.25 prices. Seller price tags remain distinct from MC bars. Still no graph. |
| `3.b` | Continuous random checks, outbids, and cuts | Every buyer samples one seller per round. An occupied unit needs a $0.25 higher offer. A matched buyer switches only to a strictly lower price. Sellers unmatched at both round boundaries cut $0.25, bounded by MC. No per-check holds. |
| `4.a` | Name the stopping state | Six accepted trades at $4 in the presentation run. Keep nontraders visible. Bottom definition: “Equilibrium is where no one wants to change.” Gold arrow points to a settled price. |

Fixture, retained from the lecture prototype:

- MB: `[6, 5, 4, 3, 6, 5, 4, 3, 2, 2]`.
- MC: `[2, 4, 3, 5, 4, 2, 6, 3, 5, 6]`.
- Gary B0; Amanda-Grace B4; Molly S0; Andrew S4.
- Initial asks: `[4.25, 6, 6, 6, 5, 6, 6, 6, 6, 6]`; B0→S4, B4→S0.
- Seed 268 gives 17 rounds, six matches, all matched prices $4. This seed is
  chosen for a readable classroom run; arbitrary seeds need not give one price.

Stopping is an exhaustive audit of permitted improvements, not a quiet random
round. The tick-based search rule is not a proof of general convergence or of
stability against every possible strategy. At the uniform $4 benchmark,
Qd = Qs = 6, counting indifferent participants. Sorted marginal units have four
strictly positive gains and two zero gains; this is not a claim that each
observed pair has the same surplus split as that sorted pairing.

## Graph bridge and algebra (implemented after discovery)

| Pause | Action | Values / reveal order |
|---|---|---|
| `4.b` | First graph; notes' recap | Keep the world beside a unit graph, x 0–10, y 0–8. Copies of buyer bars enter in arrival order, sort descending; sellers sort ascending. Add price $4 and Q=6 only after both staircases. |
| `4.c` | Move to the aggregate example | Fade the crowd and unit graph. Explicit caption “Q in thousands of pounds.” New aggregate axes x 0–90, y 0–13; D: P=12−Q/5, S: P=2+Q/20. These curves represent a larger market, not a rescaling of six people. Leave numerical equilibrium answers off the graph. |
| `4.d` | Solve quantity first | Side calculation: 2+Q/20=12−Q/5; Q/20+Q/5=10; Q/4=10; Q*=40. Reveal one step at a time. |
| `4.d.i` | Then solve price | Substitute 40 into P=2+Q/20; obtain P*=$4. Carry quantity and price into graph guides only after the calculation. |
| `4.e` | Read the combined graph | Red point and guides at (40,4); starred quantity and price. This fresh scene uses one combined graph from the bridge rather than introducing duplicate graphs just before combining them. |

Use B1/B2's grey divider, question titles, 0.7 minimum type, graph-to-math number
transfers, and unknown-before-answer convention. The six units in the toy world
are never labeled 40,000 pounds. Keep the representation change visible.

## Deviations (back end)

The notes' two tests return to the same cast. The discrete example and aggregate
example share the price but have separate quantities. A small market represents
one-unit participants; a smooth market represents thousands of pounds.

| Pause | Action | Arithmetic / named move |
|---|---|---|
| `5.a` | $3 below equilibrium; supply trace then demand trace | Aggregate Qs=20, Qd=45. Discrete Qs=4, Qd=8. Show unknown before the corresponding substitution/answer. |
| `5.b` | Name shortage with bottom definition and arrow | “Shortage: quantity demanded is greater than quantity supplied.” Amanda-Grace offers Molly $3.25; Gary is displaced. |
| `5.c` | Continuous upward adjustment | Show offers increasing; return to the supported $4 state before the other experiment. |
| `5.d` | $6 above equilibrium | Aggregate Qs=80, Qd=30. Discrete Qs=10, Qd=2. Unaccepted seller units remain visible. |
| `5.e` | Excess terminology | “Excess: quantity supplied is greater than quantity demanded.” Textbook “surplus” is crossed out and replaced with “excess”; this does not relabel CS or PS. |
| `5.f` | Molly cuts $6→$5 | Explicit staged reset has Gary at Andrew and Amanda-Grace at S5; Molly is unsold. Gary switches to Molly. This allocation is illustrative, not represented as the random discovery outcome. |
| `5.g` | Continuous downward adjustment | Unaccepted sellers cut; matched buyers take strictly cheaper offers. |
| `5.h` | Restore and test stability | Restore the saved uniform-price state. Select actual marginal participants: an MB-$4 buyer declines $4.25; an MC-$4 seller declines $3.75. Do not silently pretend these are necessarily the same pair in the discovery allocation. |

The aggregate calculations use the full graph and side calculation, then return
to the plaza beside its own **Units** graph. This keeps both sets of quantities
legible. At $3 the four initially matched buyers are B0–B3, leaving Amanda-Grace
first in the queue. At $6 Gary starts with Andrew and Amanda-Grace with S5.
After the named offer, seeded random search resumes (upward seed 473, 18 rounds;
downward seed 249, 27 rounds). Both presentation traces pass the stopping audit
and end with six $4 trades. During individual price changes, remove the common
price readout until a uniform transaction price is restored.

`5.b.i` holds the $3.25 switch; `5.d.i` holds the excess definition; `5.h.i`
shows the MB-$4 buyer refusing $4.25, `5.h.ii` the MC-$4 seller refusing $3.75,
and `5.h.iii` restores the equilibrium frame. Each final test uses an actual
pair from the saved discovery state.

## Reconciliation with the live notes

The notes changed again during this build: their latest 1.a/1.b brings the twin
graph recap back to the opening and 4.e describes their first combination.
Taylor's direct instruction here remains the animation's authority: **no graph
before discovery**. This pass uses a combined stair-step graph at 4.b and a
combined aggregate graph at 4.c, following the existing lecture prototype.
The delayed twin-graph variant can replace that bridge when the writing arc is
settled; it is not silently represented as already implemented. No notes edits
were made to resolve this difference.

The new closing prose is still marked as a draft in the notes. Leave its final
stage treatment with the PPF coda for the next pass rather than place a closing
before that unresolved tieback.

## Remaining writing-dependent material

The final PPF tieback needs a carrot price or permission to reuse A3's explicitly
illustrative exchange ratio. Do not derive a carrot price from the spinach
market. The notes' proposed exercises and B4 closer still await Taylor's final
wording. Keep those as storyboard targets; do not invent lecture prose or add
unsupported numerical markets. B4 is the next block, not B5.

## Validation record

- Pure rule suite: 35 tests pass in the shared checkout, including 10 new
  discovery tests. The three presentation traces have six $4 matches, total
  gains $12, unique reservations, no losses, and no remaining permitted moves.
- The updated full GPU render passes at 2160×1080 and 15 fps: 301 checkpoints,
  34 named teaching holds, and 176.07 seconds of motion. The proximity/color
  correction was visually checked at the affected small-cast holds, the
  complete accounting comparison, and the scale-up transition.
- Reviewed actual stopped frames: first deliberation, all five accounting
  regions, switching, crowd settlement, graph sorting, algebra, both deviation
  calculations, shortage/excess, named switches, and stability.
- Eight backward/forward restores across 3D and 2D scenes reproduce their
  original rendered frames exactly (maximum channel error 0). The browser player
  also passed an actual forward/reverse camera-transition check.
- Preview: `media/EpisodeB3_present/index.html`, generated locally; it is not
  a published course artifact. Rebuild with `--export-present`. The application
  supplies the standard ManimL forward/reverse controls.

## Review correction · compact pairs and distinct cost color

The previous small-cast price connections were too long, especially during the
challenger's approach. Players now stand nearby; contemplated marginals move
inward before the price appears and remain together on acceptance. Lines span
the bar edges and their ground shadows use the same endpoints. The accounting
close-up is still magnification of one unit, with its existing 1.10-wide bars.
The crowd already uses neighboring trading positions and keeps its faster pacing.

In the first Gary/Molly close-up, green means cost throughout: the MC bar and
label become green before the acceptance question, and the cost area later uses
that same green. Orange is reserved for PS within this comparison. Molly’s orb
stays orange, and her MC bar returns to the market's orange supply convention
when the camera pulls back. This is a local teaching distinction, not a palette
change to B1/B2 or the crowd.

Unsold offers turn grey at settlement; matched $4 tags stay red. Price-change
arrows repeat in discovery and the deviation runs. Removing a match removes
both its elevated line and its floor shadow.
