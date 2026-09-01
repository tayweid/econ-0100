# ECON 0100 Video Series — Graphite Style Guide (v1, 2026-08-26)

*Economics from scratch.* One cohesive story in six Parts; the visual system has to
carry continuity across ~30 episodes made over a year, by more than one pair of
hands. This guide is the contract: it settles every choice that recurs, explains
*why* each choice was made (so you can extend it without breaking it), and names
the ones still open.

**How to use this guide**

- **Writing a new episode?** Read §0–§3 once in full (identity, frame, color,
  type — the things you must never improvise), then use §4–§8 as reference while
  you build. `A/A0_Welcome/03_Code.py` is the reference implementation.
- **Porting or fixing old work?** Go straight to §10; it's a checklist.
- **Quick lookup?** Every color, size, and idiom lives in a table. Search this file.

Where this guide and older code disagree, **the guide wins**. Episodes import
everything from `_Assets/style.py` and never re-declare colors, sizes, or frame
settings — that indirection is what lets a system-wide change land without
touching episode files.

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
2. **The title architecture.** Flush-left azure title, muted caption stacked
   under it, generous emptiness below. Every screen has it.
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
| FPS | **60** for final renders; 10 is fine for previews. One setting, in `_Assets/style.py`. |
| Background | `BG #212121` everywhere — the same graphite as the websites (changed from #1f1f1f in v0; imperceptible on screen, meaningful in the system). No white-ground scenes (E2/E3/E4/C2 legacy files are out of spec). |
| Safe area | Keep titles ≥ 1 unit from the top (`to_edge(UP, buff=1)`), content ≥ 0.5 from sides. Leaves a strip for the notes panel / lower-third face. |
| Vertical centering | Body content is **vertically centred in the band between the title and the reserved bottom strip** (the strip holds definition lines, math rows, stored results — it is never body). Peer objects on one screen — a card column and a graph, two panels — share **one common vertical centre**, so the screen reads as a single block instead of a stack shoved under the title. In code: name the band once (`BODY_TOP` / `BODY_BOTTOM` / `BODY_MID`) and place every body object against it, rather than hand-tuning a `shift` per object. (Added 2026-08-31 from the A2 director's pass; the co-op screen's farm column and graph were 0.4 apart and both riding high.) |

**Four modes** describe the available stage layouts. They are not separate
storyboard fields; the beat's action makes the layout apparent:

- `cam` — face to camera, full frame. No animation.
- `anim` — animation full frame.
- `split` — animation on the **left**, face on the **right**, both in rounded-corner boxes on a grey ground, video box on black ("the video could be the animation on one side and a face the camera video on the other side").
- `notes` — a principle line or definition as a full-frame card (one sentence, body size). The accumulating side panel was tried and dropped as too cluttered; `style.NotesPanel` remains available if a later episode wants it.

Transitions between modes happen at beat boundaries only. Within a beat the mode is fixed.

## 2. Color

Every color is a **semantic token**. Episodes never name a raw manim color; they
use the token, so a change propagates. Three rules govern the whole palette:

- **Every hue is a noun.** A color appears on screen only because it *means*
  something (demand, Molly, a defined term). Never decorate with color.
- **Azure is reserved for the course's own voice** — titles on stage, links and
  accents on the web, the wordmark. It is never a curve, a fill, or a character.
  (Decided 2026-08-26; this is why demand is teal, not blue-blue.)
- **Marks and text are different jobs.** The six *marks* (§2b) are the only
  colors allowed to persist on the model; they were validated together for
  colorblind safety. Gold is a *text* token and never a curve — that exclusion
  is what lets the mark set pass validation.

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
sits at 3.2:1 contrast (it draws hairlines and dots, always beside white starred
labels).

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

**Gold beyond definitions**: the episode's *question lines* (*Where did all that
wealth go?*, *20 of the 30 are ports.*) are `DEFINITION` gold at the bottom edge
or under the title — gold marks "the thing to remember on this screen."

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
| `PURPLE` | `#A99CF2` | `TOTAL` (total surplus as one region) | `GUILD` <!-- ED 2026-08-30: "guild" renamed "co-op" in the F26 prose (A2/A3 notes, schedule); rename this token and the code's guild identifiers with the A2 animation rebuild. Same rebuild note: the Part A "numbers of record" below (PPF_Molly/Andrew/Guild) are still the OLD numbers and orientation — new set is Molly 10C/40S, Andrew 8C/16S, carrots horizontal. --> | — | — |
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
| Solid cards | a card representing a party (the farm square) takes the owner's token as fill, `ON_FILL` text, **no white stroke** |
| Best-response box | the player's own color; Nash cell `RED` box; efficient cell `GREEN` box; **same size** boxes |
| Number-line roles | color on a number line means a *role*: `EFFICIENT` green = chosen/benefit, `NASH` red = given up/cost (`set_color_of`) |

## 3. Typography

**Everything is LaTeX.** `Tex` for everything on screen; `MathTex` only for
display equations; `Text` never (font mismatch). Both of the stage's voices
come out of the Tex pipeline.

**The frame has three speakers** (the "Narrator" rule, decided 2026-08-26 —
this is why renders show two faces):

- **The title is the course speaking**: CMU Serif, `TITLE` azure. Same as ever.
- **Prose *under* the title is the narrator**: **CMU Sans** (LaTeX `\textsf`) —
  subtitles, statement-card clauses (*Microeconomics tells us…*), axis
  captions, welfare-legend numbers. In code this happens automatically:
  `subtitle()` and `axis_caption()` apply it, `narr_stack()` builds a
  statement card, and the `narration()` helper wraps any other narrator line.
- **The material is the book**: CMU Serif — all math, curve and item labels,
  and the full-frame cards (definitions, principles). A definition isn't the
  narrator talking; it's the book itself.

**The carve-out that makes this safe**: an under-title line that *is or is
about to become* math is material, not narration — `OC(Apple pie) = Banana
bread` sits under a title but it's an equation, and words on this stage
constantly dissolve into math (`Chocolate Cake ≺ Carrot Cake` onto a number
line). One face across that transform is the series' signature move, so math
always wins. If a line has an `=`, a `≺`, or will land on the model, it stays
serif — in code, pass `book=True` to `subtitle()` (stored OC results do this)
or use plain `stack()`.

To *see* the treatments compared (all-CMU vs. full dual vs. this rule), flip
the toggle in the type study:
https://claude.ai/code/artifact/725afeb5-f5e0-42a0-bc86-de24e4b92a28

The whole treatment hangs on one switch: **`NARRATOR_SANS` in `style.py`**
(currently `True`). Status: adopted, pending confirmation in a rendered A0
beat — the risk case is the statement card (big white CMU Sans at display
size). If it disappoints, the fallback is "D-lite" (statement cards return to
`stack()`; the small grey narrator layer keeps the flag) or `False` for
all-CMU. Don't hand-set fonts per episode either way — always go through the
idioms, so the flag stays in charge.

**Source Sans stays web-only.** The sites pair CMU Serif headings with Source
Sans 3 body; the stage's sans is CMU Sans and only CMU Sans — same pipeline,
matching metrics.

- Sizes by role, not ad-hoc scale: **episode head** 1.5 · **title** 1.2 · **body** 1.0 · **caption** 0.8 · **tick numbers** 0.7 · **part card** 3.0. Nothing below 0.7 — CMU's thin hairlines shimmer under projection and YouTube compression at small sizes; the scale floor and the 2160×1080 render are the defense.
- **Page titles** (`style.title`): `TITLE` azure, **flush left**, small top margin (buff 0.4, left 0.6). Every screen has one; figures don't get their own title — units go in a `CAPTION` **axis caption** beside the axis (`axis_caption`), e.g. title *Unemployment*, caption *rate (%)*.
- **Subtitles** (a question, a stored result): `CAPTION`, caption scale, stacked under the title and left-aligned with it (*What can a dollar get?*; the bakery's `OC(pie) = cake` lines).
- Lists: `VGroup(...).arrange(DOWN, buff=0.4, aligned_edge=LEFT)` under the title, left-aligned with it; never `to_edge(vector)` hacks. Rows that would overflow are scaled to fit the frame width, not wrapped.
- Multi-clause statements (the *Microeconomics tells us…* card): one clause per line, **no bullets**, key phrases in `DEFINITION` gold; a clause that must break continues on an **indented** second line (`\quad`). Built with `narr_stack()` — statement cards are the narrator (see the three-speakers rule above).
- **Text entry**: a sentence or card is `Write()`; a title is `FadeIn`; a row of pieces builds with the fly-in (`FadeIn` + re-center). `AddTextWordByWord` is reserved for the bumper label.
- Definitions: one line, `{{Term}}` isolated and colored `DEFINITION`, body in `INK`. Term appears in the script first ("definitions without definition"), the card comes after.
- Principle lines (*Preferences are rankings.*) are full-frame cards: one sentence, body size, `Write()`.
- Preference chains read **less-preferred on the left**: `Chocolate Cake ≺ Carrot Cake`, so they dissolve onto a number line without reordering.

## 4. Axes and graphs

- One factory: `axes(x_range, y_range, x_length=10, y_length=5)` → `MUTED` axes, `tips=False`, no ticks by default; tick numbers only when values matter for the argument.
- **Tick numerals are always `MUTED` — never colored by good.** When the goods need their colors on a graph, the **axis captions** carry them (*Carrots* in `CARROTS` orange on x, *Spinach* in `SPINACH` green on y) — the words-as-glyphs principle doing that work. (A1's colored numerals are out of spec.)
- Orientation invariants: **P vertical, Q horizontal** (B–E). **Carrots horizontal, spinach vertical** (A — as rendered in A1; reconcile `Video.py` if it disagrees). **Good A horizontal, good B vertical** (F). Wage vertical, labor horizontal (F2 — decide once).
- Curves: `axes.plot` for functions; **polyline (`set_points_as_corners`) inside `always_redraw`** for anything driven by a tracker or data — never `Transform` between two rebuilt plots (the wobble).
- Labels ride the curve end: short (`D`, `S`, `MC`, `ATC`, `MPB`), `INK`, `next_to` the right end. In C–E demand is relabeled `MPB` and supply `MPC` once externalities enter, and stays relabeled. (These labels are also the palette's safety net — every curve is identified by text, never by color alone.)
- Areas: `axes.get_area(...)` with the token's fill opacity. Hand-built `Polygon` only for shapes `get_area` can't express (tax wedge rectangle, profit box).
- Equilibrium: `GUIDE` dot + two dashed `GUIDE` drop-lines (`get_horizontal_line` / `get_vertical_line`, `dashed_ratio 0.85`, opacity 0.3 for the lines, 1.0 for the dot). Star the labels: `P^*`, `Q^*`.
- The surplus recipe is always shown **one unit → bars → triangle**, and the three-line rule text (below WTP / above price / inside quantity) is the same wording every time it recurs (B2, C1, C3).
- Say **excess**, never "surplus," for Qs > Qd.
- **Marker dots draw on top of lines.** After each `Create` of a segment, `bring_to_front` the dots (z_index alone isn't honored across plays).
- **Full-bleed images** (the Black Marble): `set_height(FRAME_HEIGHT * 1.02)` so no background shows; any title over an image gets a `BackgroundRectangle` in `BG` @ 0.7.

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
| PPF | straight lines until a bowed PPF is deliberately introduced; character colors; `Video.py` functions (`PPF_Molly = 5 − s/9`, `PPF_Andrew = 4 − s/4.5`, `PPF_Guild = 9 − s/7`) are the numbers of record |
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
- **No `Create` for boxes.** Choice boxes fade in — green first, then red — and *move* to swap. `Create` is for curves and lines.
- Default `run_time`: reveal 1, build 2–3, sweep 4–8. Bare `self.wait()` only as a VO beat; longer holds are explicit.
- Vocabulary → animation:
  | storyboard verb | manim |
  |---|---|
  | Show (card/text) | `Write` for sentences and cards; `FadeIn` for titles and objects (`FlickerIn` only for a deliberate switch-on) |
  | Draw (geometry) | `Create`, eased |
  | Add (to existing group) | `FadeIn` + `arrange` / `Transform` of the group |
  | Continue | extend the tracker |
  | Wiggle | `Indicate`-style scale pulse in `FOCUS`, 0.5 s |
  | Highlight | `SurroundingRectangle(buff=0.3)` in the relevant token, or area fill |
  | Circle | `Circle` around a cell/label (`circle_it`) |
  | Zoom / Pan | `MovingCameraScene` frame animate, smooth, 2 s |
  | Sweep | tracker from one end to the other, eased |
- Framebox reveal (`Create` → flip → `Uncreate`) is the emphasis idiom for a single line; use `framebox_it`. The box is `FOCUS` gold at a restrained stroke (~2.5 px equivalent) — an event, not a hazard sign.
- Dim overlay (`BG` rect @ 0.8) is allowed for definition cards only.
- Brackets that annotate a line fade **out** before a definition card writes **in**; never overlap the two.
- **maniml-specific tools** (all fine in render and export):
  - `self.pause(name)` — the beat boundary (§8); `loop=True` for a hold that keeps replaying in the viewer.
  - `self.add_sound(path, time_offset=0, gain=None)` — works in the viewer (plays through the system player when a live audience is connected; `time_offset`/`gain` shape only the rendered mix) and in the render (mixed into the mp4). Sound cues are beat-level: put the `add_sound` right after the beat's `pause`, and name files by beat in `00_Assets/sound/` (`0.a_bumper.wav`).
  - `FlickerIn(mob, flickers=4, seed=0, lag_ratio=0)` — switches a mobject on like an old tube light: dark, a few irregular sputters, then lit. Works on anything `FadeIn` does; `lag_ratio` staggers the sputters across submobjects. Use it sparingly — for a *reveal with attitude* (a title that "comes on", the bumper), not as a default entrance. Never for body text or definitions, which are `Write()`.

## 7. Recurring cards and devices

| Device | Spec |
|---|---|
| Episode bumper | raster `MICROECONOMICS` (Blues flicker, 4 rounds) with `Part X \| Episode N` beneath (`Part X` in `TITLE` azure, rest `CAPTION`, scale 3); the two form one **vertically centred block** (wordmark at +0.9, label at −0.9). Same bumper for the podcast intros. |
| Episode subtitle | the italic thesis line from the notes header (`*More might be possible!*`) appears under the bumper; every episode has one |
| Section title | `This class is about behavior.` pattern: a page title (§3), persists across the beats it governs |
| Last time… | `Tex('Last Time...').scale(3)`, 0.5 s in/out, then a 2–3 item recap in `notes` mode |
| Next time… | `title('Next time...')` + one line + framebox reveal |
| Definition card | §3 |
| Principle line | §3 |
| Six-parts card | six rows, each built in three fades: `Part X.` in `CAPTION` → part name in `DEFINITION` gold → subtitle in `INK`; labels are the `_Parts.md` headings; rows scale to fit the frame width |
| Choice boxes (`choice_boxes`) | `EFFICIENT` green = chosen, `NASH` red = given up; **same size** for both; fade in green then red; swapping a choice moves the boxes |
| Stored results | a running list of results (`OC(pie) = cake`) lives under the title in `CAPTION`, one line per result, added as each is found. They're equations, so they stay serif: `subtitle(..., book=True)` (§3's carve-out) |
| Simple glyphs | words-as-glyphs (§0): prefer **colored text** to a drawing (*Apple* green, *Banana* yellow — a good's own color is its noun); draw only when the object itself matters, then `INK` outlines (house, tickets). No food glyphs, no stick figures. |
| Welfare legend | right-hand column: swatch + `CS / PS / GOV / DWL` + live number in `CAPTION`, in that order — the model, not the bookkeeping, holds the eye |
| Assumptions checklist | a card listing model conditions (competitive firm: many sellers, many buyers, homogeneous good…), items lit as stated — needed in B0, E1, E2 |
| Taxonomy 2×2 | one grid object reused as a map: goods (rival × excludable) in D, market structures (sellers × differentiation) in E, current cell highlighted |
| Party cards | a solid card standing for a party (the farm square) is the owner's token fill with `ON_FILL` text — no white strokes (§2c) |

## 8. Storyboard and code conventions

- Storyboard = Markdown beat sheet (`_Storyboard_Template.md`): one heading per stable dotted ID followed immediately by its verb-first action list, for example `## 3.f · Draw the PPF`. Action is the only storyboard content, so there is no table, metadata block, status, or **Action** label. Playback order, not lexical ID order, is the episode order.
- Every student-facing beat begins at a standard Markdown link in `01_Notes.md`, for example `[▶ Beat 18](#beat-3.f)`. The visible label is only the sequential note-order name `Beat N`; the fragment is `#beat-` plus the exact dotted storyboard ID. Beat placement never authorizes adding, rewriting, polishing, or correcting the surrounding sentences. Do not add HTML beat comments, `Animation ·` kickers, descriptive labels, or duplicate prose. Exercises and `Next` passages use the same link contract. The notes keep the author's narrative and beat locations; the storyboard keeps only what happens at each beat. Concept emphasis such as `***absolute advantage***` remains ordinary prose and is never parsed as a stage direction.
- Production-only intro beats use `0.a`, `0.b`, and so on in storyboard and code. They do not appear in `01_Notes.md`. Student-facing beats begin at `1.*` and use the same exact dotted ID in notes, storyboard, and code.
- Code: one `class EpisodeXN(Scene)` with **one flat `construct()`**, the way manim is usually written. Each beat starts with a comment rule carrying the exact dotted ID, such as `# ---- 3.f`, and a stopped beat uses **`self.pause('3.f')`** as the maniml checkpoint. A file that calls `self.pause()` anywhere is *pause-anchored*: the pauses are the only checkpoints and all the plays between two of them run as one stretch — one arrow-key step, one timeline stop — so the viewer steps **beat by beat** (41 beats, not 133 plays). Write the literal `self.pause(` in the episode file; maniml detects that spelling, so a helper can't stand in for it. `self.pause(name, loop=True)` is a **looping hold**: in the live viewer the stretch that led in replays until an arrow key moves on (render/export treat it as a plain pause) — use it for a beat you talk over in class and want to keep moving (the bumper flicker, a sweep worth watching twice). **No per-beat methods** — maniml maps `construct()`'s statements to units; a `self.beat()` call hides its plays from the stepper (decided 2026-08-22; the inlining alternative is written up in `maniml/docs_helper_inlining_plan.md`). Inline helper closures (`def fly_in(...)`) are fine. Episode-specific choreography classes (`ValueLine`) live at module level in the episode file. Data/images loaded at module level. Imports from `_Assets` via the `sys.path` line. Header `# maniml 03_Code.py EpisodeXN`.
- No triple-quoted section markers inside functions (they broke 11 files); use dotted-ID comments such as `# ---- 3.f`.
- `_Assets/style.py` owns: `NotesPanel`, `on_model()`, `MODEL_CENTER/MODEL_WIDTH`, and the tokens in §2, frame/FPS, `axes()` factory, `title()`, `subtitle()`, `definition()`, `principle()`, `bumper()`, `last_time()`, `equilibrium_marker()`, `welfare_legend()`. Episodes import from it and from `Video.py` (model geometry) and never re-declare colors.

## 9. Decisions

Settled 2026-08-21:

- **Supply color = ORANGE.** Yellow-family is reserved for `FOCUS`/`DEFINITION`.
- **Notes panel: tried and removed** — built as `style.NotesPanel` and run through Episode 0; too cluttered. Principle lines and definitions are full-frame cards. The class stays in `style.py` unused.
- **Axes = `MUTED` grey** (as in `A/A0_Welcome`); the white axes in A–D code are out of spec.
- **Episode numbering**: in flux while Part A is reorganized; leave headers as they are and reconcile to `_Specs.md` codes later.
- **Intro motif**: the raster wordmark (built, in use).
- **`split` layout: animation LEFT, face RIGHT.** Keep it for eyeline continuity.

Settled 2026-08-22:

- **Utility lines are ordinal** (§5); **no per-beat methods** (§8).

Settled 2026-08-25/26 (the Graphite pass — see the design document for evidence):

- **Palette re-stepped for CVD safety and brand unification.** The six marks and the text tokens of §2 replace the manim defaults; validated against the co-occurring on-screen sets, not eyeballed.
- **Azure is reserved for the course's voice.** Titles, links, wordmark — never a curve. Demand is deep teal `#128A9B`, which separates from the title at ΔE 12.7 under CVD and validates better against the other marks than an azure demand did.
- **Gold is a text token, never a mark.** That exclusion is what makes the mark set pass validation.
- **`CAPTION #9E9E9E` splits from `MUTED #696969`.** Words vs lines. Muted *text* was at 3.0:1 — below the accessibility floor and fragile under compression.
- **`BG` = `#212121` everywhere**, unified with the websites.
- **The Narrator rule (supersedes same-week "board speaks CM, always")**: the frame has three speakers — title = the course (CMU Serif, azure), prose under the title = the narrator (CMU Sans via `\textsf`), material = the book (CMU Serif: math, model labels, definition/principle cards). Carve-out: an under-title line that is or becomes math stays serif. One switch, `NARRATOR_SANS` in `style.py`; adopted with the render test outstanding (§3 has the fallback ladder). Any stage sans is CMU Sans, never Source Sans.
- **Tick numerals never take good colors; axis captions do.**
- **One system, three surfaces**: the same tokens back `style.py` and `course.css`; thumbnails are stage frames with the raster mark; the raster mark is the channel identity.

Deferred (not needed until Part B/C):

- **Avatars** — social planner (C3), seller with a question (E1), buyer summation (B1). **No stick figures.** Direction: very simple and stylized, undecided — the words-as-glyphs principle suggests a colored initial in a circle, which the placeholder already is. Placeholder until then: a labelled `Circle` in the party's token color (`DEMAND` buyer, `SUPPLY` seller, `INK` planner) with a one-word `Tex` label beneath; speech as a `Tex` line in a `SurroundingRectangle`. Swap for the real glyph later — one helper, one place.
- **Unspecified diagrams**: game tree (D4), Edgeworth-in-PPF, the four-quadrant Map, labor market/monopsony, two-country trade panels, timeline-S&D hybrid (C2). Each needs one sketch before its block is storyboarded.
- **Split-mode chrome** design (and whether it ever needs CMU Sans).
- **Question-list / numbered-list slides** need a design pass of their own: voice (narrator sans vs. book serif), color (`DEFINITION` gold vs. `INK`), and layout. Interim decision 2026-08-30: white CMU Serif — the narrator-sans-gold treatment was tried on A2's *Two Remaining Questions* and pulled. Same open pass covers **exercise cards**; interim 2026-08-30: bodies in narrator sans (trialled on A2 — inline `$R$`/`$F$` stay serif math inside `\textsf`), heads serif gold.

## 10. Porting old work

The order matters: fix the shared assets once, then each episode is mostly a
re-render plus a short checklist.

**Once, in `_Assets/style.py`** (the Graphite document has the exact block):

1. Palette block → §2 values: the six marks, `TITLE`, `DEFINITION`, `FOCUS`,
   `CAPTION` (new token), `BG #212121`.
2. `subtitle()` and `axis_caption()` switch from `MUTED` to `CAPTION`.

**Per episode, when porting:**

1. **Colors**: confirm the file names only tokens, never raw manim colors — the
   restyle then lands automatically. Files that name raw colors get them
   replaced with the right token (what does this color *mean*?).
2. **A1-style habits** (the known off-spec patterns): party cards get the
   owner's token fill + `ON_FILL` text, no white strokes; tick numerals back to
   `MUTED`; good colors move to axis captions; area fills at 0.35, never full
   opacity.
3. **Framebox / highlight yellows** → `FOCUS #FFE14D`.
4. **White axes** → the `axes()` factory (`MUTED`, no tips).
5. **Muted text** (subtitles, stored results) → `CAPTION`.
6. Re-render, then step through beat by beat against §7's card specs.

**Mechanical fix-list surfaced by the v0 audit** (do before porting each Part):

- `SUPPLY` is an undefined name in `B1_pt2` (7 uses); `raster_font` undefined in 14 files; `manim_to_mov` (8 files) should be `Make_MOV`; `metaConfig*` dicts referenced in E2/E3 exist nowhere; `part_c` import in F3_pt2; `Video.consumer_solution` is dead.
- Stale part cards: C0 says Part B, E1 says Part D, F1 says Part E. Stale `media_dir`s (four files write to `PartC_E2`).
- Numbers: Andrew's A3 autarky point (3 C, 7 S) is outside his PPF; B1 demand readout says 35k at $2 (should be 30k); B2 states the demand intercept as 5 once (should be 8); Marryville/Maryville spelling.
- Duplicate class names silently shadow ~2,000 lines (A3 `animation_5` ×3, B3 `animation_1` ×3, F3_pt1 `title`/`animation_1` ×2).
