# Issue tracker: Local markdown

Plans, spikes and issues live under `.backlog/`.

## Conventions

### Index

- **Plan list**: `.backlog/features.md` — markdown table with columns **Plan**, **Overview**, **Status**.
  - **Plan**: link to the feature file, e.g. `[0003-plan-auth.md](items/0003-plan-auth.md)`.
  - **Overview**: one sentence (same as **Destination** on the feature file).
  - **Status**: one of `needs-detail`, `in-progress`, `resolved`, `out-of-scope`.

### Shared numbering

All backlog items share one counter under `.backlog/items/`. Next number = one greater than the highest existing `NNNN` prefix (four digits, from `0001`). Deleted numbers are never reused.

| Kind | Path |
|------|------|
| Plan | `.backlog/items/<NNNN>-plan-<feature-slug>.md` |
| Issue | `.backlog/items/<NNNN>-<slug>.md` — slug must **not** start with `feature-` or `spike-` |
| Spike (item) | `.backlog/items/<NNNN>-spike-<slug>.md` |
| Spike (findings) | `.backlog/spike/<NNNN>-<slug>.md` |

### Status (features, issues, spikes)

`needs-detail` · `in-progress` · `resolved` · `out-of-scope`

- **Canonical**: `Status:` near the top of each item file. Update `features.md` and the feature’s **Issues** / **Spikes** tables in the same edit.
- **Plan**: starts `needs-detail`; becomes `in-progress` when the first child issue or spike is created; `resolved` / `out-of-scope` only by explicit choice (see epic duck).
- **Issue / spike**: set `in-progress` when work starts; `resolved` when done (spike item when the result file exists).

### Ticket labels

Deliverable / agent-ready work may also use roles from `docs/agents/ticket-labels.md` (e.g. `Label: ready`) — separate from the four statuses above.

### Plan file body

Order of sections:

1. `Status:` (and optional metadata lines)
2. **Destination**
3. **Notes**
4. **Decisions so far**
5. **Not yet specified**
6. **Out of scope**
7. **Issues** — table: **Issue**, **Overview**, **Status** (all children, including closed)
8. **Spikes** — table: **Spike**, **Overview**, **Status**

Plan, issue, and spike item files all live in `.backlog/items/`. Link children from the feature file with same-directory paths, e.g. `[0004-login-flow.md](0004-login-flow.md)`. Link spike results with `[0006-oauth.md](../spike/0006-oauth.md)`.

### Issue file body

```markdown
Status: needs-detail
Plan: [0003-plan-auth.md](0003-plan-auth.md)
Overview: One sentence for the index table.
Type: interrogate
Blocked by:

## Question

…

## Comments
```

`Type:` is `interrogate` or `task` (not `spike` — spikes are separate item files).

### Spike item file body

```markdown
Status: needs-detail
Plan: [0003-plan-auth.md](0003-plan-auth.md)
Overview: One sentence for the index table.
Result: [0006-oauth.md](../spike/0006-oauth.md)
Blocked by:

## Question

…

## Comments
```

No `Type:` line on spike items. Findings live only in `.backlog/spike/<NNNN>-<slug>.md`; that file should link back with `Spike: [0006-spike-oauth.md](../items/0006-spike-oauth.md)`.

### Blocking

- `Blocked by: 0004, 0007` — comma-separated shared item numbers (feature, issue, or spike).
- **Frontier** (per feature): lowest `NNNN` among that feature’s issues and spikes with `needs-detail` and empty `Blocked by`.
- When any item becomes `resolved` or `out-of-scope`, remove its `NNNN` from every `Blocked by:` line in `.backlog/items/` (trim commas; delete the line if empty). Do not add a comment for the sweep alone.

### Thread

Append discussion under `## Comments` on issues and spikes.

## When a skill says "publish to the backlog"

Apply **amigo-pato** to the draft, then create the item file(s) under `.backlog/items/` and update the parent feature’s **Issues** table (and `features.md` when adding a feature).

## When a skill says "fetch the relevant ticket"

Read the path or file the user gave.

## Epic-duck operations

Used by **epic-duck**. A **feature plan** is the planning artifact; **issues** and **spike items** are children.

- **Plan file**: `.backlog/items/<NNNN>-plan-<slug>.md` (sections above).
- **Child issue**: `.backlog/items/<NNNN>-<slug>.md` with `Plan:` backlink, `Type:` (`interrogate` | `task`), `Status:`.
- **Child spike**: `.backlog/items/<NNNN>-spike-<slug>.md` plus result under `.backlog/spike/`.
- **Resolve issue**: `## Answer`, `Status: resolved`, one bullet under feature **Decisions so far**, blocker sweep, refresh tables.
- **Resolve spike**: result file written, spike item `Status: resolved`, update **Spikes** table and **Decisions so far** when appropriate.

### Starting a session (local)

1. Resolve which feature to open (user input: path, `NNNN`, slug, or close name match — confirm with user; or list `needs-detail` / `in-progress` from `features.md`; or chart a new feature).
2. **Git check** (once, before writes): if the feature file differs from `HEAD` (untracked file = plan-level change):
   - Hunks only under `## Issues` / `## Spikes` → warn that index tables changed; ask to continue.
   - Any change to plan sections (`Status`, Destination, Notes, Decisions, fog, out of scope, or above **Issues**) → list impact; ask how to proceed. Decline or wait → no writes.
3. Pick child: user-named issue/spike, else lowest `in-progress` child, else frontier → `in-progress`, else continue charting.

### Plan completion

When every child is `resolved` or `out-of-scope` and **Not yet specified** is empty, ask whether the feature is `resolved`, `out-of-scope`, or still `in-progress` with more work (new items or a fog line).
