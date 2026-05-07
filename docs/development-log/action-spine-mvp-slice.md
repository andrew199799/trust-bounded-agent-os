# Action Spine MVP Slice

## Objective

Define the smallest safe Action Spine MVP slice for a later PR.

The slice should demonstrate a single mock action proposal record that passes through enough structure to show intent, proposed action, risk tier, human confirmation requirement, non-execution status, and an audit note.

This document is planning-only. It does not introduce runtime code, executable scripts, tests, APIs, workers, schedulers, credentials, live integrations, or production plugin activation.

## Minimal User Story

As a reviewer, I can inspect one static mock action proposal record and see:

- what intent the agent interpreted;
- what action the agent proposed;
- what risk tier was assigned;
- what human confirmation token would be required before any real action;
- that the proposal was not executed;
- what audit note explains the decision path.

## In Scope

- One static mock proposal record.
- One narrow action scenario: a proposed mock file write.
- A local-only, mock-only, non-executing status.
- A visible risk tier.
- A required human confirmation token field.
- A short audit note.
- Documentation that explains how a reviewer should interpret the record.

## Out of Scope

- Runtime code.
- Executable scripts.
- Package files.
- Tests.
- Live APIs.
- Credentials or live keys.
- Schedulers.
- Workers.
- Real file writes, deletion, network calls, messages, payments, trades, health, legal, personal-data, or production actions.
- Production plugin activation.
- Claims that TBAO is production-ready.
- Any Action Spine execution framework.

## Mock-Only Safety Boundary

The next PR must preserve this boundary:

```text
local-only
mock-only
non-executing
no real credentials
no real funds
no real external side effects
```

The mock record may describe a proposed action, but it must state that the action did not execute. The human confirmation token must be illustrative only and must not unlock real behavior.

## Proposed Files For The Next PR

The next PR may add static documentation or data under a narrow mock-only path, for example:

```text
docs/development-log/action-spine-static-mock-example.md
```

If the human approves a data fixture instead of prose, keep it static and non-executing. Do not add scripts, tests, package files, runtime code, examples, APIs, scheduler, worker, credentials, or live integration surfaces yet.

## Validation Expectations For The Next PR

Validation should confirm:

- only approved mock-only documentation or static fixture files changed;
- no implementation files were added;
- no production-ready claim was introduced;
- runtime and execution-related terms appear only in negative boundary language or explicit non-execution status;
- the mock proposal contains intent, proposed action, risk tier, required human confirmation token, non-execution status, and audit note.

Expected validation commands should remain simple file and grep checks unless the human explicitly approves executable tooling later.

## Stop Condition

Stop after the smallest static mock proposal slice is defined or added for review.

Do not implement Action Spine execution. Do not add runtime code, scripts, tests, package files, APIs, scheduler, worker, credentials, live integrations, production plugin activation, or external side effects.
