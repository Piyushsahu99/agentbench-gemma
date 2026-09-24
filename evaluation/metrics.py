"""Pure metric helpers for AgentBench-Gemma.

These functions intentionally avoid model-specific dependencies so the evaluator
can be reused with different agents.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Outcome:
    task_success: bool
    regression_free: Optional[bool] = None
    iterations: int = 0
    test_executions: int = 0
    tool_calls: int = 0
    files_changed: int = 0
    patch_lines: int = 0
    wall_time_seconds: Optional[float] = None
    input_tokens: Optional[int] = None
    output_tokens: Optional[int] = None
    budget_exhaustion: bool = False


def success_rate(outcomes: list[Outcome]) -> float:
    if not outcomes:
        return 0.0
    return sum(x.task_success for x in outcomes) / len(outcomes)


def regression_free_rate(outcomes: list[Outcome]) -> Optional[float]:
    known = [x for x in outcomes if x.regression_free is not None]
    if not known:
        return None
    return sum(bool(x.regression_free) for x in known) / len(known)


def mean_iterations(outcomes: list[Outcome]) -> float:
    return sum(x.iterations for x in outcomes) / len(outcomes) if outcomes else 0.0


def mean_test_executions(outcomes: list[Outcome]) -> float:
    return sum(x.test_executions for x in outcomes) / len(outcomes) if outcomes else 0.0


def agent_efficiency_score(
    outcomes: list[Outcome],
    iteration_weight: float = 0.05,
    test_weight: float = 0.02,
) -> float:
    """Experimental efficiency metric.

    This is deliberately labelled experimental. It should not be presented as a
    validated scientific metric until its sensitivity and robustness are tested.
    """
    if not outcomes:
        return 0.0

    values = []
    for x in outcomes:
        if not x.task_success:
            values.append(0.0)
            continue
        penalty = 1.0 + iteration_weight * x.iterations + test_weight * x.test_executions
        values.append(1.0 / penalty)

    return sum(values) / len(values)
