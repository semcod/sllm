# sllm


## AI Cost Tracking

![PyPI](https://img.shields.io/badge/pypi-costs-blue) ![Version](https://img.shields.io/badge/version-0.1.5-blue) ![Python](https://img.shields.io/badge/python-3.9+-blue) ![License](https://img.shields.io/badge/license-Apache--2.0-green)
![AI Cost](https://img.shields.io/badge/AI%20Cost-$0.65-orange) ![Human Time](https://img.shields.io/badge/Human%20Time-2.0h-blue) ![Model](https://img.shields.io/badge/Model-openrouter%2Fqwen%2Fqwen3--coder--next-lightgrey)

- 🤖 **LLM usage:** $0.6531 (4 commits)
- 👤 **Human dev:** ~$200 (2.0h @ $100/h, 30min dedup)

Generated on 2026-06-03 using [openrouter/qwen/qwen3-coder-next](https://openrouter.ai/qwen/qwen3-coder-next)

---

Shell LLM control plane for the semcod/coru ecosystem.

SLLM owns the shell-client side of LLM automation: clients such as `aider`,
`claude`, `codex`, `gemini`, `qwen-code`, `opencode`, and `devin`. GUI/IDE
chat control stays in `koruide` and the existing Koru autopilot socket path.

## Commands

```bash
sllm clients
sllm drive --client aider --prompt "Refactor ticket PLF-1"          # dry-run
sllm drive --client aider --prompt "Refactor ticket PLF-1" --execute
sllm nlp "aider: napraw testy dla kolejki"                          # NLP -> DSL
sllm validate                                                       # ecosystem hooks + intents
```

`sllm drive` always saves the prompt under `.koru/sllm/prompts/` before it
executes or prints a dry-run plan.

Client notes:

- [`aider`](docs/clients/aider.md)
- [`claude-code`](docs/clients/claude-code.md)
- [`aider Docker autoloop`](docs/clients/aider-docker-autoloop.md)

## Optional ecosystem integrations

```bash
pip install -e ".[nlp]"       # nlp2dsl SDK bridge
pip install -e ".[intent]"    # intract intent validation hooks
pip install -e ".[ecosystem]" # nlp2dsl + intract + redsl + proxym + llx, Python 3.11+
```

The `nlp2dsl` bridge is opt-in at runtime:

```bash
export SLLM_NLP2DSL=1
export NLP2DSL_BACKEND_URL=http://localhost:8010
sllm nlp "uruchom claude dla ticketu PLF-123"
```

Without the service, SLLM falls back to a deterministic local parser.

`sllm validate` reports optional package availability and exposes the
`@intract.v1` intent contract used to validate `sllm.drive` DSL before shell
execution.


## License

Licensed under Apache-2.0.
