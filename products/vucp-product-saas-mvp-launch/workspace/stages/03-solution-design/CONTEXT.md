---
stage: "solution-design"
type: "synthesis"
version: "1.0"
agent: "writer"
review_required: true
risk_level: "medium"
---

# Stage 3: Solution Design

## 1. Purpose
Дефинирай MVP решението — какво прави, за кого, и какво НЕ прави.

## 2. Required Context
- All previous stages' outputs
- `/_knowledge/domain/mvp-scoping.md`
- `/_knowledge/brand/voice.md`

## 3. Knowledge Context
- `/_knowledge/domain/mvp-scoping.md`
- `/_knowledge/brand/voice.md`

## 4. Inputs
- `input/validated-problems.md`
- `input/constraints.md` (optional: budget, timeline, tech skills)

## 5. Allowed Actions
- Synthesize findings into solution definition
- Define feature set (must-have vs. nice-to-have)
- Create positioning statement
- Produce markdown outputs

## 6. Forbidden Actions
- Do not promise features beyond MVP scope
- Do not ignore validated problems
- Do not skip "will not build" section

## 7. Process
1. Review validated problems
2. Define core job-to-be-done
3. List must-have features (max 5)
4. List nice-to-have features (for v2)
5. Explicitly list "will NOT build"
6. Create positioning statement
7. Define success criteria

## 8. Outputs
- `output/solution-definition.md`
- `output/mvp-features.md`
- `output/non-features.md`

### solution-definition.md format
```markdown
# Solution Definition

## Product Name
[Working name]

## One-Line Description
[What it does, for whom, outcome]

## Core Job-to-be-Done
[The ONE thing]

## Positioning Statement
For [target customer]
Who [problem statement]
[Product] is a [category]
That [key benefit]
Unlike [competitors]
We [differentiator]

## Success Criteria
- [Specific, measurable]
- [Time-bound]
```

### mvp-features.md format
```markdown
# MVP Features

## Must-Have (Launch Critical)
1. [Feature] — [Why critical] — [Effort estimate]
2. ...

## Nice-to-Have (V2)
1. [Feature] — [Why deferred]
2. ...

## Will NOT Build (Explicit)
1. [Feature] — [Why not] — [When maybe]
2. ...
```

## 9. Verification
- [ ] Core job is singular and clear
- [ ] Must-haves are ≤ 5
- [ ] "Will not build" is explicit
- [ ] Success criteria are measurable

## 10. Review Gate
"Ето нашето MVP решение. Убедени ли сте, че това е достатъчно за първи customers? [Одобри] [Добави feature] [Премахни feature]"

## 11. Delta Update
Update logs and propose learnings
