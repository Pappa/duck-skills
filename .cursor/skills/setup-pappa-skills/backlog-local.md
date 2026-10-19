# Issue tracker: Local markdown

Specs and tickets live under `.scratch/`.

## Conventions

- One feature per directory: `.scratch/<feature-slug>/`
- Spec: `.scratch/<feature-slug>/spec.md`
- Tickets: `.scratch/<feature-slug>/issues/<NN>-<slug>.md` (numbered from `01`)
- Status: `Status:` line near top (see `triage-labels.md`)
- Thread: append under `## Comments`

## When a skill says "publish to the issue tracker"

Apply **3-amigos** to the draft, then create files under `.scratch/<feature-slug>/`.

## When a skill says "fetch the relevant ticket"

Read the path or file the user gave.

## Epic duck operations

- **Map**: `.scratch/<effort>/map.md`
- **Child**: `.scratch/<effort>/issues/NN-<slug>.md` with `Type:` and `Status:`
- **Blocking**: `Blocked by: NN, NN` — unblocked when blockers are `resolved`
- **Frontier**: open, unblocked, unclaimed; lowest number first
- **Claim**: set `Status: claimed` before work
- **Resolve**: `## Answer`, `Status: resolved`, update map **Decisions so far**
