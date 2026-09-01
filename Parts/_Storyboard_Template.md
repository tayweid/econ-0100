# Storyboard Template

A storyboard maps each student beat link in `01_Notes.md` to its on-screen
action in `03_Code.py`. The notes establish the student-facing cue and episode
order. The storyboard contains only what happens.

## Beat links in the notes

Put a standard Markdown link at the exact place where each student-facing beat
begins:

```md
[▶ Beat 18](#beat-3.f)
```

The visible text is only the episode-local reading-order label `▶ Beat N`. The
fragment is `#beat-` followed by the beat's exact dotted storyboard ID. This
keeps production naming out of the notes while preserving an exact mapping.
The link may stand on its own before a block or lead directly into the sentence
it cues:

```md
[▶ Beat 14](#beat-3.b) If Molly grows only spinach, the other
endpoint is $(0,40)$.
```

The Markdown link is the single source of the public label and the beat
location. Do not add an HTML beat comment, an `Animation ·` kicker, or a second
copy of the label. A viewer may style the link as a chip and use its fragment
to seek the matching beat; ordinary Markdown, Plass, Typst, and print still
receive useful visible text.

Exercises and `Next` passages use the same link contract. The beat control sits
at the original prose landing without rewriting the heading or question:

```md
[▶ Beat 22](#beat-3.j) *Q1 | Hagrid's PPF*
```

Conventions:

- Every student-facing animation, camera, exercise, transition, or explanation
  beat gets one Markdown link in the notes.
- Visible labels are assigned consecutively in note order: `Beat 1`, `Beat 2`,
  and so on. They do not summarize or rewrite the surrounding prose.
- Student beat IDs use the dotted form shown in the storyboard, such as `3.f`.
  The link fragment must preserve that ID exactly: `#beat-3.f`.
- Beat IDs are stable handles, not headings or outline numbering. Note order is
  episode order. Do not renumber an established beat merely because prose
  moves, and do not reuse a removed ID.
- IDs are scoped to one episode. A combined public view may qualify `3.f` with
  the episode code internally, but the source link remains `#beat-3.f`.
- A beat names a synchronized stretch, not necessarily one button press. Keep
  repeated presses in one beat unless separate synchronization is useful.
- Production-only intro beats use `0.a`, `0.b`, and so on in storyboard and
  code. They are absent from the student notes because they have no
  student-facing prose landing.

## Storyboard shape

Use one heading per beat, in note order. A short production title after the ID
is optional. Write the action directly beneath the heading as a verb-first list.
Because action is the storyboard's only content, do not add an **Action** label.

```md
# Episode [code] | [title] | Storyboard

## 0.a · [production-only intro action]

1. [Verb-first intro action.]
2. [Continue to the next production-only intro beat.]

## 1.a · [optional short production title]

1. [Verb-first action.]
2. [Next action, in execution order.]
3. [Final state that remains parked while the narration continues.]

## 1.b

- Hold full-frame camera through the marked stretch of prose.

## 1.c · [optional short production title]

- [Verb-first action.]
```

The list may be one line for a rough beat or as detailed as the choreography
requires. Camera changes, holds, loops, on-screen text, transitions, and asset
use belong in the list when they are part of what happens. Do not add separate
fields for cue, mode, scene, status, delivery, production notes, assets, or open
questions.

## Example

```md
# Episode A1 | Production Possibility Frontier | Storyboard

## 3.a · Axes and first endpoint

1. Grow axes beside the farm, carrots horizontal and spinach vertical.
2. Restore the farm at all-carrots.
3. Place the live `(C, S)` dot and readout at `(10, 0)`.

## 3.b · Second endpoint

1. Morph the farm from all-carrots to all-spinach.
2. Ride the live dot to `(0, 40)`.
3. Leave the second point marked.

## 3.f · Draw the PPF

1. Draw Molly's PPF through the accumulated points.
2. Leave the completed frontier parked while the definition lands.
```

The matching notes retain these beats without carrying the choreography:

```md
[▶ Beat 13](#beat-3.a) Put carrots, $C$, on the horizontal axis
and spinach, $S$, on the vertical axis. If Molly grows only carrots, the first
endpoint is $(10,0)$.

[▶ Beat 14](#beat-3.b) If she grows only spinach, the other
endpoint is $(0,40)$.

[▶ Beat 18](#beat-3.f) These allocations lie on a line called Molly's
production possibility frontier.
```

## Migration

Migrate one episode at a time:

1. Move every action that exists only in `01_Notes.md` into its beat section.
2. Preserve the author's narrative verbatim; do not add, rewrite, polish, or
   correct sentences while placing beats.
3. Add one sequential `▶ Beat N` Markdown link for every student-facing beat.
4. Remove the old `***Show…***`, `***Cut…***`, `[to camera]`, and `~` notes once
   their actions have a home.
5. Move production-only intro actions to `0.a`, `0.b`, and so on in storyboard
   and code; do not add corresponding links to the student notes.

An episode may keep the older convention while its storyboard is still a
placeholder. Do not leave half of one action in each file.
