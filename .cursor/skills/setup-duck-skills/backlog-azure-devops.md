# Issue tracker: Azure DevOps

Work items live in **Azure DevOps Boards** for this repo's project. Use the [Azure DevOps CLI](https://learn.microsoft.com/en-us/azure/devops/cli/?view=azure-devops) (`az extension add --name azure-devops`) or the REST API with `AZURE_DEVOPS_EXT_ORG`, project, and PAT or `az login`.

Record after setup (fill in during `/setup-duck-skills`):

- **Organization**: `https://dev.azure.com/<org>`
- **Project**: `<project name>`
- **Default area path** (optional): `<project>\<team>`
- **Default iteration** (optional): current sprint path

Infer org/project from `git remote` when possible (`dev.azure.com/<org>/<project>/_git/<repo>`).

## Conventions

- **Create work item**: `az boards work-item create --title "..." --type "User Story"` (or Task, Bug, Issue — match team process). Use `--description` with a heredoc for bodies.
- **Read**: `az boards work-item show --id <id> --open`
- **List**: `az boards query --wiql "SELECT [System.Id], [System.Title] FROM WorkItems WHERE [System.TeamProject] = '<project>' AND [System.State] <> 'Closed'"`
- **Comment**: `az boards work-item update --id <id> --discussion "..."`
- **Tags** (labels): `az boards work-item update --id <id> --fields "System.Tags=ready;epic-duck:plan"`
- **Close / resolve**: set `System.State` to the team's Done/Closed state via `--fields`.

Parent/child and dependency links use **relation types**:

- **Parent**: `az boards work-item relation add --id <child> --relation-type parent --target-id <parent>`
- **Blocked by** (predecessor): `az boards work-item relation add --id <blocked> --relation-type predecessor --target-id <blocker>` (confirm relation name matches your process template; use `System.LinkTypes.Dependency` / predecessor-successor in REST if CLI differs).

## When a skill says "publish to the backlog"

Apply **amigo-duck** to the draft, then create a work item in the configured project.

## When a skill says "fetch the relevant ticket"

`az boards work-item show` or WIQL by id; include discussion history when decisions matter.

## Epic-duck operations

Used by **epic-duck**. **Plan** parent work item tagged `epic-duck:plan`; children linked as child work items. Status vocabulary: `needs-detail`, `in-progress`, `resolved`, `out-of-scope` (state or tags per process).

- **Plan**: one work item tagged `epic-duck:plan` holding Destination / Notes / Decisions / Fog in the description.
- **Child**: child of the feature work item; tag `epic-duck:<type>` (`spike` | `decision` | `task`).
- **Blocking**: predecessor link from child to each blocker; unblocked when all predecessors are `resolved` / closed / `out-of-scope`.
- **Frontier**: children in active/needs-detail state with no open predecessors; lowest id first.
- **Claim**: assign to the driving user (`System.AssignedTo`) for the session.
- **Resolve**: discussion note with answer, move to closed/resolved state, append gist + link to feature **Decisions so far**. Remove predecessor links when a blocker is resolved or out-of-scope.
