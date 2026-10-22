# ADR 0001: Backlog ticket shapes (epic-duck)

## Status

Accepted (decision [0005](../../.backlog/items/0005-decision-ticket-shapes-and-fields.md)).

## Context

Planning skills publish to one shared backlog (local markdown and remote trackers). We need one field canon so agents and humans do not guess at headers, workflow state, or body profiles. Spike [0011](../../.backlog/spike/0011-common-fields-and-skill-needs.md) surveyed skill needs; decision 0005 locked the model.

## Decision

### Namespace

All epic-duck artefacts use **`Type: epic-duck:<kind>`** on **local markdown and remote** tags/labels:

| Kind | `Type:` value | File pattern |
|------|----------------|--------------|
| Plan | `epic-duck:plan` | `*-plan-*.md` |
| Decision | `epic-duck:decision` | `*-decision-*.md` |
| Task | `epic-duck:task` | `<NNNN>-<slug>.md` (slug not `plan-`, `decision-`, `spike-`) |
| Spike item | `epic-duck:spike` | `*-spike-*.md` |

Future non-planning work (implementation skills) will use a **different** `Type:` prefix in a later ADR. **`epic-duck:task`** is planning-era work only.

### Header order

**First line is always `Type:`**, then `Status:`, then the rest.

**Plan** (`Type: epic-duck:plan`): no `Plan:` or `Overview:` — use **Destination** as the one-line index blurb in `features.md`.

**Child** (decision, task, spike item):

```text
Type: epic-duck:<kind>
Status: <workflow>
Plan: [<NNNN>-plan-<slug>.md](<same-dir>)
Overview: <one sentence>
Result: <link>          # spike items only, when allocated
Blocked by: <NNNN, …>  # omit line when empty
```

**Spike findings** (`.backlog/spike/`): no `Type:` or `Status:`; first line `Spike:` backlink; then **`## TLDR`**; cite sources in body.

### Unified workflow (`Status:`)

Workflow state is a single field **`Status:`** (see `docs/agents/ticket-statuses.md`):

| Status | Meaning |
|--------|---------|
| `needs-triage` | Maintainer must classify; state not decidable without human input. |
| `needs-detail` | Waiting on clarity (reporter, fog, incomplete requirements). |
| `ready` | Requirements complete enough to **start** work (human or AFK agent). |
| `in-progress` | Active session on this item. |
| `resolved` | Done; outcome recorded. |
| `wontfix` | Closed with no action. |
| `out-of-scope` | Consciously excluded from the plan destination. |

**`ready`** applies to **decisions**, **tasks**, and **spikes** when the ticket is sharp enough to pick up (for decisions: clear `## Question` and resolution criteria; for deliverable tasks: full body below + amigo-duck **Approve** before publish).

### Body profiles

**Decision** (`epic-duck:decision`): `## Question`; when resolved `## Answer`; optional `## Comments`.

**Task — unblocker** (`epic-duck:task`, not `ready`): `## Question` (+ `## Answer` when resolved); optional `## Comments`.

**Task — deliverable** (`epic-duck:task`, `Status: ready`): after amigo-duck **Approve**:

- `## Problem Statement`
- `## Description`
- optional `## Notes`
- `## Out of Scope`
- `## Acceptance Criteria` (required, testable)

Header **`Overview:`** remains one line for plan index tables.

**Spike item**: `## Question`; optional `## Comments`. Resolve when findings file exists.

### Quality gates

- **`Status: ready`** on deliverable tasks: **amigo-duck Verdict: Approve** on all four axes before publish (per [0002](../../.backlog/items/0002-decision-ready-ticket-quality-bar.md)).
- **amigo-duck** review artefacts use heading **`## amigo-duck review`** (stable for evals).

### SSOT

**`docs/agents/backlog.md`** is the agent-facing operational reference (templates copied from this ADR). This ADR records rationale and canonical rules.

### Concurrent sessions (epic-duck)

- **`ready`** — default pool for starting new work with the user.
- **`in-progress`** — session claim; epic-duck **always** confirms before modifying an `in-progress` child (another agent or clone may be active; the user may have named the wrong ticket).
- **No auto-pick** — when the user does not name a child, epic-duck lists up to five lowest unblocked **`ready`** items (then `in-progress`, then frontier), reports overflow count, offers full list, and waits for a choice.

## Consequences

- Planning backlog items use `Type: epic-duck:*` and the unified `Status:` vocabulary.
- Implementation items use plain **`Type: task`** and **`Type: spike`** (rubber-duck); documented in `docs/agents/backlog.md` (decision **0014**).
- Update epic-duck, rubber-duck, amigo-duck, setup-duck-skills backlog templates.
- Triage-duck (**0006**) should assume unified `Status:` only.
