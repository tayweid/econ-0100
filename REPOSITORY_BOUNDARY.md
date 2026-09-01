# Public and private course repositories

This repository, `econ-0100`, is the canonical home for material that may be
published on the course website. Treat every committed file here as public,
even when the website does not currently link to it.

The adjacent `ECON_0100` repository is the private development side. Keep these
categories there:

- MiniExams, other interesting assessments, rubrics, and any duplicate of an
  assessment artifact;
- team documents, journals, planning notes, student records, and grading data;
- the historical Fall 2024 course tree and related 24F syllabus/simulation
  material;
- generated media caches, local shortcuts, credentials, and machine-specific
  files.

Homework and homework solutions may be public. The exception is a file that is
also an assessment artifact: the private classification follows the content,
not the filename or folder where a duplicate happens to live.

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
