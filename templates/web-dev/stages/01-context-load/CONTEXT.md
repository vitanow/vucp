---
stage: "context-load"
type: "research"
version: "1.0"
agent: "developer"
review_required: false
risk_level: "low"
---

# Stage Contract: Context Load

## Purpose

Start every Claude session by loading the full project context.
This stage produces a session-brief that confirms Claude understands
the current state before any code is written.

## Required Reading (in order)

1. `/CURRENT.md` — active feature, where we left off, blockers
2. `/WORKSPACE.md` — tech stack, conventions, patterns
3. `/_delta/ERRORS.md` — past mistakes, do not repeat
4. `/_knowledge/architecture/system-overview.md` — how the system works
5. `/_knowledge/architecture/database-schema.md` — current models

## Process

1. Read all required files above.
2. Write `output/session-brief.md` confirming:
   - What the active feature is
   - Where the last session ended
   - What files are relevant
   - Any ERRORS.md entries relevant to today's work
   - Proposed first action
3. Wait for human confirmation before proceeding to next stage.

## Outputs

- `output/session-brief.md`

## Forbidden

- Do not write any code in this stage
- Do not make assumptions about the codebase not supported by the knowledge files
