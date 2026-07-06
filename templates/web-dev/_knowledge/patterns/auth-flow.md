---
type: pattern
title: Auth Flow
description: How authentication works in this project — session, tokens, guards.
tags: [auth, authentication, jwt, session, middleware]
vucp:
  stage_triggers: [implement, review]
  load_policy: suggested
  confidence: high
  last_reviewed: 2026-06-27
---

# Auth Flow

## Strategy

<!-- Fill this in based on your actual auth implementation -->
<!-- Example: JWT access token (15min) + httpOnly refresh token (7 days) -->

## Session Access

```typescript
// Server Components & API Routes
import { getSession } from "@/server/auth"

const session = await getSession()
if (!session) redirect("/login")
const { user } = session
```

## Middleware Guard

```typescript
// middleware.ts
export function middleware(request: NextRequest) {
  const token = request.cookies.get("session")?.value
  if (!token && isProtectedRoute(request.nextUrl.pathname)) {
    return NextResponse.redirect(new URL("/login", request.url))
  }
  return NextResponse.next()
}

export const config = {
  matcher: ["/dashboard/:path*", "/api/protected/:path*"],
}
```

## Auth Rules

<!-- Project-specific rules Claude must respect -->
<!--
- Never check auth inside a Server Component — middleware handles it
- Never pass raw user ID from client to API — always get from session server-side
- Never store sensitive data in JWT payload — only userId and role
-->
