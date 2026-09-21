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

**Order:** first pair → side-view deliberation → payment and gains → buyer bidding
→ second seller and a price cut → gradual arrivals → crowd discovers a price → name equilibrium → introduce the graph/recap →
algebra → deviations. Taylor's latest review adds separate MB/MC curves during
the buildup; their combination and the algebra still follow discovery. The
approved first Gary/Molly close-up stays unchanged.

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
| `2.c` | One new person: a competing buyer | Pull back from the approved close-up. Separate fixed-frame curves enter: buyer MB on the left, seller MC on the right. Copy each person’s marginal bar into its curve; keep MB descending and MC ascending as people arrive. Amanda-Grace alone joins, MB $7 against Gary's unchanged MB $6. Molly remains the only seller, MC $2; their standing price is $4. |
| `2.c.i` | First higher offer | Amanda-Grace approaches; her bar moves beside Molly's before the short dashed $4.25 offer appears. Hold “Would they both accept this price?”; accept on advance. |
| `2.c.ii` | Gary responds | Gary offers $4.50. The pair changes, the price rises, and the displaced buyer waits nearby. Then alternate $0.25 bids without a hold on every repetition. |
| `2.c.iii` | Different MBs determine the winner | Amanda-Grace wins at $6.25. Gary's next $6.50 offer would exceed his MB $6. His bar never changes; her MB stays $7. Keep the price below her MB and show why Gary stops. |
| `2.d` | One new person: a second seller | Andrew enters only now, MC $4 and ask $6. Molly/Amanda-Grace still have their $6.25 deal. |
| `2.d.i` | Compare prices | Hold “Would Amanda-Grace keep paying $6.25?” with both sellers' prices visible. She can switch to Andrew for $6. |
| `2.d.ii` | A switch and a price cut make the prices agree | Amanda-Grace switches to Andrew at $6. Molly has no buyer and cuts $6.25→$6; Gary accepts at his MB. Two compact pairs now trade at $6. This is a demonstrated path to equal prices, not a claim that any two-pair allocation forces a unique price. |

All dollar heights share `z = baseline + scale × dollars`; the ground connection
is the projection of those exact endpoints. Dashed means contemplated; solid
means accepted but still revisable. No cancelled deal is counted as completed
trade or accumulated surplus. Payment/cost colors and reveal order follow the
actual B1/B2 implementations; the B2 revenue/cost/PS frame was inspected.

## Crowd and stopping state

| Pause | Action | Stopped frame |
|---|---|---|
| `3.a` | Grow from four people to six | Keep the two $6 deals. Add an MB-$5 buyer, then an MC-$4 seller asking $4.50. Insert each new bar into its sorted side curve. The original dashed center lookout appears on the floor. |
| `3.a.lookout` | Walk into the decision | The new buyer walks into the center ring. Pause with this buyer and the three sellers lit; dim the two other buyers and their standing connections. Highlight the buyer’s MB-$5 bar on the left. |
| `3.a.options` | Read the options on the supply side | Highlight each seller and its MC column together, one at a time. Red ticks mark the price needed to buy: $6.25 at occupied Molly, $4.50 at the new seller, $6.25 at occupied Andrew. A teal MB-$5 line crosses the right panel. Pause with “Which offer can this buyer accept?” Prices are distinct from the orange cost bars. |
| `3.a.chosen` | Make one visible choice | Highlight the $4.50 option, trace one dashed walking route, and move the buyer from the hub to that seller. Replace the route with a short red accepted-price line and its floor shadow. Then restore the full cast. |
| `3.a.i` | Grow from six to eight | Add the next buyer and seller separately. Pause with four of each. |
| `3.a.ii` | Continue one person at a time to ten of each | Alternate buyer/seller entrances with faster pacing. No mass fade-in. Seller tags are distinct from MC bars. |
| `3.b` | Faster repetitions of the same decision | Keep both sorted curves and the hub visible. Animate successful sampled visits one buyer at a time: enter the hub, highlight the checked seller and its supply column, show the required offer, then approach and match. Animate displaced buyers returning to the waiting side. Omit unchanged unsuccessful visits after the worked example; do not draw the old all-buyer web of grey rays. Seller cuts remain visible in the red tags. |
| `4.a` | Name the stopping state | Six accepted trades at $4 in the presentation run. Keep nontraders visible. Bottom definition: “Equilibrium is where no one wants to change.” Gold arrow points to a settled price. |

Fixture, updated for the unequal-MB bidding scene:

- MB: `[6, 5, 4, 3, 7, 5, 4, 3, 2, 2]`.
- MC: `[2, 4, 3, 5, 4, 2, 6, 3, 5, 6]`.
- Gary B0; Amanda-Grace B4; Molly S0; Andrew S4.
- Initial full-market asks: `[6, 4.5, 6, 6, 6, 6, 6, 6, 6, 6]`; B0→S0,
  B1→S1, B4→S4. The third deal is the demonstrated lookout choice.
- Seed 284 gives 35 rounds (18 successful visits), six matches, all matched prices $4. The seed is
  chosen for a readable classroom run; arbitrary seeds need not give one price.
- The three-person bidding trace is the existing model with values [6, 7],
  cost [2], initial ask [4], Gary initially matched, seed 0.
- Second-seller entry follows seed 4 with values [6, 7], costs [2, 4], asks
  [6.25, 6], and Amanda-Grace initially matched to Molly. The actual sequence
  is Amanda-Grace→Andrew at $6; Molly cuts to $6; Gary→Molly at $6.
- At $6 Gary is indifferent and accepts, following the model's nonnegative-gain
  convention. Uniform $6 is feasible here; it is not the unique equilibrium of
  this four-person economy. The $0.25 search process can settle at unequal
  nearby prices on other paths, so common prices are shown through actions.

Stopping is an exhaustive audit of permitted improvements, not a quiet random
round. The tick-based search rule is not a proof of general convergence or of
stability against every possible strategy. At the uniform $4 benchmark,
Qd = Qs = 6, counting indifferent participants. Sorted marginal units have four
strictly positive gains and two zero gains; this is not a claim that each
observed pair has the same surplus split as that sorted pairing.

## Graph bridge and algebra (implemented after discovery)

| Pause | Action | Values / reveal order |
|---|---|---|
| `4.b` | Bring the two curves together | Move the already-sorted side bars onto one shared unit graph, x 0–10, y 0–8. Retain their identity and sorted order; do not restart with unsorted bars. Add common price $4 and Q=6 after they meet. |
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

Taylor's latest review preserves the entire first Gary/Molly scene and replaces
simultaneous entrances with sequential arrivals. Amanda-Grace's MB is now $7
in animation code; the notes' cast comment still says $6 and belongs to the
editor. The newer `2.c` prose already describes buyer first, seller second,
then one-at-a-time expansion. Taylor confirmed that the next entrant is a
second seller, forming two pairs.

Taylor's latest direction supersedes the earlier “no graph before discovery”
restriction for the two separate marginal curves. They begin after the approved
close-up and stay on opposite sides of the plaza. The shared unit graph still
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
0–8 dollar range. The crowd camera height is 10.4. Buyer and seller positions
stay on their opposing arcs, with equal vertical spacing so adjacent price
tags remain readable. The worked survey highlights the three world sellers
and their corresponding supply columns in the same order before the question
pause. The larger run compresses this to a single checked option per visit.

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

- Pure rule suite: 38 tests pass in the shared checkout, including 13
  discovery tests. These check every auction bid, the actual switch/cut sequence
  after Andrew enters, and the lookout buyer’s one affordable option after
  including the cost of an outbid. The three presentation traces have
  six $4 matches, total gains $13, unique reservations, no losses, and no
  remaining permitted moves.
- The updated full GPU render passes at 2160×1080 and 15 fps: 508 checkpoints,
  43 named teaching holds, and 253.13 seconds of motion. Reviewed the separate
  curves at three, six, and twenty people; the center-ring survey and choice;
  the settlement; the combined graph; and the final stability frame. The
  animated state is checked against the model after every discovery round.
  Old price lines and shadows finish fading before a buyer moves; new lines
  enter after the marginals meet.
- The approved opening choreography through `2.b.vi` is unchanged; its
  first-deliberation and accounting frames were checked against the prior preview.
- Reviewed actual stopped frames: first deliberation, all five accounting
  regions, switching, crowd settlement, graph sorting, algebra, both deviation
  calculations, shortage/excess, named switches, and stability.
- Fifteen backward/forward restores across 3D and 2D scenes reproduce their
  original rendered frames exactly (maximum channel error 0). The browser player
  also passed forward/reverse buyer-choice playback. Sampled movie frames show
  the highlighted buyer in the hub, then walking along the single selected route.
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
