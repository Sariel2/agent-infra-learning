# 状态驱动 workflow 代码导读

这个 example 的核心目的：为什么固定步骤、高风险节点更适合 workflow 而不是自由 agent。

## 阅读顺序
- 先看 [app/main.py](./app/main.py)：先看 `WorkflowState`，再看 `run_workflow()`。重点是理解“状态决定分支”而不是“模型随意跳转”。
- 先看 [tests/test_main.py](./tests/test_main.py)：看测试如何验证 refund 场景必须进入人工审核节点。

## 建议运行命令
- `python -m app.main`
- `pytest`

## 建议实验
- 增加一种新意图，设计一个新分支。

## 学完后你应该能回答
- 这个 example 为什么存在，它在整个模块里对应哪个关键知识点。
- 如果把这个 example 的抽象迁移到 `agent-runtime`，会迁移到哪一层。
