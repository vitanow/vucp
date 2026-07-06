---
stage: "waitlist-setup"
type: "implementation"
version: "1.0"
agent: "operator"
review_required: true
risk_level: "medium"
---

# Stage 5: Waitlist Setup

## 1. Purpose
Създай система за събиране на имейли и комуникация с waitlist.

## 2. Required Context
- `stages/04-landing-page/output/landing-page-copy.md`
- `/_knowledge/playbooks/waitlist-setup.md`

## 3. Knowledge Context
- `/_knowledge/playbooks/waitlist-setup.md`

## 4. Inputs
- `input/landing-page-copy.md`
- `input/tech-preferences.md` (optional: user's tech stack preference)

## 5. Allowed Actions
- Recommend tools
- Write email sequence
- Create setup commands
- Provide configuration guidance

## 6. Forbidden Actions
- Do not execute commands without approval
- Do not recommend tools that violate SAFEGUARDS.md
- Do not skip GDPR compliance

## 7. Process
1. Review landing page copy
2. Recommend waitlist tool based on user's skills
3. Write complete email sequence (4 emails)
4. Create setup checklist
5. Provide configuration commands

## 8. Outputs
- `output/waitlist-strategy.md`
- `output/email-sequence.md`
- `output/setup-commands.md`

## 9. Verification
- [ ] Tool recommended matches user skills
- [ ] Email sequence has 4 emails
- [ ] GDPR compliance mentioned
- [ ] Setup commands are safe

## 10. Review Gate
"Ето стратегията за waitlist. Кой инструмент предпочитате? [Carrd] [Webflow] [Next.js + Supabase] [Друг]"

## 11. Delta Update
Log and learn
