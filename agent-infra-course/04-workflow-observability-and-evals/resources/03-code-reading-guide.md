# 04 Workflow、Observability 与 Evals 代码导读

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：02-deep-dive.md](./02-deep-dive.md) | [下一篇：04-sources.md](./04-sources.md)

## 学习总原则
- 先看讲义，再看代码。
- 先看对象模型和函数签名，再看具体执行逻辑。
- 先跑测试，再改代码，再重新验证。

## Examples 阅读顺序
### 01-stateful-workflow：状态驱动 workflow
- 这一例子主要解决：为什么固定步骤、高风险节点更适合 workflow 而不是自由 agent。
- 先看 [`01-stateful-workflow/app/main.py`](../examples/01-stateful-workflow/app/main.py)：先看 `WorkflowState`，再看 `run_workflow()`。重点是理解“状态决定分支”而不是“模型随意跳转”。
- 先看 [`01-stateful-workflow/tests/test_main.py`](../examples/01-stateful-workflow/tests/test_main.py)：看测试如何验证 refund 场景必须进入人工审核节点。
- 建议运行命令：
  - `python -m app.main`
  - `pytest`
- 建议动手实验：
  - 增加一种新意图，设计一个新分支。

### 02-eval-runner：固定数据集评测
- 这一例子主要解决：为什么没有基线数据集，就无法做稳定迭代。
- 先看 [`02-eval-runner/app/main.py`](../examples/02-eval-runner/app/main.py)：先看 `DATASET`、`choose_tool()` 和 `run_eval()`。重点不是复杂评分，而是“固定样本 + 稳定比较”。
- 先看 [`02-eval-runner/tests/test_main.py`](../examples/02-eval-runner/tests/test_main.py)：看测试如何把评测逻辑也纳入可验证范围。
- 建议运行命令：
  - `python -m app.main`
  - `pytest`
- 建议动手实验：
  - 故意改坏 `choose_tool()`，看 eval 如何暴露退化。

## module-service 阅读顺序
### agent-runtime
- 这个综合服务的目的：把 workflow、trace 和 eval 统一进同一个运行时服务。
- 先看 [`module-service/app/service.py`](../module-service/app/service.py)：先看 `classify_node()`、`run_runtime()` 与 `evaluate()`。你要看到“单次运行”和“批量验证”是两个不同但相关的能力。
- 先看 [`module-service/app/main.py`](../module-service/app/main.py)：再看 `/run` 与 `/eval` 分别暴露什么。
- 先看 [`module-service/tests/test_main.py`](../module-service/tests/test_main.py)：最后看基线评测如何被自动验证。
- 建议运行命令：
  - `uvicorn app.main:app --reload`
  - `pytest`
