# Knowledge Index

This file is the agent's map of the knowledge base.
Load this file first — then load individual files only when needed.
Never load all knowledge files at once.

## Load Policy

| Policy | Meaning |
|---|---|
| `required` | Always load for this stage |
| `suggested` | Load if relevant to current task |
| `optional` | Load only if explicitly needed |
| `ignore_by_default` | Do not load unless specifically requested |

## Semantic Search

Each knowledge file has `semantic_aliases` — alternative phrases that
map to the same concept. Use these to match what the human asks
to what the knowledge base contains, without exact keyword matching.

Example: if the human says "why are deleted records appearing",
the alias maps to `_knowledge/patterns/data-access.md` even if
the file is titled "Data Access Patterns."

---

## Knowledge Files

| Path | Type | Stage Triggers | Load Policy | Semantic Aliases |
|---|---|---|---|---|
| *(add your files here)* | | | | |

---

## Knowledge File Template

When adding a new knowledge file, include this frontmatter:

```markdown
---
type: pattern
title: "Short descriptive title"
description: "One sentence about what this file contains."
tags: [tag1, tag2]
semantic_aliases:
  - "alternative phrase for what this covers"
  - "another way someone might ask about this"
  - "problem symptom that leads here"
vucp:
  stage_triggers: [research, implement]
  load_policy: required
  confidence: high
  last_reviewed: YYYY-MM-DD
---
```

## Semantic Alias Guidelines

Write aliases as **problem descriptions or questions**, not topic names.
The topic name is already in the title. Aliases are for discovery.

Good aliases:
- "why are deleted records showing up in queries"
- "component renders twice on the client"
- "deployment failed immediately after push"

Bad aliases:
- "database"
- "soft delete"
- "deployment"

---

## Cross-References

When a knowledge file connects to an error or learning, add it here:

| Knowledge File | Related ERRORS.md entry | Related LEARNINGS.md entry |
|---|---|---|
| *(fill in as connections emerge)* | | |
