"""Risk classification for proposed local mock actions."""

from __future__ import annotations

from .models import (
    ActionRequest,
    BLAST_RADIUS_VALUES,
    REVERSIBILITY_VALUES,
    SENSITIVE_SURFACE_VALUES,
    SIDE_EFFECT_SCOPE_VALUES,
)


RISK_ORDER = ("L0", "L1", "L2", "L3", "L4")

L3_ACTION_TYPES = {
    "dependency.install",
    "config.modify",
    "code.commit",
    "memory.durable_write",
}

L4_ACTION_TYPES = {
    "file.delete",
    "payment.send",
    "trade.place",
    "email.send",
    "credential.access",
    "production.modify",
}


def _max_tier(current: str, candidate: str) -> str:
    return candidate if RISK_ORDER.index(candidate) > RISK_ORDER.index(current) else current


def _validate_request(action_request: ActionRequest) -> None:
    required_text = (
        action_request.action_id,
        action_request.agent_id,
        action_request.requested_by,
        action_request.action_type,
        action_request.target,
        action_request.intent,
        action_request.environment,
        action_request.timestamp,
    )
    if not all(isinstance(value, str) and value for value in required_text):
        raise ValueError("action request contains empty required text fields")
    if action_request.reversibility not in REVERSIBILITY_VALUES:
        raise ValueError("unknown reversibility value")
    if action_request.side_effect_scope not in SIDE_EFFECT_SCOPE_VALUES:
        raise ValueError("unknown side_effect_scope value")
    if action_request.blast_radius not in BLAST_RADIUS_VALUES:
        raise ValueError("unknown blast_radius value")
    if action_request.sensitive_surface not in SENSITIVE_SURFACE_VALUES:
        raise ValueError("unknown sensitive_surface value")
    if not isinstance(action_request.evidence, list):
        raise ValueError("evidence must be a list")


def classify_risk(action_request: ActionRequest) -> str:
    """Return the highest applicable L0-L4 risk tier for an action request."""
    _validate_request(action_request)

    scope = action_request.side_effect_scope
    if scope == "thought_only":
        risk_tier = "L0"
    elif scope == "local_read":
        risk_tier = "L1"
    elif scope == "local_write" and action_request.reversibility in {
        "reversible",
        "rollback_possible",
    }:
        risk_tier = "L2"
    elif scope in {"external_write", "production_mutation"}:
        risk_tier = "L4"
    else:
        risk_tier = "L3"

    if action_request.action_type in L3_ACTION_TYPES:
        risk_tier = _max_tier(risk_tier, "L3")
    if action_request.action_type in L4_ACTION_TYPES:
        risk_tier = _max_tier(risk_tier, "L4")

    if action_request.sensitive_surface in {"credentials", "financial", "production"}:
        risk_tier = _max_tier(risk_tier, "L4")
    elif action_request.sensitive_surface in {"pii", "legal", "health"}:
        risk_tier = _max_tier(risk_tier, "L3")

    if action_request.blast_radius == "public":
        risk_tier = _max_tier(risk_tier, "L3")
    elif action_request.blast_radius == "third_party":
        risk_tier = _max_tier(risk_tier, "L4")

    return risk_tier
