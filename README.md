# VUCP — Vitanow Unified Context Protocol

**A portable AI workspace format for inspectable, repeatable, and safer human-AI work.**

Created by **Zahari Georgiev Vitanov / Vitanow OPS**.

VUCP turns a normal project folder into a structured AI workspace with visible state, safeguards, review gates, run traces, semantic hints, cross-project patterns, and assisted autopilot.

```text
MCP connects agents to tools.
AGENTS.md tells agents what to do.
Memory systems remember facts.
VUCP makes the project workflow visible, repeatable, portable, and reviewable.
```

## Status

```text
Release:        0.5.0a10 (0.5-alpha-9.2)
Core protocol:  0.4.1
CLI:            init, lint, graph, doctor, export, dream, patterns, autopilot
License:        MIT
Creator:        Zahari Georgiev Vitanov / Vitanow OPS
```

## Who VUCP is for

VUCP is for people and teams already using AI agents, but tired of losing context between sessions.

Use VUCP if:

- you use Codex, Claude Code, Cursor, Windsurf, Gemini CLI, or other AI coding agents;
- you keep re-explaining the same project to AI;
- your agents repeat the same mistakes;
- your `AGENTS.md`, `CLAUDE.md`, or rules files are getting too long;
- you want one source of truth that can export to agent-specific instruction files;
- you need visible state, review gates, rollback-aware workflows, and run traces;
- you want reusable cross-project lessons without dumping every old project into context;
- you want AI to surface only what needs human attention.

## What VUCP gives you

```text
CURRENT.md        → what is happening now
WORKSPACE.md      → what this project is
AGENTS.md         → how agents should behave
AUTOPILOT.md      → how much autonomy is allowed
_attention/       → human attention dashboard
_delta/           → errors, learnings, logs, autopilot audit
_runs/            → traceable execution records
stages/           → structured workflow
_knowledge/       → durable project knowledge and semantic aliases
.vucpignore       → what agents should ignore
```

## Assisted Autopilot

VUCP includes **Assisted Autopilot**: human attention only when it matters.

Modes:

```text
SILENT   → agent works quietly but still interrupts for critical/forbidden actions
SURFACE  → agent works, then surfaces a short attention list; recommended default
GUIDED   → agent asks before each significant step
```

The human-facing dashboard is:

```text
_attention/ATTENTION.md
```

Autopilot is not blind autonomy, but it is also not a security boundary. Autopilot is policy, not enforcement. AUTOPILOT.md and the modes tell an agent when to stop and ask; they do not technically block anything. Whether a high-risk, destructive, production, credential, publishing, or trusted-memory action is actually stopped depends on your agent runtime and its settings (for example Claude Code hooks and permissions, Cursor agent settings, or the Codex sandbox and approval mode). Configure those for real limits.

## Lite mode

Start with 3 files instead of the full layout:

```bash
python cli/vucp_cli_mvp.py init my-project --lite
```

- `AGENTS.md`: how agents behave and when to stop and ask (instructions, not enforcement)
- `CURRENT.md`: goal, state, next step, what needs human attention
- `LEARNINGS.md`: errors and lessons, append-only

The template is about 470 tokens. lint, doctor and export understand Lite
workspaces; `vucp upgrade` moves to full mode without overwriting anything.
See `docs/LITE.md`.

## AI-guided setup

VUCP includes an AI-facing onboarding guide:

```text
VUCP_SETUP_GUIDE.ai.md
```

Paste it into Codex, Claude Code, Cursor, Windsurf, ChatGPT, or another assistant and ask it to guide you step by step.

## Quick start

Install the `vucp` command (Python 3.9+), or run the script directly:

```bash
pipx install .        # or: uv tool install .
vucp --help
```


```bash
python cli/vucp_cli_mvp.py init my-project --project "My Project" --owner "Zahari Vitanov"
python cli/vucp_cli_mvp.py lint my-project
python cli/vucp_cli_mvp.py doctor my-project
python cli/vucp_cli_mvp.py autopilot status my-project
python cli/vucp_cli_mvp.py graph my-project
```

Export agent instructions:

```bash
python cli/vucp_cli_mvp.py export claude-md my-project
python cli/vucp_cli_mvp.py export agents-md my-project
```

Use memory maintenance and cross-project patterns:

```bash
python cli/vucp_cli_mvp.py dream my-project --write
python cli/vucp_cli_mvp.py patterns my-project --patterns templates/user/_cross_project_patterns --tags cli,safety
```

`patterns --tags` semantics: multiple tags use OR (a pattern matches if any tag matches its `tags`, `applies_to` or `source_projects`); matching is case-insensitive and whitespace-trimmed; empty entries are ignored. `does_not_apply_to` wins: if any given tag appears in a pattern's `does_not_apply_to`, the pattern is excluded even when other tags match. Results are ranked by number of matched tags, then by confirmed status and confidence. No match returns 0 patterns. `--tags ""` means no tag filter; omitting `--tags` uses `user_context` from `WORKSPACE.md`.

Change Autopilot mode:

```bash
python cli/vucp_cli_mvp.py autopilot set my-project --mode SURFACE
python cli/vucp_cli_mvp.py autopilot audit my-project --json
```

## Semantic aliases and manual graph links

VUCP stays portable and plain-text, but supports lightweight semantic discovery:

```yaml
semantic_aliases:
  - "alternate wording"
  - "meaning-based search phrase"

cross_references:
  - "_delta/ERRORS.md#related-error"
  - "_knowledge/patterns/related-pattern.md"
```

This complements semantic memory systems such as Cognee, Mem0, Zep, and Letta without requiring a database.

## Repository map

```text
cli/                         Reference CLI
spec/                        Normative spec (VUCP_SPEC_v0.4.1_FINAL.md); archive/ is superseded
schemas/                     Optional schemas, when present
templates/standard/          General VUCP workspace template
templates/web-dev/           Web development template
templates/user/              Private user context and cross-project pattern templates
docs/                        Positioning, onboarding, Autopilot, adapters, Lite
demo-research-to-brief/      Demo workflow
products/                    Productized kits and examples
```

## Positioning

VUCP is not another agent.

VUCP is not another memory database.

VUCP is not a replacement for MCP.

VUCP is the project-side workspace layer for human-AI work.

## Creator

Created by **Zahari Georgiev Vitanov / Vitanow OPS**.

See:

```text
docs/ABOUT_CREATOR.md
AUTHORS.md
CITATION.cff
```
