---
name: setup-duck-skills
description: Configure a repo for duck-skills — backlog tracker (GitHub, GitLab, Azure DevOps, local markdown, or custom), ticket status vocabulary, and domain doc layout. Run once per repo before using other duck skills.
disable-model-invocation: true
---

# Setup duck skills

Scaffold per-repo configuration that duck-skills assume:

- **Backlog**: where work items and decision maps live (`docs/agents/backlog.md`)
- **Ticket status**: canonical `Status:` strings (`docs/agents/ticket-statuses.md`)
- **Domain docs**: where `GLOSSARY.md` and ADRs live, and how skills should read them

Prompt-driven setup: explore the repo, present findings, confirm with the user, then write files.

## Process

### 1. Explore

Read what exists; do not assume defaults:

- `git remote -v` and `.git/config` — GitHub, GitLab, `dev.azure.com` / `visualstudio.com`, Origin, or none?
- `AGENTS.md` / `CLAUDE.md` — existing `## Agent skills` section?
- `GLOSSARY.md`, `GLOSSARY-MAP.md`, `docs/adr/`, `docs/agents/`
- `.backlog/` — local-markdown tracker already in use?
- Monorepo signals: `pnpm-workspace.yaml`, `package.json` workspaces, multiple `packages/*` with their own `src/`

### 2. Present findings and ask

Summarise what is present and missing. One section at a time; lead with the recommended answer.

**Section A: Backlog**

> Where does this repo track specs, tickets, and epic-duck maps?

Recommend from remotes:

| Signal | Recommend |
|--------|-----------|
| `github.com` remote | GitHub Issues (`gh`) |
| GitLab remote | GitLab Issues (`glab`) |
| `dev.azure.com` / Azure DevOps remote | Azure DevOps Boards (`az boards` / REST) |
| No remote repo | Local markdown under `.backlog/` |
| Other | Freeform paragraph from the user |

For **Azure DevOps**, also confirm org, project, and team (for area path defaults) and record them in `docs/agents/backlog.md`.

Record the choice in `docs/agents/backlog.md` using a seed template from this folder.

if the choice was a local backlog, create the empty backlog here: `.backlog/features.md`.

**Section B: Ticket status vocabulary**

> Keep default `Status:` strings? (recommended: **yes**)

Defaults: `needs-triage`, `needs-detail`, `ready`, `in-progress`, `resolved`, `wontfix`, `out-of-scope`. On yes, write [ticket-statuses.md](./ticket-statuses.md) to `docs/agents/ticket-statuses.md`. On no, collect overrides.

**Section C: Domain docs**

Default **single-context** (root `GLOSSARY.md` + `docs/adr/`) without asking.

Offer **multi-context** only when monorepo signals appeared: root `GLOSSARY-MAP.md` plus per-context glossaries.

### 3. Confirm and edit

Show drafts of:

- The `## Agent skills` block for `CLAUDE.md` or `AGENTS.md`
- `docs/agents/backlog.md`, `docs/agents/domain.md`, and `docs/agents/ticket-statuses.md`

Let the user edit before writing.

### 4. Write

**Agent config file:**

- If `AGENTS.md` exists → edit it.
- Else if `CLAUDE.md` exists → edit it.
- Else if `.cursor/rules/` exists → ask the user if you should add/edit rules there or create an `AGENTS.md` file.
- Else ask which to create.

Update an existing `## Agent skills` block in place; do not duplicate.

```markdown
## Agent skills

### Backlog

[one-line summary]. See `docs/agents/backlog.md`.

### Ticket status

[one-line summary]. See `docs/agents/ticket-statuses.md`.

### Domain docs

[single-context or multi-context]. See `docs/agents/domain.md`.
```

On GitHub or GitLab, create tracker tags for status strings and `epic-duck:*` types if missing (`gh label create` / `glab label create`).

**Seed templates:**

- [backlog-github.md](./backlog-github.md)
- [backlog-gitlab.md](./backlog-gitlab.md)
- [backlog-azure-devops.md](./backlog-azure-devops.md)
- [backlog-local.md](./backlog-local.md)
- [domain.md](./domain.md)
- [ticket-statuses.md](./ticket-statuses.md)

For custom trackers, write `docs/agents/backlog.md` from the user's description.

### 5. Done

Tell the user setup is complete and which skills read these files (`epic-duck`, `rubber-duck`, `question-duck`, `architect-duck`, `amigo-duck`, `spike-duck`; **`triage-duck`** when shipped per task **0010**). They can edit `docs/agents/*.md` directly; re-run this skill only to switch trackers or restart config.
