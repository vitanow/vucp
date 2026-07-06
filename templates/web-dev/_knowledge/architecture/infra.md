---
type: architecture
title: Infrastructure
description: Deployment setup, environments, CI/CD, and operations runbook.
tags: [infrastructure, deployment, devops, ci-cd]
vucp:
  stage_triggers: [deploy-prep]
  load_policy: required
  confidence: high
  last_reviewed: 2026-06-27
---

# Infrastructure

## Environments

| Environment | URL | Branch | Deploy Trigger |
|---|---|---|---|
| Production | <!-- https://app.example.com --> | main | Push to main |
| Preview | <!-- Vercel preview URL --> | any PR | PR opened/updated |
| Local | localhost:3000 | any | manual |

## Environment Variables

See `_knowledge/reference/env-variables.md` for full list.

**Critical:** Never commit `.env.production`. All secrets via hosting provider dashboard.

## Deployment Process

```bash
# Standard deploy (via CI)
git push origin main   # triggers automatic Vercel deploy

# Manual deploy (emergency)
vercel --prod          # requires Vercel CLI and auth
```

## Database Migrations (Production)

```bash
# ALWAYS run in this order:
# 1. Deploy code first (backward-compatible schema)
# 2. Run migration AFTER deploy succeeds
# 3. Verify production, then clean up old compatibility code

npx prisma migrate deploy   # production only — uses DATABASE_URL
```

## Rollback Plan

<!-- How to roll back a bad deploy -->
<!--
1. Vercel Dashboard → Deployments → select previous → Promote to Production
2. If DB migration already ran: assess damage before reverting schema
3. Contact: <who to call>
-->
