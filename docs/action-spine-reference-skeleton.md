# Action Spine Reference Skeleton

This reference skeleton is documentation only.

It is non-executable pseudo-interface material for public discussion. It is not runnable code, no runtime consumes it, no validator exists, and it must not be treated as an implementation contract.

Real implementation work belongs in `MagicWorld2100/Twin-Brain-Agent-OS` first. Only abstracted, non-executing, non-proprietary, and non-sensitive framework material may be extracted back here.

## Pseudo-Interfaces

```text
interface Intent {
  summary: text
  source: illustrative_or_declared_source
  confidence: confidence_label
  confirmation_status: unconfirmed | confirmed
}

interface ProposedAction {
  action_type: action_shape_label
  target: mock_or_abstract_target
  description: text
  side_effect_type: none | read_like | write_like | external_like
  execution_mode: static_fixture_only
}

type RiskTier =
  | minimal
  | low
  | medium
  | high
  | blocked

interface RequiredConfirmation {
  required: true | false
  token: illustrative_confirmation_token
  reason: text
  token_effect: illustrative_only_no_runtime_effect
}

interface ExecutionStatus {
  state: not_executed
  executed: false
  blocked_reason: text
}

interface AuditNote {
  summary: text
  review_focus: text
  recovery_note: text
}

interface ActionSpineProposal {
  intent: Intent
  proposed_action: ProposedAction
  risk_tier: RiskTier
  required_confirmation: RequiredConfirmation
  execution_status: ExecutionStatus
  audit_note: AuditNote
}
```

## Boundary Notes

- Documentation only.
- Non-executable.
- No runtime consumes it.
- No validator exists.
- No API, scheduler, worker, credential, real file write, or external side effect is introduced.
- Real implementation belongs in `MagicWorld2100/Twin-Brain-Agent-OS` first.
