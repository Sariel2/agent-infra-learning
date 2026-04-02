# agent-runtime

把 workflow、trace 和 eval 统一进同一个运行时服务。

## 这个综合服务在模块里的位置
它不是一个额外 demo，而是这个模块知识点的收束点。你应该在跑完 examples 之后再来看它，这样你能看出哪些抽象是从 examples 提升而来的。

## 建议阅读顺序
- 先看 [app/service.py](./app/service.py)：先看 `classify_node()`、`run_runtime()` 与 `evaluate()`。你要看到“单次运行”和“批量验证”是两个不同但相关的能力。
- 先看 [app/main.py](./app/main.py)：再看 `/run` 与 `/eval` 分别暴露什么。
- 先看 [tests/test_main.py](./tests/test_main.py)：最后看基线评测如何被自动验证。

## 建议运行命令
- `uvicorn app.main:app --reload`
- `pytest`

## 学完后你应该能回答
- 这个服务如何把 `04 Workflow、Observability 与 Evals` 的核心概念组合到一起。
- 为什么这些能力要按当前这种分层组织。
- 如果继续扩展，这个服务最先该从哪里演进。
