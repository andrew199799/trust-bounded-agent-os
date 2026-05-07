# Action Spine Fixture Reviewer Walkthrough

## Purpose

This walkthrough explains how a human reviewer should inspect `mock-file-write.proposal.yaml` field by field.

It is practical review guidance for a static, non-executing fixture. It is not runtime behavior, validation logic, or an execution plan.

## Before You Review

Read the fixture as documentation/data only. No runtime consumes the fixture, no validator exists yet, and no execution happens.

The confirmation token is illustrative only. It must not be treated as a command, approval system, or unlock mechanism.

## Review Path

1. Identify what the agent thinks the human wants.
2. Inspect the proposed action before trusting it.
3. Check whether the action would create side effects if real.
4. Check risk tier and rationale.
5. Check whether human confirmation is required.
6. Verify that the token is illustrative only.
7. Verify that `execution_status` is `not_executed`.
8. Confirm that `safety_boundary` blocks real-world assumptions.
9. Read `audit_note` as a reviewer-facing trace.

## Field-by-field Walkthrough

- `id`: stable fixture identifier for review discussion.
- `fixture_type`: must say this is a `static_non_executing_action_spine_proposal`.
- `status`: top-level status must be `not_executed`.
- `intent.summary`: short description of what the agent thinks the human wants.
- `intent.source`: should reveal that the intent source is illustrative, not a real user record.
- `intent.confidence`: shows the mock confidence label and should not be treated as verified truth.
- `intent.confirmation_status`: should show that the intent is not confirmed human intent.
- `proposed_action.action_type`: identifies the action shape, here `mock_file_write`.
- `proposed_action.target`: should remain a mock target, not a real path.
- `proposed_action.description`: should say no file is created, modified, deleted, or written.
- `proposed_action.side_effect_type`: flags that this is write-like behavior if it were real.
- `proposed_action.execution_mode`: must be `static_fixture_only`.
- `risk.tier`: should treat the write-like proposal conservatively.
- `risk.rationale`: explains why the risk tier is conservative despite no execution.
- `risk.boundary`: should restate local-only, mock-only, non-executing limits.
- `required_confirmation.required`: should be `true` for write-like proposals.
- `required_confirmation.token`: should be `CONFIRM_MOCK_FILE_WRITE_ONLY`.
- `required_confirmation.reason`: explains why a human would need to confirm a future real action.
- `required_confirmation.token_effect`: must say the token is illustrative only and does not unlock real behavior.
- `execution_status.state`: must be `not_executed`.
- `execution_status.executed`: must be `false`.
- `execution_status.blocked_reason`: should say the fixture is static and no runtime consumes it.
- `audit_note.summary`: summarizes what happened for review.
- `audit_note.review_focus`: tells the reviewer which fields to inspect.
- `audit_note.recovery_note`: should say no recovery is needed because no real file change occurred.
- `safety_boundary.*`: every safety boundary flag should preserve local-only, mock-only, non-executing, no-real-credentials, no-real-funds, and no-external-side-effects assumptions.

## Reviewer checklist

- [ ] Is the human intent confirmed or only inferred?
- [ ] Is the proposed action specific enough to review?
- [ ] Does the action describe any write-like or side-effectful behavior?
- [ ] Is risk treated conservatively?
- [ ] Is confirmation required?
- [ ] Is the confirmation token non-operational?
- [ ] Is execution explicitly blocked?
- [ ] Is there any real credential, real path, live API, real file write, or external side effect?
- [ ] Is there enough audit information to understand what happened?

## What would be unsafe in a real implementation

- Treating inferred intent as confirmed human intent.
- Letting a confirmation token trigger real behavior.
- Consuming the fixture with runtime code.
- Hiding execution behind a static-looking file.
- Using real paths, credentials, live URLs, external services, or irreversible actions.
- Treating `not_executed` as optional.

## Current Limitation

This walkthrough is documentation only. No runtime consumes the fixture. No validator exists yet. No execution happens.

It demonstrates review structure, not enforcement capability.

## Links

- [`mock-file-write.proposal.yaml`](mock-file-write.proposal.yaml)
- [`README.md`](README.md)
- [`../framework-overview.zh-en.md`](../framework-overview.zh-en.md)
- [`../action-spine-mvp.zh-en.md`](../action-spine-mvp.zh-en.md)
