# Issue tracker: Local markdown

Plans, decisions, tasks, and spikes live under `.backlog/`.

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
| Decision | `.backlog/items/<NNNN>-decision-<slug>.md` |
| Task | `.backlog/items/<NNNN>-<slug>.md` — slug must **not** start with `plan-`, `decision-`, or `spike-` |
| Spike (item) | `.backlog/items/<NNNN>-spike-<slug>.md` |
| Spike (findings) | `.backlog/spike/<NNNN>-<slug>.md` |

### Status (features, decisions, tasks, spikes)

`needs-detail` · `in-progress` · `resolved` · `out-of-scope`

- **Canonical**: `Status:` near the top of each item file. Update `features.md` and the feature’s **Decisions** / **Tasks** / **Spikes** tables in the same edit.
- **Plan**: starts `needs-detail`; becomes `in-progress` when the first child decision, task, or spike is created; `resolved` / `out-of-scope` only by explicit choice (see epic duck).
- **Decision / task / spike**: set `in-progress` when work starts; `resolved` when done (spike item when the result file exists).

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
7. **Decisions** — table: **Decision**, **Overview**, **Status** (all decision children, including closed)
8. **Tasks** — table: **Task**, **Overview**, **Status** (all task children, including closed)
9. **Spikes** — table: **Spike**, **Overview**, **Status**

Plan, decision, task, and spike item files all live in `.backlog/items/`. Link children from the feature file with same-directory paths, e.g. `[0004-decision-login-flow.md](0004-decision-login-flow.md)`. Link spike results with `[0006-oauth.md](../spike/0006-oauth.md)`.

### Decision file body

```markdown
Status: needs-detail
Plan: [0003-plan-auth.md](0003-plan-auth.md)
Overview: One sentence for the index table.
Type: decision
Blocked by:

## Question

…

## Comments
```

`Type:` is always `decision` on decision files (not `spike` — spikes are separate item files).

### Task file body

```markdown
Status: needs-detail
Plan: [0003-plan-auth.md](0003-plan-auth.md)
Overview: One sentence for the index table.
Type: task
Blocked by:

## Question

…

## Comments
```

`Type:` is always `task` on task files. Optional `Label: ready` for agent-ready deliverables (see `docs/agents/ticket-labels.md`). Task bodies may use `## Question` / `## Answer` (unblocker) or `## Acceptance criteria` (when `Label: ready`).

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

- `Blocked by: 0004, 0007` — comma-separated shared item numbers (plan, decision, task, or spike).
- **Frontier** (per feature): lowest `NNNN` among that feature’s decisions, tasks, and spikes with `needs-detail` and empty `Blocked by`.
- When any item becomes `resolved` or `out-of-scope`, remove its `NNNN` from every `Blocked by:` line in `.backlog/items/` (trim commas; delete the line if empty). Do not add a comment for the sweep alone.

### Thread

Append discussion under `## Comments` on decisions, tasks, and spikes.

## When a skill says "publish to the backlog"

Apply **amigo-duck** to the draft, then create the item file(s) under `.backlog/items/` and update the parent feature’s **Decisions** / **Tasks** tables (and `features.md` when adding a feature).

## When a skill says "fetch the relevant ticket"

Read the path or file the user gave.

## Epic-duck operations

Used by **epic-duck**. A **feature plan** is the planning artifact; **decisions**, **tasks**, and **spike items** are children.

- **Plan file**: `.backlog/items/<NNNN>-plan-<slug>.md` (sections above).
- **Child decision**: `.backlog/items/<NNNN>-decision-<slug>.md` with `Plan:` backlink, `Type: decision`, `Status:`.
- **Child task**: `.backlog/items/<NNNN>-<slug>.md` with `Plan:` backlink, `Type: task`, `Status:`.
- **Child spike**: `.backlog/items/<NNNN>-spike-<slug>.md` plus result under `.backlog/spike/`.
- **Resolve decision**: `## Answer`, `Status: resolved`, one bullet under feature **Decisions so far**, blocker sweep, refresh tables.
- **Resolve spike**: result file written, spike item `Status: resolved`, update **Spikes** table and **Decisions so far** when appropriate.

### Starting a session (local)

1. Resolve which feature to open (user input: path, `NNNN`, slug, or close name match — confirm with user; or list `needs-detail` / `in-progress` from `features.md`; or chart a new feature).
2. **Git check** (once, before writes): if the feature file differs from `HEAD` (untracked file = plan-level change):
   - Hunks only under **Decisions** / **Tasks** / **Spikes** → warn that index tables changed; ask to continue.
   - Any change to plan sections (`Status`, Destination, Notes, Decisions so far, fog, out of scope, or above **Decisions**) → list impact; ask how to proceed. Decline or wait → no writes.
3. Pick child: user-named decision/task/spike, else lowest `in-progress` child, else frontier → `in-progress`, else continue charting.

### Plan completion

When every child is `resolved` or `out-of-scope` and **Not yet specified** is empty, ask whether the feature is `resolved`, `out-of-scope`, or still `in-progress` with more work (new items or a fog line).
