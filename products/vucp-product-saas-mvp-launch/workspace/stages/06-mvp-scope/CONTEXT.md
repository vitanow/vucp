---
stage: "mvp-scope"
type: "analysis"
version: "1.0"
agent: "researcher"
review_required: true
risk_level: "high"
---

# Stage 6: MVP Scope

## 1. Purpose
Дефинирай точно какво ще се построи, с какъв tech stack, и за колко време.

## 2. Required Context
- All previous stages
- `/_knowledge/domain/mvp-scoping.md`
- `/_knowledge/domain/pricing-strategies.md`
- `SAFEGUARDS.md` (high risk stage)

## 3. Knowledge Context
- `/_knowledge/domain/mvp-scoping.md`
- `/_knowledge/domain/pricing-strategies.md`

## 4. Inputs
- `input/mvp-features.md`
- `input/tech-skills.md` (optional)
- `input/budget.md` (optional)

## 5. Allowed Actions
- Recommend tech stack
- Create detailed spec
- Estimate timeline
- Define pricing

## 6. Forbidden Actions
- Do not recommend over-engineered solutions
- Do not skip "will not build"
- Do not ignore budget constraints

## 7. Process
1. Review MVP features
2. Recommend tech stack (3 options: simple/medium/full)
3. Create detailed build spec
4. Estimate timeline with 20% buffer
5. Define pricing strategy
6. Create success metrics

## 8. Outputs
- `output/mvp-spec.md`
- `output/tech-stack.md`
- `output/timeline.md`

## 9. Verification
- [ ] Tech stack matches user skills
- [ ] Timeline has buffer
- [ ] Pricing is defined
- [ ] Success metrics are measurable
- [ ] Rollback plan mentioned

## 10. Review Gate
"Ето пълният план за MVP. Сигурни ли сте, че това е изпълнимо? [Одобри] [Промени tech stack] [Удължи timeline]"

## 11. Delta Update
Log and learn
