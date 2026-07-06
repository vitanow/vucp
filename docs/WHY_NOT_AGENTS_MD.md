# Why not just AGENTS.md?

`AGENTS.md` is useful and VUCP supports it.

But `AGENTS.md` is mostly an instruction file.

VUCP is a workspace format.

## Difference

| Need | AGENTS.md | VUCP |
|---|---|---|
| Agent instructions | Yes | Yes |
| Current state | Usually manual | `CURRENT.md` |
| Workflow stages | No standard | `stages/*/CONTEXT.md` |
| Review gates | No standard | `review_required`, `risk_level`, `SAFEGUARDS.md` |
| Run trace | No standard | `_runs/` |
| Learning from errors | No standard | `_delta/ERRORS.md` |
| Reusable project patterns | No standard | `_cross_project_patterns/` |
| Export to tools | No standard | `vucp export` |
| Health diagnosis | No standard | `vucp doctor` |

## VUCP does not replace AGENTS.md

VUCP can generate AGENTS.md-compatible output:

```bash
python cli/vucp_cli_mvp.py export agents-md .
python cli/vucp_cli_mvp.py export codex .
```

This makes VUCP the source of truth while existing agents keep working.
