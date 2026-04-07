# 01 Python 与 Agent 基础 逐步执行说明

这一页是本模块的真正学习剧本。你不需要再自己决定“先看概念还是先跑代码”，按这里的顺序推进就可以。

## 使用方式
- 每一步都按 `讲义 -> 导读 -> example -> module-service -> 复盘` 的顺序走。
- 这模块不要急着接真实模型，重点是先把结构搭对。
- 如果你开始觉得“这些代码好像太简单”，先停一下，回到对应讲义看它在收哪一层复杂度。

## Step 1：先把服务骨架认知立住
- 先读 [study-map.md](./study-map.md)
- 再读 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 再读 [resources/05-common-mistakes.md](./resources/05-common-mistakes.md)
- 这一步要解决什么：
  - 为什么本模块不是 Python 语法课
  - 为什么结构化输出是第一块地基
  - 为什么 route / service / provider 需要分层
- 完成标准：
  - 你能不用看代码先讲清 `schema / provider / service` 分别干什么
- 如果卡住：
  - 回到 [mindmap.md](./mindmap.md)
  - 再回到 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)

## Step 2：把数据流和失败点看清楚
- 读 [resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 再读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 的总说明部分
- 最后扫一遍 [resources/04-sources.md](./resources/04-sources.md) 中关于 `FastAPI`、`Pydantic Settings`、`Responses API` 的解释
- 这一步要解决什么：
  - 从请求到响应的完整链路是什么
  - 为什么 route 不能直接调模型
  - 为什么 fake provider 会成为后面长期复用的训练手段
- 完成标准：
  - 你能说清 `request -> route -> service -> provider -> response` 这条链
- 如果卡住：
  - 回到 [resources/02-deep-dive.md](./resources/02-deep-dive.md)
  - 再看 [resources/04-sources.md](./resources/04-sources.md) 对官方来源的拆解

## Step 3：先跑结构化输出 example
- 先读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 中 `01-structured-output` 这一节
- 再读 [examples/01-structured-output/README.md](./examples/01-structured-output/README.md)
- 再读 [examples/01-structured-output/walkthrough.md](./examples/01-structured-output/walkthrough.md)
- 然后打开 [examples/01-structured-output/app/main.py](./examples/01-structured-output/app/main.py)
- 最后看 [examples/01-structured-output/tests/test_main.py](./examples/01-structured-output/tests/test_main.py)
- 建议命令：
  - `python -m app.main`
  - `pytest`
- 这一步要重点看什么：
  - `StructuredAnswer`
  - `generate_structured_answer()`
  - 为什么这里先用 deterministic stub
- 建议动手改一次：
  - 给 `StructuredAnswer` 新增字段，比如 `category`
  - 补实现和测试
- 完成标准：
  - 你能解释为什么结构化输出会直接影响测试策略
- 如果卡住：
  - 回到 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)
  - 再回到 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)

## Step 4：再跑 provider abstraction example
- 先读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 中 `02-provider-abstraction` 这一节
- 再读 [examples/02-provider-abstraction/README.md](./examples/02-provider-abstraction/README.md)
- 再读 [examples/02-provider-abstraction/walkthrough.md](./examples/02-provider-abstraction/walkthrough.md)
- 然后打开 [examples/02-provider-abstraction/app/main.py](./examples/02-provider-abstraction/app/main.py)
- 最后看 [examples/02-provider-abstraction/tests/test_main.py](./examples/02-provider-abstraction/tests/test_main.py)
- 建议命令：
  - `python -m app.main`
  - `pytest`
- 这一步要重点看什么：
  - `Provider`
  - `EchoProvider`
  - `FakeLLMProvider`
  - 业务函数如何不依赖具体实现
- 建议动手改一次：
  - 新增 `UppercaseProvider`
  - 不改业务函数，只改 provider 和测试
- 完成标准：
  - 你能解释为什么 provider 的本质是隔离变化，而不是“包一层”
- 如果卡住：
  - 回到 [resources/02-deep-dive.md](./resources/02-deep-dive.md)
  - 再看 [resources/04-sources.md](./resources/04-sources.md) 里对 `HTTPX` 和 `Responses API` 的解释

## Step 5：进入综合服务 `llm-gateway`
- 先读 [module-service/README.md](./module-service/README.md)
- 再读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 中 `llm-gateway` 这一节
- 然后打开 [module-service/app/service.py](./module-service/app/service.py)
- 再看 [module-service/app/main.py](./module-service/app/main.py)
- 最后看 [module-service/tests/test_main.py](./module-service/tests/test_main.py)
- 建议命令：
  - `uvicorn app.main:app --reload`
  - `pytest`
- 这一步要重点看什么：
  - `GenerateRequest`
  - `GenerateResponse`
  - `FakeProvider.generate()`
  - `generate(payload)`
- 完成标准：
  - 你能解释这个服务如何把 `schema + provider + HTTP 边界` 组合成最小 LLM gateway
- 如果卡住：
  - 回到 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)
  - 再回到 [project.md](./project.md)

## Step 6：把讲义、代码和出处对齐一次
- 读 [resources/04-sources.md](./resources/04-sources.md)
- 推荐顺序：
  - `FastAPI Tutorial`
  - `Pydantic Settings`
  - `OpenAI Responses API`
  - `pytest`
  - `HTTPX`
- 这一步要解决什么：
  - 把你的代码观察，重新接回外部出处
  - 确认你理解的是“为什么这样设计”，而不是“我照着写了”
- 完成标准：
  - 你能说出至少 3 条“代码结构”和“出处原理”的映射关系
- 如果卡住：
  - 回到 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)

## Step 7：收束练习和模块交接
- 做 [exercises.md](./exercises.md)
- 用 [review.md](./review.md) 复盘
- 再看 [project.md](./project.md)，确认自己是否已经具备进入 tools 模块的骨架
- 最少写下这 4 件事：
  - 1 条关于 schema 的判断
  - 1 条关于 provider 的判断
  - 1 条你在读码时发现的边界设计
  - 1 条你准备带到第 02 模块继续使用的习惯
- 完成标准：
  - 你已经不再把模型调用看成“随手调个 API”，而是看成可维护服务骨架

## 本模块结束时你应该具备什么
- 你能解释 route / service / provider 的分工
- 你知道为什么 fake provider 是合理起点
- 你能读懂一个最小 Python agent service 的数据流
