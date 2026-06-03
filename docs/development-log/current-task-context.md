# Current Task Context

## Project

Trust-Bounded Agent OS (TBAO)

## Current Stage

v0.1 public draft.

The repository currently defines TBAO as a conceptual framework, governance spine, and local mock Action Spine design. It is not production-ready and must not be treated as a runtime for real systems.

## Current Objective

Implement Action Policy Kernel v0.1 as the next human-authorized phase after the collaboration-baseline-only PR.

This phase creates a narrow, local-only, mock-only, non-executing Python prototype that turns the existing Action Spine idea into testable policy code:

```text
ActionRequest
  -> RiskClassifier
  -> PolicyDecision
  -> ApprovalTicket check
  -> ActionLedger append
```

The previous collaboration-baseline-only context is superseded for this PR.

## Authorization Boundary

Andrew authorizes only a local-only, mock-only, non-executing prototype for Action Policy Kernel v0.1.

This authorization does not allow:

- live API calls;
- schedulers;
- workers;
- credential handling;
- production plugin activation;
- real file mutation;
- real deletion;
- real payment;
- real trading;
- real email sending;
- external side effects.

Preserve the TBAO v0.1 safety boundary:

```text
local-only
mock-only
non-executing
no real credentials
no real funds
no real external side effects
```

## Responsibilities

Human:

- Owns final meaning, priorities, approvals, and scope boundaries.
- Confirms when a task may create side effects or move beyond documentation and local mock code.
- Decides when a phase is complete and when final evidence should be created.

ChatGPT:

- Helps shape task intent, phase structure, review expectations, and collaboration language.
- Keeps project framing aligned with TBAO doctrine and non-goals.
- Should avoid turning narrow implementation tasks into broad governance essays.

Codex:

- Reads `current-task-context.md` first for continuity.
- Avoids full-repository scans by default.
- Reads only the files needed for the current task.
- Makes narrow, reviewable changes.
- Uses PR body notes for intermediate status.
- Does not create evidence reports except at phase end.
- Does not add runtime, scheduler, worker, API, key, plugin activation, or execution-capable behavior.

## Current PR Budget

Maximum 4 PRs for this phase.

This PR is limited to Action Policy Kernel v0.1 primitives, examples, tests, configuration mirror, and concise documentation.

## Current Non-Goals

- No production runtime.
- No general agent framework.
- No API gateway.
- No API server.
- No Telegram Bot.
- No Web UI.
- No scheduler.
- No worker.
- No production plugin activation.
- No live API integration.
- No live keys or credential handling.
- No real file mutation or deletion.
- No real funds, payments, trades, or email sending.
- No evidence report, retrospective, or long governance essay.
- No production-readiness claim.
- No expansion into PET/KET, education product, OKX, trading, health, legal, personal-data runtime, or other scenario work.

## Files In Scope For This PR

```text
src/tbao/
configs/risk_rules.v0.1.yaml
examples/action_requests/
tests/test_risk_classifier.py
tests/test_policy_engine.py
tests/test_approval_ticket.py
tests/test_ledger.py
docs/action-policy-kernel-v0.1.md
docs/development-log/current-task-context.md
docs/development-log/current-task-status.md
```

Prefer avoiding README changes in this PR.

## Validation Commands

Run:

```sh
git status --short
python -m pytest
grep -R "production-ready" -n README.md docs AGENTS.md src tests configs examples || true
grep -R "real credentials\|real funds\|external side effects" -n README.md docs AGENTS.md src tests configs examples || true
grep -R "requests\|httpx\|urllib\|smtplib\|boto3\|openai\|okx\|binance" -n src tests configs examples || true
```

Expected result:

- Tests pass.
- No real network/API/email/payment/trading behavior.
- No credentials.
- No production-readiness claim.
- All policy decisions remain mock-only.
- Ledger never marks real execution as true.

## Stop Condition

Stop after the narrow PR is created. Do not proceed to API server, Telegram approval, Web UI, scheduler, worker, external connector, production runtime, or integration layer.
