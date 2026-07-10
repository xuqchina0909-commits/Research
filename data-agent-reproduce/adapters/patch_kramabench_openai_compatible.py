#!/usr/bin/env python3
"""Patch a local KramaBench checkout for OpenAI-compatible providers.

This adds support for OPENAI_BASE_URL and a custom DS-GURU SUT that reads
OPENAI_MODEL from the local .env file. It is intentionally small and idempotent.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KRAMA = ROOT / "repos" / "KramaBench"


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if new in text:
        return
    if old not in text:
        raise RuntimeError(f"Expected text not found in {path}: {old[:80]!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def append_once(path: Path, marker: str, block: str) -> None:
    text = path.read_text(encoding="utf-8")
    if marker in text:
        return
    path.write_text(text.rstrip() + "\n\n" + block.strip() + "\n", encoding="utf-8")


def main() -> int:
    if not KRAMA.exists():
        raise SystemExit(f"KramaBench checkout not found: {KRAMA}")

    generator_utils = KRAMA / "systems" / "dsguru" / "generator_utils.py"
    baseline_utils = KRAMA / "systems" / "dsguru" / "baseline_utils.py"
    variations = KRAMA / "systems" / "dsguru" / "baseline_system_variations.py"
    evaluate = KRAMA / "evaluate.py"

    replace_once(
        evaluate,
        '''    else:
        dataset_name = workload

    results_df = None
''',
        '''    else:
        dataset_name = workload
        # Workload variants such as legal-easy-1 use the base dataset directory.
        dataset_directory = os.path.join(project_root_dir, f"data/{dataset_name}/input")
        if not os.path.isdir(dataset_directory):
            base_dataset_name = workload.split("-", 1)[0]
            base_dataset_directory = os.path.join(
                project_root_dir, f"data/{base_dataset_name}/input"
            )
            if os.path.isdir(base_dataset_directory):
                dataset_name = base_dataset_name

    results_df = None
''',
    )

    replace_once(
        generator_utils,
        'OpenAIModelList = ["gpt-4o", "gpt-4o-mini", "gpt-4o-v", "gpt-4o-mini-v", "o3-2025-04-16"]',
        '''OpenAIModelList = [
    "gpt-4o",
    "gpt-4o-mini",
    "gpt-4o-v",
    "gpt-4o-mini-v",
    "o3-2025-04-16",
    "Qwen/Qwen2.5-7B-Instruct",
]''',
    )
    replace_once(
        generator_utils,
        '''def get_api_key(key: str) -> str:
    # get API key from environment or throw an exception if it's not set
    if key not in os.environ:
        print(f"KEY: {key}")
        print(f"{os.environ.keys()}")
        raise ValueError("key not found in environment variables")

    return os.environ[key]
''',
        '''def get_api_key(key: str) -> str:
    # get API key from environment or throw an exception if it's not set
    if key not in os.environ:
        print(f"KEY: {key}")
        print(f"{os.environ.keys()}")
        raise ValueError("key not found in environment variables")

    return os.environ[key]


def create_openai_client():
    kwargs = {"api_key": get_api_key("OPENAI_API_KEY")}
    base_url = os.environ.get("OPENAI_BASE_URL")
    if base_url:
        kwargs["base_url"] = base_url
    return OpenAI(**kwargs)
''',
    )
    replace_once(
        generator_utils,
        "if model in OpenAIModelList:\n            self.client = OpenAI(api_key=get_api_key(\"OPENAI_API_KEY\"))",
        "if model in OpenAIModelList or os.environ.get(\"OPENAI_BASE_URL\"):\n            self.client = create_openai_client()",
    )
    replace_once(
        generator_utils,
        "if self.model in OpenAIModelList:\n            self.client = OpenAI(api_key=get_api_key(\"OPENAI_API_KEY\"))",
        "if self.model in OpenAIModelList or os.environ.get(\"OPENAI_BASE_URL\"):\n            self.client = create_openai_client()",
    )

    replace_once(
        baseline_utils,
        '''load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))''',
        '''load_dotenv()
_openai_kwargs = {"api_key": os.getenv("OPENAI_API_KEY")}
if os.getenv("OPENAI_BASE_URL"):
    _openai_kwargs["base_url"] = os.getenv("OPENAI_BASE_URL")
client = OpenAI(**_openai_kwargs)''',
    )

    replace_once(
        variations,
        "from .baseline_system import BaselineLLMSystem, BaselineLLMSystemOllama",
        "import os\n\nfrom .baseline_system import BaselineLLMSystem, BaselineLLMSystemOllama",
    )
    append_once(
        variations,
        "class BaselineLLMSystemCustomOpenAIFewShot",
        '''
class BaselineLLMSystemSiliconFlowQwen7BFewShot(BaselineLLMSystem):
    def __init__(self, verbose=False, *args, **kwargs):
        super().__init__(
            model="Qwen/Qwen2.5-7B-Instruct",
            name="BaselineLLMSystemSiliconFlowQwen7BFewShot",
            variance="few_shot",
            verbose=verbose,
            supply_data_snippet=True,
            *args,
            **kwargs,
        )


class BaselineLLMSystemCustomOpenAIFewShot(BaselineLLMSystem):
    def __init__(self, verbose=False, *args, **kwargs):
        super().__init__(
            model=os.environ.get("OPENAI_MODEL", "Qwen/Qwen2.5-7B-Instruct"),
            name="BaselineLLMSystemCustomOpenAIFewShot",
            variance="few_shot",
            verbose=verbose,
            supply_data_snippet=True,
            *args,
            **kwargs,
        )
''',
    )

    print("KramaBench OpenAI-compatible patch applied.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
