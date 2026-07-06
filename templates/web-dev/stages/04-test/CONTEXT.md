---
stage: "test"
type: "verification"
version: "1.0"
agent: "developer"
review_required: true
risk_level: "medium"
---

# Stage Contract: Test

## Purpose

Write and verify tests for the implemented feature.

## Required Reading

- `input/code-changes.md` (from implement stage)
- `/_knowledge/patterns/testing-patterns.md`
- `/_knowledge/patterns/error-handling.md`

## Process

1. For each new function or component, write at least one unit test.
2. Cover the happy path AND at least one error/edge case per function.
3. Run tests locally and confirm they pass.
4. Produce `output/test-results.md` with:
   - List of tests written
   - Test results (pass/fail)
   - Coverage summary (if available)
   - Any untested areas and why

## Outputs

- `output/test-results.md`

## Forbidden

- Do not mock the real database in integration tests — use test DB or testcontainers
- Do not skip tests for "simple" functions — simple functions fail too
- Do not mark tests as passing if they haven't been run
