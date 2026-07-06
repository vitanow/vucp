# VUCP Schema v0.5.0 — SaaS MVP Launch Kit

## Product-Specific Schema

### Stage Types Used
- research (problem-validation, customer-research)
- synthesis (solution-design, landing-page, first-customers)
- analysis (mvp-scope)
- implementation (waitlist-setup, build-launch)

### Knowledge Types Used
- domain (специфично знание за SaaS/стартапи)
- playbook (стъпка-по-стъпка процедури)
- policy (brand voice, safeguards)
- metric (временни рамки, conversion rates)

### Artifact Types Used
- input (user ideas, research data)
- output (findings, copy, plans)
- report (validation summary)
- decision (feature choices, pricing)
- command (setup instructions)
- checklist (verification assets)

### Review Status Values
- pending
- approved
- approved_with_changes
- rejected
- blocked

### Risk Levels Used
- low: research, validation
- medium: copywriting, waitlist, first customers
- high: mvp scoping, build & launch

### Run Classes Used
- transient: quick experiments, draft copy
- standard: approved stage outputs
- milestone: pre-launch verification, launch day

## SaaS-Specific Conventions

### Naming
- Stages: zero-padded for ordering (01-, 02-, ...)
- Outputs: descriptive, kebab-case
- Knowledge: domain-specific, tagged

### Required Verification
- All "high" risk stages must pass `_verification/checklists/`
- Launch stage requires pre-launch checklist completion
- Rollback plan must exist for build-launch
