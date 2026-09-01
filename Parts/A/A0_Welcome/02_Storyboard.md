# Episode 0 | *Economics isn't* about *money* — Storyboard (v2, 2026-08-21)

Source: `01_Notes.md` (post-reorder). Code: `03_Code.py`, one scene `Episode0` with one flat `construct()`;
each `# BNN` section is self-contained (clears the previous beat, builds its own). Pauses are unnamed
`self.pause()` calls placed after the plays they conclude — the viewer parks there until the next press.
No `wait()`s: pacing comes from the pauses. Render: `maniml 03_Code.py Episode0 --render`. Talking-head
beats (`cam`) are gaps between sections.

## The visual spine

One recurring object — **the value line** (`value_line` / `value_marks` in `03_Code.py`): a number
line of value; choices are plain dot+label marks at positions, re-ranked by shifting a mark along the
line (`mark.animate.shift(line.n2p(new) - line.n2p(old))`), so every change is a continuous motion.
Live readers (the OC($1) max line, the A-beats-B bracket) are `always_redraw` closures over mark
positions. It's the Part B price-line idiom (B1 "Show Consumer Surplus") brought forward to day 1.

| script idea | what the value line does |
|---|---|
| preferences are rankings | items at heights, no numbers |
| utility | tick numbers appear on the line |
| "numbers don't matter" | tick numbers relabel ×100; no item moves |
| mine vs yours | two lines, same items, different heights |
| preferences change | coffee and tea slide past each other |
| op cost of a dollar | a red read line (live number) sits at the highest item; chocolate climbs past apple, the read line follows, the choice flips |
| bakery | carrot cake slides in from the bottom to the top; the "OC(pie)" read line jumps from bread to cake |
| marginal | a row of apples with falling benefit bars against a flat cost line — the staircase we'll later call demand |

Opportunity cost (B28–B32): the original green/red box animation, plus A and B on the number line with benefit/cost braces.
Titles are screen titles, top-left (`style.title`).
No notes panel (tried 2026-08-21, too cluttered); principle lines and definitions are full-frame cards.

## Beats

| # | Script cue | Mode | Action | Status |
|---|-----------|------|--------|--------|
| B01 | (cold open) | anim | Bumper: raster MICROECONOMICS over `Part A \| Episode 0`, block vertically centred | [ok] |
| B02 | "This figure shows unemployment…" | anim | Page title *Unemployment*, figure caption *rate (%)*; series scrolls with eased motion, pauses at 2008 | [ok] |
| B03 | "And as we reach 2020…" | anim | …continues through the Covid spike | [ok] |
| B04 | "Look at this graph of wealth during the Great Depression" | anim | Page title *Wealth in the Great Depression*; rise to 1929, red fall to 1933; *Where did all that wealth go?* at the bottom | [ok] |
| B05 | "take a look at this map" | anim | Black Marble full-bleed; title *The 30 largest cities in the world.*; cities grow in, gold = port; *20 of the 30 are ports.* under the title | [ok] |
| B06 | "I've been motivated…" → "Lets start at the beginning." | cam | ~2 min to camera; panel can stay up under a `split` | — |
| B10 | "I prefer carrot cake to chocolate cake." | anim | `Chocolate Cake ≺ Carrot Cake` (less preferred on the left) | [ok] |
| B11 | "dark roast coffee to medium roast" | anim | `Light Roast ≺ Dark Roast` | [ok] |
| B12 | "medium roast coffee to light roast" | anim | the pair opens while `Medium Roast ≺` fades in from above (original fly-in build for the pairs) | [ok] |
| B13 | "I could keep going, listing out…" | anim | the chain dissolves onto a horizontal number line; espresso and decaf fade in in place (decaf labelled below) | [ok] |
| B14 | "You'd be able to rank them." | anim | group fades out, next fades in with its own positions: seasons, pizza, coffees | [ok] |
| B15 | "Preferences are rankings." | anim | definition card | [ok] |
| B16 | "assign them numbers…" | anim | tick numbers 1, 5, 10 appear | [ok] |
| B17 | "These numbers are what we call 'Utility'." | anim | *Utility* definition card | [ok] |
| B20 | "multiply the numbers by 100" | anim | ticks relabel 100, 500, 1000 and back with the Utility definition still up; nothing moves | [ok] |
| B18 | "We can like different things and like the same things differently." | anim | *Me* line moves up; *You* line below: same coffees, different positions | [ok] |
| B19 | "often we'll just talk about benefits" | anim | numbers fade; *benefit* arrow under the lines | [ok] |
| B21 | "I used to like coffee more than tea" | anim | *You* line and all but Espresso fade; Tea comes in; the two slide past each other | [ok] |
| B22 | "We can't always have what we want most." | anim | card | [ok] |
| B23 | "Scarcity is more basic than money." | anim | card | [ok] |
| B24 | "nice house near the park … go to the movies more often" | anim | two bundles with `or`: big house + 2 tickets vs small house + 6 tickets; green/red choice boxes, then they swap | [ok] |
| B25 | "***who*** gets that nice house" | anim | two houses with `or`, *Taylor gets the house* / *Andrew gets the house*; green/red boxes swap | [ok] |
| B26 | "We make choices because of preferences and scarcity." | anim | card | [ok] |
| B27 | "Preferences + Scarcity = Choices" | anim | equation assembles under the sentence (`=`) | [ok] |
| B28 | "the choice of A OR B" | anim | `A or B`; green (chosen) and red (given up) boxes swap back and forth | [ok] |
| B29 | "you'll choose A… Your benefit is the value A gives you." | anim | A and B on a number line; A turns green: *benefit* = where A sits | [ok] |
| B30 | "you gave up the opportunity to have B… This is the cost" | anim | B turns red: *cost* = where B sits; a green bracket spans the gap: *A beats B* | [ok] |
| B31 | "This is what economists call opportunity cost" | anim | `Opportunity Cost(A) = B`; definition card | [ok] |
| B32 | "and if you like B more" | anim | the dots cross (eased); the bracket turns red *B beats A*; colours, boxes and equation follow | [ok] |
| B33 | "Forbes Ave Grocery… apples and bananas, each for \$1" | anim | *Apple* (green) or *Banana* (yellow); green then red boxes fade in; `Opportunity Cost(apple) = banana` | [ok] |
| B34 | "how do we know the opportunity cost of a dollar?" | anim | `\$1` coin under a value line of its uses; red read line with live number at the max; chocolate climbs past apple, the read line follows; *the choice flips* | [ok] |
| B35 | "apple pie OR a loaf of banana bread" | anim | number line: bread, pie; one red arrow under the line pie→bread; `OC(pie) = bread` stored in grey under the title; arrow fades | [ok] |
| B36 | "throws in the option for carrot cake… I love carrot cake" | anim | cake fades in where it belongs; re-find OC(pie) with one arrow → `= cake`; then cake→pie, bread→cake, one arrow at a time, each stored under the title | [ok] |
| B37 | "one more apple… marginal benefit… marginal cost" | anim | bars numbered 1–5, benefits falling (9, 7, 5, 3, 1), flat cost line at 4; ✓ ✓ ✓ ✗ ✗; *Marginal means one more.* | [ok] |
| B38 | "This is what we call Autarky" | anim | definition card | [ok] |
| B39 | "This is an example of a payoff matrix." | anim | dating game (rows You, columns Love interest) | [ok] |
| B40 | "Your love interest can either…" / "And you can…" | anim | column headers circled, then row headers | [ok] |
| B41 | "Circle everything that's relevant as it's said" | anim | cells walked in VO order | [ok] |
| B42 | "Microeconomics tells us…" | anim | title + five lines, key phrases in gold, one at a time | [ok] |
| B44 | "This class is made up of six parts." | anim | six rows: *Part X.* grey → part name gold → subtitle white (labels from `_Parts.md`) | [ok] |
| B43 | "Next time…" | anim | teaser + framebox | [ok] |
| B45 | "Who these videos are for" → end | cam | — | — |

## Pausepoints (2026-08-23)

One `self.pause()` per spoken trigger: RIGHT plays from one stop to the next, so every sentence that
should *cause* a motion gets its own stop. Rule used throughout: a beat's clear-the-screen fade
(`FadeAll`) runs as the first thing of the *next* press (never a stop on an empty screen), and the
last state of a beat holds while the talking continues. Pauses are unnamed in code; each pause block
sits under a `# BNN` header, and the ids below match those headers, listed in scene order.
90 pausepoints. Merged by Taylor 2026-08-23: B04 is one press (rise, fall, question) and B05b is one
press (title, cities, ports); the old B19 benefit-arrow beat is cut (the value line's arrow tip now
carries the direction-of-preference).

| stop | press on |
|---|---|
| (scene start) | cold open; first press = B01 raster |
| B01 | raster MICROECONOMICS fades in |
| B01b | flicker — `pause(loop=True)`, cycles seamlessly while parked |
| B01c | part label joins; holds until "This figure shows unemployment…" |
| B02 | "This figure shows unemployment…" (clears the bumper) |
| B03 | "And as we reach 2020…" |
| B04 | "Look at this graph of wealth…" (rise, fall, trough, question — one press) |
| B05 | "And take a look at this map…" |
| B05b | "Why are people crammed into cities together…?" (title, cities grow, ports key + tally — one press) |
| B10 | "I prefer carrot cake to chocolate cake." (after the B06 cam stretch; clears the map) |
| B11 | "I also prefer dark roast coffee…" |
| B12 | "I prefer medium roast coffee to light roast coffee." |
| B13 | "I could keep going…" (chain onto the number line) |
| B13b | "…listing out all the different types of coffee." (espresso, decaf) |
| B14 | "I have preferences for most things in my life." (seasons) |
| B14b | "I could ask you about most things…" (pizza) |
| B14c | "You'd be able to rank them." (back to coffee) |
| B15 | "This is how we think about preferences, as rankings." |
| B16 | "…assign them numbers…" |
| B17 | "These numbers are what we call 'Utility'." |
| B20 | "We can multiply the numbers by 100…" |
| B20b | (holds on ×100 through "the specific numbers don't matter"; press to return) |
| B18 | "We can like different things and like the same things differently." |
| B21 | "And we can change our preferences." (You-line clears, Tea comes in) |
| B21b | "…but now I like tea more than coffee." |
| B22 | "Sorry if I'm the one to break it to you…" |
| B22b | "…we can't always have what we want most." |
| B23 | "…scarcity like this is more basic than money." |
| B24 | "Most people prefer a nice house near the park…" (bundles) |
| B24b | "You may ask yourself whether you want a nice house near the park…" |
| B24c | "…or to have a small house far from the park…" |
| B25 | "But we are also asking from a societal perspective…" (houses) |
| B25b | "…***who*** gets that nice house" |
| B25c | (either could; swap) |
| B26 | "Society faces all sorts of choices like this…" |
| B27 | "I like to boil this down into a pseudomathematical relationship…" |
| B28 | "Lets say I give you the choice of A OR B." (section title + A or B) |
| B28b | "If you choose A, you can't have B." |
| B28c | "If you choose B, you can't have A. That's the scarcity." |
| B29 | "If you like A more than B, you'll choose A. That's the preference." |
| B29b | "Your benefit is the value A gives you." |
| B30 | "But because you chose A you gave up the opportunity to have B." |
| B30b | "This is the cost, the value of all the things you gave up to get it." |
| B31 | (write Opportunity Cost(A) = B) |
| B31b | "This is what economists call opportunity cost…" |
| B32 | "And if you like B more than A, you would pick B" |
| B32b | "…and the opportunity cost of B is A." |
| B33 | "…they only sell apples and bananas, each for $1." |
| B33b | "If you buy an apple, you give up what else you could do with that $1…" |
| B33c | "The opportunity cost of the apple is the next best use of your $1…" |
| B34 | "But how do we know the opportunity cost of a dollar?" |
| B34b | "So it's the maximum of their utilities." |
| B34c | "And if we decide we actually like chocolate more than we used to…" |
| B34d | "…meaning we may no longer buy the apple, but instead have the chocolate." |
| B35 | "…an apple pie OR a loaf of banana bread, but only one" |
| B35b | "…if you choose the apple pie, you would give up the banana bread." |
| B36 | "What about if the bakery throws in the option for carrot cake?" |
| B36b | "After the carrot cake, the opportunity cost of the apple pie is the carrot cake." |
| B36c-B36d | "…the opportunity cost of each of the three alternatives" (one press per table row) |
| B37 | "…it's whether to have one more apple." (title + 1–5) |
| B37b | "Say the first apple is delicious…" |
| B37c | "And each additional apple has its own cost…" |
| B37d | "If the benefit of one more apple beats its cost, have the apple." (one press per apple, ×5) |
| B37e | "We'll lean on this idea heavily…" |
| B38 | "But the choices available to us aren't always our own making." |
| B38b | "This is what we call Autarky…" |
| B39 | "This is an example of a payoff matrix." |
| B40 | "Your love interest can either choose…" |
| B40b | "And you can choose…" |
| B41 | "If your love interest is going to the movie, and you go with them…" |
| B41b | "…than if you don't go with them." |
| B41c | "…you shouldn't go to the movie and leave them hanging" |
| B41d | "…you should go with them to the theater!" |
| B42 | "Microeconomics tells us…" (matrix holds through the Micro paragraph; press shows the title) |
| B42b | remaining clauses, one press each (×5 total; clauses 1+2 share the first press) |
| B44 | "This class is made up of six parts." |
| B44b | one press per part (×6) |
| B43 | "Next time…" (final section; runs to black) |

## Stage-direction edits made in `01_Notes.md`
(animation comments only; prose untouched)
- "***Maybe we change the visual to be ranked vertically…***" → definite: the chain stands up into the ladder.
- Two "***Show all this.***" cues replaced with the concrete actions of B33–B34 and B35.
- B29/B30 cues reworded; now back to the original box animation.

## Open questions
- B37 numbers (benefits 9,7,5,3,1 vs cost 4) are mine; change if you want the cutoff elsewhere.
- B29/B30 resolved: positions and the gap, no lengths from zero (guide §5).
- B14 swap lists (seasons; pizza toppings) are placeholders for whatever you'd rather rank.
- B24 house/ticket glyphs are the "simple and stylized" placeholder direction — first real test of that look.
