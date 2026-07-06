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
Audit the draft for correctness, completeness, safety, and alignment.

## Required Root Context
- `/CURRENT.md`
- `/SAFEGUARDS.md`
- `/SCHEMA.md`
- `/_knowledge/index.md`
- `/_knowledge/policies/safety.md`
- `/_delta/ERRORS.md`

## Inputs
- `input/draft.md`

## Allowed Actions
- Review draft.
- Produce `output/review_log.md`.

## Forbidden Actions
- Silently approve incomplete or unsafe output.
- Delete prior run records.

## Outputs
- `output/review_log.md`
