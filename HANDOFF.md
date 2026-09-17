# Handoff: Plass-native solution guides (2026-09-17)

Written by Claude at the end of a session on the office machine so the work can
be finished at home in a new session. Delete this file when done.

## What this is

The solution guides for the A and B assignments were rewritten as Plass-native
Typst, one self-contained `.typ` per assignment (Taylor: "i want one file per
solution guide with everything in it, one per assignment"). The design is
recorded in the "Solution guides" bullet of `Blocks/_Style_Guide.md` (section
11); read that first.

## State of the working tree

All of this is UNCOMMITTED in the main checkout. Commit and push with GitHub
Desktop, then pull at home.

Modified: the nine guides, `Blocks/_Assets/sols.typ`, `Blocks/_Style_Guide.md`.
New: `scripts/render-sols-figures`.

The guides:

- `Blocks/A1_The_PPF/Vignette/Vignette_A1_sols.typ`
- `Blocks/A2_Advantage/Homework/Homework_A2_sols.typ`
- `Blocks/A2_Advantage/Vignette/Vignette_A2_sols.typ` (no graphs)
- `Blocks/A3_Trade/Homework/Homework_A3_sols.typ`
- `Blocks/A3_Trade/Vignette/Vignette_A3_sols.typ`
- `Blocks/B1_Demand/Homework/Homework_B1_sols.typ`
- `Blocks/B2_Supply/Homework/Homework_B2_sols.typ`
- `Blocks/B2_Supply/Vignette/Vignette_B2_sols.typ`
- `Recitations/Week_2_sols.typ` (the three A vignettes, one per page)

Each guide: handout preamble (no equation numbering), title with
`| Solutions`, the handout's question text and blanks, and after each question
a red Plass solution block. Graphs are embedded as base64 SVG data URLs in
`#image(...)`. The Typst that draws the graphs sits at the END of the same file
in a Plass comment frame (`// plass:comment` ... `// | line` ...
`// /plass:comment`), which Plass shows as a note and leaves out of the PDF.
The frame imports `Blocks/_Assets/sols.typ` (graph, seg, pt, shade, lbl,
sol-color) and draws one graph per page in `#image` order.

`scripts/render-sols-figures` (Python, needs `typst` on PATH) extracts each
guide's frame, compiles it, and replaces the n-th `#image` with the n-th page.
Last run: every guide reported "(unchanged)", i.e. the frames reproduce the
embedded SVGs byte for byte.

Removed this session (they were untracked, so nothing to revert): the seven
`*_sols_figures.typ` companions and `scripts/assemble-recitation-sols`.

## Two decisions Taylor has not confirmed

1. `Recitations/Week_2_sols.typ` is no longer assembled by a script. It is a
   standalone copy of the three vignette guides with its own frame (A1 and A3
   graphs). A change to a vignette guide has to be made there too. If you
   would rather have it assembled, a small script is easy to restore.
2. The graph helpers stay shared in `Blocks/_Assets/sols.typ` rather than
   being copied into each frame. Plass never compiles the frame, so each
   guide still opens and exports alone.

## A bug found and fixed

Plass's serializer (its PDF export path) throws on a table cell whose math is
inside a mark, e.g. `[*Frogs ($F$)*]`. The A2 and A3 homework guides had this
in table headers; changed to `[*Frogs* ($F$)]`. Rule added to the style guide.

## Still to do

- Re-export the nine `*_sols.pdf` files from Plass; they are stale. Local
  typst 0.15 cannot compile the guides (mitex fails with `unknown variable:
  kai`), so PDFs come only from Plass.
- Open one or two guides in Plass and eyeball the note strip at the end and
  the graphs.
- Commit; delete this file.

## How to verify a guide with Plass's own importer

```bash
git clone --depth 1 https://github.com/tayweid/plass && cd plass && npm ci --ignore-scripts
```

Save the script below as `verify-guides.ts` in the clone, then:

```bash
npx tsx verify-guides.ts /path/to/econ-0100/Blocks/*/*/*_sols.typ /path/to/econ-0100/Recitations/Week_2_sols.typ
```

A clean guide prints `OK` with warnings=0, islands=0, inline=0, both round
trips true, and no serialize error. Last run: all nine OK.

```ts
// Check ECON 0100 solution guides with Plass's own importer: print warnings,
// raw-Typst islands, inline Typst nodes, comment frames, and whether the
// comment payloads and data-URL images survive a parse -> serialize round trip.
import { readFileSync } from 'node:fs';
import { typToDoc } from './src/typ-parser';
import { docToTyp } from './src/typ-serializer';
import { readTypComment } from './src/editor-comments-format';

function frames(src: string): string[] {
  const lines = src.split('\n'); const out: string[] = [];
  for (let i = 0; i < lines.length; i++) { const f = readTypComment(lines, i); if (f) { out.push(f.text); i = f.next - 1; } }
  return out;
}
let bad = 0;
for (const file of process.argv.slice(2)) {
  const src = readFileSync(file, 'utf8');
  const { doc, warnings } = typToDoc(src);
  const islands: string[] = []; let inline = 0; let comments = 0; let images = 0;
  doc.descendants((n) => {
    if (n.type.name === 'code_block' && n.attrs.params === 'typst-raw') islands.push(n.textContent.slice(0, 60));
    if (n.type.name === 'typst_inline') inline++;
    if (n.type.name === 'editor_comment') comments++;
    if (n.type.name === 'image' || n.type.name === 'figure') images++;
  });
  let again = ''; let serr = '';
  try { again = docToTyp(doc); docToTyp(doc, { islands: 'print' } as any); } catch (e) { serr = String((e as Error).message); }
  const f1 = frames(src), f2 = frames(again);
  const framesOk = JSON.stringify(f1) === JSON.stringify(f2);
  const imgOk = (src.match(/data:image\/svg\+xml;base64,[A-Za-z0-9+/=]+/g) ?? []).join() === (again.match(/data:image\/svg\+xml;base64,[A-Za-z0-9+/=]+/g) ?? []).join();
  const ok = warnings.length === 0 && islands.length === 0 && inline === 0 && framesOk && imgOk && !serr;
  if (!ok) bad++;
  console.log(`${ok ? 'OK  ' : 'FAIL'} ${file}: warnings=${warnings.length} islands=${islands.length} inline=${inline} comments=${comments} images=${images} framesRoundTrip=${framesOk} imagesRoundTrip=${imgOk}`);
  if (serr) console.log('   serialize error:', serr);
  for (const w of warnings) console.log('   warning:', w);
  for (const s of islands) console.log('   island:', JSON.stringify(s));
}
process.exit(bad ? 1 : 0);
```
