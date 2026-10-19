# Issue tracker: GitHub

Issues and specs live as GitHub issues. Use the `gh` CLI.

## Conventions

- **Create**: `gh issue create --title "..." --body "..."` (heredoc for bodies).
- **Read**: `gh issue view <number> --json number,title,body,labels,comments`.
- **List**: `gh issue list` with `--label` / `--state` as needed.
- **Sub-issue of parent**: `gh issue create --parent <parent>` or `gh issue edit <parent> --add-sub-issue <child>` (`gh` 2.94+).
- **Comment**: `gh issue comment <number> --body "..."`
- **Labels**: `gh issue edit <number> --add-label "..."` / `--remove-label "..."`
- **Close**: `gh issue close <number> --comment "..."`

Infer repo from `git remote` inside the clone.

## When a skill says "publish to the backlog"

Apply **3-amigos** to the draft, then create a GitHub issue.

## When a skill says "fetch the relevant ticket"

`gh issue view` as above.

## Epic duck operations

Used by `/epic-duck`. The **map** is one issue; **tickets** are child issues.

- **Map**: issue labelled `epic-duck:map`.
- **Child**: sub-issue of the map (or `Part of #<map>` in body). Label `epic-duck:<type>` (`spike` | `interrogate` | `task`).
- **Blocking**: native issue dependencies — `gh api --method POST repos/<owner>/<repo>/issues/<child>/dependencies/blocked_by -f issue_id=<blocker-db-id>` where `issue_id` is the blocker's database id (`gh api repos/<owner>/<repo>/issues/<n> --jq .id`). Fallback: `Blocked by: #n` at top of body.
- **Frontier**: open children with no open blockers and no assignee; first in map order.
- **Claim**: `gh issue edit <n> --add-assignee @me` before other work.
- **Resolve**: comment with answer, close issue, append gist + link to map **Decisions so far**.
