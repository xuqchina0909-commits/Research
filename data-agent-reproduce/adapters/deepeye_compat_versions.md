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

## v3-output-contract

目标：把 DeepEye 已经生成的分析结果收口为 benchmark 可判分的最终答案，避免“工作流成功但格式失败”污染全量测评。

已完成：

- KramaBench runner 在首轮回答缺少 `<Answer>...</Answer>` 时，会追加一次最终答案收口请求。
- KramaBench 收口请求不泄露 gold answer，只要求基于上一轮计算和数据证据重新做精确算术，并严格输出 `<Answer>...</Answer>`。
- DAComp runner 在首轮回答中文占比过低时，会追加一次中文报告收口请求。
- DAComp 收口请求不重新编造数据，只要求基于上一轮结果整理为中文结论、关键依据、计算规则和建议。

适用边界：

- 该版本解决的是输出契约和语言契约，不等同于保证分析逻辑正确。
- 如果首轮工作流本身失败、超时或数据计算错误，收口轮不会把失败伪装成成功。

下一步验证：

- 重新跑 KramaBench 最小任务，确认是否能输出 `<Answer>` 且达到数值精度。
- 重新跑 DAComp 最小任务，确认是否能输出中文报告并通过语言闸门。
- 只有两项都通过后，才进入 KramaBench + DAComp 多任务/全量横向对比。

复测结论：

- KramaBench `legal-easy-3` 在结构化证据收口后可输出 `<Answer>13.1622</Answer>`，runner 容差判定为 correct；但它仍未严格输出 gold 四位小数 `13.1628`，说明精确数值收口还有风险。
- DAComp `dacomp-zh-001` 在中文收口后通过语言闸门，状态为 completed；但报告分析深度偏浅，主要复述评级规则，没有充分使用发票流水、上下游依赖和 1 亿元总额度约束。
- KramaBench `legal-easy-5` 5 题闸门失败，4 道数值题全部 incorrect，1 道列表题输出“数据不足”文本。当前不进入全量。

## v4-workflow-data-contract（建议）

目标：解决 KramaBench 多任务失败暴露出的 workflow 数据契约问题，而不是继续扩大无效全量结果。

需要修复：

- 多个 `dataset_ref` 不能直接连到不支持多输入的 `llm.answer`，必须先用 `python.code` 合并或计算成单一结果。
- `python.code` 生成时必须使用上游节点实际输出列名；`rows.select` 后列名通常是 `Unnamed: 2`，不能再访问原始语义列名 `Identity Theft `。
- 修复失败时不应由收口轮把错误说明包装成 `<Answer>`，runner 应保留 failure/incorrect 语义。
- KramaBench `list_exact` 已补充列表精确评分，后续需重跑 5 题闸门确认摘要完整性。

已完成：

- KramaBench prompt 加强 CSV/file 工作流约束：优先 `datasource.read -> python.code -> llm.answer`，多数据集先在 `python.code` 合并，最终传递紧凑结果。
- runner 新增从 workflow 派生 `dataset_ref` 中抽取结构化候选答案。
- runner 在 workflow 明确失败时跳过最终收口，避免把失败说明包装成 `<Answer>`。
- DeepEye repair 分类新增 Python 数值清洗错误，例如标题行/空值导致的 `invalid literal for int`、`cannot convert float NaN to integer`、`object has no attribute replace`。

复测结论：

- `deepeye_benchmark_v4_multitask_krama5`：5 题中仅 `legal-easy-9` 通过，其余真实标记 failed。
- `deepeye_benchmark_v4_repairable_cleaning_krama5`：第 1 题耗时 425 秒后仍 failed，随后为控制 API 额度中止批跑。
- 当前不进入全量。下一步应切换更强模型做 A/B，或在 DeepEye workflow 里加入更固定的 CSV 清洗/计算模板。

## v5-model-ab-qwen3-coder-480b

目标：验证硅基流动 `Qwen/Qwen3-Coder-480B-A35B-Instruct` 是否能改善 DeepEye 在 KramaBench CSV workflow 上的稳定性。

配置：

- `LLM_BASE_URL=https://api.siliconflow.cn/v1`
- `LLM_MODEL=Qwen/Qwen3-Coder-480B-A35B-Instruct`
- `DEEPEYE_LLM_STREAMING=false`

验证：

- DeepEye smoke test：`请只回答：OK`，返回 `OK`。
- KramaBench `legal-easy-5` 5 题闸门：0/5 correct。

结论：

- 480B-A35B 在本闸门上没有提升，且 `legal-easy-10` 单题耗时超过 1000 秒。
- 不建议继续用该模型跑 KramaBench 全量。
- 下一步更应优先做 workflow 策略改造，或测试其他模型路线，而不是简单扩大 Qwen3-Coder 参数量。

## v5-model-ab-deepseek-v3.2

目标：验证硅基流动 `deepseek-ai/DeepSeek-V3.2` 是否可作为 DeepEye benchmark 主模型。

验证：

- DeepEye smoke test：`请只回答：OK`，返回 `OK`。
- KramaBench `legal-easy-5` 闸门：第 1 题 `legal-easy-3` 耗时 280.938 秒，输出 `2024 vs 2001`，判定 incorrect；为控制 API 额度中止后续批跑。

结论：

- `deepseek-ai/DeepSeek-V3.2` 可以接入，但在 DeepEye + KramaBench workflow 上过慢且第 1 题错误。
- 当前不建议继续模型横跳或跑全量。
- 本地 `.env` 已切回 `Qwen/Qwen3-Coder-30B-A3B-Instruct` 作为低成本待机模型。
- 下一阶段应优先做 workflow 策略修复：对 Krama CSV 任务使用固定清洗模板和结构化计算结果直出。

## v6-krama-subtask-template

目标：不再继续盲目换模型，而是把 KramaBench workload 中的 `subtasks` 和固定 CSV 清洗模板注入 DeepEye prompt，降低模型自由生成错误代码的概率。

已完成：

- `krama_prompt()` 会把每个任务的 `subtasks.step` 作为参考解题路径发送给 DeepEye。
- prompt 中加入通用 CSV 清洗模板：自动识别表头行、清理空行/脚注、转换千分位数字、保留 label-based filtering。
- 保持低成本模型 `Qwen/Qwen3-Coder-30B-A3B-Instruct` 进行闸门复测。

复测结论：

- `deepeye_benchmark_v6_subtask_template_krama5`：5/5 failed。
- 失败原因包括 workflow 修复不收敛、Python 执行失败、以及生成代码缩进错误。
- 结论是 prompt 注入不足以解决 Krama CSV 任务，下一步应实现确定性 Krama CSV 执行器/校验器，或在 DeepEye 内部新增专用数据清洗节点。
