# VUCP Lite

Lite is a 3-file VUCP workspace for people who want the core value of VUCP
without the full folder layout.

Why: context inflation. An agent that reads every VUCP file burns context;
an agent that reads none makes the format useless. Lite keeps only what an
agent should read at the start of every session.

## The 3 files

| File | Purpose | Who writes it |
|---|---|---|
| `AGENTS.md` | How agents behave, session start/end routine, autonomy policy (SURFACE by default) | Human |
| `CURRENT.md` | Goal, state, next step, "Needs human attention" | Agent and human |
| `LEARNINGS.md` | Errors and lessons, append-only, with `status: candidate / confirmed / obsolete` | Agent, reviewed by human |

Why these three:

- `AGENTS.md` is already the cross-tool standard most agents read automatically.
  It merges VUCP's AGENTS.md, SAFEGUARDS.md and AUTOPILOT.md.
- `CURRENT.md` is VUCP's most useful idea: visible state and the next step.
  It also replaces the `_attention/` dashboard.
- `LEARNINGS.md` merges `_delta/ERRORS.md` and `_delta/LEARNINGS.md`: the memory
  that stops agents repeating mistakes.

Not included in Lite: stages, `_runs/` traces, `_knowledge/`, `MANIFEST.yaml`,
cross-project patterns, the Autopilot log. Use full mode when you need them.

## Honest limits

The autonomy policy in `AGENTS.md` is an instruction to the model, not
enforcement. Nothing in VUCP blocks an action. For real limits, use your
tool's permission settings (sandbox, allow/deny lists, hooks).

## Token budget

The template is about 470 tokens in total (cl100k_base: AGENTS.md 291,
CURRENT.md 84, LEARNINGS.md 94). lint and doctor warn when any Lite file
grows beyond 8000 characters (`LITE_FILE_TOO_LONG`).

## CLI

```bash
python cli/vucp_cli_mvp.py init my-project --lite --project "My Project" --owner "Me"
python cli/vucp_cli_mvp.py lint my-project      # reports mode: lite
python cli/vucp_cli_mvp.py doctor my-project
python cli/vucp_cli_mvp.py export claude-md my-project
python cli/vucp_cli_mvp.py upgrade my-project --dry-run
python cli/vucp_cli_mvp.py upgrade my-project
```

Detection: a workspace is Lite when `MANIFEST.yaml` is absent and `AGENTS.md`
has `vucp_mode: lite` in its frontmatter (or root `LEARNINGS.md` and
`CURRENT.md` exist). Once `MANIFEST.yaml` exists, full mode wins.

Export writes to `_publish/adapters/` like full mode. Use `--output CLAUDE.md`
to write to the workspace root instead.

## Upgrade to full mode

`vucp upgrade` is non-destructive: it only creates missing full-mode files and
folders. `AGENTS.md` and `CURRENT.md` are kept unchanged (the Lite AGENTS.md
stays as is; merge in the full template by hand if you want it). `LEARNINGS.md`
is copied to `_delta/LEARNINGS.md` and the original is left in place, so you
decide when to delete it.
