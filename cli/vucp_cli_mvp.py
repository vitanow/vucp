#!/usr/bin/env python3
"""
VUCP CLI MVP v0.5-alpha
Minimal reference CLI for VUCP Core v0.4.1.
Commands: init, lint, graph, doctor, export, dream, patterns, autopilot
Help: --help, -h, help, /?
Exit codes: 0 success, 1 validation failed, 2 invalid arguments, 3 filesystem error
"""
from __future__ import annotations
import argparse, json, os, re, sys
from dataclasses import dataclass, asdict
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

VERSION = "0.5-alpha-9.1"
PROTOCOL_VERSION = "0.4.1"
EXIT_SUCCESS=0; EXIT_VALIDATION_FAILED=1; EXIT_INVALID_ARGUMENTS=2; EXIT_FILESYSTEM_ERROR=3
ROOT_FILES=["START.md","WORKSPACE.md","CURRENT.md","AGENTS.md","MANIFEST.yaml","SCHEMA.md","SAFEGUARDS.md","DECISIONS.md",".vucpignore"]
SYSTEM_DIRS=["_inbox","_knowledge","_delta","_runs","_proposals","_verification","_publish","_archive"]
DELTA_FILES=["_delta/LOG.md","_delta/LEARNINGS.md","_delta/ERRORS.md"]
HELP=f"""
VUCP CLI MVP v{VERSION}

Usage:
  vucp <command> [options]
  python vucp_cli_mvp.py <command> [options]

Commands:
  init    Create a Standard VUCP workspace (--lite: 3-file mode)
  upgrade Upgrade a Lite workspace to full mode (non-destructive)
  lint    Validate a VUCP workspace
  graph    Generate Mermaid workflow graph
  doctor   Diagnose workspace health and instruction smells
  export   Generate AGENTS.md / CLAUDE.md / rules adapters
  dream    Propose a Dream Pass memory cleanup report
  patterns Select relevant cross-project patterns
  autopilot Read/set assisted autopilot mode and audit agent actions

Global help:
  --help, -h, help, /?

Examples:
  python vucp_cli_mvp.py init my-project --project "My Project" --owner "Zahari"
  python vucp_cli_mvp.py lint my-project
  python vucp_cli_mvp.py lint my-project --json
  python vucp_cli_mvp.py graph my-project
  python vucp_cli_mvp.py doctor my-project --json
  python vucp_cli_mvp.py export claude-md my-project
  python vucp_cli_mvp.py dream my-project --write
  python vucp_cli_mvp.py patterns my-project --tags cli,safety --json
  python vucp_cli_mvp.py autopilot status my-project
  python vucp_cli_mvp.py autopilot set my-project --mode SURFACE
  python vucp_cli_mvp.py autopilot audit my-project --json

Exit codes:
  0  success
  1  validation failed
  2  invalid arguments
  3  filesystem error

Dependency notes:
  - PyYAML is optional but recommended for full MANIFEST.yaml compatibility.
  - Without PyYAML, the CLI uses a conservative fallback parser for simple manifests.

Safety notes:
  - init refuses to write into a non-empty folder unless --force is used.
  - lint and doctor do not modify files.
  - graph writes only to _publish/workflow.mmd unless --output is provided.
  - export writes generated adapter files under _publish/ unless --output is provided.
  - dream is read-only unless --write is used.
  - autopilot status/audit are read-only; autopilot set only edits AUTOPILOT.md.
"""

@dataclass
class Issue:
    severity:str
    code:str
    message:str
    path:str=""

def today()->str: return date.today().isoformat()
def out_json(x:dict)->None: print(json.dumps(x,indent=2,ensure_ascii=False))
def norm(p:str)->Path: return Path(p).expanduser().resolve()
def stripq(s:str)->str: return s.strip().strip('"').strip("'")
def slug(s:str)->str:
    v=re.sub(r"[^a-zA-Z0-9._-]+","-",s.strip().lower()).strip("-")
    return v or "unnamed-vucp-project"
def write(path:Path, text:str)->None:
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(text.lstrip(),encoding="utf-8")
def keep(path:Path)->None:
    path.mkdir(parents=True,exist_ok=True)
    k=path/".gitkeep"
    if not k.exists(): k.write_text("",encoding="utf-8")

def try_yaml(path:Path)->Optional[dict]:
    try:
        import yaml # type: ignore
        data=yaml.safe_load(path.read_text(encoding="utf-8"))
        return data if isinstance(data,dict) else None
    except Exception:
        return None

def parse_manifest_fallback(path:Path)->dict:
    text=path.read_text(encoding="utf-8")
    project="unknown"; pipeline=[]; cur=None; in_next=False
    for raw in text.splitlines():
        stripped=raw.strip()
        if not stripped or stripped.startswith("#"): continue
        if re.match(r"^project\s*:",stripped): project=stripq(stripped.split(":",1)[1])
        m=re.match(r"^-\s+id\s*:\s*(.+)$",stripped)
        if m:
            cur={"id":stripq(m.group(1)),"next":{}}; pipeline.append(cur); in_next=False; continue
        if cur is None: continue
        if stripped=="next:": in_next=True; continue
        if in_next:
            n=re.match(r"^([A-Za-z0-9_-]+)\s*:\s*(.+)$",stripped)
            if n: cur.setdefault("next",{})[n.group(1)]=stripq(n.group(2)); continue
            if not raw.startswith((" ","\t")): in_next=False
        for key in ["path","type","agent","risk_level"]:
            m2=re.match(rf"^{key}\s*:\s*(.+)$",stripped)
            if m2: cur[key]=stripq(m2.group(1))
        m3=re.match(r"^requires_review\s*:\s*(.+)$",stripped)
        if m3: cur["requires_review"]=stripq(m3.group(1)).lower()=="true"
    return {"project":project,"pipeline":pipeline}


FRONTMATTER_LIST_FIELDS={"tags","applies_to","does_not_apply_to","source_projects","semantic_aliases","cross_references"}

def extract_frontmatter_fields(path:Path)->Dict[str,str]:
    """Minimal parser for YAML frontmatter in CONTEXT.md."""
    fields={}
    if not path.exists(): return fields
    text=path.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---"): return fields
    parts=text.split("---",2)
    if len(parts)<3: return fields
    last=None
    for raw in parts[1].splitlines():
        line=raw.strip()
        # YAML block list item ("  - value") belongs to the previous key; store comma-joined.
        if line.startswith("- ") and raw[:1] in (" ","\t","-"):
            if last not in FRONTMATTER_LIST_FIELDS: continue  # e.g. inside a block scalar or unknown key
            item=line[2:].strip().strip("\"").strip("'")
            fields[last]=f"{fields[last]}, {item}" if fields[last] else item
            continue
        if not line or line.startswith("#") or ":" not in line: continue
        k,v=line.split(":",1)
        last=k.strip()
        fields[last]=v.strip().strip("\"").strip("'")
    return fields

def is_valid_stage_folder_name(name:str)->bool:
    """Accept semantic or numbered beginner-friendly stage names."""
    return bool(re.match(r"^(?:[0-9]{2}[-_])?[a-z][a-z0-9]*(?:[-_][a-z0-9]+)*$", name))


def load_manifest(root:Path)->dict:
    mf=root/"MANIFEST.yaml"
    if not mf.exists(): return {"project":"missing-manifest","pipeline":[]}
    y=try_yaml(mf)
    if y and isinstance(y.get("pipeline"),list): return y
    return parse_manifest_fallback(mf)

def files(project:str, owner:str, language:str)->Dict[str,str]:
    d=today(); ps=slug(project)
    return {
".vucpignore": """
# Dependencies & Environments
node_modules/
.venv/
venv/
vendor/

# Build & Cache Outputs
dist/
build/
target/
.cache/
__pycache__/
*.pyc

# IDE and Git Metadata
.git/
.idea/
.vscode/

# Archives & Large Material
_archive/
*.zip
*.tar
*.gz
*.7z
*.mp4
*.mov
*.wav
*.mp3
*.psd

# Secrets and Credentials
.env
.env.*
*.key
*.pem
*.p12
secrets/
credentials/

# Local VUCP Runtime
.vucp/cache/
.vucp/tmp/
.vucp/transient_runs/
""",
"START.md": f"""
# START HERE

Welcome to this VUCP-enabled workspace.

## Onboarding Steps

1. Open `CURRENT.md` to see the present objective and blockers.
2. Review `WORKSPACE.md` to understand project boundaries.
3. If you are an AI agent, read `AGENTS.md` and follow your assigned profile.
4. Place raw material in `_inbox/`.
5. Before medium/high/critical work, check `SAFEGUARDS.md`.
6. Use `MANIFEST.yaml` to understand the active workflow.

**Protocol Compliance:** VUCP v{PROTOCOL_VERSION} Standard
""",
"WORKSPACE.md": f"""
---
protocol: VUCP
version: "{PROTOCOL_VERSION}"
project: "{project}"
owner: "{owner}"
language: "{language}"
created: "{d}"
status: "active"
---

# Workspace Identity & Boundaries

## Purpose

<!-- Describe why this project exists and its primary goal. -->

## Scope

<!-- Define what is explicitly included in this project workspace. -->

## Out of Scope

<!-- Define what is strictly excluded to prevent agent scope creep. -->

## Core Pipeline Workflows

- research
- drafting
- review
""",
"CURRENT.md": f"""
# Current Operational State

## Status

active

## Last Completed

Initial workspace setup and configuration under VUCP protocol.

## Current Problem

Project parameters undefined.

## Next Action

Define initial requirements and update `WORKSPACE.md`.

## Blockers

- None

## Do Not Touch

- Production configurations, if applicable.
- Main branch direct code execution. Use branches.

## Last Updated

{d}
""",
"AGENTS.md": """
# Agent Behavioral Contract

## General Execution Rules

1. **Context Principle:** Load only intentional context. Read `CURRENT.md` and the current stage's `CONTEXT.md` before taking action.
2. **Immutable Knowledge:** Never modify `_knowledge/` directly. Propose changes in `_proposals/knowledge_updates/`.
3. **State Sync Requirement:** After a successful standard or milestone execution, log the result in `_delta/LOG.md` and update `CURRENT.md`.
4. **Safety Requirement:** Read `SAFEGUARDS.md` before any medium, high, or critical risk action.
5. **No Silent Scope Expansion:** Do not add new goals, tools, or integrations unless approved.

## Agent Profiles

### researcher
- Gather data, extract source material, build objective facts, list ambiguity.

### writer
- Synthesize inputs into coherent documentation aligned with `_knowledge/brand/voice.md`.

### reviewer
- Audit outputs against `SAFEGUARDS.md`, `SCHEMA.md`, and verification checklists.

### operator
- Propose commands and execution plans. Cannot execute destructive actions without approval.
""",
"MANIFEST.yaml": f"""
version: "{PROTOCOL_VERSION}"
protocol: "VUCP"
project: "{ps}"

entrypoints:
  human: "START.md"
  agent: "AGENTS.md"
  current_state: "CURRENT.md"

pipeline:
  - id: research
    path: "stages/research"
    type: "research"
    agent: "researcher"
    requires_review: true
    risk_level: "low"
    knowledge:
      mode: "auto"
    outputs:
      - "findings.md"
    next:
      approved: "drafting"
      rejected: "research"

  - id: drafting
    path: "stages/drafting"
    type: "synthesis"
    agent: "writer"
    requires_review: true
    risk_level: "medium"
    knowledge:
      include:
        - "_knowledge/brand/voice.md"
    outputs:
      - "draft.md"
    next:
      approved: "review"
      rejected: "drafting"

  - id: review
    path: "stages/review"
    type: "review"
    agent: "reviewer"
    requires_review: false
    risk_level: "low"
    knowledge:
      include:
        - "_knowledge/policies/safety.md"
    outputs:
      - "review_log.md"
""",
"SCHEMA.md": """
# Workspace Schema and Naming Contracts

## Naming Standards
- Root control files must be UPPERCASE.
- System folders must use underscore prefix.
- Pipeline stage folders must use lowercase kebab-case or snake_case.

## Allowed Workspace States
active | paused | completed | blocked

## Review Gate Decisions
pending | approved | approved_with_changes | rejected | blocked

## Risk Levels
low | medium | high | critical

## Run Classes
transient | standard | milestone
""",
"SAFEGUARDS.md": """
# System Safeguards

## Core Directive

Preserve intentional operational safety. No AI agent is permitted to execute irreversible or destructive tasks without human approval in a review gate.

## Never Mutate Without Human Gate Approval

- Credentials, env files, and API configurations.
- Production database schemas or live code deployments.
- Erasure of historical run state in `_runs/`.
- Security, payment, user data, or infrastructure settings.

## Risk Classification Architecture

- **LOW:** Documentation, ideation, analysis inside isolated text folders.
- **MEDIUM:** Code synthesis, script changes with local tests, or structural rewrites.
- **HIGH:** Production-adjacent infrastructure, public releases, system integrations.
- **CRITICAL:** Credentials, destructive actions, payment systems, live databases, security policy.

## Required Before High/Critical Actions

- Risk level.
- Files changed.
- Commands proposed.
- Verification steps.
- Rollback plan.
- Human approval checkpoint.
""",
"DECISIONS.md": f"""
# Architectural & Strategic Decisions

## {d} — Initial Workspace Initialization

**Decision:** Adopt VUCP v{PROTOCOL_VERSION} file system protocol standard.

**Reason:** To ensure visibility, traceability, and reproducibility of the human-AI loop from day one.

**Impact:** Root controls use UPPERCASE names; system folders use underscore prefixes.

**Status:** active
""",
"_knowledge/index.md": """
# Knowledge Index

| Path | Type | Title | Tags | Summary | Stage Triggers |
|---|---|---|---|---|---|
| `_knowledge/brand/voice.md` | policy | Brand Voice | branding, style | Rules for communication tone. | drafting |
| `_knowledge/policies/safety.md` | policy | Safety Protocol | engineering, compliance | Rules for critical executions. | review |
""",
"_knowledge/brand/voice.md": f"""
---
type: policy
title: Brand Voice
description: Communication tone and writing rules for this workspace.
tags: [branding, style, writing]
timestamp: {d}T00:00:00Z
vucp:
  stage_triggers: [drafting, review]
  load_policy: required
  confidence: medium
  owner: "{owner}"
  last_reviewed: {d}
---

# Brand Voice

## Rules
- Be direct.
- Be useful before being clever.
- Prefer concrete examples.
- Avoid empty motivational language.
- Make assumptions explicit.
""",
"_knowledge/policies/safety.md": f"""
---
type: policy
title: Safety Protocol
description: Workspace safety policy for risky or irreversible actions.
tags: [safety, engineering, compliance]
timestamp: {d}T00:00:00Z
vucp:
  stage_triggers: [review]
  load_policy: required
  confidence: high
  owner: "{owner}"
  last_reviewed: {d}
---

# Safety Protocol

## Core Rule

Do not perform irreversible changes without explicit human approval.
""",
"_delta/LOG.md": f"""
# Chronological Operational Log

## {d} | initialization | system | SUCCESS

- Agent: system
- Output: Standard VUCP structure created.
- Review: N/A
- Notes: Workspace ready for operational workflows.
""",
"_delta/LEARNINGS.md": "# Accumulated Workspace Learnings\n\nReusable logic patterns discovered across runs go here.\n",
"_delta/ERRORS.md": "# Documented Workspace Failures & Resolutions\n\nCatalog errors here to update the context of future runs.\n",
"stages/research/CONTEXT.md": """
---
stage: "research"
type: "research"
version: "1.0"
agent: "researcher"
review_required: true
risk_level: "low"
---

# Stage Contract: Research

## Purpose
Collect and organize raw materials from `_inbox/` into `output/findings.md`.

## Required Root Context
- `/CURRENT.md`
- `/_knowledge/index.md`
- `/_delta/ERRORS.md`

## Inputs
- `input/`
- `/_inbox/`

## Allowed Actions
- Scan `_inbox/` and `input/`.
- Produce `output/findings.md`.

## Forbidden Actions
- Touch code files outside this stage folder.
- Execute network calls without explicit task allocation.

## Outputs
- `output/findings.md`
""",
"stages/drafting/CONTEXT.md": """
---
stage: "drafting"
type: "synthesis"
version: "1.0"
agent: "writer"
review_required: true
risk_level: "medium"
---

# Stage Contract: Drafting

## Purpose
Turn approved research findings into a coherent draft.

## Required Root Context
- `/CURRENT.md`
- `/SAFEGUARDS.md`
- `/_knowledge/index.md`
- `/_knowledge/brand/voice.md`
- `/_delta/ERRORS.md`

## Inputs
- `input/findings.md`

## Allowed Actions
- Read approved findings.
- Produce `output/draft.md`.
- Propose knowledge updates in `/_proposals/knowledge_updates/`.

## Forbidden Actions
- Modify `_knowledge/` directly.
- Publish final output without review.

## Outputs
- `output/draft.md`
""",
"stages/review/CONTEXT.md": """
---
stage: "review"
type: "review"
version: "1.0"
agent: "reviewer"
review_required: false
risk_level: "low"
---

# Stage Contract: Review

## Purpose
Audit the draft for correctness, completeness, safety, and alignment.

## Required Root Context
- `/CURRENT.md`
- `/SAFEGUARDS.md`
- `/SCHEMA.md`
- `/_knowledge/index.md`
- `/_knowledge/policies/safety.md`
- `/_delta/ERRORS.md`

## Inputs
- `input/draft.md`

## Allowed Actions
- Review draft.
- Produce `output/review_log.md`.

## Forbidden Actions
- Silently approve incomplete or unsafe output.
- Delete prior run records.

## Outputs
- `output/review_log.md`
""",
    }


def autopilot_files(project:str, owner:str, language:str)->Dict[str,str]:
    return {
        "AUTOPILOT.md": """
---
protocol: VUCP
type: autopilot
version: \"0.4.1\"
mode: SURFACE
owner_approval_required_for:
  - high_risk_changes
  - critical_risk_changes
  - production_writes
  - credential_changes
  - deletion_or_destructive_actions
  - publishing_or_external_communication
  - trusted_memory_promotion
attention_output: \"_attention/ATTENTION.md\"
autopilot_log: \"_delta/AUTOPILOT_LOG.md\"
---
# Assisted Autopilot

## Current mode

**Current mode:** `SURFACE`

## Modes

```yaml
mode: SILENT    # Agent works autonomously. Only interrupts for critical blocks.
mode: SURFACE   # Agent works, then surfaces a short attention list. Recommended.
mode: GUIDED    # Agent asks before each significant step. Maximum control.
```

## Human Attention Levels

```text
auto       → safe to do without interrupting
suggest    → propose a low-risk action
approval   → human approval required
blocked    → cannot proceed without human decision
```
""",
        "_attention/ATTENTION.md": """
# Attention Report

## Summary

No attention items have been generated yet.

## Needs Your Attention

No items yet.

## Lowest-Friction Next Step

Open `CURRENT.md` and confirm the current objective and next action.
""",
        "_attention/ACTIONS.md": """# Actions\n\nNo suggested actions yet.\n""",
        "_attention/RISKS.md": """# Risks\n\nNo active risks recorded yet.\n""",
        "_attention/APPROVALS.md": """# Approvals\n\nNo pending approvals.\n""",
        "_delta/AUTOPILOT_LOG.md": """
# Autopilot Log

Structured log for Assisted Autopilot.

## Schema

```yaml
type: autopilot_action
actor: agent
autopilot_mode: SURFACE
action_class: read|write|suggest|approval_required|blocked
risk_level: low|medium|high|critical
confidence: 0.82
human_approval: not_required|required|granted|denied
summary: \"Short human-readable action summary\"
why_it_matters: \"One sentence explaining relevance\"
```

## Entries

No structured autopilot actions recorded yet.
""",
    }


# --- VUCP Lite: 3-file mode (kept in sync with templates/lite/, see tests) ---
LITE_FILES=["AGENTS.md","CURRENT.md","LEARNINGS.md"]
LITE_FILE_SOFT_LIMIT=8000  # characters; Lite files are meant to stay short
LITE_TEMPLATE={'AGENTS.md': '---\nvucp_mode: lite\nproject: "<PROJECT_NAME>"\nowner: "<OWNER_NAME>"\nautonomy: SURFACE\n---\n# AGENTS.md - <PROJECT_NAME>\n\nInstructions for AI agents working in this project. These are instructions,\nnot enforcement: nothing here technically blocks an action. For real limits,\nuse your tool\'s permission settings (sandbox, allow/deny lists, hooks).\n\n## Start of every session\n\n1. Read `CURRENT.md` (state and next step).\n2. Skim `LEARNINGS.md` before repeating a similar task.\n3. Do not load other files unless the task needs them.\n\n## How to work\n\n- Keep changes small and reversible. Explain what you changed and why.\n- Ask when the goal is ambiguous instead of guessing.\n- Do not invent facts, sources, or test results.\n\n## Autonomy: SURFACE\n\nWork without asking for routine, reversible steps. Stop and ask first for:\n\n- deleting or overwriting data, irreversible changes;\n- production, deploys, payments, publishing, sending messages;\n- credentials, secrets, permissions;\n- editing this file.\n\nOther modes: GUIDED (ask before each significant step),\nSILENT (only stop for the list above).\n\n## End of every session\n\n- Update `CURRENT.md`: what changed, next step, anything needing the human.\n- Append to `LEARNINGS.md` if you hit an error or learned something reusable.\n', 'CURRENT.md': '# CURRENT - <PROJECT_NAME>\n\nLast updated: <YYYY-MM-DD>\n\n## Goal\n\n<One sentence: what this project is trying to achieve right now.>\n\n## State\n\n- <What is done, what is in progress.>\n\n## Next step\n\n- <The single next concrete action.>\n\n## Needs human attention\n\n- <Decisions, approvals, or blockers. Write "None" if empty.>\n', 'LEARNINGS.md': '# LEARNINGS - <PROJECT_NAME>\n\nAppend-only. Add new entries at the bottom; do not rewrite old ones.\nMark an outdated entry with `status: obsolete` instead of deleting it.\n\nEntry format:\n\n```\n## <date> - <short title>\ntype: error | lesson\nstatus: candidate | confirmed | obsolete\nwhat happened: <one or two lines>\nrule: <what to do differently next time>\n```\n\n## Entries\n'}

def lite_files(project:str, owner:str, day:str)->Dict[str,str]:
    out={}
    for rel,txt in LITE_TEMPLATE.items():
        out[rel]=txt.replace("<PROJECT_NAME>",project).replace("<OWNER_NAME>",owner).replace("<YYYY-MM-DD>",day)
    return out

def is_lite(root:Path)->bool:
    # Full mode wins if MANIFEST.yaml exists (e.g. after upgrade).
    if (root/"MANIFEST.yaml").exists(): return False
    if re.search(r"^vucp_mode:\s*lite\s*$", read_text_safe(root/"AGENTS.md"), re.M): return True
    return (root/"LEARNINGS.md").exists() and (root/"CURRENT.md").exists()

def lite_issues(root:Path)->List[dict]:
    issues=[]
    for rel in LITE_FILES:
        p=root/rel
        if not p.exists():
            issues.append(issue_dict("error","REQUIRED_FILE_MISSING",f"Required Lite file missing: {rel}",rel,"Run vucp init --lite or copy it from templates/lite."))
        elif len(read_text_safe(p))>LITE_FILE_SOFT_LIMIT:
            issues.append(issue_dict("warning","LITE_FILE_TOO_LONG",f"{rel} is over {LITE_FILE_SOFT_LIMIT} characters; Lite files should stay short.",rel,"Trim it, or run vucp upgrade to move to full mode."))
    cur=read_text_safe(root/"CURRENT.md")
    if cur and "## Next step" not in cur:
        issues.append(issue_dict("warning","CURRENT_NEXT_STEP_MISSING","CURRENT.md has no '## Next step' section.","CURRENT.md","Add the single next concrete action."))
    return issues

DEFAULT_GITIGNORE="""# VUCP default .gitignore (generated by vucp init)
# Private user context and secrets: never commit these.
USER_CORE.private.md
_user_contexts/private/
.vucp-user/
.env
.env.*
!.env.example
*.key
*.pem
*.p12
*.pfx

# Transient VUCP state
.vucp/cache/
.vucp/tmp/
.vucp/transient_runs/

# OS / editor noise
.DS_Store
Thumbs.db
"""

FULL_DIRS=["_inbox/ideas","_inbox/files","_inbox/notes","_runs","_proposals/knowledge_updates","_proposals/schema_changes","_proposals/workflow_changes","_verification/checklists","_verification/tests","_verification/rollback","_publish","_archive","_attention",".vucp/cache",".vucp/tmp",".vucp/transient_runs","stages/research/input","stages/research/output","stages/drafting/input","stages/drafting/output","stages/review/input","stages/review/output"]

def upgrade(args)->int:
    # Non-destructive Lite -> full upgrade: only creates missing files, never overwrites.
    root=norm(args.path)
    if not root.exists(): print(f"ERROR: workspace path does not exist: {root}",file=sys.stderr); return EXIT_FILESYSTEM_ERROR
    if not is_lite(root): print(f"ERROR: not a VUCP Lite workspace (or already full): {root}",file=sys.stderr); return EXIT_VALIDATION_FAILED
    fm=extract_frontmatter_fields(root/"AGENTS.md")
    project=fm.get("project") or root.name; owner=fm.get("owner") or "<OWNER_NAME>"
    data=files(project,owner,"en"); data.update(autopilot_files(project,owner,"en"))
    if (root/"LEARNINGS.md").exists(): data["_delta/LEARNINGS.md"]=read_text_safe(root/"LEARNINGS.md")
    created=[rel for rel in data if not (root/rel).exists()]
    kept=[rel for rel in data if (root/rel).exists()]
    if not args.dry_run:
        for rel in created: write(root/rel,data[rel])
        for d in FULL_DIRS: keep(root/d)
    payload={"ok":True,"command":"upgrade","path":str(root),"dry_run":bool(args.dry_run),"created":created,"kept":kept}
    if args.json: out_json(payload)
    else:
        print(("Would upgrade" if args.dry_run else "Upgraded")+f" Lite -> full: {root}")
        print(f"Created {len(created)} file(s); kept {len(kept)} existing file(s) unchanged: {', '.join(kept)}")
        print("LEARNINGS.md was copied to _delta/LEARNINGS.md and left in place; delete the root copy when you are ready.")
    return EXIT_SUCCESS

def init(args)->int:
    root=norm(args.path); project=args.project or root.name; owner=args.owner or "<OWNER_NAME>"; lang=args.language or "en"
    try:
        if root.exists() and any(root.iterdir()) and not args.force:
            print(f"ERROR: target folder is not empty: {root}",file=sys.stderr); print("Use --force to write into a non-empty folder.",file=sys.stderr); return EXIT_FILESYSTEM_ERROR
        root.mkdir(parents=True,exist_ok=True)
        if getattr(args,"lite",False):
            data=lite_files(project,owner,today())
            for rel,txt in data.items(): write(root/rel,txt)
            payload={"ok":True,"command":"init","mode":"lite","path":str(root),"project":project,"protocol_version":PROTOCOL_VERSION,"created_files":len(data)}
            if args.json: out_json(payload)
            else:
                print(f"Created VUCP Lite workspace: {root}")
                print("Files: "+", ".join(LITE_FILES))
                print("Next: open CURRENT.md and define the goal and next step.")
            return EXIT_SUCCESS
        data=files(project,owner,lang)
        data.update(autopilot_files(project,owner,lang))
        data[".gitignore"]=DEFAULT_GITIGNORE
        for rel,txt in data.items(): write(root/rel,txt)
        dirs=FULL_DIRS
        for d in dirs: keep(root/d)
        payload={"ok":True,"command":"init","path":str(root),"project":project,"protocol_version":PROTOCOL_VERSION,"created_files":len(data)}
        if args.json: out_json(payload)
        else:
            print(f"Created VUCP workspace: {root}")
            print(f"Project: {project}")
            print("Next: open CURRENT.md and define the first real objective.")
        return EXIT_SUCCESS
    except OSError as e:
        print(f"FILESYSTEM ERROR: {e}",file=sys.stderr); return EXIT_FILESYSTEM_ERROR

def print_lint(args,root:Path,issues:List[Issue],mode:str="full")->int:
    errors=[i for i in issues if i.severity=="error"]; warnings=[i for i in issues if i.severity=="warning"]
    payload={"ok":not errors,"command":"lint","mode":mode,"path":str(root),"errors":len(errors),"warnings":len(warnings),"issues":[asdict(i) for i in issues]}
    if args.json: out_json(payload)
    else:
        print(f"VUCP lint: {root}"+(" (lite)" if mode=="lite" else ""))
        print(("OK" if not errors else "FAILED")+f": {len(errors)} error(s), {len(warnings)} warning(s)")
        for i in issues:
            print(f"{('ERROR' if i.severity=='error' else 'WARN ')} {i.code}"+(f" [{i.path}]" if i.path else "")+f": {i.message}")
    return EXIT_SUCCESS if not errors else EXIT_VALIDATION_FAILED

def lint(args)->int:
    root=norm(args.path); issues=[]
    if not root.exists(): return print_lint(args,root,[Issue("error","ROOT_MISSING","Workspace path does not exist.",str(root))])
    if is_lite(root):
        return print_lint(args,root,[Issue(i["severity"],i["code"],i["message"],i["path"]) for i in lite_issues(root)],mode="lite")
    for rel in ROOT_FILES:
        if not (root/rel).exists(): issues.append(Issue("error","REQUIRED_FILE_MISSING",f"Required root file missing: {rel}",rel))
    for rel in SYSTEM_DIRS:
        if not (root/rel).exists(): issues.append(Issue("error","SYSTEM_DIR_MISSING",f"Required system directory missing: {rel}/",rel))
    for rel in DELTA_FILES:
        if not (root/rel).exists(): issues.append(Issue("error","DELTA_FILE_MISSING",f"Required delta file missing: {rel}",rel))
    if not (root/"_knowledge/index.md").exists(): issues.append(Issue("error","KNOWLEDGE_INDEX_MISSING","Knowledge index missing.","_knowledge/index.md"))
    mf=root/"MANIFEST.yaml"
    if not mf.exists(): issues.append(Issue("error","MANIFEST_MISSING","MANIFEST.yaml missing.","MANIFEST.yaml"))
    else:
        man=load_manifest(root); pipe=man.get("pipeline",[])
        if not pipe: issues.append(Issue("error","MANIFEST_PIPELINE_EMPTY","MANIFEST.yaml has no valid pipeline.","MANIFEST.yaml"))
        seen=set()
        for st in pipe:
            sid=str(st.get("id") or "") if isinstance(st,dict) else ""
            sp=str(st.get("path") or "") if isinstance(st,dict) else ""
            if not sid: issues.append(Issue("error","MANIFEST_STAGE_ID_MISSING","Pipeline stage missing id.","MANIFEST.yaml"))
            elif sid in seen: issues.append(Issue("error","MANIFEST_STAGE_DUPLICATE",f"Duplicate stage id: {sid}","MANIFEST.yaml"))
            else: seen.add(sid)
            if not sp: issues.append(Issue("error","MANIFEST_STAGE_PATH_MISSING",f"Stage {sid or '?'} missing path.","MANIFEST.yaml")); continue
            sd=root/sp
            if not sd.exists(): issues.append(Issue("error","STAGE_PATH_MISSING",f"Stage path does not exist: {sp}",sp))
            cf=sd/"CONTEXT.md"
            if not cf.exists():
                issues.append(Issue("error","STAGE_CONTEXT_MISSING",f"Stage missing CONTEXT.md: {sp}",str(cf)))
            else:
                fm=extract_frontmatter_fields(cf)
                for req in ["stage","type","review_required","risk_level"]:
                    if req not in fm:
                        issues.append(Issue("warning","CONTEXT_FRONTMATTER_FIELD_MISSING",f"CONTEXT.md missing frontmatter field: {req}",str(cf)))
                if "risk_level" in fm and fm["risk_level"].lower() not in ["low","medium","high","critical"]:
                    issues.append(Issue("warning","CONTEXT_RISK_INVALID",f"Invalid risk_level in CONTEXT.md: {fm['risk_level']}",str(cf)))
                if "review_required" in fm and fm["review_required"].lower() not in ["true","false"]:
                    issues.append(Issue("warning","CONTEXT_REVIEW_REQUIRED_INVALID",f"Invalid review_required in CONTEXT.md: {fm['review_required']}",str(cf)))
                if not is_valid_stage_folder_name(sd.name):
                    issues.append(Issue("warning","STAGE_NAME_NONSTANDARD",f"Stage folder name should be lowercase kebab/snake-case, optionally prefixed with 01- or 01_: {sd.name}",str(sd)))
            if not (sd/"input").exists(): issues.append(Issue("warning","STAGE_INPUT_MISSING",f"Stage missing input/ folder: {sp}",str(sd/"input")))
            if not (sd/"output").exists(): issues.append(Issue("warning","STAGE_OUTPUT_MISSING",f"Stage missing output/ folder: {sp}",str(sd/"output")))
            risk=str(st.get("risk_level","")).lower() if isinstance(st,dict) else ""
            if risk in ["high","critical"]:
                txt=(sd/"CONTEXT.md").read_text(encoding="utf-8",errors="ignore") if (sd/"CONTEXT.md").exists() else ""
                if "SAFEGUARDS.md" not in txt: issues.append(Issue("warning","HIGH_RISK_WITHOUT_SAFEGUARDS",f"High/critical risk stage should reference SAFEGUARDS.md: {sid}",str(sd/"CONTEXT.md")))
    runs=root/"_runs"
    if runs.exists() and any(p.is_dir() and "transient" in p.name.lower() for p in runs.iterdir()): issues.append(Issue("warning","TRANSIENT_RUNS_IN_RUNS","Transient-like runs found in _runs/. Use .vucp/transient_runs/ instead.","_runs"))
    return print_lint(args,root,issues)

def mid(s:str)->str:
    v=re.sub(r"[^A-Za-z0-9_]","_",s)
    return ("stage_"+v) if (not v or v[0].isdigit()) else v

def graph(args)->int:
    root=norm(args.path)
    if not root.exists(): print(f"ERROR: workspace path does not exist: {root}",file=sys.stderr); return EXIT_FILESYSTEM_ERROR
    man=load_manifest(root); pipe=man.get("pipeline",[])
    if not pipe: print("ERROR: MANIFEST.yaml has no valid pipeline.",file=sys.stderr); return EXIT_VALIDATION_FAILED
    lines=["flowchart TD"]; ids={}
    for st in pipe:
        sid=str(st.get("id","unknown")); ids[sid]=mid(sid); agent=st.get("agent",""); risk=st.get("risk_level","")
        label=sid+(f"\\nagent: {agent or '-'}\\nrisk: {risk or '-'}" if agent or risk else "")
        lines.append(f'  {ids[sid]}["{label}"]')
    for st in pipe:
        sid=str(st.get("id","unknown")); src=ids.get(sid,mid(sid)); nxt=st.get("next",{})
        if isinstance(nxt,dict) and nxt:
            for decision,target in nxt.items(): lines.append(f'  {src} -->|{decision}| {ids.get(str(target),mid(str(target)))}')
        else: lines.append(f'  {src} --> terminal_{src}(["END"])')
    out=Path(args.output) if args.output else root/"_publish/workflow.mmd"
    if not out.is_absolute(): out=root/out
    out.parent.mkdir(parents=True,exist_ok=True); out.write_text("\n".join(lines)+"\n",encoding="utf-8")
    payload={"ok":True,"command":"graph","path":str(root),"output":str(out),"stages":len(pipe)}
    if args.json: out_json(payload)
    else: print(f"Generated Mermaid graph: {out}")
    return EXIT_SUCCESS


def read_text_safe(path:Path)->str:
    try: return path.read_text(encoding="utf-8",errors="ignore")
    except Exception: return ""

def workspace_frontmatter(root:Path)->Dict[str,str]:
    return extract_frontmatter_fields(root/"WORKSPACE.md")

def issue_dict(severity:str, code:str, message:str, path:str="", suggestion:str="")->dict:
    return {"severity":severity,"code":code,"message":message,"path":path,"suggestion":suggestion}

def find_heading_value(text:str, heading:str)->str:
    lines=text.splitlines()
    for i,l in enumerate(lines):
        if l.strip().lower()==heading.strip().lower():
            for j in range(i+1,min(i+6,len(lines))):
                v=lines[j].strip()
                if v and not v.startswith("#"): return v
    return ""

def scan_instruction_smells(root:Path)->List[dict]:
    issues=[]
    for rel in ["AGENTS.md","CLAUDE.md","CURRENT.md","WORKSPACE.md","SAFЕGUARDS.md","SAFEGUARDS.md"]:
        p=root/rel
        if not p.exists(): continue
        txt=read_text_safe(p)
        if len(txt)>32000:
            issues.append(issue_dict("warning","INSTRUCTION_FILE_TOO_LONG",f"{rel} is over 32KB and may reduce agent adherence.",rel,"Split durable knowledge into _knowledge/ and stage-specific CONTEXT.md."))
        if "Do not write a single line" in txt:
            issues.append(issue_dict("warning","OVERSTRICT_STARTUP",f"{rel} contains an over-strict startup rule.",rel,"Use Light Startup / Full Startup instead of blocking all short answers."))
        if txt.count("MUST") + txt.count("must") > 40:
            issues.append(issue_dict("warning","TOO_MANY_ABSOLUTES",f"{rel} contains many absolute instructions.",rel,"Move operational rules into SAFEGUARDS.md or stage CONTEXT.md."))
    # CURRENT freshness
    cur=root/"CURRENT.md"
    if cur.exists():
        txt=read_text_safe(cur)
        if "## Last Updated" in txt:
            val=find_heading_value(txt,"## Last Updated")
            if not val:
                issues.append(issue_dict("warning","CURRENT_LAST_UPDATED_EMPTY","CURRENT.md has empty Last Updated.","CURRENT.md","Set a concrete date."))
    # Cross project selection safety
    ws=workspace_frontmatter(root)
    try: maxp=int(str(ws.get("max_cross_project_patterns","5")).strip().strip('"'))
    except Exception: maxp=5
    if maxp>5:
        issues.append(issue_dict("warning","TOO_MANY_CROSS_PROJECT_PATTERNS","max_cross_project_patterns is above 5.","WORKSPACE.md","Keep cross-project pattern loading to 3–5 to avoid context inflation."))
    return issues

def doctor(args)->int:
    root=norm(args.path)
    issues=[]
    mode="full"
    if not root.exists():
        issues.append(issue_dict("error","ROOT_MISSING","Workspace path does not exist.",str(root),"Check the path."))
    elif is_lite(root):
        mode="lite"
        issues.extend(lite_issues(root))
        if not any((p/".gitignore").exists() for p in [root, root.parent, root.parent.parent, root.parent.parent.parent]):
            issues.append(issue_dict("info","GITIGNORE_MISSING","No .gitignore found in workspace or parent directories.",".gitignore","If this folder is in git, make sure private notes are not committed."))
        issues.extend(scan_instruction_smells(root))
        lt=read_text_safe(root/"LEARNINGS.md"); lt=lt.split("## Entries",1)[1] if "## Entries" in lt else lt
        cand=len(re.findall(r"^status\s*:\s*candidate\s*$",lt,re.I|re.M))
        if cand: issues.append(issue_dict("info","LEARNING_CANDIDATES",f"Found {cand} candidate learning entries.","LEARNINGS.md","Review them and mark confirmed or obsolete."))
    else:
        for rel in ROOT_FILES:
            if not (root/rel).exists(): issues.append(issue_dict("error","REQUIRED_FILE_MISSING",f"Required root file missing: {rel}",rel,"Run vucp init or copy the missing file from templates/standard."))
        # Check .gitignore in workspace or any parent directory (up to 4 levels)
        _gi_found = any(
            (p / ".gitignore").exists()
            for p in [root, root.parent, root.parent.parent, root.parent.parent.parent]
        )
        if not _gi_found:
            issues.append(issue_dict("warning","GITIGNORE_MISSING",
                ".gitignore is missing in workspace and parent directories.",
                ".gitignore",
                "Add a .gitignore to your repository root to protect private context files."))
        if not (root/".vucpignore").exists(): issues.append(issue_dict("error","VUCPIGNORE_MISSING",".vucpignore is missing.",".vucpignore","Add VUCP context ignore rules."))
        if not (root/"AUTOPILOT.md").exists():
            issues.append(issue_dict("warning","AUTOPILOT_MISSING","AUTOPILOT.md is missing.","AUTOPILOT.md","Copy it from templates/standard or run vucp init for new workspaces."))
        else:
            ap_txt=read_text_safe(root/"AUTOPILOT.md")
            if not re.search(r"mode:\s*(SILENT|SURFACE|GUIDED)", ap_txt, re.I):
                issues.append(issue_dict("warning","AUTOPILOT_MODE_INVALID","AUTOPILOT.md has no valid mode.","AUTOPILOT.md","Use SILENT, SURFACE, or GUIDED."))
        if not (root/"_attention/ATTENTION.md").exists():
            issues.append(issue_dict("warning","ATTENTION_DASHBOARD_MISSING","_attention/ATTENTION.md is missing.","_attention/ATTENTION.md","Add the attention dashboard for low-friction human review."))
        issues.extend(scan_instruction_smells(root))
        # Dream Pass candidates
        cand=0
        for rel in ["_delta/ERRORS.md","_delta/LEARNINGS.md"]:
            t=read_text_safe(root/rel)
            cand += len(re.findall(r"status\s*:\s*candidate",t,re.I))
        if cand:
            issues.append(issue_dict("info","DREAM_PASS_CANDIDATES",f"Found {cand} candidate memory entries.","_delta/","Run: vucp dream . --write"))
    errors=[i for i in issues if i["severity"]=="error"]
    warnings=[i for i in issues if i["severity"]=="warning"]
    payload={"ok":not errors,"command":"doctor","mode":mode,"path":str(root),"errors":len(errors),"warnings":len(warnings),"issues":issues}
    if args.json: out_json(payload)
    else:
        print(f"VUCP doctor: {root}"+(" (lite)" if mode=="lite" else ""))
        print(("OK" if not errors else "FAILED")+f": {len(errors)} error(s), {len(warnings)} warning(s)")
        for i in issues:
            sev=i['severity'].upper().ljust(7)
            print(f"{sev} {i['code']}"+(f" [{i['path']}]" if i.get('path') else "")+f": {i['message']}")
            if i.get('suggestion'): print(f"        -> {i['suggestion']}")
    return EXIT_SUCCESS if not errors else EXIT_VALIDATION_FAILED

def build_adapter_content(root:Path,target:str)->str:
    if is_lite(root): return build_lite_adapter_content(root,target)
    ws=read_text_safe(root/"WORKSPACE.md")
    cur=read_text_safe(root/"CURRENT.md")
    agents=read_text_safe(root/"AGENTS.md")
    safeguards=read_text_safe(root/"SAFEGUARDS.md")
    header={
        "agents-md":"# AGENTS.md\n\nGenerated from VUCP workspace.\n",
        "codex":"# AGENTS.md\n\nGenerated for Codex from VUCP workspace.\n",
        "claude-md":"# CLAUDE.md\n\nGenerated for Claude Code from VUCP workspace.\n",
        "cursor-rules":"# VUCP Cursor Rule\n\nGenerated from VUCP workspace.\n",
        "windsurf-rules":"# VUCP Windsurf Rules\n\nGenerated from VUCP workspace.\n",
    }.get(target,"# VUCP Adapter\n")
    return f'''{header}
## What this is

This file is generated from VUCP. Do not edit this generated file as source of truth.
Edit the VUCP files instead: `WORKSPACE.md`, `CURRENT.md`, `AGENTS.md`, `SAFEGUARDS.md`, stage `CONTEXT.md` files, and `_knowledge/`.

## Current State

{cur[:4000]}

## Workspace

{ws[:4000]}

## Agent Instructions

{agents[:8000]}

## Safeguards

{safeguards[:4000]}

## VUCP Rule

When instructions conflict, prefer this order:

1. explicit human instruction;
2. `SAFEGUARDS.md`;
3. current stage `CONTEXT.md`;
4. `CURRENT.md`;
5. `WORKSPACE.md`;
6. cross-project patterns only when relevant.
'''

def build_lite_adapter_content(root:Path,target:str)->str:
    name="CLAUDE.md" if target=="claude-md" else "AGENTS.md"
    return f'''# {name}

Generated from a VUCP Lite workspace. Source of truth: `AGENTS.md`, `CURRENT.md`, `LEARNINGS.md`.
Edit those files, not this generated one.

## Agent Instructions

{read_text_safe(root/"AGENTS.md")[:8000]}

## Current State

{read_text_safe(root/"CURRENT.md")[:4000]}

## Learnings

{read_text_safe(root/"LEARNINGS.md")[:8000]}
'''

def export_adapter(args)->int:
    root=norm(args.path)
    target=args.target
    if not root.exists(): print(f"ERROR: workspace path does not exist: {root}",file=sys.stderr); return EXIT_FILESYSTEM_ERROR
    default={
        "agents-md": root/"_publish/adapters/AGENTS.generated.md",
        "codex": root/"_publish/adapters/codex/AGENTS.md",
        "claude-md": root/"_publish/adapters/claude/CLAUDE.md",
        "cursor-rules": root/"_publish/adapters/cursor/vucp.mdc",
        "windsurf-rules": root/"_publish/adapters/windsurf/vucp.md",
    }.get(target, root/"_publish/adapters/vucp.md")
    out=Path(args.output) if args.output else default
    if not out.is_absolute(): out=root/out
    out.parent.mkdir(parents=True,exist_ok=True)
    content=build_adapter_content(root,target)
    out.write_text(content,encoding="utf-8")
    payload={"ok":True,"command":"export","target":target,"path":str(root),"output":str(out),"bytes":len(content.encode('utf-8'))}
    if args.json: out_json(payload)
    else: print(f"Generated {target} adapter: {out}")
    return EXIT_SUCCESS

def dream(args)->int:
    root=norm(args.path)
    if not root.exists(): print(f"ERROR: workspace path does not exist: {root}",file=sys.stderr); return EXIT_FILESYSTEM_ERROR
    sections=[]
    for rel in ["_delta/ERRORS.md","_delta/LEARNINGS.md"]:
        t=read_text_safe(root/rel)
        candidates=len(re.findall(r"status\s*:\s*candidate",t,re.I))
        confirmed=len(re.findall(r"status\s*:\s*confirmed",t,re.I))
        sections.append((rel,candidates,confirmed))
    report=["# Dream Pass Proposal", "", f"Workspace: `{root.name}`", "", "## Summary", ""]
    for rel,cand,conf in sections:
        report.append(f"- `{rel}`: {cand} candidate(s), {conf} confirmed pattern(s)")
    report += ["", "## Suggested Review", "", "1. Promote only repeated candidates with evidence.", "2. Deprecate obsolete confirmed rules.", "3. Remove project-specific private details before cross-project promotion.", "4. Do not modify trusted memory without human approval.", "", "## Cross-Project Promotion Check", "", "Promote only if the pattern has `applies_to`, `does_not_apply_to`, `source_projects`, `evidence_count`, and `confidence`.", ""]
    content="\n".join(report)
    out=root/"_proposals/knowledge_updates/dream_pass_report.md"
    if args.write:
        out.parent.mkdir(parents=True,exist_ok=True); out.write_text(content,encoding="utf-8")
    payload={"ok":True,"command":"dream","path":str(root),"write":bool(args.write),"output":str(out) if args.write else None,"summary":[{"path":r,"candidates":c,"confirmed":f} for r,c,f in sections]}
    if args.json: out_json(payload)
    else:
        if args.write: print(f"Wrote Dream Pass proposal: {out}")
        else: print(content)
    return EXIT_SUCCESS

def parse_frontmatter_list(value:str)->List[str]:
    v=value.strip().strip('[]')
    return [x.strip().strip('"').strip("'") for x in v.split(',') if x.strip()]

def pattern_tag_matches(meta:dict, tags:List[str])->int:
    hay=[]
    for k in ["tags","applies_to","source_projects"]:
        val=meta.get(k,"")
        if isinstance(val,list): hay += [str(v) for v in val]
        elif isinstance(val,str): hay += parse_frontmatter_list(val)
    h={x.lower() for x in hay}
    h={x.strip().lower() for x in h}
    return sum(1 for t in tags if t.strip().lower() in h)


def pattern_tag_excluded(meta:dict, tags:List[str])->bool:
    # does_not_apply_to overrides positive matches (case-insensitive, trimmed).
    val=meta.get("does_not_apply_to","")
    items=[str(v) for v in val] if isinstance(val,list) else parse_frontmatter_list(str(val))
    excluded={x.strip().lower() for x in items if x.strip()}
    return any(t.strip().lower() in excluded for t in tags)


def pattern_score(meta:dict, tags:List[str])->int:
    score=0
    hay=[]
    for k in ["tags","applies_to","source_projects"]:
        val=meta.get(k,"")
        if isinstance(val,list):
            hay += [str(v) for v in val]
        elif isinstance(val,str):
            hay += parse_frontmatter_list(val)
    h={x.lower() for x in hay}
    for t in tags:
        if t.lower() in h: score+=2
    if str(meta.get("status","")).lower()=="confirmed": score+=3
    try: score += int(float(str(meta.get("confidence","0")))*2)
    except Exception: pass
    return score



def is_example_entry(item:dict, block:str)->bool:
    # Template schema/example entries use "a|b|c" placeholders or explicit example: true.
    if re.search(r"^\s*example:\s*true\s*$", block, re.I|re.M): return True
    return any("|" in str(item.get(k,"")) for k in ["action_class","risk_level","human_approval"])


def current_autopilot_mode(root:Path)->str:
    ap=root/"AUTOPILOT.md"
    if ap.exists():
        m=re.search(r"mode:\s*(SILENT|SURFACE|GUIDED)",read_text_safe(ap),re.I)
        if m: return m.group(1).upper()
    return "NOT SET"


def extract_autopilot_entries(text:str)->List[dict]:
    entries=[]
    # Ignore the documented schema section; real entries live under "## Entries".
    m=re.search(r"^##\s+Entries\s*$", text, re.M)
    if m and re.search(r"^##\s+Schema\s*$", text[:m.start()], re.M): text=text[m.end():]
    for block in re.split(r"\n---\s*\n", text):
        if "autopilot_action" not in block and "action_class:" not in block:
            continue
        item={}
        for raw in block.splitlines():
            line=raw.strip()
            if not line or line.startswith("#") or ":" not in line:
                continue
            k,v=line.split(":",1)
            k=k.strip(); v=v.strip().strip('"').strip("'")
            if k in ["type","actor","autopilot_mode","action_class","risk_level","confidence","human_approval","summary","why_it_matters","created_at"]:
                item[k]=v
        if (item.get("type")=="autopilot_action" or item.get("action_class")) and not is_example_entry(item, block):
            entries.append(item)
    return entries


def autopilot_status_error(args, root:Path, ap_file:Path, msg:str)->int:
    payload={"ok":False,"command":"autopilot","subcommand":"status","path":str(root),"mode":"INVALID","file":str(ap_file),"file_exists":True,"error":msg}
    if args.json: out_json(payload)
    print(f"ERROR: {msg}",file=sys.stderr)
    return EXIT_VALIDATION_FAILED

def autopilot(args)->int:
    # Read/set Assisted Autopilot mode and audit structured agent actions.
    root=norm(args.path)
    ap_file=root/"AUTOPILOT.md"

    if args.subcommand=="set":
        if not args.mode:
            print("ERROR: --mode required. Options: SILENT | SURFACE | GUIDED", file=sys.stderr)
            return EXIT_INVALID_ARGUMENTS
        mode=args.mode.upper()
        if mode not in ["SILENT","SURFACE","GUIDED"]:
            print(f"ERROR: invalid mode '{mode}'. Use SILENT, SURFACE, or GUIDED.", file=sys.stderr)
            return EXIT_INVALID_ARGUMENTS
        if ap_file.exists():
            content=ap_file.read_text(encoding="utf-8",errors="ignore")
            content=re.sub(r"mode:\s*(SILENT|SURFACE|GUIDED|\S+)",f"mode: {mode}",content, count=1, flags=re.I)
            content=re.sub(r"\*\*Current mode:\*\*\s*`?(SILENT|SURFACE|GUIDED|\S+)`?", f"**Current mode:** `{mode}`", content, count=1, flags=re.I)
            ap_file.write_text(content,encoding="utf-8")
        else:
            write(ap_file, f'''---
protocol: VUCP
type: autopilot
version: "{PROTOCOL_VERSION}"
mode: {mode}
attention_output: "_attention/ATTENTION.md"
autopilot_log: "_delta/AUTOPILOT_LOG.md"
---
# Assisted Autopilot

## Current mode

**Current mode:** `{mode}`
''')
        payload={"ok":True,"command":"autopilot","subcommand":"set","mode":mode,"file":str(ap_file)}
        if args.json: out_json(payload)
        else: print(f"Autopilot mode set to {mode} in {ap_file}")
        return EXIT_SUCCESS

    if args.subcommand=="audit":
        entries=[]
        for log_file in [root/"_delta/AUTOPILOT_LOG.md", root/"_delta/LOG.md"]:
            if log_file.exists():
                for e in extract_autopilot_entries(read_text_safe(log_file)):
                    e.setdefault("source", str(log_file))
                    entries.append(e)
        payload={"ok":True,"command":"autopilot","subcommand":"audit","path":str(root),"current_mode":current_autopilot_mode(root),"count":len(entries),"entries":entries[:50]}
        if args.json:
            out_json(payload)
        else:
            print(f"Current autopilot mode: {current_autopilot_mode(root)}")
            print(f"Structured autopilot actions: {len(entries)}")
            if not entries:
                print("No structured autopilot actions recorded yet.")
            for e in entries[:20]:
                print(f"- {e.get('action_class','action')} | {e.get('risk_level','risk?')} | {e.get('summary','')}")
        return EXIT_SUCCESS

    mode="NOT SET"
    if ap_file.exists():
        try:
            if not ap_file.is_file(): raise OSError("not a regular file")
            ap_txt=ap_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as e:
            return autopilot_status_error(args, root, ap_file, f"AUTOPILOT.md could not be read ({e.__class__.__name__}: {e}).")
        m=re.search(r"mode:\s*(SILENT|SURFACE|GUIDED)\b",ap_txt,re.I)
        if not m:
            return autopilot_status_error(args, root, ap_file, "AUTOPILOT.md has no valid mode. Use SILENT, SURFACE, or GUIDED (vucp autopilot set <path> --mode SURFACE).")
        mode=m.group(1).upper()
    payload={"ok":True,"command":"autopilot","subcommand":"status","path":str(root),"mode":mode,"file":str(ap_file),"file_exists":ap_file.exists()}
    if args.json: out_json(payload)
    else: print(f"Autopilot mode: {mode} ({'configured' if ap_file.exists() else 'AUTOPILOT.md missing'})")
    return EXIT_SUCCESS

def patterns(args)->int:
    root=norm(args.path)
    ws=workspace_frontmatter(root)
    p_arg=args.patterns or ws.get("cross_project_patterns","")
    # Tag semantics: OR, case-insensitive, trimmed, empty entries ignored, de-duplicated.
    # An explicit --tags "" means no filter; omitted --tags falls back to user_context.
    raw_tags=args.tags if args.tags is not None else ws.get("user_context","")
    tags=list(dict.fromkeys(t.strip().lower() for t in raw_tags.split(',') if t.strip()))
    maxn=int(args.max or ws.get("max_cross_project_patterns","5") or 5)
    candidates=[]
    search_roots=[]
    if p_arg:
        p=Path(p_arg.strip().strip('"')).expanduser()
        if p.name=="index.md": search_roots.append(p.parent)
        else: search_roots.append(p)
    # fallback to repo template library if present
    # Search for cross-project patterns in workspace, parent, and grandparent
    for ancestor in [root, root.parent, root.parent.parent]:
        tr_candidate = ancestor / "templates/user/_cross_project_patterns"
        if tr_candidate.exists() and tr_candidate not in search_roots:
            search_roots.append(tr_candidate)
    seen=set()
    for sr in search_roots:
        if not sr.exists(): continue
        for md in sr.rglob("*.md"):
            if md.name.lower() in ["index.md","readme.md"]: continue
            if md in seen: continue
            seen.add(md)
            meta=extract_frontmatter_fields(md)
            if str(meta.get("status","")).lower()!="confirmed" and not args.include_candidates: continue
            if tags and pattern_tag_excluded(meta,tags): continue
            if tags and pattern_tag_matches(meta,tags)==0: continue
            sc=pattern_score(meta,tags)
            candidates.append({"path":str(md),"matched_tags":pattern_tag_matches(meta,tags),"score":sc,"title":md.stem,"status":meta.get("status",""),"confidence":meta.get("confidence",""),"tags":meta.get("tags",""),"applies_to":meta.get("applies_to","")})
    candidates=sorted(candidates,key=lambda x:(x["matched_tags"],x["score"]),reverse=True)[:maxn]
    payload={"ok":True,"command":"patterns","path":str(root),"tags":tags,"count":len(candidates),"patterns":candidates}
    if args.json: out_json(payload)
    else:
        print(f"Selected {len(candidates)} cross-project pattern(s)")
        if tags and not candidates: print(f"No patterns match tags: {', '.join(tags)}")
        for c in candidates: print(f"- {c['title']} ({c['confidence']}) [{c['path']}]")
    return EXIT_SUCCESS


def cmd_help(c:str)->str:
    if c=="init": return """\nUsage:\n  vucp init <path> [--project NAME] [--owner NAME] [--language bg|en] [--lite] [--force] [--json]\n\nCreates a Standard VUCP workspace.\nWith --lite, creates a 3-file Lite workspace instead: AGENTS.md, CURRENT.md, LEARNINGS.md.\n\nExamples:\n  python vucp_cli_mvp.py init my-project\n  python vucp_cli_mvp.py init my-project --project \"My Project\" --owner \"Zahari\"\n  python vucp_cli_mvp.py init my-project --lite\n\nSafety:\n  Refuses to write into a non-empty folder unless --force is used.\n\nExit codes:\n  0 success\n  2 invalid arguments\n  3 filesystem error\n"""
    if c=="lint": return """\nUsage:\n  vucp lint <path> [--json]\n\nValidates a VUCP workspace structure.\n\nExamples:\n  python vucp_cli_mvp.py lint my-project\n  python vucp_cli_mvp.py lint my-project --json\n\nExit codes:\n  0 success\n  1 validation failed\n  2 invalid arguments\n"""
    if c=="graph": return """\nUsage:\n  vucp graph <path> [--output PATH] [--json]\n\nGenerates Mermaid workflow graph from MANIFEST.yaml.\n\nExamples:\n  python vucp_cli_mvp.py graph my-project\n  python vucp_cli_mvp.py graph my-project --output _publish/workflow.mmd\n\nExit codes:\n  0 success\n  1 validation failed\n  2 invalid arguments\n  3 filesystem error\n"""
    if c=="upgrade": return """
Usage:
  vucp upgrade <path> [--dry-run] [--json]

Upgrades a Lite workspace to the full VUCP layout, non-destructively:
only missing files are created; AGENTS.md and CURRENT.md are kept unchanged.
LEARNINGS.md is copied to _delta/LEARNINGS.md and the original is left in place.

Exit codes:
  0 success
  1 not a Lite workspace
  3 filesystem error
"""
    if c=="patterns": return """
Usage:
  vucp patterns <path> [--patterns PATH] [--tags a,b,c] [--max N] [--include-candidates] [--json]

Selects relevant cross-project patterns.

Tag semantics:
  - Multiple tags use OR: a pattern is selected if it matches ANY tag.
  - A pattern's tags, applies_to and source_projects are matched.
  - does_not_apply_to wins: if ANY given tag is listed in a pattern's
    does_not_apply_to, the pattern is excluded even if other tags match.
  - Matching is case-insensitive and whitespace-trimmed ("CLI" == " cli ").
  - Empty entries are ignored ("cli,,safety" == "cli,safety").
  - Results are ranked by number of matched tags, then by score
    (confirmed status, confidence).
  - If no pattern matches, 0 results are returned (exit 0).
  - --tags "" (or only separators) means no tag filter.
  - If --tags is omitted, user_context from WORKSPACE.md is used as tags.

Examples:
  python vucp_cli_mvp.py patterns my-project --tags cli,safety
  python vucp_cli_mvp.py patterns my-project --tags "CLI, deployment" --json

Exit codes:
  0 success
  2 invalid arguments
"""
    if c=="autopilot": return """
Usage:
  vucp autopilot [status|set|audit] <path> [--mode SILENT|SURFACE|GUIDED] [--json]

Reads or changes Assisted Autopilot mode and audits structured autopilot actions.

Examples:
  python vucp_cli_mvp.py autopilot status my-project
  python vucp_cli_mvp.py autopilot set my-project --mode SURFACE
  python vucp_cli_mvp.py autopilot audit my-project --json

Safety:
  status and audit are read-only. set only modifies AUTOPILOT.md.

Exit codes:
  0 success
  2 invalid arguments
  3 filesystem error
"""
    return HELP

def subparse(command:str, rest:List[str])->Tuple[argparse.Namespace,Any]:
    if rest and rest[0] in ["help","/?","--help","-h"]: print(cmd_help(command)); raise SystemExit(EXIT_SUCCESS)
    if command=="upgrade":
        p=argparse.ArgumentParser(prog="vucp upgrade",add_help=False); p.add_argument("path",nargs="?",default="."); p.add_argument("--dry-run",action="store_true"); p.add_argument("--json",action="store_true"); return p.parse_args(rest),upgrade
    if command=="init":
        p=argparse.ArgumentParser(prog="vucp init",add_help=False); p.add_argument("path",nargs="?",default="vucp-workspace"); p.add_argument("--project"); p.add_argument("--owner"); p.add_argument("--language",default="en"); p.add_argument("--force",action="store_true"); p.add_argument("--lite",action="store_true"); p.add_argument("--json",action="store_true"); return p.parse_args(rest),init
    if command=="lint":
        p=argparse.ArgumentParser(prog="vucp lint",add_help=False); p.add_argument("path",nargs="?",default="."); p.add_argument("--json",action="store_true"); return p.parse_args(rest),lint
    if command=="graph":
        p=argparse.ArgumentParser(prog="vucp graph",add_help=False); p.add_argument("path",nargs="?",default="."); p.add_argument("--output"); p.add_argument("--json",action="store_true"); return p.parse_args(rest),graph
    if command=="doctor":
        p=argparse.ArgumentParser(prog="vucp doctor",add_help=False); p.add_argument("path",nargs="?",default="."); p.add_argument("--json",action="store_true"); return p.parse_args(rest),doctor
    if command=="export":
        p=argparse.ArgumentParser(prog="vucp export",add_help=False); p.add_argument("target",choices=["agents-md","codex","claude-md","cursor-rules","windsurf-rules"]); p.add_argument("path",nargs="?",default="."); p.add_argument("--output"); p.add_argument("--json",action="store_true"); return p.parse_args(rest),export_adapter
    if command=="dream":
        p=argparse.ArgumentParser(prog="vucp dream",add_help=False); p.add_argument("path",nargs="?",default="."); p.add_argument("--write",action="store_true"); p.add_argument("--json",action="store_true"); return p.parse_args(rest),dream
    if command=="autopilot":
        p=argparse.ArgumentParser(prog="vucp autopilot",add_help=False)
        p.add_argument("subcommand",nargs="?",default="status",choices=["status","set","audit"])
        p.add_argument("path",nargs="?",default=".")
        p.add_argument("--mode")
        p.add_argument("--json",action="store_true")
        return p.parse_args(rest),autopilot
    if command=="patterns":
        p=argparse.ArgumentParser(prog="vucp patterns",add_help=False); p.add_argument("path",nargs="?",default="."); p.add_argument("--patterns"); p.add_argument("--tags"); p.add_argument("--max"); p.add_argument("--include-candidates",action="store_true"); p.add_argument("--json",action="store_true"); return p.parse_args(rest),patterns
    print(f"ERROR: unknown command: {command}",file=sys.stderr); print("Run: vucp help",file=sys.stderr); raise SystemExit(EXIT_INVALID_ARGUMENTS)

def main(argv:Optional[List[str]]=None)->int:
    argv=list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] in ["--help","-h","help","/?"]: print(HELP); return EXIT_SUCCESS
    if argv[0]=="--version": print(f"vucp {VERSION} (protocol {PROTOCOL_VERSION})"); return EXIT_SUCCESS
    try:
        args,fn=subparse(argv[0],argv[1:]); return int(fn(args))
    except SystemExit as e:
        return int(e.code) if isinstance(e.code,int) else EXIT_INVALID_ARGUMENTS
    except Exception as e:
        print(f"ERROR: {e}",file=sys.stderr); return EXIT_INVALID_ARGUMENTS

if __name__=="__main__": raise SystemExit(main())
