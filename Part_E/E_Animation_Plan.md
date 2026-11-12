# Part E animations: where things stand (2026-11-12)

This replaces the October 30 build record, which is in this file's git history. Each block has one animation and one notes file; the notes carry the storyboard as short comment tables after the paragraphs that cue them (`_Style_Guide.md` §8, storyboard and code).

| Block | Animation, scene | Holds | Notes | Market |
| --- | --- | --- | --- | --- |
| E0 Overview | `E0_Sellers/E0_Animation.py`, `EpisodeE0` | 33 | `E0_Notes.md` | none: the semester recap and the production simulation |
| E1 Costs | `E1_Costs/E1_Animation.py`, `EpisodeE1` | 48 | `E1_Notes.md` | the firm only |
| E2 Competitive Firms | `E2_Competition/E2_Animation.py`, `EpisodeE2` | 85 | `E2_Notes.md` | shared line, read in thousands |
| E3 Monopoly | `E3_Monopoly/E3_Animation.py`, `EpisodeE3` | 30 | `E3_Notes.md` | shared line, in units |
| E4 Duopoly | `E4_Duopoly/E4_Animation.py`, `EpisodeE4` | 26 | `E4_Notes.md` | shared line, in units |
| E5 Wrap-Up | `E5_Wrap_Up/E5_Animation.py`, `EpisodeE5` | 30 | `E5_Notes.md` | shared line, in units and in thousands |

Open one in the viewer from the repo root, for example:

```
maniml Part_E/E3_Monopoly/E3_Animation.py EpisodeE3
```

## One firm and one demand line

- **The firm (E1 to E5):** production Q = 10√L, a \$100 wage and \$1,000 fixed cost, so TC = 1,000 + q², MC = 2q, AVC = q, ATC = q + 1,000/q, lowest at 63.25 where q = 31.6.
- **The demand line (E2 to E5):** P = 120 − Q. E2 reads Q in thousands, because many price takers need a large market. E3 and E4 read it in units, because one or two firms with these costs fit a small one. E5 uses both and says so.
- **E2:** at a price of 100 the firm makes 50 units, ATC 70, profit 1,500. Entry lowers the price to 63.25 and profit to zero. No number E2 displays depends on the slope of demand.
- **E3:** MR = 120 − 2Q. q\* = 30, P\* = 90, ATC\* = 63.33, profit 800; efficient quantity 40. Policies: tax 20, lump sum 500, subsidy 40, subsidy with a lump sum of 1,800.
- **E4:** BR_A: q_A = 30 − ¼q_B. Nash equilibrium 24 each, 48 in total, price 72. The monopoly recap is E3's answer.
- **E5:** the same monopoly and duopoly; the competitive section solves E2's example at 100 and rolls to the long run; n sellers give q = 120/(n + 3), shown for n = 1, 2, 3, 7, 17.

## What is open

1. **Prose.** E3 is still the 2020 dictation. E4's prose stops at "best response", and E5 has none of Taylor's; both are filled with marked additions. E1 is the old video script with a few marked bridges. E0's checkpoint paragraphs are marked additions to check against the policy.
2. **Exercises.** E1 and E2 have an `Exercise/` folder and exercise cards in the animation. E3 and E4 have warmups and board questions only in their notes.
3. **E5 More Sellers.** The sweep to 17 sellers ignores the fixed cost; on this market a third seller would lose money. Whether the section stays is Taylor's call.
4. **E4 naming.** The notes are titled Oligopoly; the folder and the animation say Duopoly.
5. **Conventions.** E2 uses yellow notes, rounded readouts and exercise cards. E3 to E5 keep one gold line at the bottom, two-decimal readouts and a side panel.
6. **Timing.** The timing tables in E3 and E4 are untested proposals; E2's later rows are estimates since its sections were reordered.
7. **Plass.** The round-trip check has not been run on the notes since November 11.

## Where older material is

- Each block's `_archive/` has a dated folder with the notes, storyboards and builds that came before: `2026-11-09_consolidation` for E2 and `2026-11-11_consolidation` for E0, E1, E3, E4 and E5.
- The ports of the old 2020 code that run in ManimL: `E1_Costs/_archive/2026-11-11_consolidation/E1_Animation_original.py`, `E2_Competition/_archive/2026-11-09_consolidation/E2_Animation_original.py`, and `E3_Monopoly/_archive/2026-11-11_consolidation/E3_Animation_original.py`.
- Monopolistic competition is not taught this semester. Its notes, notebook, the unplaced fragments from E3 and a live copy of the E3 port (which holds the old entry-and-exit scenes) are in `EX_Monopolistic_Competition/`.
- The handwritten sheet "Example: Three Market Structures" is `E5_Wrap_Up/E5_Handwritten_Three_Markets.pdf`. E4 and E5 follow its steps on the shared market; the builds on the sheet's own numbers are in their archives.
