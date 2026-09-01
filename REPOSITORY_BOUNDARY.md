# Public and private course repositories

Everything committed to `econ-0100` is published. Treat every file here as
public, whether or not the website currently links to it.

Anything that should not be published goes in the adjacent `ECON_0100`
repository instead. That is the whole rule: **the repository a file lives in is
the decision**. There is no second classification step, no naming convention
that makes a file private, and no ignore rule standing in for judgement.

In practice `ECON_0100` holds live assessments, grading data, student records,
team and planning documents, and render output too large or too transient to be
worth publishing. But that list is a description, not a policy -- if something
belongs on the public side, move it here and commit it.

## The guardrail

`scripts/check-public-boundary` refuses exactly two things: credentials
(`.env`, `*.pem`, `*.key`) and per-student records (`roster*`, `grades*`,
`student_records*`). Those are never course material and cannot be unpublished
once pushed. Everything else is your call.

```sh
scripts/check-public-boundary            # staged changes
scripts/check-public-boundary --range <commit>
```

## `.gitignore`

One file, at the root. It excludes machine noise (`.DS_Store`), regenerable
build output (`*_checkpoints/`, `__pycache__/`), and credentials. It is not a
privacy mechanism -- material that should stay private belongs in `ECON_0100`,
where it is not one `git add -f` away from being published.

## History

The reorganization did not rewrite old public Git history, so material removed
from the tree may still be reachable in earlier commits.
