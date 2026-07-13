"""Apply local DeepEye compatibility patches for OpenAI-compatible providers.

This script intentionally does not write API keys. It only applies the code
changes and non-secret env defaults needed by the benchmark adapter.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEEPEYE = ROOT / "repos" / "DeepEye"
AGENT_TASKS = DEEPEYE / "packages" / "backend" / "app" / "tasks" / "agent_tasks.py"
CONFIG = DEEPEYE / "packages" / "backend" / "app" / "core" / "config.py"
SQL_EXECUTE = DEEPEYE / "packages" / "backend" / "app" / "node" / "data" / "sql_execute.py"
REPAIR_STATE = DEEPEYE / "packages" / "backend" / "app" / "workflow" / "repair" / "state.py"
WORKFLOW_PROMPTS = DEEPEYE / "packages" / "backend" / "app" / "workflow" / "prompts.py"
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
        timeout=settings.LLM_REQUEST_TIMEOUT_SECONDS,
        max_retries=settings.LLM_MAX_RETRIES,
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
        """        model=settings.LLM_MODEL,
        temperature=settings.LLM_TEMPERATURE,
        streaming=streaming,
    )
""",
        """        model=settings.LLM_MODEL,
        temperature=settings.LLM_TEMPERATURE,
        timeout=settings.LLM_REQUEST_TIMEOUT_SECONDS,
        max_retries=settings.LLM_MAX_RETRIES,
        streaming=streaming,
    )
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


def patch_config() -> None:
    text = CONFIG.read_text(encoding="utf-8")
    text = replace_once(
        text,
        """    LLM_TEMPERATURE: float = 0.7
    LLM_MAX_TOKENS: int = 8192  # max tokens for completion across agent and artifact generation
    STARTUP_WARMUP_ENABLED: bool = True
""",
        """    LLM_TEMPERATURE: float = 0.7
    LLM_MAX_TOKENS: int = 8192  # max tokens for completion across agent and artifact generation
    LLM_REQUEST_TIMEOUT_SECONDS: float = 120.0
    LLM_MAX_RETRIES: int = 1
    STARTUP_WARMUP_ENABLED: bool = True
""",
    )
    CONFIG.write_text(text, encoding="utf-8")


def patch_sql_execute() -> None:
    text = SQL_EXECUTE.read_text(encoding="utf-8")
    text = replace_once(
        text,
        """from __future__ import annotations

from typing import Any

from sqlalchemy.orm import Session
""",
        """from __future__ import annotations

import re
from typing import Any

from sqlalchemy import inspect
from sqlalchemy.orm import Session
""",
    )
    text = replace_once(
        text,
        """from deepeye.workflows.models import Node, Port
from deepeye.workflows.registry import NodeSpec


class SqlExecuteHandler:
""",
        """from deepeye.workflows.models import Node, Port
from deepeye.workflows.registry import NodeSpec


def _quote_sqlite_identifier(identifier: str) -> str:
    return '"' + identifier.replace('"', '""') + '"'


def _is_plain_sql_identifier(identifier: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", identifier))


def _auto_quote_sqlite_table_names(query: str, table_names: list[str]) -> str:
    fixed_query = query
    for table_name in sorted(table_names, key=len, reverse=True):
        if _is_plain_sql_identifier(table_name):
            continue
        quoted = _quote_sqlite_identifier(table_name)
        pattern = re.compile(
            rf'(?<!["`\\[\\w]){re.escape(table_name)}(?!["`\\]\\w])'
        )
        fixed_query = pattern.sub(quoted, fixed_query)
    return fixed_query


def _prepare_sql_query(engine, datasource_type: str | None, query: str) -> str:
    if (datasource_type or "").lower() != "sqlite":
        return query
    try:
        table_names = inspect(engine).get_table_names()
    except Exception:
        return query
    return _auto_quote_sqlite_table_names(query, table_names)


class SqlExecuteHandler:
""",
    )
    text = replace_once(
        text,
        """        engine = create_engine(connection_string)
        if self.sandbox:
""",
        """        engine = create_engine(connection_string)
        prepared_query = _prepare_sql_query(engine, datasource_type, str(query))
        if self.sandbox:
""",
    )
    text = replace_once(text, "                query=str(query),\n", "                query=prepared_query,\n")
    text = replace_once(text, "        rows = fetch_rows(engine, str(query), limit)\n", "        rows = fetch_rows(engine, prepared_query, limit)\n")
    SQL_EXECUTE.write_text(text, encoding="utf-8")


def patch_workflow_prompts() -> None:
    text = WORKFLOW_PROMPTS.read_text(encoding="utf-8")
    text = replace_once(
        text,
        """- `sql.execute` can only reference tables and columns that exist in the attached database schema. Never reference file-only columns, CSV headers, or file-derived metadata inside SQL.
- For `sql.execute`, always use explicit `AS` aliases for derived, aggregated, renamed, or ambiguous columns so downstream nodes receive stable column names.
""",
        """- `sql.execute` can only reference tables and columns that exist in the attached database schema. Never reference file-only columns, CSV headers, or file-derived metadata inside SQL.
- Quote database identifiers exactly when table or column names contain spaces, punctuation, symbols, or non-ASCII characters. For SQLite, use double quotes, for example `FROM "annual_rate_&_churn"`.
- For `sql.execute`, always use explicit `AS` aliases for derived, aggregated, renamed, or ambiguous columns so downstream nodes receive stable column names.
""",
    )
    text = replace_once(
        text,
        """- For `python.code`, do not hardcode `pd.read_csv` / `pd.read_json` based on guesses. Use the preloaded helpers `load_dataset_ref(ref)` or `load_dataset_refs(data)` so file formats are handled correctly.
- For `python.code`, never treat `data['dataset_ref']` as a single dict. It is always a list of dataset refs, even when only one upstream dataset is connected.
- Do not use legacy keys like `preview` or `preview_path` inside `python.code`. The current dataset_ref contract uses `preview_rows` for metadata preview and `path` for the sandbox file path.
""",
        """- For `python.code`, do not hardcode `pd.read_csv` / `pd.read_json` based on guesses. Use the preloaded helpers `load_dataset_ref(ref)` or `load_dataset_refs(data)` so file formats are handled correctly.
- For `python.code`, never treat `data['dataset_ref']` as a single dict. It is always a list of dataset refs, even when only one upstream dataset is connected.
- Do not use legacy keys like `preview` or `preview_path` inside `python.code`. The current dataset_ref contract uses `preview_rows` for metadata preview and `path` for the sandbox file path.
- If a calculation depends on multiple filtered/selected datasets, combine them in `python.code` and emit one compact result dataset before `llm.answer`. Do not connect multiple dataset_ref edges directly into a non-multiple input.
- Prefer doing column-sensitive CSV calculations in one `python.code` node directly after `datasource.read`; intermediate `rows.select` nodes may preserve generic columns such as `Unnamed: 2`, so downstream code must use the immediate upstream schema exactly.
- For benchmark-style exact-answer tasks, the last transform before `llm.answer` should emit a one-row or short-list dataset containing the final answer and minimal evidence, not a broad raw table.
""",
    )
    WORKFLOW_PROMPTS.write_text(text, encoding="utf-8")


def patch_repair_state() -> None:
    text = REPAIR_STATE.read_text(encoding="utf-8")
    text = replace_once(
        text,
        """                "keyerror",
                "column not found",
                "no such column",
            )
""",
        """                "keyerror",
                "column not found",
                "no such column",
                "you are trying to merge on",
                "merge on",
                "columns for key",
                "invalid literal for int",
                "invalid literal for float",
                "cannot convert float nan to integer",
                "cannot convert non-finite values",
                "object has no attribute 'replace'",
                'object has no attribute "replace"',
            )
""",
    )
    text = replace_once(
        text,
        """            "Inside `python.code`, inspect `data.get('dataset_ref', [])` metadata first and align every join, groupby, and calculation to the emitted schema.",
        ]
""",
        """            "Inside `python.code`, inspect `data.get('dataset_ref', [])` metadata first and align every join, groupby, and calculation to the emitted schema.",
            "Use `load_dataset_ref(ref)` or `load_dataset_refs(data)` for computation over complete upstream datasets; do not compute from `dataset_ref.preview_rows` except for quick schema inspection.",
            "When converting strings to numbers, remove embedded header rows and blank/null rows first; use `pd.to_numeric(..., errors='coerce')` and filter nulls instead of direct `astype(int)` on raw columns.",
            "For pandas merges, verify that join keys represent the same entity and have compatible dtypes; if a lookup table is a curve or matrix rather than an entity table, compute a mapping instead of merging on row index.",
        ]
""",
    )
    REPAIR_STATE.write_text(text, encoding="utf-8")


def main() -> None:
    patch_config()
    patch_agent_tasks()
    patch_sql_execute()
    patch_workflow_prompts()
    patch_repair_state()
    set_env_default(ENV_FILE, "DEEPEYE_LLM_STREAMING", "false")
    set_env_default(ENV_FILE, "LLM_REQUEST_TIMEOUT_SECONDS", "120")
    set_env_default(ENV_FILE, "LLM_MAX_RETRIES", "1")
    set_env_default(ENV_FILE, "DOCKER_CONTROL_TIMEOUT_SECONDS", "600")
    print("DeepEye external-model compatibility patch applied.")


if __name__ == "__main__":
    main()
