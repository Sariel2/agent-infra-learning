# 04 Workflow、Observability 与 Evals 关键资料重点与总结

## 1. LangGraph Overview
- 为什么值得读：帮助你把流程和状态显式建模。
- 重点看哪里：state、node、edge、conditional routing。
- 一句话总结：workflow 可以降低 agent 系统的不确定性。
- 读完你应该会：你能把项目画成状态图。
- 阅读说明：精读。

## 2. LangGraph Observability
- 为什么值得读：学习如何观察 graph run 过程。
- 重点看哪里：节点执行、状态变化。
- 一句话总结：过程可见是调试 agent 的基础。
- 读完你应该会：你能列出 trace 至少要包含哪些信息。
- 阅读说明：紧跟 Overview 阅读。

## 3. OpenAI Agents SDK Tracing
- 为什么值得读：从官方 runtime 视角理解 trace。
- 重点看哪里：trace id、span、metadata。
- 一句话总结：trace 是运行时治理资产。
- 读完你应该会：你能设计最小 trace schema。
- 阅读说明：重点关注概念。

## 4. OpenTelemetry Python
- 为什么值得读：理解 tracing 的通用概念。
- 重点看哪里：span、attribute、context。
- 一句话总结：trace 概念应该跨框架理解。
- 读完你应该会：你能理解埋点在记录什么。
- 阅读说明：概念性阅读。

## 5. FastAPI Background Tasks
- 为什么值得读：帮助你理解请求返回与后台任务的边界。
- 重点看哪里：后台任务、请求生命周期。
- 一句话总结：不是所有耗时操作都应该阻塞主请求。
- 读完你应该会：你能理解为什么 eval 常常适合后台执行。
- 阅读说明：选读。
