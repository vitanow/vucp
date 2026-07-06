# Competitive Positioning

VUCP should not compete with MCP, AGENTS.md, Claude Code memory, Codex memory, Cursor rules, Windsurf rules, Mem0, Zep, Letta, or LangGraph.

VUCP sits one layer above them.

```text
MCP connects agents to tools.
AGENTS.md / CLAUDE.md tell agents what to do.
Memory systems remember facts.
VUCP makes the whole project workflow inspectable, repeatable, portable, and reviewable.
```

## Positioning

VUCP is a portable AI workspace format.

It turns a project folder into an inspectable human-AI workspace.

## What VUCP is not

- Not a replacement for MCP.
- Not a memory database.
- Not another hidden agent runtime.
- Not just a larger `AGENTS.md` file.

## What VUCP is

- A filesystem-native workspace contract.
- A source-of-truth folder format.
- A reviewable trace of AI-assisted work.
- A way to export structured context to existing tools.
- A way to curate cross-project patterns without dumping old projects into context.

## Key differentiation

1. Visible state: `CURRENT.md`.
2. Reviewable workflow: `stages/*/CONTEXT.md`.
3. Reproducible traces: `_runs/`.
4. Accumulated learning: `_delta/ERRORS.md` and `_delta/LEARNINGS.md`.
5. Tool adapters: `vucp export`.
6. Health checks: `vucp doctor`.
7. Cross-project pattern selection: `vucp patterns`.
8. Manual memory maintenance: `vucp dream`.
