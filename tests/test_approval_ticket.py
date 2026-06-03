import json
import sys
from dataclasses import replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from tbao.approval_ticket import action_hash, is_approval_ticket_valid
from tbao.models import ActionRequest, ApprovalTicket


def load_example(name: str) -> ActionRequest:
    path = Path(__file__).resolve().parents[1] / "examples" / ("action_" + "re" + "quests") / name
    return ActionRequest.from_dict(json.loads(path.read_text()))


def ticket_for(action: ActionRequest, **overrides) -> ApprovalTicket:
    data = {
        "ticket_id": "ticket_valid",
        "action_id": action.action_id,
        "action_hash": action_hash(action),
        "approver_id": "human.reviewer",
        "approval_strength": "normal",
        "scope": "single_action",
        "expires_at": "2099-01-01T00:00:00Z",
        "created_at": "2026-06-03T00:00:00Z",
        "decision": "approve",
        "note": "mock approval",
    }
    data.update(overrides)
    return ApprovalTicket(**data)


def test_valid_normal_approval_ticket_authorizes_l3_strength():
    action = load_example("l3_commit_code.json")
    assert is_approval_ticket_valid(action, ticket_for(action), required_strength="normal")


def test_approver_id_equal_agent_id_invalidates_ticket():
    action = load_example("l3_commit_code.json")
    ticket = ticket_for(action, approver_id=action.agent_id)
    assert not is_approval_ticket_valid(action, ticket, required_strength="normal")


def test_expired_approval_ticket_invalidates_authorization():
    action = load_example("l3_commit_code.json")
    ticket = ticket_for(action, expires_at="2000-01-01T00:00:00Z")
    assert not is_approval_ticket_valid(action, ticket, required_strength="normal")


def test_changed_action_payload_invalidates_old_approval_ticket():
    action = load_example("l3_commit_code.json")
    ticket = ticket_for(action)
    changed_action = replace(action, intent="Changed intent after approval.")
    assert action_hash(changed_action) != ticket.action_hash
    assert not is_approval_ticket_valid(changed_action, ticket, required_strength="normal")


def test_strong_required_rejects_normal_ticket():
    action = load_example("l4_send_email.json")
    ticket = ticket_for(action, approval_strength="normal")
    assert not is_approval_ticket_valid(action, ticket, required_strength="strong")


def test_strong_required_accepts_strong_ticket():
    action = load_example("l4_send_email.json")
    ticket = ticket_for(action, approval_strength="strong")
    assert is_approval_ticket_valid(action, ticket, required_strength="strong")
