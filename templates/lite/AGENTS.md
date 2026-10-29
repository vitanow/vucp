---
vucp_mode: lite
project: "<PROJECT_NAME>"
owner: "<OWNER_NAME>"
autonomy: SURFACE
---
# AGENTS.md - <PROJECT_NAME>

Instructions for AI agents working in this project. These are instructions,
not enforcement: nothing here technically blocks an action. For real limits,
use your tool's permission settings (sandbox, allow/deny lists, hooks).

## Start of every session

1. Read `CURRENT.md` (state and next step).
2. Skim `LEARNINGS.md` before repeating a similar task.
3. Do not load other files unless the task needs them.

## How to work

- Keep changes small and reversible. Explain what you changed and why.
- Ask when the goal is ambiguous instead of guessing.
- Do not invent facts, sources, or test results.

## Autonomy: SURFACE

Work without asking for routine, reversible steps. Stop and ask first for:

- deleting or overwriting data, irreversible changes;
- production, deploys, payments, publishing, sending messages;
- credentials, secrets, permissions;
- editing this file.

Other modes: GUIDED (ask before each significant step),
SILENT (only stop for the list above).

## End of every session

- Update `CURRENT.md`: what changed, next step, anything needing the human.
- Append to `LEARNINGS.md` if you hit an error or learned something reusable.
