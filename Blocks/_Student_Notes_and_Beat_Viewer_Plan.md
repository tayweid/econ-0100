# Student Notes and Beat-Synchronized Viewer Plan

Status: implementation plan; A1 is the pilot episode

Prepared: 2026-08-31

Primary references: `_Storyboard_Template.md`, `_Parts.md`, and
`_Style_Guide.md`

## Goal

Publish each episode's notes as a clean student-facing document while keeping
all production choreography in the storyboard. The same notes source should
eventually drive a web view that places the current notes beside the animation,
follows playback, and lets a student select a moment to seek or step there.

There should be one hand-edited source for student prose and public beat
labels. HTML, Typst, JSON, search text, and timing indexes are generated
artifacts, never competing sources of truth.

## Settled source contract

### Student-facing beats are ordinary Markdown links

Place a play link at the exact point where a student-facing beat begins:

```md
[▶ Beat 18](#beat-3.f) These allocations lie on a line called Molly's
production possibility frontier.
```

The two halves have separate jobs:

- `▶ Beat 18` is the only public label. Its number is the beat's simple reading
  order in the student notes.
- `#beat-3.f` contains the exact local storyboard ID. The ID is available to a
  generator but does not appear in the rendered student text.

Do not pair the link with an HTML comment, an `Animation ·` kicker, a
descriptive label, or another copy of the prose. The standard Markdown link is
the single source of both the compact student control and the note landing.

The link may lead directly into a sentence, stand alone before a definition,
or supply the heading of a blockquote:

```md
[▶ Beat 4](#beat-1.d)

> **Opportunity cost** is the value of the next-best use of your resources.
```

```md
[▶ Beat 22](#beat-3.j) *Q1 | Hagrid's PPF*
```

Exercises and closing passages keep their original document treatment. A beat
link is inserted at the landing without rewriting their text.

Beat placement never authorizes new prose. Copy the author's narrative
verbatim, remove only explicit production directions whose actions are already
captured by the storyboard, and insert beat links. Do not add, rewrite, polish,
correct, summarize, or reorganize sentences.

### Dotted IDs describe the episode's teaching structure

Use local dotted IDs such as `3.a`, `3.b`, and `3.f` in playback order. The
number groups a coherent part of the lesson; the letter identifies a beat
within it. Once published or wired into code, an ID is a stable handle. Moving
prose does not rename it, and retired IDs are not reused.

Qualify the local ID with the episode code in generated data. For example,
A1's local `3.f` becomes `A1-3.f`.

### Beat zero is production-only

Opening bumper actions use `0.a`, `0.b`, and so on in the storyboard and code.
They do not get links in the notes because they have no student-facing prose
landing. A1 uses:

- `0.a` — wordmark;
- `0.b` — raster flicker;
- `0.c` — part, episode title, and thesis;
- `0.d` — `Last Time...` card.

The notes may still begin with their ordinary H1, thesis line, and `Last time`
heading. Those are document structure, not beat-zero controls.

### The storyboard owns action only

Every beat, including `0.*`, has one storyboard heading followed immediately
by its verb-first action list:

```md
# Episode A1 | Production Possibility Frontier | Storyboard

## 3.f · Draw the PPF

1. Draw Molly's PPF through the accumulated points.
2. Leave the completed frontier parked while the definition lands.
```

Do not add an **Action** label, metadata table, cue copy, narration, status,
delivery field, or duplicate student label. Camera changes, holds, transitions,
assets, and exact visual states belong in the action list when they are part of
what happens.

### Code and media converge on the same IDs

The final code convention is a comment rule and, where appropriate, a ManimL
checkpoint carrying the exact dotted ID:

```py
# ---- 3.f
self.pause("3.f")
```

The A1 pilot deliberately leaves the current `03_Code.py` untouched. Its old
`Bxx` names can be migrated later with the crosswalk below after the notes and
storyboard contract settles.

For rendered video, generate a timing index from the code or render process.
Do not hand-write timestamps in the notes or storyboard. The timing index must
include a render or media hash so stale times cannot silently attach to a new
render.

## Student rendering

The student sees the play symbol and short sequential label, never the dotted
production ID:

```text
▶ Beat 14
```

The plain Markdown link is the required fallback. Plass/Typst and the web
viewer may enhance it into a compact inline pill:

- one play symbol followed by `Beat N`;
- medium-weight, sentence-case text rather than a bold paragraph;
- a subtle blue-tinted fill, restrained outline, and fully rounded corners;
- enough contrast and keyboard focus to remain accessible;
- no reliance on color alone;
- no production language such as `CAM`, `ghost`, `box`, or `Animation ·`.

The enhanced style is generated from the link. Styling must never require a
second label in Typst, CSS, or JavaScript. With styling or JavaScript disabled,
the notes still read naturally.

## Parser and viewer contract

The first generator should:

1. Parse Markdown links whose destination matches `#beat-<dotted-id>`.
2. Preserve the destination exactly and derive the public label from the link
   text, removing only presentation markup and the leading play symbol.
3. Start the beat's local note span at the link and end it immediately before
   the next beat link.
4. Preserve the containing paragraph, definition, equation, exercise, or
   callout as context rather than emitting disconnected fragments.
5. Validate every note link against a storyboard heading in the same episode.
6. Accept storyboard-only `0.*` beats and mark them non-public instead of
   reporting them as missing notes.
7. Generate stable episode-qualified IDs and DOM anchors.

A minimal generated manifest can look like:

```json
{
  "episode": "A1",
  "beats": [
    {
      "id": "A1-0.a",
      "localId": "0.a",
      "public": false,
      "label": null,
      "anchor": null
    },
    {
      "id": "A1-3.f",
      "localId": "3.f",
      "public": true,
      "label": "Beat 18",
      "anchor": "beat-A1-3.f"
    }
  ]
}
```

During playback, the note span remains active while the beat animates and while
its final state is parked. Selecting the play control seeks or steps to the
start of that beat. Several code pauses may temporarily map to one conceptual
beat, but the notes and storyboard still expose one stable public control until
there is a pedagogical reason to split it.

## A1 pilot crosswalk

The migrated notes contain 38 student controls. The storyboard contains those
same 38 IDs plus four production-only `0.*` beats, for 42 beats total.

| Old code ID | New ID | Student control |
|---|---:|---|
| `B01` | `0.a` | production only — wordmark |
| `B01b` | `0.b` | production only — raster flicker |
| `B01c` | `0.c` | production only — part and thesis |
| `B02` | `0.d` | production only — Last Time card |
| `B03` | `1.a` | Beat 1 |
| `B03b` | `1.b` | Beat 2 |
| `B03c` | `1.c` | Beat 3 |
| `B04` | `1.d` | Beat 4 |
| `B04b` | `1.e` | Beat 5 |
| `B05` | `2.a` | Beat 6 |
| `B05b` | `2.b` | Beat 7 |
| `B05c` | `2.c` | Beat 8 |
| `B06` | `2.d` | Beat 9 |
| `B06b` | `2.e` | Beat 10 |
| `B06c` | `2.f` | Beat 11 |
| `B07` | `2.g` | Beat 12 |
| `B10` | `3.a` | Beat 13 |
| `B10b` | `3.b` | Beat 14 |
| `B11` | `3.c` | Beat 15 |
| `B11b` | `3.d` | Beat 16 |
| `B11c` | `3.e` | Beat 17 |
| `B12` | `3.f` | Beat 18 |
| `B13` | `3.g` | Beat 19 |
| `B13b` | `3.h` | Beat 20 |
| `B13c` | `3.i` | Beat 21 |
| `B14` | `3.j` | Beat 22 |
| `B20` | `4.a` | Beat 23 |
| `B20b` | `4.b` | Beat 24 |
| `B20c` | `4.c` | Beat 25 |
| `B20d` | `4.d` | Beat 26 |
| `B21` | `4.e` | Beat 27 |
| `B22` | `5.a` | Beat 28 |
| `B22b` | `5.b` | Beat 29 |
| `B23` | `5.c` | Beat 30 |
| `B23b` | `5.d` | Beat 31 |
| `B24` | `5.e` | Beat 32 |
| `B24b` | `5.f` | Beat 33 |
| `B24c` | `5.g` | Beat 34 |
| `B25` | `5.h` | Beat 35 |
| `B25b` | `6.a` | Beat 36 |
| `B30` | `6.b` | Beat 37 |
| `B31` | `6.c` | Beat 38 |

Retired `B13d` remains cut and should not receive a new ID.

## A1 files and preservation rule

The pilot lives in:

- `A/A1_The_PPF/01_Notes_new.md`;
- `A/A1_The_PPF/02_Storyboard_new.md`.

Keep `01_Notes.md`, `02_Storyboard.md`, and `03_Code.py` unchanged while the
new system settles. The `_new` suffix makes review and rollback straightforward.

## Implementation phases

### Phase 1 — Source migration

- Copy the original narrative into `01_Notes_new.md` verbatim, remove only the
  production-direction lines represented in the storyboard, and insert beats.
- Keep every non-intro beat as one semantic play link.
- Keep exercises verbatim with the current semester exercise file.
- Keep `02_Storyboard_new.md` action-only and validate its IDs against the
  notes links.

### Phase 2 — Plass/Typst enhancement

- Recognize beat links before ordinary link rendering.
- Turn them into an inline pill while retaining a real link/control target.
- Keep definitions, equations, exercises, and `Next` callouts as their own
  document semantics.
- Verify a full export visually, including line wrapping and page breaks.

### Phase 3 — Viewer generator

- Emit rendered notes and the beat manifest from the Markdown source.
- Add active-beat highlighting and click-to-seek behavior.
- Support keyboard navigation, visible focus, reduced motion, and a narrow
  screen layout.
- Keep the notes complete when animation or JavaScript is unavailable.

### Phase 4 — Code and timing integration

- Migrate A1's code IDs through the crosswalk in one pass.
- Emit beat-change events in the interactive viewer.
- Generate and validate timing indexes for rendered media.
- Reject stale indexes whose media hash no longer matches.

### Phase 5 — Course migration

- Migrate one episode at a time.
- Preserve legacy files until each replacement is reviewed.
- Do not leave one episode half on HTML markers and half on semantic links.

## Validation

The build should fail on:

- duplicate note links or storyboard headings;
- a non-`0.*` storyboard beat with no note link;
- a note link with no matching storyboard heading;
- a link fragment that does not preserve the exact dotted ID;
- duplicate, missing, or out-of-sequence `Beat N` labels;
- storyboard content outside a beat's action list;
- stale timing data or exercise-copy drift.

For A1 specifically, validation should confirm:

- exactly 38 note links and 42 storyboard headings;
- the only storyboard-only IDs are `0.a`, `0.b`, `0.c`, and `0.d`;
- all remaining IDs match in the same order;
- there are no `Bxx` IDs, HTML beat comments, or `Animation ·` kickers in either
  `_new` file;
- after removing beat links and the explicit production-direction lines, the
  narrative text matches `01_Notes.md` verbatim;
- the original notes, storyboard, and code remain untouched.

## Known A1 code caveats

These are code-integration issues, not reasons to weaken the source contract:

- the current `B01c` implementation contains a subtitle/thesis mismatch and
  bumper-centering differences;
- exercise cards currently contain hard-coded condensed text rather than being
  generated from the notes callouts;
- old `B20b`, `B20d`, `B24`, and `B24b` each contain two pauses under one
  conceptual beat;
- old `B01`, `B01b`, and `B31` do not expose independent pauses;
- the two camera stretches have useful note landings even though they do not
  correspond to an animated visual change.

Resolve those when code migration begins. Do not copy code quirks back into the
student notes or storyboard schema.

## Acceptance criteria

The pilot is ready for viewer work when:

- a student can read the notes without seeing stage management or production
  IDs;
- every visible play control is only `▶ Beat N`;
- every play control maps mechanically to one storyboard heading;
- intro bumper choreography exists only as `0.*` storyboard/code beats;
- the storyboard contains only action;
- the author's original prose remains verbatim apart from removed production
  directions and inserted beat controls;
- the same source can produce a readable Plass/Typst document and a structured
  side-panel manifest.
