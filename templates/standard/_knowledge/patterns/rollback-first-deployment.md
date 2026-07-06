---
type: knowledge
title: "Rollback-first deployment"
description: "Always define the rollback plan before executing any deployment."
status: confirmed
confidence: 0.92
evidence_count: 6
semantic_aliases:
  - "safe deployment"
  - "undo plan"
  - "revert strategy"
  - "production safety"
  - "before changing live systems"
  - "how to undo a deploy"
  - "what if deploy fails"
tags:
  - deployment
  - rollback
  - safety
  - operations
vucp:
  stage_triggers: [deploy-prep, review]
  load_policy: required
cross_references:
  - "_delta/ERRORS.md"
  - "SAFEGUARDS.md"
  - "~/.vucp-user/_cross_project_patterns/architecture/rollback-first-deployment.md"
---

# Rollback-First Deployment

## Rule

Before executing any deployment, define the rollback plan.
Not after. Not during. Before.

A deployment without a rollback plan is a bet.
A deployment with a rollback plan is a procedure.

## What a Rollback Plan Contains

1. **Trigger condition** — what observable symptom means "roll back now"
2. **Rollback command** — the exact command or steps to reverse the deploy
3. **Data consideration** — if a migration ran, can it be reversed?
4. **Communication** — who to notify and when
5. **Time limit** — how long to attempt recovery before rolling back

## Minimum Acceptable Rollback Plan

```markdown
## Rollback Plan

**Trigger:** Error rate > 5% for 5 minutes, or any payment failure

**Steps:**
1. Vercel Dashboard → Deployments → select previous → Promote to Production
2. Verify: [key endpoint] returns 200
3. Notify: [channel]

**If DB migration ran:**
- Assess: is the migration reversible?
- If yes: run `prisma migrate resolve --rolled-back <migration>`
- If no: escalate before reverting code
```

## What Claude Must Never Do

- Do not propose a deployment step without asking for the rollback plan first
- Do not say "we can roll back if needed" without specifying how
- Do not mark a deploy stage as complete without rollback plan in outputs

## Evidence

Pattern confirmed across: API releases, frontend deploys,
database migrations, infrastructure changes.
Cost of skipping: 2+ hour incidents that would have been
5-minute rollbacks with a plan in place.
