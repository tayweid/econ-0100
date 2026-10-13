# Episode B1 | Demand | Storyboard

Authoritative beat spec, derived line-by-line from `01_Notes.md` (rev. 2026-09-13).
Every on-screen word, number, and dataset traces to a notes sentence, an adopted
equation, or a style.py idiom — nothing else appears on screen. `03_Code.py`
implements this file exactly; deviations are bugs.

## Global conventions (binding, Taylor 2026-09-13)

- **Titles**: short azure nouns via `title()` ('Quantity Demanded', 'The Law of
  Demand', 'Consumer Surplus', 'Market Demand'). Never sentences, never gold
  keywords in the title.
- **Definitions**: gold term + white words, on the stage (under the title or in
  open frame beside the plot). Body scale per §3.
- **Graph-scene layout (Taylor 2026-09-13, round 3)**: the axes sit centered
  in the LEFT half of the frame; the RIGHT half holds the math and
  derivations (uniform white serif steps, no boxes, no emphasis frames);
  definitions run along the BOTTOM edge — smaller font (caption-scale), the
  text block squished to the bottom edge with a bit of padding.
- **Axis reads (replaces the two-sided guide rig)**: start at the KNOWN
  value's axis, draw a dashed segment from that axis to the demand line, then
  a dashed segment from the line to the OTHER axis; the dashes never extend
  past the curve. The landing value on the target axis is CIRCLED (no second
  numeral added — circle the axis's own number when it exists) and labeled at
  the terminus: `Q_d = 2` / `MB = $1`. Direction makes the plug-in visible:
  price-in reads go P axis → line → Q axis; quantity-in reads go Q axis →
  line → P axis.
- **Line creation**: a demand line is DRAWN from its top intercept downward
  (Create top-down), never faded in. When the fitted line arrives, the jagged
  data drops to a much fainter opacity than round 2 (clearly background).
- **No camera zooms anywhere.** Focus is made by fading other elements out.
- **Readouts at parks**: whole values display as integers (2, 3, 35), never
  "2.0"; decimals only when the value is fractional (1.5).
- **Axes**: established proportions (the x_length≈7 / y_length≈6–7 family,
  scaled uniformly). Never frame-wide.
- **Staircase bars**: unit bar i has its flat top at the line's value at Q = i —
  top-right corner ON the line. Chocolate bar tops: $2.00, $1.50, $1.00, $0.50.
- **Standing grey bars**: from the moment a fitted demand line stands alone on
  a stage, the faint MUTED unit staircase sits under it — each bar a standing
  decision — quiet enough that a "checked but not bought" MUTED bar still
  reads as an event. Market stage: many thin bars, same idea.
- **Adopted numbers**: individual P = 2.5 − Q/2 (dots ($4,0), ($2,1), ($1,2),
  ($0.50,4), ($0.25,6)); market P = 12 − Q/5, spinach, thousands of lbs/month.

## Act 0 | Bumper

| id | action | concludes (notes) |
|---|---|---|
| B01 | `bumper_raster` | — |
| B01b | `flicker` | — |
| B01c | `bumper_title(self, squares, 'B', 1)`; thesis *A simple way to organize preferences.* (episode subtitle, L3) | L3 |

## Act 1 | Last time — LITERAL COPY OF B0

B0_Markets/03_Code.py sections **B01–B05b copied verbatim**: 'Last Time...'
card; Part A stage (title+subtitle, PPF, alpha bow, arrow, gold core line,
including the static-then-live PPF swap and `self.remove(alpha)`); Part B
column + subtitle with the camera ease-out; the three questions keyed in with
the Option 1/Option 2 dots. Same plays, texts, camera, pauses. No restaging,
no reordering, no rewording.

| id | action | concludes |
|---|---|---|
| B02–B03d | the copied B0 block — seven stopped beats, 1:1 with B0's B01–B05b. **Verification: extract B0's own rendered frames (B0_Markets/media/EpisodeB0.mp4) at the matching pausepoints and compare — camera framing, title position, and subtitle size must match B0's render, not a reading of its code.** | L5–L11 |

*(The recitation-recap slide is CUT — Taylor 2026-09-13 round 3: "take the
recitation demand slide out all together." The act goes from the copied B0
block straight into Amanda-Grace.)*

## Act 2 | Amanda-Grace's answers (chocolate stage)

Stage: title('Quantity Demanded'); axes Q 0–7, P 0–4.5, established
proportions, ticks/numerals MUTED. The price line is the ASKING DEVICE — it
starts high and steps down; each stop elicits her dot (Taylor: "we start high,
then show amanda-grace's quantity at that price, then lower, and so on").

| id | action | concludes |
|---|---|---|
| B05 | axes in; price line arrives at **$4** ($4 marked at the P axis) | L15 (first half) |
| B05b | her dot at **(0, $4)** with label *individual quantity demanded* (L17 direction); definition (L19): **Individual Quantity Demanded** gold + white words | L15–L19 |
| B05c | price lowers to **$2**; dot **(1, $2)** | L21 |
| B05d | price lowers to **$1**; dot **(2, $1)** | L23 |
| B05e | price keeps stepping: **$0.50** → dot (4, $0.50); **$0.25** → dot (6, $0.25); price device fades; park on her data | L25–L27 |
| B06 | connect dots bottom-up with INK segments (L31); definition: **Individual Demand Curve** gold + *the full collection of quantity demanded* (L13's exact phrase) | L29–L31 |
| B07 | title → 'The Law of Demand'; definition: **Law of Demand** gold + *a good's quantity demanded falls with its price* | L33–L35 |
| B08 | **P = 2.5 − Q/2** DRAWN from the $2.50 intercept downward through the data (equation above the line, white serif); dots/segments drop to faint background opacity; hold on the $4 dot's gap above the line | L37–L39 |
| B08b | dots and segments fade out (L39); stage re-ranges to Q 0–6, P 0–2.50; **standing grey staircase bars ghost in** under the line | L39 |

*(L43's italic "Maybe add something here…" is Taylor's unresolved note — nothing
is built from it.)*

## Act 3 | Reading the line

| id | action | concludes |
|---|---|---|
| B09 | price-in read at **$1.50**: dash from the P axis at 1.50 to the line, then down to the Q axis; CIRCLE the axis's 2, label `Q_d = 2` at the terminus; steps `1.50 = 2.5 − Q/2` → `Q = 2` in the right half. No box, no duplicate numerals, dashes stop at the curve | L45–L51 |
| B09b | read moves to **$1.75**: dashes re-draw, landing between 1 and 2; label `Q_d = 1.5`; steps re-solve in the right half | L51–L53 |
| B10 | quantity-in read: dash UP from the Q axis at 3 to the line, then across to the P axis; circle the 1.00, label `MB = $1`; steps `P = 2.5 − 3/2 = 1` in the right half | L57–L59 |
| B10b | definition: **Marginal Benefit** gold + *the value of one more unit* (L63); park through L65's narration | L61–L65 |
| B11 | `exercise_card`: pasties **P = 12 − Q/2** (L113's continuing-cast note): (a) Q_d at **10 galleons** (→ 4 thousand), (b) MB at **4 thousand** (→ 10 galleons) — an inverse pair; both prices are L113's own (5 and 10 galleons) | L67 |

## Act 4 | The bars and the decision (price fixed at $1)

| id | action | concludes |
|---|---|---|
| B12 | (round-4, Taylor) the single exchange ALONE: the demand curve, its D label, the equation, and bars 2–4 all fade — only the axes, resting bar 1, and the price line at **$1** remain. The price label (`Price 1.00`) rides the line's right end at one constant size. No camera zoom. | L69 |
| B12b | bar 1 splits at the price: CS above (DEMAND 0.35), Expenditure below (GOV); the NUMBERS sit ON the boxes; the word labels sit to the RIGHT of the boxes, each vertically centred on its box. Definition **Consumer Surplus** gold + white at the bottom edge (L73) | L71–L75 |
| B12c | **the price experiments (the original code's choreography)**: raise the price above the bar top (to $2.40) — the exchange disappears: only the bar's DEMAND top edge remains, labels and numbers hidden; lower to $0.50 — she buys eagerly; settle back at **$1**. | L71, L77 first clause |
| B12c2 | **bar 2 joins and gets the exact same treatment**: the price runs the same raise/lower experiment over both bars (each bar strips to its top edge as the price passes its value), then settles at $1; the word labels ride to the right of the rightmost buying bar throughout. | L77 |
| B12d | the walk continues: bar 3 (top **$1.00** = price → buys, the zero-surplus marginal unit, expenditure box only), bar 4 (**$0.50** < $1 → **she stops** — only its DEMAND top edge remains). Numbers on boxes, words step right of bar 4; the accounting in the right half: `CS = 1.00 + 0.50 + 0.00 = $1.50`, `Expenditure = 3 × $1.00 = $3.00`. **Q_d** = the axis's 3, circled, tag beneath | L77–L83 |

## Act 5 | The triangle

| id | action | concludes |
|---|---|---|
| B13 | the bars' CS pieces merge into the **triangle** (DEMAND 0.35); the demand line and D label return to hold the area's upper edge; the price line stays on top | L85–L87 |
| B13b | `Area = ½hb` in white serif, open frame | L89–L91 |
| B13c | height on the P axis: $1.00 → $2.50, **h = $1.50** | L95–L97 |
| B13d | base on the Q axis: 0 → 3, **b = 3** | L99–L101 |
| B13e | the two numbers fly into the equation; `½(1.50)(3) = $2.25`; parked beside the bars' $1.50 total — *almost* the same number (staircase note, L111) | L103–L109 |
| B14 | `exercise_card`: pasties **P = 12 − Q/2** — (a) Q_d at **5 galleons** (→ 14 thousand), (b) CS at that price (½ · 7 · 14 = **49**) (L113 pattern, its own price) | L109–L113 |

## Act 6 | Market demand (spinach stage)

| id | action | concludes |
|---|---|---|
| B15 | card: **Market Demand $|$ Simulation** — cue the live room tally (L117 direction); stage parks | L115–L117 |
| B16 | **[PLACEHOLDER — 3D Sim beat to come]** clean card (no ghost): the sum of everyone's individual quantity demanded (L119; L121 records the decided Sim/ route) | L119 |
| B17 | title('Market Demand'); spinach axes (Q 0–60 thousand, P 0–12, established proportions), line **P = 12 − Q/5** with the equation above it; axis caption *spinach, thousands of lbs per month*; **many thin grey bars** under the line | L123–L125 |
| B17b | read at **$5**: dashed guides, $5 at P axis, **35** at Q axis; steps `5 = 12 − Q/5` → `Q = 35` | L127 |
| B17c | price to **$2**; guides follow → `Q = 50` | L131 |
| B18 | back at $5. **Expenditure is NOT bar-by-bar** — the script: "It would be very difficult to go through each one. So instead…" — one GOV rectangle fills below the price over the visible bars; steps: `35,000 × $5 = $175,000` | L133–L135 |
| B18b | **CS IS the sweep** (L139 direction): height line on the P axis (12 − 5 = $7), then sweep right THROUGH the bars, base extending, DEMAND areas accumulating bar by bar to Q = 35; steps: `½(7)(35,000) = $122,500`; park through L141 | L137–L141 |

## Act 7 | Closer

| id | action | concludes |
|---|---|---|
| B19 | limitations: the spinach stage dims wholly; two SCHEMATIC demand lines (no equations, no numbers — the sentence's picture only), the higher labeled *rich person*, the lower *poor person* (L145's words). No other copy. | L145 |
| B20 | card: **Next Time $|$ Sellers** + *What does it cost them to say yes to a trade?* (L147's words) | L147 |
