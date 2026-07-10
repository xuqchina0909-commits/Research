"""Run a minimal DeepEye workflow-engine smoke test.

This adapter does not start the full Docker Compose stack. It validates the
local Python workflow layer by building and executing DeepEye's bundled
accuracy workflow example, then writes a structured result artifact.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REPO = ROOT / "repos" / "DeepEye"
DEFAULT_OUTPUT = ROOT / "runs" / "deepeye" / "workflow_smoke" / "result.json"


def run_smoke(deepeye_repo: Path) -> dict[str, object]:
    core_path = deepeye_repo / "packages" / "core"
    if not core_path.exists():
        return {
            "system": "DeepEye",
            "status": "blocked",
            "reason": f"DeepEye core package not found: {core_path}",
        }

    sys.path.insert(0, str(core_path))

    from deepeye.workflows.engine import ExecutionEngine  # noqa: PLC0415
    from deepeye.workflows.examples import (  # noqa: PLC0415
        AccuracyHandler,
        CompareHandler,
        ListSourceHandler,
        build_accuracy_workflow,
        build_registry,
    )
    from deepeye.workflows.validation import validate_workflow_graph  # noqa: PLC0415

    started = time.perf_counter()
    registry = build_registry()
    workflow = build_accuracy_workflow()
    issues = validate_workflow_graph(workflow.root, registry=registry)

    engine = ExecutionEngine(node_registry=registry)
    engine.register_handler("list_source", ListSourceHandler())
    engine.register_handler("compare", CompareHandler())
    engine.register_handler("accuracy", AccuracyHandler())
    context = engine.run(workflow, validate=True)
    runtime = time.perf_counter() - started

    node_runs = {
        node_id: {
            "status": run.status,
            "inputs": run.inputs,
            "outputs": run.outputs,
            "error": run.error,
        }
        for node_id, run in context.runs.items()
    }
    accuracy = node_runs.get("accuracy", {}).get("outputs", {}).get("accuracy")

    return {
        "system": "DeepEye",
        "status": context.status,
        "workflow_id": workflow.id,
        "workflow_name": workflow.name,
        "validation_issues": [issue.model_dump() for issue in issues],
        "node_order": list(context.runs.keys()),
        "node_runs": node_runs,
        "final_answer": accuracy,
        "runtime_seconds": round(runtime, 4),
        "notes": (
            "Python workflow-engine smoke test only; full Docker/WebUI stack "
            "is not started in this adapter."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a minimal DeepEye workflow smoke test.")
    parser.add_argument("--deepeye-repo", default=str(DEFAULT_REPO), help="Path to local DeepEye checkout.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Path to write result JSON.")
    args = parser.parse_args()

    result = run_smoke(Path(args.deepeye_repo).resolve())
    output = Path(args.output).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result.get("status") == "success" else 1


if __name__ == "__main__":
    raise SystemExit(main())
