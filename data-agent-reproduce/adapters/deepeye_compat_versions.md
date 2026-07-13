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

v2-schema-sql-guard：

- 在 DeepEye workflow SQL 节点执行前增加 schema-aware SQL sanitizer 或 validator。
- 对所有表名和列名统一生成安全引用形式，例如 SQLite 使用 `"table name"`。
- 对含空格、`&`、`-`、中文等特殊字符的表名增加回归用例。

v2-model-routing：

- 为 DeepEye workflow planning 配置更强的工具调用/长上下文模型。
- 保留三方 OpenAI-compatible 路线，但把模型、base URL、streaming、timeout 作为可记录的实验变量。
