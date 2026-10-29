# Assisted Autopilot Layer

Status: optional v0.5 extension. Current package: `0.5.0a10` (0.5-alpha-9.2).

Assisted Autopilot lets VUCP reduce unnecessary human interaction while keeping important decisions visible.

The goal is not blind autonomy.

The goal is:

```text
AI handles safe routine checks.
Humans see only what matters.
Agents are instructed to ask for approval for risk, trust, publishing, credentials, and irreversible actions.
```

## Policy, not enforcement

Autopilot is policy, not enforcement. AUTOPILOT.md and the modes tell an agent when to stop and ask; they do not technically block anything. Whether a high-risk, destructive, production, credential, publishing, or trusted-memory action is actually stopped depends on your agent runtime and its settings (for example Claude Code hooks and permissions, Cursor agent settings, or the Codex sandbox and approval mode). Configure those for real limits.

The VUCP CLI only reads and writes files. `autopilot status` and `audit` report what the files say; they cannot prove an agent followed them.

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

## Always ask for approval (instruction to the agent)

Agents should stop and ask before the actions below. This is guidance; enforce it in the runtime if it matters.


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
