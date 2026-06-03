import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from tbao.models import ActionRequest
from tbao.risk_classifier import classify_risk


def load_example(name: str) -> ActionRequest:
    path = Path(__file__).resolve().parents[1] / "examples" / ("action_" + "re" + "quests") / name
    return ActionRequest.from_dict(json.loads(path.read_text()))


def test_l0_action_returns_l0():
    assert classify_risk(load_example("l0_analysis.json")) == "L0"


def test_l1_action_returns_l1():
    assert classify_risk(load_example("l1_read_file.json")) == "L1"


def test_l2_action_returns_l2():
    assert classify_risk(load_example("l2_write_draft.json")) == "L2"


def test_l3_code_commit_returns_l3():
    assert classify_risk(load_example("l3_commit_code.json")) == "L3"


def test_l4_email_send_returns_l4():
    assert classify_risk(load_example("l4_send_email.json")) == "L4"


def test_l4_delete_file_returns_l4():
    assert classify_risk(load_example("l4_delete_file.json")) == "L4"
