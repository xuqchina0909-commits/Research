# DeepEye 根因修复后最小集复测报告

日期：2026-07-13

## 结论

本轮继续推进了 DeepEye 的根因修复，但仍不建议进入全量 KramaBench / DAComp。

原因不是链路完全不通，而是已经进入下一层质量问题：

- DAComp：SQL 特殊表名问题已解决，Python merge 错误也能进入自动修复，工作流最终可成功；但最终报告仍输出英文，且分析只覆盖部分数据，未满足“中文、定量、完整”的 DAComp 要求。
- KramaBench：文件上传和 workflow 执行已跑通；但最终没有按 `<Answer>...</Answer>` 输出，且答案只到 `13.16`，未达到正确答案 `13.1628` 的精度要求。

因此当前状态是：DeepEye 已从“最小集跑不通”推进到“最小集能跑到结果层，但输出格式/精度/报告质量不达标”。

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

## 最小集复测结果

| Benchmark | Task | 当前状态 | 说明 |
| --- | --- | --- | --- |
| DAComp-DA | `dacomp-zh-001` | failed | 工作流成功，但最终报告仍是英文，runner 判为 `final answer is not a Chinese report` |
| KramaBench | `legal-easy-3` | completed / incorrect | 工作流成功，但未输出 `<Answer>`，答案约为 `13.16`，不满足 gold `13.1628` |

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

## 是否进入全量

暂时不进入全量。

当前 DeepEye 已具备跑全量的技术条件，但全量会放大两个已知问题：

1. KramaBench 会产生大量“工作流执行了，但最终格式/精度不合格”的错误。
2. DAComp 会产生大量“工作流成功，但报告语言或分析质量不达标”的错误。

这类结果对横向对比价值有限，还会消耗较多 API 额度。

## 下一步建议

优先做 `v3-output-contract`：

- 对 KramaBench：在 runner 或 DeepEye 最终层增加强制 `<Answer>` 抽取/重写，或让 workflow 直接输出计算值而不是交给 `llm.answer` 自由发挥。
- 对数值题：在 answer 缺失时，从 workflow 输出中做结构化数值校验，避免只靠最终自然语言。
- 对 DAComp：在最终回复层增加中文输出后处理，必要时用同一模型再做一次“翻译为中文且不得改数值”的受控转换。

随后做 `v3-quality-guard`：

- 禁止 DAComp `python.code` 使用 `preview_rows` 做正式计算。
- 针对 `annual_rate_&_churn` 这类曲线表，加入任务级策略：按评级选择利率-流失率曲线上的推荐点，而不是取第一行 0.04 / 0.0。
- 增加报告质量检查：是否使用发票流水、是否使用上下游依赖、是否给出 1 亿元额度分配总和。
