# Workspace Schema and Naming Contracts

## File Naming Standards

- Root control files: UPPERCASE (`START.md`, `CURRENT.md`, `AGENTS.md`, etc.)
- System folders: underscore prefix (`_knowledge/`, `_delta/`, `_runs/`, etc.)
- Stage folders: named by function (`research/`, `drafting/`) or numbered (`01-research/`)
- Knowledge files: kebab-case (`system-overview.md`, `api-contracts.md`)
- User context files: domain id, kebab-case (`software.md`, `physics.md`)

## Workspace Status Values

`active` | `paused` | `completed` | `blocked`

## Review Gate Decision Values

`pending` | `approved` | `approved_with_changes` | `rejected` | `blocked`

## Risk Level Values

`low` | `medium` | `high` | `critical`

## Run Classification Values

`transient` — not logged to `_runs/` or `_delta/`
`standard`  — logged to `_runs/` with RUN.md and knowledge.lock.yaml
`milestone` — logged with full knowledge snapshot

## Knowledge File Types (`type` field in frontmatter)

`architecture` | `pattern` | `decision` | `policy` | `api` | `reference` | `playbook`

## Learning and Error Status Values

`candidate`   — observed once, not yet validated
`confirmed`   — validated 3+ times across independent runs
`resolved`    — error fixed and not recurred in 3+ runs
`deprecated`  — learning no longer applies

## Confidence Score Convention

`0.0–0.39` — weak signal, observe only
`0.40–0.69` — emerging pattern, apply with caution
`0.70–0.89` — strong pattern, apply by default
`0.90–1.0`  — treat as a rule; flag explicitly if violated

## User Context Types (`type: user-context` domain values)

`software` | `physics` | `business` | `creative` | `personal`

## VUCP File Types

`user-core`    — `USER_CORE.md`, always loaded
`user-context` — `_user_contexts/<domain>.md`, loaded per project
`workspace`    — `WORKSPACE.md`, project identity
`stage`        — `CONTEXT.md` inside a stage folder
`knowledge`    — any file inside `_knowledge/`
`run`          — `RUN.md` inside `_runs/`

## Memory Layer Clarity

Each memory layer answers a different question. When in doubt about where to write something, use this table:

| Where | Answers | Scope | Written by |
|---|---|---|---|
| `USER_CORE.md` | Who am I and how do I work? | Global, all projects | Human |
| `_user_contexts/<domain>.md` | How do I work in this domain? | Domain-wide | Human |
| `WORKSPACE.md` | What is this project? | This project | Human |
| `CURRENT.md` | What is happening right now? | This session | Human + Agent |
| `_delta/ERRORS.md` | What has failed in this project? | This project | Agent (proposed) |
| `_delta/LEARNINGS.md` | What patterns emerged in this project? | This project | Agent (proposed) |
| `_knowledge/` | What stable facts does the agent need? | This project | Human + Agent |

**Rule:** If the same insight would appear in more than one layer, it belongs in the most specific one.
A pattern discovered in a physics project goes in that project's `_delta/LEARNINGS.md`, not in `_user_contexts/physics.md`.
It graduates to `_user_contexts/physics.md` only if it applies across all physics projects.

## Cross-Project Pattern Schema

Cross-project patterns are optional v0.5 extension files.

Recommended frontmatter:

```yaml
type: cross_project_pattern
status: candidate|confirmed|deprecated|rejected
confidence: 0.0
evidence_count: 1
source_projects: []
applies_to: []
does_not_apply_to: []
tags: []
last_verified: YYYY-MM-DD
```

## Cross-Project Pattern Loading Rules

- Load pattern index first.
- Select maximum 3–5 confirmed matching patterns.
- Never load all prior projects.
- Never let cross-project patterns override current project truth.

## Autopilot Mode Values

`SILENT`  — autonomous operation, log only, interrupt on critical rules only
`SURFACE` — autonomous operation + Attention List at session end (recommended)
`GUIDED`  — ask before each significant action

## Interrupt Rule Triggers

`risk_level: high|critical` | `confidence_below: 0.5` | `new_dependency: true`
`scope_expansion: true` | `errors_found: true` | `dream_pass_due: true`

## VUCP File Types (updated)

`autopilot`   — `AUTOPILOT.md`, self-regulation config
`ai-guide`    — `*.ai.md`, instructions for AI agents (not for humans)

## Assisted Autopilot Schema

`AUTOPILOT.md` frontmatter:

```yaml
protocol: VUCP
type: autopilot
version: "0.4.1"
mode: SILENT|SURFACE|GUIDED
owner_approval_required_for: []
attention_output: "_attention/ATTENTION.md"
autopilot_log: "_delta/AUTOPILOT_LOG.md"
```

Structured autopilot log entry:

```yaml
type: autopilot_action
actor: agent
autopilot_mode: SURFACE
action_class: read|write|suggest|approval_required|blocked
risk_level: low|medium|high|critical
confidence: 0.82
human_approval: not_required|required|granted|denied
summary: "Short action summary"
why_it_matters: "Why the human should care"
```

Rules:

- `SILENT` still interrupts for critical risk and forbidden actions.
- `SURFACE` is recommended for most users.
- `GUIDED` is for maximum human control.
- Cross-project patterns, Dream Pass, and memory promotion still require human approval when trust changes.
