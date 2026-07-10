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


def replace_function(path: Path, function_name: str, next_function: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    start = text.index(f"def {function_name}")
    end = text.index(f"\ndef {next_function}", start)
    if new.strip() in text:
        return
    path.write_text(text[:start] + new.rstrip() + text[end:], encoding="utf-8")


def main() -> int:
    config = REPO / "API" / "config.py"
    chat_api = REPO / "API" / "chat_api.py"
    utils = REPO / "API" / "utils.py"
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
        utils,
        '        instruction_body = user_content if user_content else "# Instruction"\n',
        '        instruction_body = user_content if user_content else "# Instruction"\n'
        '        if os.environ.get("DEEPANALYZE_EXTERNAL_COMPAT") == "1":\n'
        '            instruction_body += """\n\n'
        '兼容模式要求：你不是原生 DeepAnalyze 模型。必须完成真实任务，不要返回省略号或假设数据。\n'
        '请严格按以下流程输出：先输出 <Analyze>...</Analyze>，再输出可执行的 <Code>...</Code>。\n'
        '代码执行后，根据执行结果输出 <Answer>...</Answer>。如果使用 Markdown 代码块，也必须放入 <Code> 标签内。\n'
        '不要只解释代码，不要输出占位符。"""\n',
    )
    replace_once(
        chat_api,
        'vllm_messages.append({"role": "execute", "content": exe_output})',
        'vllm_messages.append({"role": "user", "content": f"代码执行结果如下，请基于该结果继续分析：\\n{exe_output}"})',
    )
    replace_once(
        chat_api,
        '                            code_str = Chinese_matplot_str + "\\n" + code_str',
        '                            if os.environ.get("DEEPANALYZE_EXTERNAL_COMPAT") != "1":\n                                code_str = Chinese_matplot_str + "\\n" + code_str',
    )
    replace_once(
        chat_api,
        '                        code_str = Chinese_matplot_str + "\\n" + code_str',
        '                        if os.environ.get("DEEPANALYZE_EXTERNAL_COMPAT") != "1":\n                            code_str = Chinese_matplot_str + "\\n" + code_str',
    )
    replace_once(
        chat_api,
        '                assistant_reply = ""\n                finished = False\n',
        '                assistant_reply = ""\n                finished = False\n                compat_mode = os.environ.get("DEEPANALYZE_EXTERNAL_COMPAT") == "1"\n                retry_count = 0\n',
    )
    replace_once(
        chat_api,
        '            assistant_reply = ""\n            finished = False\n',
        '            assistant_reply = ""\n            finished = False\n            compat_mode = os.environ.get("DEEPANALYZE_EXTERNAL_COMPAT") == "1"\n            retry_count = 0\n',
    )
    compat_extractor = "\n".join([
        "def extract_code_from_segment(segment: str) -> Optional[str>:",
        "    code_match = re.search(r\"<Code>(.*?)</Code>\", segment, re.DOTALL)",
        "    code_content = code_match.group(1).strip() if code_match else segment.strip()",
        "    md_match = re.search(r\"```(?:python|py)?\\\\s*(.*?)```\", code_content, re.DOTALL | re.IGNORECASE)",
        "    if md_match:",
        "        code_content = md_match.group(1).strip()",
        "    if code_content in {\"\", \"...\", \"…\", \"pass\"}:",
        "        return None",
        "    if code_match or md_match:",
        "        return code_content",
        "    if re.search(r\"(?:^|\\\\n)\\\\s*(?:import |from |pd\\\\.|print\\\\(|df\\\\s*=)\", code_content):",
        "        return code_content",
        "    return None",
        "",
    ])
    compat_extractor = compat_extractor.replace("Optional[str>", "Optional[str]")
    replace_function(utils, "extract_code_from_segment", "fix_tags_and_codeblock", compat_extractor)
    replace_once(
        chat_api,
        'vllm_messages.append({"role": "execute", "content": exe_output})',
        'vllm_messages.append({"role": "user", "content": f"代码执行结果如下，请基于该结果继续分析：\\n{exe_output}"})',
    )
    print("DeepAnalyze external backend patch applied.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
