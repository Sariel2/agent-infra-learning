# 01 Python 与 Agent 基础 模块综合项目说明

## 项目名
`llm-gateway`

## 项目定位
这是整门课第一个真正的“最小 agent 服务骨架”。它不是要做复杂 agent，而是要把模型调用、结构化输出、provider 抽象、服务分层和测试习惯组合成一个能继续长大的基础服务。

## 对应综合服务
- 服务入口：[module-service/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/01-python-agent-foundations/module-service/app/main.py)
- 服务逻辑：[module-service/app/service.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/01-python-agent-foundations/module-service/app/service.py)
- 测试入口：[module-service/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/01-python-agent-foundations/module-service/tests/test_main.py)

## 项目目标
做一个最小 LLM gateway，接收请求，返回结构化 JSON，并且具备：
- 清晰的输入输出 schema
- 可替换的 provider
- 干净的 route / service 边界
- 最小测试保护

## 你最终应该学到什么
- 为什么结构化输出是第一块地基
- 为什么 provider 的本质是隔离变化
- 为什么 route 不能直接调模型
- 为什么 fake provider 是可靠起点

## 必做项
- 提供 `/health`
- 提供 `/generate`
- 使用 `Pydantic` 表达请求和响应
- 保留稳定响应字段，例如 `answer`、`confidence`、`reasoning_summary`
- 把模型能力封装在 provider 层
- 保留最小错误处理和测试

## 推荐实现顺序
1. 先跑 `examples/01-structured-output`
2. 再跑 `examples/02-provider-abstraction`
3. 再读 [resources/03-code-reading-guide.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/01-python-agent-foundations/resources/03-code-reading-guide.md)
4. 再回到 `llm-gateway` 综合服务
5. 最后做 [review.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/01-python-agent-foundations/review.md)

## 实现清单
- `GenerateRequest` 和 `GenerateResponse` 已定义
- `FakeProvider` 已承担最小模型能力
- `generate(payload)` 已承担 service 层职责
- HTTP 层只做请求接收和响应返回
- 测试至少保护 schema 和主要行为

## 验收清单
- 我能启动服务并调用 `/generate`
- 我能解释 `GenerateRequest` 和 `GenerateResponse` 的边界
- 我能切换 provider 而不改 route
- 我能新增一个响应字段并同步修改测试
- 我能说清这个项目为什么是后面 tools、RAG、workflow 的基础

## 常见退化点
- route 里塞进模型调用和业务逻辑
- provider 名义存在，但 service 仍依赖具体实现
- 响应是 JSON 但没有稳定 schema
- 测试只验证 happy path

## 加分项
- 增加请求 ID
- 增加超时配置
- 增加 1 个新的 provider 变体
- 让 provider 可通过配置切换

## 交付物
- 一个可启动的最小 LLM gateway
- 一组能保护骨架的测试
- 一份你自己总结的 route / service / provider 分工说明

## 进入下一模块前，你应该能回答
- 为什么 schema 比文案更重要
- 为什么 provider 会成为后面长期复用的一层
- 为什么单 agent 的很多能力都会长在这个骨架上
