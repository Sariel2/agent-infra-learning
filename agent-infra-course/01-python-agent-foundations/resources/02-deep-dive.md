# 01 Python 与 Agent 基础 细节深挖

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：01-concepts-and-principles.md](./01-concepts-and-principles.md) | [下一篇：03-code-reading-guide.md](./03-code-reading-guide.md)

## 1. 从请求到响应的完整数据流
这一模块的最小链路是：
1. HTTP 请求进入 route
2. route 解析为 `GenerateRequest`
3. service 调用 provider
4. provider 返回 `GenerateResponse`
5. route 再把响应序列化返回

这个链路看起来普通，但它定义了后面所有模块的基准结构。到了 tool calling、RAG、workflow 阶段，你依然会复用同样的“入口 -> 业务 -> 适配层 -> 输出契约”模式。

## 2. 为什么 route 不应该直接调用模型
如果 route 里直接写模型调用，你很快会遇到这些问题：
- 测试需要真实外部依赖
- 模型切换会影响 HTTP 层
- 超时和重试逻辑散落在多个接口里
- 业务逻辑无法被独立复用

所以 route 最适合做的是“协议边界”，而不是“业务执行边界”。

## 3. 为什么测试从 schema 和最小行为开始
新手很容易一开始就追求端到端大测试。但在 agent infra 里，真正经常变的是 schema、provider 和执行链路。如果这些最小单元没有被测试保护住，后面每次改动都会变成猜测。

## 4. 这一模块和后面模块的关系
- 没有结构化输出，就很难可靠做 tool result
- 没有 provider 层，就很难管理真实模型接入
- 没有统一 service 层，就很难把 workflow 和 eval 接进来
