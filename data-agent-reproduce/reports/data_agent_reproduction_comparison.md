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
- DeepAnalyze demo was not run yet because it requires DeepAnalyze-8B/vLLM or a DeepAnalyze API key.
- A runnable DeepAnalyze adapter scaffold was created for later single-task execution once repositories and model settings are available.
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

Key generated files:

- `logs/environment_check.md`
- `logs/install_logs.md`
- `logs/run_logs.md`
- `reports/krama_legal_results.csv`
- `reports/krama_environment_results.csv`
- `reports/dacomp_feasibility_notes.md`
- `adapters/deepanalyze_runner.py`

No benchmark scores were fabricated.
