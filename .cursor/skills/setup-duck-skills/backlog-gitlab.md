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

## Epic-duck operations

Used by **epic-duck**. **Plan** parent issue labelled `epic-duck:plan`; children are issues. Status vocabulary: `needs-detail`, `in-progress`, `resolved`, `out-of-scope` (labels or description).

- **Plan**: issue labelled `epic-duck:plan`.
- **Child**: `Part of #<feature>` at top of description; label `epic-duck:<type>` (`spike` | `interrogate` | `task`).
- **Blocking**: `/blocked_by #<n>` quick action as a note, or `Blocked by:` line when native blocking unavailable.
- **Frontier**: children `needs-detail` / open, unblocked; lowest id first.
- **Claim**: `glab issue update <n> --assignee @me` for the session.
- **Resolve**: note answer, close or mark `resolved`, update feature **Decisions so far**. Remove blocking links when a blocker is `resolved` or `out-of-scope`.
