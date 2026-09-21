# B3 · Build equilibrium, then test deviations

Overall animation arc · September 20, 2026 · **Storyboard, not yet implemented.**

Taylor's direction: start with a small number of players, build up to equilibrium,
then put the deviations animations on the back end. This page sets the order
across the two existing animation branches while Taylor and Fable develop one
coherent script. “Companion” and “episode” in existing filenames identify source
material; they do not determine the eventual video split or playback order.

**Playback:** one exchange → close-up of its marginals and price → a few players
choosing and switching → a larger market settling → read the equilibrium on
the graph → move price away and watch incentives → return to the PPF question.

## Script and outline sources reviewed

| Source | What it contributes to this arc |
|---|---|
| [Part B outline](../B_Outline.typ) | Prices coordinate choices on the PPF. Its Equilibrium tutorial already describes contingent deals, continued searching, cancellation for a better deal, and the point where nobody wants to change. |
| [Course outline](../_Parts.md) | One arc per block and per part; B3 is the market simulation, B4 develops efficiency, and B5 changes the underlying conditions. |
| [B3 notes](01_Notes.md) | The price left unresolved by B1/B2; shortage, excess, algebra, stability, and the PPF tieback. The companion section adds the pit-market prediction/replay idea. |
| [Original simulation outline](../Bx_Market_Animation/Bx_Equilibrium_Video.typ) | One pair → multiple sellers → multiple buyers → switching → settling → graph; marginal bars and CS/PS remain the visual bridge. |
| [Original B3 script](_archive/B3_Equilibrium_Script.md) | Earlier version of the lecture/companion split; useful history, superseded by the current notes and this requested order. |
| [Lecture 11 notes](<_archive/Lecture 11 (B7).md>) | Predict the market outcome, run it, set the predicted price and test whether anyone switches; the PPF coda. These ideas are already carried into the current B3 notes. |
| [Market scene design](../Bx_Market_Animation/Market_Scene_Design.md) | Same people/model across views, provisional matching versus settlement, and explicit distinction between a simulated outcome and a competitive benchmark. |

The notes' current prose still introduces the algebraic lecture before referring
to a companion. This storyboard follows Taylor's newer order without rewriting
that prose. The latest request also brings the two-player expenditure/CS/PS
explanation into B3; market-wide efficiency and policy claims remain B4 material.

## First branch · Build equilibrium from people

Detailed staging lives in [02_Companion_Storyboard.md](02_Companion_Storyboard.md).
Reuse `PriceDiscovery` as the visual foundation. Open with a few people: move
the existing twenty-person establishing/sorting sequence to the scale-up beat.

1. **One pair.** Give the seller an explicit ask distinct from MC; let the buyer
   compare it with MB. Show the red price-height connection and its floor shadow.
2. **The same pair, close up.** Bring their marginals nearly together. Keep one
   price dividing buyer expenditure/CS and seller cost/PS, with seller receipts
   equal to buyer payment. These are the same people and same deal throughout.
3. **A few players.** Keep deliberate comparison, the held preferred connection,
   the challenger/incumbent/seller spotlight, and a clearly explained switch.
4. **The crowd.** Introduce ten buyers and ten sellers, sort their marginal
   values into the fixed graph, then run reproducible random price checks,
   cuts, and outbids continuously. No survey-by-survey deliberation holds.
5. **Equilibrium.** Show the stopping state and test whether permitted improvements
   remain. Keep unmatched participants visible. Compare the observed outcome
   with the benchmark; a quiet simulation alone does not establish equilibrium.

## Bridge · The market we will test

Retain the settled tableau, identities, and marginal values when entering the
deviations branch. Save that economic state as the reset point. A change in
price is the experiment; changing the people at the same time would obscure it.

**Proposed common crowd:** reuse the lecture prototype's existing population
for both the revised discovery run and the deviation demonstrations:

- MB: `[6, 5, 4, 3, 6, 5, 4, 3, 2, 2]`.
- MC: `[2, 4, 3, 5, 4, 2, 6, 3, 5, 6]`.
- Gary B0, Amanda-Grace B4, Molly S0, Andrew S4, as already cast in `Animate_A.py`.
- At a uniform $4, Qd = Qs = 6 with zero-gain participation. Four units have
  strictly positive gains; two marginal units have MB = MC = $4.

This is a staging proposal to avoid jumping from the old companion's roughly
$7 market to a different $4 population when testing deviations. It uses
existing data, not newly invented curves. Keep the original small-pair examples
as illustrative setups; clearly introduce the larger population at scale-up.
The revised random-search run must earn its stopping state with these data.
If it does not support the intended equilibrium demonstration, resolve the
mechanism before animating a seamless handoff to the benchmark.

**Proposed algebra placement:** after discovering the price, connect to the
smooth market graph and solve the current notes' equations, then return to the
saved crowd for deviations. Reuse the existing algebra beats rather than add a
second derivation. Taylor/Fable can move this bridge within the back half as the
script settles; the fixed requirement is discovery before deviations.

Keep the scale change explicit. Six one-unit traders are not 40,000 pounds.
The discrete crowd illustrates the mechanism; the lecture's aggregate example
uses `D: P = 12 − Q/5` and `S: P = 2 + Q/20`, with Q in thousands of pounds,
so Q* = 40 and P* = $4. Label that representation change before using the
aggregate quantities.

## Second branch · Test deviations after equilibrium

Reuse the material in [02_Episode_Storyboard.md](02_Episode_Storyboard.md) and
`Animate_A.py`, reorganized into the following back-half sequence. The old
file's table remains an inventory of existing beats, not the new global order.

### Establish the comparison

Start from the saved equilibrium. Keep MB/MC, cast, graph positions, and the
equilibrium marker fixed. Separate two experiments: a temporary market-wide
price displaced from equilibrium, and one person's attempted better deal.
Neither changes the supply/demand curves.

### Below equilibrium · shortage and upward pressure

Reuse episode `2.a`–`2.c`: set the common displayed price to $3, show the queue,
then Amanda-Grace's offer of $3.25 to Molly and Gary's displacement/rebid.
Continue the crowd response without adding per-person deliberation. Let the
price-adjustment mechanism account for any claimed return toward $4.

At $3 the discrete cast has Qd 8 and Qs 4. In the separate smooth example,
Qd = 45 and Qs = 20 thousand pounds. Never show one set of readouts on the
other population's graph. Return to the saved equilibrium before the next test.

### Above equilibrium · excess and downward pressure

Reuse episode `3.a`–`3.d`: set the displayed price to $6, leave unsold units
visible, then show Molly's cut to $5, Gary's switch from Andrew, and subsequent
cuts. Preserve the “excess” terminology. This is a useful callback to the
earlier CS/PS close-up: excess units and gains from trade are different things.

At $6 the discrete cast has Qd 2 and Qs 10. The smooth example has Qd = 30 and
Qs = 80 thousand pounds. The $6 allocation currently uses named choice lists
to put Gary with Andrew; retain this explicit staged reset rather than imply
it is necessarily the allocation reached by the random run.

### At equilibrium · an individual's deviation

Reuse episode `4.a` and `5.a` after restoring the equilibrium. Select the actual
pair and outside options that support each comparison. The existing prototype
tests Andrew raising $4 to $4.25 against an MB-$4 buyer, and an offer of $3.75
against the seller's acceptable terms. The notes also discuss a seller cutting
and a buyer offering more: use the same pair's payment/surplus geometry to show
the consequence if those illustrations are retained in the revised script.

A seller losing a marginal buyer is an example with these values, not proof
that every seller loses all business whenever a tag rises. Distinguish the
successful switches shown during discovery from the lack of a profitable
permitted deviation at the supported equilibrium. Restore the same snapshot
after each attempt so the comparisons remain interpretable.

### Coda · Prices coordinate choices

Return to the notes' PPF question using the existing `5.b` material. A price
ratio connects the markets to specialization and the choice of quantities.
The carrot price is still unspecified in the current notes; keep that writing
decision visible rather than fabricate a second market equilibrium. The current
prototype's A3 rate is an illustrative reuse, not a derived carrot price.

## Editing and implementation order

The small-player branch comes first in both the build and the eventual playback.
Next implement the crowd and its saved outcome, then the deviations using the
same data and visual vocabulary. Keep the one-pair price line and close-up as
the first visual review milestone.

For now identify beats by **scene + existing ID** (`PriceDiscovery:1.a`,
`PostedPrice:2.a`, and so on); both scenes already use the same dotted numbers
for different content. Choose unified literal pause IDs when a combined scene
is actually built. Do not renumber the author's note cues during this planning
pass. Keep the existing files runnable as references and record implemented
changes in the detailed storyboard when coding begins.

Writing reconciliation is now explicit: discovery precedes deviations; the
companion/lecture split and algebra's exact placement are still editorial;
the small-pair surplus explanation is requested. The existing rice/spinach,
Marryville/Maryville, Cindy/Amanda-Grace, and pounds/kilograms differences remain
for the writing pass. Animation layout and draft fixtures must not silently
settle those choices.
