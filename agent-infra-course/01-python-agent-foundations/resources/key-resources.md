# 01 Python 与 Agent 基础 关键资料重点与总结

## 1. FastAPI Tutorial
- 为什么值得读：决定后续所有服务的 API 骨架。
- 重点看哪里：routing、dependency injection、testing。
- 一句话总结：服务边界越清晰，后面的 provider 和 tool 接入越轻松。
- 读完你应该会：你能写出最小 API 服务。
- 阅读说明：优先读 tutorial，不必先啃高级主题。

## 2. Pydantic Settings
- 为什么值得读：配置治理是模型工程的底座。
- 重点看哪里：BaseSettings、env_file、嵌套配置。
- 一句话总结：越早收拢配置，越少后期混乱。
- 读完你应该会：你能做统一配置入口。
- 阅读说明：可配合 examples 中的 settings 示例理解。

## 3. OpenAI Responses API
- 为什么值得读：帮助你理解模型调用与结构化输出。
- 重点看哪里：response schema、structured outputs。
- 一句话总结：结构化响应是系统集成的前提。
- 读完你应该会：你能设计 provider 输入输出接口。
- 阅读说明：先抓接口形状，不纠结每个高级参数。

## 4. pytest
- 为什么值得读：所有示例和服务都附带测试。
- 重点看哪里：fixture、断言、参数化。
- 一句话总结：测试是你敢重构 provider 的前提。
- 读完你应该会：你能为 schema、service 和 route 写最小测试。
- 阅读说明：先掌握最小 happy path 与边界测试。

## 5. httpx
- 为什么值得读：理解异步 HTTP 调用模型。
- 重点看哪里：Client、AsyncClient、timeout。
- 一句话总结：很多模型调用和内部服务调用都依赖统一 HTTP 心智模型。
- 读完你应该会：你能理解 provider 为什么常用 http client 封装。
- 阅读说明：选读即可。
