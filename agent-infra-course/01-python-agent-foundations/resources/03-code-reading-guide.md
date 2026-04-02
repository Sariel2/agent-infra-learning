# 01 Python 与 Agent 基础 代码导读

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：02-deep-dive.md](./02-deep-dive.md) | [下一篇：04-sources.md](./04-sources.md)

## 学习总原则
- 先看讲义，再看代码。
- 先看对象模型和函数签名，再看具体执行逻辑。
- 先跑测试，再改代码，再重新验证。

## Examples 阅读顺序
### 01-structured-output：结构化输出
- 这一例子主要解决：模型输出为什么必须尽量变成稳定 schema。
- 先看 [`01-structured-output/app/main.py`](../examples/01-structured-output/app/main.py)：先看 `StructuredAnswer`，它不是装饰，而是系统契约。再看 `generate_structured_answer`，理解课程为什么先用 deterministic stub。
- 先看 [`01-structured-output/tests/test_main.py`](../examples/01-structured-output/tests/test_main.py)：看测试如何验证输出形状，而不是只验证一段自由文本。
- 建议运行命令：
  - `python -m app.main`
  - `pytest`
- 建议动手实验：
  - 给 `StructuredAnswer` 新增字段，再修复实现和测试。
  - 把 `confidence` 改成非法值，观察验证失败。

### 02-provider-abstraction：Provider 抽象
- 这一例子主要解决：为什么模型调用必须与业务逻辑解耦。
- 先看 [`02-provider-abstraction/app/main.py`](../examples/02-provider-abstraction/app/main.py)：先看 `Provider` 协议，再看 `EchoProvider` 与 `FakeLLMProvider`，理解“同一接口，不同实现”的工程价值。
- 先看 [`02-provider-abstraction/tests/test_main.py`](../examples/02-provider-abstraction/tests/test_main.py)：看同一业务函数如何在不同 provider 上被稳定测试。
- 建议运行命令：
  - `python -m app.main`
  - `pytest`
- 建议动手实验：
  - 新增一个 `UppercaseProvider`，不改业务函数，只扩展实现。

## module-service 阅读顺序
### llm-gateway
- 这个综合服务的目的：把结构化输出、provider 和 HTTP 服务边界组合成最小 LLM 网关。
- 先看 [`module-service/app/service.py`](../module-service/app/service.py)：先看 `GenerateRequest` 与 `GenerateResponse`，它们定义了系统输入输出契约。再看 `FakeProvider` 和 `generate()`，理解 route 不应该直接管模型。
- 先看 [`module-service/app/main.py`](../module-service/app/main.py)：再看 HTTP 层如何只做协议转换，而不承担业务逻辑。
- 先看 [`module-service/tests/test_main.py`](../module-service/tests/test_main.py)：最后看测试，确认接口契约已经被稳定验证。
- 建议运行命令：
  - `uvicorn app.main:app --reload`
  - `pytest`
