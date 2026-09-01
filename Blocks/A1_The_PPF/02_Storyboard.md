# Episode A1 | *The space of what's possible* — Storyboard (v2, 2026-08-24)

Source: `01_Notes.md`. Code: `03_Code.py`, one scene `EpisodeA1` with one flat `construct()`;
every `# Bxx` section is self-contained — it clears the previous beat's objects, builds its own,
and ends at the `self.pause()` the viewer parks on before the next section. Pauses are unnamed;
each sits under a `# Bxx` header, and the beat ids below match those headers, listed in scene
order. No `wait()`s: pacing comes from the pauses. Render: `maniml 03_Code.py EpisodeA1 --render`.
Everything in the code is `anim`; the talking-head (`cam`) gaps are the pool-table/toy-model
paragraph (between B04 and B05) and the closing paragraphs (between B25 and B30 — "So what's
happened here…" through "In Closing") — no code runs there.

**Settled 2026-08-24 — axis orientation.** This episode runs carrots **horizontal**, spinach
**vertical**, so the board equation `S = 40 − 4C` is literally the graph (x = C, y = S) and the
live readout reads `(C, S)`. `01_Notes.md` and `03_Code.py` (via `Video.py`'s `PPF_Function`
family) agree on this. It's a deliberate divergence from the style guide §4 invariant "spinach
horizontal, carrots vertical" for Part A — the guide should eventually update to match; that's a
separate task, not blocking this episode.

## The visual spine

Two recurring objects carry the episode.

**Molly's farm** (`farm`/`farm_name`, crop rectangles `carrots`/`spinach`): a rectangle on the
left whose carrot/spinach fill split IS the crop choice — changing the split is the only way
anything moves. It drives a live `(C, S)` readout dot (updaters on `c_num`/`s_num`, cleared once
the PPF is drawn) that the walked points feed into, narrows for the labor cut (B22), and gets
stamped `+ Better Carrot Tech` for the pivot (B23).

**The graph** on the right (`axes`/`ppf_graph`, carrots horizontal / spinach vertical) grows out
of the farm: the walked points (B10b–B11c) become the PPF (B12), the PPF equation and slope live
on it (B13–B13d), and the Attainability stage (B20–B24c) rebuilds farm + big axes + PPF + ghost
together to show the attainable region and its shifts.

Second device: cut-to-exercise cards (`exercise_card()` — dim overlay + gold question) at three
points, interleaving Exercise_F26 Q1–Q3 so students build Hagrid's PPF themselves before/after
each Molly reveal. Titles are screen titles, top-left (`style.title`); no notes panel.

| script idea | what the farm/graph does |
|---|---|
| opportunity cost of 1 carrot | farm split walked to the two extremes (B05b/B05c), then divided down to 1 C = 4 S (B06–B07) |
| the PPF is built from crop choices | farm split walked point by point — (10,0)→(0,40)→(5,20)→(6,16)→(3,28) (B10b–B11c) — then the line draws and the farm fills Molly-blue (B12) |
| slope = opportunity cost = marginal cost | triangle on the line, +1 C across / −4 S down from (4,24) (B13b), the OC line returns (B13c), then transforms into Marginal Cost (B13d) |
| inefficient / efficient / unattainable | all three named at one picture over the same farm+axes (B20b–B20d) |
| labor cut vs. tech gain | endpoint dots slide 10C→8C / 40S→32S as the farm narrows (B22), the frontier catches up (B22b), then pivots out to 16 C (B23b), leaving a gold "?" sliver (B24c) |

## Beats

| # | Script cue | Mode | Action | Status |
|---|-----------|------|--------|--------|
| B01 | (cold open) | anim | Bumper: raster MICROECONOMICS fades in | [ok] |
| B01b | — | anim | Flicker, blues cycling | [ok] |
| B01c | — | anim | `Part A \| Episode 1` joins under the wordmark; episode-thesis line *The space of what's possible* fades in below | [ok] |
| B02 | (silent — the Show note places this before the paragraph starts) | anim | `Last Time...` card | [ok] |
| B03 | "Last time we talked about preferences and scarcity, and that together we need to make choices that carry tradeoffs…" | anim | `Opportunity Cost` title; `A or B` with green/red choice boxes (A0 recap) | [ok] |
| B03b | (same clause, cont.) | anim | `Opportunity Cost(A) = B` writes in | [ok] |
| B03c | "…which we measure using opportunity cost." | anim | boxes and equation flip to `Opportunity Cost(B) = A` | [ok] |
| B04 | "…we define opportunity cost as the value of the next best use of your resources, where we find the value of the best thing we didn't pick." | anim | definition card | [ok] |
| B05 | "Imagine Molly, a small scale organic farmer, is good at growing spinach and carrots on her 100 hectare farm." | anim | Molly's farm outline + name | [ok] |
| B05b | "If she spends all her time growing spinach she can grow 40 tons per year." | anim | farm fills spinach-green; `40 S` slides right | [ok] |
| B05c | "If instead she spends all her time growing carrots, she can grow 10 tons per year." | anim | farm flips to carrot-orange; `or` and `10 C` slide in | [ok] |
| B06 | "What is Molly's opportunity cost for 1 ton of carrots? To find it, we set those two production values equal…" | anim | `or` → `=`; camera zooms in on the equation | [ok] |
| B06b | "…and simplify." | anim | both sides divide by 10 (`10/10 C` = `40/10 S`) | [ok] |
| B06c | "And that's it. Molly's opportunity cost of 1 unit of carrots is 4 units of spinach." | anim | reduces to `1 C` = `4 S`; farm fades out | [ok] |
| B07 | "For every 1 unit of carrots she wants to grow, she'll have to give up 4 units of spinach." | anim | `Opportunity Cost(1 C) = 4 S` writes above | [ok] |
| B10 | "Let's use an x,y graph to plot how much of each crop model is harvesting… We've already established that she can harvest 10 tons of carrots and 0 tons of spinach, or 0 tons of carrots and 40 tons of spinach." | anim | axes (carrots horizontal, spinach vertical) + farm return; live `(C, S)` readout dot at the all-carrots point (10, 0) | [ok] |
| B10b | (second extreme, same sentence) | anim | farm/dot walk to the all-spinach point (0, 40) | [ok] |
| B11 | "…if Molly plants carrots on half her land and spinach on the other half, she would have half of 10 tons of carrots and half of 40 tons of spinach." | anim | farm/dot walk to the half-split point (5, 20) | [ok] |
| B11b | "…splitting the land into 3/5 carrots and 2/5 spinach." | anim | farm/dot walk to the 3/5-carrots point (6, 16) | [ok] |
| B11c | "I'm going to run through a few more on screen." | anim | farm/dot walk to a fourth point (3, 28) | [ok] |
| B12 | "…any carrot and spinach combination Molly chooses lies on a line which we call the Production Possibility Frontier (PPF)." | anim | PPF line draws (`S = 40 − 4C`); farm fills Molly-blue; title becomes *Molly's Production Possibility Frontier* | [ok] |
| B13 | "…The slope of the PPF tells us her opportunity cost." | anim | `S = 40 − 4C` writes on the graph | [ok] |
| B13b | "To harvest 1 more unit of carrots Molly must harvest 4 fewer units of spinach." | anim | slope triangle from (4, 24): `+1 C` across, `−4 S` down; box around the `−4` coefficient | [check] |
| B13c | (same board moment, cont.) | anim | `Opportunity Cost(1 C) = 4 S` returns under the equation | [ok] |
| B13d | — | — | *cut 2026-08-25: the Marginal Cost christening is out of the session; the OC line stays* | [cut] |
| B14 | "***Cut to Exercise A1 \| Q1.***" | anim | Exercise card: Hagrid's PPF, 20 R / 30 F, opportunity cost of each good | [check] |
| B20 | "Molly's PPF shows us all the combinations of carrots and spinach that she can produce…" | anim | title *Attainability*; farm + big axes + PPF + ghost PPF return | [ok] |
| B20b | "Is it ever possible to produce at a point just inside the PPF like this?" | anim | attainable region fills; `Inefficient` dot + label at (4, 16) | [ok] |
| B20c | (trio, named together at the same picture) | anim | `Efficient` dot + label at (6, 16) | [ok] |
| B20d | (trio, named together) | anim | `Unattainable` dot + label at (8, 28) | [ok] |
| B21 | "***Cut to Exercise A1 \| Q2.***" | anim | Exercise card: is 30 R / 20 F inefficient, efficient, or unattainable? | [ok] |
| B22 | "…Her productive capacity has dropped to either 8 carrots or 32 spinach." | anim | trio + attainable region fade; endpoint dots fade in at (10,0)/(0,40) and slide to (8,0)/(0,32) as the farm's planted band narrows to 4/5 | [ok] |
| B22b | "The rest of the points along the PPF have shifted in with the extreme points." | anim | frontier transforms to the new (labor-cut) endpoints; the two endpoint dots fade out | [ok] |
| B23 | "…a new carrot harvesting technology that would double her carrot harvest but not improve her spinach harvest. What happens to Molly's PPF after this new technology?" | anim | `+ Better Carrot Tech` stamps the farm, held as a question | [ok] |
| B23b | "…she's able to grow up to 16 carrots… We see a pivot out of the PPF." | anim | labor-cut PPF ghosts grey; new PPF pivots out to (16, 0) | [ok] |
| B24 | "…a region that used to be inefficient that is now unattainable." | anim | grey region (s1, s0, g) + `No longer attainable` label | [check] |
| B24b | "And a region that used to be unattainable that is now on the frontier." | anim | pink region (c0, c2, g) + `Newly attainable` label | [ok] |
| B24c | (the sliver lost to the labor cut and regained by the tech — left as a question) | anim | gold sliver (c0, c1, s1, g) + `?` | [ok] |
| B25 | "***Cut to Exercise A1 \| Q3.***" | anim | Exercise card: Hagrid halves his time, then a revolution doubles efficiency — show both changes | [ok] |
| B30 | "…we can actually do better." (after the closing cam paragraphs) | anim | punchline card | [ok] |
| B31 | "Showing how we do this requires some mathematics and a small detour into 1800s economic history…" | anim | title *Next time…*; `A detour into 1800s economic history.` framebox reveal; runs to black | [ok] |

## Pausepoints (2026-08-24)

37 `self.pause()` calls for 40 section headers: B01 and B01b have no pause of their own — the
bumper raster, flicker, part label, and thesis line all play before the first stop, which lands
under `# B01c`. B31 has no pause either — it runs to black, same as A0's closing beat.

| stop | press on |
|---|---|
| (scene start) | cold open; first press = bumper raster, flicker, part label + thesis (B01, B01b, B01c play before the first stop) |
| B01c | thesis line settles under the part label; holds until the `Last Time...` card |
| B02 | (silent) `Last Time...` card |
| B03 | "Last time we talked about preferences and scarcity…" (title + A-or-B recap) |
| B03b | (same clause) `Opportunity Cost(A) = B` writes in |
| B03c | "…which we measure using opportunity cost." (boxes + equation flip) |
| B04 | "…the value of the next best use of your resources…" (definition card) |
| B05 | "Imagine Molly, a small scale organic farmer…" (after the pool-table cam stretch; farm appears) |
| B05b | "If she spends all her time growing spinach she can grow 40 tons per year." |
| B05c | "If instead she spends all her time growing carrots, she can grow 10 tons per year." |
| B06 | "…we set those two production values equal…" (or → =; camera zooms in) |
| B06b | "…and simplify." (divide by 10) |
| B06c | "And that's it. Molly's opportunity cost of 1 unit of carrots is 4 units of spinach." (reduces to 1 C = 4 S) |
| B07 | "For every 1 unit of carrots she wants to grow, she'll have to give up 4 units of spinach." |
| B10 | "Let's use an x,y graph to plot…" (axes + farm return; readout dot at (10, 0)) |
| B10b | "…0 tons of carrots and 40 tons of spinach." (walk to (0, 40)) |
| B11 | "…if Molly plants carrots on half her land…" (walk to (5, 20)) |
| B11b | "…splitting the land into 3/5 carrots and 2/5 spinach." (walk to (6, 16)) |
| B11c | "I'm going to run through a few more on screen." (walk to (3, 28)) |
| B12 | "…any carrot and spinach combination Molly chooses lies on a line…" (PPF draws; farm fills Molly-blue) |
| B13 | "…The slope of the PPF tells us her opportunity cost." (`S = 40 − 4C` writes) |
| B13b | "To harvest 1 more unit of carrots Molly must harvest 4 fewer units of spinach." (slope triangle from (4, 24)) |
| B13c | (same board moment) OC line returns |
| B14 | "***Cut to Exercise A1 \| Q1.***" |
| B20 | "Molly's PPF shows us all the combinations…" | 
| B20b | "Is it ever possible to produce at a point just inside the PPF like this?" (attainable region; `Inefficient` dot) |
| B20c | (trio, named together at the same picture) `Efficient` dot |
| B20d | (trio, named together) `Unattainable` dot |
| B21 | "***Cut to Exercise A1 \| Q2.***" |
| B22 | "…Her productive capacity has dropped to either 8 carrots or 32 spinach." (endpoint dots slide; farm narrows) |
| B22b | "The rest of the points along the PPF have shifted in with the extreme points." (frontier transforms; dots fade) |
| B23 | "…a new carrot harvesting technology… What happens to Molly's PPF after this new technology?" (`+ Better Carrot Tech` stamp, held as a question) |
| B23b | "…she's able to grow up to 16 carrots… We see a pivot out of the PPF." |
| B24 | "…a region that used to be inefficient that is now unattainable." |
| B24b | "And a region that used to be unattainable that is now on the frontier." |
| B24c | (the sliver, left as a question) gold `?` |
| B25 | "***Cut to Exercise A1 \| Q3.***" |
| B30 | "…we can actually do better." (after the closing cam paragraphs; punchline card) |
| B31 | "Showing how we do this requires some mathematics…" (`Next time...` framebox: "A detour into 1800s economic history."; final section, runs to black) |

## Stage-direction edits made in `01_Notes.md`
(reflects the file's current state; not edited in this pass — the notes already carry these
directions, and they now agree with the code exactly)
- ***Show:*** directions run throughout, one per beat group, matching the code section-by-section,
  including the carrots-horizontal/spinach-vertical orientation and the `(C, S)` readout order.
- The old "*Add this to the animations.*" cue in the Attainability paragraph is gone — replaced by
  three explicit Show lines (Inefficient / Efficient / Unattainable), one per trio beat.
- The three ***Cut to Exercise A1 \| Qn*** directions are present, unchanged.
- The ~~SKIP~~ strike on the inefficient paragraph (from an earlier draft) is gone — the paragraph
  is back in, un-struck, matching Q2 needing that vocabulary.
- The pool-table paragraph now sits between the recap/definition (B04) and Molly's farm (B05) —
  matches the code's cam-gap placement there.

## Open questions
- ~~B13d christens "Marginal Cost" ahead of the prose~~ — resolved 2026-08-25: the beat is cut
  from the session (code removed); the OC line stays as the beat's last state.
- Region-label placements (B24 label sits right of the axes; B24b/B24c labels at region
  centroids) — check against rendered frames.
- **B14's Hagrid exercise puts R on the vertical and F on the horizontal** — the opposite of
  Molly's now-settled carrots-horizontal/spinach-vertical orientation. The wording is verbatim
  from `Exercise/Exercise_F26.md` (and is quoted the same way in the notes), so this is a call
  about the exercise set, not the animation: if Q1 should practice the new orientation, the
  exercise text, its stale PDF, and the B14 card all change together.
