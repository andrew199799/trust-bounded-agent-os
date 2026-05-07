# Static Action Spine Fixtures

## Purpose

This directory contains static, non-executing Action Spine proposal fixtures for public review.

## What This Fixture Demonstrates

`mock-file-write.proposal.yaml` shows how a proposed mock file write can be represented before execution:

- interpreted intent;
- proposed action;
- risk tier;
- required confirmation token;
- non-execution status;
- audit note;
- explicit safety boundary.

## Field Guide

- `intent`: the mock user intent and its confirmation status.
- `proposed_action`: the illustrative action proposal. No real file write occurs.
- `risk`: conservative risk tier and rationale.
- `required_confirmation`: human confirmation requirement and illustrative token.
- `execution_status`: fixed to `not_executed`.
- `audit_note`: reviewer-facing summary, review focus, and recovery note.
- `safety_boundary`: local-only, mock-only, non-executing boundary flags.

## Safety Boundary

This fixture is static documentation/data only. No runtime consumes this file, no validator exists yet, no execution happens, and the confirmation token is illustrative only.

The fixture does not create, modify, delete, write, send, call, schedule, trade, pay, fetch, or unlock anything.

## What This Fixture Does Not Do

- no real file write occurs.
- No runtime code is added.
- No executable script is added.
- No test or validator is added.
- No API, scheduler, or worker is added.
- No credentials, live integrations, real funds, or external side effects are introduced.
- No Action Spine execution is implemented.
- No production-readiness claim is made.

## Link Back To Framework Docs

- [`../framework-overview.zh-en.md`](../framework-overview.zh-en.md)
- [`../action-spine-mvp.zh-en.md`](../action-spine-mvp.zh-en.md)
- [`../development-log/action-spine-static-mock-example.md`](../development-log/action-spine-static-mock-example.md)
