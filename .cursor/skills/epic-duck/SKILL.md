---
name: epic-duck
description: Chart a large, unclear or ambiguous piece of work as a plan with decision issues on the backlog, then resolve one decision per session until the route to the destination is clear. Use for multi-session planning, unclear scope, epic-duck, or feature-based planning.
disable-model-invocation: true
---

A **destination** is a feature too big to implement in one session and still ambiguous or unclear — the steps are not well defined. 

**Epic duck** help define the steps of the **plan** on the backlog, then resolves **issues** and **spikes** one at a time. Default mode is **plan, don't do**: each ticket resolve a decision, not deliverables.

**Refer by name** in human-facing text: titles and overviews, not bare numbers.

## The Plan

The plan is a single ticket on this repo's backlog, labelled `epic-duck:plan`. Its tickets are child issues of the feature the plan is working towards.

The plan is iterative and documents progress towards the goal, a completed feature. It lists the decisions made so far and acts as an index to the tickets that contain the decision's details.

**Where to find the backlog** Details about the backlog and issue tracker can be found in `docs/agents/backlog.md`. If you can't find it, tell the user to run `/setup-duck-skills`. Consult the tracker doc's "Epic-duck operations" section for how to work with the backlog.

### Plan body

```markdown
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

## Issues

| Issue | Overview | Status |
|-------|----------|--------|
| [0004-slug.md](0004-slug.md) | … | needs-detail |

## Spikes

| Spike | Overview | Status |
|-------|----------|--------|
| [0005-spike-slug.md](0005-spike-slug.md) | … | needs-detail |
```

Open children are listed in the tables — keep **Overview** and **Status** in sync with each child file.

### Issue body

```markdown
Status: needs-detail
Plan: [0003-plan-auth.md](0003-plan-auth.md)
Overview: One sentence.
Type: interrogate
Blocked by:

## Question

The decision or investigation this issue resolves.
```

`Type:` is `interrogate`, `spike` or `task`.

### Spike item

Separate file `.backlog/items/<NNNN>-spike-<slug>.md`; findings in `.backlog/spike/<NNNN>-<slug>.md`. Delegate investigation to the `spike` skill.

## Status vocabulary

Plans use: `needs-detail`, `in-progress`, `resolved`, `out-of-scope`. Align remote tracker state/tags with `docs/agents/backlog.md` where configured.

Tasks, issues, and spikes use: `needs-detail`, `in-progress`, `resolved`, `out-of-scope`. Align remote tracker state/tags with `docs/agents/backlog.md` where configured.

## Ticket types (issues)

- **spike** (AFK): use a **spike item** + `spike` skill.
- **interrogate** (HITL): live interview — `interrogate` or `rubber-duck` skill; agent never answers for the human.
- **task** (HITL or AFK): manual unblocker before a decision can be made.

Set child `Status: in-progress` before work. **Blocking**: `Blocked by: NNNN, NNNN` (local) or native relations (remote). **Frontier** = `needs-detail`, unblocked; lowest number first.

When any item becomes `resolved` or `out-of-scope`, remove its number from every `Blocked by:` (local) or drop blocking links (remote). Clearing the last blocker does not change the blocked item's status.

## Fog of war

**Not yet specified** holds fog toward the destination. **Ticket when** the question is sharp (even if blocked). **Fog when** you cannot phrase the question yet. Resolving children graduates fog into new items.

**Out of scope** is consciously excluded work — never graduates. Close mis-scoped items and record one line under **Out of scope**.

## Choose a feature (every session)

1. Input that **names or references by number** an existing feature → open it (path, filename, `NNNN` for `NNNN-plan-*`, slug).
2. Input that references `NNNN` for a non-feature item → open that child and its `Plan:` parent.
3. **Close name match** to a row in `features.md` → confirm filename, overview, and status with the user.
4. Input that describes **new work** and no existing feature → chart a new feature (allocate `NNNN`, row in `features.md`, `Status: needs-detail`).
5. Otherwise → list every `needs-detail` and `in-progress` feature from `features.md` (number order); user picks. Empty list → offer to chart.

`resolved` / `out-of-scope` features are not listed. If the user names one, confirm before setting `in-progress` and continuing.

### Local git check (once, before writes)

If `git status` shows changes to the **feature file only**:

- Diff vs `HEAD` (untracked feature file = plan-level change).
- Hunks only under `## Issues` / `## Spikes` → warn; ask to continue.
- Any plan section changed → ask how to proceed. Decline or wait → no writes.

Do not re-check mid-session. Other clones are invisible.

### Pick a child

User-named issue or spike → that item. Else lowest-numbered `in-progress` child for this feature. Else set frontier child to `in-progress`. If no children yet, continue **charting**.

## Chart the feature (invocation)

User brings a loose idea (often after feature selection above).

1. **Destination** — use `rubber-duck` or `interrogate` until scope and destination are clear.
2. **Breadth-first pass** — surface open decisions. If no fog remains (small enough for one session), stop and ask how to proceed without a full feature chart.
3. **Create or update feature** with Destination, Notes, empty Decisions, fog in **Not yet specified**, empty **Issues** / **Spikes** tables.
4. **Create children** you can specify now; run **3-amigos** on each deliverable backlog ticket before publish; **wire blocking in a second pass** (numbers must exist).
5. **Spike items** — optional parallel subagents on `spike/<name>` branches; link findings; do not merge throwaway branches.

Stop after charting; do not resolve children in this session except parallel spikes.

## Work through the feature (invocation)

User passes a feature (or child); optional named issue/spike.

1. Load feature body (not every child unless needed).
2. Git check (local) and pick child (above). Set `in-progress` if not already.
3. Resolve per `Type` or spike workflow. Use **Notes** for extra skills.
4. **Resolve issue**: `## Answer`, `Status: resolved`, append **Decisions so far**, blocker sweep, refresh tables.
5. Add new children; graduate fog; rule out-of-scope items.
6. When all children are `resolved` or `out-of-scope` and **Not yet specified** is empty, ask whether the feature is `resolved`, `out-of-scope`, or still `in-progress` with more work.

**One child per session** except parallel spikes during charting.

Expect concurrent editors on shared trackers.
