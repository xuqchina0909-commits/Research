# DAComp 最小数据验证记录

日期：2026-07-10

## 本地状态

- DAComp 仓库已克隆到 `data-agent-reproduce/repos/DAComp`。
- 当前 DAComp commit：`027ccaf`。
- 仓库本体包含 DAComp-DA / DAComp-DE 代码、任务索引、evaluation suite 和 baseline agent。
- 真实任务数据需要从 HuggingFace 数据集仓库下载。

## 最小数据下载

本次只下载 DAComp-DA 的一个最小任务数据：

```text
DAComp/dacomp-da
└── dacomp-001/dacomp-001.sqlite
```

本地路径：

```text
data-agent-reproduce/repos/DAComp/dacomp-da/tasks/dacomp-001/dacomp-001.sqlite
```

数据文件大小：164,876,288 bytes，约 157 MB。

## 验证任务

任务 ID：`dacomp-001`

任务类型：开放式数据分析 / 企业信贷风险分析。

任务要求：基于银行收集的小微企业信用与经营数据，结合信用评级、营收能力、利润稳定性、上下游依赖和客户流失率，设计 1 亿元年度授信额度与利率分配方案。

## 数据结构

SQLite 中包含 7 张表：

| Table | Rows | Role |
| --- | ---: | --- |
| `ch___company_info` | 123 | 有信贷记录企业信息，含信用评级与违约标记 |
| `ch___input_invoices` | 210,947 | 有信贷记录企业进项发票 |
| `ch___sales_invoices` | 162,484 | 有信贷记录企业销项发票 |
| `nch___company_info` | 302 | 无信贷记录企业信息 |
| `nch___input_invoices` | 395,175 | 无信贷记录企业进项发票 |
| `nch___sales_invoices` | 330,835 | 无信贷记录企业销项发票 |
| `annual_rate_&_churn` | 29 | 年化贷款利率与 A/B/C 信用评级客户流失率 |

## Probe 结果

新增脚本：

```text
data-agent-reproduce/adapters/dacomp_minimal_probe.py
```

输出文件：

```text
data-agent-reproduce/runs/dacomp/minimal_probe/dacomp-001.json
```

结果：

- 任务索引可读取。
- SQLite 文件可打开。
- 表结构可读取。
- 所有关键表非空。
- 可抽取样例行。

结论：DAComp-DA 的最小数据层已经验证通过，可以作为后续 DeepAnalyze / DeepEye 接入 DAComp 的首个样本任务。

## 尚未完成

- 未运行 DAComp 官方 `da-agent` baseline。
- 未运行 DAComp LLM judge。
- 未下载 DAComp-DE 数据。
- 未跑多任务评测。

下一步建议：先将 `dacomp-001` 转成 DeepAnalyze 可消费的输入，跑一个低成本真实数据分析样本；再决定是否运行 DAComp 自带三阶段 baseline。
