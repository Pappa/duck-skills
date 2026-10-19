# Issue tracker: Azure DevOps

Work items live in **Azure DevOps Boards** for this repo's project. Use the [Azure DevOps CLI](https://learn.microsoft.com/en-us/azure/devops/cli/?view=azure-devops) (`az extension add --name azure-devops`) or the REST API with `AZURE_DEVOPS_EXT_ORG`, project, and PAT or `az login`.

Record after setup (fill in during `/setup-pappa-skills`):

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
- **Tags** (labels): `az boards work-item update --id <id> --fields "System.Tags=ready-for-agent;epic-duck:map"`
- **Close / resolve**: set `System.State` to the team's Done/Closed state via `--fields`.

Parent/child and dependency links use **relation types**:

- **Parent**: `az boards work-item relation add --id <child> --relation-type parent --target-id <parent>`
- **Blocked by** (predecessor): `az boards work-item relation add --id <blocked> --relation-type predecessor --target-id <blocker>` (confirm relation name matches your process template; use `System.LinkTypes.Dependency` / predecessor-successor in REST if CLI differs).

## When a skill says "publish to the issue tracker"

Apply **3-amigos** to the draft, then create a work item in the configured project.

## When a skill says "fetch the relevant ticket"

`az boards work-item show` or WIQL by id; include discussion history when decisions matter.

## Epic duck operations

- **Map**: one work item tagged `epic-duck:map` holding Destination / Notes / Decisions / Fog in the description.
- **Child ticket**: child of the map work item; tag `epic-duck:<type>` (`research` | `prototype` | `interrogate` | `task`).
- **Blocking**: predecessor link from child to each blocker; unblocked when all predecessors are closed.
- **Frontier**: open children with no open predecessors and unassigned (or not claimed); map order.
- **Claim**: assign to the driving user (`System.AssignedTo`) before other edits.
- **Resolve**: discussion note with answer, move to closed state, append gist + link to map **Decisions so far** in the map description.
