"""Policy decisions for the local mock Action Policy Kernel."""

from __future__ import annotations

from .approval_ticket import is_approval_ticket_valid
from .models import ActionRequest, ApprovalTicket, PolicyDecision
from .risk_classifier import classify_risk


def _allowlist_contains(action_request: ActionRequest, allowlist: set[str] | list[str] | tuple[str, ...] | None) -> bool:
    if allowlist is None:
        return False
    return action_request.action_type in set(allowlist)


def decide_policy(
    action_request: ActionRequest,
    approval_ticket: ApprovalTicket | None = None,
    allowlist: set[str] | list[str] | tuple[str, ...] | None = None,
) -> PolicyDecision:
    """Decide mock policy outcome without executing the requested action."""
    try:
        risk_tier = classify_risk(action_request)
    except (AttributeError, TypeError, ValueError) as exc:
        action_id = getattr(action_request, "action_id", "unknown")
        return PolicyDecision(
            action_id=action_id,
            risk_tier="unknown",
            decision="DENY",
            reason=f"malformed or unsafe action request: {exc}",
            required_controls=["deny", "mock_only"],
            human_approval_required=False,
            strong_approval_required=False,
            executed=False,
        )

    if risk_tier == "L0":
        return PolicyDecision(
            action_id=action_request.action_id,
            risk_tier=risk_tier,
            decision="ALLOW",
            reason="pure thought, analysis, draft, or simulation",
            required_controls=["mock_only"],
            executed=False,
        )
    if risk_tier == "L1":
        return PolicyDecision(
            action_id=action_request.action_id,
            risk_tier=risk_tier,
            decision="ALLOW_LOG",
            reason="read-only local inspection path",
            required_controls=["mock_only", "log_action"],
            executed=False,
        )
    if risk_tier == "L2":
        return PolicyDecision(
            action_id=action_request.action_id,
            risk_tier=risk_tier,
            decision="ALLOW_LOG_ROLLBACK_NOTE",
            reason="low-risk reversible local write path",
            required_controls=["mock_only", "log_action", "rollback_note"],
            executed=False,
        )
    if risk_tier == "L3":
        if _allowlist_contains(action_request, allowlist):
            return PolicyDecision(
                action_id=action_request.action_id,
                risk_tier=risk_tier,
                decision="ALLOW_LOG",
                reason="L3 action type is allowlisted for mock decision path",
                required_controls=["mock_only", "log_action", "allowlist_entry"],
                human_approval_required=False,
                executed=False,
            )
        if is_approval_ticket_valid(action_request, approval_ticket, required_strength="normal"):
            return PolicyDecision(
                action_id=action_request.action_id,
                risk_tier=risk_tier,
                decision="ALLOW_LOG",
                reason="valid human approval ticket satisfies L3 policy gate",
                required_controls=["mock_only", "log_action", "approval_ticket"],
                human_approval_required=True,
                executed=False,
            )
        return PolicyDecision(
            action_id=action_request.action_id,
            risk_tier=risk_tier,
            decision="REQUIRE_APPROVAL",
            reason="L3 action requires allowlist entry or valid human approval",
            required_controls=["mock_only", "log_action", "human_approval"],
            human_approval_required=True,
            executed=False,
        )

    if is_approval_ticket_valid(action_request, approval_ticket, required_strength="strong"):
        return PolicyDecision(
            action_id=action_request.action_id,
            risk_tier=risk_tier,
            decision="ALLOW_LOG",
            reason="valid strong approval ticket permits only a mock L4 decision path",
            required_controls=["mock_only", "log_action", "strong_approval_ticket"],
            human_approval_required=True,
            strong_approval_required=True,
            executed=False,
        )
    return PolicyDecision(
        action_id=action_request.action_id,
        risk_tier=risk_tier,
        decision="DENY_BY_DEFAULT",
        reason="L4 action is denied by default without valid strong approval",
        required_controls=["mock_only", "log_action", "strong_human_approval"],
        human_approval_required=True,
        strong_approval_required=True,
        executed=False,
    )
