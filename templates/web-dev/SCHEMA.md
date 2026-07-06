# Workspace Schema and Naming Contracts

## Naming Standards
- Root control files: UPPERCASE (START.md, CURRENT.md, etc.)
- System folders: underscore prefix (_knowledge/, _delta/, etc.)
- Stage folders: numbered kebab-case (01-context-load, 02-plan, etc.)
- Knowledge files: kebab-case (system-overview.md, api-contracts.md)
- Code files: follow project conventions in WORKSPACE.md

## Workspace States
active | paused | completed | blocked

## Review Gate Decisions
pending | approved | approved_with_changes | rejected | blocked

## Risk Levels
low | medium | high | critical

## Run Classes
transient | standard | milestone

## Knowledge Types (for _knowledge/ frontmatter)
architecture | pattern | decision | policy | api | reference


## Memory Layer Clarity

| Layer | Answers | Scope |
|---|---|---|
| `USER_CORE.md` | Who am I and how do I generally work? | Cross-project personal context |
| `_user_contexts/` | How do I work in this domain? | Domain-specific personal context |
| `WORKSPACE.md` | What is this project? | Project identity and boundaries |
| `CURRENT.md` | What is happening right now? | Current operational truth |
| `_delta/ERRORS.md` | What has failed in this project? | Project-specific failure memory |
| `_delta/LEARNINGS.md` | What patterns emerged? | Project-specific learning memory |
| `_knowledge/` | What stable facts does this project know? | Stable project/domain knowledge |

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
