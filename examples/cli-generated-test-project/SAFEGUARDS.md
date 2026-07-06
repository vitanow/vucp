# System Safeguards

## Core Directive

Preserve intentional operational safety. No AI agent is permitted to execute irreversible or destructive tasks without human approval in a review gate.

## Never Mutate Without Human Gate Approval

- Credentials, env files, and API configurations.
- Production database schemas or live code deployments.
- Erasure of historical run state in `_runs/`.
- Security, payment, user data, or infrastructure settings.

## Risk Classification Architecture

- **LOW:** Documentation, ideation, analysis inside isolated text folders.
- **MEDIUM:** Code synthesis, script changes with local tests, or structural rewrites.
- **HIGH:** Production-adjacent infrastructure, public releases, system integrations.
- **CRITICAL:** Credentials, destructive actions, payment systems, live databases, security policy.

## Required Before High/Critical Actions

- Risk level.
- Files changed.
- Commands proposed.
- Verification steps.
- Rollback plan.
- Human approval checkpoint.
