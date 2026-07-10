# Data Agent Reproduction and Comparison Report

## 1. Execution Summary

- Stage 0 directory setup completed under `data-agent-reproduce/`.
- Local environment has `git`, `python3`, and `pip3`; `python`, `pip`, `node`, `npm`, and Docker are missing from PATH.
- DeepAnalyze was later cloned successfully through SSH.
- KramaBench was later provided as a manually downloaded zip and extracted successfully.
- KramaBench evaluation harness now runs under a local Python 3.12 virtual environment.
- KramaBench `DummySystem` smoke tests completed for `legal-tiny` and a 5-task `legal-easy-5` subset.
- DS-GURU official baseline was attempted after `OPENAI_API_KEY` was configured, but OpenAI returned `429 insufficient_quota`.
- SiliconFlow OpenAI-compatible Qwen/Qwen2.5-7B-Instruct was connected through a local KramaBench patch; the API call completed but produced invalid/truncated JSON on the 1-task Legal smoke test.
- SiliconFlow `Qwen/Qwen3-Coder-30B-A3B-Instruct` completed the same 1-task Legal smoke test and returned valid JSON plus executable code; the task score was still 0.0, so answer correctness remains to be improved.
- DeepAnalyze demo was not run yet because it requires DeepAnalyze-8B/vLLM or a DeepAnalyze API key.
- A runnable DeepAnalyze adapter scaffold was created for later single-task execution once repositories and model settings are available.
- DeepAnalyze API stage-2 compatibility validation was started with the configured SiliconFlow Qwen3 Coder backend; file upload and service startup passed, but the model did not reliably follow DeepAnalyze's tagged execution protocol.
- Result CSVs were generated with `not_evaluable` rows instead of fabricated scores.

## 2. Experiment Objects

| Object | Intended role in this study | Current local status |
| --- | --- | --- |
| DAComp | Later lifecycle/data-intelligence feasibility benchmark. | Not cloned; only stage 0 clone attempted. |
| KramaBench | Primary small-sample end-to-end Data Agent pipeline benchmark, starting with Legal workload. | Extracted from user-provided zip; harness smoke test runs. |
| DeepAnalyze | Primary autonomous data science agent candidate for stage 2. | Cloned successfully; README/CLI/API inspected. |
| DeepEye | Workflow-centric Data Agent candidate for later workflow-native analysis. | Not cloned; Docker also unavailable. |
| DeepPrep | Data preparation module / paper mechanism to verify later. | Mentioned in DeepAnalyze README as forthcoming companion; full runnable code not yet verified. |

## 3. Environment and Reproduction Status

See `logs/environment_check.md` and `logs/install_logs.md`.

| Capability | Status | Impact |
| --- | --- | --- |
| Git | available | Can manage the local reproduction project. |
| Python 3 | available as `python3` | Can run local adapters and lightweight analysis scripts. |
| pip | available as `pip3` | Can install Python dependencies after repositories are available. |
| Node/npm | missing | Web UI/front-end workflows are blocked. |
| Docker/Compose | missing | Containerized demos, especially for DeepEye, are blocked. |
| GitHub transfer | partially resolved | DeepAnalyze cloned successfully; KramaBench was completed through manual zip download. |

## 4. Benchmark Adaptation Plan

The intended KramaBench-to-system adapter contract is:

1. Read one benchmark task as JSON or a normalized task record.
2. Preserve the original task description and data paths.
3. Invoke the target system through CLI/API/script once its official interface is known.
4. Save generated code, execution logs, intermediate artifacts, report files, final answer, runtime, and errors.
5. Convert the result into the common CSV schema:

```text
system, task_id, workload, final_score, subtask_score, code_success, runtime, cost, error_count, human_fix_count, notes
```

Current adapter scaffold:

- `adapters/deepanalyze_runner.py`

It intentionally marks runs as `not_evaluable` when the DeepAnalyze checkout or task file is missing.

## 5. KramaBench Legal Result

Legal smoke tests were run with `DummySystem`, not with DS-GURU.

CSV path:

- `reports/krama_legal_results.csv`

Output paths:

- `runs/kramabench/results/DummySystem/legal-tiny_measures_20260710_091520.csv`
- `runs/kramabench/results/DummySystem/legal-easy-5_measures_20260710_091607.csv`
- `runs/kramabench/results/aggregated_results.csv`

Current interpretation:

- Harness and data are usable.
- `DummySystem` scores 0.0 as expected and is only a smoke test.
- DS-GURU reached OpenAI but remains blocked until API quota/billing is available.
- SiliconFlow Qwen 7B reached the provider successfully, but the first DS-GURU run failed answer extraction because the model output was invalid JSON and hit the output cap.

## 6. KramaBench Environment Result

No Environment task was run.

CSV path:

- `reports/krama_environment_results.csv`

Reason:

- The plan required Legal to run first; Legal was blocked before execution.

## 7. Stage 2 DeepAnalyze Status

Completed:

- Created `adapters/deepanalyze_runner.py`.
- Adapter writes structured run artifacts even when execution is blocked.
- DeepAnalyze repository cloned successfully.
- README and CLI docs inspected.
- DeepAnalyze supports CLI/API usage, but requires DeepAnalyze-8B through vLLM or DeepAnalyze API access.

Stage 2 compatibility validation:

- DeepAnalyze API server started successfully on local port 8200.
- The Legal CSV uploaded successfully through `/v1/files`.
- The external SiliconFlow backend was reached successfully.
- The server rejected the original internal `execute` role for the external OpenAI-compatible API; a local compatibility patch maps execution feedback to a user message.
- After that patch, Qwen3 Coder returned empty `<Analyze>`, `<Code>`, and `<Answer>` tags instead of a real executable pipeline.

Conclusion: the service and file-execution plumbing are partially validated, but this is not yet an official DeepAnalyze-8B reproduction. The official path still requires the DeepAnalyze-8B model or a DeepAnalyze API key. The durable configuration helper is `adapters/patch_deepanalyze_external_backend.py`.

Blocked:

- No DeepAnalyze API key or local DeepAnalyze-8B/vLLM service is configured.
- Node/Docker are still missing from the base environment, limiting WebUI/WebUI v2 paths.

## 8. Failure Cases

| Failure type | Observed? | Evidence |
| --- | --- | --- |
| Repository transfer failure | yes | GitHub clone/download timed out. |
| Installation failure | partially | `pip install -e` failed due setuptools flat-layout discovery; dependency-only install workaround succeeded. |
| Dataset preparation failure | no for Legal smoke | KramaBench Legal data available from zip. |
| Baseline execution failure | blocked | DS-GURU requires model API key. |
| OpenAI quota failure | yes | DS-GURU attempt returned `429 insufficient_quota`. |
| OpenAI-compatible model output failure | yes | SiliconFlow Qwen 7B returned invalid/truncated JSON for `legal-easy-3`. |
| DeepAnalyze demo failure | blocked | Requires DeepAnalyze-8B/vLLM or API key. |
| Final answer extraction failure | not reached | No task execution. |

## 9. Current Capability Comparison

| Dimension | DeepEye | DeepAnalyze | DeepPrep |
| --- | --- | --- | --- |
| Core positioning | Workflow-centric Data Agent candidate, to verify later. | End-to-end autonomous data science agent candidate, stage 2 priority. | Data preparation module / paper mechanism, to verify later. |
| Runnable locally | Not verified. | Not verified. | Not verified. |
| KramaBench adaptation | Not attempted in stage 0-2. | Adapter scaffold created; not executed. | Not attempted. |
| DAComp adaptation | Not attempted. | Not attempted. | Not attempted. |
| End-to-end analysis | Not evaluated. | Not evaluated. | Not a full SUT unless complete code is found. |
| Data preparation | Not evaluated. | Not evaluated. | Primary expected role, unverified. |
| Workflow controllability | Not evaluated. | Not evaluated. | Not evaluated. |
| Intermediate inspectability | Not evaluated. | Adapter designed to collect artifacts. | Not evaluated. |
| Report generation | Not evaluated. | Not evaluated. | Not evaluated. |
| Quantitative evaluation | Not available yet. | Not available yet. | Not available yet. |
| Engineering maturity | Not evaluated. | Not evaluated. | Not evaluated. |

## 10. Interim Technical Insight

At this point, the only defensible conclusion is about reproducibility logistics, not model/system quality:

1. A small-sample KramaBench-first plan remains appropriate, but it depends on reliable repository/data access.
2. DeepAnalyze should remain the first SUT to adapt because it is closest to the requested end-to-end analysis workflow.
3. DeepEye likely needs Node/Docker or a backend service path before serious evaluation.
4. DeepPrep should not be treated as a full SUT until its code availability is verified inside the DeepAnalyze repo or related links.
5. The evaluation harness should continue to record `not_evaluable` rather than inventing scores when systems do not run.

## 11. Next Steps

1. Restore reliable GitHub transfer or provide local zip/checkouts for KramaBench and DeepAnalyze.
2. Re-run stage 0 repository inspection.
3. Install KramaBench dependencies in an isolated Python environment.
4. Select 5-10 Legal tasks and run the official baseline.
5. Install DeepAnalyze, run its official demo, then bind `deepanalyze_runner.py` to the confirmed CLI/API.

## 12. Appendix

## 13. 最新模型验证（中文记录）

本次将硅基流动模型切换为 `Qwen/Qwen3-Coder-30B-A3B-Instruct`，配置为：

```text
OPENAI_BASE_URL=https://api.siliconflow.cn/v1
OPENAI_MODEL=Qwen/Qwen3-Coder-30B-A3B-Instruct
```

验证任务：`legal-easy-3`（通过 `legal-easy-1` 工作负载运行）。

验证结果：

- 接口调用成功。
- 返回了合法 JSON。
- 成功生成并执行了代码流程。
- 输入 token：792；输出 token：360；总 token：1152。
- 运行时间约 7.94 秒。
- 当前任务得分：0.0；原因是该精简任务没有提供数据文件，并非已证明模型计算错误。

与 `Qwen/Qwen2.5-7B-Instruct` 的对比：7B 模型在相同任务上输出被截断且不是合法 JSON；30B Coder 模型已经越过了格式和执行层面的阻塞。本次 0 分的直接原因是测试任务缺少数据文件，下一步应先恢复完整任务数据，再评价答案计算能力。

后续实验报告统一使用中文，保留模型名、类名、路径和命令等必要的英文标识。

### 数据集目录映射修复

问题原因：工作负载名为 `legal-easy-1`，旧逻辑直接寻找 `data/legal-easy-1/input`，而实际数据位于 `data/legal/input`，因此模型收到的文件列表为空。

修复内容：`evaluate.py` 现在会在工作负载目录不存在时，自动回退到连字符前的基础数据集目录，例如 `legal-easy-1` 回退到 `legal`。运行时使用 `--use_truth_subset`，只加载任务声明的 CSV 文件。

修复后验证：

- 实际加载文件：`csn-data-book-2024-csv/CSVs/2024_CSN_Number_of_Reports_by_Type.csv`
- 2001 年：86250
- 2024 年：1135291
- 正确答案：13.1628
- KramaBench 任务得分：100.0

Key generated files:

- `logs/environment_check.md`
- `logs/install_logs.md`
- `logs/run_logs.md`
- `reports/krama_legal_results.csv`
- `reports/krama_environment_results.csv`
- `reports/dacomp_feasibility_notes.md`
- `adapters/deepanalyze_runner.py`

No benchmark scores were fabricated.
