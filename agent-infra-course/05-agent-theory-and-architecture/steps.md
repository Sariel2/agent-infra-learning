# 05 Agent 原理与架构 逐步执行说明

下面的步骤不是抽象提醒，而是本模块真正的学习顺序。每一步都对应具体讲义文件、代码文件和命令。

## Step 1：先建立概念框架
- 先读 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 再读 [resources/05-common-mistakes.md](./resources/05-common-mistakes.md)
- 目标：先知道这个模块解决什么问题、边界在哪里、最容易错在哪里。
- 完成标准：你能不用看代码先讲清这个模块的核心概念。

## Step 2：读细节和原理
- 读 [resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 参考 [resources/04-sources.md](./resources/04-sources.md) 中的出处链接，但不要跳出去替代教程本身
- 目标：弄清楚这个模块背后的数据流、设计动机和失败模式。
- 完成标准：你能解释“为什么要这样设计”，而不只是“我会用”。

## Step 3：学习 example `01-pattern-comparison`
- 先读 [examples/01-pattern-comparison/README.md](./examples/01-pattern-comparison/README.md)
- 再读 [examples/01-pattern-comparison/walkthrough.md](./examples/01-pattern-comparison/walkthrough.md)
- 打开 [examples/01-pattern-comparison/app/main.py](./examples/01-pattern-comparison/app/main.py)：先看 `PatternOutput`，再看 `compare_patterns()`。重点不是实现复杂，而是对比不同 pattern 的控制流差异。
- 打开 [examples/01-pattern-comparison/tests/test_main.py](./examples/01-pattern-comparison/tests/test_main.py)：看测试如何把 pattern 对比变成稳定输出。
- 建议命令：
  - `python -m app.main`
  - `pytest`
- 完成标准：你至少做 1 处小改动，并能解释行为变化。

## Step 4：学习 example `02-boundary-checker`
- 先读 [examples/02-boundary-checker/README.md](./examples/02-boundary-checker/README.md)
- 再读 [examples/02-boundary-checker/walkthrough.md](./examples/02-boundary-checker/walkthrough.md)
- 打开 [examples/02-boundary-checker/app/main.py](./examples/02-boundary-checker/app/main.py)：先看 `Scenario`，再看 `recommend_architecture()`。它在训练你的不是算法，而是判断维度。
- 打开 [examples/02-boundary-checker/tests/test_main.py](./examples/02-boundary-checker/tests/test_main.py)：看固定场景如何导出稳定建议。
- 建议命令：
  - `python -m app.main`
  - `pytest`
- 完成标准：你至少做 1 处小改动，并能解释行为变化。

## Step 5：进入综合服务 `architecture-lab`
- 先读 [module-service/README.md](./module-service/README.md)
- 打开 [module-service/app/service.py](./module-service/app/service.py)：先看 `compare()` 和 `recommend()`，理解“模式对比”和“场景判断”是两个互补维度。
- 打开 [module-service/app/main.py](./module-service/app/main.py)：再看如何用不同接口暴露它们。
- 打开 [module-service/tests/test_main.py](./module-service/tests/test_main.py)：最后看最小自动验证如何保护判断逻辑。
- 建议命令：
  - `uvicorn app.main:app --reload`
  - `pytest`
- 完成标准：你能解释这个综合服务如何把本模块知识点串起来。

## Step 6：练习与复盘
- 做 [exercises.md](./exercises.md)
- 用 [review.md](./review.md) 做复盘
- 完成标准：至少写下 1 条失败案例、1 条修复思路、1 条你现在能讲清楚的判断原则。
