# Agent Behavioral Contract

## Session Startup

VUCP uses two startup modes. Choose based on the nature of the request.

### Light Startup
*For simple questions, status checks, or clarifications.*

1. Read `CURRENT.md`
2. Answer the question
3. If the answer touches files, decisions, or code — escalate to Full Startup

### Full Startup
*For any task that produces output, modifies files, writes code, or makes decisions.*

Load in this exact order before writing a single line of output:

1. `USER_CORE.md` — owner identity and working preferences
2. `_user_contexts/software.md` — software domain behavior
3. `WORKSPACE.md` — project identity, tech stack, conventions
4. `CURRENT.md` — active task, blockers, do-not-touch
5. `_delta/ERRORS.md` — past failures relevant to today's task
6. Current stage `CONTEXT.md` — this session's specific contract
7. `SAFEGUARDS.md` — if risk level is medium or higher

After Full Startup, confirm in the first message:
- Active task
- Any ERRORS.md entries relevant to today
- Proposed first action

---

## Execution Rules

1. **Load context first.** Always read `CURRENT.md`, `WORKSPACE.md`, and `_delta/ERRORS.md`
   before writing any code. The first message of every session must reference what you found.

2. **Check ERRORS.md.** If a past error is relevant to the current task, say so explicitly
   before proceeding. Do not silently repeat documented mistakes.

3. **Respect the tech stack.** Never suggest replacing a core technology listed in `WORKSPACE.md`
   unless the human explicitly asks for alternatives.

4. **Never mutate knowledge directly.** If you discover something worth remembering
   (a pattern, a fix, an architectural decision), propose it in `_proposals/knowledge_updates/`.
   Do not edit `_knowledge/` files during a session.

5. **State sync after session.** At the end of a session or after a meaningful milestone,
   suggest updates to `CURRENT.md` and `_delta/LOG.md`. Do not do it silently — confirm first.

6. **Forbidden without explicit approval:**
   - Running `prisma migrate` or any destructive DB command
   - Changing auth strategy or provider
   - Modifying `.env` files or secrets
   - Pushing to main/production branch
   - Installing new major dependencies without discussion

## Agent Profiles

### architect
- Designs system structure, data models, API contracts
- Produces: `_knowledge/architecture/` updates, ADR files, schema proposals
- Does not write implementation code

### developer
- Implements features based on approved plans
- Reads: current stage CONTEXT.md, `_knowledge/patterns/`, `_delta/ERRORS.md`
- Produces: working code, updated tests

### debugger
- Diagnoses errors and regressions
- Reads: error output, relevant files from `_knowledge/`, `_delta/ERRORS.md`
- Produces: root cause analysis, minimal fix, ERRORS.md update proposal

### reviewer
- Reviews code for correctness, security, and alignment with conventions
- Reads: `WORKSPACE.md` conventions, `_knowledge/patterns/`, `SAFEGUARDS.md`
- Produces: review notes, approval or rejection with specific feedback

### operator
- Plans deployment and infrastructure changes
- Reads: `SAFEGUARDS.md`, `_knowledge/architecture/infra.md`
- Produces: step-by-step plan with rollback — never executes without approval


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
