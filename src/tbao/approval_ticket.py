"""Approval ticket validation for local mock policy decisions."""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict
from datetime import datetime, timezone

from .models import (
    APPROVAL_DECISION_VALUES,
    APPROVAL_STRENGTH_VALUES,
    ActionRequest,
    ApprovalTicket,
)


def _parse_timestamp(value: str) -> datetime:
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def action_hash(action_request: ActionRequest) -> str:
    """Bind approval to the exact action request payload."""
    payload = json.dumps(asdict(action_request), sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def is_approval_ticket_valid(
    action_request: ActionRequest,
    approval_ticket: ApprovalTicket | None,
    required_strength: str = "normal",
    now: datetime | None = None,
) -> bool:
    if approval_ticket is None:
        return False
    if required_strength not in APPROVAL_STRENGTH_VALUES:
        return False
    if approval_ticket.approval_strength not in APPROVAL_STRENGTH_VALUES:
        return False
    if approval_ticket.decision not in APPROVAL_DECISION_VALUES:
        return False
    if approval_ticket.decision != "approve":
        return False
    if approval_ticket.action_id != action_request.action_id:
        return False
    if approval_ticket.approver_id == action_request.agent_id:
        return False
    if approval_ticket.action_hash != action_hash(action_request):
        return False
    if required_strength == "strong" and approval_ticket.approval_strength != "strong":
        return False

    current_time = now or datetime.now(timezone.utc)
    try:
        expires_at = _parse_timestamp(approval_ticket.expires_at)
    except ValueError:
        return False
    return expires_at > current_time
