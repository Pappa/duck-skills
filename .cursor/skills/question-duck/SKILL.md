---
name: question-duck
description: Round-based Q&A to remove ambiguities and reach a shared understanding with the user.
disable-model-invocation: true
---

Interrogate a plan or design using a thorough, round-based Q&A interview until all assumptions are documented, no ambiguities remain, and a shared understanding with the user is reached. Use this skill when refining a feature, resolving a planning decision, or sharpening a design before making changes to docs, requirements, backlog items, or code.

Interview the user until you reach **shared understanding**. Model the work as a **design tree**: decisions branch into dependent decisions.

Work in **rounds**. Each round, ask every question that is still **open**, as long as every question it **depends on** is already **closed**. Ask all of those in one round (numbered, with a recommended answer each); then wait for answers.

Format:

```
❓ **Q1** - **<title>**: <body, options if useful>

➡️ <recommended answer>

---

❓ **Q2** - **<title>**: …

➡️ …
```

Phrase questions so "yes" accepts the recommendation.

After each round, update which questions are **closed**, then compute the next **open** set. Do not ask **open** questions in the same round if they still depend on another **open** question.

**Facts are yours to find** — dispatch subagents for filesystem, docs, or tooling lookups. Do not ask the user for what you can look up. Decisions stay with the user.

Stop when there are no **open** questions left. Do not implement until the user confirms shared understanding.
