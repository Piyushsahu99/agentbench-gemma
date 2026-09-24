# Evaluation Metrics

## Outcome metrics

### Task Success
A task is successful when the frozen verification procedure passes and no required regression check fails.

### Regression-Free Success
A stricter outcome requiring the target tests and the designated regression suite to pass.

## Process metrics

- Iterations
- Test executions
- Files changed
- Lines added/deleted
- Wall-clock duration
- Token usage
- Estimated cost
- Termination reason

## Failure taxonomy

- F1: incorrect implementation
- F2: incomplete implementation
- F3: regression
- F4: test misuse
- F5: context/repository misunderstanding
- F6: tool error
- F7: environment/dependency failure
- F8: timeout or budget exhaustion

## Metric design rule

Any composite metric must be defined before the confirmatory comparison and accompanied by its component metrics. Composite scores must not replace raw outcomes.
