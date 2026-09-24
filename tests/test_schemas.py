import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_task_schema_is_valid_json():
    data = json.loads((ROOT / "benchmark/task.schema.json").read_text())
    assert data["title"] == "AgentBench-Gemma Task"

def test_trajectory_schema_is_valid_json():
    data = json.loads((ROOT / "evaluation/trajectory.schema.json").read_text())
    assert data["title"] == "AgentBench-Gemma Observable Trajectory Event"
