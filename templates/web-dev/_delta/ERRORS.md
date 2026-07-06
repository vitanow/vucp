# Documented Errors & Resolutions

<!-- This file is Claude's memory of past mistakes. -->
<!-- Format: ## Error Name / Symptom / Root Cause / Fix / Claude Instruction -->

---

## Error: Prisma client out of sync after schema change
**Discovered:** first use
**Symptom:** TypeScript errors on new fields, or runtime errors accessing new model fields.
**Root cause:** `prisma generate` not run after `schema.prisma` was modified.
**Fix:**
```bash
npx prisma generate          # regenerate client types
npx prisma migrate dev       # apply migration in dev
```
**Claude instruction:** After ANY edit to `schema.prisma`, always remind the human to run
`prisma generate`. Never write code using new schema fields before confirming generate was run.

---

## Error: "use client" added unnecessarily
**Discovered:** first use
**Symptom:** Component marked as client component but has no interactivity, causing unnecessary
client bundle increase and loss of server-side data fetching.
**Root cause:** Claude defaults to `"use client"` when unsure.
**Fix:** Remove `"use client"`. Convert to Server Component.
**Claude instruction:** Never add `"use client"` unless the component explicitly needs:
useState, useEffect, event handlers (onClick, onChange, etc.), or browser-only APIs.
When in doubt, default to Server Component.

---

## Error: Auth session checked in component instead of middleware
**Discovered:** first use
**Symptom:** Protected pages flash unauthorized state briefly, or auth check logic duplicated
across multiple components.
**Root cause:** Auth guard placed inside Server Component instead of middleware.
**Fix:** Move auth check to `middleware.ts`. Components should assume user is authenticated
if they are on a protected route.
**Claude instruction:** Never add auth session checks inside page components or layouts
for protected routes. The middleware handles this. Only call `getSession()` when you need
the user data itself, not to redirect unauthenticated users.

---

## Error: Raw Prisma error exposed in API response
**Discovered:** first use
**Symptom:** API returns `{"message": "PrismaClientKnownRequestError: ..."}` to client.
**Root cause:** Unhandled Prisma error thrown through to response.
**Fix:** Always wrap DB calls in try/catch. Map Prisma errors to clean API error responses.
**Claude instruction:** Never let Prisma errors bubble up to API responses. Always catch,
log server-side, and return a clean `{ code, message }` JSON error.

---

## Error: Missing NULL check on soft-deleted records
**Discovered:** first use
**Symptom:** Deleted records appear in queries.
**Root cause:** `deletedAt: null` filter missing from Prisma query.
**Fix:** Add `where: { deletedAt: null }` to all queries on models with soft delete.
**Claude instruction:** For any model that has a `deletedAt` field, always include
`deletedAt: null` in the where clause unless explicitly querying for deleted records.

---

## Error: Environment variable used in client component without NEXT_PUBLIC_ prefix
**Discovered:** first use
**Symptom:** Variable is `undefined` at runtime in browser, works fine in server code.
**Root cause:** Next.js only exposes env vars to the browser if prefixed with `NEXT_PUBLIC_`.
**Fix:** Either rename to `NEXT_PUBLIC_VAR_NAME` (if safe to expose) or move usage to server-only code.
**Claude instruction:** Before using `process.env.VARIABLE` in any client component or
browser-executed code, confirm it has the `NEXT_PUBLIC_` prefix. If the value is sensitive,
it must never be in client code — move to a Server Action or API route.


---

## Confidence Scoring

Use these fields for recurring entries:

```yaml
status: candidate|confirmed|deprecated|resolved
confidence: 0.0
occurrence_count: 1
last_seen: YYYY-MM-DD
```

`confidence >= 0.8` with repeated evidence should be treated as an operational rule until deprecated.
