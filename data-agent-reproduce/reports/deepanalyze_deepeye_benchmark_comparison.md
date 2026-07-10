# DeepAnalyze / DeepEye 多任务横向对比报告

日期：2026-07-10

## 1. 结论摘要

本轮按两个 benchmark 输入源进行横向验证：

- KramaBench Legal easy 5 任务。
- DAComp-DA `dacomp-001` 最小开放式分析任务。

被测系统：

- DeepAnalyze：使用 `v1-external-compat` 三方模型兼容路线，模型为硅基流动 `Qwen/Qwen3-Coder-30B-A3B-Instruct`。
- DeepEye：当前不安装 Docker，因此只能验证 Python workflow engine / backend contract，不能启动完整产品栈承接 benchmark 任务。

关键结论：

1. DeepAnalyze 可以真实读取文件、生成代码、执行代码并产出答案，但在多任务中稳定性和数据解析鲁棒性不足。
2. DeepAnalyze 在 KramaBench 5 个 Legal easy 任务中，2 个正确、2 个错误、1 个因外部模型流中断失败。
3. DeepAnalyze 在 DAComp-DA `dacomp-001` 上能读 SQLite 并产出中文报告，但分析覆盖不完整，未充分使用发票流水、上下游依赖和 churn 表。
4. DeepEye 的 workflow-centric 核心代码层验证通过，但无 Docker 条件下无法跑 WebUI、后端服务栈、沙箱执行、真实数据源接入和报告/dashboard/video 链路，因此不能纳入 benchmark 任务得分对比。
5. 当前公平横向结论是：DeepAnalyze 已进入“任务执行层”评测；DeepEye 暂停留在“工作流结构层”验证。

## 2. 运行环境与边界

### DeepAnalyze

已启动本地 DeepAnalyze API：

```text
http://127.0.0.1:8200
```

使用外部模型配置：

```text
OPENAI_BASE_URL=https://api.siliconflow.cn/v1
OPENAI_MODEL=Qwen/Qwen3-Coder-30B-A3B-Instruct
```

本轮新增 runner：

```text
data-agent-reproduce/adapters/deepanalyze_benchmark_runner.py
```

说明：

- KramaBench：上传任务声明的真实 CSV 文件，调用 DeepAnalyze API，抽取 `<Answer>` 并与 gold answer 比较。
- DAComp：上传 `dacomp-001.sqlite`，并额外上传自动生成的 SQLite schema/sample 摘要。
- 本轮 KramaBench 不是通过官方 `evaluate.py` 直接调用 DeepAnalyze，而是通过 adapter 对 gold answer 做对比。
- 本轮 DAComp 未运行官方 LLM judge。

### DeepEye

已验证：

- Python workflow engine。
- DAG / node / edge 结构校验。
- backend workflow contract / node / artifact tests。
- 最小 workflow adapter。

未启动：

- Docker Compose 服务栈。
- WebUI。
- Postgres / Redis / MinIO。
- backend-api / backend-worker / runtime-control。
- Docker-backed sandbox。
- 真实 CSV/SQLite 数据源接入。
- LLM workflow planning。
- report / dashboard / data video 产物链路。

因此 DeepEye 本轮不能执行 KramaBench/DAComp benchmark 任务。

## 3. KramaBench 结果

输入工作负载：

```text
data-agent-reproduce/repos/KramaBench/workload/legal-easy-5.json
```

输出目录：

```text
data-agent-reproduce/runs/comparisons/deepanalyze_krama_legal_easy5/kramabench
```

汇总 CSV：

```text
data-agent-reproduce/runs/comparisons/deepanalyze_krama_legal_easy5/kramabench/summary.csv
```

| Task | Expected | DeepAnalyze Answer | Result | Notes |
| --- | ---: | ---: | --- | --- |
| `legal-easy-3` | 13.1628 | 13.1628 | correct | 成功读取 CSV 并计算 2024/2001 identity theft ratio |
| `legal-easy-4` | 2111635 | 2111635 | correct | 多轮纠错后改用索引读取 CSV，最终正确 |
| `legal-easy-5` | 5435 | 5635 | wrong | 对 CSV 的金额汇总解析有误 |
| `legal-easy-9` | 2002 | 2012 | wrong | 对总报告数增长率计算/解析不符合 gold |
| `legal-easy-10` | [2010, 2011, 2012, 2013, 2014, 2019] | null | failed | 外部模型流式响应中断 |

KramaBench 本轮 DeepAnalyze 结果：

```text
completed: 4 / 5
correct: 2 / 5
failed: 1 / 5
accuracy: 40%
```

技术观察：

- DeepAnalyze 的“代码执行 + 错误反馈 + 继续修正”机制有效，`legal-easy-4` 就是典型例子。
- 对 CSV 前置标题、空行、脚注和带逗号金额的解析仍不稳定。
- 外部模型 API 流中断会导致任务失败，需要 runner 层和服务层都做更强的重试。
- `v1-external-compat` 已经能跑多任务，但离稳定 benchmark agent 还有差距。

## 4. DAComp 结果

输入任务：

```text
DAComp-DA dacomp-001
```

数据文件：

```text
data-agent-reproduce/repos/DAComp/dacomp-da/tasks/dacomp-001/dacomp-001.sqlite
```

输出目录：

```text
data-agent-reproduce/runs/comparisons/deepanalyze_dacomp001/dacomp-da/dacomp-001
```

结果：

- DeepAnalyze 成功上传 SQLite 和 schema summary。
- 成功执行 Python 代码。
- 生成了 `enterprise_risk_analysis.csv`。
- 输出了中文信贷风险分析报告。
- 官方 DAComp LLM judge 未运行。

主要问题：

- 模型起初假设数据库里有 `enterprises` 和 `credit_histories` 表，实际不存在。
- 经过执行报错后，模型能查看真实表结构并改用 `ch___company_info`。
- 最终报告主要依赖 `Credit Rating` 和 `Defaulted` 两列。
- 没有充分使用进项/销项发票流水来计算营收能力、利润稳定性或上下游依赖。
- 没有真正使用 `annual_rate_&_churn` 表做利率-流失率权衡。

结论：

DeepAnalyze 在 DAComp 开放式任务上完成了“可运行报告链路”，但报告质量不满足完整 DAComp 任务要求。后续需要更强的 schema grounding、SQL 探索策略和任务 checklist 驱动。

## 5. DeepEye 对比状态

DeepEye 本轮复跑结果：

```text
data-agent-reproduce/runs/comparisons/deepeye_core/workflow_smoke/result.json
```

结果：

- workflow engine status: success。
- 节点链：`labels -> preds -> compare -> accuracy`。
- 输出：`0.6`。

这证明 DeepEye 的 typed workflow / node execution 机制本地可运行，但不能证明它能完成 KramaBench 或 DAComp 任务。

DeepEye 要进入同台对比，至少需要下一步跑通：

1. Docker Compose。
2. 文件/数据库数据源接入。
3. LLM workflow planning。
4. sandbox code execution。
5. report/dashboard artifact 输出。
6. 可导出 workflow DAG 与节点执行日志。

## 6. 横向能力对比

| 能力 | DeepAnalyze | DeepEye |
| --- | --- | --- |
| KramaBench 任务执行 | 已跑 5 题，2 正确 / 2 错误 / 1 失败 | 未能执行 benchmark 任务 |
| DAComp 任务执行 | `dacomp-001` 跑通报告链路，但质量不足 | 未能执行 benchmark 任务 |
| 数据发现 | 能看到上传文件，CSV/SQLite 需要更强 schema grounding | 设计上支持 datasource，但未启动完整栈 |
| 代码生成与执行 | 已验证，多任务可执行 | 核心 engine 可执行 toy workflow，真实代码沙箱未跑 |
| 错误恢复 | 有效果，但不稳定 | 完整错误恢复链路未验证 |
| 中间状态可检查 | raw output、代码、执行结果可保存 | workflow node 输入输出可检查；真实任务未验证 |
| 报告生成 | 可生成 markdown/report，但内容质量不稳定 | 产品设计支持 report/dashboard/video；未验证 |
| 工作流可控性 | 当前更像线性 code interpreter loop | 强项设计是 DAG/workflow，但需要 Docker 栈验证 |
| 企业底座潜力 | 快速接入真实数据任务，短期可实验 | 架构更像企业 workflow 底座，但部署依赖重 |

## 7. 下一步建议

短期建议继续沿 DeepAnalyze 跑 benchmark，因为它已经能执行真实任务：

1. 修复 DeepAnalyze runner 的 provider 流中断重试。
2. 针对 KramaBench CSV 增加更强的结构探测提示和通用 CSV loader。
3. 对 `legal-easy-5`、`legal-easy-9`、`legal-easy-10` 做失败归因。
4. 对 DAComp 增加任务 checklist，让模型必须覆盖信用评级、营收能力、利润稳定性、上下游依赖、churn 表。

DeepEye 建议在安装 Docker 后再进入正式 benchmark：

1. 启动 Compose。
2. 用 `dacomp-001` 作为第一个真实数据源。
3. 观察 workflow DAG、AgentNode/ToolNode、SQL/Python 节点、validator/executor 行为。
4. 再决定是否与 DeepAnalyze 做完整横向评分。
