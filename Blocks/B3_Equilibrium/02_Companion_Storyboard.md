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
