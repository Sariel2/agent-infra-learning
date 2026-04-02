# 02 单 Agent 与 Tools 逐步执行说明

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

## Step 3：学习 example `01-tool-schema`
- 先读 [examples/01-tool-schema/README.md](./examples/01-tool-schema/README.md)
- 再读 [examples/01-tool-schema/walkthrough.md](./examples/01-tool-schema/walkthrough.md)
- 打开 [examples/01-tool-schema/app/main.py](./examples/01-tool-schema/app/main.py)：先看 `ToolCall` 与 `ToolResult`。这两个对象定义了模型与工具之间的协议。再看 `search_docs`，理解工具本身应该尽量简单、可预测。
- 打开 [examples/01-tool-schema/tests/test_main.py](./examples/01-tool-schema/tests/test_main.py)：看参数错误如何在进入工具逻辑前就被拦住。
- 建议命令：
  - `python -m app.main`
  - `pytest`
- 完成标准：你至少做 1 处小改动，并能解释行为变化。

## Step 4：学习 example `02-agent-loop`
- 先读 [examples/02-agent-loop/README.md](./examples/02-agent-loop/README.md)
- 再读 [examples/02-agent-loop/walkthrough.md](./examples/02-agent-loop/walkthrough.md)
- 打开 [examples/02-agent-loop/app/main.py](./examples/02-agent-loop/app/main.py)：先看 `choose_tool`，再看 `run_agent`。这里最重要的是看清“决策点”和“执行点”的分离。
- 打开 [examples/02-agent-loop/tests/test_main.py](./examples/02-agent-loop/tests/test_main.py)：看同一个 loop 如何被固定输入稳定验证。
- 建议命令：
  - `python -m app.main`
  - `pytest`
- 完成标准：你至少做 1 处小改动，并能解释行为变化。

## Step 5：进入综合服务 `support-agent`
- 先读 [module-service/README.md](./module-service/README.md)
- 打开 [module-service/app/service.py](./module-service/app/service.py)：先看工具函数，再看 `ToolTrace` 和 `run_agent`。理解为什么 trace 结构必须统一。
- 打开 [module-service/app/main.py](./module-service/app/main.py)：再看 `/run` 路由如何只承担协议职责。
- 打开 [module-service/tests/test_main.py](./module-service/tests/test_main.py)：最后看服务级测试如何验证工具选择路径。
- 建议命令：
  - `uvicorn app.main:app --reload`
  - `pytest`
- 完成标准：你能解释这个综合服务如何把本模块知识点串起来。

## Step 6：练习与复盘
- 做 [exercises.md](./exercises.md)
- 用 [review.md](./review.md) 做复盘
- 完成标准：至少写下 1 条失败案例、1 条修复思路、1 条你现在能讲清楚的判断原则。
