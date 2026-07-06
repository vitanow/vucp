---
type: pattern
title: Data Access Patterns
description: How to query the database — repository pattern, conventions, dos and don'ts.
tags: [database, prisma, patterns, data-access, repository]
vucp:
  stage_triggers: [implement]
  load_policy: required
  confidence: high
  last_reviewed: 2026-06-27
---

# Data Access Patterns

## Rule: All DB Access Through /src/server/db/

Never import Prisma client directly in components, pages, or API routes.
Always go through the repository layer.

```
src/server/db/
  index.ts          ← Prisma client singleton
  projects.ts       ← All project queries
  users.ts          ← All user queries
```

## Repository Pattern Example

```typescript
// src/server/db/projects.ts
import { db } from "./index"
import type { Project, Prisma } from "@prisma/client"

export async function getProjectsByUser(userId: string): Promise<Project[]> {
  return db.project.findMany({
    where: { ownerId: userId, deletedAt: null },
    orderBy: { createdAt: "desc" },
  })
}

export async function createProject(
  data: Prisma.ProjectCreateInput
): Promise<Project> {
  return db.project.create({ data })
}
```

## Common Mistakes Claude Must Avoid

- **Never** call `prisma.user.findMany()` directly in a Server Component
- **Never** use `include` to fetch deeply nested relations unless explicitly needed
- **Always** add `deletedAt: null` to queries if the model uses soft deletes
- **Always** handle the case where a query returns `null` — do not assume records exist
- **Never** expose raw Prisma errors to the client — catch and map to API errors

## Transaction Pattern

```typescript
// For operations that must succeed together
const result = await db.$transaction(async (tx) => {
  const project = await tx.project.create({ data: projectData })
  await tx.auditLog.create({ data: { action: "project.created", projectId: project.id } })
  return project
})
```
