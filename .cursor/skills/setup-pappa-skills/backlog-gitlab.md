# Issue tracker: GitLab

Issues and specs live as GitLab issues. Use [`glab`](https://gitlab.com/gitlab-org/cli).

## Conventions

- **Create**: `glab issue create --title "..." --description "..."`
- **Read**: `glab issue view <number> --comments`
- **List**: `glab issue list` with label filters
- **Comment**: `glab issue note <number> --message "..."`
- **Labels**: `glab issue update <number> --label "..."` / `--unlabel "..."`
- **Close**: note with explanation, then `glab issue close <number>`

## When a skill says "publish to the backlog"

Apply **3-amigos** to the draft, then create a GitLab issue.

## When a skill says "fetch the relevant ticket"

`glab issue view <number> --comments`

## Epic duck operations

- **Map**: issue labelled `epic-duck:map`.
- **Child**: `Part of #<map>` at top of description; label `epic-duck:<type>`.
- **Blocking**: `/blocked_by #<n>` quick action as a note, or `Blocked by:` line when native blocking unavailable.
- **Frontier**: open children, unblocked, unassigned; first in map order.
- **Claim**: `glab issue update <n> --assignee @me`
- **Resolve**: note answer, close, update map **Decisions so far**
