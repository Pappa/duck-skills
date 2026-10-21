# Ticket status vocabulary

Every backlog item (plans, decisions, tasks, spike items) uses one workflow field: **`Status:`**.

On remote trackers (GitHub, GitLab, Azure DevOps), map the same strings via tags or a `Status:` line in the body — see `setup-duck-skills/backlog-*.md`.

| Status | Meaning |
|--------|---------|
| `needs-triage` | Maintainer must evaluate or route; workflow state not yet decidable without human input. |
| `needs-detail` | Waiting on clarity (reporter, fog, incomplete requirements). |
| `ready` | Requirements complete and well-defined; OK for a human or AFK agent to **start** work on this item. |
| `in-progress` | A session is actively working this item. |
| `resolved` | Done; outcome recorded. |
| `wontfix` | Closed with **no action**. |
| `out-of-scope` | Consciously excluded from the plan destination. |

When a skill says **“set ready”**, set **`Status: ready`** after requirements pass **amigo-duck** where that gate applies.

Edit this table only when the workflow model changes (record rationale in `docs/adr/`).
