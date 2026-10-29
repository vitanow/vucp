# VUCP Roadmap

Status as of 0.5.0a10 (0.5-alpha-9.2). Only future work is listed here; finished work is in `CHANGELOG.md`.

## Done (for reference)

- Core spec v0.4.1 (normative), standard, web-dev and Lite templates, demo workspace.
- CLI: `init` (full and `--lite`), `upgrade`, `lint`, `doctor`, `graph`, `export`, `patterns`, `dream`, `autopilot`.
- Test suite and CI on Python 3.9/3.11/3.13; installable `vucp` package.
- 9.2 hardening and docs cleanup.

## Next: benchmark

- Measure whether VUCP helps: same tasks with and without a VUCP workspace (Lite and full), tracking tokens loaded, task success, repeated errors, and human interruptions.
- Publish the method and raw results in the repo.

## v0.6

- CLI modularization (split `cli/vucp_cli_mvp.py` into a package).
- `vucp doctor --fix` for safe automatic repairs.
- `vucp export --install` for direct AGENTS.md / CLAUDE.md installation.
- `vucp init --template web-dev`.
- `vucp context load`, `vucp snapshot`, `vucp rollback`.
- Better cross-project pattern scoring; Dream Pass approval workflow.

## Later

- `vucp wizard`, multilingual template generation.
- VUCP Hub, bridges, Human Interface Layer, agent orchestration runtime.
