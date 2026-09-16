# ECON 0100 Video Series — Graphite Style Guide (v1, 2026-08-26)

*Preferences consolidated from Taylor's B1/B2 animation session, 2026-09-15.
The current rules below incorporate the later corrections in that session;
dated decisions in §9 preserve the history.*

*Economics from scratch.* One cohesive story in six Parts; the visual system has to
carry continuity across ~30 episodes made over a year, by more than one pair of
hands. This guide is the contract: it settles every choice that recurs, explains
*why* each choice was made (so you can extend it without breaking it), and names
the ones still open.

**How to use this guide**

- **Writing a new episode?** Read §0–§3 once in full (identity, frame, color,
  type — the things you must never improvise), then use §4–§8 as reference while
  you build. Read §8's animator workflow before interpreting or delegating beats.
  `B1_Demand/03_Code.py` and `B2_Supply/03_Code.py` are the current references
  for graph choreography; B2 is the reference for flat, editable code. Use the
  specific prior episode Taylor names when a sequence is to be copied.
- **Porting or fixing old work?** Go straight to §10; it's a checklist.
- **Quick lookup?** Search by role: typography in §3, graph/math and surplus sequences in §4, animation grammar in §6, and the animator workflow in §8.

Taylor's latest explicit instructions take precedence over this guide. Where
this guide and older code disagree, use the current guide, subject to the
faithful-first-pass rule in §8. Import shared colors and styling from
`_Assets/style.py`; keep simple layout, timing, and bar-width constants visible
in `construct()` so Taylor can edit them. Do not change shared assets or other
episodes merely to implement a change scoped to one episode.

The brand system itself lives in the **Graphite repo** (`~/Projects/Graphite`,
sibling to this one): canonical token values in `tokens.json`, the palette
checker (`node tools/check_palette.mjs` after any color change), and the design
documents. The rationale, before/after mockups, and validation evidence are in
the Graphite design document:
https://claude.ai/code/artifact/24060dd6-bb64-4ebb-aa94-e9e81cab29f7
This guide is the *application* of that system to ECON 0100 — animators only
need this file; change token values in Graphite first, then propagate here and
to `style.py`.

---

## 0. The identity

**Graphite is a lecture hall after dark: a graphite ground, Computer Modern
voices, and a small set of named colors that mean the same thing everywhere
they appear.** The system spans three surfaces — the stage (video), the desk
(course sites, notes, exams), and the poster (thumbnails, end-cards) — as one
world seen at three distances.

Five things together make the look ours; no one of them alone does:

1. **The 2:1 stage.** Wider than anyone else's math video, chosen so many cards
   fit side by side.
2. **The title architecture.** Flush-left azure question title, generous
   emptiness below, and a small caption only when it adds needed information.
3. **Words as glyphs.** A colored letter or word *is* the illustration:
   `10 C = 40 S` with C in carrot-orange and S in spinach-green, *Apple* in
   green instead of a drawing of an apple. No icons, no stick figures, no
   clip art — when a drawing is truly needed (a house, tickets), it's an INK
   outline. This is a principle, not a habit: before drawing anything, ask
   whether a colored word does the job.
4. **The raster wordmark.** The pixel-flicker MICROECONOMICS mark. It is the
   brand device beyond the bumper too: favicon, site header, channel avatar,
   end-card, thumbnail badge.
5. **One law for color: every hue on screen is a noun** (§2). Color is never
   decoration.

What this is *not*: the stock manim look. We inherited manim's skeleton, not
its wardrobe — the default palette, pure-yellow highlights, and white axes are
all out of spec.

## 1. Frame and layout

| | Rule |
|---|---|
| Aspect | **2:1**, 2160×1080 (`pixel_width = 2 * pixel_height`). Chosen deliberately: "wide aspect makes it easy to show many cards." Crops cleanly to 16:9 for YouTube thumbnails. |
| FPS | **15 fps** is the preferred animation cadence, including viewer playback. Taylor tried and approved its deliberately stepped, flip-book feel; do not silently restore 30 or 60 fps for final output. In ManimL, B1/B2 set both `default_camera_config = {'fps': 15}` and `self.camera.fps = 15` because the viewer may otherwise override the scene default. |
| Background | `BG #212121` everywhere — the same graphite as the websites (changed from #1f1f1f in v0; imperceptible on screen, meaningful in the system). No white-ground scenes (E2/E3/E4/C2 legacy files are out of spec). |
| Safe area | Use the title's 0.4-unit top and 0.6-unit left margins (§3). Leave space between titles, graph headings, and unit captions; do not crowd tick numerals or quantity readouts. Bottom definitions have their own 0.05-unit bottom margin (§3). |
| Vertical centering | Body content is **vertically centred in the band between the title and the reserved bottom strip** (the strip holds definition lines, math rows, stored results — it is never body). Peer objects on one screen — a card column and a graph, two panels — share **one common vertical centre**, so the screen reads as a single block instead of a stack shoved under the title. In code: name the band once (`BODY_TOP` / `BODY_BOTTOM` / `BODY_MID`) and place every body object against it, rather than hand-tuning a `shift` per object. (Added 2026-08-31 from the A2 director's pass; the co-op screen's farm column and graph were 0.4 apart and both riding high.) |

**Four modes** describe the available stage layouts. They are not separate
storyboard fields; the beat's action makes the layout apparent:

- `cam` — face to camera, full frame. No animation.
- `anim` — animation full frame.
- `split` — animation on the **left**, face on the **right**, both in rounded-corner boxes on a grey ground, video box on black ("the video could be the animation on one side and a face the camera video on the other side").
- `notes` — a principle line or definition as a full-frame card (one sentence, body size). The accumulating side panel was tried and dropped as too cluttered; `style.NotesPanel` remains available if a later episode wants it.

Transitions between modes happen at beat boundaries only. Within a beat the mode is fixed.

**Keep the page clean.** The animation supports the spoken explanation; it does
not transcribe it. Prefer a title, the model, useful on-model labels, and the
current definition. Put price, quantity, and area labels on or beside their
graph features instead of accumulating a sidebar of prose and readouts. Reserve
the right-hand calculation area for actual math. A recap may retain a concise
list of gold terms with white definitions beside the graph; Taylor explicitly
liked that use of text. Remove highlights and annotations that have no teaching
job in the current beat.

## 2. Color

Every color is a **semantic token**. Episodes never name a raw manim color; they
use the token, so a change propagates. Three rules govern the whole palette:

- **Every hue is a noun.** A color appears on screen only because it *means*
  something (demand, Molly, a defined term). Never decorate with color.
- **Azure is reserved for the course's own voice** — titles on stage, links and
  accents on the web, the wordmark. It is never a curve, a fill, or a character.
  (Decided 2026-08-26; this is why demand is teal, not blue-blue.)
- **Marks and text are different jobs.** The six *marks* (§2b) are the persistent
  model colors. `DEFINITION` gold belongs to terms, not curves. `FOCUS` yellow
  may mark temporary measurements such as a triangle's height and base, with
  matching yellow labels and numbers; it is not a persistent curve color.

The values are not eyeballed: they were stepped in OKLCH for the graphite ground
and run through a CVD validator (Machado protan/deutan simulation, OKLab ΔE)
against the sets of colors that actually share a screen. The old manim defaults
fail measurably (supply-orange vs guide-red at ΔE 9.1 where the floor is 15;
purple at chroma 0.096 reads grey; pink↔purple at CVD ΔE 2.5). Where two hues
are confusable under deuteranopia (red/green above all), **lightness carries the
difference** — crimson sits dark, mint sits light, teal sits deep. Full evidence
tables are in the Graphite document. Two documented deviations from dashboard
convention: the mark-lightness ceiling is relaxed to OKLCH L 0.75 (a 4-px curve
on a projected stage needs more luminance than a dashboard bar), and guide-red
sits at 3.2:1 contrast in the original palette validation. The later B1/B2
treatment uses that same red for selected-value labels as well as guides, while
axis names remain white (§4).

### 2a. Ground and voice (text tokens)

| Token | Value | On BG | Use |
|---|---|---|---|
| `BG` | `#212121` | — | the one ground, video and web |
| `INK` | `WHITE` | 16.5:1 | body text, curve labels |
| `MUTED` | `#696969` | 3.0:1 | **geometry only**: axes, ticks, ghosted/"before" curves, DWL |
| `CAPTION` | `#9E9E9E` | 6.0:1 | **muted text**: subtitles, stored results, axis captions. (New in v1 — MUTED at 3.0:1 is below the 4.5:1 text floor and is the first thing YouTube compression eats. If it's words, it's CAPTION; if it's lines, it's MUTED.) |
| `TITLE` | `#4A8FF0` | 5.1:1 | the brand azure. Titles only — see the reservation rule above. (Was #0096FF.) |
| `DEFINITION` | `#E5C044` | 8.9:1 | **only** the defined term inside a definition line, and the episode's question lines. (Was #FFD700 — softened; still unmistakably gold, no longer a highlighter.) |
| `FOCUS` | `#FFE14D` | 13.4:1 | transient attention: wiggles, the optimum dot, the framebox, principle lines in E. The bright step of the same gold family (was pure YELLOW). Never a persistent curve color. |
| `ON_FILL` | `BG` | — | text sitting on a solid token-colored fill (e.g. the farm card) |

**Gold beyond definitions**: supporting *question lines* (*Where did all that
wealth go?*, *20 of the 30 are ports.*) are `DEFINITION` gold at the bottom edge
or under the title — gold marks "the thing to remember on this screen."
Question-shaped page titles remain `TITLE` azure.

**Carry meaning from graph to math.** Price, selected quantity, and MB/MC
readouts are `GUIDE` red, including the corresponding symbols and substituted
numbers in equations. `CS` and its area label use `DEMAND`; `PS` uses `SUPPLY`;
expenditure and cost labels use `GOV` green when those areas are being taught.
Height/base marks, labels, and substituted measurements use `FOCUS` yellow.
Keep neutral operators and surrounding prose white. Do not introduce a new
color for every label. Names can be white or `CAPTION` grey, and unused diagram
regions can remain blank. Avoid a screen where the same hue ambiguously means
both a good and an unrelated curve; do not invent a replacement palette without
settling that choice with Taylor.

### 2b. Marks (the six curve colors)

The only colors allowed to persist on the model. Same token, same meaning, every
Part. The token names keep manim's names (`BLUE`, `ORANGE`, …) so importing
`style.py` shadows manim's constants and even un-ported code drifts toward spec —
but note `BLUE`'s *value* is a deep teal.

| Token | Value | Market (B–E) | Part A | Games | Consumer (F) |
|---|---|---|---|---|---|
| `BLUE` | `#128A9B` (deep teal) | `DEMAND` (also MPB, MSB); CS fill | `MOLLY` | `COL_PLAYER` (them / Player 2) | `GOOD_A` (x-axis), `INDIFFERENCE` (one color for all indifference curves — F1's three-color set is out of spec); optimum dot is `FOCUS` with `MUTED` dashed drop-lines |
| `ORANGE` | `#E2803A` | `SUPPLY` (also MPC, MSC, MC); PS fill | `CARROTS` | — | — |
| `GREEN` | `#34B57A` | `GOV` (tax revenue / subsidy cost / "expenditure") | `SPINACH` | `EFFICIENT` cell box | `GOOD_B` (y-axis) |
| `RED` | `#C63944` | `GUIDE`: dashed P\*/Q\* lines, equilibrium dot, readouts. One accent, always red. | `ANDREW` | `NASH` cell box | `INCOME`, `BUDGET` |
| `PURPLE` | `#A99CF2` | `TOTAL` (total surplus as one region) | `CO_OP` (renamed from `GUILD` 2026-09-02 with the prose; `GUILD` stays in `style.py` as a deprecated alias until pre-rename episode code migrates) | — | — |
| `PINK` | `#C95AC0` | `EXT` (the externality wedge) | `TRADE` (exchange lines, post-trade bundles, gains regions) | `ROW_PLAYER` (you / Player 1) | — |

Why demand is teal and not blue-blue: azure is reserved for the voice, and the
teal separates from the azure title at ΔE 12.7 under CVD simulation with an
obvious hue difference — while validating *better* against the other marks than
an azure demand did. It also keeps the cool-vs-warm demand/supply opposition
students know from textbooks. Demand is deliberately the quietest mark (3.9:1) —
it is on screen more than anything else.

### 2c. Fills and derived colors

| Token | Recipe |
|---|---|
| `CS` | `DEMAND` @ fill opacity 0.35 — consumer surplus inherits demand's color |
| `PS` | `SUPPLY` @ 0.35 |
| `TOTAL` fill | `PURPLE` @ 0.35 |
| `DWL` | `MUTED` @ 0.5 — deadweight loss is always grey |
| `GOV` fill | `GREEN` @ 0.35 |
| `POLICY` | same color as the curve, **dashed** — a taxed/shifted curve is the same token, dashed |
| PPF regions | attainable set takes the **owner's** color @ fill opacity; what's lost is ghosted `MUTED`; what's gained is `TRADE` (`ATTAINABLE` / `LOST` / `GAINED` in style.py) |
| Solid cards | a solid party card may use the owner's token and `ON_FILL` text. An allocation diagram uses an `INK` outline, colors only the relevant allocation, and leaves unused space blank; its neutral name need not take the party color. |
| Best-response box | the player's own color; Nash cell `RED` box; efficient cell `GREEN` box; **same size** boxes |
| Number-line roles | color on a number line means a *role*: `EFFICIENT` green = chosen/benefit, `NASH` red = given up/cost (`set_color_of`) |

## 3. Typography

**Everything is LaTeX.** `Tex` for everything on screen; `MathTex` only for
display equations; `Text` never (font mismatch). Both of the stage's voices
come out of the Tex pipeline.

**CMU Serif is the default for teaching content**: titles, definitions, model
labels, calculations, recap descriptions, and the entire exercise card. Use one
consistent face across the graph and its math. Taylor rejected broad sans-serif
explanatory text as cluttered, then explicitly approved **small CMU Sans axis-unit
captions**, such as “dollars per ton” and “tons per year.” Keep those captions clear
of titles, tick numerals, and moving readouts. This narrows the older blanket
“narrator prose is sans” rule. Existing helpers may still apply `NARRATOR_SANS`;
their default is not a reason to restyle approved serif content.

**Source Sans stays web-only.** The sites pair CMU Serif headings with Source
Sans 3 body; the stage's sans is CMU Sans and only CMU Sans — same pipeline,
matching metrics.

- Sizes by role, not ad-hoc scale: **episode head** 1.5 · **title** 1.2 · **body** 1.0 · **caption** 0.8 · **tick numbers** 0.7 · **part card** 3.0. Nothing below 0.7 — CMU's thin hairlines shimmer under projection and YouTube compression at small sizes; the scale floor and the 2160×1080 render are the defense.
- **Page titles** (`style.title`): `TITLE` azure, **flush left**, small top margin (buff 0.4, left 0.6). Every screen has one; figures don't get their own title — units go in a `CAPTION` **axis caption** beside the axis (`axis_caption`), e.g. title *Unemployment*, caption *rate (%)*.
- **Titles ask the question being answered**, rather than naming the topic: “Which bars are worth buying?” or “How much do these exchanges benefit buyers?” Give the question a concrete subject; avoid an unclear “this.” Keep the question through the beats that answer it. “Last time…” and production cards may keep their established labels.
- **Subtitles** (a question, a stored result): `CAPTION`, caption scale, stacked under the title and left-aligned with it (*What can a dollar get?*; the bakery's `OC(pie) = cake` lines).
- Lists: `VGroup(...).arrange(DOWN, buff=0.4, aligned_edge=LEFT)` under the title, left-aligned with it; never `to_edge(vector)` hacks. Rows that would overflow are scaled to fit the frame width, not wrapped.
- Multi-clause statements (the *Microeconomics tells us…* card): one clause per line, **no bullets**, key phrases in `DEFINITION` gold; a clause that must break continues on an **indented** second line (`\quad`). Use CMU Serif and only the wording needed for the beat.
- **Text entry and replacement**: prefer `FadeIn` for new text. When a title, definition, or explanatory line is replaced in the same position, remove the old text first, then fade the new text in; never superimpose the outgoing and incoming words. This is the B2 treatment Taylor approved on 2026-09-15. Keep tracker-driven numeric rolls and purposeful graph-to-math number transfers. `AddTextWordByWord` is reserved for the bumper label.
- Definitions: one line, `{{Term}}` isolated and colored `DEFINITION` gold, rest in `INK` white. **All bottom definitions use one fixed text size**, including short definitions: match B2 beat 2.b's Individual Quantity Supplied line, `Tex(...).scale(0.7443)` at the default 48-point size (about 35.73 points). Center each bottom definition horizontally with `set_x(0)` and keep a tiny 0.05-unit bottom margin. Do not enlarge short lines or fit each sentence to a different size; if a future definition is too long for the 14.8-unit safe width, reflow it at the same size. This supersedes the earlier per-line shrink-to-fit and left-alignment rules (approved 2026-09-15). Full-frame definition cards retain their own body-size treatment. Term appears in the script first ("definitions without definition"), the card comes after.
- Principle lines (*Preferences are rankings.*) are full-frame cards: one sentence, body size, `FadeIn`.
- **Exercise cards**: CMU Serif throughout, gold heading aligned left inside the box, white body slightly indented relative to that heading. Leave balanced internal padding and enough line spacing. B2 uses 0.65 units from the panel's left edge for the heading and another 0.35 for the body. Keep the card to the exercise prompt; avoid extra explanatory sentences that belong in the narration.
- Preference chains read **less-preferred on the left**: `Chocolate Cake ≺ Carrot Cake`, so they dissolve onto a number line without reordering.

## 4. Axes and graphs

- One factory: `axes(x_range, y_range, x_length=10, y_length=5)` → `MUTED` axes, `tips=False`, no ticks by default; tick numbers only when values matter for the argument.
- **Tick numerals are always `MUTED` — never colored by good.** When the goods need their colors on a graph, the **axis captions** carry them (*Carrots* in `CARROTS` orange on x, *Spinach* in `SPINACH` green on y) — the words-as-glyphs principle doing that work. (A1's colored numerals are out of spec.)
- Orientation invariants: **P vertical, Q horizontal** (B–E). **Carrots horizontal, spinach vertical** (A — as rendered in A1; reconcile `Video.py` if it disagrees). **Good A horizontal, good B vertical** (F). Wage vertical, labor horizontal (F2 — decide once).
- **Axis-label positioning is the same across all graphs: vertical label LEFT of its axis, horizontal label BELOW its axis.** For P, use `next_to(ax.c2p(0,y_max), LEFT, buff=.25)`; for Q, use `next_to(ax.c2p(x_max,0), DOWN, buff=.35)`, replacing zero with the corresponding axis-origin coordinate when nonzero. Axis names are plain white `P` and `Q`; red `Q_d`/`Q_s` identify selected quantities, not the axis itself. Unit captions may sit beside those names; keep them clear of ticks, titles, and readouts.
- **Graph beside calculations**: use a subtle grey vertical divider, centered vertically and tall enough to cover the graph and its horizontal labels (B2 uses six units). Put it to the right of the entire horizontal-label group, including units such as “tons per year,” with a 0.35-unit gap. Center the math block in the remaining space between divider and right safe margin; multi-step algebra may remain left-aligned internally. Fade the divider in and out with the calculation sequence. (Approved 2026-09-15.)
- Curves: `axes.plot` for functions; **polyline (`set_points_as_corners`) inside `always_redraw`** for anything driven by a tracker or data — never `Transform` between two rebuilt plots (the wobble).
- Labels ride the curve end: short (`D`, `S`, `MC`, `ATC`, `MPB`), `INK`, `next_to` the right end. In C–E demand is relabeled `MPB` and supply `MPC` once externalities enter, and stays relabeled. (These labels are also the palette's safety net — every curve is identified by text, never by color alone.)
- Put the standing curve equation above the curve in open graph space. Use the separate math area for the worked substitution, not for a second unrelated text stack.
- Areas use the token's fill opacity. Explicit `Polygon` slices are appropriate for the editable, bar-by-bar sequences below; use axis coordinates for every boundary so bars and curves align.
- Equilibrium: `GUIDE` dot + two dashed `GUIDE` drop-lines (`get_horizontal_line` / `get_vertical_line`, `dashed_ratio 0.85`, opacity 0.3 for the lines, 1.0 for the dot). Star the labels: `P^*`, `Q^*`.
- Selected-quantity readouts use `Q_d` for demand and `Q_s` for supply, never the generic word “Quantity,” in `GUIDE` red. Keep the symbol and its chosen, unknown, or solved value red on the graph and in the calculation; carry that color through any number moving between them.
- Say **excess**, never "surplus," for Qs > Qd.
- **Keep guides and annotations above fills.** Red price/quantity lines must remain visible over bars and areas; dots sit above the guides. Yellow height/base measurements and labels such as `MC=P` also stay in front and clear of the curve. Verify the rendered stacking across plays, not just object creation order.
- **Full-bleed images** (the Black Marble): `set_height(FRAME_HEIGHT * 1.02)` so no background shows; any title over an image gets a `BackgroundRectangle` in `BG` @ 0.7.

### Reading a graph and doing the math

1. Choose and label the input in red on its axis. Follow the notes' price order
   and observed answers; do not replace the scripted elicitation with invented
   class data or a different demonstration.
2. For a price input, fade in the horizontal dashed guide out to the point,
   then extend the vertical dashed guide down to quantity. Reveal the quantity
   label after that trace. Reverse the direction when quantity is the input.
3. In a worked calculation, keep the output unknown (`?` is useful) until the
   algebra produces it. Do not reveal the answer in a label or an obvious tick
   numeral early. This does not prevent showing an observed answer when the
   notes are simply collecting data.
4. Carry a copy of the red input into the side calculation, reveal the algebra
   in steps, and carry the resulting number back to its axis. Leave both dashed
   guides and the dot visible throughout the transfer.
5. When the input changes, roll a `ValueTracker` and keep the dot, both guides,
   and readouts attached. Do not replace the tracker readout with a transform
   between separate price labels.

Introduce the Marginal Benefit/Marginal Cost definition before the arithmetic
that uses it. Motivate the idea with a simple first quantity before a later one;
do not add duplicate walkthroughs that the notes have cut. Keep individual and
market graph-to-math sequences consistent in motion, colors, label positions,
and product/units. Additional unit captions need a teaching purpose, not just
available space.

### Quantities, decisions, and surplus areas

- **Keep possible quantities visible.** Use very transparent grey bars across
  most or all of the relevant curve, so students can track the many possible
  decisions as price changes. An unchosen bar stays grey instead of disappearing.
- **Use narrow but visible slices consistently.** The approved B2 reference is
  `SLICE_WIDTH = 0.1` at its individual-graph scale, with grey fill opacity 0.10.
  One width setting governs resting bars, colored bars, recap, and closing
  graphs. On different quantity scales, preserve the visual narrowness and make
  units explicit; the 0.1 value is not a universal economic unit.
- **Align bars to the model.** Build them from axis coordinates. A sampled
  rectangular demand bar's chosen top corner lies on the curve, rather than
  placing the middle of its top on the line. State the sampling convention in
  the storyboard and keep the arithmetic consistent with it. For exact sloping
  slices, follow the curve along the top/bottom boundary; do not substitute an
  endpoint height for the total area of an interval.
- **Preserve the object when focusing.** For a B1-style isolated-unit close-up,
  fade the other bars and curve away while leaving that grey bar in place.
  Reveal the expenditure/cost component separately, then the surplus component. In B1's
  close-up, Price is red to the left of the vertical axis, the expenditure name
  sits to the right of the bar, and its number sits inside the area. Keep labels
  with the regions they explain as price changes. A supply-cost explanation may
  need the sloping curve to remain visible, as in B2; follow the approved beat.
- **Show the decision through price motion when the notes call for it.** Use
  several instructive prices. For a buyer whose price rises above MB, keep the
  rejected bar grey and hide exchange-specific CS/expenditure labels. When an
  exchange becomes worthwhile again, its components can reappear together;
  do not force a repeated introductory reveal. Restore the other grey bars and
  the curve between unit close-ups, then focus on the next surviving bar.
- **Show the region before naming its gain.** On the first surplus reveal, fade
  in the area before its definition and numerical result. Do not replace this
  visual explanation with bookkeeping text in a sidebar.
- **Finish each bar before moving on.** After the first illustrated interval,
  reveal cost/expenditure for the next bar, then that bar's PS/CS, then repeat
  for the following bar, left to right. Do not fill every cost bar and then make
  a second pass over every surplus bar. Follow the notes when a different
  accumulation is specifically intended.
- **A group of thin bars may still represent one unit.** Use a small neutral
  brace and label, such as “1 ton,” when needed to make that interval clear.
  Keep it through the interval's revenue/cost/surplus explanation, then remove
  it when expanding to the full quantity. This supersedes the earlier request
  to remove that useful brace; it does not reinstate decorative yellow marks.
- **Explain the approach to an area.** When converting sampled rectangles into
  a smooth CS triangle, repeatedly split each bar in half, then fade the fine
  bars into the triangle and expenditure rectangle. Avoid a direct shape morph
  that conceals the sum. Exact sloping slices, as in B2, already tile the area
  and need no artificial approximation step.
- **Keep the equation continuous.** Introduce the area formula once. Label its
  height and base in yellow, carry copies of the yellow numbers into the existing
  formula, and retain its prefix rather than fading it out and recreating it.
  Color `Area`/`CS`/`PS` to match the region being measured.
- **Use grey for supporting areas when only surplus is the subject.** In recap
  or preview graphs, show colored CS/PS with faint grey expenditure/cost beneath;
  do not give those supporting areas competing emphasis. Color and label them
  when they become the lesson's subject.

### Adding individuals and previewing the market

- Show aggregation as addition of individuals' quantities at the same price.
  Use a common price scale, aligned guides, and enough space below the title.
- Put the addition at the resulting quantity's position on the market graph.
  For a simple sum, pause on `2+1`, then combine it into the quantity there;
  do not insert a separate `2+1=?` arithmetic exercise.
- Introduce the market demand/supply definition before the exercise that uses
  it. Preserve the familiar individual-graph layout and movement patterns.
- When the closer asks where price comes from, the approved device is demand
  and supply side by side, a shared price moving up and down a little, attached
  guides and quantity labels, and a restrained “Next time…” cue. The CS/PS bars
  respond to price, with grey supporting areas. Use this when the notes call
  for that preview; it is not a mandatory ending for every episode.
- Possible 3D aggregation and simulation previews remained ideas to develop,
  not a settled replacement for the approved 2D choreography. Propose them
  separately and get direction before making that change.

### The number line (Episode A0's recurring object; `ValueLine` in `A/A0_Welcome/03_Code.py`)

- Horizontal, `MUTED`, higher = further **right**. Items are `GUIDE`-red dots with a `Tex` label; labels alternate above/below (`stagger`) so neighbors don't collide; below-side labels sit under the tick numbers.
- Every item position is a `ValueTracker`; the marks are `always_redraw`. Consequences: position the line by the **line's** center (`ValueLine.move_to` does), `freeze()` before fading a line so it leaves as one object, `raise_marks()` after adding so dots sit on the line.
- Tick numbers only where they carry the argument: **1, 5, 10** (→ 100, 500, 1000 for the ×100 beat). Relabel the ticks; nothing moves.
- Items **fade in in place** (no slide-ins) unless the motion *is* the point (a preference change, chocolate climbing). Those moves are one eased play (`rate_func=smooth`, ~2 s).
- Switching what's ranked: the old group fades **out fully**, then the new group fades in with its own positions.
- Read line: dashed `GUIDE` vertical from an item to a live `DecimalNumber` — the Part B price-line idiom (`reader`, `max_reader`).
- Next-best arrows: `GUIDE`, curved, always **below** the line, **one at a time**; each result is stored as a `CAPTION` subtitle line before the next arrow.
- Color on a number line means a *role*: `EFFICIENT` = chosen/benefit, `NASH` = given up/cost (`set_color_of`).

## 5. Model invariants (what must look the same every time)

**Utility lines are ordinal.** On a number line of utility/benefit, value is a *position* and comparison is the *gap* between two positions — never a length from zero (there is no zero; the ×100 beat says so). Benefit = where the chosen thing sits; cost = where the next best sits; the decision rule is the gap's sign ("A beats B"). Lengths from zero, braces with numbers, areas: only once money is on the axis (dollars have a zero and units). Decided 2026-08-22 for Episode 0 B29–B32; carries into consumer surplus (WTP − price is the same gap on a dollar line).

| Model | Fixed by convention |
|---|---|
| PPF | straight lines until a bowed PPF is deliberately introduced; character colors; `Video.py` functions on the canonical set (`PPF_Molly(c) = 40 − 4c`, `PPF_Andrew(c) = 16 − 2c`, `PPF_Coop(c) = 56 − 28c/9`; carrots horizontal, each PPF plots as S(C)) are the numbers of record — updated 2026-09-02 from the pre-flip spinach-first trio |
| S&D (spinach) | `S: P = 2Q/5`, `D: P = 8 − Q/5`, `Q* = 40/3`, `P* = 16/3`; Q in thousands of lb/month |
| S&D (generic, C) | `D: P = 10 − Q/10`, `S: P = 2 + Q/10`, eq (40, 6), axes 0–100 × 0–10 |
| Tax | wedge is a vertical segment parked **left of the axes**, slid in from the left until it "gets stuck between the curves"; `p_B` label above-left, `p_S` below-left; incidence stacked off-axis, buyer share `DEMAND`, seller share `SUPPLY` |
| Externality | built at **one quantity first** (MPC segment, EXT on top, label MSC), then swept |
| Costs | production function **left**, cost graph **right**; FC first as a horizontal line; MC through the minima of ATC and AVC with `FOCUS` dots |
| Monopoly | four curves `MC ATC MPB MR`, each readout dashed in its own curve's color; MR ends at half MPB's Q-extent; profit box `Q × (P − ATC)` |
| Payoff matrix | `Table`, row player first in each cell; walk **column headers, then row headers**, then cells in VO order |
| Consumer | tangency shown as the ratchet (nudge point → bump curve → repeat) |

## 6. Animation grammar

- **One continuous motion = one `play`.** Drive it with a `ValueTracker`; never loop short plays (each eases in/out → stutter).
- **Eased by default.** Sweeps, data draws and item moves use `rate_func=smooth` (ease in and out); `linear` only when a constant rate is itself the message.
- **Prefer fades to the default drawn-on look.** Text, boxes, fills, and usually curves enter with `FadeIn`. Use a growing guide or a drawn line only when its direction or construction is part of the explanation, as in tracing a point down to quantity. Preserve specific approved choreography instead of making a blanket animation substitution.
- **Change only the text that changes.** Keep unchanged context in place. Replacement prose drops out before the new text fades in (§3); numbers that change continuously roll on trackers. Keep deliberate number transfers and algebra substitutions when the motion explains the math. Avoid whole-line morphs for replacement prose. Updated 2026-09-15 from the B2 review.
- **Numbers are stable; when they change, they roll.** An on-screen number never changes without a pedagogical reason, and when it must, it moves as a visible tracker roll (decimals rolling, points riding) — never a swap or teleport. Changing numbers cost trust; rolling numbers *are* the content. Settled 2026-09-02 (A3's one-tracker negotiation).
- **One tracker, one source of truth.** Every representation of the same quantity — dot, dashed drops, coordinate label, caption decimals — binds to a single `ValueTracker`. Nothing can drift out of sync mid-roll; wonk becomes structurally impossible instead of hand-fixed.
- **Reveal the result after its reasoning.** Keep existing formula prefixes and context, reveal the necessary steps, and move a copy of the result back to the model when useful. Write those plays directly in `construct()` rather than hiding them in derivation machinery.
- Timing follows the teaching beat and the approved animation. Use explicit `self.pause('beat.id')` for class holds; do not replace interactive holds with timed waits. Shared bumper helpers may retain their own internal flicker timing. Several discrete bars can use short sequential plays; do not turn one continuous tracker motion into many separately eased steps.
- Vocabulary → animation:
  | storyboard verb | manim |
  |---|---|
  | Show (card/text/object) | `FadeIn`; old replacement text is removed first |
  | Trace (geometry) | grow or draw the specific guide when direction matters; otherwise `FadeIn` |
  | Add (to existing group) | `FadeIn` + `arrange` / `Transform` of the group |
  | Continue | extend the tracker |
  | Wiggle | `Indicate`-style scale pulse in `FOCUS`, 0.5 s |
  | Highlight | `SurroundingRectangle(buff=0.3)` in the relevant token, or area fill |
  | Circle | `Circle` around a cell/label (`circle_it`) |
  | Zoom / Pan | `MovingCameraScene` frame animate, smooth, 2 s |
  | Sweep | tracker from one end to the other, eased |
- Use highlight boxes, yellow marks, or extra explanatory text only when they do a specific job in the notes. A useful unit brace or area measurement is distinct from a decorative highlight.
- Dim the previous stage for a definition or exercise overlay when context helps; remove unrelated remnants when the card is intended to stand alone.
- Remove obsolete annotations before replacing their explanation. A useful unit brace can coexist with the bottom definition for that same unit (§4).
- **maniml-specific tools** (all fine in render and export):
  - `self.pause(name)` — the beat boundary (§8); `loop=True` for a hold that keeps replaying in the viewer.
  - `self.add_sound(path, time_offset=0, gain=None)` — works in the viewer (plays through the system player when a live audience is connected; `time_offset`/`gain` shape only the rendered mix) and in the render (mixed into the mp4). Sound cues are beat-level: put the `add_sound` right after the beat's `pause`, and name files by beat in `00_Assets/sound/` (`0.a_bumper.wav`).
  - `FlickerIn(mob, flickers=4, seed=0, lag_ratio=0)` — switches a mobject on like an old tube light: dark, a few irregular sputters, then lit. Works on anything `FadeIn` does; `lag_ratio` staggers the sputters across submobjects. Use it sparingly — for a *reveal with attitude* (a title that "comes on", the bumper), not as a default entrance. Never for body text or bottom definitions, which fade in (§3).

## 7. Recurring cards and devices

| Device | Spec |
|---|---|
| Episode bumper | reuse `bumper_raster`, `flicker`, and `bumper_title` from `style.py`, as in B1/B2; keep the episode thesis and pause explicit. The shared bumper is the approved exception to flat choreography. Raster `MICROECONOMICS`, label beneath, part azure and episode caption-grey. |
| Episode subtitle | the italic thesis line from the notes header (`*More might be possible!*`) appears under the bumper; every episode has one |
| Section title | the concrete question being answered, in the normal azure title style, persists across the relevant beats (§3) |
| Last time… | reuse the specified prior animation literally when requested; preserve its objects, framing, wording, and pause placement. A concise graph-side list of gold terms with white definitions is also approved, as in B2. Do not invent a replacement recap dataset or layout. |
| Next time… | a restrained cue on the relevant live model when useful; the B2 demand/supply price preview is the reference (§4). Add no automatic text stack or framebox. |
| Definition card | bottom definition is the normal on-model treatment (§3). Use a full-frame definition screen only when the notes/approved sequence calls for it; fade it in and restore the model to its prior state. |
| Tracked point | a dot and dashed guides driven by one tracker; readouts sit at the relevant axes, with values withheld until solved in a worked example (§4) |
| Principle line | §3 |
| Six-parts card | six rows, each built in three fades: `Part X.` in `CAPTION` → part name in `DEFINITION` gold → subtitle in `INK`; labels are the `_Parts.md` headings; rows scale to fit the frame width |
| Choice boxes (`choice_boxes`) | `EFFICIENT` green = chosen, `NASH` red = given up; **same size** for both; fade in green then red; swapping a choice moves the boxes |
| Stored results | a running list of results (`OC(pie) = cake`) lives under the title in `CAPTION`, one line per result, added as each is found. They're equations, so they stay serif: `subtitle(..., book=True)` (§3's carve-out) |
| Simple glyphs | words-as-glyphs (§0): prefer **colored text** to a drawing (*Apple* green, *Banana* yellow — a good's own color is its noun); draw only when the object itself matters, then `INK` outlines (house, tickets). No food glyphs, no stick figures. |
| Welfare labels | prefer labels on or beside the graph areas, with math labels in matching colors. Use a separate legend only when it helps the beat; no default accumulating sidebar. |
| Assumptions checklist | a card listing model conditions (competitive firm: many sellers, many buyers, homogeneous good…), items lit as stated — needed in B0, E1, E2 |
| Taxonomy 2×2 | one grid object reused as a map: goods (rival × excludable) in D, market structures (sellers × differentiation) in E, current cell highlighted |
| Allocation diagrams | neutral name and outline, relevant region colored, unused area blank. The region's label follows its center as the allocation changes (§2c). |

## 8. Storyboard and code conventions

- **The notes are the instructions.** Read the current `01_Notes.md` (or the episode's existing notes filename), including its quoted beat directions and editorial cuts. Taylor uses Markdown **quote blocks** for animation directions; ordinary emphasized terms in prose are not stage directions. Preserve that format. Older templates describe linked beats; retain existing links where present, but do not insert them, convert quote blocks, or rewrite notes merely to conform to an older template. The notes belong to the author, who may be editing them while animation work proceeds.
- Storyboard = Markdown beat sheet: one heading per stable dotted ID followed by its concrete, ordered actions, for example `## 3.f · Read marginal cost`. Preserve the teaching order from the notes, not lexical ID order. Keep exact on-screen wording, math, positioning, reveal order, and final visible state explicit enough to implement without a second interpretation. Brief shared layout conventions can sit at the top, as in B2; do not bury the beat actions in metadata or a large table.
- Production-only intro beats use `0.a`, `0.b`, and so on in storyboard and code. They do not appear in `01_Notes.md`. Student-facing beats begin at `1.*`; storyboard and code share the exact dotted ID and follow the notes' order. Where notes already contain beat links, preserve the matching IDs without requiring IDs to be added to quote-block directions.
- **Flat and linear code is a user-editing requirement.** Use one `class EpisodeXN(Scene)` and one `construct()` that can be read top to bottom to see what changes on screen. Object construction, placement, plays, and pauses belong there. Use plain named variables, a few visible constants, and straightforward loops for repeated bars. Avoid new per-beat methods, custom choreography helpers, nested helper functions, framework classes, or layers of callbacks that make Taylor jump around to edit a scene. Small inline updater lambdas are appropriate for objects tied to a `ValueTracker`; keep the relationship easy to see. This supersedes the earlier allowance for helper closures and custom choreography classes.
- **The intro bumper is the explicit reuse exception.** Call the shared `bumper_raster`, `flicker`, and `bumper_title` helpers instead of copying the raster alphabet and flicker implementation into each episode. Keep the episode's thesis and named pause visible in `construct()`. Shared style tokens and simple object factories such as `title()` and `axes()` remain appropriate; they do not hide a sequence of teaching actions.
- Each beat starts with its dotted-ID comment, such as `# ---- 3.f`, and a stopped beat uses **`self.pause('3.f')`**. Preserve stable IDs and the approved pause placement. ManimL recognizes the literal `self.pause(` in the episode file; helper calls must not hide these boundaries. `self.pause(name, loop=True)` is available for an intentionally repeating live hold. Keep imports from `_Assets` through the existing `sys.path` line and the header `# maniml 03_Code.py EpisodeXN`.
- No triple-quoted section markers inside functions (they broke 11 files); use dotted-ID comments such as `# ---- 3.f`.
- `_Assets/style.py` supplies the shared palette, styling, and bumper helpers. Existing older helpers are available, not instructions to use them. Follow the current 15 fps and layout rules even if a shared legacy default differs; do not refactor shared code outside the authorized edit scope.

### Animator workflow and division of labor

1. **The lead animator reads and understands the source.** Personally read the
   latest notes and the relevant prior animations before planning or delegating.
   Understand the economics, the narrative sequence, and the visual purpose of
   each beat. Do not ask Taylor to restate instructions already in the script.
   Ask a focused question when a real ambiguity remains after that reading.
2. **Start with fidelity.** For a port/cleanup, first make the original animation
   run in ManimL while staying as close to its choreography as possible. Preserve
   the work Taylor has already refined. Mechanical compatibility fixes are not
   an invitation to redesign. Propose changes or cuts when components clearly
   no longer fit the notes, and ask before making unapproved choreography/content
   changes. An explicit requested change is already authorized.
3. **Reuse approved sequences accurately.** If Taylor says to copy a review from
   an earlier block, copy that sequence, including framing and timing, rather
   than inventing an approximation. When supply mirrors demand, carry forward
   its visual and motion conventions while adapting the economic meaning.
4. **Write the storyboard before building new beats.** Turn the notes into a
   concrete implementation plan: entering objects, axis ranges, labels and
   colors, values/units, tracker behavior, exact reveal and removal order,
   pauses, and the state left for the next beat. Work out the arithmetic and
   layout here. Keep a record of which existing components are preserved and
   identify proposed cuts rather than silently omitting them.
5. **Delegate implementation, not interpretation.** Taylor's preferred division
   is lead animator for understanding, storyboard, orchestration, and review;
   Opus subagents for implementation when available. Give each delegated beat
   sufficiently precise instructions that the worker need not invent teaching
   content, choose a new layout, or guess the script's intent. State allowed
   files and the flat-code convention. Be candid if the preferred worker is
   unavailable; do not claim to have used it. The lead integrates the result and
   checks it against the notes rather than accepting a worker's “PASS” report.
6. **Respect live authoring and edit scope.** During animation work, edit only
   the authorized storyboard/code files. Do not rewrite notes, exercises, or
   other blocks without authorization. Re-read notes before implementing or
   validating affected beats if Taylor is editing them, and reconcile current
   cuts. An uncertain editorial mark warrants a specific question, not an
   invented resolution. Numerical examples may be simplified when Taylor has
   allowed it, but all equations, units, areas, and visible totals must agree;
   that permission is not blanket permission to edit prose.
7. **Review the actual visuals.** Check representative stopped frames and the
   motion that matters: tracker rolls, guide persistence, reveal order, label
   placement, and stacking. Keep mathematical and visual verification distinct.
   For a small requested update, use a targeted check and let Taylor review in
   the viewer; do not repeatedly launch full renders or widen the redesign.
   Keep progress updates concise and surface genuine issues while there is time
   to correct them.
8. **Deliver locally.** Leave the changes ready for Taylor to review and push.
   Never push to GitHub or publish repository changes through another tool or
   delegated worker. Include this restriction in any implementation handoff.

## 9. Decisions

### Current preferences from the B1/B2 session (2026-09-15)

The rules in §§1–8 above are the consolidated record. They cover the first
faithful port, author-owned notes and quote-block directions, lead/Opus division
of labor, flat editable code with the bumper exception, 15 fps, question titles,
sparse serif teaching content, white axes/red readouts, sequential graph-to-math
reveals, persistent grey quantities, narrow slices, per-bar cost then surplus,
measurement colors, recap reuse, exercise layout, and the graph/math divider.

Later choices settle these earlier alternatives: **bottom definitions are
centered**, not left-aligned; **small sans-serif unit captions are welcome**,
not broad sans-serif explanatory text; **a useful one-unit brace stays**, not
decorative highlights; **each bar's cost is followed by its surplus**, not two
whole-graph passes. Bottom text keeps the approved fixed size even when short.
Episode-specific cuts, example prices, goods, and numbers are not universal
style requirements. 3D and additional simulation sequences remain proposals.
The concern about supply and carrots sharing orange did not settle a new supply
color; retain the semantic palette and avoid ambiguous co-occurring uses.

The older decisions below are historical where superseded by those rules.

Settled 2026-08-21:

- **Supply color = ORANGE.** Yellow-family is reserved for `FOCUS`/`DEFINITION`.
- **Notes panel: tried and removed** — built as `style.NotesPanel` and run through Episode 0; too cluttered. Current bottom definitions and on-model labels are specified in §§1–4; full-frame cards are optional when the beat needs them.
- **Axes = `MUTED` grey** (as in `A/A0_Welcome`); the white axes in A–D code are out of spec.
- **Episode numbering**: in flux while Part A is reorganized; leave headers as they are and reconcile to `_Specs.md` codes later.
- **Intro motif**: the raster wordmark (built, in use).
- **`split` layout: animation LEFT, face RIGHT.** Keep it for eyeline continuity.

Settled 2026-08-22:

- **Utility lines are ordinal** (§5); **no per-beat methods** (§8).

Settled 2026-08-25/26 (the Graphite pass — see the design document for evidence):

- **Palette re-stepped for CVD safety and brand unification.** The six marks and the text tokens of §2 replace the manim defaults; validated against the co-occurring on-screen sets, not eyeballed.
- **Azure is reserved for the course's voice.** Titles, links, wordmark — never a curve. Demand is deep teal `#128A9B`, which separates from the title at ΔE 12.7 under CVD and validates better against the other marks than an azure demand did.
- **Definition gold is a text token, never a curve.** The later B1/B2 measurement idiom permits temporary `FOCUS` yellow height/base marks (§2).
- **`CAPTION #9E9E9E` splits from `MUTED #696969`.** Words vs lines. Muted *text* was at 3.0:1 — below the accessibility floor and fragile under compression.
- **`BG` = `#212121` everywhere**, unified with the websites.
- **Historical Narrator rule**: the August pass applied CMU Sans to general narrator prose through `NARRATOR_SANS`. The B1/B2 review supersedes that default with serif teaching content and small sans-serif unit captions (§3). Any stage sans remains CMU Sans, never Source Sans.
- **Tick numerals never take good colors; axis captions do.**
- **One system, three surfaces**: the same tokens back `style.py` and `course.css`; thumbnails are stage frames with the raster mark; the raster mark is the channel identity.

Settled 2026-09-02 (the A3 render passes):

- **The screen carries only what the current beat needs.** Benchmarks and reference marks (autarky ghosts, standing rates) enter for the beat that uses them and leave after; a mark with no job in the current beat is clutter. The A3 autarky markers exist for one beat — the better-in-both-goods comparison — and nowhere else.
- **Abstractions are earned: one concrete instance first.** Every device arrives as a specific instance with real numbers (one trade, one proposal, one point) before any general object; the general object appears only when a beat *needs* it, and defers to a later episode if none does. A3's trade line was cut on exactly this test — the re-entry principle ("the exchange rate maps out a line") is parked in its notes for Part B, where the price line earns it. This is the phenomenon-first christening pattern (PPF, comparative advantage, Pareto improvement) stated as a staging rule.
- The tracker and continuity rules date from these passes; §6 now incorporates the later B1/B2 preferences for fades and directly written calculation sequences.

Deferred (not needed until Part B/C):

- **Avatars** — social planner (C3), seller with a question (E1), buyer summation (B1). **No stick figures.** Direction: very simple and stylized, undecided — the words-as-glyphs principle suggests a colored initial in a circle, which the placeholder already is. Placeholder until then: a labelled `Circle` in the party's token color (`DEMAND` buyer, `SUPPLY` seller, `INK` planner) with a one-word `Tex` label beneath; speech as a `Tex` line in a `SurroundingRectangle`. Swap for the real glyph later — one helper, one place.
- **Unspecified diagrams**: game tree (D4), Edgeworth-in-PPF, the four-quadrant Map, labor market/monopsony, two-country trade panels, timeline-S&D hybrid (C2). Each needs one sketch before its block is storyboarded.
- **Split-mode chrome** design (and whether it ever needs CMU Sans).
- **Question-list / numbered-list slides** may still need a dedicated layout pass; retain the approved serif treatment. Exercise cards are now settled by the B1/B2 session: serif gold heading, serif white body, heading aligned left with the body slightly indented (§3).

## 10. Porting old work

Begin with §8's faithful-first-pass workflow. Make the requested episode run
before expanding its storyboard, preserve approved choreography, and distinguish
mechanical repairs from proposed teaching changes. Audit shared assets as needed,
but change them only within the authorized scope.

**Shared-asset audit** (only edit these when authorized):

1. Palette block → §2 values: the six marks, `TITLE`, `DEFINITION`, `FOCUS`,
   `CAPTION` (new token), `BG #212121`.
2. `subtitle()` and `axis_caption()` switch from `MUTED` to `CAPTION`.

**Per episode, when porting:**

1. **Colors**: confirm the file names only tokens, never raw manim colors — the
   restyle then lands automatically. Files that name raw colors get them
   replaced with the right token (what does this color *mean*?).
2. **Graph and card styling**: distinguish solid party cards from neutral
   allocation diagrams (§2c); tick numerals use `MUTED`, axis names white, and
   selected values red. Use sparse labels and the current definition treatment;
   area fills use the semantic token and opacity.
3. **Framebox / highlight yellows** → `FOCUS #FFE14D`.
4. **White axes** → the `axes()` factory (`MUTED`, no tips).
5. **Muted text** (subtitles, stored results) → `CAPTION`.
6. Check the affected frames and transitions against the notes and current
   specs. Use a full render when needed to validate a port or broader change;
   small styling updates need only targeted verification before viewer review.

**Historical mechanical fix-list from the v0 audit** (verify against the current
episode before applying; these values are not current model specifications):

- `SUPPLY` is an undefined name in `B1_pt2` (7 uses); `raster_font` undefined in 14 files; `manim_to_mov` (8 files) should be `Make_MOV`; `metaConfig*` dicts referenced in E2/E3 exist nowhere; `part_c` import in F3_pt2; `Video.consumer_solution` is dead.
- Stale part cards: C0 says Part B, E1 says Part D, F1 says Part E. Stale `media_dir`s (four files write to `PartC_E2`).
- Numbers: Andrew's A3 autarky point (3 C, 7 S) is outside his PPF; B1 demand readout says 35k at $2 (should be 30k); B2 states the demand intercept as 5 once (should be 8); Marryville/Maryville spelling.
- Duplicate class names silently shadow ~2,000 lines (A3 `animation_5` ×3, B3 `animation_1` ×3, F3_pt1 `title`/`animation_1` ×2).
