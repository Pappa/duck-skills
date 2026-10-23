Type: epic-duck:decision
Status: resolved
Plan: [0001-plan-duck-skills-planning-refinement.md](0001-plan-duck-skills-planning-refinement.md)
Overview: Decide how to close every open skill/doc discrepancy from spike 0003 (v2.4).
Blocked by:

## Question

For each open finding from skill inventory spike **0003** ([v2.4 synthesis](../spike/0003-skill-inventory-v2.4.md); detail in [v2.1](../spike/0003-skill-inventory-v2.1.md)–[v2.3](../spike/0003-skill-inventory-v2.3.md)), what is the **disposition** (fix now, defer with owner, or explicitly accept as-is) and **what changes** (file paths, wording rules)?

Resolution must produce a single **`## Answer`** that addresses **every row** below. For each row: **disposition**, **owner artefact** (skill, doc, backlog item, or none), and **acceptance** (how we know it is done). Do **not** re-litigate ADR 0001 shapes or re-open **0004** choreography intent — only align skills and docs to **0004** and current canon.

### Register (v2.4 — required)

| ID | Severity | Topic |
|----|----------|-------|
| C-0004-rubber | High | Rubber backlog children + **amigo-duck** before publish per **0004** vs `rubber-duck/SKILL.md` (domain-only today) |
| C-0004-epic-arch | High | Epic invokes **architect-duck** / may delegate **rubber-duck** per **0004** vs `epic-duck/SKILL.md` invoke list |
| C-readme-rubber | Medium | `README.md` planning flow implies rubber → tickets vs rubber skill |
| C-0002-stale | Medium | **0002** Answer still uses `Label: ready`, bare `Type: decision` |
| C-0011-stale | Medium | Spike **0011** still proposes `Label: ready` (superseded by **0005**/ADR) |
| C-epic-labelled | Low | Epic “labelled `epic-duck:plan`” vs local **`Type:`** |
| C-github-frontier | Low | `setup-duck-skills/backlog-github.md` frontier omits **`needs-triage`** |
| C-spike-NNNN | Low | **spike-duck** may allocate `NNNN` when epic-duck already created spike item |
| C-frontier-term | Low | “Frontier” homonym: **question-duck** vs epic/backlog |
| C-plan-notes | Low | Plan **0001** Notes: epic uses **architect-duck**; epic `SKILL.md` omits |

### Additional findings (v2.1 — required)

| ID | Severity | Topic |
|----|----------|-------|
| R4 | Low | README lists **question-duck** / **architect-duck** as model-invoked vs **0004** v1 entry-point rule |
| R6 | Low | Spike resolve bookkeeping: `backlog.md` vs `epic-duck/SKILL.md` work-through |
| R7 | Low | Optional **`## Comments`** on child templates in epic-duck vs `backlog.md` / ADR |

### Cosmetic / hygiene (v2.3 — required)

| ID | Topic |
|----|-------|
| L3 | **spike-duck** typo “authritative” in `SKILL.md` |

### Explicitly out of this decision’s scope

- **triage** behaviour and activation — decision **0006**
- **Eval harness** — out of scope on plan **0001**
- **v1 C1–C2** — already resolved (ADR 0001); no action unless Answer records “verified closed”
- **R9** / v2.4 “resolved since v1” rows — confirm closed only; no new design

### Cross-cutting rules the Answer must state

1. Whether remediation is **one deliverable task** or **multiple tasks** after this decision (and if tasks are created, their slugs or numbers).
2. Whether **resolved** backlog items (**0002**, spike **0011**) get **Answer amendments**, **Comments** pointers to **0005**/ADR, or **wontfix** on historical prose.
3. Order of operations when **0004** skill edits touch the same files as low-severity wording fixes.

## Comments

**Session notes (0014 interview):**

- **Q1:** One remediation **task** for now; user may split later if change list too large.
- **Q2:** Amend **0002** and **0011** bodies — remove legacy `Label:` / bare `Type:` prose entirely (rewrite as if always ADR canon).
- **Q3:** Same session for all edits touching the same `SKILL.md`.
- **Q4 (corrected):** **epic-duck** → `epic-duck:decision` | `epic-duck:task` | `epic-duck:spike` (planning). **rubber-duck** → plain **`Type: task`** | **`Type: spike`** (implementation/dev only; not planning). No rubber decisions. Session outcomes: clarity, doc/code change, or impl task/spike. question-duck + architect-duck; no epic↔rubber delegation.
- **Q5–Q6:** Epic invokes **architect-duck** like rubber; aligned wording.
- **Q8:** amigo-duck must review both planning and implementation item formats.
- **Q9:** existing plan only — **handover TBD** when user has ready artefact but no plan.
- **Q10–Q12:** amend **0004**; fix README; no user-callable question/architect; batch low-severity fixes.
- **Q9:** unanchored impl items: **`Status: needs-triage`**, sentinel **`Plan:`**, user message about triage later. **Q9b:** sentinel on `Plan:` line (exact string TBD in Answer).
- **Q14:** same counter/`.backlog/items/`; filenames **`NNNN-task-<slug>.md`** (planning **`epic-duck:task`** and implementation **`task`**), **`NNNN-spike-<slug>.md`**; `Type:` distinguishes families.
- **Q15:** `disable-model-invocation: true` + **`allow_implicit_invocation: true`** on question-duck & architect-duck (YAML + README).
- **Q13:** reword question-duck; reserve **Frontier** for backlog — user reviewing alternatives (see chat).

## amigo-duck review

**Verdict: Approve**

| Axis | Result |
|------|--------|
| Fit | Matches user intent: one decision to disposition all spike 0003 open findings. |
| Complete | Enumerates v2.4 register, v2.1 extras, cosmetic L3; boundaries to 0006 and eval out-of-scope are explicit. |
| Plain language | Tables scan by ID; resolution outputs are defined (disposition, artefact, acceptance). |
| INVEST | Decision-sized; testable Answer checklist per row. |

**Assumption:** “Resolve” means agreed disposition and change spec — implementation may land in follow-on **epic-duck:task** items created in the same Answer.

## Answer

### Cross-cutting

| Rule | Decision |
|------|----------|
| Follow-on work | **One** deliverable task **[0015](0015-task-remediate-skill-inventory-findings.md)** (`Status: ready`); user may split after reviewing the diff. |
| **0002** / **0011** historical prose | **Rewrite in place** — remove all `Label: ready`, bare `Type: decision`, and pre-namespace spike recommendations; text reads as if ADR 0001 always applied. |
| Edit order | All changes to the same `SKILL.md` in **one** edit pass (planning alignment + low-severity rows for that file). |
| **0004** | **Amend Answer** to match this decision (rubber impl items only, no rubber decisions, no epic↔rubber delegation). Supersedes conflicting bullets in old **0004** text. |
| Orchestrator invocation | **epic-duck** and **rubber-duck** are user-invoked only (`disable-model-invocation`); they do **not** delegate to each other. **question-duck** / **architect-duck**: not user-invoked; **`allow_implicit_invocation: true`** so epic/rubber can use them. Do not add prose restating YAML flags. |

### Two backlog families

| Publisher | `Type:` values | Filename patterns | Purpose |
|-----------|----------------|-------------------|---------|
| **epic-duck** | `epic-duck:plan`, `epic-duck:decision`, `epic-duck:task`, `epic-duck:spike` | `*-plan-*`, `*-decision-*`, `NNNN-task-<slug>.md`, `NNNN-spike-<slug>.md` | Planning |
| **rubber-duck** | `task`, `spike` (no `epic-duck:` prefix) | `NNNN-task-<slug>.md`, `NNNN-spike-<slug>.md` | Implementation / development |

Shared **NNNN** counter and `.backlog/items/` path. Spike **findings** stay `.backlog/spike/<NNNN>-<slug>.md` (no `Type:` on findings file).

**rubber-duck** does **not** create `epic-duck:decision` or any planning-type item.

**Unanchored handover:** When the user has no feature plan, rubber may still write an impl item with **`Plan: (unanchored)`**, **`Status: needs-triage`**, correct **NNNN** and impl `Type:`. Rubber **must** tell the user the ticket is **not associated with a feature** and **will need to be triaged later**. **epic-duck** attaches a real `Plan:` link when a feature is chosen.

**amigo-duck** runs before publish for **both** families; skill text must describe review rules per `Type:` profile.

### Register dispositions

| ID | Disposition | Owner | Acceptance |
|----|-------------|-------|------------|
| **C-0004-rubber** | Fix now | `rubber-duck/SKILL.md`, `backlog.md` | Rubber documents impl **task**/**spike**, outcomes, question + architect, amigo gate, unanchored rule + user message; no decisions. |
| **C-0004-epic-arch** | Fix now | `epic-duck/SKILL.md` | Epic documents **architect-duck** invoke (wording aligned with rubber); planning types only; no rubber delegation. |
| **C-readme-rubber** | Fix now | `README.md` | Rubber vs epic flows correct; rubber not generic “tickets”. |
| **C-0002-stale** | Fix now | `0002` Answer | No `Label:` / bare `Type: decision`. |
| **C-0011-stale** | Fix now | `spike/0011` findings | Rewritten to ADR canon. |
| **C-epic-labelled** | Fix now | `epic-duck/SKILL.md` | Local plans use first-line **`Type: epic-duck:plan`**; remote labels explained without implying a `Label:` header. |
| **C-github-frontier** | Fix now | `setup-duck-skills/backlog-github.md` | Frontier lists **`needs-triage`** and **`needs-detail`**. |
| **C-spike-NNNN** | Fix now | `spike-duck/SKILL.md` | Use existing spike item when epic set `Result:` / item exists. |
| **C-frontier-term** | Fix now | `question-duck/SKILL.md` | Replace interview “frontier” with **open/closed** round rules (lines 8, 26, 30); **Frontier** reserved for backlog only. |
| **C-plan-notes** | Accept | Plan **0001** Notes | Keep “epic uses architect-duck”; epic skill updated to match (**C-0004-epic-arch**). |
| **R4** | Fix now | `README.md`, question/architect YAML | Not user entry points; implicit invocation enabled. |
| **R6** | Fix now | `epic-duck/SKILL.md` | Spike resolve steps match `backlog.md` (plan tables / **Decisions so far** when appropriate). |
| **R7** | Fix now | `epic-duck/SKILL.md` templates | Optional **`## Comments`** on child templates per `backlog.md`. |
| **L3** | Fix now | `spike-duck/SKILL.md` | “authoritative” spelled correctly. |
| **v1 C1–C2** | Verified closed | — | ADR 0001; no further action. |
| **R9** | Verified closed | — | Superseded by **0005**/ADR. |

### question-duck round wording (canonical)

1. Each round, ask every question that is still **open**, as long as every question it **depends on** is already **closed**. Ask all of those in one round (numbered, with a recommended answer each); then wait for answers.
2. After each round, update which questions are **closed**, then compute the next **open** set. Do not ask **open** questions in the same round if they still depend on another **open** question.
3. Stop when there are no **open** questions left. Do not implement until the user confirms shared understanding.

### Implementation

All edits above are tracked in task **[0015-task-remediate-skill-inventory-findings.md](0015-task-remediate-skill-inventory-findings.md)** acceptance criteria.

### Amendment (planning task filenames)

Planning **`epic-duck:task`** items use **`NNNN-task-<slug>.md`** — the same path pattern as implementation **`Type: task`**. **`Type:`** on the first line distinguishes planning from implementation. ADR 0001 and existing planning task files **0015**, **0016** renamed accordingly.
