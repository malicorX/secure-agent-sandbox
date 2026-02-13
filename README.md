# Secure Agent Sandbox

Secure Agent Sandbox is an open-source, reproducible evaluation testbed for **tool-using, multi-agent systems**.

It combines:
- a **2D multi-agent environment** with **simultaneous stepping** and **local observations**
- a **capability-based tool layer** (simulated tools by default)
- a **benchmark suite + evaluation harness** with deterministic seeds, structured logs, and replay artifacts

## Why
Tool-using agents (shell/network/package installs) increase the attack surface. Today’s evaluations often measure only task success, not:
- forbidden actions under pressure
- boundary violations / policy violations
- coordination-related risk
- safety regressions across prompt/framework changes

This project provides a controlled sandbox to measure these properties before connecting agents to real machines.

## Status
Early bootstrap. Initial targets:
- env core (simultaneous + local obs)
- task DSL + baseline tasks
- simulated tool layer + policy engine
- replay + regression harness
- optional hardened sandbox runner (off by default)

## Repository layout (planned)
- `src/secure_agent_sandbox/` core package
- `src/secure_agent_sandbox/env/` environment + stepping rules
- `src/secure_agent_sandbox/tools/` tool capability layer (simulated + optional sandbox)
- `src/secure_agent_sandbox/bench/` benchmark runner, metrics, replay
- `tasks/` task definitions
- `docs/` documentation

## Safety notes
- Default benchmark uses **simulated tools only**.
- Any “real tool execution” mode (if enabled) must run in strict isolation and is off by default.

## License
Pick **MIT** or **Apache-2.0** and add the appropriate `LICENSE` file.

## Quickstart (placeholder)
```bash
uv pip install -e .
python -m secure_agent_sandbox --help
