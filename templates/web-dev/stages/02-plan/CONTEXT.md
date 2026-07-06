---
stage: "plan"
type: "synthesis"
version: "1.0"
agent: "architect"
review_required: true
risk_level: "low"
---

# Stage Contract: Plan

## Purpose

Produce a clear implementation plan before any code is written.
Human must approve the plan before implementation begins.

## Required Reading

- `/_knowledge/architecture/system-overview.md`
- `/_knowledge/architecture/api-contracts.md`
- `/_knowledge/patterns/component-structure.md`
- `/_knowledge/decisions/` (all files)
- `input/session-brief.md` (from context-load stage)

## Process

1. Read all required files.
2. Produce `output/implementation-plan.md` containing:
   - Feature summary (one paragraph)
   - Files to create (with purpose)
   - Files to modify (with what changes and why)
   - New dependencies needed (if any)
   - DB changes needed (if any — flag as HIGH RISK)
   - Edge cases to handle
   - What is explicitly OUT of scope
3. Present plan to human for approval.
4. Do not proceed to implement until `review_required` gate is passed.

## Outputs

- `output/implementation-plan.md`

## Forbidden

- Do not write implementation code in this stage
- Do not suggest changing tech stack components without flagging as a major decision
- Do not include "nice to have" items — scope to the current feature only
