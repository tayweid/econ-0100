# Note to the animator agent working on B4 — the order fork, 2026-09-22 evening

Written by Claude (the Fable side of this project) at Taylor's request, after an
audit of `03_B4.py` / `02_Storyboard.md` against `../B3_Equilibrium/00_Outline.md`
and the restaged `01_Notes.md`. This note reports state; it carries **no new
direction from Taylor**. Where anything here conflicts with what Taylor tells
you directly, Taylor wins. Do not restructure the lesson on this note alone.

## The fork

Two B4 structures exist in this directory tonight, both dated today, both
citing Taylor:

- `01_Notes.md` (restaged with Taylor this afternoon, uncommitted) teaches
  **ceiling-first**: the pinned line motivates the welfare tools; the planner
  and the theorem are the punchline.
- `02_Storyboard.md` + `03_B4.py` (your commits) teach **planner-first**: the
  recap and planner establish the benchmark; the controls are applications.

Taylor has been shown both outlines side by side and will decide the order.
Until he does, the notes he would speak from and the animation he would click
through disagree on the arc, the hook, and the beat IDs.

## Outline A — the notes as restaged (ceiling-first, Lecture-08 arc)

1. **Hook** (`1.a`–`1.b`) — hold on B3's settled frame ($4, 40=40=40); "what if
   the government decided the price should be low?"; a lock appears at $3,
   proposed.
2. **A Price Ceiling** (`2.a`–`2.d`) — pin at $3; counts fill (Qd 45, Qs 20,
   Qx 20); Amanda-Grace's B3 deliberation card returns and her "offer $3.25"
   box gets ✗ not allowed; short-side Q&A; then the welfare question.
3. **CS / PS reviews** (`3.a`–`3.c`) — brisk B1/B2 replays on the sorted rows,
   with the rationing note; the overlay names welfare = CS + PS.
4. **Welfare at $3** (`4.a`–`4.b`) — areas redraw against the ghosted
   equilibrium; DWL named at the ceiling, gold card.
5. **A Price Floor** (`5.a`–`5.c`) — mirror at $6 (30/80); Andrew's "cut to
   $5.75" ✗ not allowed; smaller DWL triangle; excess callback.
6. **Planner → theorem** (`6.a`–`6.c`) — the lock comes off; slide the line
   with a live TS readout; max at $4; First Welfare Theorem + caveats + Smith
   riff; efficiency card.
7. **Closing** (`7.a`) — handoff to B5.

## Outline B — the animation as committed (planner-first)

1. **Seven-stage B3 recap** (`1.a`–`1.i.algebra`) — exchange, bidding, two
   trades, buyers, sellers, equilibrium with B3 Q2 interrupting before $4 is
   revealed, stability, graph + algebra.
2. **The welfare question** (`2.a`–`2.c`) — "Could we do better?"; pair-20
   gain-division close-up; the planner's two choices.
3. **Who should trade** (`3.a`–`3.e`) — Q fixed at 20; buyer and seller
   substitutions → highest-value buyers, lowest-cost sellers.
4. **How many trades** (`4.a`–`4.f`) — add pairs while MB > MC; pair 40 adds
   $0 (39/40 tie kept honest); pair 41 would lose $250; sweep shows the max.
5. **The market does it** (`5.a`–`5.d`) — $4 restored; same people, same
   quantity; First Welfare Theorem named with conditions.
6. **Controls as applications** (`6.a`–`6.exercise_floor`) — benchmark $195k;
   ceiling $3 (blocked bid, DWL $47.5k, Exercise Q1); floor $6 (blocked
   undercut, DWL $11.25k, Exercise Q2).
7. **Limits** (`7.a`) — "does efficiency settle the policy question?"

Shared either way: the numbers, the blocked-bid beats, the DWL geometry, the
recap assets. The reconciliation surface is the order of the middle, the hook,
where the CS/PS review lands, and the beat IDs.

## Order-independent items from the audit

1. `02_Storyboard.md` says 52 named holds; `03_B4.py` fires 53 —
   `1.c.sellers.high` is missing from the Runnable-scenes table and the
   section list.
2. The `03_01`–`03_09` snapshots are one design behind the combined file
   (the 20:51 commit touched only `03_B4.py`); sync them or mark them stale
   where the storyboard describes them.
3. Two grammar changes still need Taylor's explicit confirmation recorded in
   the storyboard's Direction section, the way the other confirmations are
   recorded: (a) unboxed decision close-ups — B3 outline decision #7 says
   boxed deliberations, and the restaged notes still direct "box gets ✗ not
   allowed"; (b) no price line through the plaza rows — outline §3 gives one
   red line the same meaning in the plaza and on every graph. If Taylor
   approved these in live review, say so there; if not, they are open.
4. For reference: a full-construct headless run tonight completed cleanly —
   all 53 pauses fired in storyboard order (~25 s with skip_animations). The
   storyboard's numerical reference was independently re-derived and is exact
   against `00_Outline.md` §4, including the ceiling/floor welfare totals and
   the marginal pairs 21/39/40/41.
