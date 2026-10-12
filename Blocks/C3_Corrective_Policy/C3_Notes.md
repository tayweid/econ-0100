---
margin: {top: 1in, right: 0.5in, bottom: 1in, left: 0.5in}
---

## Episode C3 | *Correcting Market Failures*

<!--
Animation storyboard for C3_Animations.py, scene C3. Built 2026-10-09 as a new set of animations; the older 03_Code.py and the archived notebooks are untouched. Taylor’s notes from 01_Notes.typ are carried over below exactly as Plass exports them; the quote blocks under the numbered sections are animation directions, not replacement prose.
References: C1_Animations.py (the market, the exchange close-ups with spheres, MSC, the Q-star search, the DWL bars, the positive-externality graph); the new C2_Animations.py built the same day (its green ticked wedge, \$2 tax and \$2 subsidy labels, Tax revenue and Subsidy cost labels, red dots at the wedge ends, and its subsidy wedge sliding in from the right are matched here, since C3 follows C2); the archived C2 Taxes animation (Tutorial 3.5: the tax wedge slid in from the left, buyer and seller prices, CS, PS, GOV and DWL); the archived C3 Corrective Policies animation (Tutorial 4.2: excess and shortage at the two candidate prices, then a tax equal to the externality, then the tax dialed above and below it; the subsidy mirror).
Model: C1’s market. MB = 12 − Q/5, MC = 2 + Q/20, Q in tons, dollars per ton. Negative example: constant external cost 2 per ton, MSC = 4 + Q/20, Q-hat = 40, P-hat = 4, Q-star = 32, MB(32) = MC(32) + 2 = 5.60, MC(32) = 3.60. Corrective tax 2 per ton: P_b = 5.60, P_s = 3.60, Q = 32, revenue 64, no DWL. A tax t gives Q = 40 − 4t. Positive example: external benefit 2 per ton, MSB = 14 − Q/5, Q-star = 48, MB(48) = 2.40, MC(48) = 4.40. Corrective subsidy 2 per ton: P_s = 4.40, P_b = 2.40, Q = 48, spending 96, no DWL. Close-ups use C1’s unit values: ton 36 has MB 4.80, MC 3.80, MSC 5.80; ton 24 has MB 7.20, MC 3.20, MSC 5.20.
Axes: Q from 0 to 80 so the excess at the buyers’ price (Q_s = 72) fits; P from 0 to 13 on the tax graph and 0 to 15 on the subsidy graph. One-ton slices keep C1’s width and gap.
Conventions: topic titles in azure with every word capitalized; optional grey CMU Sans subtitles 0.10 below; the whole teaching line yellow in the bottom strip at the fixed size. Price readouts sit on the vertical axis; an intercept numeral leaves the axis while a rolling price label needs that spot. The wedge is C2’s GOV-green vertical segment with small end ticks, parked off the graph and slid in until it is stuck between the curves (from the left for the tax, from the right for the subsidy), with its green label floating above it; its ends then get red dots and red dashed guides to the axis with P_b above and P_s below, and a red Q readout under the axis with the yellow Q-star label staggered beneath. The red Q-hat guide and label, the yellow Q-star label and the DWL word leave when the planner’s price experiments start, so the rolling Q_d and Q_s readouts have the strip to themselves; the dot and the Q-star label come back with the two prices. GOV revenue and spending are green fills; CS teal, PS orange, EXT pink, DWL grey one-ton bars, never a merged triangle. Spheres are opaque with depth testing, added and removed directly. Numbers that change roll on trackers, and a rolled number is updated before it fades in (the engine crashes if its digits change mid-fade).
Verified 2026-10-09 with maniml --export-checkpoints (136 frames, one per play and pause); the frames were reviewed against this storyboard.
Not built: a Last-time card or a production bumper other than the shared one in 0.a; the subsidy dial (the tax dial in 3.g carries the equal-to lesson); a subsidy close-up; price incidence and revenue arithmetic beyond the on-graph labels (Skillsheet C3.1 does not require them).
-->

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

### 0 | Bumper

<!-- 0.a · Shared raster bumper, Part C | Episode 3, thesis line “We can offset the problems of externalities with the problems of taxes.” -->

> 0.a · The shared MICROECONOMICS raster and flicker, then Part C | Episode 3 beneath it, then the italic thesis from the notes header in grey: We can offset the problems of externalities with the problems of taxes. Pause, fade everything, clear.

### 1 | Last time: the market failure

<!-- 1.a · Title “Negative Externalities”, subtitle “A cost paid by others outside the market.” Bottom “Last time: the market exchanges 40 tons, but only 32 are efficient.” -->

> 1.a · Title: Negative Externalities. Subtitle: A cost paid by others outside the market. Rebuild C1’s final negative-externality market on wider axes, Q from 0 to 80 and P from 0 to 13: MB from (0, 12) to (60, 0), MC from (0, 2) to (80, 6), solid MSC from (0, 4) to (80, 8), white labels MB, MC, MSC at the curve ends, intercepts 12 teal, 2 orange, and 4 orange with red P-hat = immediately before it. Faint orange cost slices under MC for tons 1 to 40; pink EXT strips between MC and MSC, strong through ton 40 and faint through ton 60. Red Q-hat = 40 with its dot and dashed guides. Yellow dashed guide, dot, and Q-star = 32 label staggered below the Q-hat label. Eight separate grey DWL bars for tons 33 to 40 between MB and MSC, labeled DWL. Bottom: Last time: the market exchanges 40 tons, but only 32 are efficient. Pause.

### 2 | The social planner’s problem

<!--
2.a · Title “The Social Planner”, subtitle “Someone who wants the efficient quantity, 32 tons.” Bottom “What price gets buyers and sellers to exchange 32 tons?”
2.b · Price rolls 4 → 5.60; Q_d = 32 and Q_s = 72 under the axis (Q_s one step lower), grey excess segment. Bottom “At \$5.60, buyers want 32 tons but sellers offer 72: an excess of 40.”
2.c · Price rolls 5.60 → 3.60; Q_s = 32, Q_d = 42, grey shortage segment. Bottom “At \$3.60, sellers offer 32 tons but buyers want 42: a shortage of 10.”
2.d · Both prices on the axis, yellow \$2 gap at Q = 32. Bottom “No single price works: buyers must pay \$5.60 while sellers receive \$3.60.”
2.e · Gap pulses. Bottom “The \$2 gap between the prices is the external cost per ton.”
-->

> 2.a · Title: The Social Planner. Subtitle: Someone who wants the efficient quantity, 32 tons. Keep the market, the DWL bars, the red market dot and the yellow Q-star guide; fade the P-hat guide and label, the orange 4, the Q-hat drop and label, the Q-star label and the DWL word, because a trial price and its readouts are about to move. Bottom: What price gets buyers and sellers to exchange 32 tons? Pause.

> 2.b · Roll one price tracker from 4 up to 5.60 (the buyers’ willingness to pay for ton 32): a red dashed price line from the axis, a red P readout on the vertical axis that rolls, a red dot on MB at Q_d and a red dot on MC at Q_s, each with a dashed drop to the horizontal axis. The part of the price line between the two dots is a solid grey segment. After the roll, reveal Q_d = 32 and Q_s = 72 in red under their drops (the supply readout one step lower, so the two never collide) and the grey caption excess: 40 tons above the segment. Bottom: At \$5.60, buyers want 32 tons but sellers offer 72: an excess of 40. Pause.

> 2.c · Clear the caption and roll the price down to 3.60 (the sellers’ willingness to sell ton 32); the readouts roll with it, Q_s to 32 and Q_d to 42. Caption shortage: 10 tons below the segment, over the faint cost slices. Bottom: At \$3.60, sellers offer 32 tons but buyers want 42: a shortage of 10. Pause.

> 2.d · Remove the dots, drops, caption, and quantity readouts. Show both prices at once as red dashed guides from the axis to Q = 32, labeled P_b = 5.60 and P_s = 3.60 on the vertical axis; restore the market dot and the Q-star label. Mark the gap at Q = 32 with a yellow FOCUS measure from 3.60 to 5.60 labeled \$2. Bottom: No single price works: buyers must pay \$5.60 while sellers receive \$3.60. Pause.

> 2.e · Pulse the yellow measure once. Bottom: The \$2 gap between the prices is the external cost per ton. Pause.

### 3 | Corrective taxes

<!--
3.a · Title “Corrective Taxes”, subtitle “A tax equal to the external cost per ton.” Green wedge “\$2 tax” slides in from the left and sticks at 32; red P_b = 5.60, P_s = 3.60, Q = 32. Bottom “A \$2 tax separates the buyers’ price from the sellers’ price by \$2.” then “The wedge gets stuck at 32 tons, the efficient quantity.”
3.b · Tons 33 to 40 dim; DWL bars fade. Bottom “Exchanges 33 through 40 no longer happen, so their deadweight loss is gone.”
3.c · PS, CS and Tax revenue fills with labels. Bottom “With the tax, who gains and who pays?” then “Buyers pay \$5.60, sellers receive \$3.60, and the government collects \$2 per ton.”
3.d · Bottom “With a tax equal to the external cost, there is no deadweight loss.”
3.e.select → 3.e.values → 3.e.external → 3.e.tax → 3.e.question → 3.e.answer → 3.e → 3.e.return · Ton 36 close-up, subtitle “The 36th unit: an exchange the tax stops.” Bottom lines in order: “Buyers and sellers only consider their private costs and benefits.”, “With the tax, the seller needs at least \$5.80 to sell this ton.”, “Is there a price that would make this exchange work?”, “No price works: the buyer pays at most \$4.80 but the seller needs \$5.80.”, “The tax stops this exchange and eliminates \$1 of deadweight loss.”
3.f.select → 3.f.values → 3.f.external → 3.f.tax → 3.f.question → 3.f.answer → 3.f.social → 3.f → 3.f.return · Ton 24 close-up, subtitle “The 24th unit: an exchange the tax keeps.” Bottom lines in order: “Buyers and sellers only consider their private costs and benefits.”, “With the tax, the seller needs at least \$5.20 to sell this ton.”, “Is there a price that would make this exchange work?”, “Yes: the buyer’s \$7.20 covers the seller’s \$5.20, so this exchange continues.”, “Counting the bystanders, this exchange is still worthwhile: MB exceeds MSC.”
3.g.low → 3.g.high → 3.g · Tax dial 2 → 1 → 4 → 2. Bottom “What if the tax is smaller than the external cost?”, “A smaller tax leaves some harmful exchanges in place.”, “What if the tax is larger than the external cost?”, “A larger tax removes exchanges that were worth making.”, “The corrective tax equals the external cost: \$2 per ton.”
-->

> 3.a · Title: Corrective Taxes. Subtitle: A tax equal to the external cost per ton. Fade the two price guides and the yellow measure. Park C2’s green (GOV) ticked segment two dollars tall left of the axes, centered on 4.60 so its ends already sit at 5.60 and 3.60, labeled \$2 tax above it. Bottom: A \$2 tax separates the buyers’ price from the sellers’ price by \$2. Slide the segment horizontally in one eased play until it is stuck between MC and MB at Q = 32. Then fade in red dots at its ends and red dashed guides from them to the vertical axis with P_b = 5.60 above and P_s = 3.60 below, and a red dashed drop with Q = 32 under the axis; Q-star = 32 stays staggered beneath it. Bottom: The wedge gets stuck at 32 tons, the efficient quantity. Pause.

> 3.b · Dim the cost slices and EXT strips for tons 33 to 40 and fade the eight grey DWL bars and their label. Bottom: Exchanges 33 through 40 no longer happen, so their deadweight loss is gone. Pause.

> 3.c · Bottom: With the tax, who gains and who pays? Fade the remaining pink EXT strips to faint so the fills read cleanly. Reveal, one play each: orange PS between MC and P_s for tons 1 to 32 with a white PS label at its centroid; teal CS between P_b and MB with CS; green revenue between P_s and P_b labeled Tax revenue. Bottom: Buyers pay \$5.60, sellers receive \$3.60, and the government collects \$2 per ton. Pause.

> 3.d · Bottom: With a tax equal to the external cost, there is no deadweight loss. Pause.

> 3.e · Select ton 36 from the existing market slices (cost, EXT, and the buyer’s demand edge) with one thin yellow outline box; pause with no bottom text. Carry that pair into the canonical close-up, centered a little left of the stage so the detached cost fits at right, as the market fades: faint buyer bar to MB 4.80, faint seller bar to MC 3.80 with the filled pink EXT 2 on top reaching MSC 5.80, hard value edges, labels beside their edges, teal buyer and orange seller spheres with one grey Bystanders sphere between them and names beneath. Subtitle: The 36th unit: an exchange the tax stops. Pause on the values. Move the EXT rectangle and the grey sphere to the right as in C1, under the grey heading Externalized cost per ton with just 2 in pink, with the bottom line Buyers and sellers only consider their private costs and benefits. Pause. Add a green tax bar on the seller column from 3.80 to 5.80, labeled Tax \$2 beside it and MC + Tax \$5.80 at its top edge. Bottom: With the tax, the seller needs at least \$5.80 to sell this ton. Pause. Bottom: Is there a price that would make this exchange work? Pause. Bottom: No price works: the buyer pays at most \$4.80 but the seller needs \$5.80. Show MB < MC + Tax to the left of the buyer bar. Pause. Clear that comparison, shade the seller column between 4.80 and 5.80 grey, and reveal the grey loss gap left of the MB label with TS = −\$1 in purple and DWL = \$1 in white. Bottom: The tax stops this exchange and eliminates \$1 of deadweight loss. Pause. Remove the people directly, fade the close-up labels, and carry the pair back to its market slice as the market and subtitle return. Pause.

> 3.f · Select ton 24 the same way. Close-up on the smaller common scale that keeps MB 7.20 below the subtitle: MB 7.20, MC 3.20, EXT 2 reaching MSC 5.20. Subtitle: The 24th unit: an exchange the tax keeps. Pause on the values. Move EXT and the bystander aside with the private-costs line; pause. Green tax bar on the seller column from 3.20 to 5.20, Tax \$2, MC + Tax \$5.20. Bottom: With the tax, the seller needs at least \$5.20 to sell this ton. Pause. Bottom: Is there a price that would make this exchange work? Pause. Bottom: Yes: the buyer’s \$7.20 covers the seller’s \$5.20, so this exchange continues. Show MB > MC + Tax. Pause. Fade the tax bar and its labels, bring the EXT rectangle and the bystander back onto MC, and restore EXT 2 and MSC 5.20. Bottom: Counting the bystanders, this exchange is still worthwhile: MB exceeds MSC. Shade the buyer’s benefit above MSC teal and show TS = \$2 in purple and DWL = \$0 in white beside the purple gap guides. Pause. Return to the market as before. Pause.

> 3.g · Swap the static tax layer for a live one on a tax tracker: the wedge and its end dots sit at Q = 40 − 4t between MC and MB with \$t.tt tax above it, the P_b, P_s, and Q readouts roll, the PS, CS, and GOV fills follow the traded tons, cost slices light only through the traded quantity, and grey one-ton DWL bars appear between the traded quantity and 32: between MB and MSC for traded tons past 32, and between MSC and MB for forgone tons short of 32. The white DWL word sits right of the traded tons when the tax is small and above the curves just past Q-star when it is large, and hides within a ton of 32. Bottom: What if the tax is smaller than the external cost? Roll the tax from 2 to 1 in one play; Q = 36, four DWL bars return. Bottom: A smaller tax leaves some harmful exchanges in place. Pause. Bottom: What if the tax is larger than the external cost? Roll from 1 to 4; Q = 24, eight DWL bars between 24 and 32. Bottom: A larger tax removes exchanges that were worth making. Pause. Roll back to 2. Bottom: The corrective tax equals the external cost: \$2 per ton. Pause.

### 4 | Corrective subsidies

<!--
4.a · Title “Positive Externalities”, subtitle “A benefit received by others outside the market.” Bottom “Last time: the market exchanges 40 tons, but 48 are efficient.”
4.b · Title “The Social Planner”, subtitle “Someone who wants the efficient quantity, 48 tons.” Bottom “What price gets buyers and sellers to exchange 48 tons?”
4.c · Price rolls 4 → 2.40; shortage 40. Bottom “At \$2.40, buyers want 48 tons but sellers offer 8: a shortage of 40.”
4.d · Price rolls 2.40 → 4.40; excess 10. Bottom “At \$4.40, sellers offer 48 tons but buyers want 38: an excess of 10.”
4.e · Both prices, yellow \$2 gap at Q = 48. Bottom “No single price works: sellers must receive \$4.40 while buyers pay \$2.40.”
4.f · Bottom “The \$2 gap between the prices is the external benefit per ton.”
4.g · Title “Corrective Subsidies”, subtitle “A subsidy equal to the external benefit per ton.” Green wedge “\$2 subsidy” slides in from the right and sticks at 48; P_s = 4.40, P_b = 2.40, Q = 48. Bottom “A \$2 subsidy puts the sellers’ price \$2 above the buyers’ price.” then “The wedge gets stuck at 48 tons, the efficient quantity.”
4.h · Tons 41 to 48 light up; DWL bars fade. Bottom “Exchanges 41 through 48 now happen, so their deadweight loss is gone.”
4.i.cs → 4.i.ps → 4.i.gov → 4.i · CS alone, PS alone, Subsidy cost alone. Bottom “With the subsidy, who gains and who pays?”, “Buyers pay \$2.40, sellers receive \$4.40, and the government pays \$2 per ton.”, “With a subsidy equal to the external benefit, there is no deadweight loss.”
-->

> 4.a · Clear the stage. Title: Positive Externalities. Subtitle: A benefit received by others outside the market. Rebuild C1’s positive-externality market on the same wide axes with P from 0 to 15: MB, solid teal MSB from (0, 14) to (70, 0) with its teal intercept 14, MC, faint cost slices through ton 60 (stronger through 40), pink EXT strips above MB (strong through 40, faint through 60), red Q-hat = 40 and P-hat = 4, yellow Q-star = 48, eight grey DWL bars for tons 41 to 48 between MC and MSB, labeled DWL above them. Bottom: Last time: the market exchanges 40 tons, but 48 are efficient. Pause.

> 4.b · Title: The Social Planner. Subtitle: Someone who wants the efficient quantity, 48 tons. Fade the P-hat guide and label, the orange 2, the Q-hat drop and label, the Q-star label and the DWL word. Bottom: What price gets buyers and sellers to exchange 48 tons? Pause.

> 4.c · Roll the price from 4 down to 2.40 (the buyers’ willingness to pay for ton 48) with the same readouts and dots as 2.b; the grey segment between the dots now reads shortage: 40 tons, from Q_s = 8 to Q_d = 48. Bottom: At \$2.40, buyers want 48 tons but sellers offer 8: a shortage of 40. Pause.

> 4.d · Roll the price up to 4.40 (the sellers’ willingness to sell ton 48): Q_s = 48, Q_d = 38, caption excess: 10 tons. Bottom: At \$4.40, sellers offer 48 tons but buyers want 38: an excess of 10. Pause.

> 4.e · Both prices as red dashed guides to Q = 48: P_s = 4.40 above and P_b = 2.40 below on the vertical axis, with the yellow \$2 measure at Q = 48 between them. Bottom: No single price works: sellers must receive \$4.40 while buyers pay \$2.40. Pause.

> 4.f · Pulse the measure. Bottom: The \$2 gap between the prices is the external benefit per ton. Pause.

> 4.g · Title: Corrective Subsidies. Subtitle: A subsidy equal to the external benefit per ton. Fade the guides and measure. Park the green ticked segment two dollars tall to the right of the curves at Q = 66, centered on 3.40, labeled \$2 subsidy above it. Bottom: A \$2 subsidy puts the sellers’ price \$2 above the buyers’ price. Slide it left, as C2 did, until it is stuck between MC above and MB below at Q = 48. Red end dots, dashed guides and labels P_s = 4.40 above, P_b = 2.40 below, and Q = 48 under the axis with Q-star = 48 staggered beneath. Bottom: The wedge gets stuck at 48 tons, the efficient quantity. Pause.

> 4.h · Light the cost slices and EXT strips for tons 41 to 48 to full strength and fade the eight grey DWL bars and their label. Bottom: Exchanges 41 through 48 now happen, so their deadweight loss is gone. Pause.

> 4.i · Bottom: With the subsidy, who gains and who pays? Fade the EXT strips to faint. Because the subsidy regions overlap, show them one at a time: teal CS between P_b and MB for tons 1 to 48 with its label, pause, fade; orange PS between MC and P_s with its label, pause, fade; green spending between P_b and P_s labeled Subsidy cost, with the bottom line Buyers pay \$2.40, sellers receive \$4.40, and the government pays \$2 per ton, pause, fade. Bottom: With a subsidy equal to the external benefit, there is no deadweight loss. Pause.

### 5 | Corrective policy

<!-- 5.a · Title “Corrective Policy”. Principle line from the notes: “A tax or subsidy equal to the externality sets Q_s = Q_d = Q*.” -->

> 5.a · Clear the stage. Title: Corrective Policy. One principle line at body size, centered, from the notes’ fourth storyboard point: A tax or subsidy equal to the externality sets $Q_s = Q_d = Q^*$. Pause.
