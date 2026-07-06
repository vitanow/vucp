---
protocol: VUCP
version: "0.4.1"
project: "<PROJECT_NAME>"
owner: "<OWNER_NAME>"
language: "en"
created: "2026-06-27"
status: active
user_context: "software"
user_profile: "~/.vucp-user/USER_CORE.md"
cross_project_patterns: "~/.vucp-user/_cross_project_patterns/index.md"
cross_project_pattern_policy: "selective"
max_cross_project_patterns: 5
---

# Workspace Identity & Boundaries

## Purpose

<!-- One sentence: what does this product do and for whom? -->
<!-- Example: A SaaS platform that helps freelancers track client invoices and payments. -->

## Tech Stack

```yaml
frontend:
  framework: "<Next.js 14 | Nuxt 3 | SvelteKit | React + Vite>"
  language: "<TypeScript | JavaScript>"
  styling: "<Tailwind CSS | shadcn/ui | CSS Modules>"
  state: "<Zustand | Jotai | Redux Toolkit | React Query>"

backend:
  runtime: "<Node.js | Python | PHP>"
  framework: "<Next.js API Routes | Express | FastAPI | Laravel>"
  orm: "<Prisma | Drizzle | SQLAlchemy | Eloquent>"
  database: "<PostgreSQL | MySQL | SQLite | MongoDB>"
  cache: "<Redis | Upstash | none>"

auth:
  provider: "<NextAuth.js | Clerk | Auth.js | Supabase Auth | custom JWT>"
  strategy: "<JWT + refresh | session | OAuth>"

infra:
  hosting: "<Vercel | Railway | Fly.io | VPS | AWS>"
  ci_cd: "<GitHub Actions | none>"
  storage: "<S3 | Cloudflare R2 | Supabase Storage | none>"
  email: "<Resend | SendGrid | Postmark | none>"
  payments: "<Stripe | LemonSqueezy | none>"
```

## Repository Structure

```
<!-- Paste your actual repo tree here after setup -->
<!-- Example:
src/
  app/           ← Next.js App Router pages
  components/    ← Shared UI components
  lib/           ← Utilities, helpers
  server/        ← Server-only code
  types/         ← Shared TypeScript types
prisma/
  schema.prisma
public/
```

## Coding Conventions

```yaml
components: "<Server Components by default | Client only when needed>"
naming: "<PascalCase for components, camelCase for functions, kebab-case for files>"
imports: "<absolute @ alias | relative>"
error_handling: "<try/catch + Result type | throw and catch at boundary>"
api_style: "<REST | tRPC | GraphQL>"
validation: "<Zod | Yup | none>"
testing: "<Vitest | Jest | Playwright | none>"
```

## Architectural Patterns

```yaml
data_access: "<repository pattern | direct ORM | service layer>"
auth_guard: "<middleware | layout | per-page>"
file_structure: "<feature-based | layer-based>"
env_management: "<t3-env | dotenv | manual>"
```

## Scope

<!-- What is explicitly part of this project -->

## Out of Scope

<!-- What Claude should never touch or suggest -->
<!-- Example: "Do not suggest changing the database from PostgreSQL to anything else." -->


## Context Loading Order

For Full Startup, load context in this order:

1. Private `USER_CORE.md`, if available through `user_profile`.
2. Matching `_user_contexts/<domain>.md`, if available through `user_context`.
3. `WORKSPACE.md`.
4. `CURRENT.md`.
5. `_delta/ERRORS.md`.
6. Current stage `CONTEXT.md`.
7. `SAFEGUARDS.md` when risk is medium, high, or critical.


## Cross-Project Pattern Policy

Cross-project patterns are optional and selective.

During Full Startup, agents may read the configured cross-project pattern index and load at most `max_cross_project_patterns` confirmed patterns that match the current domain, stage, risk profile, or task.

Rules:

- Do not load entire previous projects.
- Do not load candidate patterns unless explicitly requested.
- Do not apply a pattern if `does_not_apply_to` matches the current task.
- Cross-project patterns are advisory and must not override `SAFEGUARDS.md`, `CONTEXT.md`, or direct human instruction.
