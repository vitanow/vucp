---
stage: "drafting"
type: "synthesis"
version: "1.0"
agent: "writer"
review_required: true
risk_level: "medium"
---

# Stage Contract: Drafting

## Purpose
Turn approved research findings into a coherent draft.

## Required Root Context
- `/CURRENT.md`
- `/SAFEGUARDS.md`
- `/_knowledge/index.md`
- `/_knowledge/brand/voice.md`
- `/_delta/ERRORS.md`

## Inputs
- `input/findings.md`

## Allowed Actions
- Read approved findings.
- Produce `output/draft.md`.
- Propose knowledge updates in `/_proposals/knowledge_updates/`.

## Forbidden Actions
- Modify `_knowledge/` directly.
- Publish final output without review.

## Outputs
- `output/draft.md`
