# Issue tracker: Linear

Issues and specs live in Linear. Prefer the [Linear CLI](https://github.com/linear/linear/tree/master/packages/linear-cli) when installed; otherwise use the GraphQL API with credentials from the environment (`LINEAR_API_KEY`).

## Conventions

- **Team / project**: record the default team id or key and project name in this file after setup (the setup skill should ask once and fill them in).
- **Create**: `linear issue create --title "..."` or API `issueCreate` with team id and description.
- **Read**: `linear issue view <id>` or API fetch by identifier.
- **List**: filter by team, project, or label.
- **Labels**: apply workflow labels matching `docs/agents/triage-labels.md` and `epic-duck:*` when needed.
- **Parent / child**: set `parentId` on child issues for epic-duck maps and ticket hierarchies.
- **Blocking**: use Linear's "blocked by" relation (`blockedBy` / issue relation type blocks).

## When a skill says "publish to the issue tracker"

Apply **3-amigos** to the draft, then create a Linear issue in the configured team (and project if set).

## When a skill says "fetch the relevant ticket"

Load the issue by id, identifier (`ENG-123`), or URL the user passed.

## Epic duck operations

- **Map**: one issue labelled `epic-duck:map` (create the label in Linear if missing).
- **Child**: issue with `parentId` = map; label `epic-duck:<type>`.
- **Blocking**: native blocked-by relations between issues.
- **Frontier**: open children with no open blockers and no assignee; map order.
- **Claim**: assign to the driving user before other edits.
- **Resolve**: comment with answer, mark done/cancelled per team workflow, append gist + link to map description **Decisions so far**.
