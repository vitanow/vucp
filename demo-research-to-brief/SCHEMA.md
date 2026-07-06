# Workspace Schema and Naming Contracts

## Naming Standards

- **Root Control Surfaces:** Must be UPPERCASE (`START.md`, `CURRENT.md`, `AGENTS.md`).
- **System Folders:** Must use underscore prefix (`_knowledge/`, `_delta/`, `_runs/`).
- **Pipeline Stage Folders:** Must use lowercase kebab-case or snake_case (`stages/research-pass/`, `stages/data_normalization/`).

## Allowed Workspace States

- active
- paused
- completed
- blocked

## Allowed Review Gate Decisions

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
