Type: epic-duck:decision
Status: resolved
Plan: [0001-plan-duck-skills-planning-refinement.md](0001-plan-duck-skills-planning-refinement.md)
Overview: Align ticket shapes with `docs/agents/backlog.md` and skill output.
Blocked by:

## Question

What exact shapes and required fields must epic-duck decisions, tasks, spike items, spike findings, and `ready` deliverables use so humans and agents can implement without guessing—and what changes to `docs/agents/backlog.md` (if any) are required?

## Answer

### Canon location

- **`docs/adr/0001-backlog-ticket-shapes.md`** — rationale and rules.
- **`docs/agents/backlog.md`** — agent-facing templates (SSOT for day-to-day work).
- **`docs/agents/ticket-statuses.md`** — **`Status:`** vocabulary.

### `Type:` namespace (local + remote)

| Kind | `Type:` |
|------|---------|
| Plan | `epic-duck:plan` |
| Decision | `epic-duck:decision` |
| Task (planning) | `epic-duck:task` |
| Spike item | `epic-duck:spike` |

**Header order:** **`Type:` first**, then `Status:`, then `Plan:` → `Overview:` → optional `Result:` (spike) → optional `Blocked by:`.

Plans omit `Plan:` / `Overview:`; **Destination** is the index one-liner.

Future **implementation** backlog items use a different `Type:` prefix (later feature). **`epic-duck:task`** is planning-only.

### Unified `Status:`

`needs-triage` · `needs-detail` · `ready` · `in-progress` · `resolved` · `wontfix` · `out-of-scope`

- **`ready`** — requirements complete enough to **start** work (human or AFK). Applies to **decisions**, **tasks**, and **spikes** when the ticket is sharp enough to pick up.
- **`needs-triage`** — maintainer must classify; state not decidable without user input.
- **`wontfix`** — closed, no action (parallel to **`resolved`** with outcome).

Deliverable **`epic-duck:task`**: set **`Status: ready`** only after **amigo-duck Verdict: Approve** ([0002](0002-decision-ready-ticket-quality-bar.md)).

### Body profiles

| `Type:` | Body |
|---------|------|
| `epic-duck:decision` | `## Question`; `## Answer` when resolved; optional `## Comments` |
| `epic-duck:task` (unblocker) | `## Question` (+ `## Answer`); not `ready` |
| `epic-duck:task` (`Status: ready`) | **Problem Statement**, **Description**, optional **Notes**, **Out of Scope**, **Acceptance Criteria** (required) |
| `epic-duck:spike` | `## Question`; optional `## Comments` |
| Spike findings | `Spike:` link; **`## TLDR`**; no `Type`/`Status` on file |

No separate **`## Spec`** branch; spec pointers use unblocker **Question** or become **`ready`** deliverables when an agent should execute.

### Skill / doc updates

- **amigo-duck:** review heading **`## amigo-duck review`**; kinds use `Type: epic-duck:*` and **`Status: ready`** gate.
- **epic-duck**, **setup-duck-skills** `backlog-*.md`: templates aligned with `backlog.md`.
- Migrate existing `.backlog/items/*` to this header and type scheme.

### Follow-on

- **0006** triage-duck assumes unified **`Status:`** only.
- **0010**: move to **`Status: ready`** + deliverable body when unblocked and spec-complete.

### Session semantics (epic-duck)

- **`ready`** — pickable for a new session; **`resolved`** — question answered or work complete.
- **`in-progress`** — claimed (this or another session); epic-duck **always confirms** before editing an `in-progress` child (including when named — wrong-ticket guard).
- **No auto-pick** — offer up to five lowest **`ready`** children (overflow + full-list offer), then same pattern for `in-progress` / frontier; user selects.

## Comments
