# E2 animation review

Separate working beat sheet for `E2_Animation.py`, scene `EpisodeE2`, November 9, 2026. The author’s notes (`01_Notes.md`, and the copy with build comments in `E2_Notes.md`) remain untouched. These beats supersede the storyboard comments in `E2_Notes.md`; the spoken notes still need reconciliation after the author’s prose pass. The beats below are built (November 9, on E1’s firm, Taylor’s choice) and rendered headlessly: 41 holds, 135 checkpoints, every hold reviewed. The October 30 build they replace (Codex) is in git; its problem was not polish but grain: it reached for whole areas, floating bars and a label-placement solver where the semester teaches one unit at a time on a graph that holds still.

## What departs from the semester’s style

1. **Profit arrives as whole areas, not from one unit.** 2.b fades in forty revenue strips, then forty cost strips, pours them into two bars, then fades a profit area and flies a copy to the side. B1, B2, C2 and E1 (4.d) always start from one unit with real numbers, and E1’s review made every bar exactly one output unit. Here the claim “TR = q · P” is never shown as “each unit sells for the price,” and q(P − ATC) appears as an equation rather than as the box’s width and height, which is B2’s yellow height-and-base measurement.
2. **The marginal decision is watched, not made.** 2.d drops a red dot on MC and rolls q from 40 to 50 to 100 while a side number peaks. The semester’s device is the next unit: B2 compares MC with one fixed price unit by unit (3.i–3.l), E1 4.d puts one unit’s MB beside its MC and adds units until they break even. The Part E plan listed this three-stage framing as missing and named 2.d as its natural place.
3. **The firm’s graph moves four times** (centered, beside the market, alone beside the panel, beside the market again, centered), and the market enters three times. Your E0 and E1 reviews ask for stationary panels and motion only where it is the point.
4. **A yellow zoom frame** (1.e.out) grows from the market crossing around the firm’s whole graph. The style guide reserves highlight boxes for a specific job; the semester’s “where price comes from” device is market and firm side by side with one shared price guide, which 3.b builds anyway.
5. **Supply rotates about the origin** (P = Q/α) so that entry can be a one-parameter roll, and the bottom line says “shifts down.” Your notes say shifts out; the course has always drawn shifts as parallel shifts.
6. **The side bars are the notes’ “two vertical lines,” but in a new idiom**: sliced fills on a grey floor, numbers and names in two rows under it, a floating π readout. E1 4.d already has an approved column: faint fill, solid value edge, value beside the edge, name under the base.
7. **Code the author cannot edit by reading top to bottom**: a 20-line numpy grid search (`area_word_spot`) to place TR, TC and π; nested `set_rect`, `update_profit_strips`, `place_area_word`; 120 profit polygons with per-frame updaters; a damped-cosine rate function for the long-run settle. The style guide’s flat-code rule exists for exactly this file.
8. **The costs are not E1’s.** The header says “the firm’s costs from E1,” but E1 now runs at a $100 wage (TC = 1,000 + Q², MC = 2Q, ATC = Q + 1,000/Q) and E2 still runs the old $50 firm (MC = q, ATC = q/2 + 1,000/q). Students would see a different ATC curve the class after they built it.

## Conventions and model

Keep the semester’s graphite background, azure topic titles, fixed-size gold teaching lines, white curve names, red tracing guides and readouts, grey contextual marks (the dot at ATC’s minimum included), and the Part E firm palette (MC orange, ATC purple, AVC pink, FC grey, the market’s demand and revenue teal, the price and its line red, profit orange, loss red). Whole-number readouts for quantities and totals, as in E1; per-unit prices and costs with two decimals where they are not whole.

**Model of record: E1’s firm.** Wage \$100 per hour, fixed cost \$1,000, so TC = 1,000 + q², MC = 2q, AVC = q, ATC = q + 1,000/q, lowest at q = √1,000 ≈ 31.6 where ATC = MC ≈ 63.25. The market price is \$100: q* = 50, ATC 70.00, TR 5,000, TC 3,500, π = 1,500. Market (Q in thousands): D: P = 120 − 2Q/3, meeting the price axis at 120 (Taylor, November 9: the demand curve should reach the vertical axis); S: P = (10/3)Q at the start, shifting right in parallel as firms enter (S: P = (10/3)(Q − s), s = 180 − 1.8 P*). Stops: P* 100 (Q* 30), 80 (Q* 60; firm q 40, ATC 65.00, TR 3,200, TC 2,600, π 600), 63.25 (Q* 85; q 32, π 0), 50 (Q* 105; q 25, ATC 65.00, TR 1,250, TC 1,625, π −375; AVC 25, so the firm keeps operating; the loss is less than FC 1,000). Price moves in 2.f: 80 (π 600) and 110 (q 55, ATC 73.18, TR 6,050, TC 4,025, π 2,025; at 120 the line would run through ATC’s name).

*Alternative for the long run:* FC = 900 in both episodes puts the minimum of ATC at exactly q = 30 and the long-run price at exactly \$60 (loss stop P* = 50: q 25, ATC 61.00, π −275). It changes E1’s totals (1,300, 2,500, 4,500) but none of its labor or marginal-cost numbers. Your call; the sheet below is written for FC = 1,000.

**Layout: one baseline and one price scale, and each section’s composition centred.** One baseline (origin y −2.225) and one price scale (\$0–\$130 per unit over 4.6 units) throughout; the market’s graph is 3.6 wide (Q 0–120 thousand), the firm’s 3.7 wide (q 0–70 units). Section 1 (market beside firm): market origin x −4.2, firm origin x 0.8. Section 2 (the firm with the columns): the market leaves and the firm pans left to x −4.2, centred in the space left of the divider at x 3.35; the columns stand at x 4.2, 5.2 and 6.2 (0.6 wide, 0.0003 units per dollar, on a grey base at the baseline) with the equation above them. Section 3 (all three): the market returns at x −6.1 and the firm pans to x −1.6; the columns do not move. The pans are eased, 1.6 s, as E1’s pan. (Taylor, November 9: two panels parked in a three-slot layout left a third of the frame empty; this replaces the fixed-slot and ghosted-market versions.) Axis words follow E1: the white symbol left of the vertical axis top with its grey sans unit caption to its right; the horizontal symbol below the axis end with its caption to its right. “Market” and “Firm” sit above their graphs throughout. ATC is drawn from where it comes down to \$118 and named there, clear of the caption; a grey dot (MUTED, not yellow; Taylor) marks its minimum. The bumper’s subtitle is “Competitive Firms”, the outline’s episode name (the notes’ header line, “The revenue side”, describes E3’s marginal revenue).

## 1.a–1.e · Competitive Markets

1.a · Title “Competitive Markets” (Taylor, November 9; the notes’ heading is Perfect Competition). Keep the market-structures grid with the red box on Perfect Competition, full size and centered, exactly as E1 leaves it. No bottom text.

1.b.buyers–1.b · Clear the grid. The market’s axes on the left, “Market” above them, a grey divider (B2’s graph-beside-text divider, at x 1.3, clear of the market’s captions) and the five conditions in grey centred in the space to its right; each lights white on its own hold, demand entering with “1. Many buyers” and supply with “2. Many identical sellers.” Keep the five lines from the second pass. No bottom text.

1.c · The list and its divider leave; the market stays. The firm’s graph fades in beside it, “Firm” above it, with MC, ATC and the grey dot at the minimum of ATC, the same curves students built in E1. No subtitle (the panel labels Market and Firm do that job; Taylor, November 9). No bottom text.

1.d · A red dot where S meets D, dashed guides, “P* = 100.00” on the market’s price axis, 30 under Q*. The horizontal red guide runs on across the gap to the firm’s price axis and continues across the firm’s graph as the same dashed red line, named “P = MR” (Taylor, November 9: the firm’s demand is the price, so it takes the price’s red, dashed); no separate readout on the firm’s axis while the market’s P* is there. Bottom: “Competitive firms are what we call price takers.” (This is the device 3.b currently builds; built once, here, it is the zoom.)

1.e · A red dot on the firm’s line at q = 60 with its dashed drop and 60 over q; one eased wiggle 60 → 68 → 30 → 60 (the axis ends at 70) while the market and the price stay put. No yellow frame. Bottom: “This firm changing quantity has no real effect on the price.”

## 2.a–2.f · Profit

2.a.word → 2.a · Title “Profit.” Zoomed in on the firm: the marks fade, then the market fades out as the firm pans left to sit with the columns. The firm’s price, 100.00 in red, appears on its own axis while the market is away. The word “Profit” right of the divider becomes π, then “= TR − TC” (π orange, TR teal, TC purple), at the top of the column slot. Bottom: “Profit is everything left over after we’ve paid our costs.”

2.b.unit · Start small: q = 20, red drop and 20 over q. Highlight the 20th unit as one narrow strip from the axis up to the price line, teal: this unit sells for \$100. Bottom: “Each unit sells for the market price.”

2.b.revenue · The other nineteen strips fill in one after another (the lagged fade is right here: it is the tiling). Name TR (teal, the revenue color; the price line itself is red) to the right of the area at (24.5, 85), clear of ATC and MC. Then a copy of the area lifts as one polygon into a teal column in the right slot, E1 4.d’s look: faint fill, solid teal edge, 2,000 above the edge, TR under the base; the area stays on the graph. Bottom stays.

2.b.cost · A purple dashed guide to ATC at 20 and 70.00 on the price axis. One strip from the axis to ATC: on average each unit costs \$70. Then the other nineteen; name TC right of the area at (24.5, 35), under MC. A copy of the area lifts into a purple column beside the first: 1,400, TC. Bottom: “Profit is the difference between these two areas.”

2.c.area · The two areas and their names fade; the difference remains: one orange box from ATC to P over 0–20, named π (white, at 0.8 q and 0.6 of the way up the box, since ATC cuts across its lower left; the name fades when the box is thinner than 0.3 units). Bottom: “So we usually just look at the difference on the graph.”

2.c.side · The part of the TR column above the TC column turns orange; “π = 600” above the columns. Bottom stays.

2.c · B2’s measurement: a yellow height mark up the box’s right edge labeled “P − ATC” and a yellow base mark along its top labeled “q”; copies of the two labels fly into the equation as it grows to “π = TR − TC = q(P − ATC).” The marks fade. No bottom text.

2.d.unit · The 21st unit: one white one-unit frame from q = 20 to 21 up to the price, a teal dot (revenue) where it meets the red price line and an orange dot where it meets MC. Its revenue is \$100; its cost, TC(21) − TC(20), is \$41, read in orange below and to the right of its dot (the one spot clear of MC, the ATC guide and the price line through the whole roll). The strip between MC and P is orange: what this unit adds to profit. At this scale one unit is a sliver, which is the point. Bottom: “Should we increase our quantity by 10?” (your line; the unit is how we decide).

2.d.ten · One tracker rolls the unit 21 → 30: the orange strip rides MC up toward the price, the box and the columns and every number roll with it (ATC 63.33, TR 3,000, TC 1,900, π 1,100). Bottom stays.

2.d.past · Bottom: “Profit will continue to rise until MR = MC, then it will fall.” The unit rolls on to 60: at 50 the orange strip has shrunk to nothing (unit 50 costs \$99, unit 51 costs \$101), and past 50 it flips above the price and turns red (this unit costs more than it brings in); π peaks at 1,500 at q = 50 and ends at 1,400 (ATC 76.67, TR 6,000, TC 4,600; the 61st unit costs 121).

2.d · The unit rolls back to 50 (ATC 70.00, TR 5,000, TC 3,500, π 1,500). Bottom stays.

2.e · The unit marks leave; a red dot where MC meets the price pulses once and q becomes q*. Bottom: “How much should the firm choose to produce? At MC = MR!”

2.f.low → 2.f.high → 2.f · Bottom: “This is an example of marginal thinking.” The price and q* roll together, q* riding MC: 100 → 80 (ATC 65.00, 3,200, 2,600, π 600) → 110 (73.18, 6,050, 4,025, π 2,025) → 100. The unit strip is gone; the box and columns do the work.

## 3.a–3.f · The Market, Entry And Exit, The Long Run

3.a · Title “The Market.” The equation, the ATC guide and the firm’s own price number leave; the firm pans right as the market fades back in further left, then its marks: the red crossing, P* = 100.00, Q* 30 and the price guide to the firm, as 1.d had them. Bottom: “So we need to zoom back out to see the whole market.”

3.b.demand, 3.b.supply · Demand pulses yellow, then supply, with your two sentences as written. 3.b · The crossing pulses. Bottom: “This is where the price for the firm comes from.” (The old 3.b.equilibrium is gone: the equilibrium and the bridge were built in 1.d.)

3.c · The profit box and the orange top of the TR column pulse yellow. Bottom: “At this price, the firm is making a profit, which is nice for them.”

3.d.entry · Title “Entry And Exit.” Supply shifts right in parallel; P* rolls 100 → 80, the firm’s line follows, q* rides MC to 40, the box and columns roll (π 600). Bottom: “New firms open up, so the supply curve shifts out.” (Your word.)

3.d.zero · P* 80 → 63.25: the box closes onto the yellow dot; π 0. Bottom: “Firms will continue to enter until there is no profit left.”

3.d · P* 63.25 → 50: the box flips above the price, turns red, named “Loss”; the TC column’s top turns red; “π = −375.” Bottom: “A negative profit is what we sometimes call a loss.”

3.e.avc · AVC (pink) joins the firm’s graph with a pink dot at q* = 25, below the price. Bottom: “Firms earning a loss will exit the market if price is below their AVC.”

3.e.fc · A third column, grey: 1,000, FC. Bottom: “Is operating with a loss better than exiting and paying the fixed cost?”

3.e · A copy of the red loss piece slides to the base of the FC column at the same scale, with 375 in red beside it: the loss is the smaller. Bottom: “Price is above AVC, so the loss is smaller than the fixed cost.”

3.f.exit · Title “The Long Run.” AVC and the FC column leave. Supply shifts back left; P* 50 → 63.25; the box closes. Bottom: “In the long run, if price is below ATC, firms exit, shifting supply in and the price up.”

3.f.cycle · One eased motion there and back (`there_and_back`): supply shifts out until the price is 57 (q 28.5, a small loss, the name faded) and returns to 63.25. No damped overshoot function. Bottom: “If price is above ATC, new firms enter, shifting supply out and the price down.”

3.f · The grey dot at ATC’s minimum pulses yellow under the red MC = MR dot; P* 63.25, Q* 85, q* 32, TR = TC = 2,000, π 0. Bottom: “Zero profit condition: in the long run, firms earn zero profit.”

## 4.a · Next Time

Clear the market, the columns, the divider, the readouts and the Firm label; the firm stays where section 3 put it, near the centre. Its dashed red price line gives way to a downward-sloping teal D (P = 120 − 2q). Bottom: “What happens to marginal revenue when demand slopes down?”

## Code

One `construct()` read top to bottom (663 lines, from 718, with far less machinery per line). `area_word_spot`, `place_area_word`, `set_rect` and `update_profit_strips` are gone; area names sit at fixed axis coordinates and the box’s name follows one rule. The revenue and cost areas are twenty one-unit strips for their reveal, then one polygon each; the profit box is one polygon on the two trackers; the marginal unit is a frame, a gain strip, two dots and a number on the quantity tracker (the unit is q to q + 1). The columns are plain polygons with one updater each, plus an orange cap on TR and a red cap on TC. Two `ValueTracker`s, the market price and the firm’s quantity; the wiggle of 1.e is an `UpdateFromAlphaFunc`. The equation is three `MathTex` pieces so its parts can be addressed. 41 holds.

## Open for Taylor

1. Decided November 9: E1’s firm. E3’s monopoly still runs the old \$50 costs and should be rechosen on these (for example D: P = 150 − Q/2 gives MR = MC at q = 50, P = 125, ATC 70, π 2,750).
2. FC = 1,000 (long run at 63.25 and 31.6, shown 63.25, 32) or FC = 900 (exactly 60 and 30, in E1 too).
3. The start quantity 20 has the same ATC (70.00) as q* = 50. It can be a teaching moment or a distraction; 25 (ATC 65.00, π 875) avoids it but makes the +10 step land on 35 (ATC 63.57).
4. “Should we increase our quantity by 10?” is kept as the bottom line for 2.d, with the next unit as the way of answering it.
5. The bumper subtitle “Competitive Firms” is written for this build; the notes’ header line is “The revenue side”.
6. No exercise part exists for E2. A short card after 1.e (read q* and profit at P = 100 off E1’s curves) would pose the day’s question before the Profit section, if you want one up front.
