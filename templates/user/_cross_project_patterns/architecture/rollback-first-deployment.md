---
type: cross_project_pattern
status: confirmed
confidence: 0.88
evidence_count: 4
source_projects:
  - weather-server
  - hyper-v-network
  - vucp-cli
applies_to:
  - infrastructure
  - deployment
  - production
  - cli
  - operations
does_not_apply_to:
  - simple-writing
  - naming
  - early-brainstorm
tags:
  - rollback
  - deployment
  - safety
last_verified: 2026-06-27
---

# Rollback-First Deployment

## Pattern

Before any risky execution, define:

- files changed;
- commands proposed;
- verification steps;
- rollback plan;
- human approval checkpoint.

## Why

Production-adjacent work fails less often when rollback is designed before execution.

## Use When

- modifying infrastructure;
- changing production contracts;
- creating deployment scripts;
- changing public workflows;
- touching credentials, network, data, or automation.

## Do Not Use When

- answering a short conceptual question;
- creating a non-executable draft;
- exploring rough ideas.
