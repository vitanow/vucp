> **Superseded, non-normative.** Kept for history only. The normative spec is [`spec/VUCP_SPEC_v0.4.1_FINAL.md`](../VUCP_SPEC_v0.4.1_FINAL.md).

# VUCP_SPEC_v0.4.md

# VUCP — Living Workspace Protocol  
## Vitanow Unified Context Protocol v0.4

**Status:** Draft Specification  
**Version:** 0.4  
**Author:** Zahari Georgiev Vitanov / Vitanow OPS  
**Date:** 2026-06-22  
**License:** MIT after repository creation

---

## 0. One-Line Definition

**VUCP is a filesystem-native protocol for making human-AI work inspectable, repeatable, portable, reviewable, and safer.**

A VUCP workspace turns a normal project folder into a living working environment where knowledge is stored as readable files, workflows are defined as stages, context is loaded intentionally, every run leaves a trace, errors become future memory, and humans and agents share the same source of truth.

---

## 1. Why VUCP Exists

AI systems often fail not because the model is weak, but because the context is chaotic.

Common problems:

- project knowledge is scattered across chats, docs, folders, tools, and memory;
- agents receive too much irrelevant context or too little critical context;
- outputs are not reproducible;
- human review is informal and gets lost;
- workflows are buried inside prompts instead of visible structures;
- errors repeat because the system does not remember them;
- teams cannot see why decisions were made;
- switching models or platforms breaks continuity.

VUCP exists to solve this with a simple principle:

> If the work matters, its context, process, memory, and safety rules must be visible as files.

---

## 2. Core Formula

```text
VUCP =
ICM-style Stage Engine
+ OKF-compatible Knowledge Bundle
+ Manifest Routing
+ Delta Memory
+ Review Gates
+ Safeguards
+ Reproducible Runs
+ Progressive Tooling
```

In simpler language:

```text
ICM moves the work.
OKF carries the knowledge.
MANIFEST routes the process.
Delta Memory remembers the experience.
Safeguards protect the system.
Review Gates keep humans in control.
```

---

## 3. Design Principles

1. Files are the control surface.
2. Markdown is the human interface.
3. YAML is the machine contract.
4. Knowledge, workflow, memory, and safety are separate layers.
5. Every stage has a contract.
6. Every run leaves a trace.
7. Every error becomes future context.
8. Every important decision records its reason.
9. Knowledge updates are proposed before promotion.
10. Complexity must be progressive.

---

## 4. Workspace Levels

### Level 1 — Simple

```text
my_project/
  START.md
  CURRENT.md
  IDEAS.md
  DECISIONS.md
  LOG.md
  files/
```

### Level 2 — Standard

```text
project_root/
  START.md
  WORKSPACE.md
  CURRENT.md
  AGENTS.md
  MANIFEST.yaml
  SCHEMA.md
  SAFEGUARDS.md
  DECISIONS.md
  .vucpignore

  _inbox/
  _knowledge/
    index.md
  _delta/
    LOG.md
    LEARNINGS.md
    ERRORS.md
  _runs/
  _proposals/
  _verification/
  _publish/
  _archive/

  stages/
    research/
      CONTEXT.md
      input/
      output/
    drafting/
      CONTEXT.md
      input/
      output/
    review/
      CONTEXT.md
      input/
      output/
```

### Level 3 — Pro

Pro workspaces may include `_shared/`, `_bridges/`, `_scripts/`, `_knowledge_history/`, and multiple workflows under `workflows/`.

---

## 5. Required Root Files

- `START.md` — human entry point.
- `WORKSPACE.md` — project identity and boundaries.
- `CURRENT.md` — single source of current truth.
- `AGENTS.md` — agent behavior contract.
- `MANIFEST.yaml` — declarative routing map.
- `SCHEMA.md` — naming, types, and conventions.
- `SAFEGUARDS.md` — safety control plane.
- `DECISIONS.md` — decision log.
- `.vucpignore` — AI/tool context ignore file.

---

## 6. Required System Folders

- `_inbox/` — raw capture zone.
- `_knowledge/` — OKF-compatible domain knowledge.
- `_delta/` — operational memory.
- `_runs/` — standard and milestone run records.
- `_proposals/` — proposed changes before promotion.
- `_verification/` — checklists, tests, rollback notes.
- `_publish/` — final outputs.
- `_archive/` — old/deprecated material.

---

## 7. Stage Contract

Each stage must contain:

```text
CONTEXT.md
input/
output/
```

`CONTEXT.md` defines purpose, required context, allowed actions, forbidden actions, process, outputs, verification, review gate, and delta update rules.

---

## 8. Knowledge File Format

Knowledge files are Markdown with YAML frontmatter.

VUCP-specific fields should live under the `vucp:` namespace:

```yaml
vucp:
  stage_triggers: [drafting, review]
  load_policy: required
  confidence: high
```

---

## 9. Review Gates

If `requires_review: true`, the agent must stop after producing output. Allowed review states:

- pending
- approved
- approved_with_changes
- rejected
- blocked

---

## 10. What VUCP Is Not

VUCP is not an agent framework, vector database, prompt library, task manager, cloud platform, replacement for Git, replacement for CI/CD, or replacement for human judgment.

VUCP can connect to those tools, but it should not depend on them.

---

## 11. Final Statement

A project folder can become a living workspace when its knowledge, process, memory, review, and safety rules are visible.

The beginner sees a clean folder and knows where to start.

The professional sees an auditable, reproducible, model-agnostic operating environment.

The AI agent sees structured context, clear boundaries, and a reliable path to action.

**Every project starts as a folder. VUCP makes the folder think.**
