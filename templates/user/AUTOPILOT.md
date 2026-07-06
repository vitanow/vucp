---
protocol: VUCP
type: autopilot
version: "0.4.1"
mode: SURFACE
owner_approval_required_for:
  - high_risk_changes
  - critical_risk_changes
  - production_writes
  - credential_changes
  - deletion_or_destructive_actions
  - publishing_or_external_communication
  - trusted_memory_promotion
attention_output: "_attention/ATTENTION.md"
autopilot_log: "_delta/AUTOPILOT_LOG.md"
---
# Assisted Autopilot

## Current mode

**Current mode:** `SURFACE`

## Modes

```yaml
mode: SILENT    # Agent works autonomously. Only interrupts for critical blocks.
mode: SURFACE   # Agent works, then surfaces a short attention list. Recommended.
mode: GUIDED    # Agent asks before each significant step. Maximum control.
```

## Recommended default

`SURFACE`

The agent may do safe checks and prepare recommendations, then show the human only what matters.

## Human Attention Levels

```text
auto       → safe to do without interrupting
suggest    → propose a low-risk action
approval   → human approval required
blocked    → cannot proceed without human decision
```

## Always interrupt for approval

- destructive file operations;
- production writes or deployments;
- credential or secret changes;
- legal, financial, medical, or sensitive claims;
- high/critical risk stages;
- promotion of trusted memory;
- publishing outside the workspace.

## Attention output

The human-facing report lives in:

```text
_attention/ATTENTION.md
```

Use it as the low-friction dashboard.
