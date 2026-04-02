# LocalForgeAgents

**Free production-ready agent patterns and workflows for local LLMs (Ollama and open models).**

Everything in this repository is MIT-licensed and stays 100% open and free forever.

## Goal
Provide simple, copy-pasteable, hardware-aware agent recipes that work reliably on consumer GPUs/CPUs with Ollama and other open models. Focus on timeless patterns (tool calling, reasoning loops, context management) that adapt across model updates rather than fragile one-off prompts.

## Quick Start
1. Install Ollama and pull a model (e.g. `ollama pull llama3.2` or `qwen2.5`).
2. Clone or download this repo.
3. Run the examples in the `examples/` folder.

## Legal & Disclaimer
**This project is provided "AS IS", without warranty of any kind, express or implied.**

The maintainers and contributors are not liable for any damages or issues arising from use of these patterns. Use at your own risk. Examples are for educational and personal use. Do not use for illegal activities.

All code and patterns are original guidance optimized for local setups.

## Repository Structure
- `examples/` — Ready-to-run agent patterns
- `templates/` — Reusable code snippets
- `docs/` — Hardware notes and guides (coming soon)

## Current Patterns (v0.1)
- Basic tool calling
- ReAct-style reasoning loop (optimized for local inference speed)
- Simple multi-step agent
- Basic evaluation script

More patterns will be added regularly.

## Support the Project
If these patterns save you time, consider sponsoring via GitHub Sponsors (free to set up in repo settings). Every bit helps keep free updates coming.

## Contributing
See CONTRIBUTING.md (coming soon). Feel free to open issues or PRs.

---

Maintained as an independent free project.
