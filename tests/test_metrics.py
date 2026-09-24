from evaluation.metrics import Outcome, agent_efficiency_score, mean_iterations, success_rate


def test_success_rate():
    outcomes = [Outcome(True), Outcome(False), Outcome(True)]
    assert success_rate(outcomes) == 2 / 3


def test_mean_iterations():
    outcomes = [Outcome(True, iterations=2), Outcome(True, iterations=4)]
    assert mean_iterations(outcomes) == 3


def test_efficiency_rewards_fewer_iterations():
    fast = agent_efficiency_score([Outcome(True, iterations=2, test_executions=2)])
    slow = agent_efficiency_score([Outcome(True, iterations=10, test_executions=10)])
    assert fast > slow
