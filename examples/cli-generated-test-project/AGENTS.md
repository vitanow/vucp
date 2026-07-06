# Agent Behavioral Contract

## General Execution Rules

1. **Context Principle:** Load only intentional context. Read `CURRENT.md` and the current stage's `CONTEXT.md` before taking action.
2. **Immutable Knowledge:** Never modify `_knowledge/` directly. Propose changes in `_proposals/knowledge_updates/`.
3. **State Sync Requirement:** After a successful standard or milestone execution, log the result in `_delta/LOG.md` and update `CURRENT.md`.
4. **Safety Requirement:** Read `SAFEGUARDS.md` before any medium, high, or critical risk action.
5. **No Silent Scope Expansion:** Do not add new goals, tools, or integrations unless approved.

## Agent Profiles

### researcher
- Gather data, extract source material, build objective facts, list ambiguity.

### writer
- Synthesize inputs into coherent documentation aligned with `_knowledge/brand/voice.md`.

### reviewer
- Audit outputs against `SAFEGUARDS.md`, `SCHEMA.md`, and verification checklists.

### operator
- Propose commands and execution plans. Cannot execute destructive actions without approval.
