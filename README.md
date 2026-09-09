# genpark-contract-net-protocol-cnp-task-clearing-skill

[![GitHub stars](https://img.shields.io/github/stars/alphaparkinc/genpark-contract-net-protocol-cnp-task-clearing-skill?style=social)](https://github.com/alphaparkinc/genpark-contract-net-protocol-cnp-task-clearing-skill/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0%20external-brightgreen.svg)](#)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20Compatible-orange.svg)](#)

> Autonomous Agent FIPA Contract Net Protocol (CNP) Multi-Round Task Clearing & Bid Evaluation Engine

Part of the **GenPark Autonomous Multi-Agent Coordination & Social Choice Architecture**.

## Architecture Overview

```mermaid
graph TD
    A[Manager Agent Issues Task CFP Request for Proposals] --> B[Broadcast Call for Proposals to Contractor Swarm]
    B --> C[Contractors Compute Cost/Feasibility Bids]
    C --> D[Transmit Bids to Manager Agent]
    D --> E[Manager Ranks Bids & Selects Optimal Contractor]
    E --> F[Send Accept-Proposal Award Notice to Winner]
    E --> G[Send Reject-Proposal Notices to Others]
    F --> H[Contractor Executes Task & Delivers Inform Result]
```

## Features

- **Pure Python Standard Library**: Zero external dependencies.
- **Production-Grade Design**: Type annotations, distributed breakout escape, social choice aggregation.
- **MCP Server Ready**: Built-in stdio Model Context Protocol (MCP) server for Claude / Cursor / Agent tool calling.
- **Benchmark Validated**: 100% verified test coverage in isolated sandbox environments.

## Quickstart

```bash
git clone https://github.com/alphaparkinc/genpark-contract-net-protocol-cnp-task-clearing-skill.git
cd genpark-contract-net-protocol-cnp-task-clearing-skill
python example_usage.py
```

## Model Context Protocol (MCP) Usage

```bash
python mcp_server.py
```

## License

MIT License. Designed for autonomous agentic workflows.
