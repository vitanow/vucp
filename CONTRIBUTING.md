# Contributing to VUCP

Thank you for considering a contribution to VUCP.

VUCP is a plain-text protocol and reference CLI for repeatable human-AI project work. Contributions should keep the format portable, inspectable, and safe by default.

## Good first contributions

- Documentation fixes and clearer examples.
- Template improvements that preserve backward compatibility.
- CLI lint, doctor, export, graph, or autopilot improvements.
- Additional adapter documentation for AI coding tools.
- Reproducible bug reports with command output.

## Development checks

Run these before opening a pull request:

```bash
python cli/vucp_cli_mvp.py --version
python cli/vucp_cli_mvp.py lint templates/standard --json
python cli/vucp_cli_mvp.py lint templates/web-dev --json
python cli/vucp_cli_mvp.py doctor templates/standard --json
python cli/vucp_cli_mvp.py export claude-md templates/standard --json
```

## Compatibility expectations

- Keep existing VUCP workspaces readable when possible.
- Document any schema or template change in `CHANGELOG.md`.
- Prefer plain text, Markdown, and YAML over tool-specific storage.
- Do not add secrets, private user context, generated run caches, or local environment files.

## Pull request notes

Please include:

- what changed;
- why it changed;
- how it was tested;
- any migration or compatibility impact.
