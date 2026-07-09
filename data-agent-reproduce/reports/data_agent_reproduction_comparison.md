# Data Agent Reproduction and Comparison Report

## 1. Execution Summary

- Stage 0 directory setup completed under `data-agent-reproduce/`.
- Local environment has `git`, `python3`, and `pip3`; `python`, `pip`, `node`, `npm`, and Docker are missing from PATH.
- All requested GitHub repository transfers failed due to network timeout or stalled SSH transfer.
- KramaBench Legal baseline was not run; no benchmark score is claimed.
- DeepAnalyze demo was not run because the repository was not available locally.
- A runnable DeepAnalyze adapter scaffold was created for later single-task execution once repositories and model settings are available.
- Result CSVs were generated with `not_evaluable` rows instead of fabricated scores.

## 2. Experiment Objects

| Object | Intended role in this study | Current local status |
| --- | --- | --- |
| KramaBench | Primary small-sample end-to-end Data Agent pipeline benchmark, starting with Legal workload. | Not cloned. |
| DAComp | Later lifecycle/data-intelligence feasibility benchmark. | Not cloned; only stage 0 clone attempted. |
| DeepAnalyze | Primary autonomous data science agent candidate for stage 2. | Not cloned. |
| DeepEye | Workflow-centric Data Agent candidate for later workflow-native analysis. | Not cloned; Docker also unavailable. |
| DeepPrep | Data preparation module / paper mechanism to verify later. | Not checked in stage 0-2 because DeepAnalyze repository was unavailable. |

## 3. Environment and Reproduction Status

See `logs/environment_check.md` and `logs/install_logs.md`.

| Capability | Status | Impact |
| --- | --- | --- |
| Git | available | Can manage the local reproduction project. |
| Python 3 | available as `python3` | Can run local adapters and lightweight analysis scripts. |
| pip | available as `pip3` | Can install Python dependencies after repositories are available. |
| Node/npm | missing | Web UI/front-end workflows are blocked. |
| Docker/Compose | missing | Containerized demos, especially for DeepEye, are blocked. |
| GitHub transfer | failed | Official repositories were not locally available; stages 1 and 2 could not run benchmark/system code. |

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

No Legal task was run.

CSV path:

- `reports/krama_legal_results.csv`

Reason:

- KramaBench repository could not be cloned via HTTPS, SSH, or zip download.
- No official baseline or evaluation script was locally available.

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

Blocked:

- DeepAnalyze checkout unavailable.
- Official install/demo commands could not be read locally.
- KramaBench task schema unavailable.
- No API key/model service was configured or verified.

## 8. Failure Cases

| Failure type | Observed? | Evidence |
| --- | --- | --- |
| Repository transfer failure | yes | GitHub clone/download timed out. |
| Installation failure | not reached | No repository checkout. |
| Dataset preparation failure | not reached | No KramaBench scripts/data. |
| Baseline execution failure | not reached | No runnable KramaBench code. |
| DeepAnalyze demo failure | not reached | No DeepAnalyze checkout. |
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

