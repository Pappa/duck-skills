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

duck-skills expect `docs/agents/backlog.md` (and usually `domain.md`). Run once per repository:

```
/setup-duck-skills
```

Supports GitHub, GitLab, Azure DevOps Boards, local markdown, or a custom tracker.

## Skills catalog

### User-invoked skills

| Skill               | Purpose |
|---------------------|---------|
| `setup-duck-skills` | Configure tracker, domain docs, ticket status vocabulary |
| `epic-duck`         | Large, unclear work → feature plan + **planning** backlog items (`Type: epic-duck:*`) |
| `rubber-duck`       | Single-session outcomes: clarity, docs/code, **implementation** `Type: task` / `Type: spike` |

### Composed skills (not user entry points)

Used inside **epic-duck** or **rubber-duck** only:

| Skill            | Purpose |
|------------------|---------|
| `question-duck`  | Round-based design interview |
| `architect-duck` | Glossary and ADR updates while designing |

### Other skills (model may invoke)

| Skill        | Purpose |
|--------------|---------|
| `amigo-duck` | Backlog ticket quality before publish |
| `spike-duck` | Time-boxed investigation; findings as Markdown |


## Typical planning flow

```mermaid
flowchart LR
  big[Large or unclear work]
  small[Single-session outcome]
  plan[Feature plan]
  planItems[Planning items epic-duck:*]
  implItems[Implementation task or spike]
  ed[epic-duck]
  rd[rubber-duck]
  big --> ed --> plan --> planItems
  small --> rd --> implItems
```

- **epic-duck** — chart a feature and resolve **planning** decisions, tasks, and spikes on the backlog.
- **rubber-duck** — one session: shared understanding, domain docs, or **implementation** backlog items (not planning `epic-duck:decision` items).

## Roadmap

Planned next batches: build (`implement`, `tdd`), quality (`code-review`, `diagnosing-bugs`), ship (`pr`, CI loop).
