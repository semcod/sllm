# sillm

SUMD - Structured Unified Markdown Descriptor for AI-aware project refactorization

## Contents

- [Metadata](#metadata)
- [Architecture](#architecture)
- [Dependencies](#dependencies)
- [Call Graph](#call-graph)
- [Test Contracts](#test-contracts)
- [Refactoring Analysis](#refactoring-analysis)
- [Intent](#intent)

## Metadata

- **name**: `clilm`
- **version**: `0.1.26`
- **python_requires**: `>=3.11`
- **license**: Apache-2.0
- **ai_model**: `openrouter/deep/deep-v4-pro`
- **ecosystem**: SUMD + DOQL + testql + taskfile
- **generated_from**: pyproject.toml, testql(1), app.doql.less, goal.yaml, .env.example, project/(5 analysis files)

## Architecture

```
SUMD (description) → DOQL/source (code) → taskfile (automation) → testql (verification)
```

### DOQL Application Declaration (`app.doql.less`)

```less markpact:doql path=app.doql.less
// LESS format — define @variables here as needed

app {
  name: clilm;
  version: 0.1.26;
}

dependencies {
  dev: "build>=1.0,<2.0, pytest>=8.0,<10.0, ruff>=0.11,<0.16, twine>=6.0,<7.0, goal>=2.1.0, costs>=0.1.20, pfix>=0.1.60";
}

interface[type="cli"] {
  framework: argparse;
}
interface[type="cli"] page[name="sillm"] {
  entry: sillm.cli:main;
}
interface[type="cli"] page[name="sllm"] {
  entry: sillm.cli:main;
}

integration[name="nlp"] {
  type: api;
}

tests {
  import: testql-scenarios/**/*.testql.toon.yaml;
}

env_vars {
  keys: OPENROUTER_API_KEY, LLM_MODEL, PFIX_AUTO_APPLY, PFIX_AUTO_INSTALL_DEPS, PFIX_AUTO_RESTART, PFIX_MAX_RETRIES, PFIX_DRY_RUN, PFIX_ENABLED, PFIX_GIT_COMMIT, PFIX_GIT_PREFIX, PFIX_CREATE_BACKUPS, SILLM_DEFAULT_CLIENT, SILLM_NLP2DSL;
}

deploy {
  target: pip;
}

environment[name="local"] {
  runtime: python;
  env_file: .env;
  template_file: .env.example;
  python_version: >=3.11;
  vars: LLM_MODEL, OPENROUTER_API_KEY, PFIX_AUTO_APPLY, PFIX_AUTO_INSTALL_DEPS, PFIX_AUTO_RESTART, PFIX_CREATE_BACKUPS, PFIX_DRY_RUN, PFIX_ENABLED, PFIX_GIT_COMMIT, PFIX_GIT_PREFIX, PFIX_MAX_RETRIES;
  runtime_llm: OPENROUTER_API_KEY;
  runtime_pfix: PFIX_AUTO_APPLY, PFIX_AUTO_INSTALL_DEPS, PFIX_AUTO_RESTART, PFIX_CREATE_BACKUPS, PFIX_DRY_RUN, PFIX_ENABLED, PFIX_GIT_COMMIT, PFIX_GIT_PREFIX, PFIX_MAX_RETRIES;
}
```

## Dependencies

### Runtime

*(see pyproject.toml)*

### Development

```text markpact:deps python scope=dev
build>=1.0,<2.0
pytest>=8.0,<10.0
ruff>=0.11,<0.16
twine>=6.0,<7.0
goal>=2.1.0
costs>=0.1.20
pfix>=0.1.60
```

## Call Graph

*36 nodes · 46 edges · 6 modules · CC̄=3.4*

### Hubs (by degree)

| Function | CC | in | out | total |
|----------|----|----|-----|-------|
| `_intent_from_nlp2dsl` *(in src.sillm.nlp)* | 15 ⚠ | 1 | 25 | **26** |
| `_build_parser` *(in src.sillm.cli)* | 1 | 1 | 25 | **26** |
| `launch_koru_agent` *(in src.sillm.compat)* | 8 | 0 | 17 | **17** |
| `_print` *(in src.sillm.cli)* | 6 | 7 | 10 | **17** |
| `_nlp` *(in src.sillm.cli)* | 5 | 1 | 13 | **14** |
| `build_drive_plan` *(in src.sillm.controller)* | 3 | 2 | 11 | **13** |
| `drive_shell_llm` *(in src.sillm.controller)* | 10 ⚠ | 3 | 10 | **13** |
| `_drive` *(in src.sillm.cli)* | 5 | 1 | 11 | **12** |

```toon markpact:analysis path=project/calls.toon.yaml
# code2llm call graph | /home/tom/github/semcod/sllm
# generated in 0.02s
# nodes: 36 | edges: 46 | modules: 6
# CC̄=3.4

HUBS[20]:
  src.sillm.nlp._intent_from_nlp2dsl
    CC=15  in:1  out:25  total:26
  src.sillm.cli._build_parser
    CC=1  in:1  out:25  total:26
  src.sillm.compat.launch_koru_agent
    CC=8  in:0  out:17  total:17
  src.sillm.cli._print
    CC=6  in:7  out:10  total:17
  src.sillm.cli._nlp
    CC=5  in:1  out:13  total:14
  src.sillm.controller.build_drive_plan
    CC=3  in:2  out:11  total:13
  src.sillm.controller.drive_shell_llm
    CC=10  in:3  out:10  total:13
  src.sillm.cli._drive
    CC=5  in:1  out:11  total:12
  src.sillm.validation._validate_raw_dsl
    CC=9  in:1  out:11  total:12
  src.sillm.cli.main
    CC=6  in:0  out:11  total:11
  src.sillm.registry.normalize_client_id
    CC=1  in:6  out:4  total:10
  src.sillm.controller.save_prompt
    CC=2  in:2  out:7  total:9
  src.sillm.validation.validate_intent
    CC=4  in:1  out:8  total:9
  src.sillm.compat.detect_koru_agent_rows
    CC=5  in:0  out:9  total:9
  src.sillm.validation.validate_intent_contracts
    CC=4  in:1  out:6  total:7
  src.sillm.registry.get_client_spec
    CC=3  in:6  out:1  total:7
  src.sillm.nlp._client_from_text
    CC=6  in:1  out:6  total:7
  src.sillm.cli._normalize_extra_arg_tokens
    CC=5  in:1  out:5  total:6
  src.sillm.nlp.intent_from_text
    CC=3  in:1  out:5  total:6
  src.sillm.nlp._strip_drive_prefix
    CC=5  in:1  out:5  total:6

MODULES:
  src.sillm.cli  [7 funcs]
    _build_parser  CC=1  out:25
    _drive  CC=5  out:11
    _nlp  CC=5  out:13
    _normalize_extra_arg_tokens  CC=5  out:5
    _print  CC=6  out:10
    _read_prompt  CC=4  out:4
    main  CC=6  out:11
  src.sillm.compat  [9 funcs]
    autopilot_backend_for_client  CC=2  out:1
    detect_koru_agent_rows  CC=5  out:9
    drive_koru_chat  CC=1  out:3
    is_client_available  CC=2  out:3
    is_shell_llm_client  CC=1  out:1
    launch_koru_agent  CC=8  out:17
    shell_client_ids  CC=2  out:2
    shell_process_patterns  CC=2  out:2
    tool_registry_entries  CC=4  out:4
  src.sillm.controller  [8 funcs]
    _prompt_root  CC=2  out:3
    _resolve_command  CC=2  out:3
    _resolve_spec  CC=2  out:2
    _timeout_value  CC=3  out:1
    build_drive_plan  CC=3  out:11
    drive_shell_llm  CC=10  out:10
    result_from_error  CC=1  out:2
    save_prompt  CC=2  out:7
  src.sillm.nlp  [4 funcs]
    _client_from_text  CC=6  out:6
    _intent_from_nlp2dsl  CC=15  out:25
    _strip_drive_prefix  CC=5  out:5
    intent_from_text  CC=3  out:5
  src.sillm.registry  [4 funcs]
    detect_clients  CC=4  out:3
    get_client_spec  CC=3  out:1
    iter_client_specs  CC=1  out:0
    normalize_client_id  CC=1  out:4
  src.sillm.validation  [4 funcs]
    _validate_raw_dsl  CC=9  out:11
    ecosystem_status  CC=2  out:4
    validate_intent  CC=4  out:8
    validate_intent_contracts  CC=4  out:6

EDGES:
  src.sillm.cli._drive → src.sillm.cli._print
  src.sillm.cli._drive → src.sillm.controller.drive_shell_llm
  src.sillm.cli._drive → src.sillm.controller.result_from_error
  src.sillm.cli._drive → src.sillm.cli._read_prompt
  src.sillm.cli._nlp → src.sillm.nlp.intent_from_text
  src.sillm.cli._nlp → src.sillm.validation.validate_intent
  src.sillm.cli._nlp → src.sillm.controller.drive_shell_llm
  src.sillm.cli._nlp → src.sillm.cli._print
  src.sillm.cli.main → src.sillm.cli._normalize_extra_arg_tokens
  src.sillm.cli.main → src.sillm.cli._print
  src.sillm.cli.main → src.sillm.cli._drive
  src.sillm.cli.main → src.sillm.cli._nlp
  src.sillm.cli.main → src.sillm.cli._build_parser
  src.sillm.cli.main → src.sillm.registry.detect_clients
  src.sillm.controller.save_prompt → src.sillm.controller._prompt_root
  src.sillm.controller._resolve_spec → src.sillm.registry.get_client_spec
  src.sillm.controller.build_drive_plan → src.sillm.controller._resolve_spec
  src.sillm.controller.build_drive_plan → src.sillm.controller._resolve_command
  src.sillm.controller.build_drive_plan → src.sillm.controller.save_prompt
  src.sillm.controller.drive_shell_llm → src.sillm.controller.build_drive_plan
  src.sillm.controller.drive_shell_llm → src.sillm.controller._timeout_value
  src.sillm.registry.get_client_spec → src.sillm.registry.normalize_client_id
  src.sillm.registry.detect_clients → src.sillm.registry.normalize_client_id
  src.sillm.validation.validate_intent → src.sillm.registry.get_client_spec
  src.sillm.validation.validate_intent → src.sillm.validation._validate_raw_dsl
  src.sillm.validation._validate_raw_dsl → src.sillm.registry.normalize_client_id
  src.sillm.validation.ecosystem_status → src.sillm.validation.validate_intent_contracts
  src.sillm.nlp._client_from_text → src.sillm.registry.iter_client_specs
  src.sillm.nlp._client_from_text → src.sillm.registry.normalize_client_id
  src.sillm.nlp._intent_from_nlp2dsl → src.sillm.registry.normalize_client_id
  src.sillm.nlp.intent_from_text → src.sillm.nlp._client_from_text
  src.sillm.nlp.intent_from_text → src.sillm.nlp._intent_from_nlp2dsl
  src.sillm.nlp.intent_from_text → src.sillm.registry.get_client_spec
  src.sillm.nlp.intent_from_text → src.sillm.nlp._strip_drive_prefix
  src.sillm.compat.is_shell_llm_client → src.sillm.registry.get_client_spec
  src.sillm.compat.is_client_available → src.sillm.registry.get_client_spec
  src.sillm.compat.shell_client_ids → src.sillm.registry.iter_client_specs
  src.sillm.compat.shell_process_patterns → src.sillm.registry.iter_client_specs
  src.sillm.compat.tool_registry_entries → src.sillm.registry.iter_client_specs
  src.sillm.compat.autopilot_backend_for_client → src.sillm.compat.is_shell_llm_client
  src.sillm.compat.detect_koru_agent_rows → src.sillm.registry.detect_clients
  src.sillm.compat.drive_koru_chat → src.sillm.controller.drive_shell_llm
  src.sillm.compat.launch_koru_agent → src.sillm.registry.normalize_client_id
  src.sillm.compat.launch_koru_agent → src.sillm.registry.get_client_spec
  src.sillm.compat.launch_koru_agent → src.sillm.controller.save_prompt
  src.sillm.compat.launch_koru_agent → src.sillm.controller.build_drive_plan
```

## Test Contracts

*Scenarios as contract signatures — what the system guarantees.*

### Cli (1)

**`CLI Command Tests`**

## Refactoring Analysis

*Pre-refactoring snapshot — use this section to identify targets. Generated from `project/` toon files.*

### Call Graph & Complexity (`project/calls.toon.yaml`)

```toon markpact:analysis path=project/calls.toon.yaml
# code2llm call graph | /home/tom/github/semcod/sllm
# generated in 0.02s
# nodes: 36 | edges: 46 | modules: 6
# CC̄=3.4

HUBS[20]:
  src.sillm.nlp._intent_from_nlp2dsl
    CC=15  in:1  out:25  total:26
  src.sillm.cli._build_parser
    CC=1  in:1  out:25  total:26
  src.sillm.compat.launch_koru_agent
    CC=8  in:0  out:17  total:17
  src.sillm.cli._print
    CC=6  in:7  out:10  total:17
  src.sillm.cli._nlp
    CC=5  in:1  out:13  total:14
  src.sillm.controller.build_drive_plan
    CC=3  in:2  out:11  total:13
  src.sillm.controller.drive_shell_llm
    CC=10  in:3  out:10  total:13
  src.sillm.cli._drive
    CC=5  in:1  out:11  total:12
  src.sillm.validation._validate_raw_dsl
    CC=9  in:1  out:11  total:12
  src.sillm.cli.main
    CC=6  in:0  out:11  total:11
  src.sillm.registry.normalize_client_id
    CC=1  in:6  out:4  total:10
  src.sillm.controller.save_prompt
    CC=2  in:2  out:7  total:9
  src.sillm.validation.validate_intent
    CC=4  in:1  out:8  total:9
  src.sillm.compat.detect_koru_agent_rows
    CC=5  in:0  out:9  total:9
  src.sillm.validation.validate_intent_contracts
    CC=4  in:1  out:6  total:7
  src.sillm.registry.get_client_spec
    CC=3  in:6  out:1  total:7
  src.sillm.nlp._client_from_text
    CC=6  in:1  out:6  total:7
  src.sillm.cli._normalize_extra_arg_tokens
    CC=5  in:1  out:5  total:6
  src.sillm.nlp.intent_from_text
    CC=3  in:1  out:5  total:6
  src.sillm.nlp._strip_drive_prefix
    CC=5  in:1  out:5  total:6

MODULES:
  src.sillm.cli  [7 funcs]
    _build_parser  CC=1  out:25
    _drive  CC=5  out:11
    _nlp  CC=5  out:13
    _normalize_extra_arg_tokens  CC=5  out:5
    _print  CC=6  out:10
    _read_prompt  CC=4  out:4
    main  CC=6  out:11
  src.sillm.compat  [9 funcs]
    autopilot_backend_for_client  CC=2  out:1
    detect_koru_agent_rows  CC=5  out:9
    drive_koru_chat  CC=1  out:3
    is_client_available  CC=2  out:3
    is_shell_llm_client  CC=1  out:1
    launch_koru_agent  CC=8  out:17
    shell_client_ids  CC=2  out:2
    shell_process_patterns  CC=2  out:2
    tool_registry_entries  CC=4  out:4
  src.sillm.controller  [8 funcs]
    _prompt_root  CC=2  out:3
    _resolve_command  CC=2  out:3
    _resolve_spec  CC=2  out:2
    _timeout_value  CC=3  out:1
    build_drive_plan  CC=3  out:11
    drive_shell_llm  CC=10  out:10
    result_from_error  CC=1  out:2
    save_prompt  CC=2  out:7
  src.sillm.nlp  [4 funcs]
    _client_from_text  CC=6  out:6
    _intent_from_nlp2dsl  CC=15  out:25
    _strip_drive_prefix  CC=5  out:5
    intent_from_text  CC=3  out:5
  src.sillm.registry  [4 funcs]
    detect_clients  CC=4  out:3
    get_client_spec  CC=3  out:1
    iter_client_specs  CC=1  out:0
    normalize_client_id  CC=1  out:4
  src.sillm.validation  [4 funcs]
    _validate_raw_dsl  CC=9  out:11
    ecosystem_status  CC=2  out:4
    validate_intent  CC=4  out:8
    validate_intent_contracts  CC=4  out:6

EDGES:
  src.sillm.cli._drive → src.sillm.cli._print
  src.sillm.cli._drive → src.sillm.controller.drive_shell_llm
  src.sillm.cli._drive → src.sillm.controller.result_from_error
  src.sillm.cli._drive → src.sillm.cli._read_prompt
  src.sillm.cli._nlp → src.sillm.nlp.intent_from_text
  src.sillm.cli._nlp → src.sillm.validation.validate_intent
  src.sillm.cli._nlp → src.sillm.controller.drive_shell_llm
  src.sillm.cli._nlp → src.sillm.cli._print
  src.sillm.cli.main → src.sillm.cli._normalize_extra_arg_tokens
  src.sillm.cli.main → src.sillm.cli._print
  src.sillm.cli.main → src.sillm.cli._drive
  src.sillm.cli.main → src.sillm.cli._nlp
  src.sillm.cli.main → src.sillm.cli._build_parser
  src.sillm.cli.main → src.sillm.registry.detect_clients
  src.sillm.controller.save_prompt → src.sillm.controller._prompt_root
  src.sillm.controller._resolve_spec → src.sillm.registry.get_client_spec
  src.sillm.controller.build_drive_plan → src.sillm.controller._resolve_spec
  src.sillm.controller.build_drive_plan → src.sillm.controller._resolve_command
  src.sillm.controller.build_drive_plan → src.sillm.controller.save_prompt
  src.sillm.controller.drive_shell_llm → src.sillm.controller.build_drive_plan
  src.sillm.controller.drive_shell_llm → src.sillm.controller._timeout_value
  src.sillm.registry.get_client_spec → src.sillm.registry.normalize_client_id
  src.sillm.registry.detect_clients → src.sillm.registry.normalize_client_id
  src.sillm.validation.validate_intent → src.sillm.registry.get_client_spec
  src.sillm.validation.validate_intent → src.sillm.validation._validate_raw_dsl
  src.sillm.validation._validate_raw_dsl → src.sillm.registry.normalize_client_id
  src.sillm.validation.ecosystem_status → src.sillm.validation.validate_intent_contracts
  src.sillm.nlp._client_from_text → src.sillm.registry.iter_client_specs
  src.sillm.nlp._client_from_text → src.sillm.registry.normalize_client_id
  src.sillm.nlp._intent_from_nlp2dsl → src.sillm.registry.normalize_client_id
  src.sillm.nlp.intent_from_text → src.sillm.nlp._client_from_text
  src.sillm.nlp.intent_from_text → src.sillm.nlp._intent_from_nlp2dsl
  src.sillm.nlp.intent_from_text → src.sillm.registry.get_client_spec
  src.sillm.nlp.intent_from_text → src.sillm.nlp._strip_drive_prefix
  src.sillm.compat.is_shell_llm_client → src.sillm.registry.get_client_spec
  src.sillm.compat.is_client_available → src.sillm.registry.get_client_spec
  src.sillm.compat.shell_client_ids → src.sillm.registry.iter_client_specs
  src.sillm.compat.shell_process_patterns → src.sillm.registry.iter_client_specs
  src.sillm.compat.tool_registry_entries → src.sillm.registry.iter_client_specs
  src.sillm.compat.autopilot_backend_for_client → src.sillm.compat.is_shell_llm_client
  src.sillm.compat.detect_koru_agent_rows → src.sillm.registry.detect_clients
  src.sillm.compat.drive_koru_chat → src.sillm.controller.drive_shell_llm
  src.sillm.compat.launch_koru_agent → src.sillm.registry.normalize_client_id
  src.sillm.compat.launch_koru_agent → src.sillm.registry.get_client_spec
  src.sillm.compat.launch_koru_agent → src.sillm.controller.save_prompt
  src.sillm.compat.launch_koru_agent → src.sillm.controller.build_drive_plan
```

### Code Analysis (`project/analysis.toon.yaml`)

```toon markpact:analysis path=project/analysis.toon.yaml
# code2llm | 13f 1776L | python:8,yaml:2,txt:1,shell:1,toml:1 | 2026-06-08
# generated in 0.00s
# CC̅=3.4 | critical:1/46 | dups:0 | cycles:0

HEALTH[1]:
  🟡 CC    _intent_from_nlp2dsl CC=15 (limit:15)

REFACTOR[1]:
  1. split 1 high-CC methods  (CC>15)

PIPELINES[15]:
  [1] Src [main]: main → _normalize_extra_arg_tokens
      PURITY: 100% pure
  [2] Src [shell_preview]: shell_preview
      PURITY: 100% pure
  [3] Src [to_dict]: to_dict
      PURITY: 100% pure
  [4] Src [to_dict]: to_dict
      PURITY: 100% pure
  [5] Src [command_path]: command_path
      PURITY: 100% pure
  [6] Src [to_dict]: to_dict
      PURITY: 100% pure
  [7] Src [to_dict]: to_dict
      PURITY: 100% pure
  [8] Src [is_client_available]: is_client_available → get_client_spec → normalize_client_id
      PURITY: 100% pure
  [9] Src [shell_client_ids]: shell_client_ids → iter_client_specs
      PURITY: 100% pure
  [10] Src [shell_process_patterns]: shell_process_patterns → iter_client_specs
      PURITY: 100% pure
  [11] Src [tool_registry_entries]: tool_registry_entries → iter_client_specs
      PURITY: 100% pure
  [12] Src [autopilot_backend_for_client]: autopilot_backend_for_client → is_shell_llm_client → get_client_spec → normalize_client_id
      PURITY: 100% pure
  [13] Src [detect_koru_agent_rows]: detect_koru_agent_rows → detect_clients → normalize_client_id
      PURITY: 100% pure
  [14] Src [drive_koru_chat]: drive_koru_chat → drive_shell_llm → build_drive_plan → _resolve_spec → ...(2 more)
      PURITY: 100% pure
  [15] Src [launch_koru_agent]: launch_koru_agent → normalize_client_id
      PURITY: 100% pure

LAYERS:
  src/                            CC̄=3.4    ←in:0  →out:0
  │ controller                 248L  6C   11m  CC=10     ←2
  │ compat                     205L  0C   11m  CC=8      ←0
  │ registry                   168L  1C    6m  CC=4      ←5
  │ cli                        167L  0C    7m  CC=6      ←0
  │ validation                 127L  1C    6m  CC=9      ←1
  │ !! nlp                        104L  1C    5m  CC=15     ←1
  │ __init__                    36L  0C    0m  CC=0.0    ←0
  │ __main__                     7L  0C    0m  CC=0.0    ←0
  │
  ./                              CC̄=0.0    ←in:0  →out:0
  │ !! goal.yaml                  511L  0C    0m  CC=0.0    ←0
  │ pyproject.toml              76L  0C    0m  CC=0.0    ←0
  │ tree.txt                    57L  0C    0m  CC=0.0    ←0
  │ project.sh                  50L  0C    0m  CC=0.0    ←0
  │
  testql-scenarios/               CC̄=0.0    ←in:0  →out:0
  │ generated-cli-tests.testql.toon.yaml    20L  0C    0m  CC=0.0    ←0
  │

COUPLING: no cross-package imports detected

EXTERNAL:
  validation: run `vallm batch .` → validation.toon
  duplication: run `redup scan .` → duplication.toon
```

### Duplication (`project/duplication.toon.yaml`)

```toon markpact:analysis path=project/duplication.toon.yaml
# redup/duplication | 0 groups | 8f 1062L | 2026-06-08

SUMMARY:
  files_scanned: 8
  total_lines:   1062
  dup_groups:    0
  dup_fragments: 0
  saved_lines:   0
  scan_ms:       2128
```

### Evolution / Churn (`project/evolution.toon.yaml`)

```toon markpact:analysis path=project/evolution.toon.yaml
# code2llm/evolution | 46 func | 6f | 2026-06-08
# generated in 0.00s

NEXT[2] (ranked by impact):
  [1] !  SPLIT-FUNC      _intent_from_nlp2dsl  CC=15  fan=14
      WHY: CC=15 exceeds 15
      EFFORT: ~1h  IMPACT: 210

  [2] !! SPLIT           goal.yaml
      WHY: 511L, 0 classes, max CC=0
      EFFORT: ~4h  IMPACT: 0


RISKS[1]:
  ⚠ Splitting goal.yaml may break 0 import paths

METRICS-TARGET:
  CC̄:          3.4 → ≤2.4
  max-CC:      15 → ≤7
  god-modules: 1 → 0
  high-CC(≥15): 1 → ≤0
  hub-types:   0 → ≤0

PATTERNS (language parser shared logic):
  _extract_declarations() in base.py — unified extraction for:
    - TypeScript: interfaces, types, classes, functions, arrow funcs
    - PHP: namespaces, traits, classes, functions, includes
    - Ruby: modules, classes, methods, requires
    - C++: classes, structs, functions, #includes
    - C#: classes, interfaces, methods, usings
    - Java: classes, interfaces, methods, imports
    - Go: packages, functions, structs
    - Rust: modules, functions, traits, use statements

  Shared regex patterns per language:
    - import: language-specific import/require/using patterns
    - class: class/struct/trait declarations with inheritance
    - function: function/method signatures with visibility
    - brace_tracking: for C-family languages ({ })
    - end_keyword_tracking: for Ruby (module/class/def...end)

  Benefits:
    - Consistent extraction logic across all languages
    - Reduced code duplication (~70% reduction in parser LOC)
    - Easier maintenance: fix once, apply everywhere
    - Standardized FunctionInfo/ClassInfo models

HISTORY:
  prev CC̄=3.3 → now CC̄=3.4
```

## Intent

Shell LLM client control plane for semcod/coru automation.
