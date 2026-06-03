"""Dataclass models for the local mock Action Policy Kernel."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


RISK_TIERS = ("L0", "L1", "L2", "L3", "L4")

DECISIONS = (
    "ALLOW",
    "ALLOW_LOG",
    "ALLOW_LOG_ROLLBACK_NOTE",
    "REQUIRE_APPROVAL",
    "DENY_BY_DEFAULT",
    "DENY",
)

REVERSIBILITY_VALUES = (
    "none",
    "reversible",
    "rollback_possible",
    "irreversible",
)

SIDE_EFFECT_SCOPE_VALUES = (
    "thought_only",
    "local_read",
    "local_write",
    "external_write",
    "production_mutation",
)

BLAST_RADIUS_VALUES = (
    "self",
    "workspace",
    "team",
    "public",
    "third_party",
)

SENSITIVE_SURFACE_VALUES = (
    "none",
    "credentials",
    "pii",
    "financial",
    "legal",
    "health",
    "production",
)

APPROVAL_STRENGTH_VALUES = ("normal", "strong")
APPROVAL_DECISION_VALUES = ("approve", "deny")


@dataclass(frozen=True)
class ActionRequest:
    action_id: str
    agent_id: str
    requested_by: str
    action_type: str
    target: str
    intent: str
    evidence: list[str] = field(default_factory=list)
    environment: str = "local_mock"
    reversibility: str = "none"
    side_effect_scope: str = "thought_only"
    blast_radius: str = "self"
    sensitive_surface: str = "none"
    timestamp: str = ""

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ActionRequest":
        return cls(**data)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class PolicyDecision:
    action_id: str
    risk_tier: str
    decision: str
    reason: str
    required_controls: list[str] = field(default_factory=list)
    human_approval_required: bool = False
    strong_approval_required: bool = False
    executed: bool = False


@dataclass(frozen=True)
class ApprovalTicket:
    ticket_id: str
    action_id: str
    action_hash: str
    approver_id: str
    approval_strength: str
    scope: str
    expires_at: str
    created_at: str
    decision: str
    note: str = ""


@dataclass(frozen=True)
class ActionLedgerRecord:
    action_id: str
    agent_id: str
    risk_tier: str
    decision: str
    executed: bool
    mock_executed: bool
    approval_ticket_id: str | None
    reason: str
    timestamp: str
