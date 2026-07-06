---
stage: "deploy-prep"
type: "delivery"
version: "1.0"
agent: "operator"
review_required: true
risk_level: "high"
---

# Stage Contract: Deploy Prep

## Purpose

Prepare a safe deployment plan. Human must explicitly approve before any production action.

## Required Reading

- `/_knowledge/architecture/infra.md`
- `/_knowledge/reference/env-variables.md`
- `/SAFEGUARDS.md`
- `input/code-changes.md`
- `input/review-log.md`

## Process

1. Assess deployment complexity: are there DB migrations? New env vars? Service changes?
2. Produce `output/deploy-checklist.md` with:
   - Pre-deploy steps (migrations, env var additions, cache invalidation)
   - Deploy command / process
   - Post-deploy verification steps
   - Monitoring checks (error rate, key endpoints)
3. Produce `output/rollback-plan.md` with:
   - How to detect a bad deploy
   - Step-by-step rollback procedure
   - Data recovery steps if migration was run

## Outputs

- `output/deploy-checklist.md`
- `output/rollback-plan.md`

## Forbidden

- Do not run any production commands
- Do not suggest skipping the rollback plan for "simple" deploys
- Do not approve your own checklist — human must review and confirm
