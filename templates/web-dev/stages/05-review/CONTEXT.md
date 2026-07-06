---
stage: "review"
type: "review"
version: "1.0"
agent: "reviewer"
review_required: false
risk_level: "low"
---

# Stage Contract: Review

## Purpose

Final review of the implementation for correctness, security, and alignment with project conventions.

## Required Reading

- `input/code-changes.md`
- `input/test-results.md`
- `/WORKSPACE.md` (conventions section)
- `/_knowledge/patterns/` (all files)
- `/SAFEGUARDS.md`

## Process

1. Review each changed file against the coding conventions in WORKSPACE.md.
2. Check for security issues: exposed secrets, missing auth checks, unvalidated input.
3. Check for pattern violations: client/server boundary, data access patterns, error handling.
4. Produce `output/review-log.md` with:
   - Overall verdict: APPROVED / APPROVED_WITH_CHANGES / REJECTED
   - Specific findings (file + line + issue + severity)
   - Required changes before merge (if any)
   - Suggestions (non-blocking)

## Outputs

- `output/review-log.md`
