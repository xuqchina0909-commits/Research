"""Apply local DeepEye compatibility patches for OpenAI-compatible providers.

This script intentionally does not write API keys. It only applies the code
changes and non-secret env defaults needed by the benchmark adapter.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEEPEYE = ROOT / "repos" / "DeepEye"
AGENT_TASKS = DEEPEYE / "packages" / "backend" / "app" / "tasks" / "agent_tasks.py"
ENV_FILE = DEEPEYE / ".env"


def replace_once(text: str, old: str, new: str) -> str:
    if new in text:
        return text
    if old not in text:
        raise RuntimeError(f"Patch anchor not found:\n{old}")
    return text.replace(old, new, 1)


def set_env_default(path: Path, key: str, value: str) -> None:
    if path.exists():
        lines = path.read_text(encoding="utf-8").splitlines()
    else:
        lines = []

    updated = False
    next_lines = []
    for line in lines:
        if line.startswith(f"{key}="):
            next_lines.append(f"{key}={value}")
            updated = True
        else:
            next_lines.append(line)
    if not updated:
        next_lines.append(f"{key}={value}")

    path.write_text("\n".join(next_lines) + "\n", encoding="utf-8")


def patch_agent_tasks() -> None:
    text = AGENT_TASKS.read_text(encoding="utf-8")
    text = replace_once(text, "import asyncio\nimport traceback\n", "import asyncio\nimport os\nimport traceback\n")
    text = replace_once(
        text,
        """def _create_model() -> ChatOpenAI:
    return ChatOpenAI(
        api_key=settings.LLM_API_KEY,
        base_url=settings.LLM_BASE_URL,
        model=settings.LLM_MODEL,
        temperature=settings.LLM_TEMPERATURE,
        streaming=True,
    )


async def _run_agent_async(agent_input: AgentInput) -> None:
""",
        """def _create_model() -> ChatOpenAI:
    streaming = os.getenv("DEEPEYE_LLM_STREAMING", "true").strip().lower() not in {"0", "false", "no"}
    return ChatOpenAI(
        api_key=settings.LLM_API_KEY,
        base_url=settings.LLM_BASE_URL,
        model=settings.LLM_MODEL,
        temperature=settings.LLM_TEMPERATURE,
        streaming=streaming,
    )


def _extract_last_message_content(result) -> str | None:
    if not isinstance(result, dict):
        return None
    messages = result.get("messages")
    if not isinstance(messages, list):
        return None
    for message in reversed(messages):
        content = getattr(message, "content", None)
        if isinstance(content, str) and content.strip():
            return content.strip()
    return None


async def _run_agent_async(agent_input: AgentInput) -> None:
""",
    )
    text = replace_once(
        text,
        """            await supervisor.ainvoke(
                user_input,
                thread_id=session_id,
                config={
                    "callbacks": [cb_supervisor],
                    "configurable": {
                        "datasources_context": datasources_context
                    }
                },
            )
            logger.info("[AgentTask] Agent execution finished successfully")
""",
        """            supervisor_result = await supervisor.ainvoke(
                user_input,
                thread_id=session_id,
                config={
                    "callbacks": [cb_supervisor],
                    "configurable": {
                        "datasources_context": datasources_context
                    }
                },
            )
            final_content = _extract_last_message_content(supervisor_result)
            if final_content and not collector.has_activity():
                collector.add_token("supervisor", final_content)
            logger.info("[AgentTask] Agent execution finished successfully")
""",
    )
    AGENT_TASKS.write_text(text, encoding="utf-8")


def main() -> None:
    patch_agent_tasks()
    set_env_default(ENV_FILE, "DEEPEYE_LLM_STREAMING", "false")
    set_env_default(ENV_FILE, "DOCKER_CONTROL_TIMEOUT_SECONDS", "600")
    print("DeepEye external-model compatibility patch applied.")


if __name__ == "__main__":
    main()
