import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from tbao.ledger import ActionLedger
from tbao.models import ActionRequest
from tbao.policy_engine import decide_policy


def load_example(name: str) -> ActionRequest:
    path = Path(__file__).resolve().parents[1] / "examples" / ("action_" + "re" + "quests") / name
    return ActionRequest.from_dict(json.loads(path.read_text()))


def test_ledger_record_is_appended_for_policy_decision():
    action = load_example("l1_read_file.json")
    decision = decide_policy(action)
    ledger = ActionLedger()

    record = ledger.append(action, decision)

    assert len(ledger.records) == 1
    assert ledger.records[0] == record
    assert record.action_id == action.action_id
    assert record.decision == decision.decision


def test_ledger_record_always_has_executed_false():
    action = load_example("l4_delete_file.json")
    decision = decide_policy(action)
    ledger = ActionLedger()

    record = ledger.append(action, decision, mock_executed=True)

    assert record.executed is False
    assert record.mock_executed is True
