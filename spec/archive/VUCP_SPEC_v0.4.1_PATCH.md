> **Superseded, non-normative.** Kept for history only. The normative spec is [`spec/VUCP_SPEC_v0.4.1_FINAL.md`](../VUCP_SPEC_v0.4.1_FINAL.md).

# VUCP_SPEC_v0.4.1_PATCH.md

## VUCP v0.4.1 Stabilization Patch

**Status:** Draft Patch  
**Applies to:** VUCP_SPEC_v0.4.md  
**Purpose:** Reduce context inflation, prevent Git pollution, clarify naming conventions, and stabilize workspace state synchronization.

---

## 1. `.vucpignore`

`.vucpignore` defines files and folders that VUCP agents and CLI tools should ignore by default.

It works like `.gitignore`, but for AI context loading and workspace scanning.

Agents must respect `.vucpignore` unless the human explicitly instructs otherwise.

---

## 2. `.vucp/`

`.vucp/` is the local VUCP runtime folder.

Recommended structure:

```text
.vucp/
  cache/
    context_hashes.yaml
    knowledge_index_cache.json
  tmp/
  transient_runs/
  state.yaml
```

`.vucp/cache/`, `.vucp/tmp/`, and `.vucp/transient_runs/` should usually be ignored by Git.

---

## 3. Read-if-Changed Rule

Before reading large or repeated context files, a VUCP-compatible tool may check their hash.

If the file has not changed since the last run, the tool may use a cached summary or previously loaded state.

Full files remain the source of truth. Cached summaries are optimization only.

---

## 4. Run Classification

VUCP v0.4.1 defines three run classes:

- `transient` — temporary, exploratory, usually stored under `.vucp/transient_runs/`.
- `standard` — meaningful work that affects the project, stored under `_runs/`.
- `milestone` — high-value or high-risk work with full reproducibility, stored under `_runs/` with optional `snapshot_knowledge/`.

Only milestone runs require full knowledge snapshots.

---

## 5. State Sync Rule

After every approved standard or milestone run:

1. append a summary to `_delta/LOG.md`;
2. update `CURRENT.md`;
3. update the run status in `_runs/<run_id>/RUN.md`;
4. record review status if applicable;
5. propose learnings or errors when relevant.

`CURRENT.md` represents the active operational truth. `_delta/LOG.md` represents history.

---

## 6. Naming Conventions

Root control files use uppercase names:

```text
START.md
WORKSPACE.md
CURRENT.md
AGENTS.md
MANIFEST.yaml
SCHEMA.md
SAFEGUARDS.md
DECISIONS.md
CHANGELOG.md
```

System directories start with underscore:

```text
_inbox/
_knowledge/
_delta/
_runs/
_proposals/
_verification/
_publish/
_archive/
_shared/
_bridges/
_scripts/
_knowledge_history/
```

Stage names should be lowercase kebab-case or snake_case.

---

## 7. Updated Minimal Compliance

A Standard VUCP workspace should include:

```text
START.md
WORKSPACE.md
CURRENT.md
AGENTS.md
MANIFEST.yaml
SCHEMA.md
SAFEGUARDS.md
DECISIONS.md
.vucpignore
_knowledge/index.md
_delta/LOG.md
_delta/LEARNINGS.md
_delta/ERRORS.md
at least one stage with CONTEXT.md
```

---

## 8. Updated CLI Roadmap

Recommended future commands:

```bash
vucp init
vucp wizard
vucp lint
vucp context load
vucp sync-state
vucp graph
vucp index
vucp search
vucp quick
vucp snapshot
vucp rollback
vucp doctor
```

---

## 9. Core Patch Principle

> Context must be intentional, not accidental.

A VUCP agent should not scan everything. It should load only required root context, stage contract, selected knowledge files, relevant delta memory, and explicit inputs.
