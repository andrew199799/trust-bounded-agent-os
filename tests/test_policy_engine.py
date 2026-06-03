import json
import sys
from dataclasses import replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from tbao.approval_ticket import action_hash
from tbao.models import ActionRequest, ApprovalTicket
from tbao.policy_engine import decide_policy


def load_example(name: str) -> ActionRequest:
    path = Path(__file__).resolve().parents[1] / "examples" / ("action_" + "re" + "quests") / name
    return ActionRequest.from_dict(json.loads(path.read_text()))


def ticket_for(action: ActionRequest, strength: str = "normal") -> ApprovalTicket:
    return ApprovalTicket(
        ticket_id=f"ticket_{action.action_id}_{strength}",
        action_id=action.action_id,
        action_hash=action_hash(action),
        approver_id="human.reviewer",
        approval_strength=strength,
        scope="single_action",
        expires_at="2099-01-01T00:00:00Z",
        created_at="2026-06-03T00:00:00Z",
        decision="approve",
        note="mock approval for policy test",
    )


def test_l0_action_returns_allow():
    decision = decide_policy(load_example("l0_analysis.json"))
    assert decision.risk_tier == "L0"
    assert decision.decision == "ALLOW"
    assert decision.executed is False


def test_l1_action_returns_allow_log():
    decision = decide_policy(load_example("l1_read_file.json"))
    assert decision.risk_tier == "L1"
    assert decision.decision == "ALLOW_LOG"
    assert decision.executed is False


def test_l2_action_returns_allow_log_rollback_note():
    decision = decide_policy(load_example("l2_write_draft.json"))
    assert decision.risk_tier == "L2"
    assert decision.decision == "ALLOW_LOG_ROLLBACK_NOTE"
    assert decision.executed is False


def test_l3_code_commit_requires_approval_without_ticket():
    decision = decide_policy(load_example("l3_commit_code.json"))
    assert decision.risk_tier == "L3"
    assert decision.decision == "REQUIRE_APPROVAL"
    assert decision.human_approval_required is True
    assert decision.executed is False


def test_l3_code_commit_can_pass_with_normal_approval_ticket():
    action = load_example("l3_commit_code.json")
    decision = decide_policy(action, approval_ticket=ticket_for(action, "normal"))
    assert decision.risk_tier == "L3"
    assert decision.decision == "ALLOW_LOG"
    assert decision.executed is False


def test_l4_email_send_denied_by_default_without_ticket():
    decision = decide_policy(load_example("l4_send_email.json"))
    assert decision.risk_tier == "L4"
    assert decision.decision == "DENY_BY_DEFAULT"
    assert decision.strong_approval_required is True
    assert decision.executed is False


def test_l4_email_send_cannot_pass_with_normal_approval_ticket():
    action = load_example("l4_send_email.json")
    decision = decide_policy(action, approval_ticket=ticket_for(action, "normal"))
    assert decision.risk_tier == "L4"
    assert decision.decision == "DENY_BY_DEFAULT"
    assert decision.executed is False


def test_l4_email_send_can_pass_only_with_strong_approval_ticket():
    action = load_example("l4_send_email.json")
    decision = decide_policy(action, approval_ticket=ticket_for(action, "strong"))
    assert decision.risk_tier == "L4"
    assert decision.decision == "ALLOW_LOG"
    assert decision.strong_approval_required is True
    assert decision.executed is False
    assert "mock_only" in decision.required_controls


def test_malformed_action_returns_deny():
    action = replace(load_example("l0_analysis.json"), action_id="")
    decision = decide_policy(action)
    assert decision.decision == "DENY"
    assert decision.executed is False
