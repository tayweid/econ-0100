# B3 Episode | Posted Price — 3D Storyboard (Track B)

<!-- ED (2026-09-20, Fable) — status update: the global order is now governed by 02_Storyboard.md (discovery first; these deviation beats move to the back end), and the animator is Astra. Three things below predate Taylor's 2026-09-20 direction: the Fable 5 handoff framing, "midpoint vs posted" as the track split, and the no-CS/PS-in-B3 ground rule — per-pair CS/PS is now B3 vocabulary via the discovery close-up (market-wide triangles and total surplus remain B4's). Read README.md first. The cast, data, mechanics, and beat table below remain the working inventory for the deviations branch. -->

Handoff document for the animator. Read this whole file before writing code. It is self-contained, but three neighbors give you everything else you need: [01_Notes.md](01_Notes.md) is the professor's episode script and carries the beat IDs you will stage; [02_Companion_Storyboard.md](02_Companion_Storyboard.md) is the sibling scene (Track A: bilateral price discovery, first pass built in [Animate.py](Animate.py)); [../Sim/README.md](../Sim/README.md) documents the engine, style, and run commands.

**What this scene is.** The episode's standard mechanism, made agent-visible: sellers post a price; when it is wrong, incentives fix it. Shortage → buyers bid up. Excess → sellers cut and buyers switch. Equilibrium = the price where nobody wants to change. It is the same world as Track A but with exactly one mechanic swapped: **per-seller posted price tags** instead of bilateral midpoint deals. Track A shows prices *emerging with no coordination at all*; this scene shows a *posted* price being corrected — it is the staging of the episode script itself.

**Ground rules.**
- The professor's prose is untouchable: never edit 01_Notes.md. Your storyboard authority is this file plus the bare dotted-ID beat comments in the notes (ED: comments there are editorial, not staging).
- No CS/PS overlays anywhere in this scene — surplus belongs to B4. The panel shows curves, quantities, the price line, and gauges only.
- The panel is the truth; the world is staging. All economics is computed in `market_model.py` before anything moves. An updater may move a label; it may never authorize a trade.
- Style: Graphite, from [../\_Assets/style.py](../_Assets/style.py) per [../\_Style_Guide.md](../_Style_Guide.md). DEMAND colors buyers/demand; SUPPLY colors sellers/supply. Same three-layer staging as Sim/: world plane · attached labels · screen-fixed flat model.
- Determinism: agents act in ID order; no randomness. Literal `self.pause('2.a')` checkpoints at every beat ID below, maniml conventions as in A1–A3/B0 and Animate.py.
- Questions: leave `# ANIMATOR-Q:` comments in code and list them in your report; do not resolve prose ambiguities yourself.

## Cast and data

Ten buyers, ten sellers, one unit each. Staircases cross at **$4**, matching the episode's decided market numbers (D: P = 12 − Q/5, S: P = 2 + Q/20, equilibrium (40, $4) in thousands of pounds — this little crowd *gestures at* those curves; it is not their literal data, and the flatten beat (4.b) makes the handoff).

| Side | Values (bars over heads) |
|---|---|
| Buyers (MB) | 6, 6, 5, 5, 4, 4, 3, 3, 2, 2 |
| Sellers (MC) | 2, 2, 3, 3, 4, 4, 5, 5, 6, 6 |

Checks: at $3 → Qd 8 vs Qs 4 (shortage 4); at $6 → Qd 2 vs Qs 10 (excess 8); at $4 → 6 = 6. Integer midpoints throughout; ties break by ID.

Named cast (CAST DECISION 2026-09-17, per chat — the notes currently say "Cindy" for the queue-jumper; the professor is renaming her **Amanda-Grace** in his prose pass, and this scene uses Amanda-Grace from the start):

| Agent | Side | Value | Role |
|---|---|---|---|
| **Amanda-Grace** | buyer | MB 6 | jumps the queue at the shortage ($3 → $3.25), continuing her B1 role as the willingness-to-pay buyer |
| **Gary** | buyer | MB 6 | the displaced one — bumped from Molly at the shortage; switches from Andrew to Molly's cheaper tag at the excess |
| **Molly** | seller | MC 2 | accepts Amanda-Grace's overbid; first to cut at the excess ($6 → $5) |
| **Andrew** | seller | MC 4 | sells to Gary at $6, loses him to Molly's cut, follows the cut down |
| others | — | remaining values | anonymous townsfolk |

Buyer seller-choice at $6 is story-cast: Gary buys from Andrew (choice lists are deterministic inputs, not randomness). At $6 only Gary and Amanda-Grace buy (the two MB-6 agents), so Molly is left holding crates — exactly as the notes need.

## Mechanics (the one new rule set)

State: every seller has a posted tag; a buyer is served (thread to a seller at that seller's tag price) or unserved. One unit each.

1. **Serve at posted prices**: willing buyers (MB ≥ best available tag) buy from the cheapest tags, ID/choice-list order. Willing-but-unsold sellers show **crates**; willing-but-unserved buyers form the **queue**.
2. **Shortage step** (queue > 0): an unserved willing buyer overbids a serving seller by a tick; the seller switches to the better offer; the displaced buyer joins the queue and rebids. Tags ratchet up.
3. **Excess step** (crates > 0): a crated seller cuts her tag by a tick; served buyers switch to the cheaper tag; the abandoned seller now has crates and cuts too. Tags ratchet down.
4. **Participation**: nobody deals at a loss. As tags fall, sellers with MC above the going tag pull their tags and withdraw; as tags rise, buyers with MB below drop out of the queue — the staircase fills track the moving line (movement *along* the curves, never a shift).
5. **Stopping**: both gauges at zero — no crates, no queue — and no profitable overbid or undercut exists. Tags settle in the band around $4.

Dramatized first moves use the notes' own numbers (Amanda-Grace +$0.25; Molly's cut $6 → $5); the ensuing cascade runs in **$0.25 ticks**. The notes' "and would even buy a little extra" (Gary at the lower price) is a multi-unit beat the one-unit engine defers — leave an ANIMATOR-Q if you want to fake it visually; do not add multi-unit logic for it.

Model first, animation second: implement the tag vector, `leftovers(p)`, `queue(p)`, the overbid/undercut steps, and buyer choice lists as pure functions in [../Sim/market_model.py](../Sim/market_model.py) with tests beside the existing ten (convergence into [$4 − tick, $4 + tick] from $3 and from $6; monotone gauge decline; the displacement chain terminating; no-loss participation; withdrawal/entry as the line moves; ties by ID). All 3D work waits until those pass.

## Beats

IDs are the notes' own (the beat comments in 01_Notes.md are the same storyboard — this table adds the world staging). 0.a and 4.b–5.b are panel/2D beats; the world carries 1.a–4.a.

| Beat | Notes line it lands on | World | Panel (screen-fixed) |
|---|---|---|---|
| 0.a | title | — | MICROECONOMICS raster, "Part B \| Episode 3" |
| 1.a | recap, two curves | platform in; buyers file left, sellers right; MB/MC bars grow over heads | each bar's twin flies up; twins sort into the demand staircase, then supply; the smooth B1/B2 market curves ghost over the staircases (the many-farmers limit) |
| 1.b | the floating price | a blank price tag hovers over the sellers' side | price line with "?" drifts up and down |
| 2.a | shortage at $3 | tags post $3; four sellers crate up and serve; eight buyers cross; a **queue** of four forms | line drops to 3; Qs fills 4, Qd fills 8; queue gauge reads 4 |
| 2.b | Amanda-Grace jumps the line | she steps out of the queue, offers Molly $3.25; Molly's thread to Gary snaps; Gary back to the queue | Molly's tag ticks to 3.25 |
| 2.c | shortage lesson | Gary rebids; tags ratchet up in $0.25 ticks; more sellers crate up as tags pass their MC; queue drains | line climbs; up-arrows on both sides; queue gauge → 0 near $4 |
| 3.a | excess at $6 | reset: tags post $6; all ten sellers crate up; only Gary (from Andrew) and Amanda-Grace buy; eight sellers hold **crates** | line jumps to 6; Qs 10 vs Qd 2; crates gauge reads 8 |
| 3.b | excess, not surplus | world holds | the word "surplus" appears, is gently crossed out, "excess" replaces it |
| 3.c | Molly undercuts | Molly cuts her tag to $5; Gary's thread swings from Andrew to Molly; Andrew, crated, cuts too | tags tick down; line follows |
| 3.d | excess lesson | cascade continues; high-MC sellers pull tags and withdraw; new buyers step in; crates vanish | down-arrows both sides; crates gauge → 0 near $4 |
| 4.a | the price that doesn't move | perturbation test: one seller tries $4.25 → instant crates; one buyer tries $3.75 → refused; tags settle back to $4 | both gauges read 0; the line holds still for the first time |
| 4.b–4.d | algebra | world fades under the panel | camera flattens; staircases dissolve into the smooth curves (axis relabels to thousands of pounds); equations write out; solve 2 + Q/20 = 12 − Q/5 → Q\* = 40, P\* = $4; star; combined graph |
| 5.a | stable | — | perturb-and-return on the combined graph |
| 5.b | PPF tieback | — | per the notes' 5.b beat comment (market graph to a corner; the two-farmer PPF returns; the two prices form the exchange-rate line) |

## Build order and verification

1. Model rules + tests in Sim/ (pure Python, no Manim). Run `python3 -m unittest discover -s Blocks/Sim -v` — all pre-existing tests must stay green.
2. Scene skeleton with all pausepoints and static layouts; then beat by beat. Reuse Agent, bars, panel, and thread vocabulary from Animate.py — if you extract shared helpers so both scenes import them, keep the refactor mechanical and note it in your report. New props: price tags, crates, queue markers, the two gauges.
3. Scene lives beside PriceDiscovery (same file or sibling — your call, report it). Suggested name: `PostedPrice`.
4. Verify like Sim/README describes: render, `--export-checkpoints`, walk every pause forward and backward, then `--export-present`. Check label anchors and gauge counters across seeks (see the camera-seek notes in memory: scale/shift safe, orientation not — this scene's camera should stay home until the 4.b flatten).
5. Report back: what built cleanly, every ANIMATOR-Q, and a checkpoint-per-beat screenshot set.
