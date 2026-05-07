# TBAO Public Discussion Guide

## Who Should Join The Discussion

This guide is for serious contributors who want to improve TBAO as a public framework, manifesto, and mock-only static demo.

Useful perspectives include AI agent builders, governance researchers, open-source tool designers, reviewers of agent safety boundaries, and practitioners thinking carefully about human authority over agent action.

## What Kinds Of Contributions Are Welcome

- Framework critique.
- Terminology refinement.
- Risk-tier discussion.
- Confirmation semantics.
- Audit semantics.
- Static demo improvement.
- Governance pattern discussion.
- Navigation and readability improvements that preserve the current boundary.

## What Not To Contribute Here

Do not contribute the following to this public repo:

- runtime implementation;
- proprietary implementation details;
- credentials;
- real integrations;
- production deployment material;
- business-sensitive material;
- personal data;
- validators, scripts, tests, APIs, schedulers, workers, or execution-capable code unless a future task explicitly changes scope.

## Relationship To Twin-Brain-Agent-OS

This public repository is not the full TBAO product. Real implementation work belongs in `MagicWorld2100/Twin-Brain-Agent-OS` first.

Only abstracted, non-executing, non-proprietary, and non-sensitive framework material may be extracted back here.

## Discussion Principles

- Keep human meaning sovereignty central.
- Separate framework language from implementation capability.
- Treat side-effectful action as something that must be bounded, confirmable, traceable, and recoverable.
- Keep examples mock-only unless a later public task explicitly changes scope.
- Do not imply production readiness.
- Do not include private, proprietary, or sensitive implementation details.

## First Good Discussion Topics

- Does the Action Spine sequence use the right public terms?
- Is `risk_tier` clear enough as a conservative review label?
- What should a confirmation token mean in a non-executing spec?
- What should `audit_note` explain in a static demo?
- How should public docs distinguish mock-only examples from real implementation?
- What governance patterns are general enough to discuss publicly?
