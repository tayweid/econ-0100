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

**Review cadence:** edit in the connected ManimLive development viewer,
which hot-reloads this scene from a safe checkpoint. Inspect the live frame
and nearby motion after saving. Use targeted stills/clips as a fallback; reserve
full exports for deliverables or larger milestones. The static movie viewer
does not hot-reload. See the animator workflow in `Blocks/_Style_Guide.md` §8.

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

## First pair and deliberate decisions

| Pause | Script / action | Stopped frame |
|---|---|---|
| `0.a` | Shared MICROECONOMICS bumper, Part B / Episode 3 | Notes' thesis, “Equilibrium: when no one wants to change.” |
| `2.a` | Notes 1.a/2.a: the question and the first exchange | Gary and Molly start nearby (x=±1.65), with no offered price yet. Teal MB $6, orange MC $2 above their orbs. Question title: “Would they exchange?” |
| `2.a.i` | Taylor's first-deliberation direction | Camera faces the pair from the side. Buyer left, seller right at x=±1.45; their original bars move inward between them, broaden to 1.10 units with a 0.12 gap. Molly’s MC bar, label, and orb remain orange throughout. Dashed red offer at $4, matching faint floor shadow. Only the bottom question, “Would they both accept this price?”, enters after the camera settles. No payoff labels yet. |
| `2.b` | Accept on advance | Remove question; the same price and shadow become solid. |
| `2.b.i` | Recall B1 expenditure | Green area 0–4 on the buyer's bar, then “Expenditure $4.” |
| `2.b.ii` | Recall B1 CS | Teal area 4–6, then “CS $2.” |
| `2.b.iii` | Carry the payment from buyer to seller | Trace a green, unfilled copy of Gary’s expenditure boundary, then slide it horizontally by 1.22 units onto Molly’s side without changing its size or dollar height (0–4). Gary’s expenditure fill stays in place. After the outline arrives, reveal green “Revenue $4.” Keep the revenue boundary through Cost and PS. |
| `2.b.iv` | Move the marginal-cost label | Keep the orange area 0–2. Slide the existing orange “MC $2” label from above its bar to the right of that lower area in 1.2 seconds, as the area settles into the accounting view. Do not replace it with “Cost.” Restore its above-bar tracking position during the later pullback. |
| `2.b.v` | Producer surplus | Outline the upper region between MC $2 and price $4 in orange, with no orange fill; inset the border 0.045 world units on all four sides so it fits visibly inside the green revenue boundary. This inset is a highlight margin, not a change to the $2 surplus. Then reveal “PS $2.” Expenditure equals revenue; total gain $4 = 6−2. |
| `2.b.vi` | Make the single-unit interpretation explicit | “One unit” bottom caption. Bars have widened visually; quantities have not changed. |
| `2.c` | Amanda-Grace enters on the buyer side | Pull back to Molly’s fixed seller station at (3, 1.2), Gary nearby at (1.4, 1.2), and Amanda-Grace entering from (−2.8, −1.1). Molly stays at this station through subsequent bargaining and market growth. Separate sorted MB/MC curves remain left/right. Amanda-Grace has MB $7 against Gary’s MB $6; Molly has MC $2 and a visible standing price $4. Title: “What would Amanda-Grace gain?” Andrew is absent. |
| `2.c.i` | First higher offer | Amanda-Grace walks to Molly; only the buyers change position. Her marginal moves beside Molly’s before the short dashed $4.25 offer appears. Molly’s standing $4 tag stays visible until acceptance. Hold “Would Amanda-Grace gain by offering $4.25?”; accept on advance. |
| `2.c.accepted` | Make her incentive explicit | After accepting, hold “Amanda-Grace gains $7−$4.25=$2.75.” This is her gain compared with going without the unit. Then continue the buyer bidding sequence. |
| `2.c.ii` | Gary responds | Gary offers $4.50. The pair changes, the price rises, and the displaced buyer waits nearby. Then alternate $0.25 bids without a hold on every repetition. |
| `2.c.iii` | Different MBs determine the winner | Amanda-Grace wins at $6.25. Gary's next $6.50 offer would exceed his MB $6. His bar never changes; her MB stays $7. Keep the price below her MB and show why Gary stops. |

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
| `3.a.entry` | Andrew enters deliberately | Reframe around the same fixed Molly station and Amanda-Grace’s $6.25 deal. Andrew enters at another fixed seller station; show MC $4 first, then his price $4.25 just above it in the world and supply graph. The price caption reads only “$4.25,” without “Ask.” Retain the four names for these decisions. Gary is still unmatched. |
| `3.a.switch.options` | Amanda-Grace reconsiders | She returns to the hub. Highlight her MB-$7 bar and compare Molly $6.25 with Andrew $4.25 on the supply graph. Hold “Would Amanda-Grace keep paying $6.25?” |
| `3.a.switch.accepted` | Choose the lower price | She walks to Andrew at $4.25. Molly stays put, now without a buyer. |
| `3.a.counter.options` | Gary reconsiders | Gary enters the hub. Highlight MB $6; show Molly’s open $6.25 ask versus the $4.50 needed to outbid Amanda-Grace at Andrew. Hold “Could Gary gain by offering $4.50?” |
| `3.a.counter.accepted` | Gary makes the affordable bid | Gary walks to Andrew at $4.50; Amanda-Grace returns to the buyer side. Both sellers stay in place. Continue bargaining with these four people before admitting anyone else. |
| `3.a.seller.cut` | Molly responds to losing her buyer | Buyers bid Andrew through $4.75 and $5. Show Molly still at $6.25 without a buyer; ask whether she would lower her price. Then her price falls to $6. Subsequent bids and cuts bring both sellers to $5.50. Each buyer visits the center before checking a seller; the checked MC column and offered price light together. |
| `3.a.two_pairs` | Complete the two-by-two | Gary trades with Andrew; Amanda-Grace trades with Molly. Both prices are $5.50. MBs remain $6/$7 and MCs $2/$4, so all four gain. Hold “Both trades: $5.50. Gary's gain: $0.50.” This is a demonstrated path to equal prices, not a claim that every quarter-dollar path gives equality. |
| `3.a.third_buyer` | Add only a buyer | A new buyer with MB $8 enters; supply remains exactly two units. Retain Gary, Amanda-Grace, Molly, and Andrew's names, and label the entrant “New buyer.” |
| `3.a.third.options` | A third bidder wants a unit | The new buyer enters the center, compares the two sellers, and considers $5.75 at Molly. MB $8 makes this strictly beneficial. Ask “Would the new buyer offer $5.75?” before acceptance. |
| `3.a.excluded` | Three buyers, two units | Continue permitted outbids to two prices of $6.25. The new buyer trades with Molly; Amanda-Grace trades with Andrew. Gary returns to the waiting side. Keep his MB $6 visible in the demand curve and ask “Why is Gary left out?” |
| `3.a.excluded.reason` | Compare Gary's two situations | Hold “Gary traded at $5.50. Now $6.25 > MB $6.” Gary's benefit and both sellers' costs have not changed. His earlier positive gain demonstrates that he was willing and able to trade in the two-by-two; the higher-value third buyer changes the allocation. |
| `3.a` | A third seller restores an option | With three buyers still present, add an MC-$4 seller posting $4.50. Insert its MC bar and dashed price in the supply curve. Fade out plaza price labels now that there are three sellers. Gary is still waiting; the new buyer and Amanda-Grace hold the other two units at $6.25. |
| `3.a.lookout` | Gary reconsiders | Gary returns to the center. Highlight his unchanged MB-$6 bar, dim the other two buyers and their standing connections, and keep all three sellers visible. |
| `3.a.options` | Read the three options | Highlight each world seller and its supply column together. Needed prices are $6.50 to outbid at Molly, $4.50 at the new seller, and $6.50 to outbid at Andrew. Add the teal MB-$6 guide. Hold “Would Gary trade with the new seller?” Only the new seller is affordable. |
| `3.a.chosen` | Gary trades again | Gary walks from the hub to the new seller at $4.50. Show the short accepted-price connection and floor shadow. Hold before restoring the other buyers and fading the small-cast names. Then continue one-person-at-a-time growth. |
| `3.a.i` | Grow from six to eight | Add the next buyer and seller separately. Pause with four of each. |
| `3.a.ii` | Continue one person at a time to ten of each | Alternate buyer/seller entrances with faster pacing. No mass fade-in. Keep plaza price labels absent; red dashed prices stay on the supply graph, distinct from orange MC. |
| `3.b` | Faster repetitions of the same decision | Keep both sorted curves and the hub visible. Animate successful sampled visits one buyer at a time: enter the hub, highlight the checked seller and its supply column, show the required offer, then approach and match. Animate displaced buyers returning to the waiting side. Omit unchanged unsuccessful visits after the worked example; do not draw the old all-buyer web of grey rays. Seller cuts move their red dashed supply markers downward. |
| `4.a` | Name the stopping state | Six accepted trades at $4 in the presentation run. Keep nontraders visible. Bottom definition: “Equilibrium is where no one wants to change.” Gold arrow points to a settled price. |

Fixture, updated for the unequal-MB bidding scene:

- MB: `[6, 8, 4, 3, 7, 5, 4, 3, 2, 2]`.
- MC: `[2, 4, 3, 5, 4, 2, 6, 3, 5, 6]`.
- Gary B0; Amanda-Grace B4; new buyer B1 (MB $8); Molly S0; Andrew S4.
- Initial full-market asks: `[6.25, 4.5, 6, 6, 6.25, 6, 6, 6, 6, 6]`; B0→S1,
  B1→S0, B4→S4. These three trades follow the staged competition and Gary’s
  return when the third seller arrives.
- Presentation seed 296 gives six matches at $4 after 29 rounds and 28
  successful sampled visits. The seed is
  chosen for a readable classroom run; arbitrary seeds need not give one price.
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
| `5.d` | $6 above equilibrium | Aggregate Qs=80, Qd=30. Discrete Qs=10, Qd=3. Unaccepted seller units remain visible. |
| `5.e` | Excess terminology | “Excess: quantity supplied is greater than quantity demanded.” Textbook “surplus” is crossed out and replaced with “excess”; this does not relabel CS or PS. |
| `5.f` | Molly cuts $6→$5 | Explicit staged reset has Gary at Andrew and Amanda-Grace at S5; Molly is unsold. Gary switches to Molly. This allocation is illustrative, not represented as the random discovery outcome. |
| `5.g` | Continuous downward adjustment | Unaccepted sellers cut; matched buyers take strictly cheaper offers. |
| `5.h` | Restore and test stability | Restore the saved uniform-price state. Select actual marginal participants: an MB-$4 buyer declines $4.25; an MC-$4 seller declines $3.75. Do not silently pretend these are necessarily the same pair in the discovery allocation. |

The aggregate calculations use the full graph and side calculation, then return
to the plaza beside its own **Units** graph. This keeps both sets of quantities
legible. At $3 the four initially matched buyers are B0–B3, leaving Amanda-Grace
first in the queue. At $6 Gary starts with Andrew, the new buyer with S1, and Amanda-Grace with S5.
After the named offer, seeded random search resumes (upward seed 473, 18 rounds;
downward seed 361, 29 rounds). Both presentation traces pass the stopping audit
and end with six $4 trades. During individual price changes, remove the common
price readout until a uniform transaction price is restored.

`5.b.i` holds the $3.25 switch; `5.d.i` holds the excess definition; `5.h.i`
shows the MB-$4 buyer refusing $4.25, `5.h.ii` the MC-$4 seller refusing $3.75,
and `5.h.iii` restores the equilibrium frame. Each final test uses an actual
pair from the saved discovery state.

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
0–8 dollar range. Red dashed posted-price markers begin with Molly, then follow
every seller's sorted MC column. Plaza prices remain through Andrew's entry
and both buyer decisions; the third seller triggers their removal. Solid red
highlights show the price needed for a particular choice, including the extra
$0.25 for an occupied seller. After the separate curves combine, per-seller
markers return on the unit graph during deviations; plaza price labels stay off.
The crowd camera height is 10.4. Molly keeps her (3, 1.2) station, Andrew stays
at (3, −1.2), and further sellers fill the right arc. Only buyers walk between
stations and the center. The worked survey highlights the three world sellers
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

The previous small-cast price connections were too long, especially during the
challenger's approach. Players now stand nearby; contemplated marginals move
inward before the price appears and remain together on acceptance. Lines span
the bar edges and their ground shadows use the same endpoints. The accounting
close-up is still magnification of one unit, with its existing 1.10-wide bars.
The crowd already uses neighboring trading positions and keeps its faster pacing.

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
