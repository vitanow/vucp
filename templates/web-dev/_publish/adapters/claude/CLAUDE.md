# CLAUDE.md

Generated for Claude Code from VUCP workspace.

## What this is

This file is generated from VUCP. Do not edit this generated file as source of truth.
Edit the VUCP files instead: `WORKSPACE.md`, `CURRENT.md`, `AGENTS.md`, `SAFEGUARDS.md`, stage `CONTEXT.md` files, and `_knowledge/`.

## Current State

# Current Operational State

## Status

active

## Active Feature

<!-- What are you building right now? -->
<!-- Example: User authentication — JWT login + refresh token rotation -->

## Where I Left Off

<!-- The most important sentence for Claude at the start of a new session. -->
<!-- Example: Middleware written, but refresh endpoint returns 401 on valid token. -->
<!-- Suspected cause: token expiry check uses UTC but DB stores local time. -->

## Files Changed Last Session

<!-- List the files touched. Claude will focus here first. -->
<!--
- src/middleware/auth.ts
- src/app/api/auth/refresh/route.ts
- prisma/schema.prisma (added refreshToken model)
-->

## Open Blockers

<!-- What is stopping progress? -->
<!-- Example: Need to decide: store refresh tokens in DB or Redis? -->

## Do Not Touch

<!-- Hard constraints for Claude this session -->
<!-- Example:
- Do not run prisma migrate — schema changes need review first
- Do not change the auth provider — Clerk is locked in
- Do not refactor the component structure — scope creep risk
-->

## Next Action

<!-- The single most important thing to do next -->
<!-- Example: Debug the 401 — add logging to refresh route and trace token validation -->

## Last Updated

2026-06-27


## Workspace

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


## Agent Instructions

# Agent Behavioral Contract

## Session Startup

VUCP uses two startup modes. Choose based on the nature of the request.

### Light Startup
*For simple questions, status checks, or clarifications.*

1. Read `CURRENT.md`
2. Answer the question
3. If the answer touches files, decisions, or code — escalate to Full Startup

### Full Startup
*For any task that produces output, modifies files, writes code, or makes decisions.*

Load in this exact order before writing a single line of output:

1. `USER_CORE.md` — owner identity and working preferences
2. `_user_contexts/software.md` — software domain behavior
3. `WORKSPACE.md` — project identity, tech stack, conventions
4. `CURRENT.md` — active task, blockers, do-not-touch
5. `_delta/ERRORS.md` — past failures relevant to today's task
6. Current stage `CONTEXT.md` — this session's specific contract
7. `SAFEGUARDS.md` — if risk level is medium or higher

After Full Startup, confirm in the first message:
- Active task
- Any ERRORS.md entries relevant to today
- Proposed first action

---

## Execution Rules

1. **Load context first.** Always read `CURRENT.md`, `WORKSPACE.md`, and `_delta/ERRORS.md`
   before writing any code. The first message of every session must reference what you found.

2. **Check ERRORS.md.** If a past error is relevant to the current task, say so explicitly
   before proceeding. Do not silently repeat documented mistakes.

3. **Respect the tech stack.** Never suggest replacing a core technology listed in `WORKSPACE.md`
   unless the human explicitly asks for alternatives.

4. **Never mutate knowledge directly.** If you discover something worth remembering
   (a pattern, a fix, an architectural decision), propose it in `_proposals/knowledge_updates/`.
   Do not edit `_knowledge/` files during a session.

5. **State sync after session.** At the end of a session or after a meaningful milestone,
   suggest updates to `CURRENT.md` and `_delta/LOG.md`. Do not do it silently — confirm first.

6. **Forbidden without explicit approval:**
   - Running `prisma migrate` or any destructive DB command
   - Changing auth strategy or provider
   - Modifying `.env` files or secrets
   - Pushing to main/production branch
   - Installing new major dependencies without discussion

## Agent Profiles

### architect
- Designs system structure, data models, API contracts
- Produces: `_knowledge/architecture/` updates, ADR files, schema proposals
- Does not write implementation code

### developer
- Implements features based on approved plans
- Reads: current stage CONTEXT.md, `_knowledge/patterns/`, `_delta/ERRORS.md`
- Produces: working code, updated tests

### debugger
- Diagnoses errors and regressions
- Reads: error output, relevant files from `_knowledge/`, `_delta/ERRORS.md`
- Produces: root cause analysis, minimal fix, ERRORS.md update proposal

### reviewer
- Reviews code for correctness, security, and alignment with conventions
- Reads: `WORKSPACE.md` conventions, `_knowledge/patterns/`, `SAFEGUARDS.md`
- Produces: review notes, approval or rejection with specific feedback

### operator
- Plans deployment and infrastructure changes
- Reads: `SAFEGUARDS.md`, `_knowledge/architecture/infra.md`
- Produces: step-by-step plan with rollback — never executes without approval


## Safety Rule

After repeated runs, the agent may suggest a Dream Pass.

Human approval is required before promotion, deprecation, deletion, or trusted knowledge changes.


## Safeguards

# System Safeguards

## Core Directive

No AI agent may execute irreversible or production-affecting actions without explicit human approval.

## Absolute Prohibitions (Never Without Explicit Approval)

- Run `prisma migrate`, `drizzle-kit push`, or any schema migration in production
- Deploy to production environment
- Modify `.env`, `.env.production`, or any secrets file
- Delete database records or tables
- Change authentication provider or strategy
- Install major new dependencies that change the architectural direction
- Push directly to `main` or `production` branch
- Modify payment processing code (Stripe webhooks, pricing, checkout)

## Risk Classification

**LOW** — Safe to proceed without extra confirmation
- Reading files, analyzing code, explaining concepts
- Writing new components in isolated feature folder
- Adding types, interfaces, utility functions
- Writing tests for existing code

**MEDIUM** — Confirm before proceeding, propose rollback
- Modifying existing components or API routes
- Adding new database queries
- Changing state management logic
- Updating dependencies (minor versions)

**HIGH** — Full plan required + human approval
- Schema changes (even dev)
- Auth flow modifications
- New external API integrations
- Infrastructure configuration changes
- Updating major dependencies

**CRITICAL** — Operator agent only + written rollback plan required
- Production deployments
- Database migrations in production
- Credential rotation
- Payment system changes
- Security policy changes

## Required Before HIGH/CRITICAL Actions

1. List of all files that will change
2. Exact commands to be run
3. What could go wrong
4. Step-by-step rollback plan
5. Explicit human: "approved"


## VUCP Rule

When instructions conflict, prefer this order:

1. explicit human instruction;
2. `SAFEGUARDS.md`;
3. current stage `CONTEXT.md`;
4. `CURRENT.md`;
5. `WORKSPACE.md`;
6. cross-project patterns only when relevant.
