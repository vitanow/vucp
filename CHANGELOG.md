# Changelog

## Unreleased - fix/patterns-filter-and-audit-example

### Fixed

- `patterns --tags` now actually filters: only patterns matching at least one tag are returned; when nothing matches, the CLI prints `No patterns match tags: ...` and returns an empty list (exit 0).
- Frontmatter parser now reads YAML block lists (`tags:` followed by `- item` lines). Previously such tags were read as empty, so tag matching never worked.
- `autopilot audit` no longer counts the documented schema/example entry in `_delta/AUTOPILOT_LOG.md` (placeholders like `read|write|...`, the `## Schema` section, or `example: true`).
- `autopilot audit` now reports `current_mode` read from `AUTOPILOT.md`.

### Changed

- Defined `patterns --tags` semantics: OR across tags, case-insensitive, whitespace-trimmed, empty entries ignored, duplicates removed. Results ranked by number of matched tags, then score; JSON includes `matched_tags`. An explicit `--tags ""` means no filter (previously it silently fell back to `user_context`). Documented in `patterns --help`, README, and `docs/CROSS_PROJECT_PATTERNS.md`.

### Added

- `tests/test_cli.py` pytest suite (smoke tests for init/lint/doctor/export plus regression tests for both fixes).
- `requirements-dev.txt` with pytest; CI runs the test suite.


## 0.5-alpha-9.1 — Launch-clean Assisted Autopilot

### Fixed

- Synchronized README status and CLI commands.
- Added `autopilot` to CLI help and examples.
- Fixed invalid Autopilot mode error handling.
- Fixed malformed `templates/standard/AUTOPILOT.md`.
- Added Autopilot support to `templates/web-dev/`.
- Added `_attention/` dashboard files to standard and web-dev templates.
- `init` now creates `AUTOPILOT.md`, `_attention/`, and `_delta/AUTOPILOT_LOG.md`.
- `doctor` now warns when Autopilot or attention dashboard files are missing.
- `autopilot audit` now reads structured Autopilot log entries instead of naive keyword matches.
- Removed legacy duplicate `template-standard/` folder.

### Added

- `docs/LOW_FRICTION_PROFESSIONAL_MODE.md`
- `docs/AUTOPILOT_LOG_SCHEMA.md`

### Positioning

VUCP is now ready to launch as a portable AI workspace format with AI-guided onboarding, semantic links, cross-project patterns, and Assisted Autopilot.


## v0.5-alpha-9 — 2026-06-28 (GPT merge + enhancements)

### Merged from ChatGPT alpha-7 parallel build

- `docs/SEMANTIC_ALIASES_AND_LINKS.md` — standalone specification for
  semantic aliases and cross-reference links. GPT's version was cleaner
  than our distributed approach. Enhanced with usage examples for
  index.md and LEARNINGS.md, and relationship to semantic memory tools.

- `templates/web-dev/_knowledge/patterns/rollback-first-deployment.md` —
  live example of the semantic_aliases + cross_references format in action.
  Added to templates/web-dev/, templates/standard/, and template-standard/.
  Includes confirmed pattern with 6 evidence points and complete rule set.

- `_proposals/knowledge_updates/dream_pass_report.md` — structured output
  template for Dream Pass results. Agent fills this after each pass.
  Includes promotion checklist for cross-project pattern graduation.
  Added to templates/standard/ and template-standard/.

- `docs/AI_ONBOARDING_PATTERN.md` — meta-document explaining the
  `*_SETUP_GUIDE.ai.md` pattern: design rules, autonomous mode,
  extension to marketplace products.

- `VUCP_SETUP_GUIDE.ai.md` — added Step 7b: semantic memory tool
  positioning. If the user mentions Cognee, Mem0, Zep, or Obsidian,
  the agent explains complementarity, not competition.

- `docs/AI_SETUP_GUIDE.md` — converted from duplicate to canonical
  reference. Points to `VUCP_SETUP_GUIDE.ai.md` as source of truth.

- `.github/ISSUE_TEMPLATE/` — bug_report.md and feature_request.md
  added for GitHub community contributions.

### Not merged (GPT alpha-7 missing features we have)

- Autopilot Layer (AUTOPILOT.md, vucp autopilot CLI) — not in GPT build
- patterns --tags YAML list fix — not in GPT build
- Build artifact cleanup — GPT added a new ALPHA_7_AUDIT.json to root
- semantic_aliases in template index.md — GPT had doc but not template field
- cross_references in LEARNINGS.md template — GPT had doc but not template

## v0.5-alpha-8 — 2026-06-28 (Autopilot Layer)

### Added

- `AUTOPILOT.md` — workspace self-regulation config. Declares mode
  (SILENT / SURFACE / GUIDED), interrupt rules, and Attention List format.
  Added to `template-standard/` and `templates/standard/`.

- `VUCP_SETUP_GUIDE.ai.md` — AI-first onboarding wizard. Designed to be
  given directly to an AI agent, which then guides the human through
  workspace setup. One step at a time. Human interaction optional.
  Inspired by the Cognee onboarding pattern.

- `docs/AUTOPILOT.md` — full specification of the Autopilot layer:
  three modes, interrupt rules, Attention List format, audit trail,
  design principles.

- `semantic_aliases:` field in `_knowledge/index.md` template — allows
  agents to match what humans ask to what knowledge files contain,
  without exact keyword matching. Aliases are written as problem
  descriptions, not topic names.

- `cross_references:` field in `LEARNINGS.md` template — manual graph
  connections between learnings, errors, and knowledge files. Enables
  Dream Pass to follow connections between related entries.

- `AGENTS.md` — Autopilot section added. Agents now read AUTOPILOT.md
  during Full Startup and adjust interaction behavior accordingly.
  Attention List format specified. Silent exceptions documented.

- `SCHEMA.md` — Autopilot mode values, interrupt rule triggers, and new
  file type values (`autopilot`, `ai-guide`) added.

- **CLI: `vucp autopilot`** — new command with three subcommands:
  - `vucp autopilot status` — show current mode
  - `vucp autopilot set --mode GUIDED` — change mode from CLI
  - `vucp autopilot audit` — view autonomous agent actions from LOG.md

### Design note

Autopilot resolves the professional/non-professional paradox:
the full protocol operates at depth, but the human sees only
what requires their judgment — pre-framed, pre-recommended,
requiring the minimum possible response.

The Attention List is the modern equivalent of a wizard:
the system does the work, then presents decisions that genuinely
need a human — already solved, needing only a yes.

## v0.5-alpha-7 — 2026-06-28 (bugfix)

### Fixed

- **CLI: `doctor` GITIGNORE_MISSING false positive** — doctor now checks for
  `.gitignore` in the workspace root, parent, and grandparent directories.
  Templates inside a repo with a root-level `.gitignore` no longer trigger
  a spurious warning.

- **CLI: `vucp patterns --tags` returned 0 results** — `pattern_score()` only
  handled string values for `tags` and `applies_to` fields. Pattern files use
  YAML lists. Fixed: both list and string formats now parsed correctly.

- **Typo in `AGENTS.md`** — "may suggest one may suggest one after 5+ runs"
  corrected to "may suggest one after 5+ runs". Fixed across all template variants.

- **Duplicate `## Context Loading Order` section in `WORKSPACE.md`** — two
  conflicting versions of the loading order existed in the same file (lines 32
  and 42). Removed the older version without `~/.vucp-user/` paths. One
  canonical, correct version remains.

- **Build/test JSON artifacts removed from repo root** — `BUILD_SUMMARY_ALPHA_3/4/5.json`,
  `TEST_RESULTS_*.json`, `BRAND_READY_AUDIT.json` deleted from tracked files.
  `.gitignore` updated with `BUILD_SUMMARY*.json` and `TEST_RESULTS*.json` patterns
  to prevent future commits.

- **`.gitignore` added to all template folders** — `templates/standard/`,
  `templates/web-dev/`, `template-standard/` now each contain a `.gitignore`
  so users who copy a template into a new standalone project are protected
  immediately. `vucp doctor` no longer warns on these workspaces.

# Changelog


## 0.5-alpha-6 — Brand-ready Public Launch

### Added

- Added clear creator attribution: **Zahari Georgiev Vitanov / Vitanow OPS**.
- Added `docs/ABOUT_CREATOR.md`.
- Added `AUTHORS.md`.
- Added `CITATION.cff`.
- Added `docs/BRAND_POSITIONING.md`.
- Rewrote `docs/LAUNCH_POSTS.md` with creator-aware launch copy.
- Updated README with creator block, audience section, current status, and synchronized CLI commands.

### Fixed

- Synchronized release wording to `0.5-alpha-6`.
- Kept Core protocol version as `0.4.1`.
- Clarified that VUCP promotes both the project and its creator.


## v0.5-alpha-5 — Launch-ready Tooling Layer

### Added

- Added `vucp doctor` for workspace health and instruction smell detection.
- Added `vucp export` for AGENTS.md / Codex / Claude / Cursor / Windsurf adapters.
- Added `vucp dream` for manual Dream Pass proposals.
- Added `vucp patterns` for selective cross-project pattern selection.
- Added launch docs: competitive positioning, adapters, doctor, GitHub checklist, launch posts.
- Added GitHub Actions workflow for VUCP template validation.
- Repositioned README around “portable AI workspace format.”

### Rule

VUCP is a source-of-truth workspace format that exports into existing agent ecosystems instead of competing with them.



## v0.5-alpha-4 — Cross-Project Pattern Layer

### Added

- Added optional `templates/user/_cross_project_patterns/`.
- Added `docs/CROSS_PROJECT_PATTERNS.md`.
- Added example confirmed patterns:
  - `cli-help-contract`
  - `rollback-first-deployment`
  - `context-inflation`
  - `demo-before-pitch`
- Added cross-project pattern policy fields to template `WORKSPACE.md`.
- Added selective loading rules to template `AGENTS.md`.
- Added cross-project pattern schema to template `SCHEMA.md`.

### Rule

Cross-project patterns are distilled reusable lessons, not full project memory dumps.

Agents may load only a small number of matching confirmed patterns during Full Startup.


## v0.5-alpha-3 — 2026-06-27

### Fixed (based on DeepSeek architecture review)

- `USER_CORE.md` and `_user_contexts/` moved from repository root to `templates/user/`.
  These are templates only — not active identity files. Filling them in and committing
  them to a public repository would be a privacy risk.

- Added `PRIVACY NOTE` banner to `USER_CORE.md` template with instructions
  to copy to `~/.vucp-user/` before filling in.

- `templates/user/README.md` added with four-step setup instructions and
  explanation of the four-layer context model.

- `templates/web-dev/WORKSPACE.md` — added `user_context: "software"` field.

- `templates/web-dev/AGENTS.md` — added Light Startup / Full Startup model.
  Replaced strict "do not write a single line before 5 files loaded" with
  context-appropriate startup escalation.

- `template-standard/AGENTS.md` — replaced strict startup with Light/Full model.
  USER_CORE and user_context loading marked as *(optional)* since they live outside
  the project workspace.

- `template-standard/WORKSPACE.md` — `user_context` field now marked as optional.
  Context loading order updated to reflect `~/.vucp-user/` location.

- Root `.vucpignore` added. Includes `USER_CORE.private.md` and
  `_user_contexts/private/` as protected entries.

- `template-standard/SCHEMA.md` — added Memory Layer Clarity table
  defining which layer answers which question, preventing duplicate logging.

### Positioning clarified

- User Context Layer is an **optional v0.5 extension**, not a Core v0.4.1 requirement.
- Confidence Memory is a **recommended v0.5 extension**.
- Dream Pass is a **recommended maintenance ritual**, not an automated system.
- VUCP Core v0.4.1 remains locked and unchanged.

## v0.5-alpha-2 — 2026-06-27

### Added

- `USER_CORE.md` — universal user identity file, loaded at the start of every session
  regardless of project domain. Describes who the owner is, how they think,
  how they want feedback, and what they never want from AI.

- `_user_contexts/` folder — domain-specific behavior files, one per domain.
  Each project declares its domain in `WORKSPACE.md` via `user_context: <domain>`.
  Five starter contexts included: `software`, `physics`, `business`, `creative`, `personal`.

- Confidence scoring in `_delta/ERRORS.md` — each error entry now carries
  `confidence` (0.0–1.0) and `occurrence_count`. Errors above 0.8 confidence
  are treated as hard rules by the agent.

- Confidence scoring in `_delta/LEARNINGS.md` — each learning entry now carries
  `confidence`, `validation_count`, and `status` (`candidate` / `confirmed` / `deprecated`).

- Dream Pass protocol — documented in `AGENTS.md`. A weekly maintenance pass
  that promotes confirmed patterns, deprecates stale ones, merges overlaps,
  and prunes noise from ERRORS.md and LEARNINGS.md.

- `user_context` field in `template-standard/WORKSPACE.md` frontmatter.

- Context loading order documented in `template-standard/WORKSPACE.md`
  and `template-standard/AGENTS.md`.

- Updated `SCHEMA.md` with new type values: user-core, user-context,
  confidence score convention, and learning/error status values.

### Still intentionally deferred

- vucp init --template flag (CLI does not yet scaffold user context files)
- Automated Dream Pass trigger in CLI
- Hub / federation features
- v0.5 HIL contracts

# Changelog

## v0.5-alpha-patched — Pre-GitHub Cleanup

### Fixed

- Replaced Bansko-specific demo seed with a generic coffee subscription example.
- Updated demo outputs, logs, learnings, and error notes to match the generic example.
- Fixed `project:` in `demo-research-to-brief/MANIFEST.yaml`.
- Added `demo-research-to-brief/README.md`.
- Added `requirements.txt` with optional but recommended `pyyaml>=6.0`.
- Clarified that PyYAML is optional but improves full MANIFEST.yaml compatibility.
- Added missing `_runs/`, `_publish/`, and `_archive/` folders to the SaaS MVP Launch Kit workspace.
- Patched CLI lint behavior to accept semantic and numbered stage names such as `01-problem-validation`.
- Added basic `CONTEXT.md` frontmatter checks for `stage`, `type`, `review_required`, and `risk_level`.

### Still intentionally deferred

- `vucp wizard`
- `vucp context load`
- `vucp sync-state`
- `vucp doctor`
- VUCP Hub
- Marketplace runtime
- Human Interface Layer dashboard
