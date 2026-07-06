# GitHub Launch Checklist

## Before push

- [ ] Confirm README starts with creator attribution.
- [ ] Confirm CLI version is `0.5-alpha-9.1`.
- [ ] Confirm Core protocol version is `0.4.1`.
- [ ] Confirm `AUTHORS.md` exists.
- [ ] Confirm `CITATION.cff` exists.
- [ ] Confirm `docs/ABOUT_CREATOR.md` exists.
- [ ] Confirm `docs/BRAND_POSITIONING.md` exists.
- [ ] Confirm `docs/LAUNCH_POSTS.md` contains creator-aware posts.
- [ ] Run:

```bash
python cli/vucp_cli_mvp.py --version
python cli/vucp_cli_mvp.py doctor templates/standard --json
python cli/vucp_cli_mvp.py lint templates/standard --json
python cli/vucp_cli_mvp.py lint templates/web-dev --json
```

## GitHub About

```text
Description:
A portable AI workspace format for inspectable, repeatable, and safer human-AI work.

Topics:
ai, llm, codex, claude, cursor, windsurf, developer-tools, prompt-engineering, workflow, filesystem, context-management, ai-agents
```

## Creator line

```text
Created by Zahari Georgiev Vitanov / Vitanow OPS
```

## Launch post

Use `docs/LAUNCH_POSTS.md`.

## Assisted Autopilot launch angle

VUCP now includes Assisted Autopilot: human attention only when it matters.

```text
AUTOPILOT.md
_attention/ATTENTION.md
_delta/AUTOPILOT_LOG.md
```

The recommended default is `SURFACE`: AI performs safe routine checks and then surfaces a short attention list with recommended next steps.

Created by **Zahari Georgiev Vitanov / Vitanow OPS**.
