# starter-workspace

把环境、检查项和学习准备状态组织成统一工程骨架。

## 这个综合服务在模块里的位置
它不是一个额外 demo，而是这个模块知识点的收束点。你应该在跑完 examples 之后再来看它，这样你能看出哪些抽象是从 examples 提升而来的。

## 建议阅读顺序
- 先看 [app/service.py](./app/service.py)：先看 `WorkspaceStatus` 和 `summarize_workspace`，这是课程里“先建结构”的最小缩影。
- 先看 [app/main.py](./app/main.py)：再看 FastAPI 路由，理解为什么连“学习准备状态”也值得被建成服务边界。
- 先看 [tests/test_main.py](./tests/test_main.py)：最后看测试，确认“准备完成”的定义是可以验证的。

## 建议运行命令
- `uvicorn app.main:app --reload`
- `pytest`

## 学完后你应该能回答
- 这个服务如何把 `00 总览与准备` 的核心概念组合到一起。
- 为什么这些能力要按当前这种分层组织。
- 如果继续扩展，这个服务最先该从哪里演进。
