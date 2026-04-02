# knowledge-agent

把检索、引用和短期记忆组合成可解释的知识问答服务。

## 这个综合服务在模块里的位置
它不是一个额外 demo，而是这个模块知识点的收束点。你应该在跑完 examples 之后再来看它，这样你能看出哪些抽象是从 examples 提升而来的。

## 建议阅读顺序
- 先看 [app/service.py](./app/service.py)：先看 `DOCS`、`Memory`、`retrieve()` 与 `ask()`。你要看到知识、记忆和响应模型是如何被分开的。
- 先看 [app/main.py](./app/main.py)：再看 `/ask` 路由如何只承担 HTTP 入口职责。
- 先看 [tests/test_main.py](./tests/test_main.py)：最后看测试如何确认响应里必须包含 citation。

## 建议运行命令
- `uvicorn app.main:app --reload`
- `pytest`

## 学完后你应该能回答
- 这个服务如何把 `03 RAG、Memory 与 Knowledge` 的核心概念组合到一起。
- 为什么这些能力要按当前这种分层组织。
- 如果继续扩展，这个服务最先该从哪里演进。
