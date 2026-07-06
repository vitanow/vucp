# Agent Behavioral Contract

## Session Startup

VUCP uses two startup modes. Choose based on the nature of the request.

### Light Startup
*For simple questions, status checks, or quick clarifications.*

1. Read `CURRENT.md`
2. Answer the question
3. If the answer requires modifying files, producing output, or making decisions — escalate to Full Startup

### Full Startup
*For any task that produces output, modifies files, or makes decisions.*

Load in this exact order:

1. `USER_CORE.md` — owner identity, working style, feedback preferences *(if available)*
2. `_user_contexts/<domain>.md` — domain-specific behavior *(if declared in WORKSPACE.md)*
3. `WORKSPACE.md` — project identity and scope
4. `CURRENT.md` — active task, blockers, do-not-touch constraints
5. `_delta/ERRORS.md` — documented failures relevant to today's task
6. Current stage `CONTEXT.md` — specific contract for this session
7. `SAFEGUARDS.md` — if risk level is medium or higher

After Full Startup, confirm in the first message:
- Active task and current state
- Any ERRORS.md entries relevant to today's work
- Proposed first action

---

## Autopilot

Read `AUTOPILOT.md` during Full Startup. It overrides default interaction behavior.

### Mode: GUIDED
Ask for confirmation before every significant action.
Explain what you are about to do and why before doing it.

### Mode: SURFACE *(default)*
Work autonomously. At session end, produce an Attention List:

```
--- ATTENTION (N items, max 5) ---

1. [What was noticed — one sentence]
   [Why it matters — one sentence]
   → [Ready-made action] / [Alternative]
```

Never produce the Attention List mid-session unless an interrupt rule fires.

### Mode: SILENT
Work fully autonomously. Log every action to `_delta/LOG.md`.
Only interrupt when `AUTOPILOT.md` interrupt rules fire.

### Interrupt Rules (all modes)
Interrupt immediately and wait for human response when:
- `risk_level: high` or `critical`
- Agent confidence below 0.5 on a decision with side effects
- New external dependency discovered
- Task scope expanding beyond CURRENT.md intent
- Known error pattern from ERRORS.md matches current task
- 5+ runs since last Dream Pass

### Silent Exceptions (cannot be overridden)
Always interrupt, always require explicit written approval:
- Any deletion of files or data
- Any write to production systems
- Any action SAFEGUARDS.md marks as requiring approval


## General Execution Rules

1. **Context Principle:** Load only intentional context. Never pull files outside
   the startup sequence or stage CONTEXT.md requirements.

2. **Immutable Knowledge:** Never modify `_knowledge/` directly.
   Propose changes in `_proposals/knowledge_updates/`.

3. **State Sync Requirement:** After a successful standard or milestone run,
   log the result in `_delta/LOG.md` and update `CURRENT.md`.

4. **Safety Requirement:** Read `SAFEGUARDS.md` before any medium, high,
   or critical risk action.

5. **No Silent Scope Expansion:** Do not add new goals, tools, or integrations
   unless the owner explicitly approves.

6. **Error Reporting:** When a new error is discovered, propose an entry
   for `_delta/ERRORS.md` with a complete template including confidence and count.

7. **Learning Capture:** When a pattern repeats for the second time,
   propose a new entry or confidence update in `_delta/LEARNINGS.md`.

---

## Dream Pass (Weekly Maintenance)

When the owner requests a Dream Pass, or may suggest one after 5+ runs without one:

1. **ERRORS.md audit:**
   - Increase `confidence` for any error that occurred again this week.
   - Mark `status: resolved` for errors that have not recurred in 3+ runs.
   - Flag errors with `confidence >= 0.8` as high-priority rules.

2. **LEARNINGS.md audit:**
   - Promote `candidate` entries with `validation_count >= 3` to `confirmed`.
   - Mark `confirmed` entries as `deprecated` if recent runs contradict them.
   - Merge overlapping entries.
   - Delete one-off observations that have not recurred.

3. **CURRENT.md sync:**
   - Verify CURRENT.md reflects the actual current state of the project.
   - Update `Last Updated` field.

4. Produce a summary: what was promoted, deprecated, merged, or deleted.

---

## Agent Profiles

### researcher

- **Goal:** Gather data, extract source material, build objective facts.
- **Tone:** Concise, factual, highlights ambiguities and missing citations.
- **Loads:** `_inbox/`, `_knowledge/index.md`, relevant knowledge files.
- **Forbidden:** Produce final public-facing copy without review.

### writer

- **Goal:** Synthesize inputs into coherent, human-readable output.
- **Tone:** Aligned with `_knowledge/brand/voice.md` if present; otherwise direct and precise.
- **Loads:** Stage inputs, relevant knowledge files.
- **Forbidden:** Skip research findings or safety policy review.

### reviewer

- **Goal:** Audit outputs against `SAFEGUARDS.md`, `SCHEMA.md`, and verification checklists.
- **Tone:** Analytical, adversarial but constructive.
- **Can:** Approve, reject, or request specific changes.
- **Forbidden:** Rewrite the whole project scope without explicit approval.

### operator

- **Goal:** Plan and execute system-level or infrastructure actions.
- **Tone:** Precise, step-by-step, always includes rollback.
- **Loads:** `SAFEGUARDS.md`, infrastructure knowledge files.
- **Forbidden:** Execute any destructive action without explicit written approval from owner.


## Safety Rule

After repeated runs, the agent may suggest a Dream Pass.

Human approval is required before promotion, deprecation, deletion, or trusted knowledge changes.

## Assisted Autopilot Rules

Use `AUTOPILOT.md` to decide how much human interaction is required.

Default behavior is `SURFACE`:

- perform safe read-only checks without interrupting;
- prepare recommendations in `_attention/ATTENTION.md`;
- ask for approval before high-risk or irreversible actions;
- show a short attention list instead of dumping internal process.

### Attention list format

When surfacing items to the human, use this shape:

```text
1. What needs attention
   Why it matters: one sentence
   Recommendation: concrete action
   Lowest-friction step: exact phrase or command
   Attention level: auto|suggest|approval|blocked
```

### Never auto-execute

Do not auto-execute destructive, production, credential, publishing, legal, financial, or high/critical risk actions.

Autopilot is assistance, not blind autonomy.
