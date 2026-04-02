# llm-gateway

把结构化输出、provider 和 HTTP 服务边界组合成最小 LLM 网关。

## 这个综合服务在模块里的位置
它不是一个额外 demo，而是这个模块知识点的收束点。你应该在跑完 examples 之后再来看它，这样你能看出哪些抽象是从 examples 提升而来的。

## 建议阅读顺序
- 先看 [app/service.py](./app/service.py)：先看 `GenerateRequest` 与 `GenerateResponse`，它们定义了系统输入输出契约。再看 `FakeProvider` 和 `generate()`，理解 route 不应该直接管模型。
- 先看 [app/main.py](./app/main.py)：再看 HTTP 层如何只做协议转换，而不承担业务逻辑。
- 先看 [tests/test_main.py](./tests/test_main.py)：最后看测试，确认接口契约已经被稳定验证。

## 建议运行命令
- `uvicorn app.main:app --reload`
- `pytest`

## 学完后你应该能回答
- 这个服务如何把 `01 Python 与 Agent 基础` 的核心概念组合到一起。
- 为什么这些能力要按当前这种分层组织。
- 如果继续扩展，这个服务最先该从哪里演进。
