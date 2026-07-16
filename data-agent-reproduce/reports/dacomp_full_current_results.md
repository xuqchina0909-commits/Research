# DAComp 全量当前结果记录

记录时间：2026-07-16

## 数据状态

- 已从 HuggingFace 镜像下载 DAComp-DA 英文全量数据：`tasks/`，100 个 SQLite。
- 已从 HuggingFace 镜像下载 DAComp-DA 中文全量数据：`tasks_zh/`，100 个 SQLite。
- 两个索引文件均为 100 行。
- 数据目录 `data-agent-reproduce/repos/` 已被 `.gitignore` 忽略，本次不提交大体量数据集。

## 代码改动

本轮修改了两个 benchmark runner：

- `adapters/deepanalyze_benchmark_runner.py`
  - 支持 `--dacomp-tasks` 指定中文任务索引。
  - 支持 `--dacomp-instance all` 批量运行 DAComp。
  - 支持中文 SQLite 路径优先，英文 SQLite 路径回退。
  - DAComp 批量运行时逐题落盘并写 `summary.csv`。

- `adapters/deepeye_benchmark_runner.py`
  - DAComp 中文任务优先使用 `tasks_zh/dacomp-zh-xxx/dacomp-zh-xxx.sqlite`。
  - 修复 `continue` 缩进问题，避免 DAComp 任务被整体跳过。
  - 中文收口返回 `No workflow run is available...` 时不覆盖上一轮真实输出。
  - DAComp 单题等待使用统一硬阈值，主回答和中文收口共享同一个 `--timeout` 预算。
  - 运行结束时只打印 compact summary，完整消息和报告保存在 `run_summary.json` 与逐题目录，避免终端输出过大。

## DeepAnalyze 结果

运行目录：

```text
data-agent-reproduce/runs/comparisons/deepanalyze_dacomp_zh_full
```

汇总：

| 指标 | 数值 |
|---|---:|
| 任务数 | 100 |
| completed | 99 |
| failed | 1 |
| 总运行时间 | 1148.390 秒 |
| 平均每题耗时 | 11.484 秒 |

失败任务：

| 任务 | 状态 | 原因 |
|---|---|---|
| `dacomp-zh-061` | failed | `ConnectionError: ('Connection aborted.', OSError(22, 'Invalid argument'))` |

注意：DeepAnalyze 的本轮结果未运行 DAComp 官方 LLM judge。虽然 completed 比例高，但抽样可见部分回答存在模板化、疑似未充分基于真实 SQL 计算的风险，因此当前只能作为“可批量完成链路”的结果，不能等同于高可信正式评分。

## DeepEye 结果

运行目录：

```text
data-agent-reproduce/runs/comparisons/deepeye_dacomp_zh_full
```

全量结果：

| 指标 | 数值 |
|---|---:|
| 任务数 | 100 |
| completed | 28 |
| failed | 32 |
| timeout | 40 |

阈值策略：

- 前半段曾使用 900 秒、240 秒、180 秒 timeout 进行断点续跑。
- 为避免少数长尾任务拖住全量测评，后续改为 120 秒单题硬阈值。
- 从 `dacomp-zh-065` 起，超过阈值的任务直接按 timeout 落盘并进入下一题。
- `runtime_seconds` 包含历史长等待和跨夜阻塞时间，因此本轮不把总耗时作为公平速度指标；状态分布是当前主要结论。

当前判断：

- DeepEye 已能使用完整 DAComp 中文数据进入 workflow 执行层。
- DeepEye 已跑完 DAComp 中文 100 题，但当前模型/工作流组合稳定性不足，completed 仅 28 题。
- 失败类型主要包括短文本失败、非中文报告、无 assistant 结果 timeout，以及 workflow 输出未能形成可用最终报告。
- 后段大量任务按 120 秒阈值 timeout，说明 DeepEye 后端 workflow 或模型响应存在明显长尾/阻塞风险。
- 本报告仅统计运行状态，尚未接入 DAComp 官方 LLM judge，因此不能等同于正式质量分数。

## 横向阶段性结论

| 维度 | DeepAnalyze | DeepEye |
|---|---|---|
| DAComp 中文数据接入 | 已接入 | 已接入 |
| 当前批量进度 | 100/100 | 100/100 |
| 当前 completed 比例 | 99% | 28% |
| 主要优势 | 批量链路快，几乎可跑完全量 | 能走 DeepEye 原生 workflow/数据源链路 |
| 主要风险 | 输出可信度需 judge 或 SQL trace 校验 | 稳定性、长尾响应和最终报告生成不足 |

下一步建议：保留当前提交作为版本记录；后续若继续优化 DeepEye，应优先分析 completed/failed/timeout 的逐题日志，区分模型能力问题、workflow 规划失败、后端阻塞和答案提取失败，再决定是否更换模型或调整 DeepEye 工作流约束。
