# llm-gateway

把结构化输出、provider 边界和 HTTP 服务拼成最小 LLM 网关。

## 这个综合服务的目标
- 把“模型调用”从路由层拆出来，形成稳定的 provider 边界。
- 用结构化 schema 固定输入输出，给后面 tool calling 和 workflow 打基础。
- 让你先学会“如何把模型接入做得可测试”，再去接真实模型。

## 开始前先回看
- 模块首页：[../README.md](../README.md)
- 学习地图：[../study-map.md](../study-map.md)
- 概念讲义：[../resources/01-concepts-and-principles.md](../resources/01-concepts-and-principles.md)
- 原理细节：[../resources/02-deep-dive.md](../resources/02-deep-dive.md)
- 代码导读：[../resources/03-code-reading-guide.md](../resources/03-code-reading-guide.md)
- 示例 1：[../examples/01-structured-output/app/main.py](../examples/01-structured-output/app/main.py)
- 示例 2：[../examples/02-provider-abstraction/app/main.py](../examples/02-provider-abstraction/app/main.py)

## 先理解这 3 个文件
- 核心逻辑：[app/service.py](./app/service.py)
  先看 `GenerateRequest`、`GenerateResponse`、`FakeProvider` 和 `generate()`，这是整个模块最重要的边界。
- HTTP 入口：[app/main.py](./app/main.py)
  看 `/generate` 为什么只接 payload，再把工作委托给 service。
- 最小验收：[tests/test_main.py](./tests/test_main.py)
  看测试如何固定“接口返回必须以稳定 schema 呈现”。

## 推荐实现顺序
1. 先读 [app/service.py](./app/service.py)，确认 request、response 和 provider 的职责边界。
2. 再读 [tests/test_main.py](./tests/test_main.py)，先理解“什么叫稳定输出”。
3. 最后读 [app/main.py](./app/main.py)，确认路由只是协议层。
4. 自己尝试新增一个输出字段，例如 `confidence`，观察哪些地方要一起改。

## 动手实现时每一步做什么
### Step 1：先固定输入输出契约
- 要改的文件：[app/service.py](./app/service.py)
- 要做的事：优先把 `GenerateRequest` 和 `GenerateResponse` 写稳定。
- 验收标准：输出结构至少包含 `answer`、`confidence`、`reasoning_summary`。

### Step 2：再封装 provider
- 要改的文件：[app/service.py](./app/service.py)
- 要做的事：让 `FakeProvider.generate()` 承担“模型生成”的职责，而不是让路由直接拼假数据。
- 验收标准：`generate()` 只负责调用 provider，不自己构造零散响应。

### Step 3：最后暴露接口与测试
- 要改的文件：[app/main.py](./app/main.py)
- 要改的文件：[tests/test_main.py](./tests/test_main.py)
- 要做的事：暴露 `/generate`，并用测试固定最小行为。
- 验收标准：POST `/generate` 后能稳定拿到结构化 JSON。

## 建议运行命令
- `uvicorn app.main:app --reload`
- `pytest`

## 常见退化点
- 路由直接接管模型调用，后面难以替换 provider。
- 响应结构松散，导致测试只好断言文本片段。
- 一开始就接真实模型，把外部波动和内部设计问题混在一起。

## 扩展时优先做什么
- 把 fake provider 换成真实 provider，但保留同样的接口契约。
- 增加超时、重试和统一错误模型。
- 为后续 tool calling 预留 `provider -> tool runtime` 的扩展点。

## 学完后你应该能回答
- 为什么 structured output 是 agent infra 的起点。
- 为什么 provider abstraction 先解决的是工程边界，而不是效果本身。
- 如果把真实模型接进来，哪些地方可以不改。
