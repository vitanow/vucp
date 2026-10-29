# VUCP_SPEC_v0.4.1.md

# VUCP — Living Workspace Protocol  
## Vitanow Unified Context Protocol v0.4.1

**Status:** Final MVP Specification  
**Version:** 0.4.1  
**Author:** Zahari Georgiev Vitanov / Vitanow OPS  
**Date:** 2026-06-23  
**Recommended License:** MIT License after public repository creation

---

## 0. One-Line Definition

**VUCP is a filesystem-native protocol for making human-AI work inspectable, repeatable, portable, reviewable, and safer.**

A VUCP workspace turns a normal project folder into a living working environment where:

- knowledge is stored as readable files;
- workflows are defined as stages;
- context is loaded intentionally;
- every meaningful run leaves a trace;
- errors become future memory;
- human review becomes structured data;
- humans and agents share the same source of truth.

---

## 1. Why VUCP Exists

AI systems often fail not because the model is weak, but because the context is chaotic.

Common problems:

- project knowledge is scattered across chats, docs, folders, tools, and memory;
- agents receive too much irrelevant context or too little critical context;
- outputs are not reproducible;
- human review is informal and gets lost;
- workflows are buried inside prompts instead of visible structures;
- errors repeat because the system does not remember them;
- teams cannot see why decisions were made;
- switching models or platforms breaks continuity;
- run artifacts pollute project history when every tiny interaction is preserved forever;
- agents waste tokens by rereading unchanged context.

VUCP exists to solve this with a simple principle:

> **If the work matters, its context, process, memory, and safety rules must be visible as files.**

VUCP does not require a cloud platform, database, SDK, agent framework, vector store, or proprietary runtime.

The primary coordination substrate is the filesystem.

---

## 2. Core Promise

A VUCP workspace should be:

1. **Human-readable** — a person can open the folder and understand the project.
2. **Agent-readable** — an AI agent can read the same files and act correctly.
3. **Portable** — copy the folder and the workspace still makes sense.
4. **Auditable** — important runs, decisions, errors, and reviews leave traces.
5. **Reproducible** — meaningful past runs can be inspected with the knowledge and inputs used at the time.
6. **Safe** — risky actions require safeguards, review, and rollback thinking.
7. **Efficient** — context loading should be intentional, not accidental.
8. **Progressive** — beginners start simple; professionals can scale the structure.
9. **Vendor-neutral** — works with ChatGPT, Claude, Gemini, Codex, local models, shell scripts, or human-only workflows.

---

## 3. Conceptual Formula

```text
VUCP =
ICM-style Stage Engine
+ OKF-compatible Knowledge Bundle
+ Manifest Routing
+ Delta Memory
+ Review Gates
+ Safeguards
+ Reproducible Runs
+ Context Loading Discipline
+ Progressive Tooling
```

In simpler language:

```text
ICM moves the work.
OKF carries the knowledge.
MANIFEST routes the process.
Delta Memory remembers the experience.
Safeguards protect the system.
Review Gates keep humans in control.
.vucpignore protects attention.
Run classes protect Git history.
CURRENT.md protects operational truth.
```

---

## 4. Design Principles

### 4.1 Files are the control surface

The workspace state should be inspectable through normal files and folders.

If critical state exists only inside a hidden tool, database, or chat window, the workspace is not fully explainable.

### 4.2 Markdown is the human interface

Humans should be able to read and edit most VUCP files in any text editor.

### 4.3 YAML is the machine contract

Structured metadata should live in YAML frontmatter or YAML files when agents, scripts, or validators need to parse it.

### 4.4 Knowledge, workflow, memory, and safety are separate layers

A project should not mix domain knowledge, process instructions, execution logs, and safety rules in one giant prompt.

### 4.5 Every stage has a contract

Each stage must define its purpose, required context, allowed actions, forbidden actions, inputs, outputs, review requirements, and verification steps.

### 4.6 Every meaningful run leaves a trace

Not every AI interaction deserves a permanent record. But every approved standard or milestone run should be traceable.

### 4.7 Every error becomes future context

Errors should not disappear into chat history. They should be captured in `_delta/ERRORS.md`.

### 4.8 Every important decision records its reason

A decision without reasoning becomes future confusion.

### 4.9 Knowledge updates are proposed before promotion

Agents may propose updates to `_knowledge/`, but they should not silently mutate trusted knowledge.

### 4.10 Context must be intentional, not accidental

A VUCP agent should not scan everything.

It should load only:

1. required root context;
2. stage contract;
3. selected knowledge files;
4. relevant delta memory;
5. explicit inputs.

Everything else is ignored unless requested.

### 4.11 Complexity must be progressive

VUCP must be useful in five minutes and still powerful after five years.

---

## 5. Workspace Levels

VUCP supports three levels.

The goal is not to force every user into the full structure. The goal is to allow natural growth.

---

### 5.1 Level 1 — Simple Workspace

For beginners, creators, solo projects, quick planning, or non-technical users.

```text
my_project/
  START.md
  CURRENT.md
  IDEAS.md
  DECISIONS.md
  LOG.md
  files/
```

Required files:

| File | Purpose |
|---|---|
| `START.md` | Where to begin |
| `CURRENT.md` | Current state and next action |
| `IDEAS.md` | Raw ideas and notes |
| `DECISIONS.md` | Important choices and reasons |
| `LOG.md` | Chronological progress |

Simple mode may be upgraded to Standard mode later.

---

### 5.2 Level 2 — Standard Workspace

For serious human-AI workflows.

```text
project_root/
  START.md
  WORKSPACE.md
  CURRENT.md
  AGENTS.md
  MANIFEST.yaml
  SCHEMA.md
  SAFEGUARDS.md
  DECISIONS.md
  .vucpignore

  _inbox/
  _knowledge/
    index.md
  _delta/
    LOG.md
    LEARNINGS.md
    ERRORS.md
  _runs/
  _proposals/
  _verification/
  _publish/
  _archive/

  stages/
    research/
      CONTEXT.md
      input/
      output/
    drafting/
      CONTEXT.md
      input/
      output/
    review/
      CONTEXT.md
      input/
      output/
```

This is the default VUCP structure.

---

### 5.3 Level 3 — Pro Workspace

For engineering teams, production systems, CI/CD, multi-agent setups, operations, and regulated workflows.

```text
project_root/
  START.md
  WORKSPACE.md
  CURRENT.md
  AGENTS.md
  MANIFEST.yaml
  SCHEMA.md
  SAFEGUARDS.md
  DECISIONS.md
  CHANGELOG.md
  .vucpignore

  _inbox/
  _knowledge/
  _shared/
  _delta/
  _runs/
  _proposals/
  _verification/
  _publish/
  _archive/
  _bridges/
  _scripts/
  _knowledge_history/

  workflows/
    code-change/
      audit/
        CONTEXT.md
        input/
        output/
      patch-plan/
        CONTEXT.md
        input/
        output/
      implementation-brief/
        CONTEXT.md
        input/
        output/
      verification/
        CONTEXT.md
        input/
        output/
      release-notes/
        CONTEXT.md
        input/
        output/
```

In Pro mode, `workflows/` may replace `stages/` when multiple workflow types exist inside one workspace.

---

## 6. Naming Conventions

### 6.1 Root Control Files

Root control files use uppercase names:

```text
START.md
WORKSPACE.md
CURRENT.md
AGENTS.md
MANIFEST.yaml
SCHEMA.md
SAFEGUARDS.md
DECISIONS.md
CHANGELOG.md
```

Reason:

- visually separate control files from normal project files;
- make them easy to find;
- improve cross-project consistency.

---

### 6.2 System Directories

VUCP system directories start with underscore:

```text
_inbox/
_knowledge/
_delta/
_runs/
_proposals/
_verification/
_publish/
_archive/
_shared/
_bridges/
_scripts/
_knowledge_history/
```

Reason:

- visually group protocol folders;
- keep them separate from user/domain folders;
- make scanning and tooling easier.

---

### 6.3 Local Runtime Directory

`.vucp/` is reserved for local runtime state.

```text
.vucp/
```

Reason:

- hidden by default on many systems;
- suitable for cache, temporary runs, local indexes, and non-canonical state.

---

### 6.4 Stage Names

Stage names should be lowercase kebab-case or snake_case.

Allowed:

```text
research
drafting
review
patch-plan
incident-response
data_normalization
```

Avoid:

```text
Stage 1
My Great Stage
02_FINAL_REVIEW_NEW
```

---

## 7. Required Root Files

---

### 7.1 `START.md`

Human entry point.

Purpose:

- explain how to use the workspace;
- tell the user what to read first;
- provide the simplest path to action.

Minimal example:

```markdown
# Start Here

1. Read `CURRENT.md`.
2. Put raw ideas or files in `_inbox/`.
3. Move through the workflow defined in `MANIFEST.yaml`.
4. Record important decisions in `DECISIONS.md`.
5. Check `SAFEGUARDS.md` before risky actions.
```

---

### 7.2 `WORKSPACE.md`

Identity and map of the project.

Recommended frontmatter:

```yaml
---
protocol: VUCP
version: "0.4.1"
project: "Project Name"
owner: "Owner Name"
language: "en"
created: "2026-06-23"
status: "active"
---
```

Recommended body:

```markdown
# Workspace

## Purpose
What this project exists to do.

## Scope
What is included.

## Out of Scope
What is not included.

## Main Workflows
- research
- drafting
- review

## Important Links
- `CURRENT.md`
- `MANIFEST.yaml`
- `SAFEGUARDS.md`
```

---

### 7.3 `CURRENT.md`

Single source of present operational truth.

This is one of the most important files in VUCP.

It answers:

- where are we now?
- what was last completed?
- what is blocked?
- what is the next action?
- what must not be touched?

Recommended structure:

```markdown
# Current State

## Status
active

## Last Completed
Describe the latest completed meaningful step.

## Current Problem
Describe the active problem or objective.

## Next Action
One clear next action.

## Blockers
- None

## Do Not Touch
- Production credentials
- Database schema
- Firewall rules

## Last Updated
2026-06-23
```

Rule:

> Every active workspace should have exactly one clear `Next Action`.

---

### 7.4 `AGENTS.md`

Agent behavior contract.

Defines how AI agents should behave in the workspace.

Recommended structure:

```markdown
# Agent Instructions

## General Rules
- Read `CURRENT.md` before acting.
- Read `SAFEGUARDS.md` before proposing risky changes.
- Read the current stage `CONTEXT.md`.
- Respect `.vucpignore`.
- Never silently change `_knowledge/`.
- Propose knowledge updates under `_proposals/knowledge_updates/`.
- Record meaningful findings in `_delta/`.

## Agent Profiles

### researcher
Reads broadly. Writes concise findings. Lists uncertainty.

### writer
Creates polished human-facing output. Follows brand voice.

### reviewer
Checks correctness, risks, missing assumptions, and consistency.

### operator
Can propose commands. Must not execute destructive actions without explicit approval (a policy rule; technical enforcement depends on the agent runtime).
```

---

### 7.5 `MANIFEST.yaml`

Declarative routing map.

Controls:

- workflow order;
- stage paths;
- agent roles;
- required knowledge;
- review gates;
- branching conditions;
- outputs.

Minimal example:

```yaml
version: "0.4.1"
protocol: "VUCP"
project: "example-project"

entrypoints:
  human: "START.md"
  agent: "AGENTS.md"
  current_state: "CURRENT.md"

pipeline:
  - id: research
    path: "stages/research"
    type: "research"
    agent: "researcher"
    requires_review: true
    risk_level: "low"
    knowledge:
      mode: "auto"
      include_tags: ["source", "market", "problem"]
    outputs:
      - "findings.md"
    next:
      approved: "drafting"
      rejected: "research"

  - id: drafting
    path: "stages/drafting"
    type: "synthesis"
    agent: "writer"
    requires_review: true
    risk_level: "medium"
    knowledge:
      include:
        - "_knowledge/brand/voice.md"
        - "_knowledge/policies/safety.md"
    outputs:
      - "draft.md"
    next:
      approved: "review"
      rejected: "drafting"

  - id: review
    path: "stages/review"
    type: "review"
    agent: "reviewer"
    requires_review: false
    risk_level: "low"
    outputs:
      - "review_log.md"
```

Rules:

- `id` must be unique.
- `path` must point to an existing stage folder.
- `requires_review` must be explicit.
- `risk_level` should be explicit.
- `next` may be omitted only for terminal stages.
- `knowledge.mode: auto` means the agent should use `_knowledge/index.md` and VUCP metadata to decide what to load.

---

### 7.6 `SCHEMA.md`

Defines types, conventions, required metadata, and naming rules.

Recommended content:

```markdown
# VUCP Schema v0.4.1

## Naming Standards
- Root control files are UPPERCASE.
- System directories start with `_`.
- Local runtime lives under `.vucp/`.
- Stage folders use lowercase kebab-case or snake_case.

## Stage Types
- research
- analysis
- synthesis
- drafting
- review
- implementation
- verification
- release
- incident-response

## Knowledge Types
- concept
- system
- policy
- metric
- table
- api
- playbook
- persona
- glossary_term
- decision_record

## Artifact Types
- input
- output
- report
- data
- decision
- command
- review
- proposal

## Review Status
- pending
- approved
- approved_with_changes
- rejected
- blocked

## Risk Levels
- low
- medium
- high
- critical

## Run Classes
- transient
- standard
- milestone
```

---

### 7.7 `SAFEGUARDS.md`

Safety and control plane.

Required for any project involving:

- infrastructure;
- code;
- production systems;
- finance;
- legal topics;
- medical topics;
- credentials;
- user data;
- irreversible operations.

Recommended structure:

```markdown
# Safeguards

## Never Change Without Explicit Approval
- Production credentials
- Firewall rules
- Database schema
- Payment settings
- Public output contracts
- Customer data

## Always Include Before Risky Changes
- Risk assessment
- Verification steps
- Rollback plan
- Files changed
- Commands to run manually

## Risk Levels

### Low
Documentation-only or reversible local changes.

### Medium
Code changes with tests and rollback.

### High
Production-adjacent changes.

### Critical
Credentials, security, payment, data deletion, or live infrastructure.
```

---

### 7.8 `DECISIONS.md`

Decision log.

Recommended structure:

```markdown
# Decisions

## 2026-06-23 — Decision Title

**Decision:** What was decided.

**Reason:** Why this was chosen.

**Alternatives considered:**
- Option A
- Option B

**Impact:** What this affects.

**Status:** active
```

---

### 7.9 `.vucpignore`

`.vucpignore` defines files and folders that VUCP agents and CLI tools should ignore by default.

It works like `.gitignore`, but for AI context loading and workspace scanning.

Purpose:

- prevent agents from reading irrelevant or huge folders;
- reduce token usage;
- protect archives, dependencies, secrets, build outputs, and generated files;
- make context loading predictable.

Recommended default:

```gitignore
# Dependencies
node_modules/
.venv/
venv/
vendor/

# Build outputs
dist/
build/
target/
.cache/
__pycache__/
*.pyc

# Git and IDE state
.git/
.idea/
.vscode/

# Archives and old material
_archive/
*.zip
*.tar
*.gz
*.7z

# Secrets and credentials
.env
.env.*
*.key
*.pem
*.p12
secrets/
credentials/

# Large media
*.mp4
*.mov
*.avi
*.mkv
*.wav
*.mp3
*.psd

# Local VUCP runtime
.vucp/cache/
.vucp/tmp/
.vucp/transient_runs/
```

Rule:

> Agents must respect `.vucpignore` unless the human explicitly instructs otherwise.

---

## 8. System Folders

---

### 8.1 `_inbox/`

Raw capture zone.

Use for:

- unprocessed ideas;
- screenshots;
- notes;
- files;
- user dumps;
- rough material.

Recommended structure:

```text
_inbox/
  ideas/
  files/
  notes/
```

Rule:

> `_inbox/` is allowed to be messy. The rest of the workspace should not be.

---

### 8.2 `_knowledge/`

Domain knowledge.

VUCP knowledge files should be compatible with markdown + YAML frontmatter.

Recommended structure:

```text
_knowledge/
  index.md
  systems/
  metrics/
  policies/
  playbooks/
  brand/
  glossary/
```

---

### 8.3 `_knowledge/index.md`

Fast loading index.

Purpose:

- reduce context size;
- help agents choose what to read;
- list knowledge files with summaries, tags, and stage triggers.

Example:

```markdown
# Knowledge Index

| Path | Type | Title | Tags | Summary | Stage Triggers |
|---|---|---|---|---|---|
| `_knowledge/brand/voice.md` | policy | Brand Voice | brand, writing | Rules for public voice and tone. | drafting, review |
| `_knowledge/metrics/revenue.md` | metric | Revenue | business, finance | Defines revenue calculation. | analysis |
```

Rule:

> Agents should read `_knowledge/index.md` before loading full knowledge files.

---

### 8.4 `_delta/`

Accumulated operational memory.

```text
_delta/
  LOG.md
  LEARNINGS.md
  ERRORS.md
```

#### `_delta/LOG.md`

Chronological run and progress log.

```markdown
## 2026-06-23 | run_2026-06-23_1530 | drafting | SUCCESS
- Agent: writer
- Output: draft.md
- Review: approved_with_changes
- Notes: Brand voice needed stronger opening.
```

#### `_delta/LEARNINGS.md`

Reusable patterns discovered over time.

```markdown
## Pattern: Stronger opening needed for public specs

Discovered: 2026-06-23  
Validated: 2 runs  
Rule: Public-facing VUCP documents should open with the user pain before technical structure.
```

#### `_delta/ERRORS.md`

Known errors and resolutions.

```markdown
## Error: Agent skipped SAFEGUARDS.md

Discovered: 2026-06-23  
Symptom: Proposed production change without rollback.  
Resolution: Add `SAFEGUARDS.md` to required context for all high-risk stages.  
Status: resolved
```

---

### 8.5 `_runs/`

Records of standard and milestone executions.

Recommended run structure:

```text
_runs/
  run_2026-06-23_1530/
    RUN.md
    knowledge.lock.yaml
    inputs/
    outputs/
    review.md
    artifacts/
    snapshot_knowledge/
```

`snapshot_knowledge/` is optional and should be used for milestone or high-risk runs.

Transient runs should not go here. They belong under `.vucp/transient_runs/`.

---

### 8.6 `_proposals/`

Staging area for proposed changes.

```text
_proposals/
  knowledge_updates/
  schema_changes/
  workflow_changes/
```

Rule:

> Agents may propose changes here. Humans or approved merge stages promote them.

---

### 8.7 `_verification/`

Reusable verification assets.

```text
_verification/
  checklists/
  tests/
  rollback/
```

Examples:

```text
_verification/checklists/release.md
_verification/rollback/weather-server.md
_verification/tests/cli-help.md
```

---

### 8.8 `_publish/`

Final human-facing outputs.

Use for:

- reports;
- briefs;
- diagrams;
- HTML exports;
- release documents;
- public documentation.

---

### 8.9 `_archive/`

Old, deprecated, or inactive material.

Rule:

> Agents should not load `_archive/` unless explicitly instructed.

---

### 8.10 `_bridges/` Optional

External integration configs.

```text
_bridges/
  github.yaml
  slack.yaml
  n8n.yaml
  notion.yaml
```

Rule:

> Bridges are optional and must not be required for VUCP compatibility.

---

## 9. Local Runtime: `.vucp/`

`.vucp/` is the local VUCP runtime folder.

It is used for cache, temporary runs, local indexes, lock files, and CLI state.

Recommended structure:

```text
.vucp/
  cache/
    context_hashes.yaml
    knowledge_index_cache.json
  tmp/
  transient_runs/
  state.yaml
```

Rule:

> `.vucp/` is local runtime state. It should usually be included in `.gitignore`.

Recommended `.gitignore` entry:

```gitignore
.vucp/cache/
.vucp/tmp/
.vucp/transient_runs/
```

Depending on the project, `.vucp/state.yaml` may be committed or ignored.

---

## 10. Context Inflation Control

VUCP agents often need to read:

- `CURRENT.md`
- `SAFEGUARDS.md`
- `_knowledge/index.md`
- `_delta/ERRORS.md`
- stage `CONTEXT.md`
- selected knowledge files

This can create context inflation if the same files are repeatedly loaded without change.

VUCP v0.4.1 introduces the **Read-if-Changed Rule**.

---

### 10.1 Read-if-Changed Rule

Before reading large or repeated context files, a VUCP-compatible tool may check their hash.

If the file has not changed since the last run, the tool may use a cached summary or previously loaded state.

Recommended cache file:

```text
.vucp/cache/context_hashes.yaml
```

Example:

```yaml
files:
  CURRENT.md:
    sha256: "example_hash"
    last_loaded: "2026-06-23T15:30:00Z"
    cached_summary: ".vucp/cache/CURRENT.summary.md"

  SAFEGUARDS.md:
    sha256: "example_hash"
    last_loaded: "2026-06-23T15:30:00Z"
    cached_summary: ".vucp/cache/SAFEGUARDS.summary.md"
```

Rule:

> Full files are the source of truth. Cached summaries are optimization only.

If there is any conflict between a cached summary and the actual file, the actual file wins.

---

### 10.2 Future Context Load Command

Future CLI tooling should support:

```bash
vucp context load
vucp context load --stage drafting
vucp context load --stage drafting --json
vucp context load --stage drafting --no-cache
```

Purpose:

- assemble the exact context required for a stage;
- respect `.vucpignore`;
- use `_knowledge/index.md`;
- apply `MANIFEST.yaml` rules;
- check hashes;
- reduce repeated context.

---

## 11. Run Classification

Not every AI interaction deserves a permanent `_runs/` record.

VUCP v0.4.1 defines three run classes:

```text
transient
standard
milestone
```

---

### 11.1 Transient Run

Temporary, low-value, exploratory, or quick work.

Storage:

```text
.vucp/transient_runs/
```

Usually ignored by Git.

Examples:

- quick brainstorming;
- failed draft;
- minor local experiment;
- temporary one-stage task.

---

### 11.2 Standard Run

Meaningful work that affects the project.

Storage:

```text
_runs/
```

May be committed to Git.

Examples:

- approved stage output;
- completed research pass;
- accepted draft;
- verified code-change brief;
- meaningful decision support.

---

### 11.3 Milestone Run

High-value, high-risk, or release-level work.

Storage:

```text
_runs/
  run_YYYY-MM-DD_HHMM/
    RUN.md
    knowledge.lock.yaml
    inputs/
    outputs/
    review.md
    snapshot_knowledge/
```

Should usually be committed to Git.

Examples:

- production change;
- release candidate;
- major strategy decision;
- final client report;
- infrastructure migration;
- compliance-sensitive output.

---

### 11.4 Run Storage Rule

```text
Transient runs go to `.vucp/transient_runs/`.
Standard and milestone runs go to `_runs/`.
Only milestone runs require full knowledge snapshots.
```

For normal standard runs, use:

```text
knowledge.lock.yaml
```

For milestone runs, use both:

```text
knowledge.lock.yaml
snapshot_knowledge/
```

---

## 12. State Synchronization Rule

VUCP has multiple state files:

- `CURRENT.md`
- `_delta/LOG.md`
- `_runs/<run_id>/RUN.md`
- artifact frontmatter
- review files

This can create drift if they are not updated together.

VUCP v0.4.1 defines the **State Sync Rule**.

---

### 12.1 State Sync Rule

After every approved standard or milestone run:

1. append a summary to `_delta/LOG.md`;
2. update `CURRENT.md`;
3. update the run status in `_runs/<run_id>/RUN.md`;
4. record review status if applicable;
5. propose learnings or errors when relevant.

### Required `CURRENT.md` updates

After a meaningful run, update:

```text
Last Completed
Current Problem
Next Action
Blockers
Last Updated
```

Rule:

> `CURRENT.md` must represent the active operational truth. `_delta/LOG.md` represents history.

---

### 12.2 Future Sync Command

Recommended command:

```bash
vucp sync-state
```

Purpose:

- check whether `CURRENT.md` is stale;
- compare latest `_runs/` entry with `_delta/LOG.md`;
- warn if approved run did not update current state;
- optionally update placeholders.

---

## 13. Stage Structure

Each stage is a folder with:

```text
stage_name/
  CONTEXT.md
  input/
  output/
```

Example:

```text
stages/
  research/
    CONTEXT.md
    input/
    output/
  drafting/
    CONTEXT.md
    input/
    output/
  review/
    CONTEXT.md
    input/
    output/
```

---

## 14. `CONTEXT.md` Stage Contract

Every stage must have a `CONTEXT.md`.

Recommended template:

```markdown
---
stage: "drafting"
type: "synthesis"
version: "1.0"
agent: "writer"
review_required: true
risk_level: "medium"
---

# Stage: Drafting

## 1. Purpose
Produce a clear draft from approved research findings.

## 2. Required Context
Read before acting:
- `/CURRENT.md`
- `/SAFEGUARDS.md`
- `/_knowledge/index.md`
- `/_delta/ERRORS.md`

## 3. Knowledge Context
Load these knowledge files:
- `/_knowledge/brand/voice.md`
- `/_knowledge/policies/safety.md`

## 4. Inputs
Expected input files:
- `input/findings.md`

## 5. Allowed Actions
- Read input files.
- Produce markdown outputs.
- Propose knowledge updates in `/_proposals/knowledge_updates/`.

## 6. Forbidden Actions
- Do not modify trusted knowledge directly.
- Do not delete previous runs.
- Do not perform production changes.

## 7. Process
1. Read required context.
2. Check known errors.
3. Read inputs.
4. Produce draft.
5. List assumptions and uncertainties.

## 8. Outputs
Required output files:
- `output/draft.md`

## 9. Verification
Before marking complete:
- Confirm required inputs were read.
- Confirm assumptions are listed.
- Confirm output file exists.
- Confirm no forbidden action was taken.

## 10. Review Gate
Stop after writing outputs.
Human approval required before next stage.

## 11. Delta Update
After approval:
- append result to `/_delta/LOG.md`;
- propose reusable patterns for `/_delta/LEARNINGS.md`;
- record errors in `/_delta/ERRORS.md`;
- update `CURRENT.md` for standard and milestone runs.
```

---

## 15. Knowledge File Format

VUCP knowledge files should remain compatible with a simple markdown + YAML-frontmatter model.

Recommended format:

```markdown
---
type: policy
title: Brand Voice
description: Voice and tone rules for public-facing content.
tags: [brand, writing, public]
timestamp: 2026-06-23T15:30:00Z

vucp:
  stage_triggers: [drafting, review]
  load_policy: required
  confidence: high
  owner: "Zahari Vitanov"
  last_reviewed: 2026-06-23
---

# Brand Voice

## Rules
- Direct.
- Strategic.
- Practical before poetic.
- No empty motivation.

## Do Not
- Do not sound generic.
- Do not over-explain obvious points.
```

### Required top-level fields

| Field | Required | Purpose |
|---|---:|---|
| `type` | yes | Knowledge type |
| `title` | yes | Human-readable title |
| `description` | recommended | Short description |
| `tags` | recommended | Search and routing |
| `timestamp` | recommended | Recency |

### VUCP extension namespace

VUCP-specific fields should live under:

```yaml
vucp:
```

This avoids polluting the generic knowledge format.

---

## 16. Knowledge Bridges

Knowledge bridges connect knowledge files to stages.

Recommended method:

```yaml
vucp:
  stage_triggers: [drafting, review]
  load_policy: required
```

Allowed `load_policy` values:

```text
required
suggested
optional
ignore_by_default
```

Agents should:

1. read `_knowledge/index.md`;
2. identify files matching the current stage;
3. load required files;
4. load suggested files if relevant;
5. avoid optional files unless needed.

---

## 17. Artifact Frontmatter

Important outputs should include structured review metadata.

Example:

```markdown
---
artifact_type: output
stage: drafting
run_id: run_2026-06-23_1530
review_status: pending
reviewed_by:
decision:
timestamp:
---

# Draft Output

...
```

After review:

```yaml
review_status: approved_with_changes
reviewed_by: "Zahari Vitanov"
decision: "approved_with_minor_edits"
timestamp: "2026-06-23T16:10:00Z"
```

Rule:

> Human review should become structured data, not just a comment.

---

## 18. Run Reproducibility

Each important standard or milestone run should include:

```text
RUN.md
knowledge.lock.yaml
inputs/
outputs/
review.md
```

Milestone runs may also include:

```text
snapshot_knowledge/
```

---

### 18.1 `RUN.md`

Example:

```markdown
---
run_id: run_2026-06-23_1530
stage: drafting
agent: writer
model: "unspecified"
started: 2026-06-23T15:30:00Z
completed: 2026-06-23T15:42:00Z
status: success
run_class: standard
---

# Run Summary

## Objective
Create a first draft from approved findings.

## Inputs
- `inputs/findings.md`

## Outputs
- `outputs/draft.md`

## Notes
Brand voice required stronger opening.
```

---

### 18.2 `knowledge.lock.yaml`

Example:

```yaml
run_id: "run_2026-06-23_1530"
knowledge_files:
  - path: "_knowledge/brand/voice.md"
    sha256: "example_hash"
    last_modified: "2026-06-23T14:20:00Z"
  - path: "_knowledge/policies/safety.md"
    sha256: "example_hash"
    last_modified: "2026-06-23T19:00:00Z"
```

Rule:

> For normal runs, store hashes. For milestone or high-risk runs, store full snapshots.

---

## 19. Review Gates

A review gate is a controlled pause between stages.

If `requires_review: true`, the agent must stop after producing outputs.

Allowed review decisions:

```text
pending
approved
approved_with_changes
rejected
blocked
```

Review result should be stored in:

```text
_runs/<run_id>/review.md
```

or inside the artifact frontmatter.

Example:

```markdown
---
review_status: rejected
reviewed_by: "Zahari Vitanov"
timestamp: 2026-06-23T16:20:00Z
---

# Review Notes

The draft is too generic. Rewrite with stronger practical examples.
```

---

## 20. Safeguards and Risk

Stages should define risk level:

```yaml
risk_level: low
```

Allowed values:

```text
low
medium
high
critical
```

Rules:

- `medium`, `high`, and `critical` stages should read `SAFEGUARDS.md`.
- `high` and `critical` stages must include rollback.
- destructive operations must require explicit human approval.
- note: these rules are instructions to agents. VUCP files do not enforce them; enforcement depends on the agent runtime (hooks, permissions, sandbox).
- agents should propose commands before execution when production systems are involved.

---

## 21. Manifest Routing

`MANIFEST.yaml` may define simple linear workflows or conditional workflows.

### 21.1 Linear example

```yaml
pipeline:
  - id: research
    next:
      approved: drafting

  - id: drafting
    next:
      approved: review

  - id: review
```

### 21.2 Conditional example

```yaml
pipeline:
  - id: analysis
    next:
      no_errors: delivery
      errors_found: remediation

  - id: remediation
    next:
      approved: analysis

  - id: delivery
```

Rule:

> Conditions should be simple and human-readable in v0.4.1. Complex branching belongs in future tooling.

---

## 22. CLI Roadmap

VUCP Core does not require CLI tools, but the reference implementation should provide them.

---

### 22.1 Required CLI UX

Every VUCP CLI tool should support:

```bash
--help
-h
help
/?
```

Help output should include:

- command list;
- usage;
- parameters;
- examples;
- JSON output option;
- exit codes;
- safety and rollback notes where relevant.

---

### 22.2 Proposed Commands

```bash
vucp init
vucp wizard
vucp lint
vucp context load
vucp sync-state
vucp graph
vucp index
vucp search
vucp quick
vucp snapshot
vucp rollback
vucp doctor
```

---

### 22.3 `vucp init`

Creates a workspace.

```bash
vucp init
vucp init --template code-change
vucp init --level simple
vucp init --language bg
```

---

### 22.4 `vucp wizard`

Interactive setup.

Questions:

1. Project name?
2. Project goal?
3. Language?
4. Project type?
5. Risk level?
6. Use AI agents?
7. Team size?

---

### 22.5 `vucp lint`

Validates workspace structure.

Checks:

- required files exist;
- `.vucpignore` exists;
- root control files follow uppercase convention;
- system directories use underscore convention;
- `MANIFEST.yaml` paths are valid;
- stage folders contain `CONTEXT.md`;
- required `_delta/` files exist;
- `_knowledge/index.md` exists;
- ignored folders are not referenced as required context;
- high-risk stages reference `SAFEGUARDS.md`;
- latest approved standard/milestone run is reflected in `CURRENT.md`;
- `_runs/` does not contain excessive transient runs.

---

### 22.6 `vucp context load`

Assembles the exact context required for a stage.

```bash
vucp context load --stage drafting
vucp context load --stage drafting --json
vucp context load --stage drafting --no-cache
```

---

### 22.7 `vucp sync-state`

Checks and optionally updates state alignment.

```bash
vucp sync-state
vucp sync-state --check
vucp sync-state --apply
```

---

### 22.8 `vucp graph`

Generates workflow visualization.

Outputs:

```text
_publish/workflow.mmd
_publish/workflow.html
```

---

### 22.9 `vucp index`

Updates `_knowledge/index.md`.

---

### 22.10 `vucp search`

Searches workspace knowledge.

Initial version:

```bash
vucp search "brand voice"
```

Future version:

```bash
vucp search "brand voice" --semantic
```

---

### 22.11 `vucp quick`

Temporary one-stage workspace for urgent tasks.

```bash
vucp quick "Summarize these notes"
vucp quick "Create a project plan" --keep
```

Transient quick runs should go under:

```text
.vucp/transient_runs/
```

---

### 22.12 `vucp snapshot`

Creates a reproducibility snapshot.

```bash
vucp snapshot
vucp snapshot --full-knowledge
```

---

### 22.13 `vucp rollback`

Restores previous run state or copies previous outputs.

```bash
vucp rollback run_2026-06-23_1530
```

---

### 22.14 `vucp doctor`

Checks environment health.

Examples:

- Git available?
- required folders present?
- invalid YAML?
- broken stage paths?
- missing safeguards?
- too many transient runs in `_runs/`?
- `.vucpignore` missing?

---

## 23. Templates

Initial official templates:

```text
code-change
research-to-brief
content-production
data-analysis
incident-response
business-idea-to-plan
local-operations
music-production
```

Recommended Vitanow-specific templates:

```text
weather-server-change
codex-implementation-brief
project-memory
acquisition-engine
scientific-theory-development
```

Each template should include:

```text
START.md
WORKSPACE.md
CURRENT.md
AGENTS.md
MANIFEST.yaml
SCHEMA.md
SAFEGUARDS.md
DECISIONS.md
.vucpignore
sample _knowledge/
sample _delta/
sample stages/
```

---

## 24. Bridges

Optional integrations live in `_bridges/`.

Example:

```yaml
# _bridges/n8n.yaml

on:
  review_approved:
    webhook: "https://example.com/webhook"

security:
  requires_confirmation: true
```

Supported future bridges:

```text
github
slack
discord
n8n
notion
google-drive
gmail
calendar
jira
```

Rule:

> Bridges must never be required for basic workspace operation.

---

## 25. Multilingual Support

File names should remain stable and English for compatibility:

```text
START.md
CURRENT.md
SAFEGUARDS.md
MANIFEST.yaml
```

File content may be generated in any language.

In `WORKSPACE.md`:

```yaml
language: bg
fallback_language: en
```

Rule:

> Stable filenames, local-language content.

---

## 26. Minimal Compliance

A workspace is VUCP-compatible at Standard level if it has:

```text
START.md
WORKSPACE.md
CURRENT.md
AGENTS.md
MANIFEST.yaml
SCHEMA.md
SAFEGUARDS.md
DECISIONS.md
.vucpignore
_knowledge/index.md
_delta/LOG.md
_delta/LEARNINGS.md
_delta/ERRORS.md
at least one stage with CONTEXT.md
```

`.vucp/` may be created by CLI tooling and is not required for manual compliance.

A workspace is VUCP-compatible at Simple level if it has:

```text
START.md
CURRENT.md
IDEAS.md
DECISIONS.md
LOG.md
```

---

## 27. What VUCP Is Not

VUCP is not:

- an agent framework;
- a vector database;
- a prompt library;
- a task manager;
- a cloud platform;
- a replacement for Git;
- a replacement for CI/CD;
- a replacement for human judgment.

VUCP can connect to those tools, but it should not depend on them.

---

## 28. Scope Boundaries for v0.4.1

Included in v0.4.1:

- workspace structure;
- required files;
- stage contracts;
- manifest routing;
- knowledge file conventions;
- delta memory;
- review gates;
- safeguards;
- run reproducibility;
- `.vucpignore`;
- `.vucp/` runtime convention;
- run classification;
- context cache strategy;
- state synchronization rule;
- CLI roadmap.

Not included in v0.4.1 Core:

- mandatory semantic search;
- mandatory cloud sync;
- mandatory GitHub integration;
- real-time multi-agent execution;
- automatic tool execution;
- graphical UI;
- hosted marketplace.

These may be part of future tooling or ecosystem layers.

---

## 29. Roadmap

### v0.4.1 — Final MVP Specification

- Core spec
- Stabilization patch merged
- Starter template
- First demo workspace
- Manual workflow execution

### v0.5 — CLI Foundation

- `vucp init`
- `vucp lint`
- `vucp index`
- `vucp graph`
- `vucp context load`
- 3 official templates

### v0.6 — Usability Layer

- `vucp wizard`
- `vucp quick`
- multilingual templates
- `vucp snapshot`
- `vucp rollback`
- `vucp sync-state`

### v0.7 — Ecosystem Layer

- `_bridges/`
- template installation
- community examples
- VUCP Hub directory

### v1.0 — Stable Protocol

- versioned schema;
- compatibility tests;
- official reference implementation;
- public repository;
- examples for creators, developers, operators, and researchers.

---

## 30. Example: Standard Workspace

```text
project_root/
  START.md
  WORKSPACE.md
  CURRENT.md
  AGENTS.md
  MANIFEST.yaml
  SCHEMA.md
  SAFEGUARDS.md
  DECISIONS.md
  .vucpignore

  _inbox/
    ideas/
    files/
    notes/

  _knowledge/
    index.md
    brand/
      voice.md
    policies/
      safety.md
    glossary/

  _delta/
    LOG.md
    LEARNINGS.md
    ERRORS.md

  _runs/
    run_2026-06-23_1530/
      RUN.md
      knowledge.lock.yaml
      inputs/
      outputs/
      review.md

  _proposals/
    knowledge_updates/
    schema_changes/
    workflow_changes/

  _verification/
    checklists/
    tests/
    rollback/

  _publish/
  _archive/

  stages/
    research/
      CONTEXT.md
      input/
      output/
    drafting/
      CONTEXT.md
      input/
      output/
    review/
      CONTEXT.md
      input/
      output/
```

---

## 31. Example: `CURRENT.md`

```markdown
# Current State

## Status
active

## Last Completed
VUCP v0.4.1 final MVP specification created.

## Current Problem
Build and validate the first official `vucp-template/` folder.

## Next Action
Create the starter template and demo workspace.

## Blockers
None.

## Do Not Touch
- Do not add more protocol features before the MVP template exists.
- Do not start full CLI implementation before the file structure is tested manually.

## Last Updated
2026-06-23
```

---

## 32. Example: `SAFEGUARDS.md`

```markdown
# Safeguards

## Core Rule
VUCP must stay simple enough to start manually.

## Never Add to Core Without Justification
- Mandatory cloud services
- Mandatory database
- Mandatory semantic search
- Mandatory GUI
- Mandatory external account

## Before Any Production Change
Include:
- risk level;
- files changed;
- commands proposed;
- verification steps;
- rollback plan.

## Human Approval Required
- destructive filesystem actions;
- credential changes;
- production deployment;
- firewall changes;
- database migrations;
- public release.
```

---

## 33. Example: `DECISIONS.md`

```markdown
# Decisions

## 2026-06-23 — Use English filenames with local-language content

**Decision:** Keep core filenames in English but allow content in any language.

**Reason:** Stable filenames help tools, templates, agents, GitHub examples, and cross-language compatibility.

**Impact:** Bulgarian workspaces still use `START.md`, `CURRENT.md`, and `SAFEGUARDS.md`, but their content may be Bulgarian.

**Status:** active
```

---

## 34. Example: `MANIFEST.yaml`

```yaml
version: "0.4.1"
protocol: "VUCP"
project: "vucp-demo"

entrypoints:
  human: "START.md"
  agent: "AGENTS.md"
  current_state: "CURRENT.md"

pipeline:
  - id: research
    path: "stages/research"
    type: "research"
    agent: "researcher"
    requires_review: true
    risk_level: "low"
    knowledge:
      mode: "auto"
      include_tags: ["source", "context", "problem"]
    outputs:
      - "findings.md"
    next:
      approved: "drafting"
      rejected: "research"

  - id: drafting
    path: "stages/drafting"
    type: "synthesis"
    agent: "writer"
    requires_review: true
    risk_level: "medium"
    knowledge:
      include:
        - "_knowledge/brand/voice.md"
    outputs:
      - "draft.md"
    next:
      approved: "review"
      rejected: "drafting"

  - id: review
    path: "stages/review"
    type: "review"
    agent: "reviewer"
    requires_review: false
    risk_level: "low"
    outputs:
      - "review_log.md"
```

---

## 35. Final Statement

VUCP is built on a simple belief:

> A project folder can become a living workspace when its knowledge, process, memory, review, and safety rules are visible.

The beginner sees a clean folder and knows where to start.

The professional sees an auditable, reproducible, model-agnostic operating environment.

The AI agent sees structured context, clear boundaries, and a reliable path to action.

That is the purpose of VUCP.

**Every project starts as a folder.  
VUCP makes the folder think.**
