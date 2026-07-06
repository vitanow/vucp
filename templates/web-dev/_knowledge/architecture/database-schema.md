---
type: architecture
title: Database Schema
description: Current database schema — models, relations, important fields.
tags: [database, schema, prisma, models]
vucp:
  stage_triggers: [context-load, implement]
  load_policy: required
  confidence: high
  last_reviewed: 2026-06-27
---

# Database Schema

## Current Schema Summary

<!-- Paste a simplified version of your schema here. Update when schema changes. -->
<!-- This is what Claude reads instead of asking you to explain the models. -->

```prisma
<!-- Example:

model User {
  id        String   @id @default(cuid())
  email     String   @unique
  name      String?
  role      Role     @default(USER)
  createdAt DateTime @default(now())
  sessions  Session[]
  projects  Project[]
}

model Project {
  id          String   @id @default(cuid())
  name        String
  slug        String   @unique
  ownerId     String
  owner       User     @relation(fields: [ownerId], references: [id])
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt
}

enum Role {
  USER
  ADMIN
}
-->
```

## Important Constraints

<!-- Rules Claude must know about the schema -->
<!--
- User.email is unique and immutable after creation
- Project.slug is generated on creation and never changes (used in URLs)
- Soft deletes: use deletedAt DateTime? — never hard delete User or Project
- All timestamps are UTC in DB, convert to user timezone in UI only
-->

## Recent Changes

<!-- Track schema changes here so Claude knows what's new -->
<!--
- 2026-06-20: Added refreshToken model for JWT rotation
- 2026-06-15: Added Project.isPublic boolean field
-->
