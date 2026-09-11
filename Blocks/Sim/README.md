# Part B: a small market world

This proof of concept connects people, exchanges, and the economic model.
The plane gives transactions a place to happen; a flat panel makes their
economics readable. Start with `OneAgent`, then watch the scenes in order.

## Run it

Use the course's **ManimL** command, as in A1, A2, A3, and B0:

```sh
cd Blocks/Sim
maniml part_b.py OneAgent
maniml part_b.py OneTrade
maniml part_b.py MarketRound
maniml part_b.py PolicyComparison
```

Right advances to the next named pause; left returns; up/down jump between
checkpoints. Saving the file reloads it in the development viewer.

```sh
maniml part_b.py OneAgent --render
maniml part_b.py OneAgent --export-checkpoints
maniml part_b.py OneAgent --export-present
```

These produce a video, checkpoint PNGs, and a browser presenter, respectively,
under `Blocks/Sim/media/`. Substitute any scene name. `--present` validates
the whole scene before opening a live presentation at its first checkpoint.
For numerical checks without Manim, run from the repository root:

```sh
python3 -m unittest discover -s Blocks/Sim -v
```

## Four scene types

| Scene | Teaching purpose | What happens |
|---|---|---|
| `OneAgent` | Separate value from price | A buyer moves with a floating WTP label. In the flat dollar model, price falls from 12 to 6 while WTP stays 10; potential gain becomes 4. |
| `OneTrade` | Explain one exchange before aggregating | A buyer with WTP 10 visits a seller with cost 4. A unit and payment of 6 move in opposite directions; realized CS is 4 and PS is 2. |
| `MarketRound` | Connect individual decisions to a market | Four buyers and four sellers appear with their values/costs. The same data form demand/supply steps. Three buyers approach sellers; the ledger and surplus bars accumulate. |
| `PolicyComparison` | Hold the population fixed while changing rules | Fresh rounds show the baseline, a ceiling, external damage without a ceiling, and a corrective tax. A bystander makes damage outside the exchange visible. |

These are short independent scenes, not a replacement for B0 or a finished
lecture episode. Each introduces a concrete instance before a whole market.

## Three visual layers

| Layer | Objects | Meaning |
|---|---|---|
| **World** | Tilted plane, simple buyer/seller tokens, spillover lines | Who approaches whom, who remains unmatched, and who is affected outside the exchange. Distance is not a cost. |
| **Attached information** | ID and WTP/cost above each token | The label follows its person and stays upright. Movement does not change the value. |
| **Flat model** | Dollar comparisons, D/S steps, price readouts, welfare ledger | Quantitative comparisons use screen coordinates, free from perspective distortion. |

The camera stays in one shallow 3D view. `Agent.body` is the moving world
object; `Agent.label` is projected onto the screen from its body's location.
`fixed(...)` keeps a model object on the screen. The small renderer adapter
keeps these flat labels separate from ManimL's 3D depth handling.

`scene_layers.py` also contains a temporary native-render workaround: this
ManimL version reuses a scratch depth texture in flat fills, clipping text to
the preceding 3D floor. The adapter clears that scratch texture before flat
fills. It changes no installed engine files; the browser renderer is unaffected.
The fixed camera also avoids this version's incomplete restoration of camera
orientation when seeking backward.

Graphite's `DEMAND` identifies buyers, demand, and CS; `SUPPLY` identifies
sellers, supply, and PS; `GOV` means government receipts; `EXT` means the
outside effect. Text reinforces the colors. All palette, type, and frame
settings come from [shared style](../_Assets/style.py), following the
[course guide](../_Style_Guide.md). The neutral plane is staging, not data.

## Keep the economic meanings distinct

**WTP** is a buyer's value for this unit; **cost** is a seller's opportunity
cost. Neither is an offer. The price is the payment in an untaxed trade;
with a tax, buyer payment and seller receipt are different numbers.
**Potential gain** precedes a transaction; **realized surplus** enters the
ledger after settlement. Willing buyers, willing sellers, and completed
trades are three different counts.

A round displays a price, determines willingness and pairs, animates visits,
settles trades, and summarizes the result. Each participant has one unit and
can trade once. Unmatched people remain visible. The economics is computed
before movement; an updater can move a label or roll a number, but cannot
authorize another sale. Walking speed and camera position cannot change it.

This is a **benchmark at specified prices**, not price discovery. Highest-WTP
willing buyers trade with lowest-cost willing sellers. Under the ceiling,
that priority is a rationing assumption: another allocation can have the same
quantity and lower welfare. Ties use IDs; zero-private-gain participants are
willing. The separate efficient-quantity calculation counts strictly positive
social gains.

## The example and its accounting

`BUYERS` have values `[12, 10, 8, 6]`; `SELLERS` have costs `[2, 4, 7, 9]`.
All numbers are dollars for one unit. The policy scene resets trades and
surplus between cases rather than counting the same goods twice.

| Case | Buyer pays | Seller receives | Trades | CS + PS + GOV | Damage | Social gains |
|---|---:|---:|---:|---:|---:|---:|
| Baseline | 7.5 | 7.5 | 3 | 17 | 0 | 17 |
| Ceiling | 5 | 5 | 2 | 16 | 0 | 16 |
| External damage, no ceiling | 7.5 | 7.5 | 3 | 17 | 9 | 8 |
| Corrective tax of 3 | 8.5 | 5.5 | 2 | 16 | 6 | 10 |

The ceiling leaves four buyers willing but only two sellers willing. The
tax prices are selected example prices, not a calculation of tax incidence.
With damage of 3 per exchange, the third trade creates private gain
`8 - 7 = 1` but social gain `8 - 7 - 3 = -2`. Preventing it raises social
gains. Tax revenue is a transfer; it does not erase the damage that remains.

```text
CS = value - buyer payment
PS = seller receipt - cost
GOV = buyer payment - seller receipt
social gains = CS + PS + GOV - external damage
```

## Where to edit

- [part_b.py](part_b.py): example constants, small visual helpers, and the
  four scenes. Read each flat `construct()` as a storyboard. Dotted beat
  comments and literal `self.pause('1.a')` calls follow the current course
  convention; helpers do not hide entire beats.
- [market_model.py](market_model.py): `Buyer`, `Seller`, immutable `Trade`
  records, and `clear_market(...)`. It has no Manim dependency.
- [scene_layers.py](scene_layers.py): the small ManimL adapter for the camera,
  projected labels, screen-fixed models, and native text rendering.
- [test_market_model.py](test_market_model.py): checks identities, rationing,
  taxes, subsidies, price bounds, external costs, empty markets, and ties.

Change the four values, four costs, and prices at the top of `part_b.py`.
Prices and result captions follow the constants; graph steps sort the values
and costs. Review the explanatory wording and graph ranges when changing the
example. More participants also
need more `ROWS` and room on the graph. `OneAgent` and `OneTrade` have their
own 10/4/6 example inside `construct()`. Positions only rearrange the drawing.
`number_row(...)` binds a stable label and rolling number to one tracker;
`MarketGraph` builds the market panel.

`clear_market(...)` takes a buyer price and optional `seller_price` for a tax
or subsidy, plus `external_cost` per unit. `buyer_priority` accepts a full
ordering of buyer IDs for rationing. `price_ceiling`/`price_floor` check the
given buyer price; they reject illegal inputs rather than select a price.

## Next useful extensions

Add one person's **marginal-unit schedule**, then animate copies of those
units into D/S steps while preserving their identities. The current graph
uses the same data, but does not yet animate this sorting transition.
A later **search-and-price-discovery** scene needs an information rule, an
offer-update rule, and a stopping rule. **Provisional matching** needs tentative
reservations before settlement. Price floors, subsidies, alternative rationing,
and multiple periods can reuse these views; government purchases additionally
need public inventory and a budget. Introduce each when its lesson needs it.

## Verification

All four scenes were rendered and visually checked, with presenter bundles at
2160 × 1080 and 60 fps in `media/`. The 10 economic tests pass. Checkpoint
checks cover forward, backward, and replay behavior in `OneAgent` and
`MarketRound`, including label anchors and surplus counters. `MarketRound`
was also checked in the live WebGPU viewer, including reversing and replaying
the first exchange.
