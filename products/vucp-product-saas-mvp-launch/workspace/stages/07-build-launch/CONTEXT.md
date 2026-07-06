---
stage: "build-launch"
type: "implementation"
version: "1.0"
agent: "operator"
review_required: true
risk_level: "high"
---

# Stage 7: Build & Launch

## 1. Purpose
Изгради и лансирай MVP със структуриран процес и rollback план.

## 2. Required Context
- `stages/06-mvp-scope/output/mvp-spec.md`
- `/_knowledge/playbooks/mvp-build-checklist.md`
- `SAFEGUARDS.md` (CRITICAL — high risk)
- `/_verification/checklists/pre-launch.md`

## 3. Knowledge Context
- `/_knowledge/playbooks/mvp-build-checklist.md`

## 4. Inputs
- `input/mvp-spec.md`
- `input/tech-stack.md`

## 5. Allowed Actions
- Provide build guidance
- Generate code snippets
- Create deployment checklist
- Write launch plan

## 6. Forbidden Actions
- Do not execute production commands without explicit approval
- Do not skip pre-launch checklist
- Do not launch without rollback plan
- Do not modify production without backup

## 7. Process
1. Review MVP spec
2. Follow 2-week build checklist
3. Create pre-launch verification
4. Write launch plan
5. Document rollback procedure
6. Schedule launch

## 8. Outputs
- `output/launch-plan.md`
- `output/deployment-checklist.md`

## 9. Verification
- [ ] Pre-launch checklist completed
- [ ] Rollback plan exists
- [ ] Analytics active
- [ ] Support channel ready
- [ ] User approved launch

## 10. Review Gate
"Всичко е готово за launch. Прегледайте checklist-а и потвърдете: [Launch сега] [Отложи] [Добави още проверки]"

## 11. Delta Update
After launch:
- Log launch in `/_delta/LOG.md`
- Record any issues in `/_delta/ERRORS.md`
- Update `CURRENT.md`
- This is a MILESTONE run — create full snapshot
