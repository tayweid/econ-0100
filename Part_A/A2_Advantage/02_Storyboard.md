# Episode A2 | *Better choices alone can increase what's possible* — Storyboard (v5, 2026-08-31)

> v5 (third director's pass): a new **B00 office-hours card** opens the episode before the
> bumper (photo right half, `Come to office hours :)` + hours left half, `FadeAll` into B01).
> **Numerals are INK, letters carry the good's color** everywhere the two mix — the cost-table
> entries were whole-entry green/orange and are now split (numeral white, letter colored); the
> farm-card `ON_FILL` tags are the one exemption. **Andrew's OC derivation moves off the co-op
> graph onto the table screen** (old B07/B07b/B07c become B08c/B08d/B08e, in Molly's spot,
> mirroring her ritual); only the `Indicate` pulse on his flatter PPF stays on the graph
> (B07). His `or` → `=` two-step goes with the move: he now opens on `=`, as Molly does. The
> **derivation math is rebuilt as separate numeral and letter mobjects** around a fixed `=`:
> the letters and the sign never move or re-render, and each step `Transform`s the numerals
> only, each anchored to the left of its own letter so a widening fraction grows leftward.
> **Vertical centering** is now a guide rule (§1) and is applied: on the co-op screen the farm
> column and the graph share one centre in the band under the title. The advantage beats get
> **a pause between each pair of boxes** (B04c/B04d for Absolute Advantage, B09b/B09c for
> Comparative). Net: 46 beat stops (+3 named pauses, −1 from the derivation move absorbing the
> old joint-reveal beat), 159 checkpoint images, 132 s of render.
>
> v4 (second director's pass): the specialized frontier is now **drawn by the co-op dot**, the
> way the straight line is at B06 — Andrew's round trip to his other crop traces the upper
> branch and Molly's traces the lower one, so the old one-shot `Create` splits into B11d/B11e
> with the gains fill on its own beat (B11f). In the autarky panels the farmers' names move
> **under the axes** from B15 and each one *grows into* its own self-trade rate there, so the
> in-plot curve names are gone; Andrew's `Self-Trade` label hugs his arrow; the B16e hook is
> centred on the frame; and the `Autarky` definition takes the subtitle slot the hook later
> uses, because the bottom band now belongs to the two name lines. Exercise-card **bodies are
> in the narrator's sans** (a style trial; heads stay serif gold).
>
> v3 (director's pass on the v2 render): the **B07 zoom is cut** — Andrew's OC derivation plays
> at full frame (the other two camera moves, B07e–B08b and B16b–B16d, stay). The specialization
> stretch no longer trails pink between the corners: the corner moves are dots + crop morphs
> only, and **B11d draws the true kinked co-op frontier** (0,56)–(8,40)–(18,0) in one sweep
> while the straight line ghosts to `MUTED` and `Co-op` sheds its qualifier; the gains region
> fills after. The two questions are **plain serif `INK`**, not narrator sans in gold (a
> question-list design pass is now deferred in the guide, §9), and the attribution carries
> Ricardo's dates. Both self-trade arrows are `FOCUS` gold — `GUIDE` red was invisible on
> Andrew's red panel — and his panel gets its own gold `Self-Trade` label. The final screen's
> bottom band was cramped: **B16e now retitles to `Autarky → Trade` and hangs the hook line
> under the title** as a subtitle, leaving the bottom to the two stored rate lines; the panels
> are shorter (`y_length` 4.5) and sit lower to make room.
>
> v2 (revision pass): camera moves are back; the co-op line is **traced by the co-op dot**
> instead of `Create`d; the table stretch is a faithful port of the old `animation_2` /
> `animation_3` (Molly's row derived, Andrew's revealed in one gesture, AA/CA as full-frame
> definition cards with the AA marks brought back for the CA beats); `YES!` is smaller with a
> Ricardo attribution; Andrew's panel returns for a mirrored self-trade (B16d). The invented
> whole-column boxes and the `pause(loop=True)` hold are gone.

Source: `01_Notes.md` (current, with the autarky/self-trade block pulled forward from A3).
Code: `03_Code.py`, one scene `EpisodeA2` with one flat `construct()`; every `# Bxx` section is
self-contained — it clears the previous beat's objects, builds its own, and ends at the
`self.pause()` the viewer parks on. Pauses are unnamed; the beat ids below match the section
headers, in scene order. No `wait()`s. Render: `maniml 03_Code.py EpisodeA2 --render`.

Numbers (the new canonical set): Molly 10 C / 40 S, Andrew 8 C / 16 S, carrots **horizontal**.
Co-op no-specialization line through (18, 0) and (0, 56); equal split (9, 28) sits exactly ON
that line; the specialization point (8, 40) is the kink of the true joint frontier; the gains
triangle is (18,0)–(8,40)–(0,56). Molly's self-trade from (0, 40) at 4 S per C lands exactly on
her autarky point (3, 28) — staged that way deliberately, so the sweep *derives* the point the
script picks. `Video.py`'s `PPF_Molly` / `PPF_Andrew` / `PPF_Coop` are updated to this set
(carrots-first), per the note in that file. Old A3 scene code still assumes the old functions;
it gets rewritten in the A3 port.

## The visual spine

Three recurring surfaces, all on the 2:1 stage at once when needed:

**The farm cards** (Molly top-left, Andrew below her): 2.2×2.2 outlines in the owners' colors,
whose carrot/spinach fill split is the crop choice — halves for the co-op's equal-ratio regime,
full-crop for specialization. They anchor the left margin from B03 through B07, **step off when
the table pair arrives** (B07b, as in the old `animation_2`), and return for the specialization
beat. Their two cards straddle the band centre they share with the graph (guide §1).

**The co-op graph** (right): both PPFs plus the co-op dot; the dot-sweep to the two extremes
**traces** the no-specialization line — a `GUILD` `trail_behind()` follows the co-op dot out to
(18, 0) and back up to (0, 56), then hands off to the plotted `PPF_Coop` mobject (the old
`animation_4` choreography, with the line drawn by the dot rather than `Create`d against it).
The same dots later ride to the specialization point (8, 40) one corner at a time — **no trail**,
because the path between corners is an interior chord, not a frontier. The true kinked frontier
(0,56)–(8,40)–(18,0) is then **traced by the co-op dot as well**, and what drives it is a farmer
switching crops: Andrew swings all the way to spinach and back (upper branch, slope −2), then
Molly swings all the way to carrots and back (lower branch, slope −4), with the straight line
ghosting to `MUTED` (A1's `ppf_ghost` idiom) as the first outbound leg starts. The finished trail
hands off to a plotted polyline the way B06b hands off to `PPF_Coop`; the gains triangle (from
old A3 `animation_3`) fills between the two afterwards. Curve
names park in the empty band left of the y-axis, each beside its own intercept — Molly's long
steep PPF sweeps through every in-graph spot a name could otherwise take.

**The table pair** (production + opportunity cost): a faithful port of the old `animation_2`.
All four cost entries start painted `BG` and light up **numeral-first-then-letter** (`4` in INK,
`S` in `SPINACH`); Molly's row is boxed and derived under the tables (10 C = 40 S → divide by 10
→ 1 C = 4 S → box onto `4 S`; box back to the math → 1/4 C = 1 S → box onto `1/4 C`), and then
**Andrew's row runs the identical ritual in the same spot** (8 C = 16 S → divide by 8 →
1 C = 2 S → box onto `2 S`; back to the math → 1/2 C = 1 S → box onto `1/2 C`) — the derivation
that used to play under the co-op graph. The camera frames the pair on arrival and shifts back
up only when *Andrew's* math clears, so both derivations play at the same crop.
Every derivation on the stage is built the same way: the good's **letter and the `=` are placed
once and never move or re-render**, and each algebra step `Transform`s only the numeral, which
hangs to the left of its letter with its right edge anchored — so `10` → `10/10` → `1` grows and
shrinks leftward and the line reads as arithmetic on the numbers, not as re-typesetting.
AA and CA are **full-frame definition cards**
(the old `animation_3` rhythm), and the AA label plus its two boxes come back with the tables
for the CA beat so both concepts are boxed on screen at once.

Exercise cards via `exercise_card()` (promoted from A1's file into `_Assets/style.py`).

Every animation from the old `03_Code.py` (`animation_0`–`animation_4`) and from A3's pulled-
forward material (`animation_3`'s gains region + question, `animation_4`'s self-trade sweep and
exchange-rate derivation) survives, renumbered into the beats below — and the `animation_2` /
`animation_3` table stretch is ported play-for-play, not paraphrased. Two small adaptations:
the old `or → =` two-step is gone from **both** derivations — the self-trade one because a trade
is an exchange rather than an alternative, Andrew's because it now mirrors Molly's, which has
always opened on `=` (and because the sign is a fixed mobject that never re-renders, v5) — and
the old "Guild PPF (no specialization)" → "Guild PPF" label rename becomes the qualifier line
fading as the kinked frontier draws, so `Co-op` ends up naming that line.

| script idea | what the stage does |
|---|---|
| (housekeeping, before the episode) | office-hours card: photo right half, `Come to office hours :)` + hours left half; `FadeAll` into the bumper |
| Molly is better at both | production table; AA definition card; label + boxes on Molly's two entries, **one beat each** |
| equal-ratio co-op | farms split half/half, dots at (5,20) and (4,8), copies merge into the co-op dot at (9,28) |
| the co-op PPF is a line through the extremes | dots ride to all-carrots, then all-spinach; the co-op dot *traces* the line; back to the split |
| Andrew's flatter PPF | FOCUS pulse on his curve, full frame (no zoom) — the pulse is about the *curve*, so it stays on the graph screen; his arithmetic moved to the tables |
| the cost table gets built | tables framed by the camera; Molly's row derived both ways, then Andrew's row derived both ways in the same spot |
| comparative advantage | CA definition card; tables return with the AA marks; box on Andrew-carrots, then a beat later on Molly-spinach |
| specialization beats the line | Molly's corner, then Andrew's (dots + crops, no trail); each farmer then swings all the way to their other crop and back, the co-op dot *tracing* the kinked frontier as the straight line ghosts; then the gains triangle fills |
| the two questions | numbered white serif questions + a smaller YES!; `— David Ricardo (1772 – 1823)` |
| autarky | two same-scale panels side by side; INK dots with muted drop-lines at (3,28)/(4,8) |
| self-trade | sweep (0,40)→(3,28) with live readout and exchange bars; 3 C = 12 S divides to 1 C = 4 S (zoomed); Exchange Rate = Opportunity Cost |
| both self-trades | Molly's math files into her under-axis name, which grows into her rate; Andrew's panel returns and mirrors the sweep (8,0)→(4,8) with its own gold arrow and label; his name grows the same way; the title turns to `Autarky → Trade` with the hook centred beneath it |

## Beats

| # | Script cue | Mode | Action | Status |
|---|-----------|------|--------|--------|
| B00 | (housekeeping, before the cold open) | anim | Office-hours card: the photo (`_Assets/Max_Photos/2026_08_31_rounded.png`, rounded corners baked into the alpha) fills the **right half** — equal 0.6 margins top/right/bottom, so its height is the frame's minus two margins; `Come to office hours :)` in TITLE azure at title scale on the **left half** with `2:30 – 3:30 Wed/Thurs` in CAPTION beneath, the pair centred on the photo's own vertical centre. `FadeAll` into the bumper | [ok] |
| B01 | (cold open) | anim | Bumper: raster MICROECONOMICS fades in | [ok] |
| B01b | — | anim | Flicker, blues cycling | [ok] |
| B01c | — | anim | `Part A \| Episode 2` joins; thesis line *Better choices alone can increase what's possible.* below | [ok] |
| B02 | (silent) | anim | `Last Time...` card | [ok] |
| B03 | "It turns out Molly isn't the only farmer in the area. Another farmer, Andrew…" | anim | Molly's farm card fades in, then Andrew's below it | [ok] |
| B04 | "He can grow 8 tons of carrots per year or 16 tons of spinach… ***Show: the production table***" | anim | Production table (10/40, 8/16) + `Production Table: Farmers' Capacities` line | [ok] |
| B04b | "Molly is also able to produce more of both goods, so she has the ***absolute advantage***…" | anim | Stage clears; AA **definition card** writes full-frame (`animation_3` rhythm) | [ok] |
| B04c | "…in both carrots and spinach." (***box Molly's row***) | anim | Card fades, table + farms return (the table now centred on the same band centre as the farm column, guide §1); `Absolute Advantage` gold label; box on Molly's **carrots** entry | [ok] |
| B04d | (…and spinach) | anim | Box on Molly's **spinach** entry — its own beat, so the two capacities land separately | [ok] |
| B05 | "Molly and Andrew decide to form a local farmers co-op…" | anim | Table clears; title *The Co-op*; axes (carrots horizontal) + colored axis captions; both PPFs draw with INK name labels beside their intercepts. The graph and the farm column now share **one vertical centre** in the band under the title (guide §1) | [ok] |
| B05b | "Dividing their farms equally between crops, Andrew will produce 4 carrots and 8 spinach, and Molly 5 carrots and 20 spinach." | anim | Farm fills split half/half; Molly dot (5,20), Andrew dot (4,8) | [ok] |
| B05c | "This adds up to 9 carrots and 28 spinach." | anim | Copies of the two dots merge into the purple co-op dot at (9,28) | [ok] |
| B06 | "…the co-op's PPF is just a line running through the co-op's extreme points…" | anim | Crops morph all-carrots; dots ride to (10,0)/(8,0)/(18,0); the co-op dot starts **tracing** the GUILD line | [ok] |
| B06b | "…18 carrots and 56 spinach, just the extreme points for the two farms added together." | anim | Crops morph all-spinach; dots ride to (0,40)/(0,16)/(0,56); the trail completes the line and hands off to the plotted mobject; label `Co-op` + `(no specialization)` | [ok] |
| B06c | "Under this regime…" | anim | Everything returns to the equal split | [ok] |
| B07 | "Again, this is visualized by Andrew's flatter PPF…" | anim | FOCUS pulse on Andrew's curve, with the whole graph already in view. **Only the pulse lives here now** — his arithmetic moved to B08c–B08e | [ok] |
| B07b | "***Show: the opportunity cost table joins the production table***" | anim | Graph **and farm cards** clear; the table pair fades in (all cost entries hidden) as the **camera frames the pair**; box lands on **Molly's** production row | [ok] |
| B08 | "Molly gives up 4 spinach for every carrot…" | anim | Box travels down to the math; `10 C = 40 S` → divide by 10 → `1 C = 4 S` (the `C`, `S` and `=` never move; only the numerals transform); box travels onto Molly's carrots cost entry as `4 S` lights up — **numeral INK, letter green** | [ok] |
| B08b | "…and 1/4 of a carrot for every unit of spinach." | anim | Box back to the math; the numerals flip to `1/4 C = 1 S`; box onto Molly's spinach entry as `1/4 C` lights up; her math fades. **The camera stays down** — Andrew's lands in the same spot | [ok] |
| B08c | "Like we did for Molly, Andrew's opportunity cost of carrots is 2 spinach." | anim | Box onto Andrew's production row, then down to the math spot Molly just vacated; `8 C = 16 S` fades in there (moved from the old B07, now opening on `=` like hers) | [ok] |
| B08d | (divide through, reduce) | anim | Both numerals divide by 8, then reduce to `1 C = 2 S`; box travels onto his carrots cost entry as `2 S` lights up | [ok] |
| B08e | "…and 1/2 a carrot for every unit of spinach." | anim | Box back to the math; numerals flip to `1/2 C = 1 S`; box onto his spinach entry as `1/2 C` lights up; his math fades and the **camera shifts back up**; box fades | [ok] |
| B09 | "Having a lower opportunity cost is what we call **comparative advantage**." | anim | Tables clear, camera home; CA **definition card** writes full-frame | [ok] |
| B09b | "Andrew has a comparative advantage in carrots…" | anim | Card fades; tables return **carrying the `Absolute Advantage` label and its two boxes**; `Comparative Advantage` label under the cost table; box on Andrew's `2 S` | [ok] |
| B09c | "…and Molly has a comparative advantage in spinach." | anim | Box on Molly's `1/4 C` — its own beat, as the AA pair get theirs; both concepts boxed on screen at once | [ok] |
| B09d | "When one farmer's opportunity cost is lower in one crop, the other farmer's will always be lower in the other." | anim | Two-line caption under the tables | [ok] |
| B10 | "***Cut to Exercise A2 \| Q1.***" | anim | Exercise card: McGonagall 10 R / 5 F; production + OC tables; who has AA / CA in rock cakes? | [ok] |
| B11 | "Molly realizes that maybe there's something to this idea…" | anim | Co-op stage rebuilds: title, axes, PPFs, line + labels, farms with `1C=4S` / `1C=2S` tags, half/half crops, three dots | [ok] |
| B11b | "…Molly grows only spinach, growing 40." | anim | `Spinach` advantage label writes; Molly's crops go all-spinach; her dot to (0,40); the co-op dot rides to (4,48) = (0,40)+(4,8). **No trail** | [ok] |
| B11c | "And Andrew grows only carrots, growing 8." | anim | `Carrots` label writes; Andrew's crops go all-carrots; his dot to (8,0); the co-op dot to (8,40), the kink. Still no trail | [ok] |
| B11d | "…the co-op was able to exceed the frontier." | anim | FOCUS wiggle on the co-op dot; a GUILD trail starts behind it. **Andrew's round trip**: his crops morph carrots→spinach, his dot rides (8,0)→(0,16) and the co-op dot rides (8,40)→(0,56), **tracing** the upper branch — while the straight line ghosts to MUTED and the `(no specialization)` qualifier fades, so `Co-op` now names the kinked line. Then everything returns: crops back to carrots, his dot to (8,0), the co-op dot home to the kink | [ok] |
| B11e | (Molly's side of the same move) | anim | **Molly's round trip**: her crops morph spinach→carrots, her dot rides (0,40)→(10,0) and the co-op dot rides (8,40)→(18,0), tracing the lower branch; then everything returns and the dot parks on the kink again. The completed trail hands off to a plotted GUILD polyline (0,56)–(8,40)–(18,0) — same geometry, invisible swap | [ok] |
| B11f | — | anim | The gains triangle (18,0)–(8,40)–(0,56) fills TRADE with its `Gains From Specialization` label under the graph | [ok] |
| B12 | "***Cut to Exercise A2 \| Q2.***" | anim | Exercise card: who should specialize in each good? | [ok] |
| B13 | "…we're left with two large remaining questions. First, a co-op… could be a lot of work." | anim | Title *Two Remaining Questions*; numbered line `1. But is a co-op necessary?` in plain `INK` serif (no `narration()`) | [ok] |
| B13b | "Second, can we organize specialization… making both farmers better off at the same time?" | anim | `2. Can both farmers be better off at the same time?`, same treatment, left-aligned under the first | [ok] |
| B13c | "…to which the answer is an optimistic YES!" | anim | `YES!` writes in FOCUS at scale 1.4 | [ok] |
| B14 | "…the model proposed by David Ricardo in 1817…" | anim | `— David Ricardo (1772 – 1823)` writes below and right of the YES!, `CAPTION` — a quotation attribution (em dash before the name, en dash between the years) | [ok] |
| B15 | "To model this environment, we'll set up two PPFs, one for Molly and one for Andrew." | anim | Two same-scale panels side by side; both PPFs draw, each with a plain INK name — `Molly`, `Andrew` — **centred under its own x-axis**. No in-plot curve labels: the under-axis names plus the owner-colored curves carry the identification, and the same labels grow into the stored rates later | [ok] |
| B15b | "We'll start with autarky, where the farmers don't trade with each other." | anim | Title *Autarky*; the autarky definition writes **centred in the subtitle slot under the title** (the bottom band belongs to the two name lines now) | [ok] |
| B15c | "I'm going to pick the production point of 3 tons of carrots and 28 tons of spinach for Molly, and 4 tons of carrots and 8 tons of spinach for Andrew." | anim | INK dots + muted dashed drop-lines at (3,28) and (4,8), caption coordinate labels | [ok] |
| B16 | "Each farmer could… switch part of their farm from growing their comparative advantaged crop to growing the other good. This **self-trade**…" | anim | Andrew's panel clears; endowment dot at (0,40); **FOCUS** curved arrow + gold `Self-Trade` label; sweep to (3,28) — landing on the autarky marker — with live readout and exchange bars | [ok] |
| B16b | "…has an **exchange rate** that's exactly equal to their opportunity cost." | anim | `3 C` / `12 S` fly off their bars into the equation, the `=` fading in as they land; **camera pushes in on the derivation**; divide by 3, reduce to `1 C = 4 S` — again the letters and the `=` hold still and only the numerals transform. Her under-axis `Molly` sits outside the crop and is waiting for this result — it takes it at B16d | [ok] |
| B16c | "The slope of the PPF tells us exactly what opportunity cost tells us." | anim | `Exchange Rate = Opportunity Cost`, both terms gold (still zoomed) | [ok] |
| B16d | (Andrew's side of the same move) | anim | The equation files down under her panel as the **camera returns to full frame** — and her under-axis `Molly` **grows in place into `Molly: 1 C = 4 S`** to receive it (Transform, C in CARROTS, S in SPINACH). Andrew's panel fades back in on the right with his plain under-axis `Andrew`; curved **FOCUS** arrow (8,0)→(4,8) with its own gold `Self-Trade` label **hugging the arc off its outer corner**, and a mirrored sweep with the same live readout; then his label grows the same way into `Andrew: 1 C = 2 S`. Both rates on screen together | [ok] |
| B16e | "Essentially, Molly is looking for a trade that is a better deal than her PPF." | anim | The title transforms `Autarky` → `Autarky → Trade`; the gold hook line *Molly is looking for a trade better than her self-trade.* writes in the same subtitle zone but **centred on the frame**, not left-aligned under the title — the bottom band stays with the two rate lines | [ok] |
| B17 | "***Cut to Exercise A2 \| Q3.***" | anim | Exercise card: McGonagall's cost of 1 F herself; a better trade with Hagrid | [ok] |
| B18 | "Next time…" | anim | Title *Next time...*; `Trade can make both parties better off.` framebox reveal; runs to black | [ok] |

## Pausepoints

One unnamed `self.pause()` per beat above except B01/B01b (the bumper plays through to the
B01c stop, as in A1) and B18 (runs to black with no trailing pause, as in A1's B31). Every stop
is a plain pause — the old `pause(loop=True)` at B08c is gone with the column-box beat it held.
**46 beat stops** plus the scene-start stop; 159 checkpoint images, 132 s of render. (v5
arithmetic: +3 named stops — B00, B04d, B09c — and −1 net from the derivation move, since the
three co-op stops B07/B07b/B07c become the three table stops B08c/B08d/B08e, absorbing the old
one-gesture B08c.)

| stop | press on |
|---|---|
| (scene start) | the office-hours card; first press = photo + invitation |
| B00 | (housekeeping) office hours; press = `FadeAll`, then raster, flicker, part label + thesis |
| B01c | thesis settles |
| B02 | (silent) `Last Time...` card |
| B03 | "It turns out Molly isn't the only farmer in the area…" (two farm cards) |
| B04 | "He can grow 8 tons of carrots per year or 16 tons of spinach…" (production table) |
| B04b | "…so she has the absolute advantage…" (full-frame definition card) |
| B04c | "…in both carrots and spinach." (table back; label + box on Molly's carrots) |
| B04d | (…and spinach) (box on Molly's spinach) |
| B05 | "Molly and Andrew decide to form a local farmers co-op…" (title, axes, both PPFs) |
| B05b | "Dividing their farms equally between crops…" (half splits; two dots) |
| B05c | "This adds up to 9 carrots and 28 spinach." (co-op dot merges) |
| B06 | "…the co-op's PPF is just a line…" (ride to all-carrots; the dot starts tracing the line) |
| B06b | "…running through the co-op's extreme points 18 carrots and 56 spinach…" (ride to all-spinach; the trace completes the line) |
| B06c | "Under this regime…" (return to the split) |
| B07 | "Again, this is visualized by Andrew's flatter PPF…" (curve pulse) |
| B07b | "***the opportunity cost table joins***" (farms out, tables in, camera frames the pair; box on Molly's row) |
| B08 | "Molly gives up 4 spinach for every carrot…" (10 C = 40 S → 1 C = 4 S; `4 S` lights up) |
| B08b | "…and 1/4 of a carrot for every unit of spinach." (1/4 C = 1 S; `1/4 C` lights up; camera stays down) |
| B08c | "Like we did for Molly, Andrew's opportunity cost of carrots is 2 spinach." (his row boxed; 8 C = 16 S arrives in her spot) |
| B08d | (divide through, reduces to 1 C = 2 S; `2 S` lights up) |
| B08e | "…and 1/2 a carrot for every unit of spinach." (1/2 C = 1 S; `1/2 C` lights up; camera shifts up) |
| B09 | "Having a lower opportunity cost is what we call comparative advantage." (full-frame definition card) |
| B09b | "Andrew has a comparative advantage in carrots…" (tables return with the AA marks; box on his `2 S`) |
| B09c | "…and Molly in spinach." (box on her `1/4 C`) |
| B09d | "…the other farmer's will always be lower in the other." (caption line) |
| B10 | "***Cut to Exercise A2 \| Q1.***" |
| B11 | "Molly realizes that maybe there's something to this idea…" (co-op stage rebuilds) |
| B11b | "…Molly grows only spinach, growing 40." (her corner; the co-op dot to (4,48), no trail) |
| B11c | "And Andrew grows only carrots, growing 8." (his corner; the co-op dot lands on the kink (8,40), no trail) |
| B11d | "…the co-op was able to exceed the frontier." (Andrew's round trip traces the upper branch; the straight line ghosts) |
| B11e | (Molly's round trip traces the lower branch; the finished frontier hands off to a plotted line) |
| B11f | (the gains triangle fills) |
| B12 | "***Cut to Exercise A2 \| Q2.***" |
| B13 | "First, a co-op… could be a lot of work." (numbered question 1) |
| B13b | "Second, can we organize specialization…" (numbered question 2) |
| B13c | "…an optimistic YES!" |
| B14 | "…David Ricardo…" (`— David Ricardo` attribution) |
| B15 | "…we'll set up two PPFs, one for Molly and one for Andrew." |
| B15b | "We'll start with autarky…" (title + definition) |
| B15c | "…I'm going to pick the production point of 3 tons of carrots and 28 tons of spinach for Molly…" (markers) |
| B16 | "…this self-trade…" (sweep lands on the autarky marker) |
| B16b | "…an exchange rate that's exactly equal to their opportunity cost." (3 C = 12 S → 1 C = 4 S, zoomed) |
| B16c | "The slope of the PPF tells us exactly what opportunity cost tells us." |
| B16d | (Andrew's side) her under-axis name grows into her rate as the math files into it, his panel returns and mirrors the sweep; both rates on screen |
| B16e | "…Molly is looking for a trade that is a better deal than her PPF." (retitle to `Autarky → Trade`; hook centred in the subtitle zone) |
| B17 | "***Cut to Exercise A2 \| Q3.***" |
| B18 | "Next time…" (framebox; runs to black) |

## On-screen text for review (animator-written, not from the script)

- `But is a co-op necessary?` — the old scene's "But is a guild necessary?", guild→co-op.
- `Can both farmers be better off at the same time?` — distilled from the second question.
- `Two Remaining Questions` (section title), `The Co-op`, `Autarky` (section titles).
- `Trade can make both parties better off.` — A3's episode thesis, as the next-time line.
- `Exchange Rate = Opportunity Cost` — the B16c equality, both terms gold.
- `Molly` / `Andrew` — the panels' under-axis names, from B15 (they replace the in-plot curve
  names, which are gone from this section).
- `Molly: 1 C = 4 S` / `Andrew: 1 C = 2 S` — the same two labels, grown in place into the stored
  self-trade rates at B16d.
- `— David Ricardo (1772 \textendash\ 1823)` — the B14 attribution under the `YES!` (the old
  `David Ricardo, 1817` caption became a quotation credit; the dates are his lifespan, not the
  1817 publication year — **[check]** if the director would rather cite the year of *Principles*).
- `Autarky → Trade` — the B16e retitle: the section turns the corner from autarky to trade.
- `Molly is looking for a trade better than her self-trade.` — the B16e hook, in the subtitle
  zone but centred on the frame (was *…better than her PPF.* at the bottom edge).
- `Self-Trade` — the gold label on **both** panels (B16 for Molly, B16d for Andrew).
- `Come to office hours :)` / `2:30 \textendash\ 3:30 Wed/Thurs` — the B00 card. Course
  housekeeping, not script; the hours need re-checking each term.

## Assets needed

- `_Assets/Max_Photos/2026_08_31_rounded.png` — the B00 office-hours photo, derived from
  `2026_08_31.jpg` (6144×8160) by a one-off PIL pass: downscale to 1600 px tall (1205×1600),
  rounded-rectangle alpha mask at radius 60 px, saved as PNG. The rounding is **baked into the
  alpha** because maniml's `ImageMobject` cannot be masked; regenerating means re-running that
  pass. `ImageMobject` is a bare `Mobject`, so the scene's `drop_frame()` had to be taught to
  spare it (it strips non-`VMobject`s to keep `exercise_card()` safe).
- Otherwise: raster wordmark and style helpers only.

## Open questions

- The style guide §4 orientation invariant still reads "carrots horizontal (A — as rendered in
  A1; reconcile Video.py if it disagrees)" — `Video.py` now agrees; the parenthetical can drop.
- `GUILD` token name vs. the co-op wording: the purple token in `style.py` is still `GUILD`.
  System-wide rename is out of scope here; code uses the token, screen text says co-op.
- Q1's exercise keeps R and F in the Exercise_F26 wording (same standing question as A1's B14
  about which orientation the exercises should practice).
- Label placements were fixed against rendered frames in the v2 pass: the three co-op curve
  names now sit in the empty band left of the y-axis beside their own intercepts, the
  `Gains From Specialization` label sits under the graph, and both axis captions hang off the
  *ends* of their axes so they never land on a tick numeral. **[check]** whether the director
  prefers the curve names back inside the plot area now that the crossings are understood.
- The v3 pass added a `Deferred` bullet to `_Style_Guide.md` §9: **question-list / numbered-list
  slide styling needs its own design pass** (voice sans vs. serif, color gold vs. white, layout).
  Interim decision 2026-08-30, applied here: white CMU Serif.
- The autarky panels carry a centred line above them from B15b on (the `Autarky` definition,
  then the B16e hook) *and* a name line under each x-axis, so `panel_kwargs` shrank again to
  `y_length` 4.3 with the panels at `DOWN * 0.30`; the under-axis band sits at y = −3.30 and the
  definition moved off the bottom edge into the subtitle slot. Measured clearances: 0.42 from
  the readout numerals down to the name/rate lines, 0.50 from those lines to the frame edge,
  0.37 from the subtitle line down to the panels' top ticks.
- Both `Self-Trade` labels are now anchored to their own arrow (Molly's by a graph coordinate,
  Andrew's by `next_to(arrow, UR)`), which puts his 0.15 off the arc's outer corner and 0.89
  clear of the `(4, 8)` coordinate label.
- Exercise-card bodies are in the narrator's sans as of this pass (`_Style_Guide.md` §9 trial);
  inline `$R$` / `$F$` stay serif math inside the `\textsf` wrapper, and the wrap measures the
  wrapped Tex so the line breaks match what renders.
- ~~B07 still derives *Andrew's* 1 C = 2 S under the graph…~~ **Resolved in v5**: his derivation
  moved onto the table screen (B08c–B08e), so both farmers' costs are derived in the same spot,
  in the same order, and his entries no longer appear without their own arithmetic. The `or`→`=`
  opening went with it.
- The self-trade readout's live `DecimalNumber`s are still colored by good (`3.0` in `CARROTS`,
  `28.0` in `SPINACH`) rather than INK. They carry no letter, and they are paired with the
  colored exchange bars they measure, so v5's numerals-are-INK rule was read as not reaching
  them. **[check]** whether the director wants them INK too, with the bars carrying the color.
- The autarky panels were **not** re-centred in v5: measured against the new `BODY_MID` band
  (title + centred subtitle above, two under-axis rate lines below) they were already within
  0.1 of centre, and the v4 clearances there were hand-tuned. The tables screen likewise sits
  within ~0.1 of its band centre at full frame.
- `maniml` has no `TracedPath`; the episode carries a local `trail_behind()` polyline helper.
  It is used twice as of v4 (the straight co-op line at B06/B06b and the kinked specialized
  frontier at B11d/B11e), which is a stronger case for promoting it to `_Assets/style.py`.
- `maniml` seeds `scene.mobjects` with the `CameraFrame`, and every `play(camera.frame.animate…)`
  puts one back; `exercise_card()` builds `VGroup(*scene.mobjects)` and rejects non-VMobjects,
  so the scene calls a local `drop_frame()` after every camera play. A cleaner fix belongs in
  `style.exercise_card()`.
