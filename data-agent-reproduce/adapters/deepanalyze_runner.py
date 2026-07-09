#!/usr/bin/env python3
"""Adapter scaffold for running one KramaBench task with DeepAnalyze.

The current implementation is intentionally conservative: it records all inputs
and marks the run as blocked when DeepAnalyze or the task file is unavailable.
Once the DeepAnalyze CLI/API is confirmed, wire the invocation into
`run_deepanalyze`.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from pathlib import Path
from typing import Any, Dict, Optional


def read_task(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Task file does not exist: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def discover_deepanalyze(repo_path: Path) -> Dict[str, Any]:
    files = {
        "repo_exists": repo_path.exists(),
        "readme": (repo_path / "README.md").exists(),
        "requirements": (repo_path / "requirements.txt").exists(),
        "pyproject": (repo_path / "pyproject.toml").exists(),
        "examples_dir": (repo_path / "examples").exists(),
        "scripts_dir": (repo_path / "scripts").exists(),
    }
    return files


def run_deepanalyze(
    repo_path: Path,
    task: Dict[str, Any],
    data_dir: Optional[Path],
    output_dir: Path,
) -> Dict[str, Any]:
    discovery = discover_deepanalyze(repo_path)
    if not discovery["repo_exists"]:
        return {
            "status": "blocked",
            "reason": "DeepAnalyze repository is not available locally.",
            "discovery": discovery,
            "generated_code_path": None,
            "final_answer": None,
            "cost": "unknown",
        }

    # Placeholder for the confirmed upstream command/API.
    # Example shape after inspection:
    # cmd = ["python3", "path/to/deepanalyze_entry.py", "--task", ...]
    cmd = None
    if cmd is None:
        return {
            "status": "blocked",
            "reason": "DeepAnalyze invocation is not wired yet because official CLI/API was not inspected locally.",
            "discovery": discovery,
            "generated_code_path": None,
            "final_answer": None,
            "cost": "unknown",
        }

    started = time.time()
    process = subprocess.run(
        cmd,
        cwd=str(repo_path),
        text=True,
        capture_output=True,
        check=False,
    )
    runtime = time.time() - started
    write_text(output_dir / "stdout.log", process.stdout)
    write_text(output_dir / "stderr.log", process.stderr)

    return {
        "status": "completed" if process.returncode == 0 else "failed",
        "returncode": process.returncode,
        "runtime_seconds": runtime,
        "generated_code_path": None,
        "final_answer": None,
        "cost": "unknown",
    }


def normalize_task_metadata(task: Dict[str, Any], task_path: Path) -> Dict[str, Any]:
    return {
        "task_path": str(task_path),
        "task_id": task.get("task_id") or task.get("id") or task_path.stem,
        "workload": task.get("workload") or task.get("domain") or "unknown",
        "question": task.get("question") or task.get("prompt") or task.get("instruction"),
        "raw_keys": sorted(task.keys()),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run one KramaBench task with DeepAnalyze.")
    parser.add_argument("--task-json", required=True, help="Path to one normalized KramaBench task JSON.")
    parser.add_argument("--data-dir", default=None, help="Optional path to task data directory.")
    parser.add_argument(
        "--deepanalyze-repo",
        default="data-agent-reproduce/repos/DeepAnalyze",
        help="Path to local DeepAnalyze checkout.",
    )
    parser.add_argument(
        "--out",
        default="data-agent-reproduce/runs/deepanalyze/latest",
        help="Output directory for adapter artifacts.",
    )
    args = parser.parse_args()

    started = time.time()
    task_path = Path(args.task_json).expanduser().resolve()
    data_dir = Path(args.data_dir).expanduser().resolve() if args.data_dir else None
    repo_path = Path(args.deepanalyze_repo).expanduser().resolve()
    output_dir = Path(args.out).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    result: Dict[str, Any] = {
        "system": "DeepAnalyze",
        "task_file": str(task_path),
        "data_dir": str(data_dir) if data_dir else None,
        "deepanalyze_repo": str(repo_path),
        "status": "unknown",
        "error": None,
    }

    try:
        task = read_task(task_path)
        metadata = normalize_task_metadata(task, task_path)
        write_json(output_dir / "input_task.json", task)
        write_json(output_dir / "task_metadata.json", metadata)
        system_result = run_deepanalyze(repo_path, task, data_dir, output_dir)
        result.update(system_result)
    except Exception as exc:  # Keep adapter failures inspectable.
        result.update(
            {
                "status": "failed",
                "error": f"{type(exc).__name__}: {exc}",
                "final_answer": None,
                "cost": "unknown",
            }
        )

    result["runtime_seconds"] = round(time.time() - started, 3)
    write_json(output_dir / "result.json", result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] in {"completed", "blocked"} else 1


if __name__ == "__main__":
    raise SystemExit(main())

