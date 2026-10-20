---
name: question-duck
description: Stress-test a plan or design through a relentless, round-based interview until shared understanding is reached. Use when the user wants to interrogate an idea, stress-test a design, refine decisions before writing docs or code, or when the user invokes question-duck.
---

Interview the user until you reach **shared understanding**. Model the work as a **design tree**: decisions branch into dependent decisions.

Work in **rounds**. The **frontier** is every question whose prerequisites are already settled — ask the whole frontier each round. Number questions; give a **recommended answer** per question; wait for answers before the next round.

Format:

```
❓ **Q1** - **<title>**: <body, options if useful>

➡️ <recommended answer>

---

❓ **Q2** - **<title>**: …

➡️ …
```

Phrase questions so "yes" accepts the recommendation.

After each round, recompute the frontier. Do not ask questions that depend on unsettled answers in the same round.

**Facts are yours to find** — dispatch subagents for filesystem, docs, or tooling lookups. Do not ask the user for what you can look up. Decisions stay with the user.

Stop when the frontier is empty. Do not implement until the user confirms shared understanding.
