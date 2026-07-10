# DeepAnalyze 三方模型兼容版本记录

## v1-external-compat

状态：已验证。

目标：在不改变 DeepAnalyze 原始协议的前提下，让 OpenAI-compatible 三方模型完成基础数据分析任务。

当前实现：

- 通过环境变量配置外部模型 API 地址、密钥和模型名。
- 将内部 `execute` 消息转换为标准 `user` 消息。
- 为外部模型增加明确的 `<Analyze>/<Code>/<Answer>` 输出提示。
- 为 CSV 文件提供本地小样本预览。
- 支持从 DeepAnalyze 标签、Markdown 代码块和常见普通代码文本中提取 Python。
- 无效代码自动重试，最多 2 次。
- 外部兼容模式跳过可选的 `matplotlib` 自动导入，避免阻塞纯数据计算。

验证任务：KramaBench Legal `legal-easy-3`。

验证结果：

- 成功读取 `2024_CSN_Number_of_Reports_by_Type.csv`。
- 成功执行 Python 代码。
- 经过一次代码修正后得到正确答案 `13.1628`。
- DeepAnalyze API、文件上传、代码执行和最终答案链路通过。

边界：该版本依赖提示词、代码提取和重试策略，不等同于官方 DeepAnalyze-8B 模型复现。

## v2-tool-calling（预留）

状态：未实现。

计划：将 DeepAnalyze 的标签协议改造成标准 OpenAI tool calling 或结构化 JSON 协议，统一工具调用、执行结果、错误恢复和最终答案提取。
