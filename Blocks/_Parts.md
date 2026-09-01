# Microeconomics Outline

This class tells a cohesive story of Microeconomics using visualizations and animations in six Parts. One arc for the Part. One arc for the Block. One Block per class period. One arc for the class.

## Part A | The Landscape

Better choices can benefit everyone

Set the table by drawing a line around the part of the playground the series lives in.

- *A0 | Economics isn't* about *money* — motivate economics via preferences and scarcity, opportunity cost, the PPF.
- *A1 | Coordination can improve everyone* — introduce trade on the PPF, comparative advantage, a point outside the PPF, and prices to coordinate.
- *Episode A\_ | Four Quadrant PPF* — show the relationship between labor input, production functions, and prices (introduce wages). The four-quadrant PPF squishes together production and labor inputs; specialization and the shape of the production function generate curvature in the aggregate PPF.
- *Episode A_\_ | The Map* — walk through "The Map."

## Part B | Coordination Using Markets

markets can effectively facilitate coordination

*Use prices to examine the question of where to live on the PPF*

- *Supply and Demand* — begin thinking about where to live on the PPF via sellers' costs and buyers' wants; maybe mention the market taxonomy.
- *Equilibrium* — simulation of a perfectly competitive market for rice in Marryville.
- *Welfare* — consumer surplus → producer surplus → efficiency of competitive markets.
- *Deadweight Loss and Price Controls* — price controls introduce DWL; first modeled with a price line, then re-done using government purchases.
- *First Welfare Theorem* — use price controls to show why markets maximize welfare.
- *Government Cheese* — revisit price controls via government buyups, told through government cheese.

## Part C | Externalities

externalities break the efficiency of markets

*Externalities break markets.*

- *Externalities* — positive and negative externalities and the associated market failures.
- *Corrective Taxes/Subsidies* — taxes and subsidies as a solution to market failures.
- *Elasticity* — elasticity as a way to measure the incidence of a tax on equilibrium.
- *International Trade* — import/export taxes/tariffs and combinations with domestic taxes; bring together the perfectly-competitive-market ideas.

## Part D | Strategic Interaction

Voting, taxonomy of goods, markets often aren’t the right tool.

- *Tragedy of the Commons* — simulation mapped into game theory.
- *Public Goods* — simulation mapped into game theory, using a Lindahl equilibrium and voting.
- *Paradox of Voting* — modeled after the Infinite Series video.
- *Tiebout and Club Goods* — maybe do this with a simulation.

## Part E | Sellers

market power breaks the efficiency of markets

*Sellers decisions make up the supply curve.*

- *Costs* — costs as a way of measuring the tradeoffs firms face.
- *Production Functions and Isoquants* — inputs to outputs and how they give us isoquants (may be too much for intro).
- *Marginal Revenue: Monopoly and Perfect Competition* — build the MR curve, moving demand from flat to downward sloping, showing price is the demand curve under perfect competition.
- *Monopolistic Competition* — looks like monopoly in the short run, faces perfect-competition dynamics in the long run.
- *Game Theory and Duopoly* — use duopoly to build up more baby game theory.

## Part F | Buyers

Buyers decisions shape the demand curve.

*better subtitle*

- *Utility* — turning preferences into numbers with no intrinsic zero.
- *Budget Constraint* — using prices to represent the scarcity we face.
- *Demand* — the individual's constrained-optimization decision and how it gives us demand.
- *Edgeworth Box* — how prices distribute the resources available to us; tie back to the PPF.
- *Monopsony* — build a model of monopsony.

### Overview

This project contains educational animations for an economics course, organized into 6 parts (A-F) with multiple episodes in each part. Blocks/ is a flat list of block directories; the part is the letter prefix. Each episode follows a consistent flat file structure that supports the animation production workflow.

### Directory Structure

```
Blocks/
├── _Assets/          # shared style.py, images, sound
├── A0_Welcome/       # one directory per block, prefixed by part letter and block number
├── A1_The_PPF/
├── A_Skillsheet.typ  # part-level material sits beside its blocks, prefixed by the letter
├── B0_Markets/
├── ...
└── F3_Linked_Markets/
```

### File Descriptions

**00_Assets/**

- Contains original Jupyter notebooks (.ipynb files)
- Stores any additional resources, data files, or development materials
- Preserves the original work and experimental code

**01_Notes.md**

- The written narrative for the episode
- Markdown format for easy editing and version control
- Places each student-facing beat with a standard Markdown link such as `[▶ Beat 18](#beat-3.f)`
- Leaves the author's sentences unchanged; only the compact sequential label and exact dotted storyboard ID are inserted
- Omits production-only intro beats (`0.a`, `0.b`, …), which have no student-facing note landing

**02_Storyboard.md**

- Visual planning document describing key animation sequences
- Uses one dotted-ID heading per beat in playback order, for example `## 3.f · Draw the PPF`
- Contains the transitions, visual flow, and other on-screen action for each student note link, plus production-only `0.*` intro beats

**03_Code.py**

- Clean Python file containing Manim animation classes
- Includes configuration settings (colors, frame settings)
- Uses the same exact dotted IDs as the storyboard, including production-only `0.*` intro beats
- Ready to run with: `manim 03_Code.py ClassName`
- Header comment specifies the command for easy execution

**04_Final/**

- A directory containing Davinci Resolve resources for the final video
- Final rendered animation video Media.mp4

**Exercise/**

- The in-class Exercise set for the episode: `Exercise_<semester>.md` plus its rendered `Exercise_<semester>.pdf` (e.g. `Exercise_F26.md`)
- One Exercise set per episode, named by the semester it runs, so past semesters accumulate side by side
- The `.md` header carries a usage record: where each question is interleaved in `01_Notes.md`, what moved between episodes and why, and whether the PDF is stale and needs regeneration
- Older material stays in `classwork/` (legacy name) and `_archive/`; never deleted

### The Exercise Flow

Every class period has an exercise, baked into the episode itself. The in-class rhythm:

1. **Talk** — the episode's animation carries the ideas.
2. **Cut** — the screen cuts to a question. In `01_Notes.md`, a compact link such as `[▶ Beat 22](#beat-3.j)` sits immediately before the existing question heading and text. The dim/fade/board directions live under the matching dotted-ID heading in `02_Storyboard.md`.
3. **Board** — students work the question on paper; we build it on the board.
4. **Back** — return to the animation, and repeat.

Conventions that make this work:

- **Questions live in two places on purpose.** The `Exercise/` file is the printed handout; the copy in `01_Notes.md` is the script's cue (and flows into the animations). The Exercise file's header records the interleave points so the two stay in sync.
- **One arc per episode applies to exercises too.** A question belongs to the episode whose arc it exercises, not the episode it was historically written for — e.g. the old Classwork_A2 split across Exercise A2 (comparative advantage) and Exercise A3 (trade).
- **A continuing cast beats fresh setups.** Part A's exercises run one example (Hagrid → McGonagall) across all three episodes, so each class starts with the setup already in hand.
- **Exercises land after the concept is named**, not before — a question can't use a term the script hasn't defined yet.
