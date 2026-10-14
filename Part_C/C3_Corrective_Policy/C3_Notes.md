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

**Shared layout.** A stable 6.4 × 4.6 graph, quantity range 0–80 so the planner's excess-supply example fits, and units rather than tons. MSC uses a dashed orange curve and MSB a dashed teal curve throughout; private MC and MB remain solid. On every market graph, center quantity numbers on a fixed row immediately below the horizontal axis, with their quantity symbols on a separate aligned row underneath. Symbol height and superscripts never determine the number position; use the same rows for recap markers, planner readouts, policy quantities, the tax dial, and closing graphs. Place price-gap measurements on the vertical axis. Place quantity-gap bars below both quantity readout rows, with their captions underneath, outside the plot. Grey unlabeled guides and a persistent grey dot retain the original equilibrium at (40, 4), including both planner experiments, policy graphs, close-up returns, and conclusions. Red price dots and yellow efficient dots sit above fills and guides. The externality recaps shade only DWL, with no background MB, MC or EXT bars. Close-up base bars use 0.16 opacity. Welfare uses individual unit strips. Topic titles stay blue, contextual subtitles grey, and the current teaching line yellow. Remove old subtitles before a new graph or close-up context enters.

**Close-ups (revised spec, 2026-10-14).** Keep C2's spread columns and two red price lines, with the green government bar between the actual corrected-market prices. Use the common 0.68 dollars-to-height scale, faint MB/MC bases, and C1's pink EXT stack with MSC/MSB. Close-up subtitles identify the unit and its role without repeating graph prices. Drop the separate pink $2 measure to avoid crowding prices. Show CS and PS fills with names only; the government bar and social verdict also use names only (tax, subsidy, TS, DWL). Keep numeric boundary values, prices, introductory policy measurements, and explanatory arithmetic. Read the buyer against Pb, pause, then the seller against Ps, pause, then reveal the market check/cross. Only afterward compare MB with MSC (tax) or MSB with MC (subsidy) using C1's purple bracket and icon, with a TS/DWL name only. Clear private welfare fills and dim price annotations and private brackets during the social comparison so a transfer is never counted as a real benefit or cost. Keep “Will they exchange?” unchanged on the left. Reveal the buyer comparison, then its own check/cross and pause before the seller comparison. Reveal the seller’s own check/cross separately; retain both verdicts through the social comparison. Private comparison brackets are teal for buyers and orange for sellers; dashed projections and the social bracket stay purple. Keep the society question on the right, exact source-slice returns, and the existing conclusion layout.

**Shared C2 market labels.** Price readouts end 0.20 units left of the price axis. Use green “Tax = $2” and “Subsidy = $2” beside the dashed measurements, with their right edges aligned with the prices. Keep the rolling tax number; when the two prices get close, move that measurement's text left far enough to avoid the price readouts. Label the tax-revenue welfare region GOV, including the tax dial; explanatory prose still calls it government revenue.

**Policy-curve explanation.** Add one temporary landing beat after each wedge is established. Green strips cover the externality interval (above MC for tax, above MB for subsidy); the corresponding dashed policy curve coincides with the already-dashed social curve. Merge the curve names by crossfading, then restore the clean graph. Preserve the user's dashed MSC/MSB convention and units throughout. No adjusted-cost/benefit curves enter the close-ups.

### 0 | Bumper

> **0.a.** Shared raster bumper and Part C | Episode 3. Preserve the thesis: “We can offset the problems of externalities with the problems of taxes.” Fade and clear before the market.

### 1 | Negative-externality recap

> **1.a.** Title “Negative Externalities”; subtitle “Maximize society’s total welfare.” Show MB, MC and MSC without benefit/cost/externality fills; DWL is the only shaded area. Grey original-equilibrium dot and red Q̂ = 40; yellow efficient dot and Q* = 32. Eight grey DWL strips between MB and MSC, from 32 to 40. Bottom: “Last time: the market exchanges 40 units, but only 32 are efficient.”

### 2 | The planner's price problem

**Quantity readouts (both planner sequences).** Center each number directly beneath its vertical guide on one fixed row below the horizontal axis. Show Qd and Qs on the row beneath their numbers only when the quantities are well separated; fade those labels away as they approach. During the crossing, briefly keep just one number to avoid overlapping digits, then restore both as they separate. Measure excess or shortage with a grey segment below both quantity readout rows, horizontally aligned with the two quantity guides. Keep this bar at a fixed height even when the Qd/Qs symbols fade away. Center its caption just beneath the bar, clear of the bottom teaching line; no gap indicator sits on the axis or at the trial-price height.

> **2.a.** Title “The Social Planner”; subtitle “Maximize society’s total welfare.” Clear the old price label; replace the red market guides with grey original-equilibrium guides. Remove the DWL strips and label for the entire single-price experiment. Restore them when the actual tax starts rising from zero. Keep the grey equilibrium dot, efficient marker, and aligned quantity readouts 40 / Q̂ and 32 / Q* until the price experiment begins. Ask: “What price gets buyers and sellers to exchange 32 units?”

> **2.b.** Fade out the Q̂ and Q* readouts as the price starts rolling from $4 to $5.60, before Qd and Qs appear. Keep the grey dot fixed at the original equilibrium throughout. The same buyer and seller dots move on their respective curves. Show Qd = 32, Qs = 72, and a grey excess segment labeled “excess: 40 units.” Bottom: “The price that works for buyers creates excess supply.”

> **2.c.** Roll to $3.60. Qs = 32 and Qd = 42, with a grey “shortage: 10 units.” Bottom: “The price that works for sellers creates a shortage.”

> **2.d.** Remove trial readouts and show both prices at Q = 32: Pb = $5.60 and Ps = $3.60. A yellow height measure spans those two prices on the vertical axis, with $2 just to its left between the price labels. Bottom: “One price cannot get both sides to the efficient quantity.”

> **2.e.** Emphasize the gap: “The $2 gap between the prices is the external cost per unit.”

### 3 | Corrective tax

**Policy consistency review.** Both policies use aligned axis numbers with quantity symbols below, dashed social curves, grey original-equilibrium dots and guides, axis-based gap measurements, and a clean planner price experiment. Each actual policy starts at the original equilibrium with DWL, separates prices while shrinking DWL, then extracts the wedge outward (tax left, subsidy right). Selection pauses carry yellow teaching notes; the compact decision scenes follow the revised price-and-welfare specification below. Tax revenue regions can remain together because they do not overlap; subsidy welfare regions remain sequential because they overlap.

> **3.a.start.** Title “Corrective Taxes”; subtitle “A tax equal to the external cost per unit.” Clear the planner's target prices and yellow gap measurement. Return to Q = 40, P = $4, with grey DWL strips from 32 to 40 and a DWL label above them. Keep the grey original-equilibrium dot and guides, dashed MSC, and yellow efficient marker. Start with one shared price label. Bottom: “Start at the market equilibrium, with no tax.”

> **3.a.prices.** Raise the tax continuously from $0 to $2: Q = 40 − 4t, Pb = 4 + 0.8t, Ps = 4 − 0.2t. Both red dots follow their curves; price guides and axis numbers follow the tracker. Separate price labels only when there is room; quantity numbers stay on their fixed row. Clip DWL strips continuously at the moving quantity, shrinking the area between 32 and Q to zero. Bottom during motion: “As the tax rises, prices separate and deadweight loss shrinks.” Pause at Pb = $5.60, Ps = $3.60, Q = 32, with Qᵗᵃˣ = Q* below the number. Bottom: “A $2 tax brings quantity to 32 and eliminates deadweight loss.” No green wedge appears before this result.

> **3.a.wedge.** Reveal a narrow green bar between the two prices at Q = 32. Slide a copy OUT to the left, just beyond the price axis, retaining the original bar between the curves. Show “Tax = $2” to the left of the extracted bar. Bottom: “The tax is the $2 gap between the buyers' and sellers' prices.” Pause.

> **3.a.** Replace the extracted solid bar with a dashed green height measure just left of the price axis, retaining its “Tax = $2” label. Use a 2.5-width dashed line at Q-coordinate −1.2; the dynamic marker follows both prices and disappears when they coincide. Keep the solid wedge in the graph. Both axis readouts travel with the market through welfare and close-up returns.

> **3.a.curve.** Keep the wedge, prices, quantity, grey reference dot/guides, and efficient marker. Sweep opaque green $2 strips over the original 40 cost slices, with the pink externality underneath; fade in the dashed MC + tax curve on MSC. Crossfade their names to MSC = MC + tax. Bottom: “A $2 tax lifts MC onto MSC: private and social costs match.” Restore the original MSC name and remove the temporary strips and policy curve before 3.b.

> **3.b.** Keep the clean graph with the wedge at Q = 32. Bottom: “Exchanges 33 through 40 no longer happen, so their deadweight loss is gone.” DWL has already shrunk to zero as the tax rose; do not add a separate removal sweep.

> **3.c.** At the existing graph coordinates, build orange PS strips, then teal CS strips, then green government-revenue strips through Q = 32. Retain the tax label and dashed height measure at the price axis, clear of the welfare labels. Bottom: “Buyers pay $5.60, sellers receive $3.60, and the government collects $2 per unit.”

> **3.d.** “With a tax equal to the external cost, there is no deadweight loss.”

#### Trade the tax prevents

> **3.e.select → 3.e.values.** Select unit 36 with “Let's check an exchange that happened before the tax.” Carry its matching slices into C2's spread layout. MB $4.80; MC $3.80; pink EXT from $3.80 to MSC $5.80. Add the unit subtitle, people and bottom questions; no pink dollar measure.

> **3.e.prices.** Reveal Pb $5.60 above Ps $3.60, the named red price lines, and the middle green bar labeled tax spanning those prices.

> **3.e.buyer.** Teal shortfall bracket from MB $4.80 to Pb $5.60. “The buyer: value $4.80 against a price of $5.60.” No CS fill.

> **3.e.buyer.answer.** Reveal a red cross beside the teal buyer bracket and pause before introducing the seller.

> **3.e.seller.** Keep the buyer comparison; reveal the seller's orange shortfall bracket from Ps $3.60 to MC $3.80. “The seller: cost $3.80 against a price of $3.60.” No PS fill.

> **3.e.private.** Reveal a separate red cross beside the orange seller bracket, retaining the buyer’s cross. “Neither side wants this trade at these prices.”

> **3.e.social.compare → 3.e.social.** Dim the prices and transfer, dim private brackets but retain both red crosses, then measure MB–MSC on the right. Pause before the red cross / DWL and grey $4.80–$5.80 interval on the seller's stack, matching C1. “Good: this trade would have cost society $1.” This is potential harm prevented by the tax.

> **3.e.return.** Remove all close-up annotations and people; return the same slices and restore exactly the preceding market and subtitle.

#### Trade the tax preserves

> **3.f.select → 3.f.values → 3.f.prices.** Select unit 24 with “Let's check an exchange that still happens with the tax.” Same 0.68-scale spread layout, with the shorter subtitle “Unit 24: still exchanged.” to leave the tall value and its left projection clear: MB $7.20, MC $3.20, MSC $5.20; prices Pb $5.60 and Ps $3.60, green bar labeled tax between them. Seller-cost projections skip the Ps name as well as the price number.

> **3.f.buyer.** Grow teal CS from $5.60 to $7.20, labeled CS only; project the gain to a teal bracket on the left. “The buyer: value $7.20 against a price of $5.60.”

> **3.f.buyer.answer.** Reveal a green check beside the teal buyer bracket and pause before introducing the seller.

> **3.f.seller.** Grow orange PS from $3.20 to $3.60, labeled PS only; project the gain to an orange bracket on the left. “The seller: cost $3.20 against a price of $3.60.”

> **3.f.private.** Reveal a separate green check beside the orange seller bracket, retaining the buyer’s check. “Both sides want this trade at these prices.”

> **3.f.social.compare → 3.f.social.** Remove the private fills and dim prices; compare MB $7.20 with MSC $5.20 using the purple right-hand bracket. Pause before the green check / TS. “Good: this trade is worth $2 to society.” Do not add the government's transfer to welfare.

> **3.f.return.** Clear the close-up and restore the exact market and source slices.

#### Tax size

> **3.g.low.** Subtitle “Adjusting the tax around the $2 external cost.” Roll tax 2 → 1. Q = 36, Pb = $4.80, Ps = $3.80. Prices, filled wedge, quantity, individual CS/PS/GOV strips and label positions follow the tracker. Keep the green “Tax = $1” readout at the midpoint of the two prices; it moves left as the gap narrows to stay clear of the price labels. The thin uncapped dashed vertical height measure stays just left of the price axis. Grey DWL grows only over 32–36. Clip partially crossed units while moving. Bottom: “A smaller tax leaves some harmful exchanges in place.”

> **3.g.reset.** Return tax 1 → 2 and Q = 32. Bottom: “Back to the corrective tax: $2 per unit.”

> **3.g.high.** Roll tax 2 → 4. Q = 24, Pb = $7.20, Ps = $3.20. Grey DWL now represents worthwhile forgone units 24–32. Bottom: “A larger tax removes exchanges that were worth making.”

> **3.g.** Return tax 4 → 2. “The corrective tax equals the external cost: $2 per unit.”

> **3.g.summary.** Clear updaters, replace the moving tax readout with the fixed “Tax = $2” label at the same axis position, and move the existing graph left, keeping its geometry and dashed tax height measure. On the right, first show yellow “Tax = EXT”; below it, reveal a yellow downward implication arrow, “32 units” in muted grey, then red Qᵗᵃˣ = Q*. The grey quantity sits between the yellow statement and the red equality. Bottom: “A corrective tax prevents costly exchanges and preserves worthwhile ones.”

### 4 | Corrective subsidy

> **4.a.** Positive-externality recap in the same footprint, with price axis to 15. Title “Positive Externalities”; subtitle “Maximize society’s total welfare.” Show MB, MC and MSB without benefit/cost/externality fills; DWL is the only shaded area. MB and MSB stay teal, MC orange. Grey original-equilibrium dot at (40,4); yellow efficient dot at (48,4.4). Grey DWL strips represent forgone trades 41–48. Bottom: “Last time: the market exchanges 40 units, but 48 are efficient.”

> **4.b.** Return to “The Social Planner,” with subtitle “Maximize society’s total welfare.” Ask what price gets both sides to exchange 48 units. Clear the price label, DWL strips, and DWL label for the entire single-price experiment; retain the grey original-equilibrium dot and guides. Keep the aligned 40 / Q̂ and 48 / Q* readouts visible until the price experiment begins.

> **4.c.** Fade out the Q̂ and Q* readouts as the price starts rolling 4 → 2.40, before Qd and Qs appear. Keep the grey dot fixed at the original equilibrium throughout. Show Qd = 48, Qs = 8, shortage 40. “The price that works for buyers creates a shortage.”

> **4.d.** Roll price 2.40 → 4.40: Qs = 48, Qd = 38, excess 10. “The price that works for sellers creates excess supply.”

> **4.e.** Replace trial readouts with simultaneous Ps = $4.40 and Pb = $2.40 at Q = 48, with a yellow height measure on the vertical axis and $2 just to its left between the price labels. “One price cannot get both sides to the efficient quantity.”

> **4.f.** “The $2 gap between the prices is the external benefit per unit.”

> **4.g.start.** Title “Corrective Subsidies”; subtitle “A subsidy equal to the external benefit per unit.” Clear the planner's target-price guides and yellow gap measurement, and return to the actual no-subsidy market at Q = 40, P = $4. Restore eight grey DWL strips from 40 to 48, with the DWL label above them. Retain the original grey equilibrium dot and guides, dashed MSB, and the yellow efficient marker. Show one price label while buyers and sellers pay/receive the same price. Bottom: “Start at the market equilibrium, with no subsidy.”

> **4.g.prices.** Raise one subsidy tracker continuously from $0 to $2: Q = 40 + 4s, Ps = 4 + 0.2s, Pb = 4 − 0.8s. The two red price dots separate along MC and MB; horizontal price guides, axis prices, and the full-height quantity drop move with them. Replace the initial shared price label with separate Pb and Ps labels only when there is room. Keep quantity numbers on the existing axis row, with Qˢᵘᵇˢⁱᵈʸ beneath. Shrink the grey DWL strips from the moving quantity to 48, clipping the partially crossed strip rather than fading whole units. The DWL area is $0.125(48 − Q)², reaching zero at Q = 48. Bottom during motion: “As the subsidy rises, prices separate and deadweight loss shrinks.” Pause at Ps = $4.40, Pb = $2.40, Q = 48; replace the quantity symbol with Qˢᵘᵇˢⁱᵈʸ = Q*. Bottom: “A $2 subsidy brings quantity to 48 and eliminates deadweight loss.” No green wedge appears before this result.

> **4.g.wedge.** Only after the price result, reveal the narrow green bar between the two prices at Q = 48. Slide a copy OUT to the right, beyond the graph at Q-coordinate 88, retaining the original bar between the curves. Reveal “$2 subsidy” beside the extracted bar. Bottom: “The subsidy is the $2 gap between the sellers' and buyers' prices.” Pause so the wedge explains the price separation that has already happened.

> **4.g.** Clear the temporary right-hand illustration. Leave the original green bar at Q = 48, and show a dashed green height measure just left of the price axis spanning $2.40–$4.40, with “Subsidy = $2” just to its left. These final objects travel with the graph through the later close-up and conclusion. Quantity remains 48 on the number row, with Qˢᵘᵇˢⁱᵈʸ = Q* below it.

> **4.g.curve.** Mirror 3.a.curve over 48 units: green subsidy strips above MB cover pink EXT up to MSB; dashed MB + subsidy coincides with MSB. Crossfade to MSB = MB + subsidy. “A $2 subsidy lifts MB onto MSB: private and social benefits match.” Keep the prices and wedge; remove temporary strips/curve and restore MSB before 4.h.

> **4.h.** Keep the clean graph with the wedge at Q = 48. “The subsidy enables worthwhile trades that the market leaves out.” DWL has already shrunk to zero as the subsidy increased; do not reintroduce the old strips for a separate removal sweep.

#### Worthwhile trade the subsidy enables

> **4.h.select → 4.h.values.** Highlight unit 44 with “Let's check an exchange that would not have happened before the subsidy.” Carry its matching slices into the same layout: MB $3.20, pink EXT to MSB $5.20, MC $4.20. Questions and people stay in the same positions as the tax examples.

> **4.h.prices.** Reveal Ps $4.40 above Pb $2.40 and the middle green bar labeled subsidy between the prices.

> **4.h.buyer.** Grow teal CS $2.40–$3.20, labeled CS; project the gain to a teal bracket on the left. “The buyer: value $3.20 against a price of $2.40.”

> **4.h.buyer.answer.** Reveal a green check beside the teal buyer bracket and pause before introducing the seller.

> **4.h.seller.** Grow orange PS $4.20–$4.40, labeled PS without a dollar amount. Keep this small interval legible with its label immediately above the narrow fill and an orange comparison bracket on the left. “The seller: cost $4.20 against a price of $4.40.”

> **4.h.private.** Reveal the seller’s separate green check, retaining the buyer’s check: “Both sides want this trade at these prices.”

> **4.h.social.compare → 4.h.social.** Remove private fills and dim prices/transfer; compare MSB $5.20 to MC $4.20 using C1's purple bracket. Pause before the green check / TS. “Good: this trade is worth $1 to society.” The $2 subsidy is a transfer, distinct from the pink real benefit.

> **4.h.return.** Remove all close-up objects, return the source slices and restore the same graph and subtitle.

#### Subsidy welfare

> **4.i.cs → 4.i.ps → 4.i.gov.** Show CS, PS and government spending as individual vertical strips at existing coordinates. These areas overlap, so show them one at a time, removing each before the next. Bottom after the spending reveal: “Buyers pay $2.40, sellers receive $4.40, and the government pays $2 per unit.”

> **4.i.** Remove the spending bars and their label. “With a subsidy equal to the external benefit, there is no deadweight loss.”

### 5 | End on the corrected market

> **5.a.** Move the same clean subsidy graph left. On the right, first show yellow “Subsidy = EXT”; below it, reveal a yellow downward implication arrow, “48 units” in muted grey, then red Qˢᵘᵇˢⁱᵈʸ = Q*. The grey quantity sits between the yellow statement and the red equality. Bottom: “A corrective subsidy enables worthwhile exchanges the market would miss.” Match the tax conclusion's spacing and staged reveal in 3.g.summary: the policy equals the externality, implying that the market quantity equals the efficient quantity.

<!-- Validation 2026-10-12: complete scene run produced 153 checkpoint images. Reviewed the graph, planner, close-up, tax-dial, subsidy and conclusion frames. Final targeted renders and backward checkpoint restoration passed; checked price/quantity arithmetic, highest dot layers, fractional strip clipping, zero orphan slices/subtitles after all three returns, and subsidy-spending cleanup. Development viewer navigation also reviewed. Exports remain temporary review artifacts, not the published student bundle. -->

<!-- Validation 2026-10-14: complete scene run and 67 unique literal pause IDs pass. Reviewed 44 restored checkpoints, including backward visits, individual buyer/seller verdict timing, all three close-up returns, both curve-overlap beats, tax-dial labels and conclusions. Sampled six zoom/return transitions, four surplus-fill growth animations, two strip sweeps and four tax-dial transitions. Verified C1 social arithmetic, names-only welfare labels, transfers between prices, fixed exchange questions, both private verdicts persisting through the social comparison, and no orphan close-up objects/subtitles. A final targeted render checks the 24th-unit subtitle and Ps-label clearance. The dashed tax measurement recovers after zero. Syntax, diff whitespace and the notes parser pass; import/export has no warnings. Review renders remain temporary, outside repository media. -->
