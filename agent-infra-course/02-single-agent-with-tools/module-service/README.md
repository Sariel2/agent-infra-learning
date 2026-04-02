# support-agent

用统一 trace 结构把单 agent、三个工具和失败恢复组合成支持服务。

## 这个综合服务在模块里的位置
它不是一个额外 demo，而是这个模块知识点的收束点。你应该在跑完 examples 之后再来看它，这样你能看出哪些抽象是从 examples 提升而来的。

## 建议阅读顺序
- 先看 [app/service.py](./app/service.py)：先看工具函数，再看 `ToolTrace` 和 `run_agent`。理解为什么 trace 结构必须统一。
- 先看 [app/main.py](./app/main.py)：再看 `/run` 路由如何只承担协议职责。
- 先看 [tests/test_main.py](./tests/test_main.py)：最后看服务级测试如何验证工具选择路径。

## 建议运行命令
- `uvicorn app.main:app --reload`
- `pytest`

## 学完后你应该能回答
- 这个服务如何把 `02 单 Agent 与 Tools` 的核心概念组合到一起。
- 为什么这些能力要按当前这种分层组织。
- 如果继续扩展，这个服务最先该从哪里演进。
