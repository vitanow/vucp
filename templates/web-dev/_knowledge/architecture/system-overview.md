---
type: architecture
title: System Overview
description: High-level architecture of the project — how the pieces connect.
tags: [architecture, overview, system-design]
vucp:
  stage_triggers: [context-load, plan, review]
  load_policy: required
  confidence: high
  last_reviewed: 2026-06-27
---

# System Overview

## Architecture Style

<!-- Example: Monolithic Next.js app with App Router, PostgreSQL via Prisma, deployed on Vercel -->

## Request Flow

```
<!-- Describe how a typical request flows through the system -->
<!-- Example:
Browser → Next.js Edge Middleware (auth check)
       → App Router Page (server component)
       → Server Action / API Route
       → Prisma ORM
       → PostgreSQL (Supabase)
       → Response
-->
```

## Key Boundaries

<!-- What are the hard boundaries in the system? -->
<!-- Example:
- All DB access goes through /src/server/db/ — never import Prisma directly in components
- Client components never access the DB — always via Server Actions or API routes
- Auth checks happen at middleware level — do not duplicate in pages
-->

## External Services

<!-- List all third-party services and what they do -->
<!--
| Service | Purpose | SDK |
|---|---|---|
| Supabase | PostgreSQL + Auth | @supabase/supabase-js |
| Stripe | Payments | stripe |
| Resend | Transactional email | resend |
| Cloudflare R2 | File storage | AWS S3 SDK |
-->

## Deployment Architecture

<!-- How is this deployed? What environments exist? -->
<!--
- Production: Vercel (auto-deploy from main)
- Preview: Vercel Preview (auto-deploy from PRs)
- Local: Docker Compose (postgres + redis)
-->
