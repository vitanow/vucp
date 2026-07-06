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
