# Tool Adapters

VUCP should meet users where they already work.

The CLI can generate adapter files for existing AI tools:

```bash
python cli/vucp_cli_mvp.py export agents-md .
python cli/vucp_cli_mvp.py export codex .
python cli/vucp_cli_mvp.py export claude-md .
python cli/vucp_cli_mvp.py export cursor-rules .
python cli/vucp_cli_mvp.py export windsurf-rules .
```

Generated files are placed under:

```text
_publish/adapters/
```

## Principle

Do not maintain five different instruction systems manually.

Maintain VUCP as source of truth, then export adapters.
