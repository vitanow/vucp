---
type: pattern
title: Testing Patterns
description: How tests are structured and written in this project.
tags: [testing, vitest, playwright, patterns]
vucp:
  stage_triggers: [test]
  load_policy: required
  confidence: medium
  last_reviewed: 2026-06-27
---

# Testing Patterns

## Test Stack

```yaml
unit: Vitest
integration: Vitest + testcontainers (or Prisma test environment)
e2e: Playwright
```

## Unit Test Template

```typescript
// src/server/db/projects.test.ts
import { describe, it, expect, vi } from "vitest"
import { getProjectsByUser } from "./projects"

vi.mock("./index", () => ({
  db: {
    project: {
      findMany: vi.fn(),
    },
  },
}))

describe("getProjectsByUser", () => {
  it("returns projects for a valid user", async () => {
    const mockProjects = [{ id: "1", name: "Test", ownerId: "user-1", deletedAt: null }]
    vi.mocked(db.project.findMany).mockResolvedValue(mockProjects)

    const result = await getProjectsByUser("user-1")
    expect(result).toEqual(mockProjects)
    expect(db.project.findMany).toHaveBeenCalledWith({
      where: { ownerId: "user-1", deletedAt: null },
      orderBy: { createdAt: "desc" },
    })
  })
})
```

## What Claude Must Always Do in Tests

- Mock external dependencies (DB, APIs, email) — never hit real services in unit tests
- Test the error path as well as the happy path
- Use descriptive test names: `it("returns 401 when token is expired")`
- Never test implementation details — test behavior
