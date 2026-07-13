# DeepEye 兼容路线版本记录

日期：2026-07-13

## v1-docker-stack

目标：让 DeepEye 完整 Docker Compose 栈在本机可启动，并接入 benchmark runner。

已完成：

- Docker Desktop 已安装并可运行。
- DeepEye 前端、后端 API、Postgres、Redis、MinIO、runtime-control 等服务已启动。
- `backend-worker` 首次构建因依赖下载超时失败，临时复用 backend API 镜像启动 worker。
- 通过 HTTP API 打通 auth、session、datasource、chat、messages 链路。

风险：

- `backend-worker` 镜像复用是本地验证手段，不是正式生产构建方式。
- 如需长期稳定评测，应在网络稳定时重新构建 worker 镜像。

## v1-external-model-compat

目标：兼容硅基流动 OpenAI-compatible API 和 `Qwen/Qwen3-Coder-30B-A3B-Instruct`。

已完成：

- 新增 `DEEPEYE_LLM_STREAMING=false`，绕开外部模型流式响应超时问题。
- DeepEye 后端 agent task 支持从环境变量控制 LangChain streaming。
- DeepEye 非流式模式下，如果 callback collector 没有收到 token，会从 `supervisor.ainvoke()` 返回值提取最后一条 assistant 内容并持久化。
- 新增 `DOCKER_CONTROL_TIMEOUT_SECONDS=600`，降低 runtime-control 首次构建或长执行时的控制超时概率。
- 新增可复用补丁脚本：`data-agent-reproduce/adapters/patch_deepeye_external_model_compat.py`。

当前仍未解决：

- KramaBench 最小任务在 DeepEye workflow planning 阶段会长时间等待或反复模型重试，当前模型/服务组合无法稳定完成。
- DAComp 最小任务能进入 workflow 执行，但模型生成 SQL 时没有给 `annual_rate_&_churn` 这类特殊表名加双引号，触发 SQLite syntax error，并在自动修复次数耗尽后失败。

## 下一版本建议

## v2-schema-sql-guard

目标：从执行层根治 DAComp 中特殊表名导致的 SQL 失败。

已完成：

- `sql.execute` 在 SQLite 数据源执行前读取真实表名。
- 对 schema 中包含空格、符号、标点或非普通标识符的表名，自动把 SQL 中未引用的真实表名替换为 SQLite 双引号引用。
- workflow prompt 增加规则：表名/列名包含特殊字符时必须引用，例如 `FROM "annual_rate_&_churn"`。
- 补丁脚本已纳入该修复。

适用边界：

- 当前只自动修复 SQLite 表名，不修改普通表名，不处理任意 SQL 重写。
- 这个修复覆盖 DAComp `annual_rate_&_churn` 失败点，但不保证模型后续 Python join/分析逻辑一定正确。

## 后续建议

v2-schema-sql-guard-plus：

- 在 DeepEye workflow SQL 节点执行前增加 schema-aware SQL sanitizer 或 validator。
- 对所有表名和列名统一生成安全引用形式，而不只是特殊表名兜底。
- 对含空格、`&`、`-`、中文等特殊字符的表名增加回归用例。

v2-model-routing：

- 为 DeepEye workflow planning 配置更强的工具调用/长上下文模型。
- 保留三方 OpenAI-compatible 路线，但把模型、base URL、streaming、timeout 作为可记录的实验变量。

## v2-model-timeout-boundary

目标：避免外部 OpenAI-compatible 模型长时间悬挂导致 benchmark runner 等待几十分钟。

已完成：

- DeepEye agent 使用 `LLM_REQUEST_TIMEOUT_SECONDS` 控制 ChatOpenAI 请求超时。
- DeepEye agent 使用 `LLM_MAX_RETRIES` 控制 ChatOpenAI 最大重试次数。
- 本地默认记录为 `LLM_REQUEST_TIMEOUT_SECONDS=120`、`LLM_MAX_RETRIES=1`。

当前判断：

- 这不是提升答案质量的修复，而是让失败变得可控、可统计。
- 当前硅基流动 `Qwen/Qwen3-Coder-30B-A3B-Instruct` 在 DeepEye supervisor/workflow planning 上仍可能不稳定。后续如果最小集仍超时，应切换更强工具调用模型做 A/B。

## v2-python-repair-guard

目标：让常见 `python.code` schema/merge 运行错误进入 DeepEye 自动修复，而不是直接终止。

已完成：

- 将 pandas merge key 类型不一致错误，例如 `You are trying to merge on str and int64 columns`，归类为 `workflow_python_schema_invalid`。
- repair issues 增加约束：计算必须使用 `load_dataset_ref(ref)` / `load_dataset_refs(data)` 读取完整上游数据，不能只基于 `dataset_ref.preview_rows`。
- repair issues 增加约束：pandas merge 前必须确认 join key 表示同一实体且 dtype 兼容；如果上游表是曲线/矩阵，应改用映射或规则计算，不要按行索引合并。

复测结论：

- DAComp `dacomp-zh-001` 已能从初始 Python merge 失败进入 `update_workflow` + `run_workflow` 修复循环，并最终得到 workflow success。
- 但最终报告仍被当前模型输出为英文，且分析质量不足，因此 benchmark runner 已按“不是中文报告”标记为 failed。

## v2-upload-timeout

目标：避免 KramaBench 小 CSV 上传/同步 sandbox 时因 runner 180 秒读超时而误判。

已完成：

- DeepEye benchmark runner 将 file datasource upload timeout 从 180 秒提高到 600 秒。

复测结论：

- KramaBench `legal-easy-3` 已越过 datasource 上传和 workflow 执行，能成功生成工作流并得到回答。
- 但最终回答未按 `<Answer>...</Answer>` 输出，且只给出约 `13.16`，未达到 gold `13.1628` 的 4 位小数精度，因此仍判为 incorrect。
