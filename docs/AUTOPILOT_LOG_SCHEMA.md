# Autopilot Log

Structured log for agent actions performed or proposed under Assisted Autopilot.

## Schema

```yaml
type: autopilot_action
actor: agent
autopilot_mode: SURFACE
action_class: read|write|suggest|approval_required|blocked
risk_level: low|medium|high|critical
confidence: 0.82
human_approval: not_required|required|granted|denied
summary: "Short human-readable action summary"
why_it_matters: "One sentence explaining relevance"
created_at: 2026-06-30
```

## Entries

No structured autopilot actions recorded yet.
