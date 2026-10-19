# Issue tracker: Local markdown

Specs and tickets live under `.backlog/`.

## Conventions

- One feature per directory: `.backlog/<feature-slug>/`
- Spec: `.backlog/<feature-slug>/spec.md`
- Tickets: `.backlog/<feature-slug>/issues/<NN>-<slug>.md` (numbered from `01`)
- Status: `Status:` line near top (see `triage-labels.md`)
- Thread: append under `## Comments`

## When a skill says "publish to the backlog"

Apply **3-amigos** to the draft, then create files under `.backlog/<feature-slug>/`.

## When a skill says "fetch the relevant ticket"

Read the path or file the user gave.

## Epic duck operations

- **Map**: `.backlog/<effort>/map.md`
- **Child**: `.backlog/<effort>/issues/NN-<slug>.md` with `Type:` and `Status:`
- **Blocking**: `Blocked by: NN, NN` — unblocked when blockers are `resolved`
- **Frontier**: open, unblocked, unclaimed; lowest number first
- **Claim**: set `Status: claimed` before work
- **Resolve**: `## Answer`, `Status: resolved`, update map **Decisions so far**
