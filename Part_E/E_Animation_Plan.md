# Part E animation push: where things stand (2026-10-30)

Five blocks, one animation each. Every file below renders headlessly in the ManimLive engine;
nothing is committed. The old `01_Notes.md`, `02_Storyboard.md` and `03_Code.py` in each block are
untouched.

| Block | Class (course page) | Modern animation | Holds | Original port |
|---|---|---|---|---|
| E1 Costs | Mon Nov 2 | `E1_Costs/E1_Animation.py`, `EpisodeE1` | 56 | `E1_Animation_original.py` |
| E2 Competitive Firms | Wed Nov 4 | `E2_Competition/E2_Animation.py`, `EpisodeE2` | 43 | `E2_Animation_original.py` |
| E3 Monopoly | Mon Nov 9 | `E3_Monopoly/E3_Animation.py`, `EpisodeE3` | 30 | `E3_Animation_original.py` |
| E4 Duopoly | Wed Nov 11 | `E4_Duopoly/E4_Animation.py`, `EpisodeE4` | 26 | none: the old episode was the handwritten sheet |
| E5 Wrap-Up | if time | `E5_Wrap_Up/E5_Animation.py`, `EpisodeE5` (new folder) | 30 | none |

Open one in the viewer from the repo root, for example:

```
maniml Part_E/E1_Costs/E1_Animation.py EpisodeE1
```

Each modern file has a storyboard companion, `E<n>_Notes.md`. For E1–E4 it is your `01_Notes.md`,
byte for byte, plus Plass comments: a top comment (file and scene, model numbers, what came from the old
animation, **Choices left for Taylor**) and one comment per section listing its beats as built and what is
**Not built**. E5 has no notes yet, so its file is storyboard only (C4's format). All five pass Plass's
round-trip check.

## The originals (`E<n>_Animation_original.py`)

The old code as it was, made to run: old manim's `GraphScene` and `TextMobject` are rebuilt at the top of
each file, and the lost `tutorials.py` settings are reconstructed from the 2020 video thumbnails. Choreography,
wording, numbers and colors are unchanged; every judgment call is marked `# PORT`.

- **E1**: `CostsA` (production function → total cost; its class header was lost, rebuilt), `CostsB` (the
  2020 "Tutorial 5.1 | Production Costs" video: TC, the rise/run MC sweep, the cost equations, MC/ATC/AVC,
  "In the long run all costs are variable."), and the later CE scenes `animation_0`–`animation_4`
  (0 is the stale "Part D | Sellers" outline; 1 is the production-function → costs rewrite; 2–4 are stubs).
- **E2**: `PerfectCompA` (the 2020 "Tutorial 5.2" video: costs, P = 80, the profit box sweep) and
  `PerfectCompB` (firm beside market, entry/exit cycles).
- **E3**: `Monopoly` (the old construct only ran its intro), `MonopolyPreview` (labeled: runs Monopoly's
  uncalled methods, which turned out to be copies of the competitive-firm code), `MonopolisticComp` (the
  monopoly picture from the 2020 video, p = 75, q = 50, Π = 1500, then monopolistic-competition entry/exit
  with and without a tax) and `MonopolisticCompB` (its outro bullets).

## Models of record

- **E1–E3 (from the old code):** MC = q, ATC = q/2 + 1000/q, AVC = q/2, FC = 1,000. E1 derives these from
  F(L) = 10√L with w = $50 per worker (new: chosen so the production function produces the old costs).
  E2: P = 80 → q = 80, profit 2,200; long run P = √2000 ≈ 44.72. E3: D: P = 100 − Q/2, MR = 100 − Q,
  q* = 50, P* = 75, ATC* = 45, profit 1,500; Q_sp = 66.7.
- **E4–E5 (your handwritten sheet):** D: P = 200 − Q/2, every firm MC = 20 + q. Monopoly 90 / 155;
  duopoly BR_A: q_A = 90 − ¼q_B, Nash 72 / 72, Q = 144, P = 128; competitive (10 firms) Q = 300, P = 50,
  q = 30. FC = 450 is inferred (not on the sheet) so the competitive firm's long run sits at minimum ATC.
  E5's "through n": q = 360/(n + 3), and the markup P − MC = q/2 shrinks as sellers are added
  (n = 1, 2, 3, 6, 15).

## Shared choices across the five files

Each is a constant at the top of `construct()`, so it changes in one place:

- Colors: MC orange; ATC and TC purple ("total"); AVC and VC pink; AFC and FC grey; demand / P = MR teal;
  monopoly MR pink; profit fill orange; loss red; tax revenue green; DWL grey. In E4, firm A is pink and
  firm B teal, as in Part D's games.
- The market-structures grid (sellers × homogeneous/differentiated) is built in E1 and reused at the top of
  E2–E4 with that block's cell boxed (D2's taxonomy pattern).
- Your sheet's five-step "Firm's Problem" card appears in E4 and E5 with the same wording (E3 shows
  steps 1–4, since its notes have no entry/exit).

## Decisions for you, roughly in order of impact

1. **One market for all of Part E?** E1–E3 use the old code's firm; E4–E5 use the sheet's market. They
   could share one, so the monopoly in E3 is the monopoly in E5.
2. **AVC is a straight line in the old model**, so "MC runs through the minimum of AVC" and a shutdown
   price below AVC can't be shown (E1 and E2 build the ATC versions and say so). A cubic VC would fix both.
3. **FC = 1,000 puts the long-run price at 44.72.** FC = 800 makes it exactly 40.
4. **Marginal three-stage framing** (close-up → one unit on the graph → the market), the Part C core idea,
   is not built here. Natural places: E1 4.d (MB vs MC bars), E2 2.d ("should we increase our quantity by
   10?"), E3 section 2 (MR from two points).
5. **On-screen lines the builders wrote.** Every bottom line not taken from your notes is listed under
   "Choices left for Taylor" in that block's storyboard.
6. E5 has no thesis line yet. Its n = 15 stop lands on the same outcome as the sheet's 10 price takers
   (a coincidence of the numbers); n = 12 is the suggested alternative.
7. The colors above, and whether loss should be red.

## Suggested order for the push

E1 first (Monday): open `EpisodeE1` in the viewer beside `E1_Notes.md`, react to the beats, and keep the
storyboard comments in step with each change. Then E2, E3, E4. E5 can wait until the four class blocks are
settled.
