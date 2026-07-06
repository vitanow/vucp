# Semantic Aliases and Manual Graph Links

Status: optional v0.5 extension.

VUCP is filesystem-native and plain-text. It does not require a vector database or graph database.

It can still support lightweight semantic discovery through:

1. `semantic_aliases`
2. `cross_references`

## `semantic_aliases`

Use when a concept may be searched for with different words.

```yaml
---
type: knowledge
title: "Rollback-first deployment"
semantic_aliases:
  - "safe deployment"
  - "undo plan"
  - "revert strategy"
  - "production safety"
tags:
  - deployment
  - safety
  - rollback
---
```

## `cross_references`

Use to create manual graph links between related VUCP files.

```yaml
cross_references:
  - "_delta/ERRORS.md#missing-rollback-plan"
  - "_knowledge/patterns/deployment-safety.md"
  - "~/.vucp-user/_cross_project_patterns/architecture/rollback-first-deployment.md"
```

## Rules

- Use 3–7 aliases per important knowledge item.
- Use 1–5 cross references per learning/error/pattern.
- Do not follow every cross-reference automatically.
- Do not recursively load the whole graph.
- A semantic alias is a hint, not proof.

## Usage in _knowledge/index.md

The `_knowledge/index.md` table should reference aliases for discovery:

```markdown
| Path | Type | Title | Tags | Semantic Aliases |
|---|---|---|---|---|
| `_knowledge/patterns/data-access.md` | pattern | Data Access | database | "deleted records appearing", "NULL in query results" |
```

## Usage in _delta/LEARNINGS.md and ERRORS.md

Add `cross_references:` to any entry that connects to another file:

```markdown
## Learning: Always NULL-check before JOIN
confidence: 0.91
cross_references:
  - "_delta/ERRORS.md#prisma-null-join"
  - "_knowledge/patterns/data-access.md"
  - "~/.vucp-user/_user_contexts/software.md"
```

## Relationship to Semantic Memory Tools

VUCP semantic aliases are not a replacement for vector search or tools
like Cognee, Mem0, or Zep. They are a lightweight, portable alternative
that works without any external dependency.

Use semantic aliases when you want discoverable knowledge with zero setup.
Use a semantic memory tool when you need meaning-based search across
large corpora or personal fact retrieval across projects.
