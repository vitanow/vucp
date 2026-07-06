# Assisted Autopilot Layer

Status: optional v0.5 extension. Current package: `0.5-alpha-9.1`.

Assisted Autopilot lets VUCP reduce unnecessary human interaction while keeping important decisions visible.

The goal is not blind autonomy.

The goal is:

```text
AI handles safe routine checks.
Humans see only what matters.
Approvals are required for risk, trust, publishing, credentials, and irreversible actions.
```

## Modes

```text
SILENT   → agent works quietly but still interrupts for critical/forbidden actions
SURFACE  → agent works, then surfaces a short attention list; recommended default
GUIDED   → agent asks before each significant step
```

## Human attention only when it matters

The human should not have to inspect every file.

VUCP surfaces a compact dashboard:

```text
_attention/ATTENTION.md
```

Each item should explain:

- what needs attention;
- why it matters;
- recommended action;
- lowest-friction next step;
- attention level: `auto`, `suggest`, `approval`, or `blocked`.

## Always require approval

- high/critical risk work;
- destructive actions;
- production writes and deployments;
- credentials and secrets;
- publishing or external communication;
- legal, financial, medical, or sensitive claims;
- trusted memory promotion;
- changes that override `SAFEGUARDS.md`.

## CLI

```bash
python cli/vucp_cli_mvp.py autopilot status my-project
python cli/vucp_cli_mvp.py autopilot set my-project --mode SURFACE
python cli/vucp_cli_mvp.py autopilot audit my-project --json
```

## Structured audit

Autopilot actions should be logged in:

```text
_delta/AUTOPILOT_LOG.md
```

Using entries like:

```yaml
type: autopilot_action
actor: agent
autopilot_mode: SURFACE
action_class: suggest
risk_level: low
confidence: 0.86
human_approval: not_required
summary: "Generated attention report from doctor findings"
why_it_matters: "Keeps the human focused on actionable items"
```
