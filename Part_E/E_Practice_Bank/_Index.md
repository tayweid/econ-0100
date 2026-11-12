# Part E Practice Bank

Every Part E practice handout from past semesters. Started 2026-10-13 with material moved out of the Part C bank, and filled on 2026-11-04 from the five per-block `Practice_Bank` folders (E1 Costs, E2 Competition, E3 Monopoly, E4 Duopoly, E5 Policy and Market Power), which are now gone. Every move was a `git mv`. Names are `<Kind>_<Block>_<story>_<semester>`. The block is where the question fits this year, not its old label: the old banks filed "Vignette E3" toffee files under E2, and E5 held Q2–Q4 of the 24F Homework E1 and Vignette E1. PDFs, PNGs and ink solutions sit beside their handout, and each PDF is kept whole.

**Nothing was deleted, and every copy stays in the bank under its own name.** That includes reissues from other semesters, rewordings, pieces split out of a whole handout, and re-renders. `_archive/_duplicates/` holds **identical copies only**. Each one is identical to a file that stays here, and it is named by its old block path: `E5_Policy_and_Market_Power__Homework_E5_sols.pdf` was `E5_Policy_and_Market_Power/Practice_Bank/Homework_E5_sols.pdf`, and `E2_Competition__archive__…` came from that bank's own `_archive/`. Two tests count as identical. One is a byte-for-byte match (`cmp`). The other, for `.md` only, is a match once the leading `<!-- … -->` source header lines are stripped. The full list is at the end.

How to read a name:
- **Semester** comes from the source header (`renamed from 23F.md`, `ECON_0100_24F/…`). The four Honors in-class handouts that print a 2021 date (Vignettes 6, 7, 8 and 9) are named F21, although they were filed under 22F, 23F or 24F.
- **`-oldq` / `-oldhw`** keep the source's own tag: an older handout found in the 24F folder. Its PDF is the earlier print.
- **`_source`** is the copy taken from the course's own notebook or .md (`Source: ECON_0100_…`). The unsuffixed copy with the same name was extracted from the printed handout. The two differ only in markup (answer-space notes, image lines, headings).
- **Same story slug, different block** means pieces of one handout: `Homework_E1_broomstick-costs_F24` (Q1) and `Homework_E5_broomstick-costs_F24` (Q2–Q4). The whole PDF and key sit under the first piece's name. **`_partD`** is a piece holding a question's setup plus Part D only.

## Built from this bank (Fall 2026)

| Built | Uses | Source | Solutions |
|---|---|---|---|
| Exercise E1 | Economic Sudoku | `Classwork_E1_economic-sudoku_F24` (the Fall 2024 Classwork E1), verbatim | worked in the guide; checked against the ink key `Classwork_E1_economic-sudoku_sols.pdf` / `.png` |
| Exercise E2 | *Corrected 2026-11-12: the current Exercise E2 (Choosing Quantity, Operating or Leaving, A Higher Marginal Cost) no longer contains it, so the Toffee tax is unused again and stays in the bank.* Was: Q2 Traditional Toffee Specific Tax | `Classwork_E2_toffee-tax_F23` (Q1 of the Fall 2023 Classwork E2), verbatim; Q1 Economic Sudoku Sells is new, the E1 table with a market price (2026-11-09) | the story and graphs in the guide follow the ink key `Classwork_E2_toffee-tax_sols.pdf` |
| Vignette E1 (2026-11-12) | Q1 The Witching Hour’s Workshop, new (Claude’s proposal, E1.1); Q2 Cost Curves and Policies: graph the three firms’ curves, then one policy per firm on the same row of graphs | `Vignette_E1_cauldron-costs_F24` Q1, verbatim, in Taylor’s rewritten story; the policy sentence is Claude’s | agrees with the ink key `Vignette_E1_cauldron-costs_sols_F24.pdf` (checked 2026-11-12) |
| Vignette E1 Long (2026-11-12; `E1_Costs/Vignette/Vignette_E1_Long`, listed under E1’s extras) | The whole Fall 2024 Vignette E1 with every question separate: Cost Curves, Lump Sum Tax, Per Unit Tax, Per Unit Subsidy, three graphs each. Posted as extra practice, not run in class | `Vignette_E1_cauldron-costs_F24` Q1 and `Vignette_E5_cauldron-costs_F24` Q2 to Q4, verbatim | agrees with the same ink key |
| Homework E1 (draft, 2026-11-11; Q2 added and the policy questions moved in from Homework E2, 2026-11-12) | Q1 Skyline Custom Brooms and Q2 CloudSweep Brooms are new (began as Claude’s proposal, E1.1); Q3 Cost Structures: the base-case matching (a fill-in on paper) and the three policy questions, on the matrix redrawn in full | `Homework_E1_broomstick-costs_F24` Q1 and `Homework_E5_broomstick-costs_F24` Q2 to Q4, verbatim | Q3 agrees with the ink key `Homework_E1_broomstick-costs_sols_F24.pdf` (checked 2026-11-12) |
| Vignette E2 (rebuilt 2026-11-12) | Q1 A Higher Marginal Cost: Taylor’s Exercise E2 wording (Q1 b and c, Q3, Q2 a) for a cauldron workshop, TC = 400 + 10q + q², with a 10-coin tax | none from the bank. Earlier versions and the Toffee Subsidy draft are in `../E2_Competition/_archive/2026-11-12_story_change/` | Claude’s own; no ink key |
| Homework E2 (rebuilt 2026-11-12) | Q1 A Price for Brooms is new (Claude’s proposal, E2.1 and E2.2); Policies and Cost Curves moved to Homework E1 and The History of the Broomstick Market moved to Homework E3 (as its Q2), both on 2026-11-12 ; Q2 Subsidizing Bludgers added 2026-11-12 | `Homework_E2_bludgers-snitches_F21`, verbatim (Q2). The history question (`Vignette_E2_broomstick-history_F24`, verbatim) is in Homework E3. The Subsidizing Bludgers draft of 2026-11-11 is in `../E2_Competition/_archive/2026-11-12_story_change/` | Q2 follows the ink key `Homework_4_sols_F21.pdf` (checked 2026-11-12) |
| Vignette E3 (draft, 2026-11-11) | Q1 Unicorn Horn | `Vignette_E3_unicorn-horn_F24`, spelling corrected | written for the guide; not yet checked against the ink keys `Vignette_E3_unicorn-horn_sols_F21.pdf` / `_F22.pdf` |
| Homework E3 (draft, 2026-11-11) | Q1 The Cauldron Consolidation | `Homework_E3_cauldron-consolidation_F24`, spelling corrected | agrees with the ink key `Homework_E3_cauldron-consolidation_sols_F23.pdf` |
| Vignette E4 (draft, 2026-11-11) | Q1 The Wandmaker's Dilemma | `Vignette_E4_wandmakers-dilemma_F24`, spelling corrected | written for the guide; no key in the bank |
| Homework E4 (draft, 2026-11-11) | Q1 Wandmaker's Dilemma (P = 200 - Q, MC 20) | `Vignette_E4_wandmaker-symmetric_F21`, spelling corrected | written for the guide; no key in the bank |

Economic Sudoku is now **used**. The same table (AFC 120/–/40/30/24, AVC 100/–/90/–/108, ATC 220/150/130/–/132, MC 80/90/130/–) is every copy below. So it is used up everywhere: Classwork E1 F23 and F24, and Vignette E1 F22, S23, F23 and F24. The ink key is printed "Econ 101 | Vignette E1" (a Spring 2023 print, scanned 2023-03-30). It is the same table, so it is the key for every copy.

## Practice and checkpoint allocation (Fall 2026, draft 2026-11-11)

The working skill list is in `../E_Skillsheet.md` (a draft; the codes below are its codes, not the older E2.1 to E5.1 tags on the stems in `../../ECON_0100/Checkpoints/E/`). **Reserved** means held out of every Exercise, Vignette and Homework so the Demo and the Checkpoint versions can use it. Stories and numbers below are the ones to keep out of practice.

| Skill | Exercise | Vignette | Homework | Reserved for Demo and Checkpoint E |
|---|---|---|---|---|
| E1.1 Production Functions | to write (Simulation E's table is the natural source) | to write | to write | None existed. Four drafted 2026-11-12 (Claude’s proposals): `Stems_2026/_README.md` beside the older stems |
| E1.2 Cost Curves | Economic Sudoku (posted) | Cauldron costs (graph the curves) | Broomstick costs (match the curves) | None existed. Four drafted 2026-11-12 (Claude’s proposals): `Stems_2026/_README.md` beside the older stems |
| E2.1 The Competitive Firm | Exercise E2 Q1 to Q2a | to write | Cauldron Consolidation a, b (in HW E3) | Dwindling Dealers Q1 to Q2 (23F MiniExam, three number sets). Three more drafted 2026-11-12 (Claude’s proposals): `Stems_2026/_README.md` |
| E2.2 Entry, Exit & the Long Run | Exercise E2 Q2b to Q3 | Toffee subsidy | Subsidizing Bludgers | Taxing Cauldrons (`E2.1_cauldron-tax-competitive`); Toffee lump-sum tax (`E2.1_toffee-competitive-policy`); Cauldron Conundrum subsidy (`From_C`); Pumpkin Pasty article, a demand fall (`MiniExam_4`). All four are written stories and need a do-form |
| E3.1 Monopoly Price & Quantity | to write | Unicorn Horn | Cauldron Consolidation c, d | Golden Snitches A to C (`E3.1_golden-snitch-monopoly`); Wizard's Chess a to c (`E3.1_wizards-chess-monopoly`); Racing Broom Q1 to Q2 (24F MiniExam); Flue merger (`E3.1_flue-network-duopoly`); Breaking Up A Monopoly, monopoly half |
| E3.2 Market Power & Deadweight Loss | to write | to write | Cauldron Consolidation e | Racing Broom Q3 (24F MiniExam). **One only**; Golden Snitches and Wizard's Chess each need a deadweight-loss part added. Three more drafted 2026-11-12 (Claude’s proposals): `Stems_2026/_README.md` |
| E4.1 Best Responses in a Duopoly | Big Flue Networks a, b (`Classwork_E4_flue-networks_F24`, P = 200 - Q, MC 10) if used | Wandmaker's Dilemma (matrix; P = 100 - Q, MC 10) | not asked directly in HW E4 | Big Flue merger exam numbers (P = 400 - Q, MC 40; `MiniExam_6`); Parallel Wandmaker, different marginal costs (`E4.1_wandmakers-dilemma`); Breaking Up A Monopoly Q4 (23S, `MiniExam_E2`) |
| E4.2 Duopoly Equilibrium | Big Flue Networks c to e if used | Wandmaker's Dilemma c | Wandmaker's Dilemma (P = 200 - Q, MC 20) | Big Flue (P = 400 - Q, MC 40); Dwindling Dealers Q4 to Q5 (23F); Racing Broom Q4 to Q5 (24F); three-firm wandmakers (`Tutorial_E4_wandmakers-triopoly_F23`) |

Collisions to keep in mind:
- `E4.1_flue-network-duopoly` uses the Classwork's numbers (P = 200 - Q, MC 10). If Big Flue Networks is Exercise E4, the Checkpoint must use the exam numbers (P = 400 - Q, MC 40) instead.
- Breaking Up A Monopoly (P = 100 - Q, MC 10) shares its numbers with Vignette E4. Its duopoly half is the same problem under another story.
- Vignette E4 and Homework E4 share a story (Olivander and Gregorovitch) with different numbers.
- The past MiniExams chain monopoly, duopoly and competition in one question. Under one question per skill each reserved item above is only the named parts, given its own numbers.


## What's in the bank, by block

### E1 Costs

| Files | What's in it |
|---|---|
| `Classwork_E1_economic-sudoku_F24` (+pdf, ink key `_sols.pdf` and `_sols.png`) | **Used** (Exercise E1). The table in full. The PDF is headed "Econ 0100 \| Classwork E1, Due in Recitation" (rendered 2023-11-01). |
| `Classwork_E1_economic-sudoku_F23` | The F23 Classwork E1. The text only: the table was an image (`economic_sudoku.png`), which is not here. |
| `Vignette_E1_economic-sudoku_F22` (+pdf) | The F22 Vignette E1, dated October 25, 2022. The table in full. |
| `Vignette_E1_economic-sudoku_S23`, `_F23` | The S23 and F23 Vignette E1. Text only, table an image. They differ only in the image line's archive path. |
| `Vignette_E1_economic-sudoku_F24-oldq` (+pdf) | The table again. The PDF is the "Econ 101" Spring 2023 print. |
| `Vignette_E1_cauldron-costs_F24` (+whole PDF, ink key `_sols_F24.pdf`) | Careful Consideration of Cauldron Costs, the 24F Vignette E1, Q1: graph ATC and MC for three cauldron firms (high FC with constant MC, some FC with rising MC, no FC with constant MC). Its Q2–Q4 are `Vignette_E5_cauldron-costs_F24`. The PDF and key (scanned 2024-11-07) cover all four questions. |
| `Homework_E1_broomstick-costs_F24` and `_F24_source` (+whole PDF, `_matrix_F24.png`, ink key `_sols_F24.pdf`) | The 24F Homework E1 (CloudSweep, Skyline, SwiftTech), Q1: match a 3×4 matrix of cost-curve graphs to the three firms. Its Q2–Q4 are `Homework_E5_broomstick-costs_F24`. The `_source` copy includes the matrix image line (`HW_E1_matrix.png`, which is the PNG here). The PDF and key (scanned 2024-11-15) cover all four questions. |

### E2 Competitive firms (price takers, entry and exit, the long run)

| Files | What's in it |
|---|---|
| `Classwork_E2_toffee-tax_F23` and `_F23_source` (+pdf, ink key `Classwork_E2_toffee-tax_sols.pdf`) | Unused as of 2026-11-12 (it was Exercise E2 Q2 until the Exercise was rewritten). Traditional Toffee Specific Tax: a per-unit tax in a market anyone can enter; tell the story to the long run. The key is a two-question print: Q2, **Traditional Toffee Lump-Sum Tax**, exists only in that PDF. No .md, and it was not transcribed. |
| `Vignette_E2_toffee-subsidy_F22` (+pdf, ink key `_sols_F22.pdf`) | Traditional Toffee Subsidy, the F22 Vignette E3 (November 8, 2022). |
| `Vignette_E2_toffee-subsidy_F21` (+pdf) | The same question as Honors Vignette 6, from the "Lecture Map" of November 2, 2021. It says "cauldron manufacturers" where it means toffee makers, struck by hand. The PDF carries in-class ink. |
| `Vignette_E2_broomstick-history_F24` and `_F24_source` (+pdf; Katie's PDF below) | The History of the Broomstick Market, the 24F Vignette E5. Shooting Star's patent runs out, and many makers produce *identical* brooms; tell the story to the long run. |
| `Vignette_E2_broomstick-history_F22` (+pdf), `_S23`, `_F23`, `_F24-oldq` (+pdf, the Econ 101 print) | The same question, as Vignette E2 in F22, S23 and F23. `_sols_S23.pdf` is the ink key on the Econ 101 Spring 2023 print. |
| `Vignette_E2_broomstick-history_katie_F24.pdf` | **Taylor to check:** the old file name (`Vignette_E5_sols_Katie_Power.pdf`) carries a person's name. It is probably a student's handwritten work on the 24F Vignette E5. If so, it should leave this public repository. It was not opened or read. It was matched to this story by its old name and its date (2024-11-21) only. An identical copy is in `_archive/_duplicates/E2_Competition__Vignette_E3_sols_3.pdf`, under a name with no "Katie" in it. |
| `Homework_E2_bludgers-snitches_F21` | Subsidizing Bludgers, Q1 of the 21F Homework 4: a subsidy in a market with easy entry, to the long run. Its Q2, Golden Snitches, is under E3. The ink key for the whole Homework 4 is `Homework_4_sols_F21.pdf`. There is no handout PDF. |
| `Homework_4_demo_taxing-cauldrons_F22` (+pdf, ink key `_sols_F21.pdf`) | In the bank since 2026-10-13 (see the first table below). Q1 Taxing Cauldrons fits E2, and Q2 Wizard's Chess fits E3. |

### E3 Monopoly

| Files | What's in it |
|---|---|
| `Vignette_E3_unicorn-horn_F22` (+pdf, ink key `_sols_F22.pdf`) | Unicorn Horn: one seller, P = 50 − Q, MR = 50 − 2Q, MC 5; find Q, P and profit. The F22 Vignette E5. |
| `Vignette_E3_unicorn-horn_F23` and `_F23_source` (+pdf, the Econ 101 Spring 2023 print) | The same question, as the F23 Vignette E5. |
| `Vignette_E3_unicorn-horn_F21` (+pdf, ink key `_sols_F21.pdf`) | The same question as Honors Vignette 7, November 4, 2021. The .md transcribes the in-class work typed into that handout. The PDF carries the ink. |
| `Vignette_E3_unicorn-horn_F24` and `_F24_source` (+pdf) | The 24F Vignette E4, reworded ("voluntarily donated by unicorns", Q1–Q3). |
| `Vignette_E3_unicorn-broomstick_F24` (+pdf) | The 24F Vignette E2 as first issued (2024-11-14). Q1 is Unicorn Horn (24F wording), and Q2 is The History of the Broomstick Market. A day later it was split into Vignette E4 and Vignette E5. |
| `Homework_E3_cauldron-consolidation_F23`, `_F23_source`, `_F24-oldhw` (+pdf, the 2023 print, due November 17), ink key `_sols_F23.pdf` | The Cauldron Consolidation, the F23 Homework E1. A competitive self-stirring-cauldron market (MC = Q + 10, P = 1010 − Q/2, P = 20) is bought up by Cauldron Charmers (MR = 1010 − Q); find price, quantity, profit and DWL before and after. Also starts from E2 (the competitive baseline). |
| `Homework_E3_cauldron-consolidation_F24` (+pdf) and `_F24_source` | The same question, as the 24F Homework E2 ("Firms produce", Q1–Q5 "of 5"). |
| `Homework_E3_snitches-broomsticks_F21` and `_F22` (+pdf, the 2021 print, due November 14), ink key `_sols_F21.pdf` | Homework 5, Fall 2021. Q1 Golden Snitches: one seller, P = 100 − Q, MC 10; Parts A–C give Q, P and profit, and Part D is a lump-sum tax. Q2 Broomsticks: a fixed annual subsidy to makers of differentiated brooms, to the long run (E5). |
| `Homework_E3_snitches-broomsticks-wands_F22` (+whole PDF), `_F22_source`, `_F22_source_partD`, and `Homework_E4_snitches-broomsticks-wands_F22` | Homework E, Fall 2022 (due November 15). Q1 Golden Snitches (reworded: "Use one graph to answer parts A through C") and Q2 Broomsticks are in the first file. Q3, the asymmetric Wandmaker's Dilemma, is the E4 file. The `_source` files are its Q1 Parts A–C and Q1 Part D. |
| `Homework_E3_bludgers-snitches_F21` and `_F21_partD` | Golden Snitches as Q2 of the 21F Homework 4, Parts A–C and Part D. It is the same question as Homework 5's Q1. |
| `Homework_E3_sherbet-chess-wands_F22` and `_F22_partD` | Wizard's Chess, Q2 of the F22 Homework E Demo: P = 10 − 2Q, MR = 10 − 4Q, MC 1. Parts A–C, then Part D, a 1-galleon subsidy. It is the same question as Q2 of `Homework_4_demo_taxing-cauldrons_F22`. The whole PDF is `Homework_E5_sherbet-chess-wands_F22.pdf`. |

Taxes and subsidies on a monopolist (the Part D questions) are in this year's E3 episode, so they are filed here. They would also fit E5.

### E4 Duopoly and oligopoly

| Files | What's in it |
|---|---|
| `Classwork_E4_flue-networks_F24` (+pdf, the 2023 render, ink key `Classwork_E4_flue-networks_sols.pdf`) and `_F23` | Big Flue Networks: a symmetric Cournot duopoly, P = 200 − Q, MC 10. Best responses, Nash quantities, price, total profit, DWL. |
| `Vignette_E4_wandmakers-dilemma_F23`, `_F24`, `_F24-alt` (+pdf, the Econ 101 Spring 2023 print) | The Wandmaker's Dilemma: a 2×2 high/low output game (900, 900 / 500, 1500 / 1500, 500 / 700, 700), then Cournot with P = 100 − Q, MC 10. `_F24-alt` was `24F_Vignette_E.md`, with a plain table in place of the LaTeX array. There is no key. |
| `Vignette_E4_wandmaker-symmetric_F21` (+pdf) | Honors Vignette 9, November 18, 2021: Cournot with P = 200 − Q, MC 20 for both. |
| `Homework_E4_wandmaker-asymmetric_F21` | Q1 of the 21F Homework 6: P = 200 − Q, MC 20 and 30, with Part D a 10-galleon subsidy. The same text is Q3 of the F22 Homework E (`Homework_E4_snitches-broomsticks-wands_F22`). The rest of Homework 6 is in Part F. |
| `Homework_E4_sherbet-chess-wands_F22`, with `Homework_E4_parallel-wandmaker_F21.pdf` and its ink key `_sols_F21.pdf` | The Parallel Wandmaker's Dilemma: P = 100 − Q, MC 10 and 5, with Part D a "subsidy" modeled as a 10-galleon cost *increase*. The .md is Q3 of the F22 Homework E Demo. The PDF and key are the 21F Homework 6 Demo, where the same question is Q1. Its Q2, Luna's Problem (a budget constraint), belongs to Part F; the Part F bank has its own .md (`Homework_6_demo`). |
| `Homework_E4_breakup-monopoly_F23`, `_F23_source`, `_F24-oldhw` (+pdf, the 2023 print, due November 29) | Breaking Up A Monopoly: a monopoly (P = 100 − Q, MC 10), then broken into a symmetric Cournot pair; compare quantity, price and profit. It was the F23 Homework E2. There is no key. |
| `Tutorial_E4_wandmakers-triopoly_F23` | The 2023 tutorial sheet. Q1 is a duopoly (Q = 100 − P, MC 10), and Q2 adds a third firm, the bank's only three-firm Cournot. The source's MR typos are kept and noted in the file. |
| `Homework_unused_wand-duopoly_F21` | In the bank since 2026-10-23 (see the second table below). |

### E5 Policy and market power (monopolistic competition, policy, comparing structures)

| Files | What's in it |
|---|---|
| `Vignette_E5_numbus-2000_F22` (+pdf, ink key `_sols_F22.pdf`) | Numbus 2000 (sic): branded brooms in a stable market, then a better broom enters. Tell the story for makers like Cleansweep, to the long run. This is monopolistic competition. The F22 Vignette E4. |
| `Vignette_E5_numbus-2000_F21` (+pdf, ink key `_sols_F21.pdf`) | The same question, as Honors Vignette 8 on November 11, 2021 (filed as 24F_Vignette_8). |
| `Vignette_E5_numbus-2000_F24` | The same question, as the 24F Vignette E6. |
| `Vignette_E5_cauldron-costs_F24` and `_F24_source` | Q2–Q4 of the 24F Vignette E1 (Careful Consideration of Cauldron Costs): model a lump-sum tax, a per-unit tax and a per-unit subsidy on the three firms' cost curves. The PDF and key are under `Vignette_E1_cauldron-costs_F24`. |
| `Vignette_E5_command-of-costs_F23` (+pdf, the Econ 101 Spring 2023 print), `_F23_source`, `_S23` | Carefully Crafting the Command of Costs, Vignette E4 in S23 and F23. It has the same three cauldron firms, with a longer setup: lump-sum tax, lump-sum subsidy, per-unit tax and per-unit subsidy. It is the predecessor of the 24F Cauldron Costs. |
| `Homework_E5_broomstick-costs_F24` | Q2–Q4 of the 24F Homework E1: which matrix graph shows a 4-galleon per-unit subsidy, a 5-galleon tax, a 500-galleon lump-sum fee. The PDF, PNG and key are under `Homework_E1_broomstick-costs_F24`. |
| `Homework_E5_broomstick-history-branded_F21` and `_F22` (+pdf, the 2021 print), ink key `_sols_F21.pdf` | The History of the Broomstick Market with *slightly different* brooms (monopolistic competition). It is the Homework 5 Demo, Fall 2021, filed again under 22F. Compare the E2 vignette, where the brooms are identical. |
| `Homework_E5_sherbet-chess-wands_F22` and `_F22_source` (+whole PDF, six pages) | A Favourite Muggle Candy (Sherbet Lemons), Q1 of the F22 Homework E Demo. WWW is the only licensed seller, then many sellers with their own recipes enter; tell the story to the long run. Q2 (Wizard's Chess) and Q3 (Parallel Wandmaker) are the E3 and E4 files with the same slug. There is no key for F22. |

Lump-sum and per-unit taxes on cost curves (the cauldron, broomstick and Command of Costs questions) could also sit in E1 if this year's E1 shows how taxes move cost curves. The old banks put them in E5, and that is kept.

## What's left

Part D's convention, kept here: **Exercises come from past Classwork, Vignettes from past Vignettes, Homework from past Homework.** Unused stories, by slot:

| Slot | Unused stories in this bank |
|---|---|
| Vignette E1 | Cauldron Costs Q1 (graph ATC/MC for three firms). Economic Sudoku is used. |
| Vignette E2 | Traditional Toffee Subsidy (F21, F22, key); The History of the Broomstick Market, identical brooms (F22–F24, S23 key) |
| Vignette E3 | Unicorn Horn (F21, F22 keys; reworded F24) |
| Vignette E4 | The Wandmaker's Dilemma, 2×2 game + Cournot (no key); symmetric wandmakers, 200 − Q (F21) |
| Vignette E5 | Numbus 2000 (F21, F22 keys); Command of Costs; Cauldron Costs Q2–Q4 (key) |
| Exercise E2 | Built, with new questions. Traditional Toffee Specific Tax is unused again (2026-11-12); its Lump-Sum Tax twin (key PDF only) stays unused, kept for Exercise E5 |
| Exercise E3 | No past Classwork. The nearest are Golden Snitches or Wizard's Chess (Homework), or Unicorn Horn (Vignette). |
| Exercise E4 | Big Flue Networks (Classwork E3 F23/F24, key); the 2023 tutorial (duopoly, triopoly) |
| Exercise E5 | No past Classwork. Toffee Lump-Sum Tax (key PDF only) is the closest. |
| Homework E1 | Broomstick Costs Q1 (matrix matching, key) |
| Homework E2 | Taxing Cauldrons (F21 demo, key). Subsidizing Bludgers is used (Homework E2 Q2, 2026-11-12). |
| Homework E3 | Golden Snitches A–D (F21 key); Wizard's Chess A–D (F21 demo key); The Cauldron Consolidation (F23 key) |
| Homework E4 | Breaking Up A Monopoly; asymmetric Wandmaker's Dilemma (200 − Q, MC 20/30); Parallel Wandmaker (100 − Q, MC 10/5, F21 key); the unused A-and-B wand duopoly |
| Homework E5 | Broomsticks fixed annual subsidy (F21 key); broomstick history, branded (F21 key); Sherbet Lemons; Broomstick Costs Q2–Q4 (key) |

The matching checkpoint material (Demos, MiniExams, keys and the `E2.1`–`E5.1` stems for Toffee, Cauldron tax, Golden Snitch, Wizard's Chess, Flue Network and Wandmaker's Dilemma) is in `../ECON_0100/Checkpoints/E/`. It is a read-only reference, and nothing there was moved. Before placing a story here, check it is not already on Checkpoint E.

## Moved in earlier

Started 2026-10-13 with material moved out of the Part C bank because it is about long-run behavior (free entry), which is Part E.

| File | What's in it |
|---|---|
| `Homework_4_demo_taxing-cauldrons_F22` (+pdf, ink key `Homework_4_demo_taxing-cauldrons_sols_F21.pdf`) | Q1 Taxing Cauldrons: a tax in a market anyone can enter, "using a couple of graphs … explain what happened" (long-run, E2). Q2 Monopoly! Wizard's Chess, P = 10 − 2Q, MC 1, with a lump-sum tax and a 1-galleon subsidy (E3). |

*Corrected 2026-11-04:* this row first named `Homework_4_sols_F21.pdf` as the key. That PDF is the key to Homework 4 itself, Fall 2021 (Q1 Subsidizing Bludgers, Q2 Golden Snitches). The Homework 4 Demo key (Taxing Cauldrons, Monopoly!) came in from the E2 bank as `Homework_4_demo_taxing-cauldrons_sols_F21.pdf`. Both stay.

The matching checkpoint-side copies (the Cauldron Conundrum and Subsidizing Bludgers subsidies) are in `ECON_0100/Checkpoints/E/From_C/`.

Moved in from the Part D bank on 2026-10-23:

| File | What's in it |
|---|---|
| `Homework_unused_wand-duopoly_F21.md` | The last question of an unused 21F homework: two wand sellers A and B, Q = 100 − P, MC 10, given MR; Cournot outputs and price (E4). A different version from the Ollivander and Gregorovitch wand duopoly (200 − Q), formerly in `E4_Duopoly/Practice_Bank/` (now `Homework_E4_wandmaker-asymmetric_F21` and `Vignette_E4_wandmaker-symmetric_F21` here), and from `ECON_0100/Checkpoints/E/E4.1_wandmakers-dilemma.md`. No PDF or key. |

## `_archive/_used/` (used word for word, moved 2026-11-12)

These files hold question text that a Fall 2026 handout now uses word for word, apart from headers, layout and spelling. The tables above still name them; they are in `_archive/_used/`, not in the bank. Ink keys, and prints or images that also cover unused questions, stayed in the bank.

| Used in | Files moved | Stayed in the bank |
|---|---|---|
| Exercise E1 | Every Economic Sudoku copy: `Classwork_E1_economic-sudoku_F23`, `_F24` (+pdf); `Vignette_E1_economic-sudoku_F22` (+pdf), `_S23`, `_F23`, `_F24-oldq` (+pdf) | the ink key `Classwork_E1_economic-sudoku_sols.pdf` / `.png` |
| Vignette E1 and Vignette E1 Long | `Vignette_E1_cauldron-costs_F24.md` (Q1); `Vignette_E5_cauldron-costs_F24`, `_F24_source` (Q2 to Q4), used word for word in Vignette E1 Long | the whole PDF and ink key; Command of Costs; Toffee Subsidy, back in the bank unused |
| Homework E1 | `Homework_E1_broomstick-costs_F24.md`, `_F24_source.md` (Q1); `Homework_E5_broomstick-costs_F24` (Q2 to Q4, moved here from Homework E2 on 2026-11-12) | its PDF, matrix PNG and ink key |
| Homework E2 (rebuilt 2026-11-12, broomstick makers) | `Homework_E2_bludgers-snitches_F21`; (moved to Homework E3 with the question:) every identical-brooms copy of The History of the Broomstick Market: `Vignette_E2_broomstick-history_F22` (+pdf), `_S23`, `_F23`, `_F24` (+pdf), `_F24_source`, `_F24-oldq` (+pdf) | the S23 key and the `_katie_` PDF for the broomstick history; the branded-brooms version (E5). Subsidizing Bludgers is Homework E2 Q2 again (2026-11-12); its file is in `_archive/_used/` and its key `Homework_4_sols_F21.pdf` stays in the bank |
| Vignette E3 | `Vignette_E3_unicorn-horn_F24` (+pdf), `_F24_source` | the F21, F22 and F23 copies (earlier wording), `Vignette_E3_unicorn-broomstick_F24` (its Q2 is unused), both keys |
| Homework E3 | `Homework_E3_cauldron-consolidation_F24` (+pdf), `_F24_source`, `_F23`, `_F23_source`, `_F24-oldhw` (+pdf). The F23 copies differ from F24 only in the header, the question numbering and two spellings | the ink key `_sols_F23.pdf` |
| Vignette E4 | `Vignette_E4_wandmakers-dilemma_F24`, `_F23`, `_F24-alt` (+pdf). The same wording; `_F24-alt` sets the table differently | `Unplaced_E4_wandmakers-dilemma_S23` (different text) |
| Homework E4 | `Vignette_E4_wandmaker-symmetric_F21` (+pdf) | |

## `_archive/_duplicates/` (identical copies only)

Each file here is identical to the bank file named beside it. Nothing else was archived.

| Archived copy | Identical to (stays in the bank) | Test |
|---|---|---|
| `E2_Competition__Homework_E2_sols.pdf` | `Homework_E3_cauldron-consolidation_sols_F23.pdf` | cmp |
| `E2_Competition__Homework_E_demo_sols_2.pdf` | `Homework_E5_broomstick-history-branded_sols_F21.pdf` | cmp |
| `E2_Competition__Vignette_E3_sols_3.pdf` | `Vignette_E2_broomstick-history_katie_F24.pdf` (**Taylor to check**, above) | cmp |
| `E2_Competition__archive__Vignette_E3_sols_4.pdf` | `Vignette_E2_toffee-subsidy_F21.pdf` | cmp |
| `E2_Competition__archive__Vignette_E3_v2_sols.pdf` | `Vignette_E2_toffee-subsidy_F21.pdf` | cmp |
| `E3_Monopoly__Homework_5_sols.pdf` | `Homework_4_sols_F21.pdf` | cmp |
| `E3_Monopoly__Vignette_E2_sols.pdf` | `Vignette_E2_broomstick-history_sols_S23.pdf` | cmp |
| `E3_Monopoly__Vignette_E5_v5.md` (the S23 notebook copy) | `Vignette_E3_unicorn-horn_F23_source.md` | header-stripped .md |
| `E4_Duopoly__Vignette_E3_v2.md` (the S23 notebook copy) | `Vignette_E4_wandmakers-dilemma_F23.md` | header-stripped .md |
| `E5_Policy_and_Market_Power__Classwork_E2_sols.pdf` | `Classwork_E2_toffee-tax_sols.pdf` | cmp |
| `E5_Policy_and_Market_Power__Homework_E5_demo_sols_2.pdf` | `Homework_E4_parallel-wandmaker_sols_F21.pdf` | cmp |
| `E5_Policy_and_Market_Power__Homework_E5_sols.pdf` | `Homework_E1_broomstick-costs_sols_F24.pdf` | cmp |
| `E5_Policy_and_Market_Power__Homework_E5_sols_2.pdf` | `Homework_4_sols_F21.pdf` | cmp |
| `E5_Policy_and_Market_Power__Homework_E5_sols_3.pdf` | `Homework_E3_snitches-broomsticks_sols_F21.pdf` | cmp |
| `E5_Policy_and_Market_Power__Vignette_E1_sols.pdf` | `Vignette_E1_cauldron-costs_sols_F24.pdf` | cmp |
| `E5_Policy_and_Market_Power__Vignette_E3_sols.pdf` | `Vignette_E2_toffee-subsidy_sols_F22.pdf` | cmp |

## Not in this bank

The blocks' own `_archive/` folders (`E1_Costs/_archive/` and the others), their notes, storyboards and animation files, `E1_Costs/Exercise/`, and `E4_Duopoly/04_Handwritten.pdf` were left where they are.
