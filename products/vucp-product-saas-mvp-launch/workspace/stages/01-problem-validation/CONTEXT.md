---
stage: "problem-validation"
type: "research"
version: "1.0"
agent: "researcher"
review_required: true
risk_level: "low"
---

# Stage 1: Problem Validation

## 1. Purpose
Валидирай, че проблемът е реален, болезнен и достатъчно голям, за да подкрепи бизнес.

## 2. Required Context
Read before acting:
- `/CURRENT.md`
- `/SAFEGUARDS.md`
- `/_knowledge/index.md`
- `/_delta/ERRORS.md`

## 3. Knowledge Context
Load these knowledge files:
- `/_knowledge/domain/customer-research.md` (Mom Test principles)
- `/_knowledge/playbooks/customer-interview.md` (interview structure)

## 4. Inputs
Expected input files:
- `input/idea-description.md` (user's raw idea from _inbox/)

If missing, ask user: "Опиши идеята си в 2-3 изречения. Какъв проблем решаваш? За кого?"

## 5. Allowed Actions
- Read input files
- Research problem space (ask user for context, don't hallucinate)
- Produce markdown outputs
- Propose knowledge updates in `/_proposals/knowledge_updates/`
- Ask clarifying questions

## 6. Forbidden Actions
- Do not assume market size without data
- Do not skip to solution before validating problem
- Do not modify trusted knowledge directly
- Do not delete previous runs
- Do not perform production changes

## 7. Process
1. Read required context
2. Check known errors in `/_delta/ERRORS.md`
3. Read user's idea description
4. Ask 3-5 clarifying questions about the problem
5. Help user articulate:
   - Specific problem (not "productivity", but "spend 2 hours daily organizing tasks")
   - Who has this problem (specific persona)
   - How they currently solve it (competition = status quo)
   - Why current solutions fail
6. Produce structured problem statement
7. List 3 testable hypotheses

## 8. Outputs
Required output files:
- `output/problem-statement.md`
- `output/hypothesis-list.md`

### problem-statement.md format
```markdown
# Problem Statement

## The Problem
[1-2 sentences, specific and vivid]

## Who Has It
[Specific persona, not "everyone"]

## Current Solutions
[What they do now]

## Why Current Solutions Fail
[Specific gaps]

## Problem Size Estimate
[How many people? How often? How much does it cost them?]

## Confidence Level
[High/Medium/Low + why]
```

### hypothesis-list.md format
```markdown
# Testable Hypotheses

## H1: [Statement]
- Test: [How to validate]
- Success criteria: [What proves it]
- Time: [How long to test]

## H2: [Statement]
...

## H3: [Statement]
...
```

## 9. Verification
Before marking complete:
- [ ] Problem is specific, not generic
- [ ] Persona is defined
- [ ] At least 3 hypotheses are testable
- [ ] User has reviewed and approved
- [ ] No forbidden action was taken

## 10. Review Gate
Stop after writing outputs.
Human approval required before next stage.

Present to user:
"Ето какво открихме за проблема. Убедени ли сте, че това е правилният фокус? [Одобри] [Промени] [Добави още]"

## 11. Delta Update
After approval:
- Append result to `/_delta/LOG.md`
- Propose reusable patterns for `/_delta/LEARNINGS.md`
- Update `CURRENT.md` for standard and milestone runs
