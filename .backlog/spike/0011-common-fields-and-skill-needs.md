Spike: [0011-spike-common-fields-and-skill-needs.md](../items/0011-spike-common-fields-and-skill-needs.md)

# Common fields and ticket shapes

## TLDR

Use a **shared common-fields header** on every `.backlog/items/*` file (`Status`, `Overview` where applicable, `Plan:` backlink, `Blocked by:`), then **body profiles** by kind. **`docs/agents/backlog.md` is the single source of truth** for local markdown. **`Type: decision`** is the main body exception (`## Question` / `## Answer`). **`Label: ready`** on **`Type: task`** is the second exception (`## Acceptance criteria`, full amigo-duck). **Spike items** add `Result:`; **spike findings** are free-form research docs with `Spike:` backlink + **TLDR**. **Plans** use `Destination` instead of `Overview` and omit `Plan:`. Record the canon in an ADR via **0005**; align **amigo-duck** to local kinds (not `epic-duck:spike` on files).

Upstream **writing-for-agents** favours checkable completion criteria and one authoritative doc—maps to testable AC and `backlog.md`. **pr** skill favours fixed sections (Summary, Evidence)—maps to optional `## Evidence` on large ready tasks only.

Sources: `docs/agents/backlog.md`, `.cursor/skills/*/SKILL.md`, `.backlog/spike/0003-skill-inventory.md`, `~/.agents/skills/writing-for-agents/SKILL.md`, `~/.agents/skills/pr/SKILL.md`.

---

## Recommendation summary

| Kind | File pattern | Common fields | Body profile |
|------|----------------|---------------|--------------|
| **Plan** | `*-plan-*.md` | `Status` only at item level; indexed in `features.md` | Destination, Notes, Decisions so far, Not yet specified, Out of scope, Decisions, Tasks, Spikes |
| **Decision** | `<NNNN>-decision-<slug>.md` | + `Plan`, `Overview`, `Type: decision`, `Blocked by` | `## Question`; when resolved `## Answer`; `## Comments` |
| **Task** | `<NNNN>-<slug>.md` (slug not `plan-`, `decision-`, `spike-`) | + `Type: task`, optional `Label:` | **Branch A — unblocker:** `## Question` (+ `## Answer` when resolved). **Branch B — ready:** `Label: ready` + `## Acceptance criteria` (+ optional `## User intent`, `## Out of scope for this ticket`) |
| **Spike item** | `*-spike-*.md` | + `Plan`, `Overview`, `Result`, `Blocked by` (no `Type:`) | `## Question`; `## Comments` |
| **Spike findings** | `.backlog/spike/<NNNN>-*.md` | `Spike:` link line | **TLDR**; research sections; cite sources |
| **Ready deliverable** | Task with `Label: ready` | Same as task branch B | amigo-duck treats draft as story + AC (INVEST full) |

Spikes are always spike **items** (+ findings file), never a `Type:` on decision or task files.

---

## Common fields (local markdown)

Ordered block for **decisions**, **tasks**, and **spike items** (canonical order for **0005** / ADR):

```markdown
Status: <needs-detail|in-progress|resolved|out-of-scope>
Plan: [<NNNN>-plan-<slug>.md](<same-dir>)
Overview: <one sentence>
Type: decision | task          # decisions and tasks only; omit on spike items
Label: ready                   # optional; only roles from ticket-labels.md
Blocked by:                    # optional; comma-separated NNNN
```

**Plans** start with `Status:` then **Destination** (acts as overview for `features.md`). No `Plan:` line.

**Remote trackers** (GitHub/GitLab/Azure): map `Type` + `Label` to `epic-duck:<type>` tags and triage labels per `setup-duck-skills/backlog-*.md`; do not duplicate tag names as extra markdown fields on local files.

---

## Body profiles and skill needs

### amigo-duck

| Input kind | Required body for review | INVEST |
|------------|--------------------------|--------|
| `Label: ready` | `Overview` + testable `## Acceptance criteria` | Full |
| `Type: decision` | `## Question` (+ `## Answer` if resolving) | Light |
| `Type: task` (no ready) | `## Question` or spec pointer; deliverable clear | Light–medium |
| Spike item (pre-publish) | `## Question` | Light |

**Skill change (0005):** Replace `` `epic-duck:spike` `` with “spike **item**” / “findings file”; rename output heading from `## 3 amigos session` to `## amigo-duck review` (eval artefacts depend on stable heading).

### epic-duck

- Publishes all shapes above; must match `backlog.md`.
- Resolved decisions: require `## Answer` before `Status: resolved`.
- Charting: spike **item** first, `Result:` path, then spike-duck writes findings.

### spike-duck

- Findings: top `Spike:` backlink; **TLDR**; no `Status` on findings file.
- When `Result:` already exists on spike item, do not allocate a new `NNNN`.

### rubber-duck / architect-duck

- No backlog fields; glossary/ADR only. Ready tickets may **point to** `GLOSSARY.md` in AC.

### setup-duck-skills / triage-duck (future)

- Seeds `backlog.md` + `ticket-labels.md`. Future triage reads `Status` + optional `Label:`; do not conflate `Status:` (workflow) with `needs-detail` label (triage role)—document in **0006**.

---

## Exceptions (why not one body for all)

| Exception | Reason |
|-----------|--------|
| **Decision** | Decision unit: Question/Answer + Decision resolution metric (**0002**); not story AC. |
| **Label: ready** | AFK/human execution needs INVEST AC, not a decision Question. |
| **Plan** | Index + fog + decision log; not a child ticket. |
| **Spike findings** | Research narrative; spike item holds tracker metadata. |
| **Task without ready** (e.g. implement when spec elsewhere) | Today uses `## Question` as spec pointer + ad-hoc deliverable in Comments (**0009**). **0005** should standardise: either `Label: ready` + AC, or `## Spec` + link to spike result—pick one pattern to reduce variance. |

No third `Type:` value needed if **ready** is expressed via `Label:` on `Type: task`.

---

## Contradictions to fix in 0005

| ID | Action |
|----|--------|
| C3 | Edit `amigo-duck/SKILL.md`: local kind names (`decision`, `task`, spike item, `Label: ready`). |
| C6 | Document in `backlog.md`: local plan ≡ remote `epic-duck:plan` via `features.md` + filename. |
| 0009 pattern | Migrate implement tasks to `Label: ready` + AC **or** formal `## Spec` section (0005 decision). |

---

## ADR scope (for 0005)

Create `docs/adr/0001-backlog-ticket-shapes.md` (or next free number) containing:

1. Purpose: one family of shapes for duck-skills + evals.
2. Common-fields table (this spike).
3. Body profiles (templates copied from ADR into `backlog.md`—ADR is rationale + canonical templates; `backlog.md` is agent-facing SSOT per writing-for-agents).
4. Local vs remote label mapping (one paragraph).
5. Deferred: triage-duck field interactions (**0006**).

---

## External reference (Matt Pocock / Total TypeScript skills)

| Upstream idea | Application here |
|---------------|------------------|
| **writing-for-agents:** completion criteria must be checkable | `## Acceptance criteria` on ready tasks; `## Answer` completes decisions |
| **writing-for-agents:** single source of truth | `docs/agents/backlog.md` over epic-duck inline templates |
| **writing-for-agents:** disclose by branch | Body profiles instead of one mega-template |
| **pr:** fixed sections for human review | Optional `## Evidence` on ready tasks when verification is non-obvious (not required for spike findings) |

---

## Open choice for 0005 (not blocking spike)

**Implement-style tasks** without `Label: ready` today (**0009**): adopt **(a)** require `Label: ready` + AC before agent execution, or **(b)** keep `Type: task` + `## Spec` linking spike/ADR. Recommendation: **(a)** for anything an agent runs AFK; **(b)** only for human-only chores.
