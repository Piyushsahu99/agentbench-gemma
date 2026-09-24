# AgentBench-Gemma

**A reproducible benchmark and trajectory-aware evaluation resource for agentic software engineering with Gemma models.**

AgentBench-Gemma is an open research resource for studying *how* coding agents solve repository-level software-engineering tasks, not only whether they eventually pass tests.

## Research question

> How do planning, tool use, self-repair, context selection, and stopping strategies affect the effectiveness and efficiency of Gemma-based software-engineering agents?

## Resource components

- **Benchmark tasks** — small, auditable repository-level tasks spanning bug fixing, feature implementation, refactoring, testing, and dependency/API changes.
- **Agent harness** — a common interface for baseline and agentic systems.
- **Trajectory schema** — records observable agent actions, tool calls, test outcomes, and file changes without requiring publication of private chain-of-thought.
- **Evaluation suite** — task success, regression detection, iteration count, test executions, token/cost accounting when available, latency, and patch size.
- **Ablation protocol** — controlled comparison of direct generation, tool use, planning, and self-repair.
- **Reproducible experiments** — configuration files and scripts intended for cloud execution.

## Status

This repository is an **active research prototype** for the Google - The Gemma 4 Developer Agent Paper Track. Results will be added only after experiments are actually run and independently checked.

## Planned benchmark protocol

1. Select permissively licensed, reproducible software tasks.
2. Freeze task descriptions and test commands before agent evaluation.
3. Run multiple agent configurations under the same task and compute budget.
4. Record observable trajectories and final patches.
5. Execute the repository's tests in a clean environment.
6. Report both success and efficiency metrics.
7. Perform ablations and error analysis.

## Reproducibility principles

- No credentials or private data in the repository.
- Record model identifier, prompt/configuration version, software versions, and execution environment.
- Separate benchmark construction from evaluation.
- Never report a result before the underlying experiment has been run.
- Verify licenses for repositories, datasets, and dependencies before redistribution.

## Repository layout

```
agentbench-gemma/
├── benchmark/          # Task specifications and metadata
├── agents/             # Agent interfaces and implementations
├── evaluation/         # Metrics and evaluation runners
├── experiments/        # Experiment configs and result artifacts
├── docs/               # Research design and methodology
├── tests/              # Unit tests for the resource
├── paper/              # Paper source and figures
├── scripts/             # Reproducibility utilities
└── README.md
```

## Research integrity

AgentBench-Gemma is a research resource, not a claim that any particular configuration is superior. Comparative conclusions will be supported by measured experiments, uncertainty/error analysis, and clearly stated limitations.

## License

Apache License 2.0. See [LICENSE](LICENSE).
