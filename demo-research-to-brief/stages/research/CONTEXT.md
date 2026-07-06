---
stage: "research"
type: "research"
version: "1.0"
agent: "researcher"
review_required: true
risk_level: "low"
---

# Stage Contract: Research

## 1. Purpose

Collect and organize raw materials from `_inbox/` into a structured `findings.md` artifact.

## 2. Required Root Context

- `/CURRENT.md`
- `/_knowledge/index.md`
- `/_delta/ERRORS.md`

## 3. Inputs

Expected input sources:

- `input/`
- `/_inbox/`

## 4. Allowed Actions

- Scan `_inbox/` and `input/` data files.
- Produce `output/findings.md`.
- List missing information and assumptions.

## 5. Forbidden Actions

- Touch code files outside this stage folder.
- Execute network calls without explicit task allocation.
- Produce final public-facing copy.

## 6. Process

1. Read required root context.
2. Review available inbox and input files.
3. Extract facts, claims, open questions, and sources.
4. Write structured findings.
5. Mark uncertainties clearly.

## 7. Outputs

- `output/findings.md`

## 8. Verification

Before completion:

- Confirm all relevant inputs were considered.
- Confirm uncertainties are listed.
- Confirm no forbidden action was taken.

## 9. Review Gate

Human review required before moving to drafting.

## 10. Delta Update

After approval, append summary to `/_delta/LOG.md`.
