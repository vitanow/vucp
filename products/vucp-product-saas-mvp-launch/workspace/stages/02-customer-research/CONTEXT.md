---
stage: "customer-research"
type: "research"
version: "1.0"
agent: "researcher"
review_required: true
risk_level: "low"
---

# Stage 2: Customer Research

## 1. Purpose
Намери и интервюирай 5+ потенциални клиенти за валидиране на проблема.

## 2. Required Context
- `/CURRENT.md`
- `/SAFEGUARDS.md`
- `/_knowledge/index.md`
- `/_delta/ERRORS.md`
- `stages/01-problem-validation/output/problem-statement.md`
- `stages/01-problem-validation/output/hypothesis-list.md`

## 3. Knowledge Context
- `/_knowledge/playbooks/customer-interview.md`
- `/_knowledge/domain/customer-research.md`

## 4. Inputs
- `input/target-persona.md` (user-defined or AI-suggested)
- `input/interview-candidates.md` (optional: list of potential interviewees)

## 5. Allowed Actions
- Read input files
- Generate interview scripts
- Suggest where to find interviewees
- Create interview tracking template
- Produce findings summary

## 6. Forbidden Actions
- Do not fabricate interview data
- Do not skip interviews and "simulate" findings
- Do not modify trusted knowledge directly

## 7. Process
1. Review problem statement from Stage 1
2. Define/refine target persona
3. Generate 3 interview scripts (different angles)
4. Suggest 10+ places to find interviewees
5. Create interview tracking spreadsheet/template
6. After user completes interviews (or provides notes), analyze patterns
7. Produce findings summary

## 8. Outputs
- `output/interview-scripts.md` (3 scripts)
- `output/findings-summary.md` (pattern analysis)
- `output/validated-problems.md` (confirmed vs. rejected hypotheses)

### findings-summary.md format
```markdown
# Customer Research Findings

## Interviews Conducted
[Number, dates, roles]

## Key Patterns
### Pattern 1: [Theme]
- Evidence: [Quotes, numbers]
- Confidence: High/Medium/Low

### Pattern 2: [Theme]
...

## Validated Hypotheses
- H1: [Status + evidence]
- H2: [Status + evidence]
- H3: [Status + evidence]

## Surprises
[What we didn't expect]

## Open Questions
[What we still don't know]

## Next Steps
[What to do with these findings]
```

## 9. Verification
- [ ] At least 3 interview scripts generated
- [ ] 10+ candidate sources suggested
- [ ] Pattern analysis based on real data (or explicit "simulated" note)
- [ ] Hypotheses updated with evidence

## 10. Review Gate
"Ето какво научихме от (предложените) интервюта. Готови ли сте да дефинираме решението? [Одобри] [Нужни са още интервюта] [Промени фокуса]"

## 11. Delta Update
After approval, update logs and learnings
