# Benchmark Design

## Design principle

AgentBench-Gemma is designed as a **controlled research resource**, not as a replacement for large established benchmarks.

The initial release will use a small, auditable suite of self-contained tasks. Each task is designed so that:
- the starting repository is reproducible,
- the task statement is frozen before evaluation,
- tests define executable acceptance criteria,
- the fixture license permits redistribution,
- and the task can run in an isolated environment.

## Task categories

- bug_fix
- feature
- refactor
- test
- api_change

## Task record

Each task should contain:

- task_id
- version
- category
- language
- difficulty
- description
- setup_command
- test_command
- expected_files
- acceptance_tests
- license
- source
- checksum

## Evaluation rule

A task is successful only when its acceptance tests pass in a clean evaluation environment and no protected regression test fails.

## Dataset growth

Start with 5 internal validation tasks. Expand to 10, then 30+, only after the harness is stable. The benchmark should never be inflated merely to increase the apparent size of the resource.

## External benchmark relationship

SWE-bench and related repository-level benchmarks remain important external reference points. AgentBench-Gemma's contribution is the controlled analysis of workflow factors and observable trajectories rather than a claim to replace those benchmarks.
