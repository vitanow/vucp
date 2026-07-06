# Demo: Research to Brief

This folder is a **completed example workspace** showing VUCP in action.

Do not copy this folder as your starting point.

Use it to understand how artifacts move through a VUCP workflow:

1. raw material begins in `_inbox/`;
2. `stages/research/output/findings.md` is produced;
3. `stages/drafting/output/draft.md` is produced;
4. `stages/review/output/review_log.md` records the review;
5. `_delta/LOG.md` captures chronological history;
6. `_runs/` preserves reproducible run records.

To start a new project, copy `template-standard/` or run:

```bash
python cli/vucp_cli_mvp.py init my-project
```
