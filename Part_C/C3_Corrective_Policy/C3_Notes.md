---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

## Episode C3 | *Correcting Market Failures*

*We can offset the problems of externalities with the problems of taxes.*

#### Corrective taxes

Story Board

1. How does the social planner get prices such that q_s = q_d = q_SOC?

2. If the price is set at buyers WTP, excess.

3. If the price is set at sellers WTS, shortage.

4. A tax or subsidy equal to the externality sets q_s = q_d = q_SOC.

5. Subsidy

As you might suspect from the names these are the components of the good that are private. And as we’ve done repeatedly we can find the equilibrium price and quantity ignoring externalities by intersecting the private supply and private demand curves. This is what we’ll call the private equilibrium.

In the presence of this negative externality though looking only at the private supply and private demand curves ignores the externalized costs.

### Animation design | C2 continuity

C3 uses C2's compact bars and two-question teaching sequence. Preserve the planner's failed single-price experiments, then explain how a corrective policy gets both sides to the efficient quantity. The source remains flat in `C3_Animations.py`; the identifiers below are literal pausepoints.

**Model.** MB = 12 − Q/5; MC = 2 + Q/20; externality = $2 per unit. The unregulated market exchanges 40 units at $4. Negative externalities: MSC = MC + 2 and Q* = 32. Positive externalities: MSB = MB + 2 and Q* = 48.

**Shared layout.** A stable 6.4 × 4.6 graph, quantity range 0–80 so the planner's excess-supply example fits, and units rather than tons. MSC uses a dashed orange curve and MSB a dashed teal curve throughout; private MC and MB remain solid. On every market graph, center quantity numbers on a fixed row immediately below the horizontal axis, with their quantity symbols on a separate aligned row underneath. Symbol height and superscripts never determine the number position; use the same rows for recap markers, planner readouts, policy quantities, the tax dial, and closing graphs. Place price-gap measurements on the vertical axis and quantity-gap measurements on the horizontal axis, with their numeric captions outside the plot. Grey unlabeled guides and a persistent grey dot retain the original equilibrium at (40, 4), including both planner experiments, policy graphs, close-up returns, and conclusions. Red price dots and yellow efficient dots sit above fills and guides. Base MB, MC and EXT bars use 0.16 opacity and appear only on exchanged quantities. Welfare uses individual unit strips. Topic titles stay blue, contextual subtitles grey, and the current teaching line yellow. Remove old subtitles before a new graph or close-up context enters.

**Close-ups.** Carry the selected MB/MC/EXT slices into the same compact columns each time, then back to the exact source slice. No unmatched group transforms or leftover grey highlight. Names live on the bars: MB/MC below their edges, MSC/MSB above, EXT inside the pink portion. Numeric values sit beside their corresponding levels. A dashed pink height measure gives the $2 externality. Yellow questions remain along the bottom left and right. Purple dashed projections measure the relevant comparison; pause before revealing a green check or red cross. Show only one social amount, TS or potential DWL. Government transfers occupy the middle gap, distinct from external cost or benefit.

### 0 | Bumper

> **0.a.** Shared raster bumper and Part C | Episode 3. Preserve the thesis: “We can offset the problems of externalities with the problems of taxes.” Fade and clear before the market.

### 1 | Negative-externality recap

> **1.a.** Title “Negative Externalities”; subtitle “A cost paid by others outside the market.” MB, MC and MSC with faint benefit/cost/externality strips through Q = 40. Grey original-equilibrium dot and red Q̂ = 40; yellow efficient dot and Q* = 32. Eight grey DWL strips between MB and MSC, from 32 to 40. Bottom: “Last time: the market exchanges 40 units, but only 32 are efficient.”

### 2 | The planner's price problem

**Quantity readouts (both planner sequences).** Center each number directly beneath its vertical guide on one fixed row below the horizontal axis. Show Qd and Qs on the row beneath their numbers only when the quantities are well separated; fade those labels away as they approach. During the crossing, briefly keep just one number to avoid overlapping digits, then restore both as they separate. Measure excess or shortage with a grey segment on the horizontal axis between the two quantity guides. Center its caption below both quantity rows, clear of the labels and the bottom teaching line; no gap indicator remains at the trial-price height.

> **2.a.** Title “The Social Planner”; subtitle “Someone who wants the efficient quantity, 32 units.” Clear the background strips and old price label; replace the red market guides with grey original-equilibrium guides. Remove the DWL strips and label for the entire price experiment and wedge setup. Keep the grey equilibrium dot, efficient marker, and aligned quantity readouts 40 / Q̂ and 32 / Q* until the price experiment begins. Ask: “What price gets buyers and sellers to exchange 32 units?”

> **2.b.** Fade out the Q̂ and Q* readouts as the price starts rolling from $4 to $5.60, before Qd and Qs appear. Keep the grey dot fixed at the original equilibrium throughout. The same buyer and seller dots move on their respective curves. Show Qd = 32, Qs = 72, and a grey excess segment labeled “excess: 40 units.” Bottom: “The price that works for buyers creates excess supply.”

> **2.c.** Roll to $3.60. Qs = 32 and Qd = 42, with a grey “shortage: 10 units.” Bottom: “The price that works for sellers creates a shortage.”

> **2.d.** Remove trial readouts and show both prices at Q = 32: Pb = $5.60 and Ps = $3.60. A yellow height measure spans those two prices on the vertical axis, with $2 just to its left between the price labels. Bottom: “One price cannot get both sides to the efficient quantity.”

> **2.e.** Emphasize the gap: “The $2 gap between the prices is the external cost per unit.”

### 3 | Corrective tax

> **3.a.** Title “Corrective Taxes”; subtitle “A tax equal to the external cost per unit.” Start a narrow filled green $2 bar on the price axis with “$2 tax” just to its left. Slide only the solid bar into the MB–MC gap at Q = 32, leaving the label and a dashed green vertical measure of the same height at the price axis. Both price dots and dashed guides appear; the quantity drop reaches the upper price. Place 32 nearest the axis, with Qᵗᵃˣ = Q* on the label row below it. Bottom: “The wedge gets stuck at 32 units, the efficient quantity.”

> **3.b.** Keep the clean graph with the wedge at Q = 32. Bottom: “Exchanges 33 through 40 no longer happen, so their deadweight loss is gone.” The recap DWL strips have already left; do not reintroduce them for a removal sweep.

> **3.c.** At the existing graph coordinates, build orange PS strips, then teal CS strips, then green government-revenue strips through Q = 32. The axis tax label and its dashed height measure leave together before the area labels enter. Bottom: “Buyers pay $5.60, sellers receive $3.60, and the government collects $2 per unit.”

> **3.d.** “With a tax equal to the external cost, there is no deadweight loss.”

#### Trade the tax prevents

> **3.e.select → 3.e.values.** Select unit 36, then move its matching slices into the compact bars: MB = $4.80, MC = $3.80, MSC = $5.80. The unit subtitle replaces the graph subtitle. Reveal the two yellow questions and the $2 external-cost measure.

> **3.e.tax → 3.e.question → 3.e.answer.** Show Pb = $5.60, Ps = $3.60 and a separate middle green tax transfer. Project MB versus Pb and MC versus Ps to the left. Pause on the measurements; then reveal the red cross.

> **3.e.social → 3.e.** Fade the government transfer and private measuring lines; dim the price information. Project MB and MSC to the right, pause, then reveal the red cross and “DWL $1,” with the corresponding grey portion on the bar. Bottom: “The tax prevents a trade that would create $1 of deadweight loss.” This is the harm *if the trade occurred*, not a loss caused by the corrective tax.

> **3.e.return.** Clear close-up annotations and people. Return the same three slices to their original location, restore the market and its subtitle, and remove the temporary slice.

#### Trade the tax preserves

> **3.f.select → 3.f.values.** Repeat the same geometry and scale for unit 24: MB = $7.20, MC = $3.20, MSC = $5.20.

> **3.f.tax → 3.f.question → 3.f.answer.** Reveal the actual prices and tax transfer. Measure both participants' private gains and pause before the green check.

> **3.f.social → 3.f.** Fade the transfer and private measurements. Measure MB − MSC on the right; pause before the green check and “TS $2.” Highlight that $2 interval on the buyer's bar. Bottom: “This trade generates $2 of social surplus.”

> **3.f.return.** Return the matching slices and remove the temporary close-up, restoring exactly the previous market.

#### Tax size

> **3.g.low.** Subtitle “Adjusting the tax around the $2 external cost.” Roll tax 2 → 1. Q = 36, Pb = $4.80, Ps = $3.80. Prices, filled wedge, quantity, individual CS/PS/revenue strips and label positions follow the tracker. Grey DWL grows only over 32–36. Clip partially crossed units while moving. Bottom: “A smaller tax leaves some harmful exchanges in place.”

> **3.g.reset.** Return tax 1 → 2 and Q = 32. Bottom: “Back to the corrective tax: $2 per unit.”

> **3.g.high.** Roll tax 2 → 4. Q = 24, Pb = $7.20, Ps = $3.20. Grey DWL now represents worthwhile forgone units 24–32. Bottom: “A larger tax removes exchanges that were worth making.”

> **3.g.** Return tax 4 → 2. “The corrective tax equals the external cost: $2 per unit.”

> **3.g.summary.** Clear updaters, remove the moving tax label and its backing rectangle, and move the existing graph left, keeping its geometry. On the right, first show yellow “Tax = EXT”; below it, reveal a yellow downward implication arrow leading to red Qᵗᵃˣ = Q*, with “32 units” in muted grey underneath. Bottom: “A corrective tax prevents costly exchanges and preserves worthwhile ones.”

### 4 | Corrective subsidy

> **4.a.** Positive-externality recap in the same footprint, with price axis to 15. Title “Positive Externalities”; subtitle “A benefit received by others outside the market.” Faint MB, MC and EXT strips only through Q = 40; MB and MSB stay teal, MC orange. Grey original-equilibrium dot at (40,4); yellow efficient dot at (48,4.4). Grey DWL strips represent forgone trades 41–48. Bottom: “Last time: the market exchanges 40 units, but 48 are efficient.”

> **4.b.** Return to “The Social Planner,” asking what price gets both sides to exchange 48 units. Clear the background strips, price label, DWL strips, and DWL label for the entire single-price experiment; retain the grey original-equilibrium dot and guides. Keep the aligned 40 / Q̂ and 48 / Q* readouts visible until the price experiment begins.

> **4.c.** Fade out the Q̂ and Q* readouts as the price starts rolling 4 → 2.40, before Qd and Qs appear. Keep the grey dot fixed at the original equilibrium throughout. Show Qd = 48, Qs = 8, shortage 40. “The price that works for buyers creates a shortage.”

> **4.d.** Roll price 2.40 → 4.40: Qs = 48, Qd = 38, excess 10. “The price that works for sellers creates excess supply.”

> **4.e.** Replace trial readouts with simultaneous Ps = $4.40 and Pb = $2.40 at Q = 48, with a yellow height measure on the vertical axis and $2 just to its left between the price labels. “One price cannot get both sides to the efficient quantity.”

> **4.f.** “The $2 gap between the prices is the external benefit per unit.”

> **4.g.start.** Title “Corrective Subsidies”; subtitle “A subsidy equal to the external benefit per unit.” Clear the planner's target-price guides and yellow gap measurement, and return to the actual no-subsidy market at Q = 40, P = $4. Restore eight grey DWL strips from 40 to 48, with the DWL label above them. Retain the original grey equilibrium dot and guides, dashed MSB, and the yellow efficient marker. Show one price label while buyers and sellers pay/receive the same price. Bottom: “Start at the market equilibrium, with no subsidy.”

> **4.g.prices.** Raise one subsidy tracker continuously from $0 to $2: Q = 40 + 4s, Ps = 4 + 0.2s, Pb = 4 − 0.8s. The two red price dots separate along MC and MB; horizontal price guides, axis prices, and the full-height quantity drop move with them. Replace the initial shared price label with separate Pb and Ps labels only when there is room. Keep quantity numbers on the existing axis row, with Qˢᵘᵇˢⁱᵈʸ beneath. Shrink the grey DWL strips from the moving quantity to 48, clipping the partially crossed strip rather than fading whole units. The DWL area is $0.125(48 − Q)², reaching zero at Q = 48. Bottom during motion: “As the subsidy rises, prices separate and deadweight loss shrinks.” Pause at Ps = $4.40, Pb = $2.40, Q = 48; replace the quantity symbol with Qˢᵘᵇˢⁱᵈʸ = Q*. Bottom: “A $2 subsidy brings quantity to 48 and eliminates deadweight loss.” No green wedge appears before this result.

> **4.g.wedge.** Only after the price result, reveal the narrow green bar between the two prices at Q = 48. Slide a copy OUT to the right, beyond the graph at Q-coordinate 88, retaining the original bar between the curves. Reveal “$2 subsidy” beside the extracted bar. Bottom: “The subsidy is the $2 gap between the sellers' and buyers' prices.” Pause so the wedge explains the price separation that has already happened.

> **4.g.** Clear the temporary right-hand illustration. Leave the original green bar at Q = 48, and show a dashed green height measure on the price axis spanning $2.40–$4.40, with “$2 subsidy” just to its left. These final objects travel with the graph through the later close-up and conclusion. Quantity remains 48 on the number row, with Qˢᵘᵇˢⁱᵈʸ = Q* below it.

> **4.h.** Keep the clean graph with the wedge at Q = 48. “The subsidy enables worthwhile trades that the market leaves out.” DWL has already shrunk to zero as the subsidy increased; do not reintroduce the old strips for a separate removal sweep.

#### Worthwhile trade the subsidy enables

> **4.h.select → 4.h.values.** Highlight unit 44 and pause with the yellow bottom note “Let's check an exchange that would not have happened before the subsidy.” Fade the note as the zoom begins. Carry unit 44's matching slices into compact bars: MB = $3.20 and EXT = $2 on the buyer's side, giving MSB = $5.20; MC = $4.20 on the seller's side. Same bottom questions, people, scale and measurement style.

> **4.h.question → 4.h.answer.** First compare MB and MC without the subsidy. Pause before revealing the red cross. “Without the subsidy, this trade does not happen.”

> **4.h.social → 4.h.surplus.** Project MSB and MC to the right; pause before revealing the green check and “TS $1.” “This trade would generate $1 of social surplus.”

> **4.h.subsidy → 4.h.enabled.** Reveal Pb = $2.40, Ps = $4.40 and the middle green subsidy transfer. Remove the separate externality measurement to avoid crowding the new price, while retaining the EXT bar and label. Replace the left measurement with the actual buyer/seller price comparisons. Pause, then reveal the green check. Retain the right social conclusion; the transfer is not counted in social benefit. “The $2 subsidy makes this worthwhile trade happen.”

> **4.h.return.** Clear all close-up annotations, restore the same market, return the source slices, and remove them.

#### Subsidy welfare

> **4.i.cs → 4.i.ps → 4.i.gov.** Show CS, PS and government spending as individual vertical strips at existing coordinates. These areas overlap, so show them one at a time, removing each before the next. Bottom after the spending reveal: “Buyers pay $2.40, sellers receive $4.40, and the government pays $2 per unit.”

> **4.i.** Remove the spending bars and their label. “With a subsidy equal to the external benefit, there is no deadweight loss.”

### 5 | End on the corrected market

> **5.a.** Move the same clean subsidy graph left. On the right: Qˢᵘᵇˢⁱᵈʸ = Q*, 48 units, and “Subsidy = external benefit.” Bottom: “A corrective subsidy enables worthwhile trades the market would miss.” This mirrors the tax conclusion in 3.g.summary and preserves the planner's central result: the policy aligns the market quantity with the efficient quantity.

<!-- Validation 2026-10-12: complete scene run produced 153 checkpoint images. Reviewed the graph, planner, close-up, tax-dial, subsidy and conclusion frames. Final targeted renders and backward checkpoint restoration passed; checked price/quantity arithmetic, highest dot layers, fractional strip clipping, zero orphan slices/subtitles after all three returns, and subsidy-spending cleanup. Development viewer navigation also reviewed. Exports remain temporary review artifacts, not the published student bundle. -->
