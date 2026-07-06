---
protocol: VUCP
version: "0.4.1"
project: "<PROJECT_NAME>"
owner: "<OWNER_NAME>"
language: "en"
created: "2026-06-27"
status: active
user_context: "<software | physics | business | creative | personal>"
user_profile: "~/.vucp-user/USER_CORE.md"
cross_project_patterns: "~/.vucp-user/_cross_project_patterns/index.md"
cross_project_pattern_policy: "selective"
max_cross_project_patterns: 5
---

# Workspace Identity & Boundaries

## Purpose

<!-- Describe why this project exists and its primary goal. -->

## Scope

<!-- Define what is explicitly included in this project workspace. -->

## Out of Scope

<!-- Define what is strictly excluded to prevent agent scope creep. -->

## Core Pipeline Workflows

- research
- drafting
- review

## Context Loading Order

At the start of every Full Startup session, load in this order:

1. `~/.vucp-user/USER_CORE.md` — who the owner is *(optional, load if available)*
2. `~/.vucp-user/_user_contexts/<user_context>.md` — domain behavior *(optional)*
3. `CURRENT.md` — current state and active task *(always)*
4. `_delta/ERRORS.md` — past failures to avoid *(always)*
5. Current stage `CONTEXT.md` — this session's contract *(always)*

## Cross-Project Pattern Policy

Cross-project patterns are optional and selective.

During Full Startup, agents may read the configured cross-project pattern index and load at most `max_cross_project_patterns` confirmed patterns that match the current domain, stage, risk profile, or task.

Rules:

- Do not load entire previous projects.
- Do not load candidate patterns unless explicitly requested.
- Do not apply a pattern if `does_not_apply_to` matches the current task.
- Cross-project patterns are advisory and must not override `SAFEGUARDS.md`, `CONTEXT.md`, or direct human instruction.
