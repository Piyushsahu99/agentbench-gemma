# Research Design

## Working title

**AgentBench-Gemma: A Trajectory-Aware Benchmark for Evaluating Agentic Software Engineering**

## Motivation

Binary task success is necessary but incomplete for comparing coding agents. Two systems can both solve a task while differing substantially in number of failed attempts, test executions, edits, latency, and resource consumption.

AgentBench-Gemma therefore evaluates both **outcome** and **process-level observables**.

## Research questions

### RQ1
Does structured planning improve repository-level task success compared with direct generation?

### RQ2
Does test-driven self-repair improve recovery from implementation failures?

### RQ3
How does additional iteration affect success and efficiency?

### RQ4
Can context-selection strategies reduce resource use without materially reducing task success?

### RQ5
Which observable trajectory patterns are associated with successful versus unsuccessful runs?

## Initial configurations

### Direct
Task → model → patch

### Tool-use
Task → model → inspect/search/edit/test → patch

### Planning
Task → planner → implementation → tests

### Self-repair
Task → plan → implementation → tests → diagnose → repair → verify

The exact implementations and prompts will be frozen before the main comparison.

## Primary outcome metrics

- Task success rate
- Regression-free test pass rate

## Secondary metrics

- Number of agent iterations
- Number of test executions
- Number of files changed
- Patch size
- Wall-clock latency
- Token usage, when reliably available
- API/model cost, when applicable
- Failure category

## Proposed efficiency metric

We will investigate a normalized efficiency measure combining successful completion with resource use. The final formula will be selected **before the confirmatory experiment** and reported with sensitivity analysis rather than tuned to favor a desired result.

## Trajectory schema

We record observable events such as:

- model request
- repository inspection
- file read
- search
- file edit
- test execution
- test result
- diagnostic action
- final patch
- termination reason

Private chain-of-thought is not required for the benchmark and will not be collected as a research dependency.

## Benchmark construction principles

Tasks should:

1. Have a deterministic or well-defined verification procedure.
2. Be redistributable under a compatible license, or be referenced without redistributing restricted material.
3. Have a frozen task statement and test command.
4. Include enough metadata to reproduce the evaluation.
5. Avoid contamination where feasible.
6. Include a mixture of task types and difficulty levels.

## Experimental discipline

- Freeze task set and evaluation commands before comparing agents.
- Use identical compute/time budgets where practical.
- Run repeated trials when stochasticity materially affects results.
- Report failures and exclusions.
- Keep benchmark construction separate from result analysis.
- Never fabricate missing metrics.

## Current status

This document describes the pre-experiment protocol. It is intentionally not a results section.
