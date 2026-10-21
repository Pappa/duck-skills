---
name: amigo-duck
description: Reviews backlog tickets and requirements before publish — fit to the user's request, completeness, unambiguous acceptance criteria, ISO 24495 plain language, and INVEST. Use when creating or updating a backlog ticket, user story, work item, or issue; when drafting acceptance criteria; when the user invokes amigo-duck; or when another skill is about to publish to the backlog.
---

# amigo-duck

Run this **before** creating or updating a backlog ticket on the backlog (including tickets drafted by epic-duck, implement flows, or ad-hoc agent work). Do not publish until the review passes or the user explicitly accepts documented gaps.

## Inputs

Collect:

1. **User intent** — the original request, spec excerpt, or conversation goal the ticket must satisfy.
2. **Draft ticket** — title, description, acceptance criteria (or equivalent fields).

If intent is missing, ask one short question or infer from immediate context and state the assumption in the review.

## Review axes

Work all four axes. Cite the draft text when flagging issues.

### 1. Fit to the user's request

- Every acceptance criterion supports a stated user or business need from the intent.
- Must-have outcomes from the intent appear in the ticket; nothing critical is only implied.
- Scope in the ticket does not exceed the intent unless labeled **out of scope for this ticket** or **follow-up**.
- Contradictions between intent and ticket are called out, not silently "fixed."

### 2. Complete and unambiguous

- **Who** (role or actor), **when** (trigger or precondition), and **what** (observable outcome) are clear for each requirement.
- Acceptance criteria are **testable** — a reviewer could verify pass/fail without guessing.
- No unresolved **and/or**, **etc.**, **as needed**, **appropriate**, **fast**, **easy**, **secure** without measurable or defined meaning.
- Dependencies, data, and edge cases that block implementation are either in the ticket or explicitly deferred with a pointer.

### 3. ISO 24495 plain language

Apply [ISO 24495-1](https://www.iso.org/standard/78907.html) plain-language practice:

- **Relevant**: lead with what the reader must do or decide; cut background they do not need to implement.
- **Findable**: use headings or lists so criteria scan quickly; one main idea per bullet.
- **Understandable**: common words; short sentences; active voice; define domain terms (or point to `GLOSSARY.md`).
- **Usable**: imperative or clear outcome statements; consistent terms throughout (no synonym drift).

Flag sentences that fail plain language and propose a rewrite.

### 4. INVEST (user-story-sized backlog items)

When the item is a deliverable backlog ticket (not an epic-duck **decision** ticket whose only job is to resolve a question), check:

| Criterion | Pass when |
|-----------|-----------|
| **Independent** | Can be done without unfinished siblings, or dependencies are explicit blockers. |
| **Negotiable** | Describes outcome, not a fixed implementation recipe. |
| **Valuable** | Delivers visible value to a user or stakeholder. |
| **Estimable** | Team could size it with stated scope. |
| **Small** | Completable in one iteration; split if not. |
| **Testable** | Acceptance criteria prove done. |

Epic-duck **`Type: decision`** tickets (remote: `epic-duck:decision`, `epic-duck:spike`, etc.): require clear **Question** and resolution criteria; INVEST applies lightly (valuable + testable resolution), not full story sizing.

## Process

1. Run the four axes against the draft.
2. If all pass → **Approve** with a one-line summary.
3. If any fail → **Revise**: list findings by axis with quoted draft fragments and suggested rewrites; produce an updated ticket body; re-run the review on the revision.
4. Publish to the tracker only after **Approve**, or after the user says to publish despite listed gaps (record those gaps in the ticket).

## Output format

```markdown
## 3 amigos session

**Verdict:** Approve | Revise

### Fit to request
- …

### Complete and unambiguous
- …

### Plain language (ISO 24495)
- …

### INVEST
- …

### Revised ticket (if Revise)
<title and body ready to publish>
```

Keep the review under what is needed to act; prefer concrete rewrites over general advice.
