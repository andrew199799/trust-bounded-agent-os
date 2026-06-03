# Action Policy Kernel v0.1

## Purpose

Action Policy Kernel v0.1 converts the Action Spine idea from static documentation into a local mock policy kernel. It models how a proposed agent action can be classified, gated, approved or denied, and recorded before any real execution path exists.

The kernel validates authority boundaries around proposed actions. It is not a production runtime, a general agent framework, or an API gateway.

## Scope

This prototype remains inside the TBAO v0.1 safety boundary:

```text
local-only
mock-only
non-executing
no credentials
no funds
no external side effects
```

No real action is executed. Policy decisions may mark a mock decision path, but `executed` remains `false`.

## Flow

```text
ActionRequest -> RiskClassifier -> PolicyDecision -> ApprovalTicket -> ActionLedger
```

- `ActionRequest` describes the proposed action, actor, target, intent, evidence, environment, reversibility, side-effect scope, blast radius, sensitive surface, and timestamp.
- `RiskClassifier` assigns the highest applicable L0-L4 risk tier.
- `PolicyDecision` records whether the action is allowed, logged, approval-gated, denied by default, or denied.
- `ApprovalTicket` can satisfy L3 or L4 gates only when it is valid, unexpired, human-issued, and bound to the exact action hash.
- `ActionLedger` appends the decision path. It does not record a real execution result.

## Risk Tiers

| Tier | Meaning | Default handling |
| --- | --- | --- |
| L0 | pure thought, analysis, draft, simulation | `ALLOW` |
| L1 | read-only inspection, tests, scans | `ALLOW_LOG` |
| L2 | low-risk writes, temporary files, draft files | `ALLOW_LOG_ROLLBACK_NOTE` |
| L3 | configuration changes, dependency install, code commit, durable memory write | `REQUIRE_APPROVAL` unless allowlisted or approved |
| L4 | deletion, payment, trade, external message send, production modification, credential access | `DENY_BY_DEFAULT` unless strong approval exists |

## Approval Model

An agent may request an action, but it cannot approve its own action. An approval ticket is valid only when:

- `approver_id` differs from the requesting `agent_id`;
- the ticket decision is `approve`;
- the ticket is not expired;
- the ticket `action_id` matches the action;
- the ticket `action_hash` matches the exact current action payload.

Normal approval can satisfy L3. L4 requires strong approval. If the action payload changes after approval, the old ticket no longer applies because the action hash changes.

Even with valid strong approval for L4, the kernel permits only a mock decision path. It does not send email, delete files, move funds, place trades, modify production, access credentials, or call external systems.

## Explicit Non-Goals

- no runtime execution
- no API server
- no Telegram Bot
- no Web UI
- no scheduler
- no worker
- no production-readiness claim
- no live APIs, credentials, funds, external messages, deletion, trading, or production modification

## Implementation Notes

The v0.1 package lives under `src/tbao/` and uses Python standard-library dataclasses. `configs/risk_rules.v0.1.yaml` mirrors the rules for human review; it is not a dynamic rules engine in this PR.
