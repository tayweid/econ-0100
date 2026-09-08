# Notes | Demo A

Claude's working notes on `Demo_A.typ`. Kept here because Plass drops Typst comments on save; the comment block inside the `.typ` will disappear the first time it is saved from Plass. Never opened in Plass. Updated 2026-09-07.

## Provenance

The F24 Demo A, Colin Creevey (20 pasties or 5 cakes) and Katie Bell (15 pasties or 8 cakes), verbatim, in the Checkpoint layout, split along skill lines: old Q1 became Q1 and Q2(a); old Q2 became Q2(b); old Q3 became Q3; old Q4 became Q4(a); old Q5 became Q2(c) and Q4(b). Stems are restated so each question stands alone. Sub-part letters and headings are the only additions. Source: `ECON_0100/Checkpoints/A/_Archive/24F_Demo_A.md`, with Q2 and Q3 wording taken from the exam versions because the F24 Demo's Q2 asked yes/no attainability and its Q3 sentence was garbled. Solutions to the unsplit original: `_Archive/Demo_A_sols.pdf`, the scanned "Taylor's Version".

The intro carries both the Checkpoint boilerplate (Checkpoint and 20 minutes substituted) and the Demo paragraph ("Demos are similar to Checkpoints"), with the email dropped and "classmakes" corrected. The sentence "Each question is labeled with the skill it practices from Skillsheet A" is Claude's, kept at Taylor's request.

## Additions of 2026-09-07, tagged *[Claude]* in the file

Taylor asked for Wednesday's question types to appear on the Demo so students have seen them before the Checkpoint. Each added item is prefixed *[Claude]* in the `.typ` for Taylor to rewrite and untag. They copy the Arthur exam's wording with Colin's numbers.

- **Q2(c)–(e)**, yes/no attainability of 20 pasties, 20 pasties and 1 cake, 19 pasties. Answers: yes (efficient), no, yes (inefficient).
- **Q2(f)–(g)**, shift versus pivot. The lead-in states that 8 pasties and 3 cakes is efficient, which it is (frontier 20 − 4·3 = 8). Tripling pasties pivots the frontier out, so the point becomes inefficient. Cutting labor shifts it in, so the point becomes unattainable.
- **Q4 opportunity cost table**, given so that Q4 stands alone and so students meet the read-a-given-table type. Values: Colin 1/4 cake per pasty, 4 pasties per cake; Katie 8/15 cake per pasty, 15/8 pasties per cake.
- **Q4(a)**, who specializes in cakes: Katie (15/8 < 4).
- **Q4(c)**, select-all rates for 1 cake: 2 and 3 pasties work (range 15/8 to 4); 1 and 5 do not. Two correct options, where the F24 lists had one.

Sub-parts were re-lettered: old Q2(c) is now Q2(h), old Q4(a) is now Q4(b), old Q4(b) is now Q4(d).

## Answer checks

Q1: 4 P. Q2(b): inefficient (frontier is 12 P at 2 C). Q2(c): the 8-hour PPF has intercepts 32 P and 8 C, parallel to the old one. Q3: AA in pasties Colin, CA in pasties Colin (OC of a pasty is 1/4 C for Colin, 8/15 C for Katie). Q4(a): any rate between 15/8 and 4 pasties per cake, so 2 or 3 pasties. Q4(b): still 4 P; the hours change shifts the PPF without changing the slope.

## Known issues

- Demo A is Vignettes A1–A3 word for word, so it adds no new rep and sits closer to practice than rule 1 wants.
- Demo A is Demo-shaped and Checkpoint versions 1 and 2 are Arthur-shaped; see `ECON_0100/Checkpoints/A/Checkpoint_A_notes.md`.
- The website link in `course-content.yaml.js` points at `Blocks/A_MiniExam/Demo_A.pdf`, which is exported from Plass and does not exist until that export happens. `scripts/check-course` reports it missing until then.

## Uncovered bullets

For Taylor to write: A1.1 next best alternative and reciprocals; A1.2 slope as the OC of the horizontal good, and pivot from technology; A2.1 AA and CA in cakes, and AA in both but one CA each (Colin has AA in pasties and Katie in cakes, so the numbers can't show it); A3.1 who specializes, the range of rates, beyond autarky and who rejects, and the effect of the capacity change on the trade.
