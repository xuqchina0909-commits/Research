# DeepEye 根因修复后最小集复测报告

日期：2026-07-13

## 结论

本轮继续推进了 DeepEye 的根因修复和输出收口，但仍不建议进入全量 KramaBench / DAComp。

原因不是链路完全不通，而是已经进入下一层质量问题：

- DAComp：SQL 特殊表名问题已解决，Python merge 错误也能进入自动修复，工作流最终可成功；通过二次收口后可以输出中文报告，但分析深度仍偏浅，对营收能力、盈利稳定性、上下游依赖和额度总额约束使用不足。
- KramaBench：文件上传和 workflow 执行已跑通；通过二次收口后可以输出 `<Answer>...</Answer>`，但 5 题闸门显示答案稳定性不足，数值题仍大量错误。

因此当前状态是：DeepEye 已从“最小集跑不通”推进到“最小集可收口”，但还没有达到“多任务稳定可全量测评”。

## 已完成修复

1. SQLite 特殊表名引用修复

- `sql.execute` 执行前读取 SQLite schema。
- 对包含符号/标点/空格的真实表名自动补双引号。
- 已验证 `annual_rate_&_churn` 不再触发 `near "&": syntax error`。

2. Python 错误自动修复

- pandas merge key 类型不一致错误现在会被归类为可修复。
- DeepEye 能在 DAComp 中从 `python.code` merge 失败进入 `update_workflow`，并重跑成功。

3. 外部模型请求边界

- 增加 `LLM_REQUEST_TIMEOUT_SECONDS=120`。
- 增加 `LLM_MAX_RETRIES=1`。
- 普通 DeepEye smoke test 可返回 `OK`。

4. KramaBench 上传超时

- runner 文件上传超时从 180 秒提高到 600 秒。
- KramaBench `legal-easy-3` 已越过 datasource 上传/同步阶段。

5. runner 判定修正

- “工作流规划已停止 / Workflow execution failed” 不再误记为 completed。
- DAComp 最终非中文报告会标记为 failed。

6. 输出契约收口

- KramaBench 首轮缺少 `<Answer>` 时，会追加一次最终答案收口请求。
- KramaBench 收口请求会带上从 workflow trace 抽取的结构化证据，不泄露 gold answer。
- DAComp 首轮报告中文占比过低时，会追加一次中文报告收口请求。
- KramaBench runner 增加列表题精确评分，避免 `list_exact` 任务漏判。

## 最小集复测结果

| Benchmark | Task | 当前状态 | 说明 |
| --- | --- | --- | --- |
| DAComp-DA | `dacomp-zh-001` | completed | 二次收口后输出中文报告；但报告主要基于评级和首行流失率，分析质量仍需增强 |
| KramaBench | `legal-easy-3` | completed / correct by tolerance | 二次收口后输出 `<Answer>13.1622</Answer>`；runner 容差判定通过，但未严格等于四位小数 gold `13.1628` |

## 多任务闸门结果

KramaBench `legal-easy-5` 5 题闸门结果：

| Task | Gold | DeepEye final answer | 判定 |
| --- | --- | --- | --- |
| `legal-easy-3` | `13.1628` | `0.0000` | incorrect |
| `legal-easy-4` | `2111635` | `1390952` | incorrect |
| `legal-easy-5` | `5435` | `5059` | incorrect |
| `legal-easy-9` | `2002` | `2003` | incorrect |
| `legal-easy-10` | `[2010, 2011, 2012, 2013, 2014, 2019]` | 数据不足说明文本 | incorrect / 待列表评分补丁重跑 |

结论：DeepEye 当前在 KramaBench 多任务上不稳定，不能进入全量；主要失败点不是接口链路，而是 workflow 修复失败、列名/多输入处理不稳定，以及 `llm.answer` 未正确消费 workflow 输出。

## v4 数据契约闸门复测

本轮继续做了 `v4-workflow-data-contract`：

- KramaBench prompt 增加 workflow 数据契约：CSV 题优先 `datasource.read -> python.code -> llm.answer`，多数据源必须先在 `python.code` 合并，最后传给 `llm.answer` 的应是紧凑结果数据集。
- runner 增加结构化答案抽取：如果 workflow 已产生短列表或单行数值结果，优先从派生 `dataset_ref` 中抽取候选答案，减少 `llm.answer` 自然语言错误。
- runner 增加失败防污染：workflow 明确失败时，不再进入 `<Answer>` 收口。
- DeepEye repair 分类新增 Python 数值清洗错误：`invalid literal for int/float`、`cannot convert float NaN to integer`、`object has no attribute replace` 等会进入可修复类型。

复测结果：

| Run | 结果 | 说明 |
| --- | --- | --- |
| `deepeye_benchmark_v4_multitask_krama5` | 1/5 correct | `legal-easy-9` 通过；其余任务真实标记为 failed，不再假 completed |
| `deepeye_benchmark_v4_repairable_cleaning_krama5` | 中止于第 2 题 | 第 1 题耗时 425 秒后仍 failed；为避免继续消耗 API 额度，中止批跑 |

新的判断：

- v4 改善了评测真实性：失败不再伪装成答案，列表题也能严格判分。
- v4 尚未让 DeepEye + 当前 `Qwen/Qwen3-Coder-30B-A3B-Instruct` 达到 KramaBench 多任务稳定运行。
- 当前瓶颈主要是模型生成的 `python.code` 对 CSV 表头行、空行、NaN 的处理不稳，且自动修复轮次很容易耗尽。

## 关键结果文件

DAComp 中文约束复测：

```text
data-agent-reproduce/runs/deepeye_benchmark_chinese_guard/dacomp-da/dacomp-da-zh/dacomp-zh-001/result.json
data-agent-reproduce/runs/deepeye_benchmark_chinese_guard/dacomp-da/dacomp-da-zh/summary.csv
```

KramaBench 上传超时修复后复测：

```text
data-agent-reproduce/runs/deepeye_benchmark_krama_upload600/kramabench/legal-easy-1/legal-easy-3/result.json
data-agent-reproduce/runs/deepeye_benchmark_krama_upload600/kramabench/legal-easy-1/summary.csv
```

v3 输出契约复测：

```text
data-agent-reproduce/runs/deepeye_benchmark_v3_evidence_contract_krama/kramabench/legal-easy-1/summary.csv
data-agent-reproduce/runs/deepeye_benchmark_v3_output_contract_dacomp/dacomp-da/dacomp-da-zh/summary.csv
data-agent-reproduce/runs/deepeye_benchmark_v3_multitask_krama5/kramabench/legal-easy-5/summary.csv
```

## 是否进入全量

暂时不进入全量。

当前 DeepEye 已具备跑全量的技术条件，但多任务闸门已经证明全量会放大两个已知问题：

1. KramaBench 会产生大量“工作流执行或收口了，但答案错误”的结果。
2. DAComp 会产生大量“工作流成功，但报告分析深度不达标”的结果。

这类结果对横向对比价值有限，还会消耗较多 API 额度。

## 下一步建议

优先做 `v5-model-or-workflow-strategy`：

- 路线 A：切换更强的代码/工具调用模型做 A/B，例如更强 Qwen Coder 或 DeepSeek Coder/R1 系列，先只跑 Krama `legal-easy-5` 闸门。
- 路线 B：继续改 DeepEye workflow 策略，在 CSV benchmark 任务中注入更固定的数据清洗模板，减少模型自由生成 Python 的空间。
- 路线 C：保留 DeepEye 原生结果，同时在 adapter 中增加“结构化执行结果抽取/校验”作为单独指标，不把它混同为原生 DeepEye 准确率。

随后做 `v3-quality-guard`：

- 禁止 DAComp `python.code` 使用 `preview_rows` 做正式计算。
- 针对 `annual_rate_&_churn` 这类曲线表，加入任务级策略：按评级选择利率-流失率曲线上的推荐点，而不是取第一行 0.04 / 0.0。
- 增加报告质量检查：是否使用发票流水、是否使用上下游依赖、是否给出 1 亿元额度分配总和。
