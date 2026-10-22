---
name: epic-duck
description: Chart a large, unclear or ambiguous piece of work as a plan with decisions on the backlog, then resolve one decision per session until the route to the destination is clear. Use for multi-session planning, unclear scope, epic-duck, or feature-based planning.
disable-model-invocation: true
---

A **destination** is a feature too big to implement in one session and still ambiguous or unclear — the steps are not well defined. 

**Epic duck** help define the steps of the **plan** on the backlog, then resolves **decisions**, **tasks**, and **spikes** one at a time. Default mode is **plan, don't do**: each decision ticket resolves a question, not deliverables.

**Refer by name** in human-readable plain langauge: titles and overviews, not bare numbers.

## The Plan

The plan is a single ticket on this repo's backlog. On **local** markdown use **`Type: epic-duck:plan`** (first line), `features.md`, and `*-plan-*.md`. On **remote** trackers, label/tag **`epic-duck:plan`**. Its children are **planning-era** items: `epic-duck:decision`, `epic-duck:task`, and `epic-duck:spike` only (not implementation `Type: task` / `Type: spike` from **rubber-duck** — see `docs/agents/backlog.md`).

The plan is iterative and documents progress towards the goal, a completed feature. It lists the decisions made so far and acts as an index to the tickets that contain the decision's details.

**Where to find the backlog** Details about the backlog and issue tracker can be found in `docs/agents/backlog.md`. If you can't find it, tell the user to run `/setup-duck-skills`. Consult the tracker doc's "Epic-duck operations" section for how to work with the backlog.

### Creating the plan

Don't assume you understand the users inital request, plan or idea. **Always**, use the `question-duck` skill to dig into the idea, ask questions to clarify requirements and edge cases, ensure all assumptions are documented and that you and the user have a **shared understanding**.

Use the `amigo-duck` skill to review the draft ticket, and take their suggestions on board to update the ticket before adding it to the backlog.

### Plan body

```markdown
Type: epic-duck:plan
Status: needs-detail

## Destination

One or two lines: the spec, decision, or change this effort is finding its way to.

## Notes

Domain context; skills to consult; effort-specific preferences.

## Decisions so far

- [<overview or title>](link): one-line gist

## Not yet specified

Fog: in-scope questions not sharp enough to ticket yet.

## Out of scope

Work ruled beyond this destination (with links to closed items when relevant).

## Decisions

| Decision | Overview | Status |
|----------|----------|--------|
| [0004-decision-slug.md](0004-decision-slug.md) | … | needs-detail |

## Tasks

| Task | Overview | Status |
|------|----------|--------|
| [0016-task-slug.md](0016-task-slug.md) | … | needs-detail |

## Spikes

| Spike | Overview | Status |
|-------|----------|--------|
| [0005-spike-slug.md](0005-spike-slug.md) | … | needs-detail |
```

Open children are listed in the tables — keep **Overview** and **Status** in sync with each child file.

### Decision body

```markdown
Type: epic-duck:decision
Status: needs-detail
Plan: [0003-plan-auth.md](0003-plan-auth.md)
Overview: One sentence.
Blocked by:

## Question

The decision this ticket resolves.

## Comments
```

Set **`Status: ready`** when the question is sharp enough to resolve. `Type:` is always `epic-duck:decision` on decision files.

### Task body

Unblocker:

```markdown
Type: epic-duck:task
Status: needs-detail
Plan: [0003-plan-auth.md](0003-plan-auth.md)
Overview: One sentence.
Blocked by:

## Question

What must be done before a related decision can proceed (when used as an unblocker).

## Comments
```

Deliverable (`Status: ready` after **amigo-duck** **Approve**): **Problem Statement**, **Description**, optional **Notes** / **Out of Scope**, **Acceptance Criteria** — see `docs/agents/backlog.md`.

### Spike item

```markdown
Type: epic-duck:spike
Status: needs-detail
Plan: [0003-plan-auth.md](0003-plan-auth.md)
Overview: One sentence.
Result: [0005-oauth.md](../spike/0005-oauth.md)
Blocked by:

## Question

## Comments
```

Findings in `.backlog/spike/<NNNN>-<slug>.md`. Delegate investigation to the `spike-duck` skill.

### Skills invoked

- **question-duck** — plan creation, charting, resolving decisions (HITL).
- **architect-duck** — when glossary or ADRs need updating during epic work (same role as within **rubber-duck**).
- **amigo-duck** — before publish of any planning child.
- **spike-duck** — spike children (findings file).

## Status vocabulary

Single field **`Status:`** on all items — `docs/agents/ticket-statuses.md` (`needs-triage`, `needs-detail`, `ready`, `in-progress`, `resolved`, `wontfix`, `out-of-scope`). Align remote trackers with `docs/agents/backlog.md`.

## Ticket types

- **epic-duck:decision** (HITL): live interview — `question-duck` skill; agent never answers for the human.
- **epic-duck:task** (HITL or AFK): unblocker (`## Question`) or deliverable (`Status: ready` + acceptance body).
- **epic-duck:spike** (AFK): spike item + `spike-duck` skill.

For all ticket types, use the `amigo-duck` skill to review and improve the ticket requirements.

Set child `Status: in-progress` when **this session** starts work on that child (after any confirmation below). **Blocking**: `Blocked by: NNNN, NNNN` (local) or native relations (remote). **Frontier** = `needs-triage` or `needs-detail`, unblocked; lowest number first. **Session pool** = unblocked **`ready`** children.

### Status and concurrent sessions

- **`ready`** — requirements are complete; safe for epic-duck to offer for a new work session (with the user).
- **`in-progress`** — a session has claimed the item (this chat or another clone/agent). Assume another actor may be editing until the user says otherwise.
- **`resolved`** / **`wontfix`** / **`out-of-scope`** — closed; do not reopen without user confirmation.

Before **any write** to a child whose `Status:` is **`in-progress`**, ask the user to confirm take-over or continuation — **including when they named that child** (they may have picked the wrong ticket). If they decline, pick a different child or wait.

When **this session** begins work on a child that is `ready`, `needs-detail`, or `needs-triage`, set **`Status: in-progress`** (and sync the plan table) before substantive edits.

When any item becomes `resolved` or `out-of-scope`, remove its number from every `Blocked by:` (local) or drop blocking links (remote). Clearing the last blocker does not change the blocked item's status.

## Fog of war

**Not yet specified** holds fog toward the destination. **Ticket when** the question is sharp (even if blocked). **Fog when** you cannot phrase the question yet. Resolving children graduates fog into new items.

**Out of scope** is consciously excluded work — never graduates. Close mis-scoped items and record one line under **Out of scope**.

## Choose a feature (every session)

1. User input that **names or references by number** an existing feature → open it (path, filename, `NNNN` for `NNNN-plan-*`, slug).
2. User input that references `NNNN` for a non-feature item → open that child and its `Plan:` parent.
3. User input that is a **close name match** to a row in `features.md` → confirm filename, overview, and status with the user.
4. User input that describes **new work** and no existing feature → chart a new feature (allocate `NNNN`, row in `features.md`, `Status: needs-detail`).
5. Otherwise → list every `needs-detail` and `in-progress` feature from `features.md` (number order); user picks. Empty list → offer to chart.

`resolved` / `out-of-scope` features are not listed. If the user names one, confirm before setting `in-progress` and continuing.

### Local git check (once, before writes)

If `git status` shows changes to the **feature file only**:

- Diff vs `HEAD` (untracked feature file = plan-level change).
- Hunks only under **Decisions** / **Tasks** / **Spikes** → warn; ask to continue.
- Any plan section changed → ask how to proceed. Decline or wait → no writes.

Do not re-check mid-session. Other clones are invisible.

### Pick a child

1. **User-named** decision, task, or spike → open that item. If its `Status:` is **`in-progress`**, **explicitly confirm** with the user before edits (wrong-ticket guard). Read-only peek does not require take-over confirmation.
2. **No name** — do **not** auto-select. Among unblocked children with **`Status: ready`**, list the **lowest five** by `NNNN` (title/overview + status). If more than five exist, say how many are not shown and ask whether they want the **full list** before choosing. Wait for the user to pick one.
3. If no **`ready`** children → list **`in-progress`** children (same five + overflow rule) and **ask** before any take-over; do not auto-continue.
4. If neither **`ready`** nor **`in-progress`** candidates → list up to **five** **frontier** children (`needs-triage` or `needs-detail`, unblocked); same overflow rule; user picks. Set **`Status: in-progress`** when this session starts work on the chosen item.
5. If no children yet, continue **charting**.

## Chart the feature (invocation)

User brings a loose idea (often after feature selection above).

1. **Destination** — use `question-duck` until scope and destination are clear.
2. **Breadth-first pass** — surface open decisions. If no fog remains (small enough for one session), stop and ask how to proceed without a full feature chart.
3. **Create or update feature** with Destination, Notes, empty Decisions so far, fog in **Not yet specified**, empty **Decisions** / **Tasks** / **Spikes** tables.
4. **Create children** you can specify now; run **amigo-duck** on each deliverable backlog ticket before publish; **wire blocking in a second pass** (numbers must exist).
5. **Spike items** — optional parallel subagents on `spike/<name>` branches; link findings; do not merge throwaway branches.

Stop after charting; do not resolve children in this session except parallel spikes.

## Work through the feature (invocation)

User passes a feature (or child); optional named decision, task, or spike.

1. Load feature body (not every child unless needed).
2. Git check (local) and pick child (above). Set `in-progress` when this session starts work (after confirmation if required).
3. Resolve per `Type` or spike workflow. Use **Notes** for extra skills.
4. **Resolve decision**: `## Answer`, `Status: resolved`, append **Decisions so far**, blocker sweep, refresh tables.
5. **Resolve spike**: findings file complete (via **spike-duck**), spike item `Status: resolved`, update plan **Spikes** table and **Decisions so far** when appropriate (`docs/agents/backlog.md`).
6. Add new children; graduate fog; rule out-of-scope items.
7. When all children are `resolved` or `out-of-scope` and **Not yet specified** is empty, ask whether the feature is `resolved`, `out-of-scope`, or still `in-progress` with more work.

When attaching an unanchored implementation item (`Plan: (unanchored)` from **rubber-duck**), set a real **`Plan:`** link on that item and move **`Status:`** off `needs-triage` when the user confirms the feature.

**One child per session** except parallel spikes during charting.

Expect concurrent editors on shared trackers.
