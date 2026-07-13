# DeepEye 最小集验证状态报告

日期：2026-07-13

## 结论

本轮没有进入全量 KramaBench / DAComp 测评。

原因是 DeepEye 的最小集还没有通过：KramaBench 最小任务没有稳定完成，DAComp 最小任务进入了工作流执行层但最终失败。现在直接跑全量会主要消耗 API 额度和本机时间，结果大概率是一批同类失败，不适合作为横向对比报告。

## 已打通能力

- DeepEye Docker 服务栈已启动。
- DeepEye API 链路已验证：登录/注册、创建 session、上传文件 datasource、创建 SQLite datasource、发起 chat、轮询消息。
- `backend-worker` 已启动，Celery worker 能消费任务。
- 普通模型问答 smoke test 已通过，提示“请只回答：OK”可返回 `OK`。
- 新增 benchmark runner：

```text
data-agent-reproduce/adapters/deepeye_benchmark_runner.py
```

- 新增三方模型兼容补丁记录：

```text
data-agent-reproduce/adapters/deepeye_compat_versions.md
data-agent-reproduce/adapters/patch_deepeye_external_model_compat.py
```

## 最小集结果

| Benchmark | Task | 状态 | 关键原因 |
| --- | --- | --- | --- |
| KramaBench | `legal-easy-3` | failed | DeepEye 已到模型调用路径，但在 workflow planning 阶段出现长时间等待或反复 `/chat/completions` 重试，当前硅基流动 Qwen 配置未稳定产出答案 |
| DAComp-DA | `dacomp-zh-001` | failed | workflow path 已跑通，但 SQL 节点对表 `annual_rate_&_churn` 未加双引号，SQLite 报 `near "&": syntax error`，自动修复次数耗尽 |

## 结果文件

KramaBench：

```text
data-agent-reproduce/runs/deepeye_benchmark_min/kramabench/legal-easy-1/legal-easy-3/result.json
data-agent-reproduce/runs/deepeye_benchmark_min/kramabench/legal-easy-1/summary.csv
```

DAComp：

```text
data-agent-reproduce/runs/deepeye_benchmark_min/dacomp-da/dacomp-da-zh/dacomp-zh-001/result.json
data-agent-reproduce/runs/deepeye_benchmark_min/dacomp-da/dacomp-da-zh/summary.csv
```

## 对“是否可以跑全量”的判断

暂时不建议跑全量。

全量前至少需要先完成两个根本修复：

1. SQL/schema grounding 修复：让 DeepEye 在生成 SQLite SQL 时稳定引用特殊表名和列名，尤其是 `annual_rate_&_churn` 这类包含特殊字符的表。
2. 模型稳定性修复：当前 `Qwen/Qwen3-Coder-30B-A3B-Instruct` 在 DeepEye workflow planning 上不够稳定，需要更强工具调用模型，或进一步调整 DeepEye prompt、timeout、retry 和非流式输出解析。

## 建议下一步

优先进入 `v2-schema-sql-guard`：

- 给 DeepEye workflow 的 SQL 执行节点加一层 schema-aware 检查。
- 将表名/列名统一安全引用。
- 用 DAComp `dacomp-zh-001` 作为回归任务，直到能产出完整中文分析报告。

随后再处理 KramaBench：

- 先用同一最小任务 `legal-easy-3` 验证 workflow planning 是否能稳定完成。
- 如果仍卡在模型规划阶段，再切换更强的三方模型做 A/B。

只有当这两个最小任务都能完成后，再进入全量集更稳妥。
