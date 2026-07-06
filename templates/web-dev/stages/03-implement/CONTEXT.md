---
stage: "implement"
type: "implementation"
version: "1.0"
agent: "developer"
review_required: true
risk_level: "medium"
---

# Stage Contract: Implement

## Purpose

Write the code for the approved implementation plan.

## Required Reading

- `input/implementation-plan.md` (approved plan from stage 02)
- `/_knowledge/patterns/component-structure.md`
- `/_knowledge/patterns/data-access.md`
- `/_knowledge/patterns/error-handling.md`
- `/_delta/ERRORS.md`
- `/SAFEGUARDS.md` (check risk level of each change)

## Process

1. Implement exactly what the approved plan specifies — no more, no less.
2. Follow all patterns in `_knowledge/patterns/`.
3. Before every DB-related change, verify against `_knowledge/architecture/database-schema.md`.
4. Produce `output/code-changes.md` with:
   - Every file created or modified
   - Summary of what changed in each file
   - Any deviations from the plan (flag and explain)
   - Any new questions or blockers discovered
5. Produce `output/files-changed.md` as a simple list of paths.

## Outputs

- `output/code-changes.md`
- `output/files-changed.md`

## Forbidden

- Do not modify files not listed in the approved plan without flagging
- Do not run database migrations
- Do not install new dependencies without flagging in code-changes.md
- Do not commit or push
