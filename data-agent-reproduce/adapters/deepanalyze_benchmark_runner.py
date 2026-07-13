"""Run small KramaBench/DAComp samples through the local DeepAnalyze API."""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import sqlite3
import time
from pathlib import Path
from typing import Any, Iterable

import requests


ROOT = Path(__file__).resolve().parents[1]
KRAMA = ROOT / "repos" / "KramaBench"
DACOMP = ROOT / "repos" / "DAComp"
DEFAULT_API = "http://127.0.0.1:8200"


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def health(api_base: str) -> bool:
    try:
        res = requests.get(f"{api_base}/health", timeout=5)
        return res.ok
    except requests.RequestException:
        return False


def upload_file(api_base: str, file_path: Path) -> str:
    with file_path.open("rb") as handle:
        res = requests.post(
            f"{api_base}/v1/files",
            files={"file": (file_path.name, handle)},
            data={"purpose": "file-extract"},
            timeout=120,
        )
    res.raise_for_status()
    return res.json()["id"]


def stream_chat(api_base: str, model: str, prompt: str, file_ids: list[str], timeout: int) -> dict[str, Any]:
    started = time.time()
    response = requests.post(
        f"{api_base}/v1/chat/completions",
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt, "file_ids": file_ids}],
            "file_ids": file_ids,
            "temperature": 0.2,
            "stream": True,
        },
        stream=True,
        timeout=timeout,
    )
    response.raise_for_status()

    text_parts: list[str] = []
    final_delta: dict[str, Any] = {}
    for raw_line in response.iter_lines(decode_unicode=True):
        if not raw_line or not raw_line.startswith("data: "):
            continue
        payload = raw_line[6:]
        if payload == "[DONE]":
            break
        try:
            data = json.loads(payload)
        except json.JSONDecodeError:
            continue
        choices = data.get("choices") or []
        if not choices:
            continue
        delta = choices[0].get("delta") or {}
        content = delta.get("content")
        if content:
            text_parts.append(content)
        else:
            final_delta.update(delta)

    full_text = "".join(text_parts)
    return {
        "text": full_text,
        "final_delta": final_delta,
        "runtime_seconds": round(time.time() - started, 3),
    }


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
    correct = math.isclose(pred_num, exp_num, rel_tol=1e-4, abs_tol=tolerance)
    return {
        "correct": correct,
        "predicted_number": pred_num,
        "expected_number": exp_num,
        "tolerance": tolerance,
    }


def load_krama_tasks(workload: Path, limit: int | None) -> list[dict[str, Any]]:
    tasks = json.loads(workload.read_text(encoding="utf-8"))
    return tasks[:limit] if limit else tasks


def find_krama_data_file(filename: str) -> Path:
    candidates = list((KRAMA / "data" / "legal" / "input").rglob(filename))
    if not candidates:
        raise FileNotFoundError(f"KramaBench data source not found: {filename}")
    return candidates[0]


def krama_prompt(task: dict[str, Any]) -> str:
    expected_type = task.get("answer_type", "unknown")
    return (
        "You are evaluating a benchmark task. Use the attached real data files only. "
        "Write and execute Python code to compute the answer. "
        "Return the final benchmark answer inside <Answer>...</Answer>.\n\n"
        f"Task ID: {task['id']}\n"
        f"Question: {task['query']}\n"
        f"Expected answer type: {expected_type}\n"
        "Do not simulate data. Do not use web access."
    )


def run_krama(args: argparse.Namespace) -> dict[str, Any]:
    tasks = load_krama_tasks(Path(args.workload), args.limit)
    out_dir = Path(args.output) / "kramabench"
    rows = []
    task_results = []
    for task in tasks:
        task_id = task["id"]
        task_dir = out_dir / task_id
        task_dir.mkdir(parents=True, exist_ok=True)
        existing_result = task_dir / "result.json"
        if existing_result.exists() and not args.overwrite:
            payload = json.loads(existing_result.read_text(encoding="utf-8"))
            task_results.append(payload)
            rows.append(summary_row_from_payload(payload))
            continue

        started = time.time()
        try:
            data_paths = [find_krama_data_file(name) for name in task.get("data_sources", [])]
            file_ids = [upload_file(args.api_base, path) for path in data_paths]
            result = stream_chat(args.api_base, args.model, krama_prompt(task), file_ids, args.timeout)
            answer = extract_answer(result["text"])
            score = score_numeric(answer, task.get("answer")) if str(task.get("answer_type", "")).startswith("numeric") else {
                "correct": None,
                "reason": "non-numeric scoring not implemented",
            }
            payload = {
                "benchmark": "KramaBench",
                "system": "DeepAnalyze",
                "task_id": task_id,
                "status": "completed",
                "question": task.get("query"),
                "data_sources": [str(path) for path in data_paths],
                "expected_answer": task.get("answer"),
                "answer_type": task.get("answer_type"),
                "final_answer": answer,
                "score": score,
                **result,
            }
        except Exception as exc:  # Keep batch runs going when one model call fails.
            error_text = f"{type(exc).__name__}: {exc}"
            payload = {
                "benchmark": "KramaBench",
                "system": "DeepAnalyze",
                "task_id": task_id,
                "status": "failed",
                "question": task.get("query"),
                "data_sources": task.get("data_sources", []),
                "expected_answer": task.get("answer"),
                "answer_type": task.get("answer_type"),
                "final_answer": None,
                "score": {"correct": False, "reason": error_text},
                "text": error_text,
                "final_delta": {},
                "runtime_seconds": round(time.time() - started, 3),
            }
        write_json(task_dir / "result.json", payload)
        (task_dir / "raw_output.txt").write_text(str(payload.get("text") or ""), encoding="utf-8")
        task_results.append(payload)
        rows.append(summary_row_from_payload(payload))
    write_csv(out_dir / "summary.csv", rows)
    return {"benchmark": "KramaBench", "results": task_results, "summary_csv": str(out_dir / "summary.csv")}


def summary_row_from_payload(payload: dict[str, Any]) -> dict[str, Any]:
    score = payload.get("score") or {}
    return {
        "benchmark": payload.get("benchmark"),
        "system": payload.get("system"),
        "task_id": payload.get("task_id"),
        "status": payload.get("status", "completed"),
        "correct": score.get("correct"),
        "expected_answer": payload.get("expected_answer"),
        "final_answer": payload.get("final_answer"),
        "runtime_seconds": payload.get("runtime_seconds"),
        "notes": score.get("reason", ""),
    }


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def dacomp_sqlite_path(instance_id: str) -> Path:
    if instance_id.startswith("dacomp-zh-"):
        english_id = instance_id.replace("dacomp-zh-", "dacomp-")
        candidates = [
            DACOMP / "dacomp-da" / "tasks_zh" / instance_id / f"{instance_id}.sqlite",
            DACOMP / "dacomp-da" / "tasks" / english_id / f"{english_id}.sqlite",
        ]
    else:
        zh_id = instance_id.replace("dacomp-", "dacomp-zh-", 1)
        candidates = [
            DACOMP / "dacomp-da" / "tasks" / instance_id / f"{instance_id}.sqlite",
            DACOMP / "dacomp-da" / "tasks_zh" / zh_id / f"{zh_id}.sqlite",
        ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise FileNotFoundError("Missing DAComp SQLite. Tried: " + ", ".join(str(path) for path in candidates))


def build_sqlite_summary(sqlite_path: Path, output_path: Path, sample_rows: int = 3) -> Path:
    con = sqlite3.connect(sqlite_path)
    con.row_factory = sqlite3.Row
    lines = [f"# SQLite 数据摘要\n", f"文件: `{sqlite_path.name}`\n"]
    try:
        tables = [
            row[0]
            for row in con.execute("select name from sqlite_master where type='table' order by name").fetchall()
        ]
        for table in tables:
            row_count = con.execute(f'select count(*) from "{table}"').fetchone()[0]
            columns = con.execute(f'pragma table_info("{table}")').fetchall()
            lines.append(f"\n## {table}\n")
            lines.append(f"- Rows: {row_count}\n")
            lines.append("- Columns: " + ", ".join(f"{col[1]} ({col[2]})" for col in columns) + "\n")
            sample = [dict(row) for row in con.execute(f'select * from "{table}" limit ?', (sample_rows,)).fetchall()]
            lines.append("```json\n" + json.dumps(sample, ensure_ascii=False, indent=2) + "\n```\n")
    finally:
        con.close()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path


def dacomp_prompt(task: dict[str, Any]) -> str:
    return (
        "Use the attached SQLite database and schema summary to perform a concise benchmark-style data analysis. "
        "Write and execute Python code against the real SQLite file. "
        "Produce a Chinese analytical answer with concrete metrics and an allocation rule. "
        "Return the final report inside <Answer>...</Answer>.\n\n"
        f"Task ID: {task['instance_id']}\n"
        f"Instruction: {task['instruction']}\n"
        "Do not simulate data. Do not use web access."
    )


def dacomp_summary_row(payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "benchmark": "DAComp-DA",
        "system": "DeepAnalyze",
        "task_id": payload.get("task_id"),
        "status": payload.get("status", "completed"),
        "judge_status": payload.get("judge_status", "not_run"),
        "runtime_seconds": payload.get("runtime_seconds"),
        "final_answer_chars": len(payload.get("final_answer") or ""),
        "notes": payload.get("notes") or payload.get("text", "")[:200],
    }


def run_dacomp(args: argparse.Namespace) -> dict[str, Any]:
    task_file = Path(args.dacomp_tasks)
    tasks = load_jsonl(task_file)
    if args.dacomp_instance != "all":
        tasks = [task for task in tasks if task.get("instance_id") == args.dacomp_instance]
        if not tasks:
            raise ValueError(f"DAComp task not found: {args.dacomp_instance}")
    if args.limit:
        tasks = tasks[: args.limit]

    out_dir = Path(args.output) / "dacomp-da" / task_file.stem
    rows: list[dict[str, Any]] = []
    results: list[dict[str, Any]] = []
    for task in tasks:
        instance_id = task["instance_id"]
        task_dir = out_dir / instance_id
        result_path = task_dir / "result.json"
        if result_path.exists() and not args.overwrite:
            payload = json.loads(result_path.read_text(encoding="utf-8"))
            results.append(payload)
            rows.append(dacomp_summary_row(payload))
            continue

        started = time.time()
        try:
            sqlite_path = dacomp_sqlite_path(instance_id)
            summary_path = build_sqlite_summary(sqlite_path, task_dir / f"{instance_id}_schema_summary.md")
            file_ids = [upload_file(args.api_base, sqlite_path), upload_file(args.api_base, summary_path)]
            result = stream_chat(args.api_base, args.model, dacomp_prompt(task), file_ids, args.timeout)
            answer = extract_answer(result["text"])
            payload = {
                "benchmark": "DAComp-DA",
                "system": "DeepAnalyze",
                "task_id": instance_id,
                "status": "completed",
                "task": task,
                "data_sources": [str(sqlite_path), str(summary_path)],
                "final_answer": answer,
                "judge_status": "not_run",
                "notes": "Open-ended DAComp task; official LLM judge not run in this sample.",
                **result,
            }
        except Exception as exc:
            payload = {
                "benchmark": "DAComp-DA",
                "system": "DeepAnalyze",
                "task_id": instance_id,
                "status": "failed",
                "task": task,
                "data_sources": [],
                "final_answer": None,
                "judge_status": "not_run",
                "notes": f"{type(exc).__name__}: {exc}",
                "text": f"{type(exc).__name__}: {exc}",
                "runtime_seconds": round(time.time() - started, 3),
            }
        write_json(result_path, payload)
        (task_dir / "raw_output.txt").write_text(str(payload.get("text") or ""), encoding="utf-8")
        results.append(payload)
        rows.append(dacomp_summary_row(payload))
        write_csv(out_dir / "summary.csv", rows)
    return {"benchmark": "DAComp-DA", "results": results, "summary_csv": str(out_dir / "summary.csv")}


def main() -> int:
    parser = argparse.ArgumentParser(description="Run DeepAnalyze benchmark samples.")
    parser.add_argument("--api-base", default=DEFAULT_API)
    parser.add_argument("--model", required=True)
    parser.add_argument("--output", default=str(ROOT / "runs" / "comparisons" / "deepanalyze"))
    parser.add_argument("--timeout", type=int, default=900)
    parser.add_argument("--suite", choices=["krama", "dacomp", "both"], default="both")
    parser.add_argument("--workload", default=str(KRAMA / "workload" / "legal-easy-5.json"))
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--dacomp-tasks", default=str(DACOMP / "dacomp-da" / "tasks" / "dacomp-da.jsonl"))
    parser.add_argument("--dacomp-instance", default="dacomp-001")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    if not health(args.api_base):
        raise SystemExit(f"DeepAnalyze API is not healthy at {args.api_base}")

    results: dict[str, Any] = {"system": "DeepAnalyze", "suites": {}}
    if args.suite in {"krama", "both"}:
        results["suites"]["krama"] = run_krama(args)
    if args.suite in {"dacomp", "both"}:
        results["suites"]["dacomp"] = run_dacomp(args)
    write_json(Path(args.output) / "run_manifest.json", results)
    print(json.dumps(results, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
