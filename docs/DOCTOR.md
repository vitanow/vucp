# vucp doctor

`vucp doctor` checks workspace health and instruction smells.

```bash
python cli/vucp_cli_mvp.py doctor .
python cli/vucp_cli_mvp.py doctor . --json
```

It checks for:

- missing required VUCP files;
- missing `.gitignore` / `.vucpignore`;
- stale or empty `CURRENT.md` status;
- overlong instruction files;
- over-strict startup language;
- too many cross-project patterns;
- candidate memories ready for Dream Pass.

This is the first practical value layer above the spec.
