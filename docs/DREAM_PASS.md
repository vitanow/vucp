# Dream Pass

Status: recommended manual maintenance ritual.

Dream Pass is a review process for keeping VUCP memory useful.

It is inspired by confidence-scored memory systems where repeated signals become preferences or rules only after evidence accumulates.

## Inputs

- `_delta/ERRORS.md`
- `_delta/LEARNINGS.md`
- `_proposals/knowledge_updates/`
- recent `_runs/`

## Actions

- Promote repeated candidate patterns to confirmed.
- Deprecate stale patterns.
- Remove or archive noise.
- Update confidence and occurrence counts.
- Propose knowledge updates when appropriate.

## Rule

Dream Pass is manual in 0.5-alpha-6.

Agents may propose changes, but humans approve promotion, deprecation, or removal.


## Safety Rule

After repeated runs, the agent may suggest a Dream Pass.

Human approval is required before promotion, deprecation, deletion, or trusted knowledge changes.

## Cross-Project Pattern Promotion

Dream Pass may propose promotion from project-local memory to cross-project pattern.

Promotion path:

```text
_delta/ERRORS.md or _delta/LEARNINGS.md
→ _proposals/knowledge_updates/
→ candidate cross-project pattern
→ confirmed cross-project pattern after repeated evidence
```

Rules:

- Human approval required.
- Remove project-specific secrets, names, credentials, and private client details.
- Add `applies_to` and `does_not_apply_to`.
- Add `source_projects` and `evidence_count`.
- Do not promote one-off observations as confirmed patterns.
