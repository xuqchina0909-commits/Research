# DeepEye / DeepPrep 基本验证记录

日期：2026-07-10

## DeepEye

本次目标不是启动完整 WebUI/Docker 栈，而是先验证 DeepEye 是否具备可本地运行的核心 workflow 能力。

本地状态：

- 源码已克隆到 `data-agent-reproduce/repos/DeepEye`。
- 官方完整启动路径依赖 Docker Compose、Postgres、Redis、MinIO、后端 API、Celery worker、runtime-control、frontend 和 nginx gateway。
- 当前系统 PATH 中缺少 Docker，因此完整服务栈未启动。
- 已创建独立 Python 3.12 虚拟环境：`data-agent-reproduce/.venvs/deepeye`。
- 已安装 `packages/core` 和 `packages/backend` 的 Python 依赖。

验证结果：

- `packages/core/tests`：13 passed。
- 轻量 backend workflow 测试：17 passed。
- workflow contract schema 可导出到 DeepEye 本地 checkout 的 `packages/contracts/workflow-artifact.schema.json`。
- 新增 adapter：`data-agent-reproduce/adapters/deepeye_runner.py`。
- adapter 输出：`data-agent-reproduce/runs/deepeye/workflow_smoke/result.json`。

adapter 验证内容：

- 构造 DeepEye 内置 accuracy workflow。
- 校验 DAG 无结构错误。
- 执行 `labels -> preds -> compare -> accuracy` 节点链。
- 每个节点的输入、输出、状态和错误字段均被保存。
- 最终结果为 `0.6`，表示 5 个布尔预测中 3 个匹配标签。

结论：

DeepEye 的 Python workflow engine 和后端 workflow 契约已经通过基本验证。完整 DeepEye 产品栈仍需要 Docker Compose 才能启动，因此暂时不能声称 WebUI、数据库连接、文件上传、沙箱执行、dashboard/report/video 产物链路已跑通。

## DeepPrep

本地 DeepAnalyze README 将 DeepPrep 描述为将 raw tables 转换为 analysis-ready data 的 data-preparation companion，并链接到 arXiv 论文。

本地检查结果：

- DeepAnalyze 仓库中没有发现独立可运行的 DeepPrep 模块。
- `DeepAnalyze/playground/DABStep-Research/dabstep_research.jsonl` 中存在多条 `type = "Data Preparation"` 的任务样本，可用于未来模拟 DeepPrep 类任务。
- 当前没有发现可直接安装、调用、评测的 DeepPrep SUT。

结论：

DeepPrep 暂不纳入完整横向评测。后续可以用 DABStep / KramaBench 中的数据清洗与转换类任务，作为 DeepPrep 机制的替代验证样本；如果 DeepPrep 完整代码发布，再升级为独立 SUT。

## DeepEye Docker 完整栈验证

日期：2026-07-11

本次目标是补齐此前缺失的 Docker 环境，启动 DeepEye 官方 Docker Compose 产品栈。

本地配置：

- Docker Desktop 已安装并可用。
- Docker Engine：29.6.1。
- Docker Compose：v5.2.0。
- Docker context：`desktop-linux`。
- DeepEye 本地 `.env` 已生成，复用 KramaBench `.env` 中的三方 OpenAI-compatible 模型配置。
- 本地访问端口：`http://localhost:8080`。

启动服务：

- `postgres`
- `redis`
- `minio`
- `runtime-control`
- `backend-migrate`
- `backend-api`
- `frontend`
- `gateway`

验证结果：

- `docker compose config --quiet`：通过。
- `postgres`：healthy。
- `minio`：healthy。
- `runtime-control`：healthy。
- `backend-api`：healthy。
- `backend-api` 容器内健康检查：通过。
- `runtime-control` 容器内健康检查：通过。
- `http://localhost:8080`：返回 HTTP 200。

修复记录：

- 首次启动时，`POSTGRES_PASSWORD` 为空导致 Postgres 初始化失败。
- 根因是本地随机密码变量未导出给 `.env` 写入步骤。
- 已重新写入非空本地密钥并强制重建容器配置，随后完整服务链启动成功。

结论：

DeepEye 已从“核心 workflow/backend 测试可跑”升级为“官方 Docker Compose 完整产品栈可启动、健康检查通过、Web 入口可访问”。下一步可以基于 Web/API 层验证文件上传、数据源连接、工作流执行，以及 KramaBench/DAComp 任务适配。
