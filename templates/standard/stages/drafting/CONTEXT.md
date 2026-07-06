---
stage: "drafting"
type: "synthesis"
version: "1.0"
agent: "writer"
review_required: true
risk_level: "medium"
---

# Stage Contract: Drafting

## 1. Purpose

Turn approved research findings into a coherent draft.

## 2. Required Root Context

- `/CURRENT.md`
- `/SAFEGUARDS.md`
- `/_knowledge/index.md`
- `/_knowledge/brand/voice.md`
- `/_delta/ERRORS.md`

## 3. Inputs

Expected input files:

- `input/findings.md`

## 4. Allowed Actions

- Read approved findings.
- Produce `output/draft.md`.
- Propose knowledge updates in `/_proposals/knowledge_updates/`.

## 5. Forbidden Actions

- Modify `_knowledge/` directly.
- Publish final output without review.
- Ignore open uncertainties from research.

## 6. Process

1. Read required context.
2. Read approved findings.
3. Synthesize into a clear draft.
4. Preserve uncertainty where needed.
5. Prepare for review.

## 7. Outputs

- `output/draft.md`

## 8. Verification

Before completion:

- Confirm draft uses findings.
- Confirm assumptions are visible.
- Confirm voice rules were followed.
- Confirm no direct `_knowledge/` mutation occurred.

## 9. Review Gate

Human review required before moving to review/finalization.

## 10. Delta Update

After approval, append summary to `/_delta/LOG.md`.
