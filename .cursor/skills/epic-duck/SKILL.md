---
name: epic-duck
description: Chart a large, foggy effort as a map of decision tickets on the backlog, then resolve one decision per session until the route to the destination is clear. Use for multi-session planning, unclear scope, epic-duck, or map-based planning.
disable-model-invocation: true
---

A **destination** is too big to implement in one session and still wrapped in **fog** — the path is not visible yet. **Epic duck** finds the path as a **map** on the backlog, then works **decision tickets** one at a time. Default mode is **plan, don't do**: tickets resolve decisions, not deliverables, unless the map's **Notes** say otherwise.

Read `docs/agents/backlog.md` (Epic duck operations). If missing, run `/setup-pappa-skills`.

**Refer by name** in human-facing text: ticket titles, not bare `#42`.

## Map artifact

One tracker issue labelled `epic-duck:map`. Child issues are tickets. The map is an **index** — decisions live in ticket bodies and resolution comments, not duplicated on the map.

### Map body

```markdown
## Destination

One or two lines: the spec, decision, or change this effort is finding its way to.

## Notes

Domain context; skills to consult; effort-specific preferences.

## Decisions so far

- [<closed ticket title>](link): one-line gist

## Not yet specified

Fog: in-scope questions not sharp enough to ticket yet.

## Out of scope

Work ruled beyond this destination (with links to closed tickets when relevant).
```

Open tickets are **not** listed on the map — query the tracker.

### Ticket body

```markdown
## Question

The decision or investigation this ticket resolves.
```

Label `epic-duck:<type>`: `spike` | `interrogate` | `task`. Epic duck tickets do **not** use `ready-for-agent`.

**Claim** before work (assignee / `Status: claimed`). **Blocking** uses native relations or the tracker's body convention. **Frontier** = open, unblocked, unclaimed children.

## Ticket types

- **spike** (AFK): facts from docs or APIs — delegate to the `spike` skill in a subagent.
- **interrogate** (HITL): live interview — `interrogate` or `rubber-duck` skill; agent never answers for the human.
- **task** (HITL or AFK): manual unblocker (access, signup, data move) before a decision can be made.

## Fog of war

**Not yet specified** holds fog toward the destination. **Ticket when** the question is sharp (even if blocked). **Fog when** you cannot phrase the question yet. Resolving tickets graduates fog into new tickets.

**Out of scope** is consciously excluded work — never graduates. Close mis-scoped tickets and record one line under **Out of scope**.

## Chart the map (invocation)

User brings a loose idea.

1. **Destination** — use `rubber-duck` or `interrogate` until scope and destination are clear.
2. **Breadth-first pass** — surface open decisions across the space. If no fog remains (small enough for one session), stop and ask how to proceed without a map.
3. **Create map** with Destination, Notes, empty Decisions, fog in **Not yet specified**.
4. **Create tickets** you can specify now; run **3-amigos** on each deliverable backlog ticket before publish; **wire blocking in a second pass** (ids must exist).
5. **Spike tickets** — optional parallel subagents on `spike/<name>` branches; link findings on tickets; do not merge throwaway branches.

Stop after charting; do not resolve tickets in this session except parallel spikes.

## Work through the map (invocation)

User passes map id/URL; optional ticket.

1. Load map body only (not every ticket).
2. Pick ticket: user-named, else first frontier ticket. **Claim** first.
3. Resolve per `epic-duck:<type>` label. Use **Notes** for extra skills.
4. **Resolve**: answer comment, close ticket, append to map **Decisions so far**.
5. Add new tickets; graduate fog; rule out-of-scope tickets.

**One ticket per session** except parallel spikes during charting.

Expect concurrent editors on the tracker.
