---
type: cross_project_pattern
status: confirmed
confidence: 0.95
evidence_count: 5
source_projects:
  - obd-controller
  - weather-server
  - vucp-cli
applies_to:
  - cli
  - automation
  - scripts
  - developer-tools
does_not_apply_to:
  - static-document
  - social-post
  - brainstorming
tags:
  - cli
  - help
  - safety
last_verified: 2026-06-27
---

# CLI Help Contract

## Pattern

Every CLI tool should support:

- `--help`
- `-h`
- `help`
- `/?` when useful for Windows/operator habits

## Why

The user works across Windows, Linux, shell, Codex, and operational environments. Help must be discoverable from multiple habits.

## Use When

- creating scripts;
- creating CLI tools;
- writing automation;
- producing Codex implementation briefs.

## Do Not Use When

- writing static documents;
- writing UI copy;
- brainstorming names.

## Agent Instruction

When proposing a CLI tool, include a help system, examples, JSON output where useful, exit codes, and safety/rollback notes.
