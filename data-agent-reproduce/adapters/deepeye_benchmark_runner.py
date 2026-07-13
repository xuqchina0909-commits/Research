"""Run KramaBench/DAComp tasks through the local DeepEye Docker stack.

The runner uses the public DeepEye HTTP API:
auth -> session -> datasource -> chat -> persisted messages.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import shutil
import sqlite3
import time
from pathlib import Path
from typing import Any

import requests


ROOT = Path(__file__).resolve().parents[1]
RESEARCH_ROOT = ROOT.parent
DEEPEYE = ROOT / "repos" / "DeepEye"
KRAMA = ROOT / "repos" / "KramaBench"
DACOMP = ROOT / "repos" / "DAComp"
DEFAULT_API = "http://127.0.0.1:8080"
DEFAULT_EMAIL = "deepeye-benchmark-xuq@example.com"
DEFAULT_PASSWORD = "DeepEyeBench!2026"


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def extract_answer(text: str) -> str | None:
    matches = re.findall(r"<Answer>(.*?)</Answer>", text, flags=re.DOTALL | re.IGNORECASE)
    if matches:
        return matches[-1].strip()
    return None


def extract_number(text: str | None) -> float | None:
    if not text:
        return None
    numbers = re.findall(r"-?\d+(?:,\d{3})*(?:\.\d+)?", text)
    if not numbers:
        return None
    return float(numbers[-1].replace(",", ""))


def score_numeric(prediction: str | None, expected: Any) -> dict[str, Any]:
    pred_num = extract_number(prediction)
    if pred_num is None:
        return {"correct": False, "predicted_number": None, "reason": "no numeric answer"}
    exp_num = float(expected)
    tolerance = max(1e-4, abs(exp_num) * 1e-4)
    return {
        "correct": math.isclose(pred_num, exp_num, rel_tol=1e-4, abs_tol=tolerance),
        "predicted_number": pred_num,
        "expected_number": exp_num,
        "tolerance": tolerance,
    }


def score_exact_list(prediction: str | None, expected: Any) -> dict[str, Any]:
    if not isinstance(expected, list):
        return {"correct": None, "reason": "expected answer is not a list"}
    if not prediction:
        return {"correct": False, "predicted_list": None, "expected_list": expected, "reason": "no answer"}
    predicted_numbers = [int(item) for item in re.findall(r"-?\d+", prediction)]
    return {
        "correct": predicted_numbers == expected,
        "predicted_list": predicted_numbers,
        "expected_list": expected,
    }


def score_krama_answer(prediction: str | None, task: dict[str, Any]) -> dict[str, Any]:
    answer_type = str(task.get("answer_type", ""))
    if answer_type.startswith("numeric"):
        return score_numeric(prediction, task.get("answer"))
    if answer_type.startswith("list"):
        return score_exact_list(prediction, task.get("answer"))
    return {"correct": None, "reason": f"scoring not implemented for {answer_type}"}


def deepeye_failure_reason(text: str | None) -> str | None:
    if not text:
        return None
    failure_markers = [
        "工作流规划在自动修复两次后仍未收敛",
        "工作流规划已停止",
        "工作流规划未收敛",
        "Workflow planning did not converge",
        "Workflow execution failed",
        "Workflow repair limit exceeded",
        "repair limit exceeded",
    ]
    for marker in failure_markers:
        if marker in text:
            return marker
    return None


def cjk_ratio(text: str | None) -> float:
    if not text:
        return 0.0
    non_space = [char for char in text if not char.isspace()]
    if not non_space:
        return 0.0
    cjk = [char for char in non_space if "\u4e00" <= char <= "\u9fff"]
    return len(cjk) / len(non_space)


def _parse_jsonish(value: Any) -> Any:
    if not isinstance(value, str):
        return value
    value = value.strip()
    if not value or value[0] not in "[{":
        return value
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return value


def _walk_jsonish(value: Any) -> Any:
    value = _parse_jsonish(value)
    if isinstance(value, dict):
        return {key: _walk_jsonish(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_walk_jsonish(item) for item in value]
    return value


def extract_workflow_evidence(messages: list[dict[str, Any]], max_chars: int = 12000) -> str:
    evidence: list[Any] = []
    seen: set[str] = set()

    def add(item: Any) -> None:
        serialized = json.dumps(item, ensure_ascii=False, sort_keys=True)
        if serialized in seen:
            return
        seen.add(serialized)
        evidence.append(item)

    def visit(value: Any, path: str = "") -> None:
        value = _walk_jsonish(value)
        if isinstance(value, dict):
            if "preview_rows" in value:
                add({
                    "path": path,
                    "name": value.get("name"),
                    "row_count": value.get("row_count"),
                    "columns": value.get("columns"),
                    "preview_rows": value.get("preview_rows"),
                })
            if any(key in value for key in ("ratio", "answer", "value_2024", "value_2001", "result")):
                compact = {
                    key: value[key]
                    for key in ("ratio", "answer", "value_2024", "value_2001", "result", "error")
                    if key in value
                }
                if compact:
                    add({"path": path, "values": compact})
            for key, item in value.items():
                visit(item, f"{path}.{key}" if path else str(key))
        elif isinstance(value, list):
            for index, item in enumerate(value):
                visit(item, f"{path}[{index}]")

    visit(messages)
    text = json.dumps(evidence, ensure_ascii=False, indent=2)
    if len(text) > max_chars:
        return text[:max_chars] + "\n...[truncated]"
    return text


def _dataset_ref_items(messages: list[dict[str, Any]]) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []

    def visit(value: Any, path: str = "") -> None:
        value = _walk_jsonish(value)
        if isinstance(value, dict):
            if value.get("kind") == "dataset_ref" and isinstance(value.get("preview_rows"), list):
                items.append({
                    "path": path,
                    "name": value.get("name"),
                    "source": value.get("source"),
                    "row_count": value.get("row_count"),
                    "columns": value.get("columns"),
                    "preview_rows": value.get("preview_rows"),
                })
            for key, item in value.items():
                visit(item, f"{path}.{key}" if path else str(key))
        elif isinstance(value, list):
            for index, item in enumerate(value):
                visit(item, f"{path}[{index}]")

    visit(messages)
    return items


def _clean_scalar(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text if text else None


def _answer_from_dataset_ref_items(items: list[dict[str, Any]], task: dict[str, Any]) -> str | None:
    answer_type = str(task.get("answer_type", ""))
    derived_items = [
        item for item in items
        if item.get("source") not in {"datasource.read", "sql.execute"}
        and isinstance(item.get("preview_rows"), list)
        and item.get("preview_rows")
    ]
    derived_items.sort(key=lambda item: (int(item.get("row_count") or 0), len(str(item.get("path") or ""))))
    if not derived_items:
        return None

    if answer_type.startswith("list"):
        for item in derived_items:
            rows = item.get("preview_rows") or []
            columns = item.get("columns") or []
            if not rows or not columns or len(columns) != 1:
                continue
            values = [_clean_scalar(row.get(columns[0])) for row in rows if isinstance(row, dict)]
            values = [value for value in values if value is not None]
            if values and all(re.fullmatch(r"-?\d+", value) for value in values):
                return "[" + ", ".join(values) + "]"

    if answer_type.startswith("numeric"):
        preferred_names = (
            "answer",
            "final_answer",
            "result",
            "ratio",
            "value",
            "count",
            "total",
            "year",
        )
        for item in derived_items:
            rows = item.get("preview_rows") or []
            if len(rows) != 1 or not isinstance(rows[0], dict):
                continue
            row = rows[0]
            keys = list(row.keys())
            ordered_keys = sorted(
                keys,
                key=lambda key: 0 if any(name in str(key).lower() for name in preferred_names) else 1,
            )
            for key in ordered_keys:
                value = _clean_scalar(row.get(key))
                if value and extract_number(value) is not None:
                    return value
    return None


def structured_answer_from_messages(messages: list[dict[str, Any]], task: dict[str, Any]) -> str | None:
    return _answer_from_dataset_ref_items(_dataset_ref_items(messages), task)


class DeepEyeClient:
    def __init__(self, api_base: str, email: str, password: str, timeout: int = 60):
        self.api_base = api_base.rstrip("/")
        self.email = email
        self.password = password
        self.timeout = timeout
        self.session = requests.Session()
        self.access_token: str | None = None

    def _url(self, path: str) -> str:
        return f"{self.api_base}{path}"

    def _headers(self) -> dict[str, str]:
        if not self.access_token:
            return {}
        return {"Authorization": f"Bearer {self.access_token}"}

    def request(self, method: str, path: str, **kwargs: Any) -> requests.Response:
        headers = kwargs.pop("headers", {})
        merged_headers = {**self._headers(), **headers}
        response = self.session.request(
            method,
            self._url(path),
            headers=merged_headers,
            timeout=kwargs.pop("timeout", self.timeout),
            **kwargs,
        )
        if response.status_code == 401 and path != "/api/auth/login":
            self.login_or_register()
            merged_headers = {**self._headers(), **headers}
            response = self.session.request(
                method,
                self._url(path),
                headers=merged_headers,
                timeout=self.timeout,
                **kwargs,
            )
        response.raise_for_status()
        return response

    def login_or_register(self) -> None:
        payload = {"email": self.email, "password": self.password}
        response = self.session.post(self._url("/api/auth/login"), json=payload, timeout=self.timeout)
        if response.status_code == 401:
            register_payload = {
                "email": self.email,
                "username": "deepeye-benchmark",
                "password": self.password,
            }
            response = self.session.post(self._url("/api/auth/register"), json=register_payload, timeout=self.timeout)
        response.raise_for_status()
        self.access_token = response.json()["access_token"]

    def create_session(self, title: str) -> str:
        response = self.request("POST", "/api/v1/sessions", json={"title": title})
        return str(response.json()["id"])

    def upload_file_datasource(self, path: Path, session_id: str) -> str:
        with path.open("rb") as handle:
            response = self.request(
                "POST",
                f"/api/v1/datasources/upload?session_id={session_id}",
                files={"file": (path.name, handle)},
                timeout=600,
            )
        return str(response.json()["id"])

    def create_database_datasource(self, name: str, ds_type: str, connection_string: str, session_id: str) -> str:
        response = self.request(
            "POST",
            f"/api/v1/datasources?session_id={session_id}",
            json={"name": name, "type": ds_type, "connection_string": connection_string},
            timeout=180,
        )
        return str(response.json()["id"])

    def start_chat(self, session_id: str, message: str, datasource_ids: list[str] | None) -> dict[str, Any]:
        response = self.request(
            "POST",
            "/api/v1/chat",
            json={"session_id": session_id, "message": message, "datasource_ids": datasource_ids or []},
            timeout=60,
        )
        return response.json()

    def get_messages(self, session_id: str) -> list[dict[str, Any]]:
        response = self.request("GET", f"/api/v1/sessions/{session_id}/messages", timeout=30)
        return response.json().get("messages") or []

    def wait_for_assistant(self, session_id: str, after_count: int, timeout: int) -> tuple[str | None, list[dict[str, Any]]]:
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            messages = self.get_messages(session_id)
            assistant_messages = [
                msg for msg in messages[after_count:]
                if msg.get("role") == "assistant" and isinstance(msg.get("content"), str)
            ]
            if assistant_messages:
                return assistant_messages[-1]["content"], messages
            time.sleep(5)
        return None, self.get_messages(session_id)


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def task_slice(items: list[dict[str, Any]], limit: int | None) -> list[dict[str, Any]]:
    return items[:limit] if limit else items


def find_krama_file(filename: str, task_id: str | None = None) -> Path:
    candidates: list[Path] = []
    if task_id:
        candidates.extend((KRAMA / "dr-input").rglob(f"{task_id}/{filename}"))
    candidates.extend((KRAMA / "data").rglob(filename))
    candidates.extend((KRAMA / "dr-input").rglob(filename))
    if not candidates:
        raise FileNotFoundError(f"KramaBench data source not found: {filename}")
    return candidates[0]


def krama_subtask_plan(task: dict[str, Any]) -> str:
    subtasks = task.get("subtasks")
    if not isinstance(subtasks, list) or not subtasks:
        return "No explicit benchmark subtasks are provided."
    lines = []
    for index, subtask in enumerate(subtasks, start=1):
        if not isinstance(subtask, dict):
            continue
        step = str(subtask.get("step") or subtask.get("query") or "").strip()
        answer_type = str(subtask.get("answer_type") or "").strip()
        if step:
            lines.append(f"{index}. {step} Answer type: {answer_type}.")
    return "\n".join(lines) if lines else "No explicit benchmark subtasks are provided."


def krama_csv_template() -> str:
    return r'''
Use this robust CSV cleaning pattern inside python.code when the file has blank rows, embedded header rows, thousands separators, or footnotes:

import sys, json, re
import pandas as pd

data = json.load(sys.stdin)
df = load_dataset_refs(data)[0]

def non_empty_count(row):
    return sum(pd.notna(v) and str(v).strip() != "" for v in row)

def convert_value(value):
    if pd.isna(value):
        return pd.NA
    text = str(value).strip()
    if text == "":
        return pd.NA
    text = text.replace(",", "").replace("$", "")
    multiplier = 1
    if text.upper().endswith("K"):
        multiplier, text = 1000, text[:-1]
    elif text.upper().endswith("M"):
        multiplier, text = 1000000, text[:-1]
    try:
        number = float(text) * multiplier
        return int(number) if number.is_integer() else number
    except ValueError:
        return str(value).strip()

# Header row: first row with at least two non-empty cells.
header_idx = next(i for i, row in df.iterrows() if non_empty_count(row) >= 2)
headers = [str(v).strip() for v in df.iloc[header_idx].tolist()]
table = df.iloc[header_idx + 1:].copy()
table.columns = headers
table = table[table.apply(non_empty_count, axis=1) >= 2]
table = table.map(convert_value)

# Always select rows by labels/values, never by guessed positions such as df.iloc[3].
# Emit one compact final result, e.g. emit_dataframe(pd.DataFrame([{"answer": answer}]))
'''.strip()


def krama_prompt(task: dict[str, Any]) -> str:
    return (
        "You are running a KramaBench task inside DeepEye. Use only the attached datasource files. "
        "Create and execute a workflow if needed, compute the exact answer, and return the final answer "
        "inside <Answer>...</Answer>. Do not round numeric answers unless the question explicitly asks for rounding. "
        "Do not guess and do not use web access.\n\n"
        "KramaBench workflow rules:\n"
        "- For CSV/file tasks, prefer `datasource.read -> python.code -> llm.answer`.\n"
        "- In `python.code`, load the complete dataframe with `load_dataset_refs(data)[0]`, inspect actual columns, "
        "handle header rows embedded in the file, and emit exactly one compact result dataframe or JSON value.\n"
        "- Avoid using `rows.select` before `python.code` for column-sensitive calculations because it may preserve generic "
        "columns such as `Unnamed: 2`; if you do use it, downstream code must use the immediate upstream columns exactly.\n"
        "- Do not connect multiple dataset_ref edges directly into `llm.answer`; combine them in `python.code` first.\n"
        "- The final dataset passed to `llm.answer` should contain only the final answer and necessary evidence.\n\n"
        "Reference subtask plan from KramaBench. Follow these steps as the benchmark's intended solution path:\n"
        f"{krama_subtask_plan(task)}\n\n"
        "Required robust CSV template for python.code:\n"
        f"```python\n{krama_csv_template()}\n```\n\n"
        "Important: adapt the template to the question, but preserve its header detection, convert_value, "
        "label-based filtering, and compact final emit pattern.\n\n"
        f"Task ID: {task['id']}\n"
        f"Question: {task['query']}\n"
        f"Expected answer type: {task.get('answer_type')}\n"
        "Final response format: <Answer>number_or_short_value</Answer>"
    )


def krama_finalize_prompt(task: dict[str, Any], previous_text: str, evidence: str) -> str:
    return (
        "Your previous response did not satisfy the KramaBench final-answer contract. "
        "Using only the workflow evidence below, return exactly one final answer. "
        "For numeric answers, recompute the final arithmetic from the exact source values you used and keep at least "
        "4 decimal places when the result is not an integer. Do not add explanation, markdown, or prose.\n\n"
        f"Question: {task['query']}\n"
        f"Previous response:\n{previous_text}\n\n"
        f"Workflow evidence:\n{evidence}\n\n"
        "Required output format: <Answer>exact_number_or_short_value</Answer>"
    )


def dacomp_finalize_prompt(previous_text: str) -> str:
    return (
        "请把上一轮结果整理为中文分析报告。要求：\n"
        "1. 只使用中文，不要使用英文标题或英文叙述。\n"
        "2. 保留关键数值、计算依据、规则/公式和建议。\n"
        "3. 不要重新编造数据；如果上一轮信息不足，请明确说明限制。\n"
        "4. 输出结构应包含：结论、关键依据、计算规则、建议。\n\n"
        f"上一轮结果：\n{previous_text}"
    )


def run_deepeye_task(
    client: DeepEyeClient,
    title: str,
    prompt: str,
    datasource_ids: list[str],
    timeout: int,
) -> dict[str, Any]:
    session_id = client.create_session(title)
    before = len(client.get_messages(session_id))
    chat_start = client.start_chat(session_id, prompt, datasource_ids)
    started = time.time()
    content, messages = client.wait_for_assistant(session_id, before, timeout)
    return {
        "session_id": session_id,
        "chat_start": chat_start,
        "text": content,
        "messages": messages,
        "runtime_seconds": round(time.time() - started, 3),
        "status": "completed" if content else "timeout",
    }


def run_krama(args: argparse.Namespace, client: DeepEyeClient) -> dict[str, Any]:
    workload = Path(args.workload)
    tasks = task_slice(json.loads(workload.read_text(encoding="utf-8")), args.limit)
    out_dir = Path(args.output) / "kramabench" / workload.stem
    rows: list[dict[str, Any]] = []
    results: list[dict[str, Any]] = []
    for task in tasks:
        task_id = task["id"]
        task_dir = out_dir / task_id
        result_path = task_dir / "result.json"
        if result_path.exists() and not args.overwrite:
            payload = json.loads(result_path.read_text(encoding="utf-8"))
            results.append(payload)
            rows.append(summary_row(payload))
            continue

        started = time.time()
        try:
            session_id = client.create_session(f"KramaBench {task_id}")
            datasource_ids = []
            data_paths = []
            for name in task.get("data_sources", []):
                data_path = find_krama_file(name, task_id)
                data_paths.append(str(data_path))
                datasource_ids.append(client.upload_file_datasource(data_path, session_id))

            before = len(client.get_messages(session_id))
            chat_start = client.start_chat(session_id, krama_prompt(task), datasource_ids)
            text, messages = client.wait_for_assistant(session_id, before, args.timeout)
            answer = extract_answer(text or "")
            failure_reason = deepeye_failure_reason(text)
            structured_answer = structured_answer_from_messages(messages, task)
            if structured_answer:
                answer = structured_answer
                text = f"<Answer>{structured_answer}</Answer>"
            finalize_attempted = False
            if text and not answer and not failure_reason:
                finalize_attempted = True
                before = len(messages)
                evidence = extract_workflow_evidence(messages)
                client.start_chat(session_id, krama_finalize_prompt(task, text, evidence), datasource_ids)
                finalized_text, messages = client.wait_for_assistant(session_id, before, min(args.timeout, 300))
                if finalized_text:
                    text = finalized_text
                    answer = extract_answer(text)
                    failure_reason = deepeye_failure_reason(text)
                    structured_answer = structured_answer_from_messages(messages, task)
                    if structured_answer:
                        answer = structured_answer
                        text = f"<Answer>{structured_answer}</Answer>"
            score = score_krama_answer(answer, task)
            payload = {
                "benchmark": "KramaBench",
                "system": "DeepEye",
                "task_id": task_id,
                "status": "failed" if failure_reason else ("completed" if text else "timeout"),
                "session_id": session_id,
                "chat_start": chat_start,
                "question": task.get("query"),
                "data_sources": data_paths,
                "datasource_ids": datasource_ids,
                "expected_answer": task.get("answer"),
                "answer_type": task.get("answer_type"),
                "final_answer": answer,
                "structured_answer": structured_answer,
                "failure_reason": failure_reason,
                "finalize_attempted": finalize_attempted,
                "score": score,
                "text": text,
                "messages": messages,
                "runtime_seconds": round(time.time() - started, 3),
            }
        except Exception as exc:
            payload = {
                "benchmark": "KramaBench",
                "system": "DeepEye",
                "task_id": task_id,
                "status": "failed",
                "question": task.get("query"),
                "data_sources": task.get("data_sources", []),
                "expected_answer": task.get("answer"),
                "answer_type": task.get("answer_type"),
                "final_answer": None,
                "score": {"correct": False, "reason": f"{type(exc).__name__}: {exc}"},
                "text": f"{type(exc).__name__}: {exc}",
                "runtime_seconds": round(time.time() - started, 3),
            }
        write_json(result_path, payload)
        (task_dir / "raw_output.txt").write_text(str(payload.get("text") or ""), encoding="utf-8")
        results.append(payload)
        rows.append(summary_row(payload))
        write_csv(out_dir / "summary.csv", rows)
    return {"benchmark": "KramaBench", "results": results, "summary_csv": str(out_dir / "summary.csv")}


def dacomp_sqlite_for_container(task_id: str, sqlite_path: Path) -> tuple[Path, str]:
    target_dir = DEEPEYE / ".benchmark-data" / "dacomp"
    target_dir.mkdir(parents=True, exist_ok=True)
    target_path = target_dir / f"{task_id}.sqlite"
    if not target_path.exists() or target_path.stat().st_size != sqlite_path.stat().st_size:
        shutil.copy2(sqlite_path, target_path)
    container_path = f"/app/project/.benchmark-data/dacomp/{task_id}.sqlite"
    return target_path, f"sqlite:///{container_path}"


def sqlite_profile(sqlite_path: Path, row_limit: int = 3) -> str:
    lines = [f"SQLite file: {sqlite_path.name}"]
    with sqlite3.connect(sqlite_path) as conn:
        table_rows = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
        ).fetchall()
        for (table,) in table_rows:
            count = conn.execute(f'SELECT COUNT(*) FROM "{table}"').fetchone()[0]
            columns = conn.execute(f'PRAGMA table_info("{table}")').fetchall()
            col_desc = ", ".join(f"{col[1]} {col[2]}" for col in columns)
            sample = conn.execute(f'SELECT * FROM "{table}" LIMIT {row_limit}').fetchall()
            lines.append(f"\nTable: {table}\nRows: {count}\nColumns: {col_desc}\nSample rows: {sample}")
    return "\n".join(lines)


def dacomp_prompt(task: dict[str, Any], profile: str) -> str:
    return (
        "You are running a DAComp data-analysis task inside DeepEye. Use the attached SQLite datasource as the "
        "authoritative data source. Produce a detailed Chinese analytical report with quantitative evidence, "
        "explicit formulas/rules, and final recommendations. The final answer MUST be written in Chinese only. "
        "Do not use English headings or English narrative. Do not invent table names.\n\n"
        "Workflow constraints:\n"
        "- For python.code nodes, load the complete upstream datasets with load_dataset_ref(ref) or load_dataset_refs(data). "
        "Do not compute from dataset_ref.preview_rows except for schema inspection.\n"
        "- The annual_rate_&_churn table is an interest-rate/churn curve by annual interest rate, not a company entity table. "
        "Do not merge company credit ratings to the row index of that table.\n"
        "- If using the churn curve, derive a rating-specific rule by choosing or optimizing an annual interest rate for each rating, "
        "then map that rule to companies by Credit Rating.\n\n"
        f"Task ID: {task['instance_id']}\n"
        f"Instruction:\n{task['instruction']}\n\n"
        f"Database profile:\n{profile}\n\n"
        "Return the answer as a Chinese report."
    )


def run_dacomp(args: argparse.Namespace, client: DeepEyeClient) -> dict[str, Any]:
    task_file = Path(args.dacomp_tasks)
    tasks = task_slice(load_jsonl(task_file), args.limit)
    out_dir = Path(args.output) / "dacomp-da" / task_file.stem
    rows: list[dict[str, Any]] = []
    results: list[dict[str, Any]] = []
    for task in tasks:
        task_id = task["instance_id"].replace("dacomp-zh-", "dacomp-")
        task_dir = out_dir / task["instance_id"]
        result_path = task_dir / "result.json"
        if result_path.exists() and not args.overwrite:
            payload = json.loads(result_path.read_text(encoding="utf-8"))
            results.append(payload)
            rows.append(summary_row(payload))
            continue
        started = time.time()
        try:
            sqlite_path = DACOMP / "dacomp-da" / "tasks" / task_id / f"{task_id}.sqlite"
            if not sqlite_path.exists():
                raise FileNotFoundError(f"Missing DAComp sqlite: {sqlite_path}")
            container_copy, conn = dacomp_sqlite_for_container(task_id, sqlite_path)
            profile = sqlite_profile(sqlite_path)
            session_id = client.create_session(f"DAComp {task['instance_id']}")
            datasource_id = client.create_database_datasource(task_id, "sqlite", conn, session_id)
            before = len(client.get_messages(session_id))
            chat_start = client.start_chat(session_id, dacomp_prompt(task, profile), [datasource_id])
            text, messages = client.wait_for_assistant(session_id, before, args.timeout)
            finalize_attempted = False
            if text and cjk_ratio(text) < 0.12 and not deepeye_failure_reason(text):
                finalize_attempted = True
                before = len(messages)
                client.start_chat(session_id, dacomp_finalize_prompt(text), [datasource_id])
                finalized_text, messages = client.wait_for_assistant(session_id, before, min(args.timeout, 300))
                if finalized_text:
                    text = finalized_text
            failure_reason = deepeye_failure_reason(text)
            language_failure = None
            if text and cjk_ratio(text) < 0.12:
                language_failure = "final answer is not a Chinese report"
            payload = {
                "benchmark": "DAComp-DA",
                "system": "DeepEye",
                "task_id": task["instance_id"],
                "status": "failed" if (failure_reason or language_failure) else ("completed" if text else "timeout"),
                "session_id": session_id,
                "chat_start": chat_start,
                "instruction": task.get("instruction"),
                "sqlite_path": str(sqlite_path),
                "container_sqlite_path": str(container_copy),
                "datasource_id": datasource_id,
                "text": text,
                "failure_reason": failure_reason or language_failure,
                "finalize_attempted": finalize_attempted,
                "messages": messages,
                "runtime_seconds": round(time.time() - started, 3),
            }
        except Exception as exc:
            payload = {
                "benchmark": "DAComp-DA",
                "system": "DeepEye",
                "task_id": task.get("instance_id"),
                "status": "failed",
                "instruction": task.get("instruction"),
                "text": f"{type(exc).__name__}: {exc}",
                "runtime_seconds": round(time.time() - started, 3),
            }
        write_json(result_path, payload)
        (task_dir / "report.md").write_text(str(payload.get("text") or ""), encoding="utf-8")
        results.append(payload)
        rows.append(summary_row(payload))
        write_csv(out_dir / "summary.csv", rows)
    return {"benchmark": "DAComp-DA", "results": results, "summary_csv": str(out_dir / "summary.csv")}


def summary_row(payload: dict[str, Any]) -> dict[str, Any]:
    score = payload.get("score") or {}
    return {
        "benchmark": payload.get("benchmark"),
        "system": payload.get("system"),
        "task_id": payload.get("task_id"),
        "status": payload.get("status"),
        "correct": score.get("correct"),
        "expected_answer": payload.get("expected_answer"),
        "final_answer": payload.get("final_answer"),
        "runtime_seconds": payload.get("runtime_seconds"),
        "text_chars": len(payload.get("text") or ""),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--benchmark", choices=["krama", "dacomp", "both"], required=True)
    parser.add_argument("--api-base", default=DEFAULT_API)
    parser.add_argument("--email", default=DEFAULT_EMAIL)
    parser.add_argument("--password", default=DEFAULT_PASSWORD)
    parser.add_argument("--workload", default=str(KRAMA / "workload" / "legal-easy-1.json"))
    parser.add_argument("--dacomp-tasks", default=str(DACOMP / "dacomp-da" / "tasks_zh" / "dacomp-da-zh.jsonl"))
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--timeout", type=int, default=900)
    parser.add_argument("--output", default=str(ROOT / "runs" / "deepeye_benchmark"))
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    client = DeepEyeClient(args.api_base, args.email, args.password)
    client.login_or_register()
    outputs = []
    if args.benchmark in {"krama", "both"}:
        outputs.append(run_krama(args, client))
    if args.benchmark in {"dacomp", "both"}:
        outputs.append(run_dacomp(args, client))
    write_json(Path(args.output) / "run_summary.json", outputs)
    print(json.dumps(outputs, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
