---
type: pattern
title: Component Structure
description: How components are organized and written in this project.
tags: [components, patterns, react, nextjs, structure]
vucp:
  stage_triggers: [implement, review]
  load_policy: required
  confidence: high
  last_reviewed: 2026-06-27
---

# Component Structure

## Rules

```yaml
server_components: "default — use unless interactivity required"
client_components: "add 'use client' only when: useState, useEffect, event handlers, browser APIs"
colocation: "keep component-specific types, hooks, and utils in same folder"
barrel_exports: "index.ts per feature folder, not per component"
```

## File Structure Per Feature

```
src/features/projects/
  components/
    ProjectCard.tsx        ← pure display, server component
    ProjectList.tsx        ← maps data, server component
    CreateProjectForm.tsx  ← form with state, client component
  hooks/
    useProjectForm.ts      ← client-side form logic
  actions/
    createProject.ts       ← server action
  types.ts                 ← feature-specific types
  index.ts                 ← public API of this feature
```

## Component Template

```tsx
// Server Component (default)
import type { Project } from "@/types"

interface ProjectCardProps {
  project: Project
  className?: string
}

export function ProjectCard({ project, className }: ProjectCardProps) {
  return (
    <div className={className}>
      <!-- content -->
    </div>
  )
}
```

```tsx
// Client Component (only when needed)
"use client"

import { useState } from "react"

interface Props {
  onSubmit: (data: FormData) => Promise<void>
}

export function CreateProjectForm({ onSubmit }: Props) {
  const [isPending, setIsPending] = useState(false)
  <!-- ... -->
}
```

## What Claude Should Never Do

- Do not add `"use client"` to a component that doesn't need it
- Do not import server-only modules in client components
- Do not put business logic in UI components — extract to hooks or actions
- Do not create a new component file for something used only once inline
