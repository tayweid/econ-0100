# Public and private course repositories

This repository, `econ-0100`, is the canonical home for material that may be
published on the course website. Treat every committed file here as public,
even when the website does not currently link to it.

The adjacent `ECON_0100` repository is the private development side. Keep these
categories there:

- live MiniExams, other interesting assessments, rubrics, and any duplicate of
  an assessment artifact still in use;
- team documents, journals, planning notes, student records, and grading data;
- the historical Fall 2024 course tree and related 24F syllabus/simulation
  material;
- generated media caches, local shortcuts, credentials, and machine-specific
  files.

Homework and homework solutions may be public. The exception is a file that is
also an assessment artifact: the private classification follows the content,
not the filename or folder where a duplicate happens to live.

## Retired assessments are practice material

Past-semester MiniExam papers, their solutions, and their rubrics are published
as student practice once they are retired. The marker is location: a file under
an `_archive/` directory is treated as retired, and the boundary check exempts
it from the MiniExam, `me_`-prefix and rubric rules on that basis. The live
equivalents outside `_archive/` stay private, and `Parts/Z/` stays private
wherever it sits. Retiring a paper therefore means moving it into `_archive/`,
not renaming it.

Built presentation viewers are also public. `Parts/**/media/` is otherwise
development-only, with `*_present/` carved out, since that is what the site
links to for the animations.

## Normal workflow

Develop public-facing notes, storyboards, code, homework, solutions, specs,
syllabi, and simulations directly in this repository. Develop material that is
never meant for the website directly in `ECON_0100`. There is no recurring
whole-repository sync step.

Before committing public material, stage it and run:

```sh
scripts/check-public-boundary
```

The check rejects known private paths and exact-content copies of the private
assessment/planning artifacts present at the reorganization checkpoint. It is
a guardrail, not a substitute for reviewing what is being published.

The reorganization does not rewrite old public Git history. The boundary check
prevents new private material from being introduced from this point forward.
