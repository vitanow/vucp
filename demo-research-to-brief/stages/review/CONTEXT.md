---
stage: "review"
type: "review"
version: "1.0"
agent: "reviewer"
review_required: false
risk_level: "low"
---

# Stage Contract: Review

## 1. Purpose

Audit the draft for correctness, completeness, safety, and alignment with workspace rules.

## 2. Required Root Context

- `/CURRENT.md`
- `/SAFEGUARDS.md`
- `/SCHEMA.md`
- `/_knowledge/index.md`
- `/_knowledge/policies/safety.md`
- `/_delta/ERRORS.md`

## 3. Inputs

Expected input files:

- `input/draft.md`

## 4. Allowed Actions

- Review draft.
- Produce `output/review_log.md`.
- Mark approval status.
- Suggest corrections.
- Propose learnings/errors updates.

## 5. Forbidden Actions

- Silently approve incomplete or unsafe output.
- Delete prior run records.
- Rewrite project scope.

## 6. Process

1. Read required context.
2. Check draft against safety and schema.
3. Identify gaps, risks, and missing assumptions.
4. Decide review status.
5. Write review log.

## 7. Outputs

- `output/review_log.md`

## 8. Verification

Before completion:

- Confirm review status is explicit.
- Confirm risks are listed.
- Confirm next action is clear.

## 9. Review Gate

No additional review gate is required unless risk is high or critical.

## 10. Delta Update

After review, append outcome to `/_delta/LOG.md`.
