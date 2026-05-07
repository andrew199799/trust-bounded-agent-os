# Static Mock Action Spine Proposal Example

## Purpose

This document adds one static mock Action Spine proposal example for reviewer inspection.

It is documentation only. It does not create, modify, delete, send, call, schedule, trade, pay, fetch, execute, or unlock anything.

## Static Mock Proposal Record

```yaml
intent: "Draft a local note that summarizes a mock review checkpoint."
proposed_action:
  action_type: "mock_file_write"
  target: "mock:/workspace/review-checkpoint.md"
  description: "Illustrative proposed mock file write only; no file is created, modified, or written."
risk_tier: "L2_controlled_mock_side_effect"
required_confirmation_token: "CONFIRM_MOCK_FILE_WRITE_ONLY"
execution_status: not_executed
audit_note: "The action was only proposed for static review. It was not executed, and the confirmation token is illustrative only; it does not unlock real behavior."
```

## Field Explanation

- `intent`: short mock user intent interpreted by the agent.
- `proposed_action`: illustrative mock file write proposal. It is not performed.
- `risk_tier`: conservative L2-aligned tier for a low-risk write-like proposal, marked as controlled and mock-only because no real side effect occurs.
- `required_confirmation_token`: illustrative human confirmation phrase that a reviewer can inspect. It does not unlock runtime behavior or real action.
- `execution_status`: fixed to `not_executed`.
- `audit_note`: short reviewer-facing note explaining that the action was proposed only and no real behavior was triggered.

## Reviewer Checklist

- The proposal includes intent, proposed action, risk tier, required confirmation token, execution status, and audit note.
- The proposed action is clearly marked as illustrative and not performed.
- `execution_status` is `not_executed`.
- The confirmation token is illustrative only.
- No runtime behavior, script, API, scheduler, worker, credential, live integration, real file write, or external side effect is introduced.

## Safety Boundary

This static example preserves the TBAO v0.1 boundary:

```text
local-only
mock-only
non-executing
no real credentials
no real funds
no real external side effects
```

It does not claim production readiness and does not implement Action Spine execution.

## Stop Condition

Stop at this static mock proposal example.

Do not add runtime code, executable scripts, tests, package files, APIs, scheduler, worker, credentials, live integrations, real file writes, external side effects, production plugin activation, or production-readiness claims.
