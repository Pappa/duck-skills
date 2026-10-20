# duck-skills

Personal agent skills for software engineering — heavily influenced by (like, copied from) [Matt Pocock's skills](https://github.com/mattpocock/skills), rewritten for my workflow.

## Why "duck" skills?

The name comes from the practice of ["rubber ducking"](https://en.wikipedia.org/wiki/Rubber_duck_debugging) in Software Engineering, originally described in [The Pragmatic Programmer](https://en.wikipedia.org/wiki/The_Pragmatic_Programmer) by Andrew Hunt and David Thomas. It refers to solving problems by simply explaining the problem to another person (or originally an actual rubber duck). In the process of articulating the problem, we very often find the solution without any actual input from the "duck". In practice, people often use the term to also mean hashing out ideas together.

But mostly, I just needed to find some skill names that didn't clash with other commonly used skills.

## Use in this repo

Skills live in **`.cursor/skills/`**. Open this repository in Cursor and invoke with `/skill-name` or attach the skill in chat — no symlink needed while iterating here.

## Use in other repos

Symlink individual skills (or the whole folder) into `~/.cursor/skills/`:

```bash
ln -sfn "$(pwd)/.cursor/skills/rubber-duck" ~/.cursor/skills/rubber-duck
```

## Per-repo setup

Planning skills expect `docs/agents/backlog.md` (and usually `domain.md`). Run once per repository:

```
/setup-duck-skills
```

Supports GitHub, GitLab, Azure DevOps Boards, local markdown, or a custom tracker.

## Skills catalog

### User-invoked skills

| Skill               | Purpose |
|---------------------|---------|
| `setup-duck-skills` | Configure tracker, domain docs, optional ticket labels |
| `epic-duck`         | Large, unclear or ambiguous piece of work → feature plan + decision issues on tracker |
| `rubber-duck`       | Design interview + glossary/ADR updates (`interrogate` + `architect-duck`) |

### Model-invoked skills

| Skill               | Purpose |
|---------------------|---------|
| `interrogate`       | Round-based design interview |
| `architect-duck`    | Glossary and ADR updates while designing |
| `amigo-pato`        | Backlog ticket quality (fit, clarity, ISO 24495, INVEST) before publish |
| `spike-duck`        | Time-boxed investigation; findings as Markdown in the repo |


## Typical planning flow

```mermaid
flowchart LR
  idea[Big, complex idea]
  idea2[Small, single-ticket idea]
  plan[Feature plan]
  issues[Issues on backlog]
  ed[epic-duck]
  rd[rubber-duck]
  dd[dev-duck (TODO)]
  idea --> ed --> plan --> issues --> dd
  idea2 --> rd --> issues --> dd
```

- **Small enough to complete in one session**: `rubber-duck` (terms and ADRs as you decide)
- **Large, unclear or ambiguous piece of work**: `epic-duck` to chart a feature, then `rubber-duck` on individual issues

## Roadmap

Planned next batches: build (`implement`, `tdd`), quality (`code-review`, `diagnosing-bugs`), ship (`pr`, CI loop).
