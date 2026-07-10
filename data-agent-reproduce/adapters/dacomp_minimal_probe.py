"""Probe a minimal DAComp-DA task without running a model agent."""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DACOMP = ROOT / "repos" / "DAComp"
DEFAULT_OUTPUT = ROOT / "runs" / "dacomp" / "minimal_probe" / "dacomp-001.json"


def load_task(task_index: Path, instance_id: str) -> dict[str, Any]:
    with task_index.open("r", encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            if obj.get("instance_id") == instance_id:
                return obj
    raise ValueError(f"Task not found in {task_index}: {instance_id}")


def probe_sqlite(sqlite_path: Path, sample_rows: int) -> dict[str, Any]:
    if not sqlite_path.exists():
        return {
            "status": "missing",
            "path": str(sqlite_path),
            "tables": [],
        }

    con = sqlite3.connect(sqlite_path)
    con.row_factory = sqlite3.Row
    try:
        tables = [
            row[0]
            for row in con.execute(
                "select name from sqlite_master where type='table' order by name"
            ).fetchall()
        ]
        table_profiles = []
        for table in tables:
            columns = [
                {"name": row[1], "type": row[2]}
                for row in con.execute(f'pragma table_info("{table}")').fetchall()
            ]
            row_count = con.execute(f'select count(*) from "{table}"').fetchone()[0]
            rows = [
                dict(row)
                for row in con.execute(f'select * from "{table}" limit ?', (sample_rows,)).fetchall()
            ]
            table_profiles.append(
                {
                    "name": table,
                    "row_count": row_count,
                    "columns": columns,
                    "sample_rows": rows,
                }
            )
        return {
            "status": "available",
            "path": str(sqlite_path),
            "size_bytes": sqlite_path.stat().st_size,
            "tables": table_profiles,
        }
    finally:
        con.close()


def main() -> int:
    parser = argparse.ArgumentParser(description="Probe one minimal DAComp-DA task.")
    parser.add_argument("--dacomp-repo", default=str(DEFAULT_DACOMP), help="Path to DAComp checkout.")
    parser.add_argument("--instance-id", default="dacomp-001")
    parser.add_argument("--sample-rows", type=int, default=2)
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    args = parser.parse_args()

    repo = Path(args.dacomp_repo).resolve()
    task_index = repo / "dacomp-da" / "tasks" / "dacomp-da.jsonl"
    sqlite_path = repo / "dacomp-da" / "tasks" / args.instance_id / f"{args.instance_id}.sqlite"

    task = load_task(task_index, args.instance_id)
    data = probe_sqlite(sqlite_path, args.sample_rows)
    result = {
        "benchmark": "DAComp-DA",
        "status": "success" if data["status"] == "available" else "blocked",
        "instance_id": args.instance_id,
        "task": task,
        "data": data,
        "notes": "Data/index probe only; no model agent or LLM judge was run.",
    }

    output = Path(args.output).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["status"] == "success" else 1


if __name__ == "__main__":
    raise SystemExit(main())
