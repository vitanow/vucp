---
type: pattern
title: Error Handling
description: How errors are caught, mapped, and returned — API, Server Actions, and UI.
tags: [errors, patterns, api, server-actions, typescript]
vucp:
  stage_triggers: [implement, review]
  load_policy: required
  confidence: high
  last_reviewed: 2026-06-27
---

# Error Handling

## API Routes

```typescript
// Always return consistent error shape
export async function POST(request: Request) {
  try {
    const body = await request.json()
    const validated = schema.parse(body) // Zod — throws if invalid

    const result = await createProject(validated)
    return Response.json({ data: result }, { status: 201 })

  } catch (error) {
    if (error instanceof ZodError) {
      return Response.json(
        { code: "VALIDATION_ERROR", message: "Invalid input", details: error.flatten() },
        { status: 400 }
      )
    }
    // Log to monitoring, never expose internals
    console.error("[POST /api/projects]", error)
    return Response.json(
      { code: "INTERNAL_ERROR", message: "Something went wrong" },
      { status: 500 }
    )
  }
}
```

## Server Actions

```typescript
"use server"

export async function createProject(formData: FormData) {
  const session = await getSession()
  if (!session) redirect("/login")

  const validated = projectSchema.safeParse(Object.fromEntries(formData))
  if (!validated.success) {
    return { error: validated.error.flatten().fieldErrors }
  }

  try {
    const project = await db.createProject({ ...validated.data, ownerId: session.user.id })
    revalidatePath("/projects")
    return { data: project }
  } catch (error) {
    return { error: { _form: ["Failed to create project"] } }
  }
}
```

## UI Error Display

```tsx
// Never crash the whole page — use error boundaries
// For form errors: display inline, not as alerts
// For async errors: toast notification
```

## What Claude Must Never Do

- Never `throw new Error("message")` in an API route without catching it
- Never return raw Prisma/DB error messages to the client
- Never use `any` as the error type — use `unknown` and narrow
- Never ignore the error case in `safeParse` results
