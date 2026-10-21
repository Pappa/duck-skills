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

Apply **amigo-duck** to the draft, then create a GitHub issue.

## When a skill says "fetch the relevant ticket"

`gh issue view` as above.

## Epic-duck operations

Used by **epic-duck**. The **feature** (parent) is one issue labelled `epic-duck:plan`; **children** are sub-issues. Use the same **`Status:`** strings as local markdown (`docs/agents/ticket-statuses.md`) — as labels and/or `Status:` in the body (match team practice).

- **Plan**: issue labelled `epic-duck:plan` (Destination, Notes, Decisions, fog, Out of scope in body).
- **Child**: sub-issue of the feature (or `Part of #<parent>` in body). Label `epic-duck:<type>` (`spike` | `decision` | `task`).
- **Blocking**: native issue dependencies — `gh api --method POST repos/<owner>/<repo>/issues/<child>/dependencies/blocked_by -f issue_id=<blocker-db-id>` where `issue_id` is the blocker's database id (`gh api repos/<owner>/<repo>/issues/<n> --jq .id`). Fallback: `Blocked by: #n` at top of body.
- **Frontier**: children in `needs-detail` (or open) with no open blockers; lowest id first.
- **Claim**: `gh issue edit <n> --add-assignee @me` before other work (session-long on remote; no per-round toggle).
- **Resolve**: comment with answer, close or mark `resolved`, append gist + link to feature **Decisions so far**. When a blocker is `resolved` or `out-of-scope`, remove its blocking links from dependents.
