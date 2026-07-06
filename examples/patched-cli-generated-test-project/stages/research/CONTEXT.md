---
stage: "research"
type: "research"
version: "1.0"
agent: "researcher"
review_required: true
risk_level: "low"
---

# Stage Contract: Research

## Purpose
Collect and organize raw materials from `_inbox/` into `output/findings.md`.

## Required Root Context
- `/CURRENT.md`
- `/_knowledge/index.md`
- `/_delta/ERRORS.md`

## Inputs
- `input/`
- `/_inbox/`

## Allowed Actions
- Scan `_inbox/` and `input/`.
- Produce `output/findings.md`.

## Forbidden Actions
- Touch code files outside this stage folder.
- Execute network calls without explicit task allocation.

## Outputs
- `output/findings.md`
