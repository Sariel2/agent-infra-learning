# 00 总览与准备 逐步执行说明

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

## Step 3：学习 example `01-settings-and-logging`
- 先读 [examples/01-settings-and-logging/README.md](./examples/01-settings-and-logging/README.md)
- 再读 [examples/01-settings-and-logging/walkthrough.md](./examples/01-settings-and-logging/walkthrough.md)
- 打开 [examples/01-settings-and-logging/app/main.py](./examples/01-settings-and-logging/app/main.py)：先看 `Settings` 和 `build_log_context`，理解“先固定系统形状，再讨论复杂能力”。
- 打开 [examples/01-settings-and-logging/tests/test_main.py](./examples/01-settings-and-logging/tests/test_main.py)：再看测试，观察课程如何把抽象对象转成可验证行为。
- 建议命令：
  - `python -m app.main`
  - `pytest`
- 完成标准：你至少做 1 处小改动，并能解释行为变化。

## Step 4：学习 example `02-project-smoke-test`
- 先读 [examples/02-project-smoke-test/README.md](./examples/02-project-smoke-test/README.md)
- 再读 [examples/02-project-smoke-test/walkthrough.md](./examples/02-project-smoke-test/walkthrough.md)
- 打开 [examples/02-project-smoke-test/app/main.py](./examples/02-project-smoke-test/app/main.py)：看 `ProjectStatus` 与 `summarize_status`，理解“能运行”和“已准备好”不是一回事。
- 打开 [examples/02-project-smoke-test/tests/test_main.py](./examples/02-project-smoke-test/tests/test_main.py)：看 smoke test 如何把学习状态转成明确检查项。
- 建议命令：
  - `python -m app.main`
  - `pytest`
- 完成标准：你至少做 1 处小改动，并能解释行为变化。

## Step 5：进入综合服务 `starter-workspace`
- 先读 [module-service/README.md](./module-service/README.md)
- 打开 [module-service/app/service.py](./module-service/app/service.py)：先看 `WorkspaceStatus` 和 `summarize_workspace`，这是课程里“先建结构”的最小缩影。
- 打开 [module-service/app/main.py](./module-service/app/main.py)：再看 FastAPI 路由，理解为什么连“学习准备状态”也值得被建成服务边界。
- 打开 [module-service/tests/test_main.py](./module-service/tests/test_main.py)：最后看测试，确认“准备完成”的定义是可以验证的。
- 建议命令：
  - `uvicorn app.main:app --reload`
  - `pytest`
- 完成标准：你能解释这个综合服务如何把本模块知识点串起来。

## Step 6：练习与复盘
- 做 [exercises.md](./exercises.md)
- 用 [review.md](./review.md) 做复盘
- 完成标准：至少写下 1 条失败案例、1 条修复思路、1 条你现在能讲清楚的判断原则。
