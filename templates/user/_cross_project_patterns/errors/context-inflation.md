---
type: cross_project_pattern
status: confirmed
confidence: 0.86
evidence_count: 3
source_projects:
  - vucp-core
  - vucp-cli
  - hermes-memory-review
applies_to:
  - ai-workflows
  - agent-context
  - documentation
  - project-memory
does_not_apply_to:
  - tiny-one-off-task
tags:
  - context
  - tokens
  - agent-quality
last_verified: 2026-06-27
---

# Context Inflation

## Pattern

More context is not always better.

Agents should load intentional, stage-relevant context instead of scanning the whole repository or all prior projects.

## Symptoms

- answers become generic;
- agent mixes unrelated projects;
- token cost increases;
- old constraints override current instructions;
- false analogies appear.

## Resolution

Use:

- `.vucpignore`;
- `_knowledge/index.md`;
- stage-specific `CONTEXT.md`;
- selected cross-project patterns only;
- max 3–5 cross-project patterns per Full Startup.
