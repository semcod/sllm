from __future__ import annotations

from pathlib import Path

from sllm.compat import (
    SHELL_AUTOPILOT_BACKEND,
    SHELL_BACKEND_PROFILE_ID,
    agent_backend_aliases,
    agent_backend_profiles,
    autopilot_backend_for_client,
    detect_koru_agent_rows,
    is_client_available,
    shell_client_ids,
    shell_process_patterns,
    tool_registry_entries,
)
from sllm.controller import ShellDriveRequest, build_drive_plan
from sllm.nlp import ShellIntent, intent_from_text
from sllm.registry import detect_clients, get_client_spec, normalize_client_id
from sllm.validation import (
    ecosystem_status,
    intent_contracts,
    validate_intent,
    validate_intent_contracts,
)


def test_registry_normalizes_common_aliases() -> None:
    assert normalize_client_id("claude") == "claude-code"
    assert normalize_client_id("codex-cli") == "codex"
    assert get_client_spec("aider") is not None


def test_detect_clients_marks_available_from_injected_which() -> None:
    rows = detect_clients(which=lambda name: f"/bin/{name}" if name == "aider" else None)
    aider = next(row for row in rows if row["id"] == "aider")
    claude = next(row for row in rows if row["id"] == "claude-code")
    assert aider["available"] is True
    assert claude["available"] is False


def test_compat_exports_koru_agent_rows(monkeypatch) -> None:
    def fake_which(name: str) -> str | None:
        return "/usr/bin/claude" if name == "claude" else None

    monkeypatch.setattr("shutil.which", fake_which)
    rows = detect_koru_agent_rows()
    claude = next(row for row in rows if row["id"] == "claude-code")
    assert "claude-code" in shell_client_ids()
    assert autopilot_backend_for_client("claude") == SHELL_AUTOPILOT_BACKEND
    assert claude["available"] is True
    assert claude["launchable"] is True
    assert claude["command"] == "/usr/bin/claude"
    assert is_client_available("claude") is True
    assert is_client_available("aider") is False
    assert ("codex", "Codex CLI", ("codex",)) in shell_process_patterns()
    registry = {str(row["id"]): row for row in tool_registry_entries()}
    assert registry["aider"]["category"] == "cli_agent"
    assert registry["aider"]["invoke"] == (
        "koru sllm drive --client aider --prompt '<prompt>' --execute"
    )
    assert registry["codex-cli"]["invoke"] == (
        "koru sllm drive --client codex --prompt '<prompt>' --execute"
    )
    assert agent_backend_aliases()["sllm_shell"] == SHELL_BACKEND_PROFILE_ID
    assert agent_backend_profiles()[0]["id"] == SHELL_BACKEND_PROFILE_ID


def test_build_drive_plan_uses_message_file_for_aider(monkeypatch, tmp_path: Path) -> None:
    def fake_which(name: str) -> str | None:
        return f"/usr/bin/{name}" if name == "aider" else None

    monkeypatch.setattr("shutil.which", fake_which)
    plan = build_drive_plan(
        ShellDriveRequest(
            client_id="aider",
            prompt="Fix PLF-1",
            project=tmp_path,
        )
    )
    assert plan.argv[:2] == ("/usr/bin/aider", "--message-file")
    assert plan.prompt_path.exists()
    assert plan.stdin_text is None


def test_nlp_rules_select_client_and_prompt() -> None:
    intent = intent_from_text("aider: napraw testy", default_client="claude")
    assert intent.client_id == "aider"
    assert intent.prompt == "napraw testy"
    assert validate_intent(intent).ok is True


def test_validate_intent_rejects_raw_dsl_without_sllm_drive() -> None:
    intent = ShellIntent(
        client_id="aider",
        prompt="Fix tests",
        raw_dsl={"steps": [{"action": "send_email", "config": {}}]},
    )
    result = validate_intent(intent)
    assert result.ok is False
    assert "raw_dsl has no sllm drive action" in result.errors


def test_intent_contracts_are_exposed_for_ecosystem_validation() -> None:
    assert intent_contracts()
    contracts = validate_intent_contracts()
    assert contracts["ok"] is True
    status = ecosystem_status()
    assert "sllm.drive" in status["expected_actions"]
    assert "intent_contracts" in status
