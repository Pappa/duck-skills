# Ticket status vocabulary

Skills use a single workflow field **`Status:`** on every backlog item (plans, decisions, tasks, spike items). There is no separate `Label:` line.

Remote trackers (GitHub, GitLab, Azure DevOps) map the same strings via tags, labels, or description `Status:` — see `setup-duck-skills/backlog-*.md`.

| Status | Meaning |
|--------|---------|
| `needs-triage` | Maintainer must evaluate or route; workflow state not yet decidable without human input. |
| `needs-detail` | Waiting on clarity (reporter, fog, incomplete requirements). |
| `ready` | Requirements complete and well-defined; OK for a human or AFK agent to **start** work on this item. Epic-duck treats unblocked **`ready`** children as the default pool for new work in a session. |
| `in-progress` | **Claimed** — a session is actively working this item (this chat or another). Epic-duck must **confirm with the user** before editing body, status, or resolution — **including when the user named that ticket** (they may have meant a different item). Stale `in-progress` is possible; confirmation covers take-over. |
| `resolved` | Done; outcome recorded (`## Answer`, spike result, deliverable complete). |
| `wontfix` | Closed with **no action** (workflow ended, rejected). |
| `out-of-scope` | Consciously excluded from the plan destination. |

When a skill says **“set ready”** or **“apply the ready status”**, set **`Status: ready`** after requirements pass **amigo-duck** where that gate applies (see `docs/agents/backlog.md`).

Edit this table only when the workflow model changes (record rationale in `docs/adr/`).
