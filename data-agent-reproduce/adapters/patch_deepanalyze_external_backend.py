#!/usr/bin/env python3
"""Configure a local DeepAnalyze checkout for an OpenAI-compatible backend."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT / "repos" / "DeepAnalyze"


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if new in text:
        return
    if old not in text:
        raise RuntimeError(f"Expected text not found in {path}: {old!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def main() -> int:
    config = REPO / "API" / "config.py"
    chat_api = REPO / "API" / "chat_api.py"
    replace_once(
        config,
        'API_BASE = "http://localhost:8000/v1"  # vLLM API endpoint\nMODEL_PATH = "DeepAnalyze-8B"',
        'API_BASE = os.environ.get("DEEPANALYZE_MODEL_API_BASE", "http://localhost:8000/v1")\nMODEL_PATH = os.environ.get("DEEPANALYZE_MODEL", "DeepAnalyze-8B")',
    )
    replace_once(
        chat_api,
        'vllm_client = openai.OpenAI(base_url=API_BASE, api_key="dummy")\nvllm_client_async = openai.AsyncOpenAI(base_url=API_BASE, api_key="dummy")',
        'model_api_key = os.environ.get("DEEPANALYZE_MODEL_API_KEY", "dummy")\nvllm_client = openai.OpenAI(base_url=API_BASE, api_key=model_api_key)\nvllm_client_async = openai.AsyncOpenAI(base_url=API_BASE, api_key=model_api_key)',
    )
    replace_once(
        chat_api,
        'vllm_messages.append({"role": "execute", "content": exe_output})',
        'vllm_messages.append({"role": "user", "content": f"代码执行结果如下，请基于该结果继续分析：\\n{exe_output}"})',
    )
    replace_once(
        chat_api,
        'vllm_messages.append({"role": "execute", "content": exe_output})',
        'vllm_messages.append({"role": "user", "content": f"代码执行结果如下，请基于该结果继续分析：\\n{exe_output}"})',
    )
    print("DeepAnalyze external backend patch applied.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
