"""In-memory ledger for local mock policy decisions."""

from __future__ import annotations

from datetime import datetime, timezone

from .models import ActionLedgerRecord, ActionRequest, ApprovalTicket, PolicyDecision


class ActionLedger:
    """Append-only in-memory ledger for policy decisions, not real executions."""

    def __init__(self) -> None:
        self._records: list[ActionLedgerRecord] = []

    @property
    def records(self) -> tuple[ActionLedgerRecord, ...]:
        return tuple(self._records)

    def append(
        self,
        action_request: ActionRequest,
        policy_decision: PolicyDecision,
        approval_ticket: ApprovalTicket | None = None,
        mock_executed: bool = True,
    ) -> ActionLedgerRecord:
        record = ActionLedgerRecord(
            action_id=action_request.action_id,
            agent_id=action_request.agent_id,
            risk_tier=policy_decision.risk_tier,
            decision=policy_decision.decision,
            executed=False,
            mock_executed=mock_executed,
            approval_ticket_id=approval_ticket.ticket_id if approval_ticket else None,
            reason=policy_decision.reason,
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
        self._records.append(record)
        return record
